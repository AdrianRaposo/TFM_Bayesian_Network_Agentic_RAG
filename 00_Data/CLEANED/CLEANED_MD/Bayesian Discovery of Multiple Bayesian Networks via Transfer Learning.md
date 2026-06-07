# Bayesian Discovery of Multiple Bayesian Networks via Transfer Learning 

Diane Oyen<br>University of New Mexico<br>doyen@cs.unm.edu

Terran Lane<br>Google, Inc<br>terran.lane@gmail.com


#### Abstract

Bayesian network structure learning algorithms with limited data are being used in domains such as systems biology and neuroscience to gain insight into the underlying processes that produce observed data. Learning reliable networks from limited data is difficult, therefore transfer learning can improve the robustness of learned networks by leveraging data from related tasks. Existing transfer learning algorithms for Bayesian network structure learning give a single maximum a posteriori estimate of network models. Yet, many other models may be equally likely, and so a more informative result is provided by Bayesian structure discovery. Bayesian structure discovery algorithms estimate posterior probabilities of structural features, such as edges. We present transfer learning for Bayesian structure discovery which allows us to explore the shared and unique structural features among related tasks. Efficient computation requires that our transfer learning objective factors into local calculations, which we prove is given by a broad class of transfer biases. Theoretically, we show the efficiency of our approach. Empirically, we show that compared to single task learning, transfer learning is better able to positively identify true edges. We apply the method to whole-brain neuroimaging data.


## I. INTRODUCTION

The discovery of structural features in Bayesian networks is of great interest in scientific domains such as bioinformatics and neuroscience. The goal is to understand the relationships among variables in a system, such as genes in a gene expression network or activity levels of regions of the brain in functional brain networks. However, the data collected is often done in several separate but related experiments. Therefore, the full data set is actually composed of several distinct, but related, subsets of data - called tasks in transfer learning. For each task there may not be enough samples to learn a robust model. Transfer learning leverages information among tasks to smooth learned models [1], [2]. These smoothed models tend to be more robust to sample noise and generalize to holdout data better than models learned without transfer. Furthermore, in unsupervised learning, the set of models learned among tasks will share many features in common, easing interpretation of the models. Differences among the learned task-specific models are more likely to be due to real differences in the generating distribution of the data rather than spurious differences [3], [4].

Existing transfer Bayesian network learning algorithms have two major limitations: 1) they use heuristic search over the space of sets of graphs; and 2) produce a single point maximum a posteriori model. Yet, there may be many other solutions of similar likelihood and therefore a point solution will not give a full picture of likely relationships among
variables. A point solution can perform well at predicting future data, but it is misleading to present such a solution to the domain expert as the only model that explains the data. Instead, we would like to learn a posterior distribution over solutions and extract meaningful summary statistics about features of interest. Such algorithms exist for learning individual Bayesian networks and are referred to as network discovery [5], [6]. Extending these algorithms for transfer network learning is not trivial, as we explain in the next paragraph.

Algorithms for estimating the posterior probability distribution for a single network generally fall into two categories: those that search over structure space and those that search over order space. Structure-space algorithms make small local changes to the learned graph structure (typically, the addition, removal or reversal of a single edge). For these small changes, updating the likelihood of the graph, and therefore the posterior distribution, is fast but covering the full space of structures can be slow and can get stuck in local maxima [7], [8]. Extending those structure-search algorithms to multiple tasks would explode the model search space exponentially, exacerbating convergence issues. On the other hand, order-search algorithms exploit the tractability of calculating posteriors given a fixed ordering of the variables (described in more detail later). Node order dictates which nodes are allowed to be parents to any given node, and therefore changes in node order are more global than structure-space changes. There are relatively efficient algorithms for calculating exact posteriors of structural features [6], [9] or approximate posteriors [5], [10] that have been shown to be faster than structure-search. However, there is no structural prior provided in these orderspace formulations; instead there is a prior over orders. We do not want to impose transfer at the level of orders, but rather at the level of structures (a particular edge appearing in one task will be preferred in other tasks).

Our main challenge, therefore, is to incorporate a structural bias term into the order-search formulation. With such a bias term, we can impose a transfer bias to learn more robust networks, while leveraging the most efficient Bayesian discovery algorithms that currently exist. Our major contribution is proving that structural bias can be efficiently incorporated into the order-conditioned network discovery formulation. We prove that our transfer formulation factors into local calculations. Thus, we provide the first transfer algorithm that can calculate exact posteriors for multiple networks of moderate size. We are also the first to show how transfer can incorporated into state-of-the-art order-search approximation algorithms for larger networks.

Our contribution is a proof that structure bias can be efficiently incorporated into order-conditioned Bayesian structure discovery: a necessary requirement for using the efficient algorithms of network discovery [5], [6]. This is a finding that can impact many structure discovery problems. We give a specific formulation of multitask Bayesian network discovery that uses the structure bias to transfer information among tasks. We further show that we can take a Bayesian approach to average over all possible settings of the transfer parameter rather than needing to select this parameter. Empirical results on networks, of size 8 variables and 37 variables, indicate that our transfer approach learns posterior probabilities that are closer to the optimal values than single-task learning algorithms. We apply our multitask algorithm to neuroimaging data with 150 variables and demonstrate that the multitask algorithm produces fewer spurious edges than the non-multitask algorithm while providing more knowledge discovery information than the standard point solution.

## II. Related Work

Network structure discovery in the face of limited data is an extensively studied problem. With limited data, the posterior probability of even the optimal network may be quite small, however Friedman and Koller (2003) show that the marginal posterior probabilities over subgraphs or structural features can be quite high given the same data [5]. They propose the so-called order-MCMC algorithm for estimating such posterior probabilities. Koivisto and Sood (2004) give a dynamic programming method for calculating exact posterior probabilities of network features conditioned on orders [6]. Further improvements are made to make the approach more memory efficient [9] and to produce partial-order MCMC [10]. We show how to extend these single-task learning approaches to the transfer learning problem.

Transfer and multitask learning leverage information among related problems called tasks [1], [2]. Formulations for multitask learning of Bayesian networks exist [3], [11]. Starting from these, we derive an inductive bias toward similar structures among related tasks. However, the solutions to the multitask problems in these papers are found through heuristic search, producing a point estimate rather than a posterior distribution, which we desire. They also require a parameter that determines the strength of transfer bias.

Another approach to learning Bayesian networks from limited data uses the concept of network discovery with a prior over structures obtained from domain knowledge [8], [12]. However, these approaches resort to using MCMC in structure space (rather than order space) to avoid the difficulties in assigning priors conditioned on orders. Furthermore, they do not solve the problem considered here of multiask learning.

## III. Preliminaries

First, we introduce background information about Bayesian structure discovery for learning a single task and then describe MAP multitask Bayesian network objectives. We combine ideas from both of these approaches to produce Bayesian structure discovery of multitask Bayesian networks.

Bayesian networks compactly describe joint probability distributions by encoding conditional independencies in multivariate data. A Bayesian network $B=\{G, \theta\}$ describes the joint probability distribution over $n$ random variables $\mathbf{X}=$ $\left[X_{1}, X_{2}, \ldots, X_{n}\right]$, where $G$ is a directed acyclic graph (DAG) and the conditional probability distributions are parameterized by $\theta$ [13]. An edge $\left(X_{i}, X_{j}\right)$ in $G$ means that the child $X_{j}$ is conditionally independent of all non-descendants given its parent $X_{i}$. The structure of the network, $G$, is of particular interest in many domains as it is easy to interpret and gives valuable information about the interaction of variables.

## A. Structural Feature Discovery

Given a limited amount of data, the posterior probability of any network may be quite small. However, summary statistics regarding structural features of networks may have high posterior even with limited data [5]. Structural features (such as an edge) can be described by an indicator function $f$ such that for $f(G)=1$ the feature exists in graph $G$, otherwise $f(G)=0$. The posterior probability of the feature is equivalent to the expectation of its indicator, $P(f \mid D)=\sum_{G} P(G \mid D) f(G)$. However, this sum can be intractable, as the number of DAGs is super-exponential in the number of variables.

An important insight to making this sum tractable is that we could fix the order of the variables. An order, $\prec$, is a permutation on the indices of the variables $X_{\prec(1)}, X_{\prec(2)}, \ldots, X_{\prec(n)}$ such that parents must precede children in the order, i.e. $X_{j}$ cannot be a parent of $X_{i}$ if $\prec(j) \geq \prec(i)$. Given an order, learning optimal parents for each child factors into local calculations, and summing over DAGs consistent with the order is tractable [14], [15]. [5] condition on a node order, and then obtain the unconditional posterior by summing over orders:

$$
P(f \mid D)=\frac{1}{P(D)} \sum_{\prec} P(\prec) \sum_{G \searrow \prec} P(D \mid G) P(G \mid \prec) f(G)
$$

Note that these two formulations for $P(f \mid D)$ are not the same, as most DAGs, $G$, will be consistent with multiple orders, $\prec$. Typically, this formulation produces an acceptable bias in favor of simpler structures.
[6] give an efficient method for calculating this sum. The approach is rather involved, so we summarize only the key points here. They make several reasonable assumptions, then break the calculation into three steps. First, we describe the modularity assumptions:

1) Parameter modularity: Modularity of the Bayesian network parameters must also hold, $P(\theta \mid G)=\prod_{i=1}^{n} P\left(\theta_{i, \pi_{i}} \mid \pi_{i}\right)$ and $P(X=x \mid G)=\prod_{i=1}^{n} P\left(x_{i} \mid x_{\pi_{i}}, \theta_{i, \pi_{i}}\right)$.
2) Structure prior modularity: The network model prior must be modular so that $P(G, \prec)=$ $c \prod_{i=1}^{n} P\left(U_{i}\right) P\left(\pi\left(X_{i}\right)\right)$, where $U_{i}$ is the set of variables preceding $X_{i}$ in the order $\prec$ (potential parents of $X_{i}$ ) and $c$ is a normalization constant.
3) Feature modularity: The features must be modular, $f(G)=\prod_{i=1}^{n} f_{i}\left(\pi\left(X_{i}\right)\right)$ where $\pi\left(X_{i}\right)$ is the parent set of variable $i$.

The most common feature to look for is a directed edge $u \rightarrow v$ s.t. $f=1$ if $X_{u} \in \pi_{v}$, which is clearly modular. If these modularity assumptions hold, then the likelihood over

order space factors into local calculations as shown in Eq 1 [6].

$$
\begin{aligned}
P(f, D \mid \prec) & =\prod_{i=1}^{n} \sum_{\pi_{i} \subseteq U_{i}} P\left(\pi_{i} \mid U_{i}\right) P\left(x_{i} \mid \pi_{i}\right) f_{i}\left(\pi_{i}\right) \\
P(f \mid D) & =\frac{1}{P(D)} \sum_{\prec} P(\prec) P(f, D \mid \prec)
\end{aligned}
$$

where $\pi_{i}=\pi\left(X_{i}\right)$ is the parent set of variable $i$. The unconditional posterior for the features is obtained by summing over orders, using the following steps:

1) Calculate family scores: $\beta_{i}\left(\pi_{i}\right)=$ $P\left(\pi_{i}\right) P\left(x_{i} \mid \pi_{i}\right) f_{i}\left(\pi_{i}\right)$ for each node $i$ and potential set of parents $\pi_{i}$. The computational complexity of each of these is some function $C(m)$ of the number of samples $m$. The maximum number of parents allowed for any node is typically fixed to a small natural number, $r$. Therefore, there are $O\left(N^{r+1}\right)$ of these functions to calculate for a total complexity of $O\left(N^{r+1} C(m)\right)$.
2) Calculate local contribution of each subset $U \subseteq$ $V-\{i\}$ of potential parents of $i: \alpha_{i}(U)=$ $\sum_{\pi_{i} \subseteq U} P\left(\pi_{i}\right) P\left(x_{i} \mid \pi_{i}\right) f_{i}\left(\pi_{i}\right)$. Using a truncated fast Möbius transform and pre-computed $\beta$ 's, all of the $\alpha$ functions are computed in $O\left(n 2^{n}\right)$ time.
3) Sum over the subset lattice of the various $U_{i}$ to obtain the sum over orders $\prec$. Using dynamic programming, this sum takes time $O\left(n 2^{n}\right)$.

The total computational complexity for a single task is $O\left(n 2^{n}+n^{r+1} C(m)\right)$. This is the exact calculation of the posterior. For large networks, roughly $n>30$, the exponential term is intractible. In these cases, MCMC simulations give an approximation to the posterior probability, so that $P(f \mid D) \approx$ $\frac{1}{N} \sum_{t=1}^{T} P\left(\prec_{t}\right) P\left(f \mid D, \prec_{t}\right)$ for $\prec_{t}$ sampled from order space [5] or partial orders [10].

## B. Multitask Bayesian Networks

Multitask Bayesian network learning leverages knowledge among a set of related tasks by applying a bias toward learning similar networks among the tasks. The underlying assumption is that much of the network is shared among tasks, yet a few differences may exist. By leveraging information among tasks, we can learn more robust networks than would be possible from a single small sample [3]. We will apply a similar bias mechanism for network discovery. First we describe the objective function of existing MAP estimate algorithms, which has been shown to be effective at leveraging information. A set of tasks with data sets $D^{(k)}$ and networks $G^{(k)}$ for $k \in\{1, \ldots, K\}$ can be learned by optimizing:

$$
\begin{aligned}
& P(\mathcal{G} \mid \mathcal{D})=P\left(G^{(1)}, \ldots, G^{(K)} \mid D^{(1)}, \ldots, D^{(K)}\right)= \\
& P\left(D^{(1)}, \ldots, D^{(K)} \mid G^{(1)}, \ldots, G^{(K)}\right) \frac{P(\mathcal{G})}{P(\mathcal{D})}
\end{aligned}
$$

In existing multitask network learning formulations, the joint structure prior, $P(\mathcal{G})$, is used to encode a bias toward similar structures by penalizing differences in network structure among tasks [3], [11]. We can assume that $P\left(D^{(k)} \mid G^{(k)}\right)$ is independent of all other $G^{(i)}$ so Eq 2 simplifies and the joint prior over structures can be described by pairwise sharing of information among tasks as in Eq 3.

$$
\begin{aligned}
& P_{M T L}(\mathcal{G} \mid \mathcal{D}, \lambda)=\frac{P(\mathcal{G} \mid \lambda)}{P(\mathcal{D})} \prod_{k=1}^{K} P\left(D^{(k)} \mid G^{(k)}\right) \\
& P(\mathcal{G} \mid \lambda)=\frac{1}{Z} \prod_{k=1}^{K} P\left(G^{(k)}\right) \prod_{i=1}^{k-1} \lambda(1-\lambda)^{\Delta\left(G^{(k)}, G^{(i)}\right)}
\end{aligned}
$$

where $Z$ is a normalization constant and $\Delta$ is any graph distance metric, such as edit distance, that measures the number of structural differences between graphs $G^{(k)}$ and $G^{(i)}$.

## IV. Multitask Feature Discovery

In this section, we present our novel Bayesian approach to structure discovery in multitask Bayesian networks. The challenge is finding a way to bias structures to be similar among tasks, like Eq 3, while maintaining the efficiency of calculating feature posteriors that factor into local calculations, like Eq 1. First we formulate the problem, describe structural bias terms that are order-modular, provide a Bayesian approach for handling the strength of the bias, and finally describe practical implementation issues.

## A. Problem Formulation

Instead of learning the feature posteriors from a single task-specific data set, we have $K$ tasks from which we will leverage data. We define the indicator $f^{(k)}=f\left(G^{(k)}\right)$. Our goal is to learn a feature for each task $P\left(f^{(k)} \mid D^{(1)}, \ldots, D^{(K)}\right)$ $\forall k \in\{1, \ldots, K\}$. Again, all formulations are written for a single feature (e.g. a directed edge), but calculating them simultaneously (e.g. all edges in a network) takes the same time. To simplify the development of the objective, we will consider, without loss of generality, the case where $K=2$.

$$
\begin{aligned}
& P\left(f^{(1)} \mid D^{(1)}, D^{(2)}\right)= \\
& \quad=\sum_{\prec} P\left(\prec\right) \sum_{G^{(1)} \subseteq \prec} P\left(G^{(1)} \mid D^{(1)}, D^{(2)}\right) f\left(G^{(1)}\right) \\
& \quad=\sum_{\prec} \sum_{G^{(1)} \subseteq \prec} f\left(G^{(1)}\right) \times\left[\sum_{G^{(2)} \subseteq \prec} P\left(G^{(1)}, G^{(2)} \mid D^{(1)}, D^{(2)}\right)\right] \\
& \quad=\frac{1}{P\left(D^{(1)}, D^{(2)}\right)} \sum_{\prec} \sum_{G^{(1)} \subseteq \prec} f\left(G^{(1)}\right) P\left(D^{(1)} \mid G^{(1)}\right) \times \\
& \quad\left[\sum_{G^{(2)} \subseteq \prec} P\left(D^{(2)} \mid G^{(2)}\right) P\left(G^{(1)}, G^{(2)}\right)\right]
\end{aligned}
$$

For the purpose of calculating the transfer bias, we impose the same order, $\prec$, on both tasks, and then marginalize over orders. This restriction makes computation more efficient, and it seems reasonable to bias a feature contingent on a particular ordering toward the evidence from other tasks while they are restricted to the same set of possible graph structures. Rewriting Eq 4 as a joint probability conditioned on an order,

we get the following:

$$
\begin{aligned}
P\left(f^{(1)}, D^{(1)}, D^{(2)} \mid \prec\right)=\sum_{G^{(1)} \subseteq \prec} & f\left(G^{(1)}\right) P\left(D^{(1)} \mid G^{(1)}\right) \times \\
& {\left[\sum_{G^{(2)} \subseteq \prec} P\left(D^{(2)} \mid G^{(2)}\right) P\left(G^{(1)}, G^{(2)} \mid \prec\right)\right]}
\end{aligned}
$$

Our formulation imposes a transfer bias at the level of structure, $P\left(G^{(1)}, G^{(2)} \mid \prec\right)$, which is more intuitive than at the level of orders. To calculate this sum efficiently, it is necessary to factor it into a product over local sums. We prove that this is indeed possible, for appropriately chosen structure priors. In addition to the modularity assumptions already stated, we impose an additional modularity assumption, which we call Assumption 4) Transfer prior modularity: $P\left(G^{(1)}, G^{(2)} \mid \prec\right)=\prod_{i=1}^{n} P\left(\pi_{i}^{(1)}, \pi_{i}^{(2)} \mid U_{i}\right)$. Examples of priors that obey this assumption are graph distance measures that count the number of edge additions and deletions, so this is a reasonable requirement.
Theorem 1. If $G^{(1)}, \ldots, G^{(K)}$ obey the four assumptions of modularity, then

$$
\begin{gathered}
P\left(f^{(1)}, \mathcal{D} \mid \prec\right)=\prod_{i \in V} \sum_{\pi_{i}^{(1)} \subseteq U_{i}} f_{i}\left(\pi_{i}^{(1)}\right) P\left(x_{i}^{(1)} \mid \pi_{i}^{(1)}\right) \times \\
{\left[\sum_{\pi_{i}^{(2)} \subseteq U_{i}} P\left(x_{i}^{(2)} \mid \pi_{i}^{(2)}\right) P\left(\pi_{i}^{(1)}, \pi_{i}^{(2)} \mid U_{i}\right)\right]}
\end{gathered}
$$

Proof Sketch: Apply the chain rule and marginalize over graph structure to get Eq 5. Use the modularity properties on each term in the product, and notice that the result factors into the desired form.

$$
\begin{aligned}
& P\left(f^{(1)}, \mathcal{D} \mid \prec\right)=\sum_{G^{(1)} \subseteq \prec} f\left(G^{(1)}\right) P\left(D^{(1)} \mid G^{(1)}\right) \times \\
& {\left[\sum_{G^{(2)} \subseteq \prec} P\left(D^{(2)} \mid G^{(2)}\right) P\left(G^{(1)}, G^{(2)} \mid \prec\right)\right] } \\
& =\sum_{\pi_{i}^{(1)} \subseteq U_{i}} \cdots \sum_{\pi_{n}^{(1)} \subseteq U_{n}} \prod_{i=1}^{n}\left[f_{i}\left(\pi_{i}^{(1)}\right) P\left(x_{i}^{(1)} \mid \pi_{i}^{(1)}\right)\right] \times \\
& {\left[\sum_{\pi_{1}^{(2)} \subseteq U_{1}} \cdots \sum_{\pi_{n}^{(2)} \subseteq U_{n}} \prod_{i=1}^{n} P\left(x_{i}^{(2)} \mid \pi_{i}^{(2)}\right) P\left(\pi_{i}^{(1)}, \pi_{i}^{(2)} \mid U_{i}\right)\right]}
\end{aligned}
$$

The details of the proof are straightforward, yet space consuming, and so are omitted. See [6] for a similar proof.

## B. Computational Complexity

The power of Theorem 1 is the computational savings that we gain. Using the factored posterior, we only need to change Step 1 of the order-space algorithm outlined in Section III-A, the calculation of the family scores. The transfer-biased family
scores are calculated as:

$$
\begin{aligned}
\beta_{k i}\left(\pi_{i}\right) & =f_{i}\left(\pi_{i}^{(k)}\right) P\left(x_{i}^{(k)} \mid \pi_{i}^{(k)}\right) P\left(\pi_{i}^{(k)}, \pi_{i}^{(j)}\right) \\
& =f_{i}\left(\pi_{i}^{(k)}\right) P\left(x_{i}^{(k)} \mid \pi_{i}^{(k)}\right) \times \\
& {\left[\sum_{j \neq k} \sum_{\pi_{i}^{(j)} \subseteq U_{i}} P\left(x_{i}^{(j)} \mid \pi_{i}^{(j)}\right) P\left(\pi_{i}^{(k)}, \pi_{i}^{(j)}\right)\right]}
\end{aligned}
$$

There are now $K n^{r+1}$ of these families to calculate and each one has a sum over $O\left(K n^{r}\right)$ terms. The computational complexity increases from the single-task time of $O\left(n^{r+1} C(m)\right)$ to $O\left(K^{2} n^{2 r+1} C(m)\right)$. Steps 2 and 3 remain unchanged with an exponential complexity that can be reduced through MCMC approximation.

Even the polynomial term becomes unmanageable for networks with more than 30 or so nodes and must be approximated. We note that in many cases the family scores $P\left(x_{i}^{(j)} \mid \pi_{i}^{(j)}\right)$ are exponentially larger for some $\pi_{i}^{(j)} \subseteq U_{i}$ than others. Therefore, we can use a simple approximation by summing over only the most likely parent sets. While calculating the family scores, we create a set of the highestscoring families, called set $\mathcal{H}_{i}^{(k)}$ for each node in each task. To populate this set, we simply include $h$ parent sets that give the highest $P\left(x_{i}^{(k)} \mid \pi_{i}^{(k)}\right)$, for some constant $h$. Then we use the approximate structural prior:

$$
P_{i}\left(\pi_{i}^{(k)}\right) \approx \sum_{\pi_{i}^{(j)} \in \mathcal{H}_{i}^{(j)}} P\left(x_{i}^{(j)} \mid \pi_{i}^{(j)}\right) P\left(\pi_{i}^{(k)}, \pi_{i}^{(j)} \mid U_{i}\right)
$$

## C. Transfer via Structure Bias

Now that we know we can incorporate transfer bias, we need to select a modular bias term that transfers knowledge among tasks. The MAP multitask algorithms use a penalty on the number of differences between tasks using a graph distance function. In that case, the number of edges that must be added, deleted, or reversed to edit one graph into the other is penalized. Due to our modularity constraint, our transfer bias must be defined as a function on pairs of parent sets $\left(\pi_{i}^{(k)}, \pi_{i}^{(j)}\right)$, rather than graphs. We choose to penalize the number of edge additions which breaks down into local calculations: the number of parents present in $\pi_{i}^{(k)}$ that are not present in $\pi_{i}^{(j)}$. In other words, the size of the set difference $\Delta_{i k j}=\left|\pi_{i}^{(k)} \backslash \pi_{i}^{(j)}\right|$ will be biased toward small values. To encourage the number of differences to be small, we apply a penalty in the form of a geometric distribution,

$$
P\left(\pi_{i}^{(k)}, \pi_{i}^{(j)} \mid U_{i}, \lambda\right)=\frac{1}{Z}(1-\lambda)^{\Delta_{i k j}}
$$

Calculation of the normalization constant requires summing over an exponential number of possible combinations of parent sets $\left(\pi_{i}^{(k)}, \pi_{i}^{(j)}\right)$. However, we found show how to simplify the sum into an easy closed form. We employ a shortcut by noting that there are a finite number of values that $\Delta_{i k j}$ can take and we find a closed form for calculating the number of parent-set combinations that produce each value of $\Delta_{i k j}$.

$$
\begin{aligned}
Z & =\sum_{\pi_{i}^{(k)} \subseteq U_{i}} \sum_{\pi_{i}^{(j)} \subseteq U_{i}}(1-\lambda)^{\Delta_{i k j}} \\
& =(4-\lambda)\left|U_{i}\right|
\end{aligned}
$$

Here we give a sketch of the derivation of Eq 8. First, we simplify the inner sum by fixing parent set $\pi_{i}^{(1)}$ and counting how many parent sets $\pi_{i}^{(2)}$ will give $\Delta_{i k j}=0$ ($\pi_{i}^{(2)}$ can contain any parents from the set $\left\{U_{i} \backslash \pi_{i}^{(1)}\right\}$ but none from $\pi_{i}^{(1)}$ ); then how many $\pi_{i}^{(2)}$ will give $\Delta_{i k j}=1$ ( $\pi_{i}^{(2)}$ can contain any parents from the set $\left\{U_{i} \backslash \pi_{i}^{(1)}\right\}$ and exactly one from $\pi_{i}^{(1)}$ ); etc, up to the maximum of $\Delta_{i k j}=\left|\pi_{i}^{(1)}\right|$. This sum turns out to be a binomial expansion, and so we can write it in closed form. Next, we perform a similar expansion of the outer sum over parent sets $\pi_{i}^{(1)}$ that have size $\left|\pi_{i}^{(1)}\right|=0$, and $\left|\pi_{i}^{(1)}\right|=1$, etc up to the maximum $\left|\pi_{i}^{(1)}\right|=\left|U_{i}\right|$. This sum also turns out to be a binomial expansion and therefore can be simplified into a closed form. ${ }^{1}$

Plugging Eq 8 into Eq 7 gives the structure prior:

$$
P\left(\pi_{i}^{(k)}, \pi_{i}^{(j)} \mid U_{i}, \lambda\right)=\frac{(1-\lambda)^{\Delta_{i k j}}}{(4-\lambda)^{\left|U_{i}\right|}}
$$

The parameter $\lambda, 0 \leq \lambda \leq 1$, controls the strength of transfer bias. When $\lambda=0$, the prior becomes uniform and therefore there is no transfer. When $\lambda=1$, the prior is non-zero only when no edge additions occur, and therefore the only parents that are allowed are those that are likely in the other tasks.

## D. Bayesian Model Averaging

We have just introduced an additional parameter, $\lambda$, which is a bit of a nuisance. Existing MAP algorithms cannot avoid dealing with this, and they typically estimate $\lambda$ by optimizing over a held out validation set. This is computationally expensive and reduces the amount of available data for training. Rather than selecting a fixed value for $\lambda$, we perform Bayesian model averaging over all possible values of $\lambda$. This Bayesian approach is compelling as the true amount of similarity among tasks is unknown, and the "true" value of $\lambda$ is only incidental to our objective of learning the structure likelihoods. Furthermore, it saves us the computation of running the algorithm for several values of $\lambda$, and we do not need to hold-out data for tuning.

We set an uninformative uniform prior, $p\left(\lambda \mid U_{i}\right)=1$ for $0 \leq \lambda \leq 1$, and marginalize over $\lambda$.

$$
\begin{aligned}
P\left(\pi_{i}^{(k)}, \pi_{i}^{(j)} \mid U_{i}\right) & =\int_{0}^{1} P\left(\pi_{i}^{(k)}, \pi_{i}^{(j)} \mid U_{i}, \lambda\right) p\left(\lambda \mid U_{i}\right) d \lambda \\
& =\int_{0}^{1} \frac{(1-\lambda)^{\Delta_{i k j}}}{(4-\lambda)^{\left|U_{i}\right|} d \lambda} \\
& =\frac{{ }_{2} \mathrm{~F}_{1}\left(\left|U_{i}\right|, 1 ; \Delta_{i k j}+2 ; 1 / 4\right)}{4^{\left|U_{i}\right|}\left(\Delta_{i k j}+1\right)}
\end{aligned}
$$

where ${ }_{2} \mathrm{~F}_{1}$ is the ordinary hypergeometric function:

$$
\begin{aligned}
& { }_{2} \mathrm{~F}_{1}\left(\left|U_{i}\right|, 1 ; \Delta_{i k j}+2 ; 1 / 4\right)= \\
& \quad \sum_{n=0}^{\infty} \frac{\Gamma(1+n)}{\Gamma(1)} \cdot \frac{\Gamma\left(\left|U_{i}\right|+n\right)}{\Gamma\left(\left|U_{i}\right|\right)} \cdot \frac{\Gamma\left(\Delta_{i k j}+2\right)}{\Gamma\left(\Delta_{i k j}+2+n\right)} \cdot \frac{1}{4^{n} n!}
\end{aligned}
$$

The last step in Eq 10 is obtained by applying an identity given by Euler in 1748 [16]. If $\beta$ is the beta function and ${ }_{2} \mathrm{~F}_{1}$

[^0]![img-0.jpeg](img-0.jpeg)

Fig. 1: Posterior probability estimate for each edge in the asia network from various large sample sets (means calculated from 20 sample sets). Blue curves are true edges, green are reverse of a true edge, pink are non-edges. (Best viewed in color.)
is the ordinary hypergeometric function, then

$$
\begin{aligned}
\int_{0}^{1} x^{b-1}(1-x)^{c-b-1} & (1-z x)^{-a} d x= \\
& \beta(b, c-b)_{2} \mathrm{~F}_{1}(a, b ; c ; z)
\end{aligned}
$$

for $\Re(c)>\Re(b)>0$. We let $x=\lambda, a=\left|U_{i}\right|, b=1, c=$ $\Delta_{i k j}+2$, and $z=1 / 4$. Then the condition, $\Delta_{i k j}+2>1>0$, holds for any $\Delta_{i k j} \geq 0$ which is the valid range for $\Delta_{i k j}$. Plugging these values into the identity gives the solution to the integral as:

$$
\beta\left(1, \Delta_{i k j}+1\right)_{2} \mathrm{~F}_{1}\left(\left|U_{i}\right|, 1 ; \Delta_{i k j}+2 ; 1 / 4\right)
$$

which simplies to the solution given in Eq 10.
We are only interested in calculating ${ }_{2} \mathrm{~F}_{1}$ for combinations of integer-values of $\Delta_{i k j}$ and $\left|U_{i}\right|$ for $0 \leq \Delta_{i k j} \leq\left|U_{i}\right|<n$. For these values, ${ }_{2} \mathrm{~F}_{1}$ is convergent and efficient solvers exist. Thus, we can plug the result of Eq 10 into the equation of Theorem 1.

Bayesian model averaging is made possible by conditioning on orders. Existing multitask network learning algorithms that search in DAG space [3], [11] would be required to calculate a normalization constant like that in Eq 8 but with sums over all possible DAGs, and no closed form has been found for such a sum.

## V. EXPERIMENTS

Multitask learning should be able to identify true edges and non-edges with less data than is possible with traditional single-task learning. We compare our MTL structure discovery algorithm against two baselines. The first baseline is singletask learning (STL), where each network is learned independently of the other tasks. The other baseline (POOL) takes the opposite extreme by pooling data from all tasks together and treating it as a single task. POOL uses the strongest leveraging of data among tasks possible and so it should perform best if the separate tasks are actually the same distribution. For all approaches, we use the BeanDisco implementation for exact and approximate network discovery [10]. For MTL, the scoring function of BeanDisco is modified as described above. For POOL, the data are merged before applying the algorithm.


[^0]:    ${ }^{1}$ Algebraic details of this calculation are space consuming and can be supplied in an online supplement.

![img-1.jpeg](img-1.jpeg)

Fig. 2: Example posterior probability estimate for each edge in a modified *asia* network from various small sample sets (means calculated from 20 sample sets). Up is good for blue and cyan curves. Down is good for red and green curves.

### A. Benchmark Data

Synthetic data is generated from benchmark Bayesian networks, *asia* which has 8 variables [17] and *alarm* which has 37 variables [18]. Even when the generative model is known, it is not obvious how to measure the performance of a network discovery algorithm. To give a clear picture of our objective, see Figure 1. On the small *asia* network we can calculate the true posterior likelihoods of structural features given the data. Sample noise affects the true posterior likelihood of structural features but the posteriors appear to stabilize for large training sets. Even so, one edge has been consistently identified in the reverse direction of the true edge and another true edge represents such a subtle dependency that it is not discernible from this amount of data. Therefore, we use the posterior estimates from large training sets as our ground truth $$P^*(f|D)$$. In the case of *asia*, $$P^*(f|D) = \hat{P}_{STL}(f|D_{5000})$$.

We need a set of related networks and so we modify some structures of the given benchmark network to create similar but different networks. We delete each edge with some probability $$p_{del}$$ and vary $$p_{del}$$ from 0.1 to 0.5 to create sets of networks with more or less features in common for various experiments. If an edge is deleted, the conditional probability table for the child of the deleted edge is updated by marginalizing over the deleted parent. In our experiments, the full generative model is repeated 10 times to produce 10 different sets of K networks each for a given $$p_{del}$$.

### B. Benchmark Results

The goal of transfer learning is to accelerate the learning curve at smaller training set sizes by leveraging data among similar tasks. If we look closely at the results for one particular modified *asia* network, we can see what effect multitask learning has. Figure 2a shows the estimated posteriors from STL at smaller sample sizes. Even at these small sample sizes, the posteriors of the true edges tend to be higher than those of non-edges. However, compared to the estimates from large samples, these posteriors exhibit high variance and many are quite far from the large-sample posterior value (in the figure, error bars omitted for readability). The question is whether multitask learning can produce a steeper learning curve.

TABLE I: Performance increase for *asia* in terms of AUC given by MTL vs STL and MTL vs POOL


Figure 2b shows the learning curve achieved by MTL on the same network, using data leveraged from one other task, where some but not all edges are in common between the two tasks. This learning curve shows a wider gap between the estimated values of true edges and non-edges. In that sense, the learning curve is better than STL because it is better at separating the true edges from the non-edges at smaller training set sizes. In particular, this gain is achieved through the lower estimates of non-edges. In other words, non-edges are more quickly identified as such through transfer learning than without. On the other hand, the raw estimates of true edges tend to have such high variance (both with STL and with MTL) that it is not possible to say that one algorithm is doing better than the other in terms of converging on the actual $$P^*(f|D)$$.

Figure 2c shows the learning curve obtained by POOL on the same modified *asia* network. POOL combined the data from two modified networks with some edges in common. The algorithm effectively has twice as much data to work with as STL, therefore the learning curves are steeper. Yet there are quite a few non-edges with high posterior values.

To quantify these results, we measure how well the estimates for true edges separate from the estimates for non-edges. There is potentially a directed edge between each ordered pair of nodes. We call this set of potential edges E. We quantify the ground truth using the $$P^*(f|D)$$ values

![img-2.jpeg](img-2.jpeg)

Fig. 3: ROC curves for *asia*. Each point is the (FP rate, TP rate) aggregated over 2 tasks and 10 trials of the generative model, for a particular value of τ. Arrow indicates where STL and POOL curves cross.

obtained from large samples and identify the set of "true" edges E<sup>∗</sup> = {f ∈ E | P<sup>∗</sup>(f|D) > 0.5}.

To differentiate learned edges from learned non-edges, we assign a threshold τ and call any feature an edge if its posterior is greater than the threshold, E = {f ∈ E|P(f|D) > τ}. By varying τ, 0 ≤ τ ≤ 1, we can investigate the tradeoff between the rates of true-positives (TP) and false-positives (FP) in E by constructing an ROC curve (Figure 3). The TP rate is |E↔E<sup>∗</sup>|/|E|. The FP rate is |E \ E<sup>∗</sup>|/(|E| − |E|).

Figure 3 shows that various algorithms have different strengths along the ROC curve. The ROC shows that the patterns indicated in Figure 2 are borne out more generally; that is, STL is slowest to positively identify true edges, while POOL has difficulty eliminating false positives. MTL achieves the greatest overall separation of true edges and non-edges. Initially, at the left end of the ROC curve, with low false positive rates both MTL and STL perform best, finding more true positives than POOL. However, the performance of STL falls off as the false positive rate increases: STL is missing some true positives that both MTL and POOL are able to identify. MTL gives us the best of both worlds, giving the best overall performance.

Area under the curve (AUC) summarizes the overall performance along the ROC curve. We report AUC for various amounts of training data in Table I across 30 trials of the generative model. With these small training sets, the difficulty of the problem presented by each trial can vary quite a bit, therefore, the performance of each algorithm is compared directly on each trial by looking at how much greater the AUC is for MTL than the other algorithm. This increase in AUC score per trial is then averaged over all trials to give the numbers in Table I. Furthermore, a paired-T test is performed to determine whether this increase in performance is significant at the 5% confidence level. The winner of the paired-T test is given in Table I.

Similar experiments are performed on the larger *alarm* network. This network is too large for exact posterior computation, therefore we use MCMC approximation. We set MCMC hyper-parameters as recommended by [10], specifically, bucket size = 10, burn-in samples = 1000, sub-sample interval = 10 and total samples = 100. We tried other values (notably more

TABLE II: Performance increase on *alarm* for AUC given by MTL versus STL and MTL versus POOL


![img-3.jpeg](img-3.jpeg)

Fig. 5: Example ROC curves for *alarm* data. Each point represents the (FP rate, TP rate) aggregated over 2 tasks and 10 trials of the generative model, for a particular value of τ.

samples, larger sub-sample interval, and longer burn-in) and found that they give nearly the same results. We also use the transfer approximation described in Section IV-B, with h = 1000. For the ground truth *alarm* network, we use 10,000 training samples to estimate the true posterior of each feature, P<sup>∗</sup>(f|D) = P̂_{STL}(f|D_{10,000}).

The alarm network contains 37 variables, therefore there are 1,332 ordered pairs of nodes or potential edges in the set E. Of these, only 46 are true edges. We see again that on this data set, MTL estimates lower posteriors for the non-edges than STL or POOL (see Figure 4). The ROC curves in Figure 5 show that POOL routinely identifies many false positives. The curves for MTL and STL are closer, but again MTL is better at reducing the number of false positives. This makes differentiating the true edges from the false edges easier at small training set sizes, see Table II for AUC results. MTL dominates STL for small training sets. MTL dominates POOL at all training set sizes.

## VI. APPLICATION TO NEUROIMAGING

Our goal is to find functional brain networks associated with schizophrenia. We start with functional magnetic resonance image (fMRI) data that measure the activity levels in regions of interest (ROI) in the brain. The activity level for each ROI is de-trended using a sliding window mean and then discretized into four levels representing Very Low, Low, High and Very High activity levels (relative to the mean activity level of that ROI). The functional brain network is modeled as a Bayesian network of information sharing using a multinomial of discretized activity level among ROIs. Data has been collected from 86 healthy control subjects (*controls*) and

![img-4.jpeg](img-4.jpeg)

Fig. 4: Example posterior probability estimate for each edge in a modified *alarm* network from various small sample sets (means calculated from 20 sample sets). Blue curves are true edges shared by both tasks, cyan curves are true edges unique to this task, green are reverse of a true edge, red are non-edges. Up is good for blue and cyan curves. Down is good for red and green curves.

74 schizophrenia patients (*patients*). For each subject, there are 384 full-brain scans which are the samples in our training data. Brain images are parcellated using the Talaraich atlas giving 150 ROIs. Therefore, for each subject, we have a 150 × 384 data matrix. We concatenate the data from several subjects to create the training data for each task. We apply both our MTL algorithm and the standard STL Bayesian structure discovery algorithm. As our goal is to identify different structures between tasks, we do not use the POOL method that learns identical structures for both tasks.

The number of subjects in this study is much larger than in many other studies that we are interested in. We would like to learn reliable networks from small studies, and so we sub-sample the subjects in this study to see how consistent our results are across subsets of subjects. For evaluation purposes, we use the full set of data (86 controls and 74 patients) to learn a large-sample model and use this learned model as the ground truth to measure the small-sample results against. The results show how well learned models over various subsets of subjects are representative of the larger *control* and *patient* populations.

We limit the size of the parent sets to *r* = 2. With this setting, the time to calculate family scores is approximately 3 hours. For MTL family score calculation, we use the approximation method described in Section IV-B with *h* = 10,000. MCMC approximation is used to estimate the posterior likelihood of edges [10], with hyper-parameters bucket size = 10, burn-in samples = 5000, sub-sample interval = 10 and total samples = 1000.

### A. Small Samples

MTL estimates significantly lower posterior likelihoods on non-edges compared to STL. Evaluating results on real data is complicated by the fact that we do not have ground truth of known networks. Thereroe, we looked at the trend of estimates on smaller subset of the subjects and compare the results against the STL estimate from the full set of data. Figure 6a shows that for edges that are *not* determined to have real dependencies in the full data set (i.e. non-edges), the posterior estimate is significantly lower for MTL than STL. Significance

![img-5.jpeg](img-5.jpeg)

Fig. 6: Estimated posterior of features from small subsets of subjects. Points are perturbed horizontally for visibility.

was determined via a paired-t test at the 95% confidence level over various subsets of subjects selected. Figure 6b shows that there is no difference between MTL and STL in terms of the posterior estimate of true edges (according to paired-t test at 95% confidence). Therefore, MTL is able to eliminate the non-edges with less data than STL, corroborating results from the benchmark (*asia* and *alarm*) networks.

### B. Learned Dependencies

In practice, rather than giving a complete network as a solution to the neuroscientists, the solution is presented as a list of likely dependencies or visualized using network layout software with edge thicknesses proportional to the probability of the dependency. The functional brain networks learned in this paper are large enough the static images are difficult to read. In this paper, we are more concerned with the robustness of learned models rather than the brain networks themselves; therefore, we display the edge likelihoods as an adjacency matrix. Figure 7 shows the mean of the posterior likelihoods across the 10 bootstrap samples of sets of subjects. High probability edges are black squares in the heatmaps. In this experiment, we see that overall the edge likelihoods learned are sparse and they are fairly consistent across subsets of subjects. The likelihoods become "sharper" (closer to 0 or 1) as the amount of data increases, as expected. However, even for small

![img-6.jpeg](img-6.jpeg)

Fig. 7: Posterior probability estimates for each edge learned from neuroimage data. Means calculated from 10 sample sets.

numbers of subjects, we find clear patterns emerging. We also see that many dependencies are common to both the *control* and *patient* groups of subjects, while a few distinct differences are also visible. Through this type of visualization, a domain expert can gain insight into the possible interactions among variables in the system. The weight of the likelihood of each edge is important information to the domain scientist, which is not available from maximum a posterior multitask learning algorithms.

## VII. DISCUSSION

Our structure bias in the order-modular framework for Bayesian network structure discovery can be applied to many other problems currently being researched. In this paper, we demonstrate the application of structural bias to the problem of multitask learning. We find promising results from our approach and expect that further improvements can be made by tailoring the bias term to the application. Additionally, more sophisticated methods for approximating the transfer bias on large networks could be explored.

Implementation of a structural bias in Bayesian structure discovery is critical for solving other problems as well. [8] propose incorporating prior knowledge about biological networks in the form of a structural feature bias. Rather than using the exact calculation of posteriors that are possible when conditioning on orders, they attempt to find a different MCMC method for approximation. Their motivation was that it is inconvenient to define priors in the space of orders rather than structure. Our Theorem 1 shows that it is indeed possible to define structural priors at the structure level to use the efficient algorithms that rely on conditioning on orders.

This structural bias term could also be used to transfer knowledge about the direction of Bayesian network edges from interventional experiments [19]. Active learning of Bayesian network structure has been shown to significantly speed the learning of edges, particularly for getting directionality [20]. Multitask active learning algorithms would be useful for transferring knowledge from an experiment where interventions are possible to a similar domain where such interventions may be more expensive or impossible. Recent work proposes principled methods for the transfer of causal relationships between domains [21]. Our paper provides a critical algorithmic mechanism to implement such transfer of knowledge.

## VIII. CONCLUSIONS

We have presented a multitask Bayesian network structure algorithm. This algorithm is able to successfully leverage data from related tasks to improve the estimate of network structure features given limited amounts of data. The primary contribution is determining that structural priors that are order-modular can be used to impose inductive bias among tasks. By using local structural priors, we achieve three goals simultaneously: 1) an intuitive inductive bias at the level of structures rather than orders; 2) take advantage of the most efficient structure discovery algorithms; and 3) closed form Bayesian model averaging over the transfer strength parameter. Empirical evidence suggests that multitask learning of Bayesian networks reduces the number of spurious dependencies learned, particularly at small sample set sizes.

Acknowledgments: Thanks to Vincent Clark and the Mind Research Network for providing data and interesting data mining problems. Also, thanks to Eric Eaton and Paul Ruvolo for helpful discussions. Work funded by a grant from ONR N000141110139.
