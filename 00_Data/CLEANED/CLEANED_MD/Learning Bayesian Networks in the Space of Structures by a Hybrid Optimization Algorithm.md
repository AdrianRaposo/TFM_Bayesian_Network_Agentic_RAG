# Learning Bayesian Networks in the Space of Structures by a Hybrid Optimization Algorithm 

M. Zhu, S. Liu, J. Jiang<br>Mingmin Zhu*, Sanyang Liu<br>School of Mathematics and Statistics, Xidian University<br>2 South Taibai Road, Xi'an, China, 710071<br>*Corresponding author: zmmzhu2010@126.com<br>liusanyang@126.com

## Jiewei Jiang

School of Computer Science and Technology, Xidian University
2 South Taibai Road, Xi'an, China, 710071
jiangjw924@126.com


#### Abstract

Bayesian networks (BNs) are one of the most widely used class for machine learning and decision making tasks especially in uncertain domains. However, learning BN structure from data is a typical NP-hard problem. In this paper, we present a novel hybrid algorithm for BN structure learning, called MMABC. It's based on a recently introduced meta-heuristic, which has been successfully applied to solve a variety of optimization problems: Artificial Bee Colony (ABC). MMABC algorithm consists of three phases: (i) obtain an initial undirected graph by the subroutine MMPC. (ii) Generate the initial population of solutions based on the undirected graph and (iii) perform the ABC algorithm to orient the edges. We describe all the elements necessary to tackle our learning problem, and experimentally compare the performance of our algorithm with two state-of-the-art algorithms reported in the literature. Computational results demonstrate that our algorithm achieves better performance than other two related algorithms.


Keywords: Bayesian network, Artificial Bee Colony, Structural learning, Metaheuristics, Scoring function.

## 1 Introduction

Bayesian networks (BNs), also known as belief networks, are becoming a popular tool for representing uncertainty in artificial intelligence. They have been applied to a wide range of tasks such as natural spoken dialog systems, vision recognition, expert systems, medical diagnosis, and genetic regulatory network inference [1-6]. With a network at hand, probabilistic inference can be performed to predict the outcome of some variables based on the observations of others $[7,8]$. There has been a lot of work in the last ten years on the learning of BNs for both graph structure and probability parameters. However, learning the structure is harder and, arguably, more critical. Most of these algorithms can be grouped into two different categories: constraint-based methods $[9,10,11]$ and search-and-score methods [12,13,14]. The first one poses the learning process as a constraint satisfaction problem, and then constructs a network structure by testing the conditional independence relations. The second one poses the learning problem as a structure optimization problem. Namely, it uses a score metric to evaluate every candidate network structure, and then, finds a network structure with the best score. Though the implement of the former approach is relatively simple, the computation for high-order conditional independence tests is complex and irresponsible. Thus, the score-and-search approach gradually becomes a popular approach for learning BNs $[15,16,17]$.

Recently, a hybrid algorithm that combines the conditional independence methodology with scoring metric optimization, max-min hill climbing (MMHC) 18 , has been introduced and proven to be very competitive. In MMHC approach, after reconstructing an undirected graph encoding parent-child relationships by using the max-min parents and children (MMPC) algorithm, a greedy Bayesian scoring hill-climbing search is used to orientate the edges.

In this paper, the idea is further explored, by using the artificial bee colony (ABC) 19, 20 algorithm to perform the edge orientation. We call the new hybrid algorithm max-min artificial bee colony (MMABC) algorithm. The ABC algorithm can be used to search for the near-optimal graph in the space of directed acyclic graphs (DAGs). We describe all the elements necessary to tackle our learning problem using this meta-heuristic, and experimentally compare the performance of our ABC-based algorithm with other algorithms used in the literature. The remainder of this paper is organized as follows. Section 2 describes the concepts and methods related to BNs. We introduce the ABC algorithm and our main algorithm in Section 3. Simulation studies are conducted to demonstrate the performance of our algorithm and existing algorithms in Section 4. Finally, in Section 5, we conclude and outline our future work.

# 2 Preliminaries 

In this section we briefly review some basic concepts related to BNs and how to learn them.
A BN is a graphical representation of a joint probability distribution that includes two components. One is a directed acyclic graph (DAG) $G=(V, E)$, where $V=\left\{v_{1}, v_{2}, \ldots, v_{n}\right\}$, the set of nodes, represents the random variables, and $E$ is the set of edges, represents direct dependency relationships between variables. The other is a conditional probability table that quantifies the effects $\left(p\left(v_{i} \mid p a\left(v_{i}\right)\right)\right)$ that the parent set of $v_{i}$ have on the variable $v_{i}$ in $G$, where $p a\left(v_{i}\right)$ is the parent set of $v_{i}$ in $G$, i.e., $p a\left(v_{i}\right)=\left\{v_{j} \mid v_{j} \rightarrow v_{i} \in E, v_{j} \in V \backslash v_{i}\right\}$. If $v_{j}$ is the parent of $v_{i}$, then $v_{i}$ is the child of $v_{j}$ in $G$. Learning the structure of BN is equivalent to identifying the structure of the DAG $G$ that best matches the data set $D$. Robinson [21] showed that the number $f(n)$ of possible structures for BN having $n$ nodes is given by the recurrence formula:

$$
f(n)=\sum_{i=1}^{n}(-1)^{i+1} \frac{n!}{i!(n-i)!} 2^{i(n-1)} f(n-i)
$$

Searching for the best structure is difficult because the search space increase exponentially with the number of variables. It has been proven to be an NP-hard problem [22].

Recently, a new and quite competitive method, the MMHC algorithm [18], that combines both scoring-based and conditional independence test approaches has been introduced. It first learns the undirected graph (i.e., the edges without their orientation) of a BN using a local discovery algorithm called the max-min parents and children (MMPC) algorithm. Then, it orients the undirected graph using a greedy hill climbing search. The subroutine MMPC is sound in the sample limit. It attempts to quickly identify the set of parents and children $p c\left(v_{i}\right)$ of a variable $v_{i}$ in two phases. In the first phase, variables that are conditionally independent on $v_{i}$ can enter the set of candidate parents and children according to a heuristic function. In each iteration, variable $v_{j}$ enters the candidate set that maximizes the minimum association to $v_{i}$ given the current candidate set. In the second phase, the false-positive variables that possibly entered the candidate set in the first phase are removed. More detailed explanation can be found in 18.

In this paper, we first use the MMPC algorithm to learn the undirected graph of a BN, and then orientate the edges by applying the artificial bee colony (ABC) algorithm. In the following, we briefly introduce the ABC algorithm, which is a new meta-heuristic approach inspired by the intelligent foraging behavior of honeybee swarm. After that, we give the main algorithm of this paper.

# 3 Learning Bayesian networks using the ABC algorithm 

### 3.1 The Artificial Bee Colony algorithm

The ABC [20] algorithm is a swarm based meta-heuristic that simulates foraging behavior of honey bees. This algorithm includes three kinds of bees considering the division of labor: employed bees, onlooker bees and scout bees. A bee that is currently exploiting a food source is called an employed bee. A bee waiting in the hive for making decision to choose a food source is named as an onlooker. A bee carrying out a random search for a new food source is called a scout. An employed bee keeps a food source in her mind when she leaves from the hive and she shares the information about her food source with onlookers on dance area. Onlookers select a food source by watching the dances of the employed bees and try to improve this source. If a food source is abandoned, its employed bee becomes a scout to explore new food sources randomly. Scouts either randomly search the environment in order to find a new food source depending on an internal motivation or based on possible external clues.
![img-0.jpeg](img-0.jpeg)

Figure 1: Flowchart of the ABC algorithm
![img-1.jpeg](img-1.jpeg)

Figure 2: Three edge operators used in the MMABC algorithm

In ABC algorithm each food source represents a possible solution for the problem and the fitness value of the solution corresponds to the nectar amount of this food source. Each food source is exploited by only one employed bee. In other words, the number of employed bees is equal to the number of candidate solutions. Similar to the other swarm intelligence based approaches, the ABC algorithm is also an iterative process. It repeats a series of steps until a termination criterion is met. We show all these steps and interactions between them as a flowchart on Figure 1.

# 3.2 A hybrid algorithm for learning BNs using ABC optimization 

The above basic ABC algorithm, originally designed for the continuous nature of optimization problems, can not directly be used for discrete problems. In this section, we develop a new ABC-based algorithm for learning BNs that performs the search in the space of directed acyclic graphs. The new algorithm is called MMABC for short. We first use the MMPC algorithm to learn the undirected graph of a BN. Based on this undirected graph $U G$, the initial population for MMABC is produced randomly. More specifically, the edges of the initial graph corresponding to each individual are randomly selected from the edge set of $U G$, which is the candidate edge set of the optimal BN structure. This greatly reduces the randomness of the initial population and improve the convergence speed. The main components of our MMABC algorithm are described below.

## a. Initialization.

Let $m$ and $n$ denote the total number of food sources and the number of variables in a BN, respectively. Since the structure of a BN is a directed graph $G=(V, E)$, we represent each individual by a binary node-node adjacency matrix $X=\left(x_{i j}\right)_{n \times n}, i, j=1,2, \ldots, n$. Entry $(i, j)$ is 1 if there is a directed arc from node $i$ to node $j$, and 0 otherwise. That is,

$$
x_{i j}= \begin{cases}1, & \text { if } V_{i} \rightarrow V_{j} \in E \\ 0, & \text { if } V_{i} \rightarrow V_{j} \notin E\end{cases}
$$

Initial food sources (solutions) $X_{k}=\left(x_{i j}\right)_{n \times n}, k=1,2, \ldots, m$ are generated randomly by selecting edges from an undirected graph $U G=(V, \bar{E})$, which is obtained by MMPC. Counters which store the numbers of trials of solutions are reset to 0 in this phase.

## b. Employed Bees Phase.

Each employed bee is associated with only one food source site. An employed bee generates a neighboring solution by three operators: edge insertion, edge deletion and edge reversal. We show these three operators in Figure 2. Let $X_{k}$ and $X_{k}{ }^{*}$ denote the current solution and the generated one, respectively. The quality of the graph $G$ corresponding to $X_{k}{ }^{*}$ is measured by the K2 score function [23] as follows:

$$
\begin{gathered}
f_{K 2}(G, D)=\sum_{i=1}^{n} f_{K 2}\left(v_{i}, p a\left(v_{i}\right) \mid D_{v_{i}, p a\left(v_{i}\right)}\right) \\
f_{K 2}\left(v_{i}, p a\left(v_{i}\right) \mid D_{v_{i}, p a\left(v_{i}\right)}\right)=\sum_{j=1}^{q_{i}}\left[\log \left(\frac{\left(r_{i}-1\right)!}{\left(N_{i j}+r_{i}-1\right)!}\right)+\sum_{k=1}^{r_{i}} \log \left(N_{i j k}!\right)\right]
\end{gathered}
$$

where $D$ is the domain data set. $D_{v_{i}, p a\left(v_{i}\right)}$ are the statistics of the variable $v_{i}$ and $p a\left(v_{i}\right)$ in $D$, i.e., the number of instances in $D$ that match each possible instantiation of $v_{i}$ and $p a\left(v_{i}\right)$. $N_{i j k}$ is the number of cases in $D$ where $v_{i}$ is in its $k$ th state and its parents are in their $j$ th state. $N_{i j}=\sum_{k=1}^{r_{i}} N_{i j k}$ denotes the number of cases in $D$ where $p a\left(v_{i}\right)$ is in its $j$ th state and $r_{i}$ denotes the number of states of variable $v_{i}, q_{i}$ is the number of parent configurations of $v_{i}$. Because the K2 metric is decomposable and the graphs corresponding to $X_{k}{ }^{*}$ and $X_{k}$ are different from one edge by each one of three operators, we can reuse most of the computations made in the food source $X_{k}$. In other words, we only need to update the statistics corresponding to the variables whose parent sets have been modified. Thus, the time performance can be greatly enhanced.

As our problem is a maximization problem and the value of $f_{K 2}(\cdot)$ is negative, therefore, the fitness value assigned to the solution $X_{k}{ }^{*}$ is determined using the following expression:

$$
f i t_{k}=\frac{1}{1+a b s\left(f_{k}\right)}
$$

where $f_{k}$ is the K2 value of the graph $G$ corresponding to $X_{k}{ }^{*}$. A greedy selection is employed between $X_{k}$ and $X_{k}{ }^{*}$ such that the better one is selected depending on fitness values representing the nectar amount of the food sources at $X_{k}$ and $X_{k}{ }^{*}$. If $X_{k}$ cannot be improved, its counter is incremented by 1 , otherwise, the counter is reset to 0 .

# c. Onlooker Bees Phase. 

An onlooker bee evaluates the nectar information taken from all employed bees and chooses a food source site with a probability related to its nectar amount. The roulette wheel selection scheme is used here in which each slice is proportional in size to the fitness value as follows:

$$
p_{k}=\frac{f i t_{k}}{\sum_{j=1}^{m} f i t_{j}}
$$

By doing so, the onlooker bees are encouraged to visit the food sources that have higher nectar amounts. Briefly, food source selection by onlookers is based on the information provided by employed bees. A uniform random number within the range $[0,1]$ is obtained for each source. If the probability value $p_{k}$ is greater than this random number, then the onlooker bee generates a neighboring food source again by using three operators as in the case of the employed bee. After the source is evaluated, greedy selection is applied. If solution $X_{k}$ cannot be improved, its counter is incremented by 1 , otherwise, the counter is reset to 0 . This process is repeated until all onlookers are distributed onto food source sites.

## d. Scout Bees Phase.

If the value of the counter is greater than the control parameter "limit", then the food source associated with this counter is abandoned. Assume that the abandoned source is $X_{k}$, then the scout randomly discovers a new food source $X_{k}{ }^{*}$ which can be achieved by randomly generating any directed acyclic graph. This procedure can increase solutions diversity and avoid falling into the local optimum. In our algorithm, there is only a single food source which can be abandoned in each cycle, and only one employed bee can be a scout.

## e. Termination.

If a termination is not satisfied, go to Employed Bees Phase; otherwise stop the procedure and output the best food source found so far.

As shown in Algorithm 1, the MMABC algorithm first constructs the undirected graph $U G$ of the underlying BN structure by the MMPC algorithm, which obtained the parents and children of each variable. It gives the best-so-far undirected graph, from which the initial population can be generated randomly by selecting $n-1$ edges from $U G$ (assumed the underlying BN has $n$ variables). Figure 3 shows the process of generating initial population by a simple example. Consider the second graph in Figure 2. Assumed that its undirected graph $U G$ obtained by MMPC is shown in Figure 3 (a). By randomly selecting 3 directed edges from $U G$, we can get an initial solution. Figure 3(b), Figure 3(c) and Figure 3(d) show 3 solutions of the initial population generated from Figure 3(a).

After producing and evaluating the initial population, the main loop of the MMABC algorithm then begins for Iter iterations. Step 7 and 15 show one of the edge operators can be chosen to obtain the neighbor of the current solution in Employed Bees Phase and Onlooker Bees Phase, respectively. Each of the operators can be chosen randomly with equal probability. If there is a cycle in the generated graph, another new graph can be achieved again.

## 4 Experimental results

In this section, we present the experimental results carried out with our algorithm and compare MMABC with two hybrid heuristic methods: MMHC [18] and MMACO [24]. In all the

```
Algorithm 1 The MMABC algorithm.
1. Obtain the undirected graph \(U G\) by MMPC;
2. Generate the initial population of solutions \(X_{k}, k=1,2, \ldots, m, t r_{k}=0 . m\) is the total number of food sources. \(t r_{k}\) is the non-improvement
    number of the solution \(X_{k}\), used for abandonment;
3. Evaluate the population;
4. Iter \(=1\);
5. repeat
6. for \(k=1\) to \(m\) do
7. Produce a new food source \(X_{k}{ }^{\times}\)for the employed bee of the food source \(X_{k}\) by using one of the three edge operators and evaluate its
        quality according to equation (3);
8. Apply a greedy selection process between \(X_{k}{ }^{\times}\)and \(X_{k}\) and select the better one;
9. If solution \(X_{k}\) does not improve \(t r_{k}=t r_{k}+1\), otherwise \(t r_{k}=0\);
10. end for
11. Calculate the probability value \(p_{k}\) by (6), \(k=1,2, \ldots, m\);
12. \(t=0, k=1\);
13. repeat
14. if random \(<p_{k}\) then
15. Produce a new food source \(X_{k}{ }^{\times}\)for the onlooker bee of the food source \(X_{k}\) by using one of the three edge operators and evaluate its
        quality by (3);
16. Apply a greedy selection process between \(X_{k}{ }^{\times}\)and \(X_{k}\) and select the better one;
17. If solution \(X_{k}\) does not improve \(t r_{k}=t r_{k}+1\), otherwise \(t r_{k}=0\);
18. \(t=t+1\);
19. end if
20. until \(t=m\);
21. if \(\max \left(t r_{k}\right)>\) limit then
22. Replace \(X_{k}\) with a new randomly produced solution;
23. end if
24. Memorize the best solution achieved so far;
25. Iter=Iter \(=1\);
26. until Iter=Maximum Iteration.
```

Figure 3: The MMABC algorithm
![img-2.jpeg](img-2.jpeg)

Figure 4: The process of generating initial population

cases the scoring metric used to guide the search is the K2 metric, so, the difference among implementations is minimized. All these experiments are based on the BN toolbox written by Murphy [25] and the Causal Explorer System developed by Aliferis et al.[26]. The experimental platform is a personal computer with Pentium 4, 3.06 GHz CPU, 1.0 GB memory, and Windows XP.

The standard way of assessing the accuracy of a learning method is to draw samples from a known BN, apply structure learning on the artificial data, and to compare the learned structure with the original one. To benchmark our method, we investigate its performance on artificial data with real-world characteristics focusing on the well-known Asia [27], Insurance [28], and Alarm [29] networks. The first one is a small BN using a fictitious medical example that considers the dependence of the health status of a patient (having tuberculosis, lung cancer, or bronchitis) on risk factors (visit to Asia and smoking) and clinical observations (Dyspnea and X-ray). It consists of eight nodes with eight edges connecting them. Each random variable is discrete in nature and can take two states. The second example is a network for estimating the expected claim costs for a car insurance policyholder. It consists of 27 nodes and 52 edges. The last one is a medical diagnostic system for patient monitoring. It consists of 37 nodes and 46 edges connecting them. The random variables in the ALARM network are discrete in nature and can take two, three, or four states. The characteristics of the networks are summarized in Table 1. For these three networks, data sets with $200,500,1000,3000$, and 5000 samples are drawn. For each of the sample sizes, ten independent data sets are generated by applying Gibbs sampling [30] on the benchmark networks, resulting in a set of 50 data sets for each network. 10 replicates are done for each of different network parameters and sample size. We will discuss our experimental results in more detail in the following two subsections.

Table 1: Bayesian networks


Table 2: The K2 values for the true networks with different samples


# 4.1 Comparison of the solution quality 

In this subsection, we compare the performance of the different algorithms on all of the data sets. Our main objective in these experiments is to determine whether MMABC is more efficient and effective than the other two hybrid algorithms. For MMABC and MMACO, the population size is set to 20 , and the maximum number of iterations is set to 100 . The significant level used

in these algorithms is set to 0.05 . Other parameter settings of the MMACO algorithm can be found in [24]. The parameter "limit" for MMABC is set to 6 , namely, if the solution associated with an employed bee does not improve for 6 times, then that solution is replaced by some randomly generated solution. In order to provide an objective measure of network structure reconstruction behavior, we compare the underlying DAG with the learned DAG and record the structural hamming distance (SHD), where SHD is defined as the total number of operations to verify the learned DAG to the underlying DAG. The K2 scoring function was also presented to measure the learned network structure, which could be used to compare the quality of the structures obtained by different algorithms. The K2 values for the true network structures with different data sets can be seen in Table 2.

Table 3: The results for three algorithms with different datasets


Table 3 provides the mean and standard deviation of the K2 score and the mean SHD values obtained for the learned networks with different data sets. $\mu \pm \sigma$ indicates the mean and the standard deviation over the executions carried out. We have carried out 10 executions of each algorithm and for each domain considered. In Table 3, the first six rows display the results of three algorithms on Asia data sets, and the rest twelve rows is the results on Insurance and Alarm data sets. For example, figures in the second row are the SHD values obtained by the MMABC algorithm on Asia data sets. Figures in the third row are their corresponding mean and standard deviation of the K2 scores. On the whole, we can see that MMACO algorithm is a little better than MMHC algorithm on the Asia network, and our algorithm is best. However, in the case of Insurance and Alarm networks, the advantages of MMABC and MMACO are more evident, and MMABC performs better than MMACO, which means our algorithm has better performance with more complicated networks. The K2 score of our algorithm is always closer

to that of the original network. The reason is that the construction process of a BN for an ant is dependent much too on the pheromone and heuristic information of candidate arcs, which is prone to overfitting. Although it can be seen that the K2 score of MMABC and MMACO becomes similar as the sample size increase, MMABC has a lower SHD value. We also note that in some cases, the score obtained by MMACO is better than that of MMABC, but MMABC has lower SHD values. This indicates that a better score does not necessarily mean a better SHD value and vice-versa. It can occur because of small size and because of the parameters given to the scoring function, which have been shown to produce differences in scoring function behavior. It is worth mentioning that the standard deviation of the MMABC is lower than that of the other two algorithms, which means that the MMABC guarantees good quality networks with less fluctuation than other algorithms.

# 4.2 Comparison of the convergence and time performance 

In order to measure the convergence speed and the runtime complexity to learn the structure, we compared with the typical runs of the MMABC and MMACO algorithms on the same data set by large number of experiments.
![img-3.jpeg](img-3.jpeg)

Figure 5: Comparison of the solution quality for MMACO and MMABC on Asia data sets: (a) Scores for Asia; (b) SHD for Asia

Figure 4 and Figure 5 show the curves of the convergence performance on two data sets, Asia1000 and Alarm-5000, respectively. In these figures, the abscissas depict the number of iterations, and the Y-coordinates depict the K2 score or SHD value of the learned graph. $U S$ specifies the underlying score of the original network. From a general point of view, MMABC achieve better quality networks in the initial stages of the optimization and has a rapidly converging learning curve, which means that MMABC require a significantly lower number of iterations than MMACO to achieve networks of better quality. Although we are testing on two very different data sets, we obtain similar observation that as the score is improving over iterations, the SHD value is deteriorating. It provides strong evidence that MMABC is performing well against the MMACO algorithm.

In Figure 6, we test MMABC with 4 different population sizes on Asia-1000: 10 (MMABC1), 20 (MMABC2), 30 (MM ABC3), 40 (MMABC4). From the curves in Figure 6(a) and Figure 6(b), it can be found that the population size $m$ can have an effect on the convergence speed of the algorithm. In other words, MMABC takes a comparatively large number of iterations to converge to an acceptable solution with a small number of bees. Because a large population

![img-4.jpeg](img-4.jpeg)

Figure 6: Comparison of the solution quality for MMACO and MMABC on Alarm data sets: (a) Scores for Alarm; (b) SHD for Alarm
![img-5.jpeg](img-5.jpeg)

Figure 7: Comparison of the solution quality for different population sizes on Asia data sets: (a) Scores for Asia; (b) SHD for Asia

means that more food sources are employed, there are more different solutions examined than in a smaller population. On the other hand, the time consumed also increased proportionally with increasing population size. It should be noted that tiny changes to the score value can lead to large structural changes as an algorithm converges towards the optimum network.
![img-6.jpeg](img-6.jpeg)

Figure 8: Comparison of the time performance on two networks: (a) Running time for Asia data sets; (b) Running time for Alarm data sets

Figure 7 gives the average running time to reach the best solution for three algorithms on two networks. Based on Figure 7, we can see that the proposed MMABC has a considerable better time performance than MMACO, and MMHC has the best time performance. However, from the results of Table 3, we can see that MMHC obtains worse K2 score and SHD values. Moreover, the advantage is very obvious when the data set is large on the same network, namely, the bigger the sample size, the more obvious the improvement. We also noted that the running time of MMABC is affected less by the size of data but more by the problem dimension. It means that MMABC is not sensitive to the increase of the sample capacity and able to handle very large data sets.

# Conclusions 

In this paper we have designed and implemented a hybrid ABC-based algorithm for the BN structure learning problem. Ideas from constraint based local learning and score-based ABC were combined into effective learning processes. Its application to several benchmark networks yielded better results than the previously used MMHC and MMACO algorithms.

This paper demonstrates the capability of ABC algorithm in learning a probability graphical model. Ideas presented in this paper can be applied to many other probability graphical problems also, such as dynamic BN, chain graph, etc. Moreover, we have applied the basic three edge operators for determining the neighboring solutions in MMABC. It will be interesting to see whether there exists some alternative approach to serve the same purpose here. We also intend to expand this analysis to larger benchmark networks and make further conclusions on the usefulness of the constraint-based and score-based learning approaches. Finally, although we assume in this paper that the data are completely observed, missing data or data with latent variables may arise in practice. Generalization of the proposed algorithm to incomplete data is of great research interest.

# Acknowledgment 

The authors would like to thank the editor and the anonymous reviewers for their insightful comments and suggestions. This work has been partially supported by the National Natural Science Foundation of China (Grant No. 61373174, 11401454), the Natural Science Foundation of Shannxi Province, China (Grant No. 2014JQ1031) and the Fundamental Research Funds for the Central Universities (Grant No. JB140711).
