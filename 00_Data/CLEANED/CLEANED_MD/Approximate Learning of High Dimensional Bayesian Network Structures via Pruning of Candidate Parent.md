# Article 

## Approximate Learning of High Dimensional Bayesian Network Structures via Pruning of Candidate Parent Sets

Zhigao Guo ${ }^{1, *}$ and Anthony C. Constantinou ${ }^{1,2, *}$<br>1 Bayesian Artificial Intelligence Research Lab, School of Electronic Engineering and Computer Science, Queen Mary University of London, London E1 4NS, UK<br>2 The Alan Turing Institute, British Library, 96 Euston Road, London NW1 2DB, UK<br>* Correspondence: zhigao.guo@qmul.ac.uk (Z.G.); a.constantinou@qmul.ac.uk (A.C.C.)<br>Received: 10 September 2020; Accepted: 7 October 2020; Published: 10 October 2020

check for updates


#### Abstract

Score-based algorithms that learn Bayesian Network (BN) structures provide solutions ranging from different levels of approximate learning to exact learning. Approximate solutions exist because exact learning is generally not applicable to networks of moderate or higher complexity. In general, approximate solutions tend to sacrifice accuracy for speed, where the aim is to minimise the loss in accuracy and maximise the gain in speed. While some approximate algorithms are optimised to handle thousands of variables, these algorithms may still be unable to learn such high dimensional structures. Some of the most efficient score-based algorithms cast the structure learning problem as a combinatorial optimisation of candidate parent sets. This paper explores a strategy towards pruning the size of candidate parent sets, and which could form part of existing score-based algorithms as an additional pruning phase aimed at high dimensionality problems. The results illustrate how different levels of pruning affect the learning speed relative to the loss in accuracy in terms of model fitting, and show that aggressive pruning may be required to produce approximate solutions for high complexity problems.


Keywords: structure learning; probabilistic graphical models; pruning

## 1. Introduction

A Bayesian Network (BN) [1] is a probabilistic graphical model represented by a Directed Acyclic Graph (DAG). The structure of a BN captures the relationships between nodes, whereas the conditional parameters capture the type and magnitude of those relationships. A BN differs from other graphical models, such as neural networks, in that it offers a transparent representation of a problem where the relationships between variables (i.e., arcs) represent conditional or causal relationships. Moreover, the uncertain conditional distributions in BNs can be used for both predictive and diagnostic (i.e., inverse) inference, providing the potential for a higher level of artificial intelligence. For example, knowledge-based BNs are often assumed to represent causal or influential networks and enable decision makers to reason about intervention [2]. On the other hand, structure of BNs, and especially those based on search-and-score solutions on which this paper focuses, are generally assumed to represent networks with conditional-rather than causal-relationships, although the class of constraint-based learning (which we cover below) is often used to discover relationships that could, under various assumptions, be interpreted causally [3].

Formally, a BN model represents a factorisation of the joint distribution of random variables $X=\left(X_{1}, X_{2}, \cdots, X_{n}\right)$. Each BN has two elements, structure $G$ and parameters $\theta$. Constructing a BN involves both structure learning and parameter learning, and both learning approaches may involve

combination of data with knowledge [4-7]. Given observational data $D$, a complete $\mathrm{BN}\{G, \theta\}$ can be learnt by maximising the likelihood:

$$
P(G, \theta \mid D)=P(G \mid D) P(\theta \mid G, D)
$$

and the parameters of the network can be learnt by maximising

$$
P(\theta \mid G, D)=\prod_{i=1}^{n} P\left(\theta_{i} \mid \Pi_{i}, D\right)
$$

where $\Pi_{i}$ denotes the parents of node $X_{i}$ indicated by structure $G$. Depending on the prior assumption, the parameter learning process of each node can be solved using Maximum Likelihood estimation given data $D$, or Maximum A Posteriori estimation given data $D$ and a subjective prior.

On the other hand, the BN structure learning (BNSL) problem represents a more challenging task in that it cannot be solved by simply maximising the fitting of the local networks to the data. The structure learning process must take into consideration the complexity of the model in order to avoid overfitting. In fact, the problem of BNSL is NP-hard, which means that it is generally not possible to perform exhaustive search in the search space of possible graphs, and this is because the number of possible structures grows super-exponentially with the number of nodes $n[8]$ :

$$
f(n)=\sum_{i=1}^{n}(-1)^{i+1} \frac{n!}{(n-i)!n!} 2^{i(n-i)} f(n-1)
$$

Algorithms that learn BN structures are typically classified into three categories: (a) score-based learning that searches over the space of possible graphs and returns the graph that maximises a scoring function, (b) constraint-based learning that prunes and orientates edges using conditional independence tests, and (c) hybrid learning that combines the above two strategies. In this paper, we focus on the problem of score-based learning.

A score-based algorithm is generally composed of two parts: (a) a search strategy that transverses the search space, and (b) a scoring function that evaluates a given graph with respect to the observed data. Well-known search strategies in the field of BNSL include the greedy hill-climbing search, tabu search, simulated annealing, genetic algorithms, dynamic programming, A* algorithm, and branch-and-bound strategies. The objective functions are typically based on either the Bayesian score or other model selection scores. Bayesian scores evaluate the posterior probability of the candidate structures and include variations of the Bayesian Dirichlet score, such as the Bayesian Dirichlet with equivalence and uniform priors (BDeu) [9,10], and the Bayesian Dirichlet sparse (BDs) [11]. Well-established scores for model selection include the Akaike Information Criterion (AIC) [12] and the Bayesian Informatic Criterion (BIC), often also referred to as the Minimum Description Length (MDL) [13]. Other less popular model selection scores include the Mutual Information Test (MIT) [14], the factorized Normalized Maximum Likelihood (fNML) [15], and the qutotient Normalized Maximum Likelihood (qNML) [16].

Score-based approaches further operate in two different ways. The first approach involves scoring a graph only when the graph is visited by the search method, which typically involves exploring neighbouring graphs and following the search path that maximises the fitting score via arc reversals, additions and removals. The second approach involves generating scores for local networks (i.e., a node and its parents) in advance, and searching over combinations of local networks given the pre-generated scores, thereby formulating a combinatorial optimisation problem. The algorithms that fall in the former category are generally based on efficient heuristics such as hill-climbing, but tend to stuck in local optimum solutions, thereby offering an approximate solution to the problem of BNSL. While algorithms of the latter category are also generally approximate, they can be more easily adjusted

to offer exact learning solutions that guarantee to return a graph with score not lower than the global maximum score. This paper focuses on this latter subcategory of score-based learning.

Algorithms such as the Integer Linear Programming (ILP) [17,18] explore local networks in the form of the Candidate Parent Sets (CPSs), usually up to a bounded maximum in-degree, and offer an exact solution. Other exact learning algorithms which cast the BNSL problem as a combinatorial optimisation problem include the Dynamic Programming (DP) [19,20], the A* algorithm [21] and the Branch-and-Bound (B\&B) [22,23]. However, exact learning is generally restricted to problems of low complexity. Evidently, the efficiency of these algorithms is determined by the number of CPSs. For example, the ILP algorithm is restricted to CPSs of size up to one million. However, order-based algorithms such as OBS [24], ASOBS [25,26] and MINOBS [27] explore in the node ordering space, in which the number of structures consistent with the orderings that consist of $n$ nodes is [28]

$$
f(n)=\prod_{i=1}^{n} 2^{n-1}=2^{n(n-i) / 2}
$$

Compared with Equation (3), the number of structures is substantially reduced. For example, for 10 nodes, there are $3.5 \times 10^{13}$ different structures instead of $4.2 \times 10^{18}$ computed by Equation (3). Therefore, order-based algorithms are able to search for approximate solutions in problems that involve hundreds of variables.

In this paper we focus on score-based algorithms that learn BN graphs via local learning of CPSs. Specifically, we investigate the relationship between different levels of pruning on CPSs and the loss in accuracy in terms of the BDeu score. The remainder of this paper is organised as follows: Section 2 provides the problem statement and methodology, Section 3 provides the results, and we provide our concluding remarks and directions for future research in Section 4.

# 2. Problem Statement and Methodology 

Different pruning rules have been proposed to improve the scalability and the efficiency of score-based algorithms that operate on CPSs. Pruning approaches in this context generally aim to reduce the number of CPSs [22,29-32]. The efficacy of a pruning strategy can be significant in the reduction of computational complexity, and this depends on the number of the variables, the level of maximum in-degree and the number of observations in the data. For example, Table 1 presents a sample of the CPSs of node " 0 " in the Audio-train data set (https://github.com/arranger1044/awesome-spn\# dataset), which consists of 100 variables and 15,000 observations. If we assume maximum-in-degree of 1 , with no pruning, this produces $100 \cdot\left(C_{99}^{0}+C_{99}^{1}\right)=10,000$ CPSs, whereas for maximum-in-degree of 2 increases to $100 \cdot\left(C_{99}^{0}+C_{99}^{1}+C_{99}^{2}\right)=495,100$ CPSs, and for maximum in-degree of 3 increases to $100 \cdot\left(C_{99}^{0}+C_{99}^{1}+C_{99}^{2}+C_{99}^{3}\right)=16,180,000$ CPSs.

Table 1. Sample CPSs of node " 0 ", ordered by BDeu score with max in-degree 3. The example is based on Audio-train dataset which incorporates 100 variables.


Pruning rules can be used to discard CPSs that are impossible to exist in optimal structures. Based on the observation that a parent set cannot be optimal if its subsets have higher scores [24], the CPSs that are left after applying these pruning rules are called "legal CPSs". Table 2 presents an example where, in a network with four nodes $\{1,2,3,4\}$, part of the CPSs (those in bold) are pruned with the remaining CPSs representing the so-called legal CPSs. Figure 1 also illustrates all the possible CPSs of node 1, given a maximum in-degree of 3. As shown in Table 2, the CPSs, $\{2,3\},\{2,4\}$ and $\{2,3,4\}$ are pruned and do not form part of the legal CPSs of node 1 because a) the score of CPS $\{2,3\}$ is lower than its subset $\{3\}$, the score of CPS $\{2,4\}$ is lower than its subset $\{4\}$, and the score of CPS $\{2,3,4\}$ is lower than its subset $\{3,4\}$. In total, six CPSs are pruned out of the 32 possible CPSs. Figure 2 presents the optimal structure and shows that none of the pruned CPSs (or that only the legal CPSs) are part of the optimal structure.

Table 2. An example BN with four nodes and the legal CPSs that remain after pruning the CPSs that are impossible to exist (highlighted in bold), as determined by the BDeu score. The example assumes four nodes, a maximum in-degree (ID) of 3, and a sample size of 5000.


![img-0.jpeg](img-0.jpeg)

Figure 1. All possible CPSs of node " 1 " (not shown in the diagram) under the assumption the maximum in-degree is 3 .

We use the GOBNILP software (https://www.cs.york.ac.uk/aig/sw/gobnilp/) to obtain the legal CPSs. For example, the legal CPSs for the Audio-train data set, under maximum in-degree of 3, is $7,343,077$ which represents a $45.4 \%$ of the total number of all possible CPSs. Table 3 presents the number and rates of legal CPSs, in relation to the number of all possible CPSs, over different sample sizes of the Audio-train data set and varied maximum in-degrees. The results show that the level of pruning decreases with sample size and increases with maximum in-degree. This is because a higher sample size leads to the detection of more dependencies whereas a higher maximum in-degree produces a higher number of possible dependencies that need to be explored. Still, this level of pruning is insufficient for high dimensionality problems. In general, the combinatorial optimisation problem of CPSs remains unsolvable for data sets that are large in terms of the number of the variables, with higher levels of maximum in-degree and data sample size further increasing complexity.

![img-1.jpeg](img-1.jpeg)

**Figure 2.** The optimal structure learnt from the CPSs presented in Table 2.

**Table 3.** The number and rates of legal CPSs in relation to the all possible CPSs for subsets of Audio-train data over varying samples sizes and maximum in-degrees.


In this paper, we investigate the effect of different levels of pruning on legal CPSs. The effect is investigated both in terms of the gain in speed and the loss in accuracy, where the loss in accuracy is measured as a discrepancy Δ between the fitting scores of two learnt graphs defined as

$$ \Delta = (S^* - S) / S^* \tag{5} $$

where *S* denotes the BDeu score of a graph generated from pruning, and *S** denotes the BDeu score of the baseline graph generated without pruning. This approach is based on the B&B algorithm proposed by Cassio de Campos [22], where the construction of the graph iterates over possible CPSs and starts from the most likely CPS per node. Specifically, we explore the CPSs expressed in the format shown in Table 1, where legal CPSs for each node are sorted in a descending order as determined by the local BDeu score. Different levels of pruning are explored by pruning different percentages of legal CPSs for each node, starting from the bottom-ranked CPSs of each node in terms of BDeu score. This means that the search in the space of possible DAGs starts from the most promising parent sets of each node. A valid DAG is ensured by skipping CPSs that lead to cycles. A valid DAG is achieved by ensuring that the learnt DAG incorporates at least one root node, which is a node having no parents [33]. This means that the exploration of CPSs must also include 'empty' CPSs (i.e., no parent), as shown in Table 1.

Three different levels of complexity are investigated, where the pruned result is compared to the unpruned result. The unpruned result represents the exact result for moderate complexity problems, although we cannot guarantee this will be the case for higher complexity problems. We define the three different levels of complexity as follows:

- (a) Moderate complexity, which assumes less than 1 million legal CPSs per network;
- (b) High complexity, which assumes more than 1 million and less than 10 million legal CPSs per network;
- (c) Very high complexity, which assumes more than 10 million legal CPSs per network.

We generate BDeu scores using the GOBNILP software and search for the optimal CPSs using different algorithms. Experiments on networks of moderate and high complexity were carried on an Intel Core i7-8750H CPU at 2.2 GHz with 16 GB of RAM, where each optimisation is assigned a maximum 9.2 GB of memory. Experiments on networks of very high complexity were carried on an Intel Core i7-8700 CPU at 3.2 GHz with 32 GB of RAM, where each optimisation is assigned a maximum 25 GB of memory. All experiments are restricted to 24 h of structure learning runtime.

# 3. Results 

The experiments presented in this section are based on BNs and relevant data that are available on the GOBNILP website; link (https://www.cs.york.ac.uk/aig/sw/gobnilp/\#benchmarks) for the networks used in Section 3.1, and link (https://www.cs.york.ac.uk/aig/sw/gobnilp/ for the networks used in Sections 3.1 and 3.3.)

### 3.1. Pruning Legal CPSs of Moderate Complexity

We start the investigation by focusing on BNSL problems of moderate complexity, which we restrict to networks with up to 1 million legal CPSs. Table 4 lists the six networks with their corresponding number of legal CPSs for each case study and sample size combination, assuming a maximum in-degree of 3 .

Table 4. Moderate complexity case studies (nodes|max in-degree in true networks), depicting the total number of legal CPSs per network, as well as the average number of CPSs per node in that network, for network and sample size combination. The number of legal CPSs assume a maximum in-degree of 3 .


Tables 5 and 6 present the loss in accuracy from different levels of CPSs pruning. The effect is measured as a discrepancy $\Delta$ defined in Section 2. For example, in Table 5, $90 \%$ pruning of the CPSs on Asia with sample size 100 leads to a graph that deviates $6.7 \%$, or $0.67 \%$, in terms of BDeu score from the unpruned baseline graph. Note that $90 \%$ pruning of CPSs implies that, for each node, only the $10 \%$ most relevant CPSs are considered in searching for the optimal graph.

Overall, the results suggest that higher sample sizes encourage more aggressive pruning. This is reasonable because a higher sample size implies that the ordering of legal CPSs is more accurate and hence, the pruning also becomes more accurate in terms of pruning the least relevant CPSs. The results show that, in most cases, the loss in accuracy increases faster when pruning exceeds the level of $30 \%$. However, the results from the Hailfinder and Carpo networks suggest that even minor levels of pruning can have a negative impact on the BDeu score, however small this impact may be. All the moderate complexity experiments completed search within four minutes, except the case of Carpo-10000 which took approximately twelve minutes to complete. From this, we can conclude that unless the intention is to save seconds or minutes of structure learning runtime, pruning of legal CPSs is less desirable in problems of moderate complexity.

Table 5. Loss in accuracy for different levels of pruning, as a discrepancy $\Delta$ in BDeu score from the unpruned score, based on the three different sample sizes for case studies Asia, Insurance and Water.


Table 6. Loss in accuracy for different levels of pruning, as a discrepancy $\Delta$ in BDeu score from the unpruned score, based on the three different sample sizes for case studies Alarm, Hailfinder and Carpo.


# 3.2. Pruning Legal CPSs of High Complexity 

This subsection reports the results from pruning based on high complexity case studies that involve problems where the number of legal CPSs ranges between 1 million and 10 million. For this scenario, we used the real-world data sets called Audio-train which consists of 100 variables and 15,000 observations, and Kosarek-test which consists of 190 variables and 6675 observations. We used GOBNILP to generate the BDeu scores for CPSs. This process took 90 and 1398 seconds to complete respectively, with GOBNILP returning 7,343,077 and 5,748,931 legal CPSs, respectively.

Because GOBNILP's ILP algorithm is restricted to CPSs of size less than 1 million, we replaced ILP with the approximate algorithm called MINOBS (https://github.com/kkourin/mobs). The change from exact to approximate learning was inevitable since exact solutions are only applicable to problems of relatively low complexity. In fact, the results show that even an approximate algorithm such as MINOBS fails to complete search within the 24 -hour runtime limit in the absence of pruning. At 24 h of runtime, we stop the search and obtain the highest scoring graph discovered up to that point.

Table 7 presents the results from this set of experiments. The results suggest that problems of high complexity may benefit considerably from pruning compared to problems of moderate complexity. In fact, the results show that it may be safe to perform aggressive pruning on legal CPSs without, or with limited, loss in accuracy, in exchange for a considerable reduction in runtime. For example, $90 \%$ pruning on the CPSs of the Audio-train data set is found to reduce runtime needed to first discover the highest scoring graph by approximately 21 folds without, or in exchange for a trivial, reduction in the BDeu score. Note that while the time needed to first discover the highest scoring graph is generally expected to decrease with higher levels of pruning, Table 7 shows that this is generally, although not always, the case.

Table 7. Loss in accuracy for different levels of pruning, as a discrepancy $\Delta$ in BDeu score from the unpruned score, based on the three different sample sizes for case studies Audio-train and Kosarek-test. Time (secs) represents the time needed by the MINOBS algorithm to first discover the highest scoring graph within the 24 h of search.


The increased benefit from pruning, observed in the case of the Audio-train and Kosarek-test data sets, relative to the data sets of moderate complexity investigated in Section 3.1, can be explained by the higher number of CPSs in the network. This is because when working with higher numbers of CPSs and a low bounded maximum in-degree (in this case, 3), even $90 \%$ pruning of legal CPSs makes it likely that the top three most relevant variables (out of hundreds of variables) will not be part of those pruned.

# 3.3. Pruning Legal CPSs of Very High Complexity 

Lastly, we investigate the effect of pruning in case studies that incorporate more than 10 million legal CPSs. For this purpose, we used the EachMovie-train and Reuters-52-train data sets taken from the same repository. EachMovie-train consists of 500 variables and 4524 observations, whereas Reuters-52-train consists of 889 variables and 6532 observations. As with the high complexity cases, we perform the experiments using the MINOBS algorithm. The GOBNILP software generated a total of $21,985,307$ and $37,479,789$ legal CPSs, in 134 and 616 seconds respectively. However, in these experiments we had to reduce the maximum in-degree from 3 to 2 . This was necessary to avoid running out of memory.

The results in Table 8 suggest that we can derive conclusions that are similar to those derived for the high complexity experiments in Section 3.2. Specifically, the pruning strategy appears to have a minor impact on accuracy of very high complexity network scores, in exchange for potentially large reductions in runtime. Note that while higher levels of pruning always reduce the time required to find the highest scoring graphs from those explored within the 24 h runtime limit in the case of EachMovie-train, the effectiveness of pruning is not as consistent in the case of Reuters-52-train. This suggests that the pruning effectiveness also depends on the data set and may not be solely due to randomness as discussed in Section 3.2.

Table 8. Loss in accuracy for different levels of pruning, as a discrepancy $\Delta$ in BDeu score from the unpruned score, based on the three different sample sizes for case studies EachMovie-train and Reuters-52. Time (secs) represents the time needed by the MINOBS algorithm to first discover the highest scoring graph within the 24 h of search.


# 4. Conclusions

This study investigated the effectiveness of different levels of CPS pruning across problems of varied complexity. The results suggest that it is generally not beneficial to perform pruning of legal CPSs on problems of moderate or lower complexity. This is because the risk of pruning relevant CPSs increases in low complexity case studies that tend to incorporate a lower number of variables, in exchange for relatively minor improvements in speed. On the other hand, the results from problems of higher complexity show potential for major benefit from this type of pruning. This is because these problems tend to incorporate hundreds or thousands of variables, and such a high number of variables makes it easier to determine and prune irrelevant parent-sets, thereby minorly impacting accuracy in exchange for considerable gains in speed. Importantly, problems of very high complexity are often unsolvable and could benefit enormously from any form of effective pruning. The pruning strategy investigated in this paper applies to any type of score-based learning, including the traditional greedy hill-climbing heuristics where pruned legal CPSs could be used to restrict the path of arc additions.

Future work can be extended in various directions. Firstly, more experiments are needed to derive stronger conclusions about the effect of this type of pruning across different algorithms and hyperparameter settings (e.g., over different bounded maximum in-degree). Other research directions include investigating this type of pruning on ordered-based algorithms, where such a pruning strategy could be used to restrict the search space of ordered-based graphs. Lastly, other studies have shown that maximising an objective function does not necessarily imply a more accurate causal graph, especially when the data incorporate noise [34]. This diminishes the importance of exact learning and invites future work where the effect of pruning is judged in terms of graphical structure, in addition to its impact on a fitting score.

Author Contributions: Conceptualization, Z.G.; Methodology, Z.G.; Data curation, Z.G.; Validation, Z.G.; Formal analysis, Z.G. and A.C.C.; Investigation, Z.G. and A.C.C.; Writing-original draft preparation, Z.G.; Writing-review and editing, A.C.C.; Supervision A.C.C.; Project administration, A.C.C.; Funding acquisition, A.C.C. All authors have read and agreed to the published version of the manuscript. Funding: This research was funded by the ERSRC Fellowship project EP/S001646/1 on Bayesian Artificial Intelligence for Decision Making under Uncertainty [35], and by the Alan Turing Institute in the UK under the EPSRC grant EP/N510129/1. Conflicts of Interest: The authors declare no conflict of interest.
