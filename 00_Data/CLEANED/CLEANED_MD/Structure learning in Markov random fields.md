# Best-Choice Edge Grafting for Efficient Structure Learning of Markov Random Fields 

Walid Chaabene<br>Department of Computer Science Virginia Tech

Bert Huang<br>Department of Computer Science<br>Virginia Tech


#### Abstract

Incremental methods for structure learning of pairwise Markov random fields (MRFs), such as grafting, improve scalability by avoiding inference over the entire feature space in each optimization step. Instead, inference is performed over an incrementally grown active set of features. In this paper, we address key computational bottlenecks that current incremental techniques still suffer by introducing best-choice edge grafting, an incremental, structured method that activates edges as groups of features in a streaming setting. The method uses a reservoir of edges that satisfy an activation condition, approximating the search for the optimal edge to activate. It also reorganizes the search space using search-history and structure heuristics. Experiments show a significant speedup for structure learning and a controllable trade-off between the speed and quality of learning.


## 1 Introduction

A powerful family of approaches for learning the structure of Markov random fields (MRFs) is based on minimizing $\ell_{1}$-regularized scores such as the negative log likelihood [2] of a fully connected MRF. The $\ell_{1}$ regularization reduces the parameters of irrelevant edges to zero. The main challenge when using these methods is that, for large MRFs, the feature space becomes extremely large and causes an overwhelming computational cost. Active-set methods, such as grafting [10, 15, 18], were introduced to promote more scalability. Despite the benefits of active-set learning, grafting retains significant computational costs: As a mandatory pre-learning step, grafting computes sufficient statistics of all possible variable pairs to enable greedy activation tests on the entire search space, and each iteration of grafting requires a search over the large combinatorial space of all possible edges.
This paper introduces best-choice edge grafting, an active-set method that activates edges in a streaming fashion as groups of parameters. The method is agnostic to the underlying inference method. We derive an edge-activation test using a structured group- $\ell_{1}$ learning objective. Structure learning is performed in a priority order: Edges are assigned different search priorities. We use a combination of random sampling and a min-heap priority queue [16] to efficiently explore the prioritized search space. The method performs "online" edge activation using a control sample of candidate edges stored in a limited-memory reservoir. Search priorities are updated based on the search history and structural information derived from the partially constructed MRF structure learned so far. These strategies allow on-demand computation of sufficient statistics for edges that are likely to be activated, which eliminates the heavy computation of grafting's pre-learning phase. Best-choice edge grafting can start-and often finish—learning well before grafting is able to begin learning. We also introduce a trade-off parameter to balance the speed of learning and the quality of learned MRFs. Our experiments show that best-choice edge grafting scales better to large datasets than grafting. Synthetic experiments show that the proposed method performs well at recovering the true structure, while real data experiments show that we learn high-quality MRFs from large and diverse datasets.

# 2 Background and Preliminaries 

Throughout this paper, we consider the case of log-linear, pairwise Markov random fields (MRFs). Based on a given MRF structure, the probability of a set of variables $x=\left\{x_{1}, \ldots, x_{n}\right\}$ is $p_{w}(x)=$ $\frac{1}{Z(w)} \prod_{c \in C} \phi_{c}(x ; w)$, where $Z(w)$ is a normalizing partition function $Z(w)=\sum_{x} \prod_{c \in C} \phi_{c}(x ; w)$, and $\phi$ is a clique potential function $\phi_{c}(x ; w)=\exp \left(\sum_{k \in c} w_{k}^{\top} f_{k}(x)\right)$. The set $C$ contains sets of indices representing cliques and variables, and $f_{k}(x)$ are feature functions often defined as indicator functions. In the case of pairwise Markov random fields, a clique can refer to either a node or an edge. A pairwise MRF is associated with an undirected graph $G(V, E)$, where $V$ is the set of $n$ nodes corresponding to variables, and $E$ is the set of edges corresponding to pairwise cliques. The factorization for a pairwise MRF is $p_{w}(x)=\frac{1}{Z(w)} \prod_{i \in V} \phi_{i}(x ; w) \prod_{(i, j) \in E} \phi_{i j}(x ; w)$.

### 2.1 Parameter Learning Through $\ell_{1}$-Regularized Likelihood

Given a set of data $X=\left\{x^{(m)}\right\}_{m=1 \ldots N}$, the likelihood is expressed as $l(w)=\prod_{m=1}^{N} p_{w}\left(x^{(m)}\right)$. We formulate learning as a minimization of a scaled negative log likelihood $L(w)$, where $L(w)=$ $-\frac{1}{N} \sum_{m=1}^{N} \log p_{w}\left(x^{(m)}\right)=-\frac{1}{N} \sum_{m=1}^{N}\left(w^{\top} f\left(x^{(m)}\right)\right)+\log Z(w)$, and $w$ and $f$ correspond to the vectors of $w_{k}$ and $f_{k}$, respectively. Minimizing $L(w)$ is often done using gradients. The gradient of $\log Z(W)$ with respect to the $k^{t h}$ feature is the model's expectation of the $k^{t h}$ feature function [8]: $\frac{\partial \log Z}{\partial w_{k}}=E_{w}\left[f_{k}(x)\right]=\sum_{x} p_{w}(x) f_{k}(x)$. The gradient of $L$ with respect to the $k^{t h}$ feature is

$$
\frac{\partial L}{\partial w_{k}}=-\frac{1}{N} \sum_{m=1}^{N} f_{k}\left(x^{(m)}\right)+E_{w}\left[f_{k}(x)\right]=E_{w}\left[f_{k}(x)\right]-E_{D}\left[f_{k}(x)\right]:=\delta_{k} L
$$

In other words, the feature-wise gradient $\delta_{k} L$ is the error between the data expectation $E_{D}$ and the model expectation $E_{w}$ of $f_{k}(x)$. The goal of learning can be seen as minimizing that error. To avoid over-fitting and to promote sparsity of the learned weights and of the learned Markov network, classical methods add an $\ell_{1}$ regularization and solve $\min _{w} L(w)+\lambda\|w\|_{1}$.

### 2.2 Learning Challenges

Learning with the gradient in Eq. (1) is prohibitively expensive for three reasons: (i) The expectation requires computing sufficient statistics for every unary and pairwise feature, which is especially expensive for large datasets. (ii) The classical $\ell_{1}$ formulation ignores the structure of MRFs and treats parameters independently. This treatment dismisses the importance of local consistencies and the power of Markov independence encoded in structure. Finally, (iii) inference of the model expectations $E_{w}\left[f_{k}(x)\right]$ is generally \#P-complete [8]. Existing techniques focus on minimizing the cost of the inference subroutine (iii). Active-set methods allow the learning optimization to compute inference over simpler MRFs. And various approximate inference methods efficiently approximate the expectations, such as loopy belief propagation and its variants [6, 9, 11, 12, 14, 17] and pseudolikelihood [3]. Group sparsity methods [5] can be straightforwardly adapted to address the structural coherence issue (ii). Our approach extends these methods of handling issues (ii) and (iii) while also addressing the critical bottleneck of sufficient statistic computation (i) and additional bottlenecks in active-set algorithms.

### 2.3 Grafting

Grafting and its variants $[10,15,18]$ are active-set learning approaches that alternate between two primary operations: (1) They learn parameters for an active set $S$ of features (e.g., using a sub-gradient method); and (2) they expand the active set by activating one feature using a gradient test based on the Karush-Kuhn-Tucker (KKT) conditions of the $\ell_{1}$-regularized objective. Grafting converges when the activation step does not find any new feature or when a predefined maximum number of features $f_{\max }$ is reached. Grafting has a startup bottleneck with an $O\left(n^{2} N s_{\max }^{2}\right)$ computational cost to compute the sufficient statistics for each feature, for a system of $n$ variables and a maximum number of states $s_{\max }$. Grafting also involves an exhaustive $O\left(n^{2} s_{\max }^{2}\right)$-time search to activate each feature. These bottlenecks translate to poor scalability for large systems and datasets.
Although grafting is fairly suitable for learning MRFs, it does not consider structural information or different clique-memberships of features. Furthermore, while grafting avoids expensive inference, it

still requires various quadratic-cost operations: one that scales with the typically large amount of data and one that must be repeated each iteration of the main learning loop.

# 2.4 Group Sparsity and Edge Grafting 

Using $\ell_{1}$ regularization promotes sparsity uniformly across all parameters. Different regularizers can instead enforce structured sparsity [5]. A similar approach leads to a natural extension of grafting for MRF structure learning. We refer to this variation as edge grafting, as it activates edges instead of features. Accordingly, we define the search set $F$ and the active set $S$ respectively as sets of inactive and active edges. To include structural information in the likelihood function, we use group- $\ell_{1}$ regularization. This regularization prefers parameters of each node and each edge to be homogeneous and whole edges to be sparse. We define the group- $\ell_{1}$ negative log likelihood as follows:

$$
\mathbb{L}(w)=L(w)+\sum_{g \in G} \lambda d_{g}\left\|w_{g}\right\|_{2}+\lambda_{2}\|w\|_{2}^{2}
$$

Each group $g$ contains the weights for either a node or an edge. Consequently, $w_{g}$ refers to the sub-vector containing all weights related to features of group $g$. We define $d_{g}$ as the number of states per clique. As in elastic-net methods [19], we add the $\ell_{2}$-norm to avoid some shortcomings of group- $\ell_{1}$ regularization, such as parameter imbalance and aggressive group selection. We derive a KKT optimality condition:

$$
\begin{cases}\frac{\left\|\delta_{g} L\right\|_{2}}{d_{g}}+\lambda_{2}\left\|w_{g}\right\|_{2}^{2}=0 & \text { if }\left\|w_{g}\right\|_{2} \neq 0 \\ \frac{\left\|\delta_{g} L\right\|_{2}}{d_{g}} \leq \lambda & \text { if }\left\|w_{g}\right\|_{2}=0\end{cases}
$$

where $\delta_{g} L$ is the sub-vector constructed using the entries of the gradient vector $L$ corresponding to group $g$. From this condition, we derive an edge-activation test for a given edge $e \in F$,

$$
C_{2}: s_{e}>\lambda
$$

where $s_{e}$ is the activation score representing the error between the model $\hat{p}_{w}(e)$ and the data $p_{D}(e)$ :

$$
s_{e}=\frac{1}{d_{e}}\left\|\delta_{e} L\right\|_{2}=\frac{1}{d_{e}}\left\|\hat{p}_{w}(e)-p_{D}(e)\right\|_{2}
$$

By using the group- $\ell_{1}$ regularizer and maintaining an active set of edges, edge grafting runs analogously to grafting but activates parameters for entire edge potentials. Edge-based group- $\ell_{1}$ regularization encourages structural sparsity consistent with Markov notions of variable independence.

## 3 Best-Choice Edge Grafting

Edge grafting requires computing sufficient statistics for all possible edges and searching over all possible edges at each iteration. Each of these operations costs $O\left(n^{2}\right)$ time. We propose best-choice edge grafting, a method that grafts edges in a streaming fashion using a variation of reservoir sampling [13]. This method activates edges without considering the entire search space. Best-choice edge grafting computes statistics on-demand within the learning loop, and it reorganizes the search space by assigning search priorities to edges based on search history and the structure of the partially constructed MRF graph. This reorganization helps the method test edges more likely to be relevant.

We include pseudocode for the discussed algorithms in the appendix.

### 3.1 Method Overview

Best-choice edge grafting activates edges without exhaustively computing all sufficient statistics or performing all activation tests. Instead, the approach starts activating edges by computing a small fraction of the edge sufficient statistics. A naive strategy would be to activate the first encountered edge that satisfies $C_{2}$, i.e., a "first-hit" approach. However, this approach can introduce many spurious edges. We propose an adaptive approach inspired by best-choice problems that uses a control sample of edges satisfying $C_{2}$ stored in a limited-memory reservoir $R$. By maintaining a reservoir of potential edges to activate, we increase the probability of the algorithm activating relevant edges. (See the discussion in our complexity analysis in Sec. 3.2.) Moreover, by introducing a reservoir strategy, we directly generalize both the first-hit approach and exhaustive edge grafting, which can be equivalently viewed as using size-one reservoirs and unlimited reservoirs, respectively.

A key subroutine for best-choice edge grafting selects the candidate edge with the most priority. We define a mechanism that combines random sampling with a min-heap priority queue [16] to allow fast priority-based selection that requires no quadratic-time operations under mild assumptions. At all times, the edges are grouped into prioritized edges and unseen edges. A prioritized edge is any edge whose priority is adjusted by the algorithm, and all prioritized edges are stored in the priority queue. Unseen edges are implicitly assigned a default priority score $\rho_{0}$, but they are not explicitly stored. To select the edge with maximum priority, the algorithm first examines the maximum prioritized edge from the priority queue and compares it to $\rho_{0}$. If the edge extracted from the priority queue has lower priority than $\rho_{0}$ or if the priority queue is empty, we repeatedly sample random edges until we sample one that is not already prioritized. As we show in Sec. 3.2, the probability of sampling an already prioritized edge approaches zero asymptotically as the number of variables grows.
The learning loop selects edges in order of priority score and places edges that pass the activation test into the reservoir, which retains the edges that most violate the optimality condition. Once enough edges have been seen, the algorithm selects edges to activate from the reservoir and then performs inference to update the model expectations. The priority queue and reservoir are then updated based on the newly estimated MRF structure (see Secs. 3.1.1 and 3.1.2), and the next iteration begins.
There are no quadratic-time operations within the main loop. Though there may in the worst case be $O\left(n^{2}\right)$ elements in the priority queue, each insertion, removal, or update operation costs time logarithmic in the number of stored elements, which is $O\left(\log \left(n^{2}\right)\right)=O(2 \log (n))=O(\log (n))$. This efficiency enables prioritization and management of the large search space.

# 3.1.1 Reservoir management 

Best-choice edge grafting strategically manages the reservoir to retain edges likely to be relevant. Let $A \in F$ be the unknown set of all edges that currently satisfy $C_{2}$. We construct a control sample $R \subseteq A$ from which we activate edges. Edges in the search set $F$ are initially assigned equal, default priorities $\rho_{0}$. These priorities will be adjusted based on informed heuristics. The method iterates through $F$ by extracting the highest priority edge, generating a prioritized stream of edges to test. If a tested edge satisfies $C_{2}$, it is added to $R$. Otherwise, it is ignored.
When a maximum number of edge tests $t_{\max }$ is reached, we start activating edges. To maintain a high-quality reservoir, edge activation only starts after we fill $R$ to capacity in the first edge-activation iteration. Furthermore, if $R$ reaches its capacity before $t_{\max }$ is reached, we replace the minimumscoring edge in $R$ with the newly tested edge whenever it has a higher score. We use a simple strategy to activate edges in the reservoir with high activation scores where we consider edges that have at least an above-average score. We compute the average activation score $\mu=\frac{1}{|R|} \sum_{e \in R} s_{e}$, and then we define a confidence interval for choosing edges that are likely to be relevant as $I_{\alpha}=$ $\left[\mu+\alpha\left(\max _{e \in R} s_{e}-\mu\right), \max _{e \in R} s_{e}\right]$, where $\alpha \in[0,1]$. The algorithm considers activating edges with activation scores no less than $\tau_{\alpha}=(1-\alpha) \mu+\alpha \max _{e \in R} s_{e}$. After deriving $\tau_{\alpha}$, edges are activated in a decreasing order with respect to their scores. To avoid redundant edges and to promote scale-free structure, we only activate edges that are not adjacent. Note that when $\alpha=1$, we only select the maximum-scoring edge. Reducing $\alpha$ increases the number of edges to be activated at a certain step but can also result in adding spurious edges. See the pseudocode in the appendix.
After each optimization step, edge gradients change. Therefore, scores of reservoir edges are updated, and edges that no longer satisfy $C_{2}$ are dropped from the reservoir.

### 3.1.2 Search space reorganization

Best-choice edge grafting performs search space reorganization by assigning and updating the search priority of edges in the priority queue. The aim of this reorganization is to increase the quality of the received stream of edges and the reservoir. We leverage search history and structural information.
Search history Each activation iteration, an edge with a small activation score is unlikely to satisfy $C_{2}$ in the future and is placed further toward the tail of the priority queue. We define an edge-violation offset $v_{e}=1-\frac{s_{e}}{2}$. When the activation tests fail or edges are dropped from $R$, the low-score edges are not immediately returned to the priority queue but instead are "frozen" and placed-along with their violation offsets-in a separate container $L$. When the search priority queue is emptied, we refill it by re-injecting frozen edges from $L$ with their respective violation offsets as their new priorities.

Table 1: Time complexity of different methods. The second column measures how much computation is necessary at startup. Edge grafting requires the sufficient statistics of all possible edges to do any activation, while best-choice edge grafting only computes statistics as needed. The activation-step cost is the cost to decide which edge to activate next. For reference, we include the approximate cost to approximate the expectations and gradient, which is typically linear in the size of the current active set (e.g., belief propagation or pseudolikelihood).


Partial structure information As the active set grows, so does the underlying MRF graph $G$. The resulting partial structure contains rich information about dependencies between variables. We rely on the hypothesis that graphs of real networks have a scale-free structure [1]. We promote such structure in the learned MRF graph by encouraging testing of edges incident to central nodes. We start by measuring node centrality on the partially constructed MRF graph $G$ to detect hub nodes. A degree-based node centrality $c_{i}$ for a node $i$ is the fraction of all possible neighbors $N_{i}$ it is connected to: $c_{i}=|N_{i}|/(\mid V|-1)$. We then use a centrality threshold $\bar{c}$ to identify the set of hubs $H=\{i \in V$ such that $c_{i}>\bar{c}\}$. Finally, we prioritize all edges incident to nodes in $H$ by decrementing their priorities by 1 . The total cost of updating the min-heap structure is $O(\mid H|n \log (n))$, where $O(\log (n))$ is the cost of updating the priority of an edge. Reorganizing the priority queue pushes edges more likely to be relevant to the front of the queue. This induces a higher-quality reservoir and promotes the activation of higher-quality edges at each activation iteration.

# 3.2 Complexity Analysis 

The selection of a candidate edge, either from the priority queue or from random sampling, is at most an $O(\log n)$ cost under the assumption that we only observe $O(n)$ candidate edges through learning. For each edge selection, we must examine the highest priority entry in the priority queue, which costs $O(\log n)$. Then if that priority is better than the default priority, the selection task is complete. If not, we must randomly sample an unseen edge. Randomly sampling any edge costs $O(1)$ time, and checking that the edge has not yet been seen requires another $O(1)$ set-membership check. If the edge has been seen, then we need additional samples until we sample an unseen edge. Fortunately, if the number of seen edges is less than some constant factor of $n$, i.e., $\beta n$, then the probability of sampling a previously seen edge is $\beta n /\binom{n}{2}$, or $2 \beta /(n-1)$, which asymptotically approaches zero.
If it takes the algorithm $r$ edge tests to fill the reservoir in one pass, then best-choice edge grafting performs $\tilde{O}\left(r N s_{\max}^{2}\right)$ operations to compute the sufficient statistics necessary to fill the reservoir and activate the first edges. (We use $\tilde{O}$ notation, omitting the logarithmic costs of using the priority queue.) To activate the $j^{t h}$ edge, the algorithm needs to perform at most $\tilde{O}\left(\left(r+j t_{\max }\right) N s_{\max}^{2}\right)$ operations, where $t_{\max }$ is the allowed number of edge tests between two activation steps.

In most cases, we can assume that it takes the algorithm $r=O(\mid R \mid)$ tests to fill the reservoir $R$. Furthermore, to construct a relevant reservoir, we set $|R|=O(n)$. We also set $t_{\max } \ll n$, so to activate the $j^{\text {th }}$ edge, the algorithm needs to compute at most $O\left((n+\right.$ $\left.j t_{\max } N s_{\max }^{2}\right)$ sufficient statistics tables. In the case of edge grafting, the algorithm needs to compute $O\left(n^{2} N s_{\max }^{2}\right)$ to start grafting the first edge. Since $\left(n+j t_{\max }\right) \ll n^{2}$, our method provides a drastic speedup, as we circumvent the quadratic term in $n$ and replace it with a linear term. Finally, between each activation step, we must compute approximate expectations to obtain the gradient. Approximate inference techniques typically take time linear in the number of active edges. Table 1 summarizes the different time complexity for the discussed algorithms.

# 4 Experimental Evaluation 

Our experiments include simulation of reservoir-based search and evaluation of the speed and quality of learning from synthetic and real data. We use datasets of different variable dimensions and dataset sizes. In the synthetic setting, we simulate MRFs and generate data using a Gibbs sampler. In the real setting, we use two datasets. We use exhaustive edge grafting (labeled "EG" in figures) as our primary baseline. To show the benefits of the reservoir, we also include best-choice edge grafting with no reservoir ("first hit"), which activates the first edge that passes the edge-activation condition.

### 4.1 Benefits of the Reservoir

We analyze the increase in edge quality that the reservoir provides. The reservoir management protocol mimics a reservoir of randomly selected entries from the full population. Asymptotically, the relative percentile of any randomly chosen edge is equivalent to a uniform random variable in the range $[0,1]$. The rank of the best edge in a size- $|R|$ reservoir is thus analogous to the minimum of $|R|$ uniform draws. It is well known that the expected value of this minimum is $1 /(|R|+1)$. We simulate the behavior in finite settings, sampling $|R|$ ranks from the list of all possible numbers from 1 to $\binom{n}{2}$ and taking the minimum. We then plot the average minimum rank over 100 trials, using $n=400$ with values of $|R|$ from 1 to 500. Fig. 1 plots the average ranks over the trials. The results suggest that a small reservoir provides significant gains over using first hit $(|R|=1)$. Using an unlimited reservoir-i.e., grafting-only provides negligible gains over a small reservoir. Since grafting is equivalent to a reservoir of size $\binom{400}{2}$, or 79,800 , the benefits of using a reservoir are evident.

### 4.2 Synthetic Data

We construct random, scale-free structured MRFs with variables having five states each. We generate preferential-attachment graphs [1] of size 200, 400, and 600, with 498,500, 1,997,000, and 4,495,500 parameters, respectively. We then use Gibbs sampling to generate a set of 20,000 data points, which we randomly split as training and held-out test data. We use grid search to tune the learning parameters. We fix $|R|=n$, and $t_{\max } \ll n$. See the appendix for more details on the experimental setup.
Faster convergence We first investigate the behavior of different methods when executed until no violating edge remains in the search space. We measure the different methods' convergence speeds and confirm that they lead to similar solutions. Figure 5 shows that all methods reach a similar solution, but best-choice edge grafting has a faster convergence rate. The first-hit baseline starts with a fast descent rate, but its activation of lower-violation edges eventually causes it to converge slower than edge grafting. Using a reservoir maintains a steep descent until convergence. These experiments also confirm that edge grafting suffers a major cost of computing sufficient statistics, causing it to start optimization after best-choice edge grafting has nearly converged.
Controllable tradeoff between learning speed and quality In subsequent experiments, we fix the maximum number of activated edges to $3 n$, stopping early when each algorithm exhausts this limit. We first measure the objective value during learning and plot it over running time in Fig. 2. We observe similar trends: Best-choice edge grafting provides significant speedups over exhaustive and first-hit edge grafting. Higher $\alpha$ values enable better quality but result in a slower optimization. Experiments on held-out testing data (Fig. 3) show that there is a positive correlation between the learning objective and the test negative log pseudo-likelihood (NLPL), which confirms that the
![img-0.jpeg](img-0.jpeg)

Figure 2: Loss vs. time (seconds) for varying MRF sizes with $O(n)$ edges.

![img-1.jpeg](img-1.jpeg)

Figure 3: Negative log pseudo-likelihood (NLPL) vs. time (seconds) for varying MRFs sizes with $O(n)$ edges.
![img-2.jpeg](img-2.jpeg)

Figure 4: Recall vs. time (seconds) for varying MRFs sizes with $O(n)$ edges.
learned models do not over-fit even with small values of $\alpha$. The first-hit baseline reaches the edge limit faster, but its lower-quality edges cause slower convergence (see Fig. 5) and a lower quality model (Figs. 2 and 4).

Faster edge activation For increasing amounts of variables, the learning gap between bestchoice edge grafting and exhaustive edge grafting increases, which demonstrates the better scalability of the best-choice algorithm. In the smaller graphs, exhaustive edge grafting has the advantage that its greedy search for the worstviolating edge enables large improvements in the objective (and pseudo-likelihood). However, in the larger graphs, even though edge grafting precomputes sufficient statistics, the remaining $O\left(n^{2}\right)$ cost of the greedy search causes its objective to descend at a slower rate than the best choice variants, which avoid this exhaustive search. This high cost is especially evident in the 600 -variable problems (e.g., Fig. 2c), where it takes nearly ten times as long for edge grafting to add the desired number of edges as the reservoir-based best-choice approaches.
![img-3.jpeg](img-3.jpeg)

Figure 5: Objective values vs. seconds during full convergence of all methods ( 200 nodes). The first-hit method takes around 30,000 seconds to converge, so we truncate the horizontal axis for a better view of the other methods.

Structure learning quality Fig. 4 plots the recall of true edges over time until the maximum number of added edges is met. Increasing values of $\alpha$ lead to better recall for different MRF sizes. However, this comes at the cost of a more expensive learning optimization. In fact, for smaller values of $\alpha$, best-choice edge grafting tends to activate more edges but with lower quality, which introduces a greater number of false-positive edges. This result suggests that, while higher values of $\alpha$ help recover the true structure, if the goal of learning the MRF structure is to produce a good generative model, then lower $\alpha$ values speed up learning with only a small loss in quality.
Effectiveness of structure heuristics To evaluate the effectiveness of structure heuristics, Fig. 6 plots the edge recall-for the same limited number of activated edges-with and without the structurebased priority queue reorganization. The significant gap between the recall curves shows that the

heuristics produce a higher-quality edge stream from the priority queue, resulting in a higher-quality reservoir and more relevant edges to activate.

# 4.3 Real Data 

We use the Jester joke ratings [4] and Yummly recipes [7] datasets. Jester is a joke ratings dataset containing 100 jokes and 73,421 user ratings. We use jokes as variables and user ratings as instances. We map the ratings interval from a continuous interval in $[0,20]$ to a discrete interval from 1 to 5 , leading to 124,250 parameters. We sample 10,000 recipes from the Yummly data, using the 489 most common ingredients (which occur in at least 150 recipes) as binary variables and each recipe as a data instance, leading to 478,242 parameters.
Figure 7 shows a positive correlation between the minimization of the learning objective and the testing negative log pseudo-likelihood. The results are similar to those from the synthetic experiments, where best-choice edge grafting converges faster than edge grafting, and smaller values of $\alpha$ result in a faster convergence. The different datasets illustrate the higher scalability of best-choice edge grafting, as its advantage in convergence time over edge grafting increases with dimensionality.
![img-4.jpeg](img-4.jpeg)
(a) Jester Objective
![img-5.jpeg](img-5.jpeg)
(c) Yummly Objective
![img-6.jpeg](img-6.jpeg)

Figure 6: Role of structure heuristics in improving the quality of the learned MRF over training time (seconds). The proposed heuristics (labeled "s") produce higher recall for an MRF of 200 nodes and 600 edges.
![img-7.jpeg](img-7.jpeg)
(b) Jester NLPL
![img-8.jpeg](img-8.jpeg)
(d) Yummly NLPL

Figure 7: Learning objective (a, c) and negative log pseudo-likelihood (b, d) vs. seconds for Jester and Yummly.

## 5 Conclusion

We presented best-choice edge grafting, a method based on a group- $\ell_{1}$ formulation and reservoir sampling. This incremental method activates edges instead of features and uses a reservoir to approximate greedy activation. Theoretical analysis of the iteration complexity shows that the method provides higher scalability than exhaustive edge grafting by avoiding its major bottlenecks. Experiments on synthetic and real data demonstrate that best-choice edge grafting yields faster convergence on multiple datasets, while also achieving structure recovery and predictive ability similar to the more costly exhaustive edge grafting.

## A Edge Grafting and Best-Choice Edge Grafting Algorithms

We summarize edge grafting, as discussed in Section 3.1, in Algorithm 1.
Figure 8 presents a high-level description of the best-choice edge-activation mechanism: From left to right, the first structure is the priority queue ( $p q$ ) initialized with the set of all possible edges. The next diamond-shaped box represents the activation test $C_{2}$, after which an edge is either added to the reservoir $(R)$ or to the frozen edge container $L$. The $t_{\max }$ box represents when the maximum number of edge tests is reached, after which edges are activated. The gray dashed line on the right $\left(R_{\min }\right)$

Algorithm 1 Edge Grafting
1: Define EdgeNum as the maximum allowed number of edges to graft
2: Initialize $E=\emptyset$ and $F=$ set of all possible edges
3: Compute sufficient statistics of $e \forall e \in F$
# cost: $O\left(n^{2} N s_{\max }^{2}\right)$
4: AddedEges $=0$
5: Continue $=$ True
6: while EdgeNum $>$ AddedEges and Continue do
7: Compute score $s_{e} \forall e \in F$
# cost: $O\left(n^{2} s_{\max }^{2}\right)$
8: $e^{*}=\arg \max _{s \in F} s_{e}$.
# cost: $O\left(n^{2}\right)$
9: if $s_{e^{*}}>\lambda$ then
10: $\quad E=E \cup\left\{e^{*}\right\} ; F=F \backslash\left\{e^{*}\right\}$
11: $\quad$ AddedEges $=$ AddedEges +1
12: $\quad$ Perform optimization over new active set
13: else
14: $\quad$ Continue $=$ False
15: end if
16: end while
indicates the injection of the minimum scoring edge in $R$ into $L$, when $R$ is full. The gray dashed line on the left (refill(L)) indicates refilling the priority queue with the frozen edges once it is emptied.

The priority-queue reorganization subroutine is summarized in Algorithm 2, and the activation mechanism is presented in Algorithm 3. These form the underlying components to construct the main best-choice edge grafting framework in Algorithm 4.

Figure 8: High-level operational scheme of the edge activation mechanism.
![img-9.jpeg](img-9.jpeg)

Algorithm 2 Reorganize PQ
1: Compute centrality measures over partially constructed MRF graph $G$
2: Construct the hub set $H$
# cost: $O(n)$
3: for $h \in H$ do
4: for $n \in V$ do
5: $\quad p q[(h, n)]=p q[(h, n)]-1$
# total loop cost: $O(|H| n \log (n))$
6: end for
7: end for

# B Note on Initializing the Priority Queue 

Our experiments show that there is only a small practical benefit of using random sampling for default-priority edges. For the data sizes in our experiments, the $O\left(n^{2}\right)$ cost to instead initialize the full priority queue was negligible, since it is a one-time operation. The quadratic cost only becomes a practical bottleneck when it is repeated or compounded by the data size $N$, as is the case for edge

```
Algorithm 3 Activation Test
    : Reorganize pq using Algorithm 2
    \(E^{*}=\emptyset\)
    \(t=0\)
    repeat
        if \(p q\) is empty then
            if \(R\) is empty then
                Break
            end if
            \(p q=\operatorname{Refill}(L)\)
        end if
        Extract edge \(e\) with highest priority from \(p q\) or by random sampling if \(p q\) is empty or lower
            priority than default
            if Sufficient statistics of \(e\) not already computed then
                Compute sufficient statistics of \(e\)
                    \# cost: \(O\left(N s_{\max }^{2}\right)\)
            end if
        Compute score \(s_{e} . \quad \#\) cost: \(O\left(s_{\max }^{2}\right)\)
        if \(s_{e}>\lambda\) and \(R\) not full then
            Add \(e\) to \(R\)
            else if \(s_{e}>\lambda\) and \(\left(R\) is full and \(R_{\min }<s_{e}\right)\) then
                Replace \(R_{\min}\) by \(e\).
                    \# \(R_{\min }:\) minimum scroing edge in \(R\)
                Place \(R_{\min }$ in \(L\).
            else
                Place \(e\) in \(L\)
            end if
        until \(t=t_{\max }\)
        Compute \(\tau\)
        for \(e \in R\) s.t \(s_{e} \geq \tau\) do
            if \(e\) not adjacent to edges in \(E^{*}\) then
                \(E^{*} \cup\{e\}\)
            end if
        end for
Algorithm 4 Best-Choice Edge Grafting
    Define EdgeNum as the maximum allowed number of edges to graft
    Initialize \(E=\emptyset, F=\) set of all possible edges
    Initialize empty \(p q\)
    AddedEges \(=0\)
    Fill \(R\) to capacity
    while EdgeNum > AddedEges do
        Get set \(E^{*}\) of edges to activate using Algorithm 3
        if \(E^{*}\) is empty then
            Break
            end if
            for \(e^{*}\) in \(E^{*}\) do
                \(E=E \cup\left\{e^{*}\right\} ; F=F \backslash\left\{e^{*}\right\}\)
            AddedEges \(=\) AddedEges +1
        end for
        Perform an optimization over active parameters.
    end while
```

grafting. Thus, our experiments report running times where our best-choice edge-grafting methods take an extra half second or less for the one-time initialization of the full priority queue.

# C Synthetic Data Generation Details 

We generate MRFs with different sizes and variables cardinality five. In particular, we generate structures of size 200, 400, and 600, with 498,500, 1,997,000, and 4,495,500 parameters, respectively.

We first construct random, scale-free structured graphs. To do so, we use a preferential-attachment model where we grow a graph by attaching new nodes, each with two edges that are preferentially attached to existing nodes with high node centrality. The algorithm produces $(2 n-4)$ edges. For each node and each created edge, we sample their corresponding parameters from a normal distribution with a mean equal to 100 and standard deviations $\sigma_{v}=0.5$ (for nodes) and $\sigma_{e}=1$ (for edges). This setting puts more emphasis on the edges (pairwise relationships between nodes) and helps avoid making the model overly dependent on only the unary potentials.
To generate data, we use a Gibbs sampler to generate a set of 20,000 data points, which we randomly split as 19,000 training data points and 1,000 held-out testing data points.

Parameter tuning We use a grid search to detect the best combination of $\lambda$ and $\lambda_{2}$. We limit our search range to the set $\left\{10^{-4}, 10^{-3}, 10^{-2}, 10^{-1}, 1\right\}$ for $\lambda$ and the set $\{0.5,0.75,1,1.5\}$ for $\lambda_{2}$. For each case, we choose the pair $\left(\lambda, \lambda_{2}\right)$ that produces the best recall and test NLPL for the baseline, i.e., edge grafting. It is worth noting that we did not notice a high sensitivity of the methods for different values of $\lambda_{2}$, whereas smaller values of $\lambda$ produce spurious edges for different methods.