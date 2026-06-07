# Partition MCMC for Inference on Acyclic Digraphs* 

Jack Kuipers<br>JACK.KUIPERS@BSSE.ETHZ.CH<br>D-BSSE, ETH Zurich<br>Mattenstrasse 26<br>4058 Basel, Switzerland

Giusi Moffa<br>Division of Psychiatry<br>University College London<br>London, UK


#### Abstract

Acyclic digraphs are the underlying representation of Bayesian networks, a widely used class of probabilistic graphical models. Learning the underlying graph from data is a way of gaining insights about the structural properties of a domain. Structure learning forms one of the inference challenges of statistical graphical models.

MCMC methods, notably structure MCMC, to sample graphs from the posterior distribution given the data are probably the only viable option for Bayesian model averaging. Score modularity and restrictions on the number of parents of each node allow the graphs to be grouped into larger collections, which can be scored as a whole to improve the chain's convergence. Current examples of algorithms taking advantage of grouping are the biased order MCMC, which acts on the alternative space of permuted triangular matrices, and non ergodic edge reversal moves.

Here we propose a novel algorithm, which employs the underlying combinatorial structure of DAGs to define a new grouping. As a result convergence is improved compared to structure MCMC, while still retaining the property of producing an unbiased sample. Finally the method can be combined with edge reversal moves to improve the sampler further.


Keywords: Bayesian Networks, Structure Learning, MCMC.

## 1. Introduction

A key question in applied statistics is to learn the relationship between a number of interacting entities and their surrounding environment. Examples include the many genes of a genome, the molecules in a cell, the different cells of an organism, demographics, economic and political factors in the dynamics of society, behavioural habits and biology in the development and progression of diseases. Most often, not only is the strength of the relationship between the variables unknown but so too is the connectivity structure itself, and of great scientific interest. Think for instance of gene regulatory networks (Friedman et al., 2000; Husmeier, 2003; Friedman, 2004; Rau et al., 2012) and cellular signalling pathways (Sachs et al., 2005; Mukherjee and Speed, 2008; Hill et al., 2012), including their development over time (Husmeier, 2003; Rau et al., 2012; Hill et al., 2012).

Probabilistic graphical models provide a framework for characterising the joint probability distribution of the variables in a domain and making inference about features of

[^0]
[^0]:    *. R code is available at https://github.com/annlia/partitionMCMC

interest. Bayesian networks are a popular class of probabilistic graphical models with directed acyclic graphs (DAGs) as their underlying structure. The representation is such that the joint probability distributions of the nodes of the network can be written as a product of the conditional distribution of each node given its parents in the graph. In general no structural information is available and the learning process involves both estimating the graphical structure and the parameters which characterise the conditional probability distributions of each node on its parents, given a particular network topology.

A rather comprehensive overview of approaches for Bayesian network learning is given by Daly et al. (2011). Structure learning is known to be a hard problem, especially due to the super-exponential growth of the DAG space when increasing the number of nodes. Broadly speaking the literature about structure learning can be divided into two classes: constraint-based methods, and score and search algorithms (as discussed for example in Koller and Friedman, 2009).

The edges of a Bayesian network encode conditional independence relationships, which constitute the main ingredient of constraint based learning methods, such as the widely used PC algorithm (Spirtes et al., 2000; Kalisch and Bühlmann, 2007) which was also recently implemented in the pcalg R package (Kalisch et al., 2012). Starting from a complete skeleton, decisions about whether edges should be deleted are made recursively based on tests of conditional independence. The tests start from pairwise comparisons and increase in complexity. By their very nature, methods building on this strategy are sensitive to local errors of the tests and to the order in which they are run (Colombo and Maathuis, 2014), but they tend to scale relatively well with the dimension.

On the other side of the spectrum are score and search algorithms, which rely on the definition of a measure of fit of a graphical model to the observed data. The fit is typically evaluated by scoring the entire network, with the drawback that the method requires exploration of the large network space.

In an attempt to exploit the strengths of each approach, hybrid solutions have also been proposed, as for example the max-min-hill-climbing method of Tsamardinos et al. (2006). Their algorithm first learns a skeleton of admissible edges in the network and then proceeds by a greedy hill-climbing restricted to the space of structures compatible with the learned skeleton. Hybrid methods take advantage of the constraint based ideas to perform - possibly rather conservative - significance tests in a first phase, only to reduce the search space of a second score and search phase.

The direction of the edges in a Bayesian network are interesting from a causal perspective, since the connections learned from observational data may help unveil unknown causal relations. Due to the great potential for shedding light on important scientific questions, the possibility of deriving causal statements from DAGs has had great appeal ever since the causal interpretation of Bayesian networks was proposed (Pearl and Verma, 1991; Pearl, 2000). Caution must however be taken in interpreting DAGs causally (Dawid, 2010), since it is only justified under strict and quite likely untestable assumptions, such as not having unmeasured confounders. Moreover, graphical structures encoding the same conditional independencies cannot be distinguished from observational data, so that even in the best case scenario only the equivalence class of all the networks describing the same probability distribution can be inferred.

Recently Maathuis et al. (2009) proposed an interesting extension of the intervention calculus of Pearl (2000) to scenarios where the underlying DAG is unknown and only an equivalence class can be learned from data, while retaining the strict assumptions of faithfulness and absence of unobserved confounders. A combination of observational and interventional data may however help to distinguish between the models of an equivalence class (Cooper and Yoo, 1999; Eaton and Murphy, 2007b; Hauser and Bühlmann, 2015; see also Friedman et al., 2000 for a concise discussion about the discovery of causal patterns from observational data).

The focus of our work is on score and search methods, and in particular on MCMC methods for the graph space exploration. The main advantage of MCMC approaches with respect to methods based on greedy searches and other optimisation algorithms is that they can provide a collection of samples from the posterior distribution of the graph given the data. This means that inference can be made in the spirit of Bayesian model averaging, since the expectation of given network features, such as the posterior probability of an individual edge, can be estimated by averaging over the sample (Madigan and York, 1995). The possibility of conducting Bayesian model averaging is especially important in high dimensional domains with sparse data, where no single best model can be clearly identified, so that relying on the best scoring model to perform inference is unjustified.

The first MCMC algorithm over graph structures is due to Madigan and York (1995), later refined by Giudici and Castelo (2003). To improve on the mixing and convergence, Friedman and Koller (2003) suggested to build a Markov chain on the space of node orders instead, at the price of introducing a bias in the sampling. For smaller systems, space and time complexity are such that an efficient option is given by dynamic programming (Koivisto and Sood, 2004), which can also be used to extend the proposals of standard structure MCMC in a hybrid method (Eaton and Murphy, 2007b). Within the MCMC approach, to avoid the bias in order MCMC, while keeping reasonable convergence, Grzegorczyk and Husmeier (2008) more recently proposed a new edge reversal move combining ideas both of standard structure and order MCMC.

In this paper we present a novel MCMC algorithm designed on the combinatorial structure of DAGs, with the advantage of improving convergence with respect to structure MCMC. At the same time it still provides an unbiased sample since it acts directly on the space of DAGs. It can also be combined with the algorithm of Grzegorczyk and Husmeier (2008), in place of structure, to promote convergence.

Bayesian networks provide a valuable tool for gaining insights from observational data about the mechanism underlying the data generating process, and help to design experiments which can validate observational findings. Efficient tools for structure learning are therefore highly important. While there are a number of software packages, such as pcalg (Kalisch et al., 2012) and bnlearn (Scutari, 2010) in R, for constraint based learning methods, publicly available tools for MCMC based structure learning algorithms are less common, with the possible exception of BDAGL (Eaton and Murphy, 2007a). In tandem with dynamic programming approaches, both standard structure, and MCMC in the space of orders are implemented in BDAGL, but not the more recent new edge reversal move of Grzegorczyk and Husmeier (2008) and the package is written for Matlab.

With this paper we provide R code for structure (Madigan and York, 1995) and order (Friedman and Koller, 2003) MCMC, together with the algorithm of Grzegorczyk and Husmeier (2008) and our newly proposed partition MCMC.

# 2. Terminology and notation of Bayesian networks 

Given a set of $n$ random variables $\boldsymbol{X}=\left\{X_{1}, \ldots, X_{n}\right\}$ we are interested in characterising their joint probability distribution by means of a directed graphical model. A Bayesian network $\mathcal{B}=(\mathcal{G}, \theta)$ can be fully specified by associating a set of parameters $\theta$ to a directed acyclic graph $\mathcal{G}$ whose nodes are the random variables in $\boldsymbol{X}$. The parameters $\theta$ specify a conditional probability distribution $P\left(X_{i} \mid \mathbf{P a}_{i}\right)$ for each variable $X_{i}$ given the set of its parents $\mathbf{P a}_{i}$ in the graph $\mathcal{G}$. From the Markov assumption (Koller and Friedman, 2009) that each variable $X_{i}$ is independent of its non-descendants given its parents in the graph $\mathcal{G}$, it follows that the joint probability distribution described by the Bayesian network $\mathcal{B}$ factorizes as

$$
P\left(X_{1}, \ldots, X_{n}\right)=\prod_{i}^{n} P\left(X_{i} \mid \mathbf{P a}_{i}\right)
$$

The random variables in $\boldsymbol{X}$ can be discrete, continuous, or a mixture of both. In our examples we will focus on continuous variables with a multivariate Gaussian distribution (Geiger and Heckerman, 2002; see also the correction in Consonni and Rocca, 2012; Kuipers et al., 2014).

In practice we may want to learn a Bayesian network $\mathcal{B}$ which best explains a set of independent observations $D$ from the distribution of the variables in $\boldsymbol{X}$. The estimation of a Bayesian network breaks up into two steps (Cowell et al., 2007), referred to as structure and parameter learning. Given the data $D$ we wish to learn the structural dependence of the variables in $\boldsymbol{X}$ encoded by a DAG $\mathcal{G}$ and estimate a set of parameters $\theta$ for the corresponding $\mathcal{G}$. The focus of our work here is on the structure learning, in the context of search and score algorithms.

It is well known, however, that the structure of the network, or in other words the DAG, is identifiable only up to an equivalence class. All DAGs in an equivalence class encode the same probability distribution. Equivalent DAGs share the same skeleton, or undirected underlying graph, and the same v-structures (two parents with the same child and no direct edge between them, Verma and Pearl, 1990). In practice, even from perfect or noiseless data, when all conditional independencies are known exactly, we can only learn the common features of an equivalence class (Maathuis et al., 2009), which can be represented by a completed partially directed acyclic graph (CPDAG) or an essential graph (Andersson et al., 1997).

The scoring functions for the graphical structure are typically derived from a Bayesian approach, where the score for a DAG $\mathcal{G}$ is defined as its posterior probability given the data $D$

$$
P(\mathcal{G} \mid D) \propto P(D \mid \mathcal{G}) P(\mathcal{G})
$$

with $P(\mathcal{G})$ a prior distribution over graphical structures. The marginal likelihood $P(D \mid \mathcal{G})$ is obtained by integrating the likelihood function $P(D \mid \mathcal{G}, \theta)$ over the parameter prior $P(\theta \mid \mathcal{G})$ for a given graph $\mathcal{G}$ and over the parameter space $\Theta$. When the prior satisfies the conditions

of structure modularity, parameter independence and parameter modularity as defined by Heckerman and Geiger (1995), and if the data is complete, the score is structure equivalent and decomposable (Friedman et al., 2000; Friedman and Koller, 2003)

$$
P(\mathcal{G} \mid D) \propto P(D \mid \mathcal{G}) P(\mathcal{G})=\prod_{i} S\left(X_{i}, \mathbf{P a}_{i} \mid D\right)
$$

where $S$ is a score function depending only on the node variable $X_{i}$ and its parents. The decomposability is important from an implementation point of view, since it means that during a structure search, only the score of the nodes whose parents change with respect to the previously scored structure needs to be reevaluated. Since the number of possible DAGs grows super-exponentially with the number of vertices, an exhaustive search quickly becomes impracticable even for a moderate number of nodes. State of the art approaches rely on approximate solutions, in particular from simulation methods based on MCMC.

# 3. Structure learning of Bayesian networks by MCMC methods 

Before presenting our algorithm, we briefly review the current state of the art of MCMC methods for structure learning of Bayesian networks. The most common strategies rely either on elementary moves in the graph structure, involving a single edge, or on sampling in the space of node orders, but leading to biased samples. The novelty of our approach consists in starting from the combinatorial representation of DAGs to build an efficient MCMC scheme directly on the space of DAGs.

### 3.1 Structure MCMC

The classical MCMC method for learning the underlying structure of Bayesian networks dates back to Madigan and York (1995) and is referred to by Friedman and Koller (2003) as structure MCMC. It is based on the simple idea of building a Markov chain on the space of graphical models, such that its stationary distribution is the posterior distribution $P(\mathcal{G} \mid D)$ of the network $\mathcal{G}$ given the data $D$. The simplest procedure constructs a random walk by means of the simple operations of addition and deletion of single edges in a Metropolis Hastings algorithm.

Given a DAG $\mathcal{G}_{j}$ at iteration $j$, find the neighbourhood $\operatorname{nbd}\left(\mathcal{G}_{j}\right)$ of all DAGs with one edge added or deleted (and including $\mathcal{G}_{j}$ itself). Sample a new graph $\mathcal{G}^{\prime}$ uniformly from this neighbourhood with proposal probability

$$
q\left(\mathcal{G}^{\prime} \mid \mathcal{G}\right)=\left\{\begin{array}{cl}
\frac{1}{\# \operatorname{nbd}\left(\mathcal{G}_{j}\right)} & \text { if } \mathcal{G}^{\prime} \in \operatorname{nbd}\left(\mathcal{G}_{j}\right) \\
0 & \text { otherwise }
\end{array}\right.
$$

as defined by Madigan and York (1995).
The acceptance probability for the proposed graph in a Metropolis Hastings algorithm is then

$$
\rho=\min \left\{1, \frac{q\left(\mathcal{G}_{j} \mid \mathcal{G}^{\prime}\right) P\left(\mathcal{G}^{\prime} \mid D\right)}{q\left(\mathcal{G}^{\prime} \mid \mathcal{G}_{j}\right) P\left(\mathcal{G}_{j} \mid D\right)}\right\}=\min \left\{1, \frac{\# \operatorname{nbd}\left(\mathcal{G}_{j}\right) P\left(\mathcal{G}^{\prime} \mid D\right)}{\# \operatorname{nbd}\left(\mathcal{G}^{\prime}\right) P\left(\mathcal{G}_{j} \mid D\right)}\right\}
$$

so that the next state in the chain $\mathcal{G}_{j+1}=\mathcal{G}^{\prime}$ with probability $\rho$ and $\mathcal{G}_{j+1}=\mathcal{G}_{j}$ otherwise.

Once the chain converges, it provides a sample $\mathcal{G}^{\star}$ of a graphical structure from the posterior distribution $P(\mathcal{G} \mid D)$, providing the means to conduct inference based on Bayesian model averaging. Typically this means collecting a (correlated) sequence of DAGs from one or several MCMC chains, after a burn-in period to decouple from the starting point of the chain. Since processing the DAGs after they have been sampled can be quite computationally expensive, thinning is often appropriate (Link and Eaton, 2012).

By modifying the original algorithm of Madigan and York (1995) to include the possibility of reversing an edge, the convergence speed can be greatly improved (Giudici and Castelo, 2003). Moreover, rejection sampling from a larger fixed sized neighbourhood can be employed to avoid explicitly calculating the neighbourhood, which can further speed up the implementation (Giudici and Castelo, 2003). Even with these improvements, structure MCMC can still struggle to converge for relatively small DAGs. In Appendix A. 2 for example, severe convergence difficulties are already apparent for DAGs with 14 nodes.

To assess the accuracy of structure learning algorithms, Tsamardinos et al. (2006) introduced the structural Hamming distance (SHD) on CPDAGs. The SHD corresponds to the number of simple operations, namely additions and deletions of both directed and undirected edges, or reversing of directed edges, required to go from one CPDAG to the other.

Although the SHD is calculated on CPDAGs rather than DAGs (to avoid penalising statistically non identifiable differences), one could say that the SHD is the rational behind structure MCMC. Namely, proposals are limited to graphical structures with a SHD of 1 from the current graph. Interestingly, what complicates things for exploring the space of graphical structures is not only the super-exponential growth of their space size, but also the fact that the behaviour of the SHD does not necessarily correspond to similar behaviours in the likelihood landscape. The score of a network may in fact change substantially when performing small changes to the structure (Friedman and Koller, 2003), or it may, on the other hand, vary very little when making more important modifications to the network structure.

Intuition suggests that it should be possible to define more efficient MCMC schemes by making proposals which more closely reflect the likelihood landscape. Defining suitable distances between graphical structures to help design better schemes is unfortunately not straightforward. In the context of causal graphs a distance was recently defined (Peters and Bühlmann, 2015), though purely based on a graphical criterion, directly related to the network interpretation in terms of differences in the causal inference statements deriving from each structure.

# 3.2 Order MCMC 

To overcome the slow mixing property of structure MCMC, Friedman and Koller introduced the order MCMC algorithm (Friedman and Koller, 2003). Key is the concept of a node ordering $\prec$ which is simply a permutation of the $n$ node labels. The nodes are essentially lined up in a chain and labelled according to the given permutation. The DAGs belonging to the corresponding order are such that each node may only have parents from further up the chain, or following it in the ordering.

For example if for $n=3$ we choose the ordering $3,1,2$ then node 3 could have either of the others (or both or none) as parents. Node 1 may only have node 2 (or none) as parents while node 2 is forced to have no parents. The possible choices of parents can be represented as an adjacency matrix where the rows and columns are labelled according to the order


so that only the lower triangular elements can differ from 0 . Each choice for the lower triangular elements is a different DAG and there are therefore 8 different DAGs compatible with this ordering of 3 nodes.

The great insight of Friedman and Koller (2003) was that if the score is modular, and we precompute the score of each node's possible parent sets, we can efficiently sum the scores of all the DAGs compatible with a particular node ordering. For each node we simply sum the scores of all the parent sets that do not include nodes preceding it in the ordering. The product of the node score sums over possible parent sets provides a score $R(\prec \mid D)$ of the entire order $\prec$ given the data $D$

$$
R(\prec \mid D)=\sum_{\mathcal{G} \in \prec} P(\mathcal{G} \mid D) \propto \prod_{i=1}^{n} \sum_{\mathbf{P a}_{i} \in \prec} S\left(X_{i}, \mathbf{P a}_{i} \mid D\right)
$$

However, for each node the number of parents sets is $2^{n-1}$ which all need to be scored and searched through to find the score of each order. To prevent the exponential complexity as $n$ increases, a hard limit $K$ on the size of the parent sets is typically introduced to reduce the complexity of scoring each node to order $n^{K}$. A low threshold could exclude highly scoring DAGs while increasing $K$ too highly could increase the computational cost without a concomitant improvement in the DAGs included. One therefore aims to select the lowest value which still encapsulates the bulk of the posterior weight.

A Markov chain can then be constructed on the smaller space of node orders rather than the space of all DAG structures. A chain with stationary distribution proportional to $R(\prec \mid D)$ can be produced by a Metropolis Hastings algorithm with acceptance probability

$$
\rho=\min \left\{1, \frac{q\left(\prec_{j} \mid \prec^{\prime}\right) R\left(\prec^{\prime} \mid D\right)}{q\left(\prec^{\prime} \mid \prec_{j}\right) R\left(\prec_{j} \mid D\right)}\right\}
$$

where $q\left(\prec^{\prime} \mid \prec\right)$ is the probability of proposing a move to $\prec^{\prime}$ from $\prec$, and can be any move in the space of permutations or orders (see Friedman and Koller, 2003, for some examples). The simplest move consists in flipping two nodes in the order while leaving the other unchanged. This is symmetric so that the $q$ terms in (2) cancel.

Upon convergence, order MCMC provides a sample of an order $\prec^{*}$ from a distribution proportional to the score $R(\prec \mid D)$ over the space of $n$ ! possible orders of the nodes of the graphical structure. Given a sampled order, one can sample a DAG by sampling the parents of each node independently according to the scores of its permissible parent sets.

By grouping together and averaging the score over so many DAGs, the convergence properties of the MCMC chain on the much smaller space of orders are vastly improved compared to structure MCMC (Madigan and York, 1995; Giudici and Castelo, 2003).

The convergence improvement, however, only works by ignoring the combinatorial structure of DAGs and working on the much simpler space of permuted triangular matrices. With $n$ nodes there are $2^{L}$ DAGs consistent with each order with $L=n(n-1) / 2$ the number of lower triangular elements, since each can take one of two values. There are also $n$ ! orders giving a total of $n!2^{L}$ permuted lower triangular matrices. The number of DAGs, $a_{n}$, is exponentially smaller, as can be seen from the asymptotic behaviour (Robinson, 1970, 1973; Stanley, 1973)

$$
a_{n} \sim \frac{n!2^{L}}{M q^{n}}
$$

where $M=0.574 \ldots$ and $q=1.48 \ldots$ are constants. The number of orders each DAG belongs to is therefore exponentially large on average (it can range from 1 to $n!$ ). The fact that a given graph $\mathcal{G}$ may be consistent with more than one order induces a bias in the posterior distribution defined on the space of graphical structures.

This bias arises since the expression in equation (1) does not exactly correspond to the posterior distribution $P(\prec \mid D)$ which can be written instead as

$$
P(\prec \mid D)=\sum_{G} P(\mathcal{G}, \prec \mid D)=\sum_{G \in \prec} P(\prec \mid \mathcal{G}) P(\mathcal{G} \mid D)
$$

The difference with respect to (1) consists of the term $P(\prec \mid \mathcal{G})$, which is the inverse of the number of orders the DAG $\mathcal{G}$ is consistent with. Neglecting this term in the order MCMC algorithm then weights DAGs by the number of orders they belong to, resulting in the aforementioned bias.

This weighting can also be seen as a consequence of placing a prior on orders $P(\prec)$. The prior on graphs is then determined as $P(\mathcal{G})=\sum_{\prec} P(\mathcal{G} \mid \prec) P(\prec)$ so each DAG obtains a contribution from each order it can belong to. Attempts to remove the bias via importance sampling (Ellis and Wong, 2008) can help for small graphs, but they struggle as the size increases due to the exponential number of orders DAGs can be consistent with on average.

# 3.3 New edge reversal moves 

Since the bias is the main problem with order MCMC, while the slow convergence is the main limit of structure MCMC, Grzegorczyk and Husmeier (2008) introduced a novel edge reversal move into structure MCMC in an attempt to overcome both difficulties. Their new move also relies on the key feature of order MCMC, of combining the score of many possible parent sets. Moreover, when an edge is reversed, the parents of the two nodes that it connects are resampled according to their score. Since the jumps are chosen according to their score, the chain moves to more probable DAGs more quickly, which vastly improves the convergence of structure MCMC. The edge reversal move typically results in the proposal of DAGs with a SHD bigger than 1 from the current graph in the chain, so that larger jumps than those of structure MCMC are possible.

Since the edge reversal operation requires the knowledge of the scores of many possible parent sets, again a hard limit $K$ on the size of such sets is usually introduced as in order MCMC. Moreover by itself the new edge reversal move is not ergodic in the space of DAGs. To overcome this problem, the complete sampling algorithm of Grzegorczyk and Husmeier (2008) combines the new move with an underlying structure MCMC chain in a mixture,

where a new reversal move is proposed with a given probability $p_{\text {rev }}$ and a classical structure move with probability $1-p_{\text {rev }}$. Since both structure MCMC and the new edge reversal move are unbiased, the algorithm based on their mixture is also unbiased in the space of DAGs.

At the same time as avoiding the bias inherent in order MCMC the algorithm of Grzegorczyk and Husmeier (2008) exhibits much better convergence than structure MCMC. One may try to combine all the currently available methods to find the most efficient way of sampling DAGs according to their posterior probabilities. A valid strategy consists of using order MCMC to find a graph from which to start a chain, which is then continued with the mixture of structure MCMC and edge reversal.

# 4. Partition MCMC 

In the current paper we propose a novel MCMC method which adheres to the philosophy of order MCMC but which respects the combinatorial structure of DAGs. In particular, we define a MCMC algorithm on the space of node partitions, essentially a subdivision of orders necessary to avoid over representing certain DAGs. The subdivision will in general slow the convergence compared to order MCMC, but by acting directly on the space of acyclic digraphs our algorithm does not suffer from bias. As for edge reversal, one may run order MCMC to start the chain and then continue with partition MCMC to remove the bias.

The grouping of DAGs into partitions means that the convergence is much improved with respect to structure MCMC. Moreover, we can efficiently combine our method with the new edge reversal move of Grzegorczyk and Husmeier (2008) and improve upon their MCMC sampler.

### 4.1 Outpoints

DAGs, since they do not admit cycles, must have at least one outpoint, defined as a node with no incoming arcs. Outpoints are also known as sources. In Figure 1 for example nodes 1,3 and 5 are outpoints. If these, and their outgoing edges, are removed from the graph then we are left with a smaller DAG. A single outpoint is then left as node 4 , which when removed leaves node 2 as the sole outpoint. This property allows DAGs to be built recursively and enumerated (Robinson, 1970, 1973), which also means they can be sampled uniformly (Kuipers and Moffa, 2015).

If we combine the outpoints at every stage into $m$ sets each of size $k_{i}$ then since all nodes are placed somewhere, $\sum_{i=1}^{m} k_{i}=n$ and we have partitioned $n$ into $\left[k_{1}, k_{2}, \ldots k_{m}\right]$. For example in Figure 1, we have the following three sets: $\{2\},\{4\}$ and $\{1,3,5\}$ and the partition $[1,1,3]$. The partition order is reversed from Kuipers and Moffa (2015).

When arranging the partitioned sets of nodes in groups from left to right, edges are only allowed to come from sets, or partition elements, further to the right. The arrangement is similar to the ordering used in order MCMC, but there are two additional restrictions:

- nodes in the same partition element are not allowed to be connected to each other (otherwise they would not be concurrent outpoints)

![img-0.jpeg](img-0.jpeg)

Figure 1: By collecting the outpoints at each step into a set, the DAG on the left can be redrawn according to the partition $[1,1,3]$ where now edges are only allowed to come from the right.

- nodes must be connected to by at least one directed edge from the nodes in the adjacent partition element to the right (otherwise they would be outpoints at an earlier stage).

For example, in Figure 1 node 2 must receive an edge from node 4.

# 4.2 MCMC for uniform sampling 

The number of DAGs belonging to a given partition follows from the number of edge possibilities. Let $S_{j}=\sum_{i=j}^{m} k_{i}$ then

$$
a_{\left[k_{1}, \ldots, k_{m}\right]}=\frac{n!}{k_{1}!\ldots k_{m}!} \prod_{j=1}^{m-1}\left(2^{k_{j+1}}-1\right)^{k_{j}} \prod_{j=1}^{m-2} 2^{k_{j} S_{j+2}}
$$

The first combinatorial term is the number of ways of distributing the $n$ nodes into the $m$ partition elements of size $k_{1}, \ldots, k_{m}$. Basically, permuting the nodes labels inside a partition element has no effect on the set of DAGs consistent with the partition. The second term counts the number of ways in which the nodes in each partition element can receive edges from the adjacent element to the right, where subtracting 1 inside the bracket excludes the case when the nodes receive no edges. The final term is the number of possible edges from nodes in partition elements even further right. The number of DAGs in a partition therefore varies from 1 for the partition with a single element up to $n!2^{L-n+1}$ for the partition with $n$ elements.

By assigning each partition $P$ a score $a_{P}$, a MCMC scheme was previously introduced in the space of partitions to sample DAGs uniformly (Kuipers and Moffa, 2015). In particular the moves were chosen so that the ratio of scores $\frac{a_{P}!}{a_{P}}$ in the acceptance probability simplified and was as cheap as possible to evaluate. Here we extend the method to sample from a posterior distribution in the context of Bayesian inference for directed graphical models. Namely, a MCMC sampling procedure can be built from the combinatorial structure of DAGs, which comprises:

- an ordered partition of $n$, namely $\lambda=\left[k_{1}, k_{2}, \ldots k_{m}\right]$ with $\sum k_{i}=n$

- a permutation $\pi$ on the node labels
- edges connecting the nodes (with certain restrictions).


# 4.3 Scoring partitions 

For a given partition and permutation, permuting the labels inside a partition element does not matter, so an ordering can be fixed. Denote by $\pi_{\lambda}$ a single representative of the equivalent permutations with respect to the partition $\lambda$ so that the pair $\left(\lambda, \pi_{\lambda}\right)=\Lambda$ can be viewed as a labelled partition.

Analogously to order MCMC, for a given labelled partition $\Lambda$ and with a modular score we can score all permissible parent sets for each node. From the list of all parent sets we exclude any with a member in the same partition element or in one further left. Only parent sets with at least one member in the partition element immediately to the right need to be included. For example, if $\lambda=[1,2,2]$ and $\pi_{\lambda}=2,3,4,1,5$ as in Figure 2(c), we can look at the possible parent sets for node 3 . Nodes 2 and 4 are excluded as possible parents while at least one of 1 and 5 must be included, resulting in three possible parent sets.

By summing the scores of the permissible parent sets for each node (and multiplying the sums for all nodes), we treat all the possible edge combinations and hence combine the score of all DAGs consistent with the given labelled partition $\Lambda$. The total score so obtained coincides with the posterior probability of the labelled partition

$$
P(\Lambda \mid D)=\sum_{\mathcal{G}} P(\Lambda \mid \mathcal{G}, D) P(\mathcal{G} \mid D) \equiv \sum_{\mathcal{G} \in \Lambda} P(\mathcal{G} \mid D) \propto \prod_{i=1}^{n} \sum_{\mathbf{P a}_{i} \in \Lambda} S\left(X_{i}, \mathbf{P a}_{i} \mid D\right)
$$

and a MCMC chain can be built on the joint space of partitions and permutations. Each MCMC move needs to propose a new labelled partition $\Lambda^{\prime}$ which is accepted with probability

$$
\rho=\min \left\{1, \frac{\# \operatorname{nbd}(\Lambda) P\left(\Lambda^{\prime} \mid D\right)}{\# \operatorname{nbd}\left(\Lambda^{\prime}\right) P(\Lambda \mid D)}\right\}
$$

where the neighbourhood needs to be calculated for each move type.

### 4.4 Basic move

The basic move consists of splitting a partition into two or joining two adjacent ones. In Kuipers and Moffa (2015) this move was performed by a mapping to binary sequences. As an example, in Figure 1 which is redrawn in Figure 2(a), node 4 may be joined to node 2 or the set $\{1,3,5\}$ and the partition element containing $\{1,3,5\}$ may be split in two. If we do split $\{1,3,5\}$ into two by separating off node 3 to the left, we move from Figure 2(a) to Figure 2(b). Further joining nodes 3 and 4 gives the labelled partition in Figure 2(c).

However when splitting an element of size $k$ into two elements of size $c$ and $k-c$ respectively there are $\binom{k}{c}$ ways to separate the nodes and correspondingly update the permutation. With $(m-1)$ ways of joining partition elements, the size of the neighbourhood is then

$$
m-1+\sum_{i=1}^{m} \sum_{c=1}^{k_{i}-1}\binom{k_{i}}{c}=m-1+\sum_{i=1}^{m}\left(2^{k_{i}}-2\right)=-m-1+\sum_{i=1}^{m} 2^{k_{i}}
$$

![img-1.jpeg](img-1.jpeg)

Figure 2: From the partition $\lambda=[1,1,3]$ in Figure 1 drawn in (a) splitting the partition element containing nodes $\{1,3,5\}$ into two by moving node 3 into a new partition element on the left leads to the labelled partition in (b) with $\lambda=[1,1,1,2]$. Further combining the two partition elements containing nodes 4 and 3 leads to the partition in (c) with $\lambda=[1,2,2]$.

Algorithm 1 Sample a proposal partition $\Lambda^{\prime}$ from the neighbourhood of $\Lambda$
input An ordered partition $\Lambda$
Sample an integer $j$ uniformly from $1: \# \operatorname{nbd}(\Lambda)$ where

$$
\# \operatorname{nbd}(\Lambda)=m-1+\sum_{i=1}^{m} \sum_{c=1}^{k_{i}-1}\binom{k_{i}}{c}
$$

with $m$ the number of partition elements in $\Lambda$ and $k_{i}$ the size of element $i$
if $j<m$ then
Join partition elements $j$ and $j+1$ of $\Lambda$ to form $\Lambda^{\prime}$
else
Find minimum $i^{\star}$ such that

$$
j \leq m-1+\sum_{i=1}^{i^{\star}} \sum_{c=1}^{k_{i}-1}\binom{k_{i}}{c}
$$

Find minimum $c^{\star}$ such that

$$
j \leq m-1+\sum_{i=1}^{i^{\star}-1} \sum_{c=1}^{k_{i}-1}\binom{k_{i}}{c}+\sum_{c=1}^{c^{\star}}\binom{k_{i^{\star}}}{c}
$$

Sample $c^{\star}$ nodes from partition element $i^{\star}$ in $\Lambda$
Split them off into a new partition element on the left to form $\Lambda^{\prime}$
end if
return $\Lambda^{\prime}$

We can therefore sample from the neighbourhood uniformly as summarised in Algorithm 1. This then allows us to define the full MCMC scheme for the basic move in Algorithm 2.

```
Algorithm 2 Basic MCMC in the partition space
    input Chain length \(T\) and an initial ordered partition \(\Lambda_{0}\)
    for \(t=1\) to \(T\) do
        Sample \(\alpha\) uniformly from \((0,1)\)
        if \(\alpha<0.01\) then \(\triangleright\) Small probability to stay still
            \(\Lambda_{t}=\Lambda_{t-1}\)
        else
            Sample a proposal partition \(\Lambda^{\prime}\) from \(\Lambda_{t-1}\) using Algorithm 1
            Sample \(\alpha\) uniformly from \((0,1)\)
            if \(\alpha<\frac{\# \operatorname{nbd}(\Lambda) P\left(\Lambda^{\prime} \mid D\right)}{\# \operatorname{nbd}\left(\Lambda^{\prime}\right) P(\Lambda \mid D)}\) then
                \(\Lambda_{t}=\Lambda^{\prime}\)
            else
                \(\Lambda_{t}=\Lambda_{t-1}\)
            end if
        end if
        Sample DAG \(\mathcal{G}_{t}\) from \(\Lambda_{t}\) weighted following \(P\left(\Lambda_{t} \mid D\right)=\sum_{\mathcal{G} \in \Lambda_{t}} P(\mathcal{G} \mid D)\)
    end for
    return \(\left\{\mathcal{G}_{t}\right\}\)
```

When joining two partition elements, only the nodes from the partition element on the left and its adjacent element further left need to be rescored. Similarly, when splitting a partition element, only the nodes in the newly formed element on the left, and its adjacent element further left need to be rescored.

# 4.5 Sampling DAGs 

Splitting and joining partitions are inverse moves of each other, so the moves are reversible. Since all partition elements can be joined into a single one in up to $(n-1)$ steps and then separated out into a new labelled partition in up to $(n-1)$ further steps, the chain is certainly irreducible after $2(n-1)$ steps and introducing a small probability of staying still, will avoid the possibility of a periodic chain. Finally (4) ensures detailed balance since

$$
\begin{aligned}
P(\Lambda \mid D) P\left(\Lambda \rightarrow \Lambda^{\prime}\right) & =\frac{P(\Lambda \mid D)}{\# \operatorname{nbd}(\Lambda)} \min \left\{1, \frac{\# \operatorname{nbd}(\Lambda) P\left(\Lambda^{\prime} \mid D\right)}{\# \operatorname{nbd}\left(\Lambda^{\prime}\right) P(\Lambda \mid D)}\right\} \\
& =\min \left\{\frac{P(\Lambda \mid D)}{\# \operatorname{nbd}(\Lambda)}, \frac{P\left(\Lambda^{\prime} \mid D\right)}{\# \operatorname{nbd}\left(\Lambda^{\prime}\right)}\right\}=P\left(\Lambda^{\prime} \mid D\right) P\left(\Lambda^{\prime} \rightarrow \Lambda\right)
\end{aligned}
$$

The conditions to sample labelled partitions from the posterior $P(\Lambda \mid D)$ are therefore satisfied.

Since $P(\Lambda \mid D)=\sum_{\mathcal{G} \in \Lambda} P(\mathcal{G} \mid D)$ as in (3), from each sampled labelled partition $\Lambda$ we sample a single DAG, $\mathcal{G} \in \Lambda$, weighted according to $P(\mathcal{G} \mid D)$ to obtain DAGs sampled from their posterior. This DAG sampling step is then included in the MCMC scheme, for example with the basic partition move as outlined in Algorithm 2.

![img-2.jpeg](img-2.jpeg)

Figure 3: Redrawing the partition with $\lambda=[1,2,2]$ from Figure 2(c) with spaces either side of the partition elements highlighted as in (a), we first sample node 4 and choose to move it into the partition element containing node 2 to arrive at the partition in (b) with $\lambda=[2,1,2]$. Then we sample node 2 itself and choose to move it to a new partition element creating the partition in (c) with $\lambda=[1,1,1,2]$.

# 4.6 Additional partition move 

To change the size of a partition element however, it is necessary first to split nodes off and then join them to a different partition element. For example, going from Figure 2(a) to Figure 2(c) takes two basic move steps. A partition move could also be considered whereby we swap nodes directly from one partition element to another.

It is possible to move one node at a time. For example, each node may move either to a different partition element or to one of the gaps in between (or outside) to create a new partition element containing a single node. In the partition of Figure 2(c) with $m=3$ elements, there are a total of four gaps as highlighted in Figure 3(a). To make a move, first sample a node uniformly from the $n$ available. Then place that node in one of the $(m+1)$ gaps or $(m-1)$ different partition elements, also chosen uniformly. In the example of Figure 3, we first sample node 4 to move to the first partition element, then node 2 to move to the third gap. The neighbourhood of the move given the partition is simply $2 m n$.

However, moving one node from a partition element containing two nodes into the gap to the right, or the other node into the gap to the left, leads to the same labelled partition. Likewise moving a node from a partition element containing a single node into the gap either side, the partition remains unchanged. To marginally improve the convergence, the latter possibility is excluded, and nodes from partition elements with two nodes are not allowed to move into the gap immediately to their left. The neighbourhood calculation also needs to be adjusted to account for these exclusions.

As a node can be moved anywhere in the partition, a larger number of nodes might need to be rescored at each step. However, this move can be weighted relative to the basic move to keep the average number of nodes that need to be rescored down to around 4 . This is independent of $n$, which keeps the complexity of the scheme lower.

### 4.7 Permutation moves

Currently, exploring the space of permutations requires us to appropriately combine and split partition elements. We could instead add moves directly in the space of permutations.

The simplest strategy consists of swapping two elements sampled uniformly at each step. It then takes $(n-1)$ steps to build an irreducible chain on the space of permutations. The size of the neighbourhood is independent of the partition and fixed at $L$.

However, swapping nodes inside the same partition element does not change anything and just increases the probability of staying still. Excluding such possibilities and only swapping nodes in different partition elements, the neighbourhood is then smaller and equal to

$$
\sum_{i=1}^{m} \frac{k_{i}\left(n-k_{i}\right)}{2}
$$

Finally, one could consider only allowing nodes in adjacent partition elements to be swapped. The idea here would be that this move would be more 'local' and be more likely to choose a swap with a high score. Only a smaller number of nodes need to be rescored leading to faster steps in the chain. The neighbourhood is smaller still and equal to

$$
\sum_{i=1}^{m} k_{i} k_{i+1}
$$

but the irreducibility length in the space of permutations increases up to order $n^{2}$. Accordingly, local steps get stuck more easily in high scoring areas reducing convergence and mixing but as compensation more moves can be performed in the same computational time. We can balance the two types of permutation moves to benefit from the positive aspects of both and improve the overall convergence. In particular we again weight them to keep the average number of nodes to rescore down to about 4 .

# 4.8 Combining moves 

The partition and permutation neighbourhoods could be combined into a single larger neighbourhood to sample uniformly from (including the current point). For simplicity, we sample each move type with a fixed probability.

## 5. Partition MCMC with edge reversal

In the edge reversal move of Grzegorczyk and Husmeier (2008), new parent sets of the two nodes connected by the edge selected for reversal are also sampled. Since they are sampled according to their score, higher scoring DAGs are proposed more often, and the chain moves more quickly. However, the move is non ergodic, and needs to be built on an underlying irreducible framework like structure MCMC, which was the choice in Grzegorczyk and Husmeier (2008).

Since partition MCMC offers an alternative to structure, it can be used as the underlying MCMC method instead. A DAG is simply sampled from the current labelled partition according to the list of scores, the new edge reversal move from that DAG is performed exactly as in Grzegorczyk and Husmeier (2008), and the proposed DAG is accepted with the same probability. If accepted, the new DAG is mapped to its labelled partition, which is then used for further partition MCMC steps. Since the starting DAG is sampled from the current partition, the relative scores of the start and end partition cancel (like the steps in the new edge reversal move) and we need no further correction.

Explicitly, the transition probability from $\Lambda$ to $\Lambda^{\prime}$ through the DAGs $\mathcal{G} \in \Lambda$ and $\mathcal{G}^{\prime} \in \Lambda^{\prime}$ is

$$
K_{\mathcal{G}^{\prime} \mid \mathcal{G}}\left(\Lambda^{\prime} \mid \Lambda\right)=\frac{P(\mathcal{G} \mid D)}{P(\Lambda \mid D)} K^{\triangleright}\left(\mathcal{G}^{\prime} \mid \mathcal{G}\right)
$$

where the first term is the probability of sampling a DAG from the partition with normalisation as in (3) and $K^{\triangleright}\left(\mathcal{G}^{\prime} \mid \mathcal{G}\right)$ is the transition probability of the edge reversal move in Grzegorczyk and Husmeier (2008) from $\mathcal{G}$ to $\mathcal{G}^{\prime}$. Since that move satisfies detailed balance

$$
\frac{P\left(\mathcal{G}^{\prime} \mid D\right)}{P(\mathcal{G} \mid D)}=\frac{K^{\triangleright}\left(\mathcal{G}^{\prime} \mid \mathcal{G}\right)}{K^{\triangleright}\left(\mathcal{G} \mid \mathcal{G}^{\prime}\right)}
$$

substituting into (5) leads directly to

$$
\frac{K_{\mathcal{G}^{\prime} \mid \mathcal{G}}\left(\Lambda^{\prime} \mid \Lambda\right)}{K_{\mathcal{G} \mid \mathcal{G}^{\prime}}\left(\Lambda \mid \Lambda^{\prime}\right)}=\frac{P\left(\Lambda^{\prime} \mid D\right)}{P(\Lambda \mid D)}
$$

so that detailed balance holds for the edge reversal move inside partition MCMC when the DAG is sampled from the current labelled partition.

Finally we need to consider the possibility that there is more than one path between partitions so that

$$
K\left(\Lambda^{\prime} \mid \Lambda\right)=\sum_{\mathcal{G}, \mathcal{G}^{\prime}} K_{\mathcal{G}^{\prime} \mid \mathcal{G}}\left(\Lambda^{\prime} \mid \Lambda\right)
$$

is the total transition probability between the two partitions. Detailed balance

$$
P(\Lambda \mid D) K\left(\Lambda^{\prime} \mid \Lambda\right)=K\left(\Lambda \mid \Lambda^{\prime}\right) P\left(\Lambda^{\prime} \mid D\right)
$$

follows from (6), rearranged and summed.
The computational expense of an edge reversal move involves examining the possible parent sets four times. Namely, for both nodes attached to the edge which is reversed and for both the forward and backward move. It therefore has roughly the same computational cost as a partition MCMC move. However, if the move is accepted, the entire new partition needs to be scored from scratch by rescoring all the nodes. Therefore a relative cost of approximately $\frac{n}{4}$ is added to each accepted move, slightly reducing the length of the chain compared to standard partition MCMC.

# 6. Conclusions 

As demonstrated in Appendix A, partition MCMC allows DAGs to be sampled from the posterior much more efficiently than standard structure MCMC, without the bias of order MCMC (Friedman and Koller, 2003). The current state of the art edge reversal move of Grzegorczyk and Husmeier (2008) can be built into the partition sampler, improving on the convergence of their algorithm which required an underlying structure MCMC. Partitions are a way of putting MCMC on DAGs in a more natural mathematical framework, where the algorithm acts on their combinatorial representation. This representation may provide a means to define distances alternative to the SHD via moves in the space of partitions. As such, partition MCMC opens up new possibilities. Here we chose some simple moves to

demonstrate the idea, but many more could be defined and the choice optimised, maybe even adaptively depending on the score landscape. Structure MCMC on the other hand is a very mature methodology and therefore highly optimised over the years, while it is hard to envisage simple modifications of the edge reversal move of Grzegorczyk and Husmeier (2008). The combinatorial approach we present, being novel, may offer wider scope for improvement.

With the aim of inferring a single Bayesian network from scarce data, Elidan (2011) suggested an adaptation of structural EM based on bootstrap aggregating or bagging (Efron, 1979; Breiman, 1996). The focus here is instead on sampling from the posterior, in order to enable Bayesian model averaging, for example to estimate posterior probabilities of given structural features. As noted by Friedman et al. (1999), an approximation to Bayesian estimation can be obtained from the bootstrap approach. However, the quality of the estimates decreases when moving away from the mode. In other words, the structure set obtained from the bootstrap samples provides a distribution of the maximum likelihood estimator and as such does not lead to an adequate description of the posterior. Typically the maximal likelihood search is performed in the structure space, but a more natural approach would be to use the order or partition space as we discuss in Appendix B. However the complexity of such a search is the same as sampling from the posterior. Hence the bagging approximation can be avoided since partition MCMC provides access to the full posterior.

In Appendix A we look at example of densely connected graphs with up to 20 nodes. From the complexity arguments also discussed in Appendix B, fixing the computational cost we can increase the number of nodes while decreasing the limit on the number of parents. For example, graphs with 20 nodes and no parent limit would be comparable to graphs with 100 nodes with up to 2 or 3 parents each.

In some cases some of the structural features of the domain under study may be known from previous studies or expert knowledge. It is then useful to include prior information in the learning process, as suggested for example by Mukherjee and Speed (2008); Werhli and Husmeier (2007). Modular priors, such as on edges, can be easily accounted for in partition MCMC, order or edge reversal. Non modular priors could be included in structure MCMC (Mukherjee and Speed, 2008), but the slow convergence of the algorithm makes this of little practical interest for domains of moderate size, therefore they would most naturally be corrected for by means of importance sampling.

The idea behind partition MCMC is analogous to order MCMC which may be seen as an elegant solution to the somewhat different problem of sampling triangular matrices. By simply enforcing the chain to respect the combinatorial structure of DAGs via the partitions, we can now solve the problem of interest. Alternatively, one could wish to sample CPDAGs, in which case partition MCMC would still be solving slightly the wrong problem. Madigan et al. (1996) proposed a method to sample essential graphs (or CPDAGs) as an extension of structure MCMC, which can be sped up following the approach of Peña (2007) for the uniform case. Recent improvements also allow the uniform sampling of large sparse essential graphs (He et al., 2013) However, as discussed by Kuipers and Moffa (2015), the convergence on CPDAGs is notably slower than for DAGs, and at present no better methods like edge reversal (Grzegorczyk and Husmeier, 2008) or partition MCMC are available for the space of CPDAGs. Moreover, the overcounting of CPDAGs when working on DAGs instead is

bound by a low constant and is approximately 4 , so that rejection or importance sampling should be preferable when combined with an efficient method for DAGs. For example one could try to approximately evaluate feature prevalence in the essential graph space following the ideas of Ellis and Wong (2008). Namely, assuming each essential graph has a different score, and since equivalent DAGs necessarily have the same score, one would only keep a single copy of any equally scoring DAGs.

In contrast the overcounting of lower triangular matrices compared to DAGs grows exponentially, explaining the difficulties encountered when employing importance sampling to correct for the bias of order MCMC. With an implicit assumption that such a correction via importance sampling is possible, there has been work to improve order MCMC by working on partial orders (Niinimäki et al., 2011) or sampling directly on the space of orders using dynamic programming (Koivisto and Sood, 2004). Currently, an improved dynamic programming approach to order MCMC has been proposed (He et al., 2015) with approximate bias removal following the work of Ellis and Wong (2008). Of course, none of these approaches can sample DAGs from the posterior as with our partition MCMC approach. However trying to build the dynamic programming framework on the space of partitions rather than orders may be an interesting direction to explore as a possible way to sample DAGs correctly and efficiently.

# Appendix A. Comparison of the different MCMC methods 

The standard set of moves through the space of DAGs is to change one edge at a time (Madigan and York, 1995; Giudici and Castelo, 2003). Which edges can be added, deleted or reversed can be calculated with the help of the incidence and ancestor matrices. For example each nonzero entry in the incidence matrix can be set to 0 to delete an edge, giving the neighbouring graphs with one edge fewer. Edges cannot be added to ancestors, as this would create a cycle, or to where an edge already exists. The neighbours with one edge more can thus be easily found. Finally, edge reversal can be thought of as a particular two step move of deleting an edge and adding it back in the opposite direction. Appropriately multiplying the ancestor and incidence matrices, provides the nondirect ancestors. Reversing the edge to any of them would create a cycle. The neighbours with an edge reversed are then derived from the remaining nonzero entries of the incidence matrix.

Given the ancestor and incidence matrices, calculating the neighbourhood is $O\left(n^{2}\right)$ for the edge additions and $O\left(n^{3}\right)$ for the edge reversals. (We ignore possible faster matrix multiplication algorithms.) Once a new DAG is sampled from the neighbourhood, the ancestor matrix can be updated in $O\left(n^{2}\right)$ (Giudici and Castelo, 2003) and the new neighbourhood size needs to be calculated before accepting the move.

We work with the BGe score (Geiger and Heckerman, 1994; Heckerman and Geiger, 1995; Geiger and Heckerman, 2002), corrected as in Consonni and Rocca (2012); Kuipers et al. (2014) and sped up following Kuipers et al. (2014). Since this score is modular, each node is scored separately from the others just depending on its parent set. With edge addition or deletion, only one node needs to be rescored while two are rescored with an edge reversal. The scoring involves finding the determinant of a matrix of the size of the parent set with a complexity up to $K^{3}$ when the size of the parents sets are limited to $K$.

Since here we limit the parent sets, the scoring may be quicker than calculating the neighbourhoods and there have been proposals to improve the speed of the chain by avoiding to explicitly calculate the neighbourhood at each step. In an approach designed for uniform sampling (Melançon et al., 2001) one can simply swap an element (from 0 to 1 or back) of the incidence matrix chosen uniformly. Moves which would create a cycle are rejected and can be checked in a time between $O(n)$ and $O\left(n^{2}\right)$ with a typical $O(n \log (n))$ behaviour (Alon and Rodeh, 1978) which here would depend on the higher scoring DAGs. A reversal move can also be introduced (Melançon and Philippe, 2004). Alternatively, Giudici and Castelo (2003) keep track of the ancestor matrix which allows them to check whether the moves are legal in $O(n)$. Only when moves are accepted based on the score does the ancestor matrix need to be updated at a cost $O\left(n^{2}\right)$. Of course convergence is slowed down by not calculating the neighbourhood exactly but the idea is that this is more than compensated for by speeding up the moves.

Since the exact computation time depends on many factors we employ the following simplifications in our comparison. We find the number of steps of standard structure MCMC that have approximately the same computational time as the alternatives detailed below and then run the chains $n$ times longer. Although the examples are far from the asymptotic limit where edge reversal is more expensive than the other moves, this factor is chosen is to compensate for possible speed ups that could be implemented. With the compensation, the unavoidable time spent scoring DAGs is comparable to the run time of the alternatives, representing the limit of any speed ups.

Both Friedman and Koller (2003) and Grzegorczyk and Husmeier (2008) suggested a more constant time factor $\approx 10$ between structure and alternative steps. Although it may depend heavily on the exact implementation, it wouldn't be in line with asymptotic reasoning but for $n \approx 10$ would be roughly in line with our implementation. Our comparison however would become more favourable to structure MCMC as $n$ increases.

The standard move in order MCMC consists of swapping any two elements in the permutation of node labels (so the chain takes less than $n$ steps to become irreducible). However, it means you need to rescore the nodes selected and all the nodes inbetween them (on average $\frac{n+4}{3}$ nodes). Instead one could swap adjacent elements and only need to rescore 2 nodes (making the steps quicker) but the chain takes order $n^{2}$ steps to become irreducible. We employ a mixture of both moves with the probability of each chosen so that they both take the same computational time. Since the standard move includes the other, it should be chosen with probability $6 n /\left(n^{2}+10 n-24\right)$ to achieve this, meaning that around 4 nodes need to be rescored on average. This improves the behaviour of order MCMC and makes the time complexity of each step independent of $n$. A small $1 \%$ probability of staying still is included to ensure aperiodicity of the chain.

For partition MCMC we choose a partition move to a permutation move with a ratio of $3: 2$ and inside each class we choose the larger move with $6 n /\left(n^{2}+10 n-24\right)$ so that on average about 3 nodes and one partition element (typically a further node) are rescored at each step. Likewise a small $1 \%$ probability of staying still is included.

The edge reversal move of Grzegorczyk and Husmeier (2008) is not irreducible by itself and it needs to be incorporated into an irreducible scheme like structure MCMC. Since for the edge reversal move we need to score 4 lots of possible parent sets, 2 for the forward move and 2 for the reverse move, this takes a similar time on average to each partition

![img-3.jpeg](img-3.jpeg)

Figure 4: A run of 50 thousand steps of structure MCMC for the simulated data with different seeds starting at the empty DAG. In the top plots edge reversals are allowed and we seem to hover around the maximally scoring DAG (red dotted line). In the bottom plots, edge reversal is excluded and we do not even approach the maximal scoring DAG.

MCMC move. For the comparison we fix the probability of the new edge reversal move to $7 / 100 \approx 1 / 15$ as in Grzegorczyk and Husmeier (2008) and use the artificial timing of the structure steps to set the total time to match partition MCMC. Note that the edge reversal move requires knowledge of the descendants matrix once the edge to be reversed has been removed. This is obtained in a naive matrix multiplication implementation of order $n^{4}$ compared to the order $n^{K}$ of scoring and sampling parent sets. Despite the complexity, the actual computational time was negligible in our examples and faster than a less complex algorithm, but this step could be sped up for larger graphs.

When the edge reversal move of Grzegorczyk and Husmeier (2008) is combined with partition MCMC instead we keep the probability of choosing the edge reversal move at $7 / 100$. If such a move is accepted though we need to rescore all the nodes for the next partition step which slows down the implementation and leads to marginally shorter chains.

# A. 1 Simulated example 

We generated 100 observations from the DAG in Figure 1 with 5 nodes and no maximum number of parents $(K=4)$. The data were generated from a normal with regression on the parents with coefficient 2 .

First we ran standard structure MCMC (Madigan and York, 1995) for 50 thousand steps recording a thousand evenly spaced DAGs. Figure 4 shows trace plots from two different seeds. The highest score of the DAGs covered in the chain is plotted as the green solid line which is placed at the top of each graph. If visible, the score of the DAG used to generate the data is plotted as the red dotted line. In the lower plots we excluded the possibility

![img-4.jpeg](img-4.jpeg)

Figure 5: A run of 40 thousand steps of structure MCMC with the new edge reversal move of Grzegorczyk and Husmeier (2008) and different seeds. The edge move is selected with probability 0.07 . The performance seems the same as standard structure MCMC, but with a large improvement when standard edge reversals are excluded as shown by the bottom rows.
of edge reversal. Although, as discussed above, one can speed up the chain without edge reversal, as can be seen in the plots the poor performance of the chain makes this a false economy since the level of the best DAG is not reached. The large improvement with edge reversal is detailed in Giudici and Castelo (2003) and in the following subsections we no longer consider the case without it.

When including the edge reversal move of Grzegorczyk and Husmeier (2008) we run the chain for 40 thousand steps. In this example we ran structure MCMC with and without the standard edge reversal move. In the top plots of Figure 5 there is hardly any difference from those in Figure 4 other than maybe a slight worsening due to a shorter chain. The new edge reversal vastly improves the algorithm without a standard edge reversal, as can be seen by comparing the bottom plots, but this is not surprising given the addition of some type of edge reversal.

Removing the standard edge reversal could lead to a speed up of structure, but a degradation in the performance is still evident when comparing the two rows of Figure 5. Since the new edge reversal constitutes the computationally most expensive part, any speed up of the structure part would be damped and unlikely to be worth considering in general situations.

For the same simulated data, we ran partition MCMC. The time needed for 13 thousand steps (dividing by 5) of structure MCMC allows for approximately 10 thousand steps of partition MCMC. Some trace plots are given in Figure 6 where the top plots show the score of the current partition, while the bottom plots show the score of a DAG sampled from that

![img-5.jpeg](img-5.jpeg)

Figure 6: Run of 10 thousand steps of partition MCMC with different seeds on simulated data from a DAG with 5 nodes.
![img-6.jpeg](img-6.jpeg)

Figure 7: Run of 9 thousand steps of partition MCMC including the edge reversal move of Grzegorczyk and Husmeier (2008) with different seeds on simulated data from a DAG with 5 nodes.
partition. When comparing the bottom plots to the top plots of Figure 4 we see similar behaviour, with what looks like slower convergence of partition due to the shorter chain.

Incorporating the new edge reversal move, we can run around 9 thousand steps in the same time with the results in Figure 7, which are similar.

![img-7.jpeg](img-7.jpeg)

Figure 8: Run of 20 thousand steps of order MCMC with different seeds for simulated data from a DAG with 5 nodes.

Finally we run order MCMC. In the plots in Figure 8, the top line is in the space of orders with the scores of the entire order while the bottom lines are the score of DAGs sampled from each order at each step. There are now 8 orders the DAG in Figure 1 is compatible with and we draw red dotted lines for the total scores of each of those orders. The performance is much better than structure even with the edge reversal move of Grzegorczyk and Husmeier (2008). Of course order MCMC is working in a much bigger and overlapping space so we would expect better performance.

# A. 2 Boston housing data 

A dataset used as a benchmark is the Boston Housing data from the UCI repository (Lichman, 2013). It consists of $N=506$ observations from $n=14$ continuous variables. Both Friedman and Koller (2003) and Grzegorczyk and Husmeier (2008) run their algorithms on the Boston Housing data in order to analyse convergence with respect to structure MCMC. Here we also use the same dataset to compare the performance of the different algorithms we consider. We cannot compare directly to the results in Friedman and Koller (2003); Grzegorczyk and Husmeier (2008) since their implementation is not available and moreover they are most likely based on one of the incorrect versions of the BGe score (Geiger and Heckerman, 1994; Heckerman and Geiger, 1995; Geiger and Heckerman, 2002), which has only recently been corrected (Consonni and Rocca, 2012; Kuipers et al., 2014).

We first run one million steps of structure MCMC with different seeds. Trace plots are shown in Figure 9. Even with such a long run, the chains have not converged.

When implementing partition MCMC, dividing by $n=14$ and adjusting the times, we run the chain for 60 thousand steps as opposed to the 1 million we ran for structure MCMC. Since each partition MCMC step takes a very similar time to an order MCMC step or the edge reversal move of Grzegorczyk and Husmeier (2008) we are penalising partition

![img-8.jpeg](img-8.jpeg)

Figure 9: A run of 1 million steps of structure MCMC with different seeds for the Boston Housing data. As can be seen the different runs arrive at different plateaux, some of which are very far away from the global maximum set at 0 .

MCMC by a factor of $n=14$ which is comparable to the constant factor of 10 employed by Friedman and Koller (2003); Grzegorczyk and Husmeier (2008). When looking at the trace plots in Figure 10 we can see much better performance than observed for structure MCMC in Figure 9. Most of the runs seem to arrive close to where the global maximum resides, which is set to 0 in the graphs. The remaining run and the deviations from the plateaux give us an idea of the convergence time.

Convergence of structure MCMC is well known to become rather slow as the graphs get larger and the score landscape more peaked. Partition MCMC seems a simple method to improve the convergence by combining many DAGs in the space of labelled partitions. Previous approaches to improve structure MCMC such as order MCMC (Friedman and Koller, 2003) and the edge reversal of Grzegorczyk and Husmeier (2008) also relied on the combination of DAGs into larger classes.

The difference between pure structure MCMC and its combination with the edge reversal move of Grzegorczyk and Husmeier (2008) was not evident for the previous simulated example, since the space is quite small and the chains are already quite long. Looking at the behaviour of the algorithms on the Boston Housing data instead highlights the improvement. Now we run the chains for half a million steps and plot the results in Figure 11. None of the runs are as far away as the worst examples in Figure 9 though one a run still behaves similarly to the other examples of Figure 9. Two of the examples in Figure 11 are around the global maximum however. When comparing to partition MCMC, local exploration seems better from the longer runs, but correspondingly long times are spent around each horizontal level. The latter is due of course to the structure moves but the edge reversal moves increase the chance of large jumps to new levels (and hence finding the global maximum) though they are still rarely successful.

![img-9.jpeg](img-9.jpeg)

Figure 10: A run of 60 thousand steps of partition MCMC with different seeds for the Boston Housing data. While the first remains some distance away from the global maximum set at 0 , the other runs approach a plateau near or at the maximum itself.
![img-10.jpeg](img-10.jpeg)

Figure 11: A run of half a million steps of the new edge reversal MCMC with different seeds for the Boston Housing data. The top two reach the region of the global maximum, while the others are some distance away.

![img-11.jpeg](img-11.jpeg)

Figure 12: A run of 56 thousand steps of partition MCMC with edge reversal with different seeds for the Boston Housing data. The runs on the right seem to reach the global maximum set at 0 , while the first plot remains just a little lower.

Combining the edge reversal with partition MCMC instead we run chains of 56 thousand steps as opposed to the 60 thousand before. Of course the exact timing of each run depends on the acceptance probability and can be quite variable. Trace plots are shown in Figure 12 and they seem to combine the best features of Figures 10 and 11.

For comparison, we also run order MCMC for 150 thousand steps, for which trace plots appear in Figure 13. The performance in finding the maximum is the best, but a relative score region between -10 and -14 seems overly represented, which may be due to the bias.

To compare the ability of the algorithms to discover the maximum, the four example trace plots presented do not suffice so we run each of the better unbiased methods with 100 different seeds. A density plot of the maximal scores they discover is presented in Figure 14. Edge reversal finds the maximum most often, partition MCMC the least. Partition MCMC however finds a large range of possible values as opposed to the handful found by edge reversal suggesting that the edge reversal chains follow more similar paths through the score landscape. Combining partition MCMC with edge reversal provides intermediate behaviour.

# A. 3 Simulation from a more connected DAG 

Keeping $n=14$ we move to a simulation of a more connected DAG with $K=6$. We sample uniformly a lower triangular $(0,1)$ matrix and remove elements at random from any column with more than $K$ non-zero entries until only $K$ remain. We then pick a random permutation of the nodes and use the resulting DAG to generate $N=500$ observations following a normal distribution with regression on the parents. So far the setup is like the Boston Housing data, but with a more connected underlying DAG. Again we run the

![img-12.jpeg](img-12.jpeg)

Figure 13: A run of 150 thousand steps of order MCMC with different seeds for the Boston Housing data. All the runs reach the global maximum at 0 , but there seems to be a strong propensity to explore a region between -10 and -14 .
![img-13.jpeg](img-13.jpeg)

Figure 14: Density plots of the maximal score found by partition MCMC (solid blue), structure with edge reversal (dashed orange) and partition with edge reversal (dotted purple) for the Boston Housing data.

![img-14.jpeg](img-14.jpeg)

Figure 15: Density plots of the maximal score found by partition MCMC (solid blue), structure with edge reversal (dashed orange) and partition with edge reversal (dotted purple) for simulated data on 14 nodes. In the inset, we zoom in the region around 0 with a narrower convolving function.
different methods with 100 seeds and keep track of the maximal scores discovered by the chains. The density plot of the maximal scores is an imperfect measure of how good each method is, but indicative. Keeping half a million steps for structure with the new edge reversal move of Grzegorczyk and Husmeier (2008), instead of timing the structure steps we assume they take negligible time and run partition MCMC for 0.07 times the number of steps, or 35 thousand. The combined partition with edge reversal is run for 32 thousand steps each time. The resulting density of maxima is plotted in Figure 15. Despite the slight chain length advantage for edge reversal, it performs worse than partition MCMC with a large tail far away from the global maximum but with a smaller spread around the maximum itself. The behaviour is a reflection of the relatively small number of different score regions edge reversal discovers compared to the wider spread of partition MCMC. The clear favourite in Figure 15 is the combination of partition MCMC with edge reversal. These results suggest that the combination would be the preferred algorithm for inference on DAGs as the size and connectivity increases.

# A. 4 Larger simulations 

When moving to larger graphs with $n=18$ and $n=20$ with $N=200$ observations and a limit of $K=5$ on the parents we observe the same improvement by combining edge reversal with partition MCMC as shown in Figure 16.

![img-15.jpeg](img-15.jpeg)

Figure 16: Density plots of the maximal score found by partition MCMC (solid blue), structure with edge reversal (dashed orange) and partition with edge reversal (dotted purple) for simulated data on 18 nodes (left) and 20 nodes (right).

# Appendix B. MAP discovery 

Although we focus on sampling from the posterior, MCMC methods can be adapted to perform a stochastic search for maximum a posteriori (MAP) graphs, or, by replacing the score function appropriately, for (penalized) maximum likelihood discovery.

A common approach for structure search is greedy hill-climbing, but it has the drawback of stopping in the first local maximum, where MCMC schemes may get only temporarily trapped, as for example in the plateaux visible for the $n=14$ Boston Housing example in Figure 9 .

The complexity of a structure based greedy hill-climbing approach involves testing $O\left(n^{2}\right)$ neighbours at each step to find and move to the best one. Each neighbour must be scored, which with a fixed limit $K$ on the number of parents is $O(1)$. After each step, the neighbourhood can be updated in $O\left(n^{2}\right)$ using the ideas of Giudici and Castelo (2003). The structure moves take $O\left(n^{2}\right)$ steps to move through the DAG space leading to a complexity of $O\left(n^{4}\right)$ to find each local optimum. The overall complexity may be higher if the number of restarts required also grows with $n$.

A stochastic search based on structure MCMC, using for example simulated annealing, has a complexity of approximately $O\left(n^{5} \ln n\right)$ (Kuipers and Moffa, 2015) which may grow further if the peakiness of the score landscape likewise grows with $n$. For practical implementations the coefficients of the complexities play a large role. Based on the order of complexity though, hill-climbing appears to have the edge; even more so with the improvements in Tsamardinos et al. (2006) in the context of hybrid methods.

For moderate sized problems, as with 14 nodes in Figure 9, structure MCMC gets trapped in low-scoring local maxima, suggesting that greedy searches would also suffer for larger graphs. Instead one can search directly in the order or partition space. The bias due to working in the space of orders rather than the DAG space is not of great concern for MAP learning. Therefore we start with the simpler permutation space of node orderings $\prec$, of size $n$ !. Each order gets assigned the maximal score of all the DAGs consistent with

that node ordering

$$
Q(\prec \mid D)=\max _{G \in \prec} P(G \mid D)^{\gamma}
$$

Instead of hill-climbing through the orders, one can perform a stochastic search with a symmetric MCMC through the space of permutations with acceptance probability

$$
\rho=\min \left\{1, \frac{Q(\prec^{\prime} \mid D)^{\gamma}}{Q(\prec \mid D)^{\gamma}}\right\}
$$

Throughout the chain the algorithm can keep track of the maximal ordering and hence the maximal DAG discovered. The power $\gamma$ flattens or sharpens the score landscape and can be tuned to help find the maximum as quickly as possible. Increasing $\gamma$ as the chain is run corresponds to simulated annealing.

From a complexity perspective, if each move swaps two nodes at a time, it takes $n$ steps for the chain over the space of permutations to become irreducible. On this irreducible scale of $n$ steps, we assume that the exponential convergence of the MCMC has a rate which is asymptotically independent of $n$. The chain needs to converge at least to the scale of the inverse size of the space. To get to $\sim \frac{1}{n!}$ suggests that at least $n \ln n$ irreducible rounds or $O\left(n^{2} \ln n\right)$ MCMC steps are required for good convergence and maximum discovery properties. The complexity of each MCMC step when carefully weighted as in Appendix A is $O\left(n^{K}\right)$ leading to an overall behaviour of at least $O\left(n^{K+2} \ln n\right)$. Order and partition MCMC also have the same complexity. Of course the coefficients may be very different especially due to the possibility of tuning $\gamma$ to speed up the MAP discovery.

For a greedy hill-climbing order search, at each step $O\left(n^{2}\right)$ neighbouring orders are examined. Moving through this neighbourhood efficiently by only swapping adjacent elements at each step, the cost of scoring each neighbour is still $O\left(n^{K}\right)$. Moving through the order space requires $O(n)$ steps leading to a minimum complexity of $O\left(n^{K+3}\right)$ with possible increases depending on how the number of restarts relates to $n$.

The stochastic search may have lower complexity than greedy hill-climbing on orders, and can cope with an uneven score landscape, but its main advantage is the possibility of providing an indication of the confidence that the maximum is the global one.

Imagine the search uncovers a maximally scoring DAG which belongs to a single order. To test whether this local maximum may be the global one, a stochastic search is run $Z$ times, discovering the candidate global maximum on $z$ of those runs. The probability of discovering the maximum on each run would be estimated as $p^{\star}=\frac{z}{Z}$. Since the search, once converged, is sampling proportionally to $Q^{\gamma}$, it is more likely to hit higher scoring graphs, if they exist. The probability of doing so on each run should be greater than $p^{\star}$. The probability of missing any higher scoring graphs on any of the runs should be less than about $\left(1-p^{\star}\right)^{Z}$. By modifing $\gamma, Z$ and the lengths of the runs, we can reduce the bound to any acceptably low value.

If the candidate maximum happens to belong to $W$ orders the same reasoning leads to a weaker bound of $\left(1-\frac{z}{W Z}\right)^{Z}$. Alternatively, one can can turn to the partition space with a unique representation of each DAG, though there may still be equivalent DAGs in other partitions.
