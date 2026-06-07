# Exact Bayesian Network Learning in Estimation of Distribution Algorithms 

Carlos Echegoyen, Jose A. Lozano, Roberto Santana, and Pedro Larrañaga


#### Abstract

This paper introduces exact learning of Bayesian networks in estimation of distribution algorithms. The estimation of Bayesian network algorithm (EBNA) is used to analyze the impact of learning the optimal (exact) structure in the search. By applying recently introduced methods that allow learning optimal Bayesian networks, we investigate two important issues in EDAs. First, we analyze the question of whether learning more accurate (exact) models of the dependencies implies a better performance of EDAs. Second, we are able to study the way in which the problem structure is translated into the probabilistic model when exact learning is accomplished.


## I. INTRODUCTION

Estimation of distribution algorithms (EDAs) [1], [2] are evolutionary algorithms that use probability models instead of the typical genetic operators employed by genetic algorithms (GAs) [3]. In EDAs, machine learning methods are used to extract relevant features of the search space. The collected information is represented using a probabilistic model which is later employed to generate new points. In this way, probabilistic models are used to lead the search to promising areas of the search space.

EDAs mainly differ in the class of probabilistic models used and the methods applied to learn and sample these models. One class of the models that has been extensively applied in EDAs is Bayesian networks [4]. One of the benefits of EDAs that use these types of models [5], [6], [7], [8] is that the complexity of the learned structure depends on the characteristics of the data (selected individuals). Additionally, the analysis of the networks learned during the search can provide information about the problem structure.

One important problem in EDAs is to analyze how the choices of the probabilistic models and of the learning and sampling algorithms can influence the adequate balance between exploration and exploitation. There are a number of papers [9], [10], [11], [12] that report on the way in which the performance of EDAs can dramatically change according to changes in the parameters that determine the learning of the models. Although, in the case of EDAs that use Bayesian networks, the role of the parameters that penalize the complexity of the networks has been studied, a similar analysis of the accuracy of the methods used for finding the best network and its influence in the behavior of EDAs has not been conducted.

[^0]Another related and important issue in EDAs is how the features of the search space are reflected in the learned probability models. This issue, which has received attention from the EDA community [10], [13], [14], [15], is essential to understand the mechanisms that allow EDAs to efficiently sample the search space during the optimization process. However, the question of analyzing the relationship between the search space and the structure of the learned probabilistic models becomes difficult due to two main reasons: The stochastic nature of EDAs' search, and the fact that methods used for learning the models are, in general, able to find only approximate, suboptimal, structures.

In this paper we present an alternative that allows one to study the effect that learning accurate models of the population produce in the behavior of EDAs based on Bayesian networks. Additionally, our contribution serves as a solution to extract more accurate information about the relationship between the problem structure, the search distributions and the probabilistic dependencies learned during the search.

Our approach is based on the use of recently published methods for learning optimal (exact) Bayesian networks [16], [17], [18], [19]. Methods that do exact Bayesian structure learning compute, given a set of data and a prespecified score (in our case, the BIC score [20]), the network structure that optimizes the score. Since the problem of learning the optimal Bayesian network is NP-hard [21], these methods set constraints on the maximum number of variables and/or cases they can deal with. Usually, dynamic programming algorithms are used to learn the structure.

The paper is organized as follows. In the next section Bayesian networks are presented, the general procedures to learn these networks from data are discussed. In Section III, we focus on the type of search strategies used to find the Bayesian network structure. Approximate and exact learning methods are analyzed. Section IV introduces the EBNA algorithm. In Section V, the functions used to evaluate the exact and local learning methods used by EBNA are introduced. This section presents and discusses the results of the different experiments conducted. Work related to our proposal is analyzed in Section VI. The conclusions of our paper are presented in Section VII.

## II. BAYESIAN NETWORKS

## A. Notation

Let $X$ be a random variable. A value of $X$ is denoted $x$. $\mathbf{X}=\left(X_{1}, \ldots, X_{n}\right)$ will denote a vector of random variables. We will use $\mathbf{x}=\left(x_{1}, \ldots, x_{n}\right)$ to denote an assignment to the variables. We will work with discrete variables. The joint


[^0]:    Intelligent Systems Group, Department of Computer Science and Artificial Intelligence, University of the Basque Country, Paseo Manuel de Lardizábal 1, 20080 San Sebastián - Donostia, Spain. email: (ja.lozano@ehu.es, cechegoyenf01@ikasle.ehu.es, rsantana@si.ehu.es, pedro.larranaga@ehu.es)

probability mass function of $\mathbf{x}$ is represented as $p(\mathbf{X}=\mathbf{x})$ or $p(\mathbf{x}) . p\left(\mathbf{x}_{S}\right)$ will denote the marginal probability distribution for $\mathbf{X}_{S}$. We use $p\left(X_{i}=x_{i} \mid X_{j}=x_{j}\right)$ or, in a simplified form, $p\left(x_{i} \mid x_{j}\right)$, to denote the conditional probability distribution of $X_{i}$ given $X_{j}=x_{j}$.

Formally, a Bayesian network [22] is a pair $(S, \boldsymbol{\theta})$ representing a graphical factorization of a probability distribution. The structure $S$ is a directed acyclic graph which reflects the set of conditional (in)dependencies among the variables. The factorization of the probability distribution is codified by $S$ :

$$
p(\mathbf{x})=\prod_{i=1}^{n} p\left(x_{i} \mid \mathbf{p a}_{i}\right)
$$

where $\mathbf{p a}_{i}$ denotes a value of variable $\mathbf{P a}_{i}$, the parent set of $X_{i}$ (variables from which there exists an arc to $X_{i}$ in the graph $S$ ). On the other hand, $\boldsymbol{\theta}$ is a set of parameters for the local probability distributions associated with each variable. If the variable $X_{i}$ has $r_{i}$ possible values, $x_{i}^{1}, \ldots, x_{i}^{r_{i}}$, the local distribution $p\left(x_{i} \mid \mathbf{p a}_{i}^{j}, \boldsymbol{\theta}_{i}\right)$ is an unrestricted discrete distribution:

$$
p\left(x_{i}^{k} \mid \mathbf{p a}_{i}^{j}, \boldsymbol{\theta}_{i}\right) \equiv \theta_{i j k}
$$

where $\mathbf{p a}_{i}^{1}, \ldots, \mathbf{p a}_{i}^{q_{i}}$ denote the values of $\mathbf{P a}_{i}$ and the term $q_{i}$ denotes the number of possible different instances of the parent variables of $X_{i}$. In other words, the parameter $\theta_{i j k}$ represents the probability of variable $X_{i}$ being in its $k$-th value, knowing that the set of its parent variables is in its $j$-th value. Therefore, the local parameters are given by $\boldsymbol{\theta}_{i}=$ $\left(\left(\left(\theta_{i j k}\right)_{k=1}^{r_{i}}\right)_{j=1}^{q_{i}}\right)$.

## B. Learning Bayesian networks from data

There are different strategies to learn the structure of a Bayesian network. We focus on a method called "score + search" which is the one used in the experiments presented in this paper. In this strategy, given a database $D$ and a Bayesian network whose structure is denoted by $S$, a value (score) which evaluates how well the Bayesian network represents the probability distribution of the database $D$ is assigned. Different scores can be used. In this work we have used the Bayesian Information Criterion score (BIC) [20] (based on penalized maximum likelihood).

A general formula for a penalized maximum likelihood score can be written as follows:

$$
\log p(D \mid S, \hat{\boldsymbol{\theta}})-f(N) \operatorname{dim}(S)
$$

where $\operatorname{dim}(S)$ is the dimension -number of parameters needed to specify the model- of the Bayesian network with a structure given by $S$. Thus:

$$
\operatorname{dim}(S)=\sum_{i=1}^{n} q_{i}\left(r_{i}-1\right)
$$

and $f(N)$ is a non negative penalization function. The Jeffreys-Schwarz criterion, sometimes called BIC [20] takes
into account $f(N)=\frac{1}{2} \log N$. Thus the $B I C$ score can be written as follows:

$$
\begin{aligned}
B I C(S, D)= & \log \prod_{w=1}^{N} \prod_{i=1}^{n} p\left(x_{w, i} \mid \mathbf{p a}_{i}^{S}, \hat{\boldsymbol{\theta}}_{i}\right) \\
& -\frac{1}{2} \log N \sum_{i=1}^{n} q_{i}\left(r_{i}-1\right)
\end{aligned}
$$

To find the Bayesian network that optimizes the score implies solving an optimization problem. This can be done with exhaustive or heuristic search algorithms. In Section III, we analyze two variants for finding the Bayesian network structures. Each structure is evaluated using the maximum likelihood parameters.

## C. Learning of the parameters

Once the structure has been learned, the parameters of the Bayesian network are calculated using the Laplace correction:

$$
\hat{\theta}_{i j k}=\frac{N_{i j k}+1}{N_{i j}+2}
$$

where $N_{i j k}$ denotes the number of cases in $D$ in which the variable $X_{i}$ has the value $x_{i}^{k}$ and $\boldsymbol{P} \boldsymbol{a}_{i}$ has its $j^{\text {th }}$ value, and $N_{i j}=\sum_{k=1}^{r_{i}} N_{i j k}$.

## III. Methods for LEARNING BAYESIAN NETWORKS

Once we have defined a score to evaluate Bayesian networks, we have to set a search process to find the Bayesian network that maximizes the score given the data. Approximate and exact methods can be used.

## A. Learning an approximate model

In practical applications, we need to find an adequate model structure as quickly as possible. Therefore, a simple algorithm which returns a good structure, even if not optimal, is preferred. An algorithm that fulfills these criteria is Algorithm B [23] which is typically used by most of Bayesiannetwork based EDAs. Algorithm B is a greedy search which starts with an arc-less structure and, at each step, adds the arc with the maximum improvement in the score. The algorithm finishes when there is no arc whose addition improves the score.

## B. Learning the exact model

Since learning the Bayesian network structure is an NPhard problem, for a long time the goal of learning exact Bayesian networks was constrained to problems with a very reduced number of variables. In [17], an algorithm for learning the exact structure in less than super-exponential complexity with respect to $n$ is introduced for the first time. The time complexity of this method is $O\left(n 2^{n}+n^{k+1} C(m)\right)$ where $k$ is a constant maximum in-degree, and $C(m)$ is the cost of computing a single local marginal conditional likelihood for $m$ instances.

Singh and Moore [19] present a more efficient method called OPTORD which is feasible for $n<22$ and is shown to work with $n=22$. The method is compared to local search heuristic to learn Bayesian networks in a number of datasets, obtaining better scoring solutions that the alternatives tested.

In [18], a more efficient method is presented. The algorithm was shown to learn a best network for a data set of 29 variables. Algorithm 1 presents the main steps of the method.

## Algorithm 1: Exact learning algorithm

1. Calculate the local scores for all $n 2^{n-1}$ different (variable, variable set)-pairs.
2 Using the local scores, find best parents for all $n 2^{n-1}$ (variable, variable set)-pairs.
3 Find the best sink for all $2^{n}$ variables.
4 Using the results from Step 3, find a best ordering of the variables.
5 Find a best network using results computed in Steps 2 and 4.

The total score of the Bayesian structure can be decomposed in the computation of local scores. Therefore, in the first step only local scores are computed. On the other hand, the concept of sink, and specifically the best sink of the Bayesian network, plays an important role in the algorithm. A sink is a node with no outgoing arcs (i.e. a node that is not a parent of any other node). Every directed acyclic graph (DAG) has at least one sink. The identification of sinks by Algorithm 1 allows one to obtain best ordering in reverse order and this fact is used to find the best parents following the order computed. More details about the algorithm can be found in [18].

We use an implementation ${ }^{1}$ of Algorithm 1. The computational complexity of the algorithm is $\mathrm{o}\left(n^{2} 2^{n-2}\right)$. The memory requirements of the method is $2^{n+2}$ bytes and the disk-space requirement is $12 n 2^{n-1}$ bytes.

## IV. ESTIMATION OF DISTRIBUTION ALGORITHMS BASED ON BAYESIAN NETWORKS

The estimation of Bayesian networks algorithm (EBNA) allows statistics of unrestricted order in the factorization of the joint probability distribution. This distribution is encoded by a Bayesian network that is learned from the database containing the selected individuals at each generation. It has been applied with good results to a variety of problems [24], [25], [26], [27], [28]. Other algorithms based on the use of Bayesian networks have been proposed in [6], [7], [8]. A pseudocode of EBNA is shown in Algorithm 2.

In the experiments presented in this paper, EBNA uses truncation selection and the number of selected individuals equals half of the population. The best solution at each generation is passed to the next population, therefore, at each generation $N-1$ new solutions are sampled. The stop criteria changed according to the type of experiments conducted.

[^0]Algorithm 2: EBNA ${ }_{B I C}$
$B N_{0} \leftarrow\left(S_{0}, \boldsymbol{\theta}^{0}\right)$ where $S_{0}$ is an arc-less DAG, and $\boldsymbol{\theta}^{0}$ is uniform
$p_{0}(\mathbf{x})=\prod_{i=1}^{n} p\left(x_{i}\right)=\prod_{i=1}^{n} \frac{1}{r_{i}}$.
$D_{0} \leftarrow$ Sample $M$ individuals from $p_{0}(\mathbf{x})$.
$\mathrm{t} \leftarrow 1$
do $\{$
$D_{t-1}^{g_{e}} \leftarrow$ Select $N$ individuals from $D_{t-1}$.
$S_{t}^{*} \leftarrow$ Using a search method find one network structure according to the BIC score.
$\boldsymbol{\theta}^{t} \leftarrow$ Calculate $\theta_{i j k}^{t}$ using $D_{t-1}^{g_{e}}$ as the data set.
$B N_{t} \leftarrow\left(S_{t}^{*}, \boldsymbol{\theta}^{t}\right)$.
$D_{t} \leftarrow$ Sample $M$ individuals from $B N_{t}$.
$\}$ until Stop criterion is met.

## V. EXPERIMENTS

The experiments are oriented to compare the EBNA versions that use the two different Bayesian network learning schemes described in Section III. We call them EBNA-Exact and EBNA-Local.

We used three different criteria to compare the algorithms. The time complexity, the convergence reliability and the way in which probabilistic dependencies are represented in the structure of the Bayesian network. A set of test functions that represent different classes of problems are chosen for the experiments. First, we introduce the functions that will be used in our experiments. Then, experiments that illustrate the relationship between the number of evaluations and the behavior of the EBNA with the different learning algorithms are shown. We then present experiments on the convergence reliability of the algorithms. Finally, experiments that show the evolution of the networks learned at different iterations of the algorithm are presented.

## A. Function benchmark

Let $u(\mathbf{x})=\sum_{i=1}^{n} x_{i}, f(\mathbf{x})$ is a unitation function if $\forall \mathbf{x}, \mathbf{y} \in\{0,1\}^{n}, u(\mathbf{x})=u(\mathbf{y}) \Rightarrow f(\mathbf{x})=f(\mathbf{y})$. A unitation function is defined in terms of its unitation value $u(\mathbf{x})$, or in a simpler way $u$.

Function OneMax:

$$
\text { OneMax }(\mathbf{x})=\sum_{i=1}^{n} x_{i}=u(\mathbf{x})
$$

Unitation functions are also useful for the definition of a class of functions where the difficulty is given by the interactions that arise among subsets of variables. One example of this class of deceptive functions is $f_{3 \text { deceptive }}[3]$.

$$
f_{3 \text { deceptive }}(\mathbf{x})=\sum_{i=1}^{i=\frac{n}{3}} f_{d e c}^{3}\left(x_{3 i-2}, x_{3 i-1}, x_{3 i}\right)
$$

where $f_{d e c}^{3}$ is defined as:


[^0]:    ${ }^{1}$ The $\mathrm{c}++$ code of this implementation is available from http://www.cs.helsinki.fi/u/tsilande/sw/bene/download/

For function Checkerboard the goal of the problem is to create a checkerboard pattern of 0's and 1's in an $N x N$ grid. Only the primary four directions are considered in the evaluation. For each position in an $(N-2)(N-2)$ grid centered in an $N x N$ grid, $+1$ is added for each of the four neighbors that are set to the opposite value. The maximum evaluation for the function is $4(N-2)(N-2)$.

Function FourPeaks is a modification of the SixPeaks problem [29] and it can be defined mathematically as:

$$
\begin{aligned}
& F_{\text {FourPeaks }}(\mathbf{x}, t)= \\
& \max \{\operatorname{tail}(0, \mathbf{x}), \operatorname{head}(1, \mathbf{x}), \operatorname{tail}(1, \mathbf{x}), \operatorname{head}(0, \mathbf{x})\}+\mathcal{R}(\mathbf{x}, t)
\end{aligned}
$$

where

$$
\begin{aligned}
& \operatorname{tail}(b, \boldsymbol{x})=\text { number of trailing } b \text { 's in } \boldsymbol{x} \\
& \operatorname{head}(b, \boldsymbol{x})=\text { number of leading } b \text { 's in } \boldsymbol{x}
\end{aligned}
$$

$\mathcal{R}(\boldsymbol{x}, t)=\left\{\begin{array}{rl}n & \text { if } \operatorname{tail}(0, \boldsymbol{x})>t \text { and } \operatorname{head}(1, \boldsymbol{x})>t \text { or } \\ & \operatorname{tail}(1, \boldsymbol{x})>t \text { and } \operatorname{head}(0, \boldsymbol{x})>t \\ 0 & \text { otherwise . }\end{array}\right.$

The goal is to maximize the function. For an even number of variables this function has 2 global optima, located at the points:

$$
(\overbrace{0,0, \ldots, 0}^{t} 1,1, \ldots, 1) \quad(\overbrace{1,1, \ldots, 1}^{t} 0,0, \ldots, 0)
$$

These points are very difficult to get because they are isolated. On the other hand, two local optima $(0,0, \ldots, 0)$, $(1,1, \ldots, 1)$ are very easily reachable. The value of $t$ was set to $\frac{n}{2}-1$.

Function Cuban5 [30] is a non-separable additive function. The second best value of this function is very close to the global optimum.

$$
\begin{aligned}
& \operatorname{Cuban} 5(\mathbf{x})= \\
& F_{\text {cuban1 }}^{5}\left(s_{0}\right)+\sum_{j=0}^{m}\left(F_{\text {cuban2 }}^{5}\left(s_{2 j+1}\right)+F_{\text {cuban1 }}^{5}\left(s_{2 j+2}\right)\right)
\end{aligned}
$$

where

$$
s_{i}=x_{4 i} x_{4 i+1} x_{4 i+2} x_{4 i+3} x_{4 i+4} \text { and } n=4(2 m+1)+1
$$

$$
F_{\text {cuban1 }}^{3}(\mathbf{x})= \begin{cases}0.595 & \text { for } \quad \mathbf{x}=000 \\ 0.200 & \text { for } \quad \mathbf{x}=001 \\ 0.595 & \text { for } \quad \mathbf{x}=010 \\ 0.100 & \text { for } \quad \mathbf{x}=011 \\ 1.000 & \text { for } \quad \mathbf{x}=100 \\ 0.050 & \text { for } \quad \mathbf{x}=101 \\ 0.090 & \text { for } \quad \mathbf{x}=110 \\ 0.150 & \text { for } \quad \mathbf{x}=111\end{cases}
$$

$$
\begin{aligned}
& F_{\text {cuban1 }}^{5}(\mathbf{x})= \\
& \left\{\begin{array}{ll}
4 F_{\text {cuban1 }}^{3}\left(x_{1}, x_{2}, x_{3}\right) & \text { if } x_{2}=x_{4} \text { and } x_{3}=x_{5} \\
0 & \text { otherwise }
\end{array}\right. \\
& F_{\text {cuban2 }}^{5}(\mathbf{x})= \begin{cases}u(\mathbf{x}) & \text { for } \quad x_{5}=0 \\
0 & \text { for } \quad x_{1}=0, x_{5}=1 \\
u(\mathbf{x})-2 & \text { for } \quad x_{1}=1, x_{5}=1\end{cases}
\end{aligned}
$$

## B. Time complexity analysis

The time complexity analysis experiments were conducted for functions OneMax and Checkerboard. The objective is to evaluate the average number of generations to find the optimum needed by EBNA-Local and EBNA-Exact. We start with a population of 10 individuals and the population size is increased by 10 until a maximum population size of 150 is reached. For each possible combination of function, number of variables $n$, and population size $N, 100$ experiments are conducted.
![img-0.jpeg](img-0.jpeg)

Fig. 1. Time complexity analysis for function OneMax, $n=10$.

For the OneMax function we conducted experiments for $n \in\{10,12,15,20\}$. The idea was to evaluate, under the dimension constraints imposed by the exact learning algorithm, the scalability of both EBNA versions. The results of the experiments for $n \in\{10,12,15\}$ are shown in Figures 1, 2 and 3, respectively. For $n=20$, the computational cost of the experiments was very high and therefore only 50 experiments were conducted. The average results are shown in Figure 4.

![img-1.jpeg](img-1.jpeg)

Fig. 2. Time complexity analysis for function OneMax, $n=12$.
![img-2.jpeg](img-2.jpeg)

Fig. 3. Time complexity analysis for function OneMax, $n=15$.

The analysis of Figures 1, 2, 3 and 4, respectively, reveals that both algorithms exhibit the same time complexity pattern. However, EBNA-Exact needs, in general, a higher number of evaluations than EBNA-Local to find the optimal solution for the first time. The difference in the number of generations is less evident when the population size approaches 150. For this simple function, it seems that the error in the learning of the model, introduced by the approximate learning algorithm, is beneficial for the search.

For the Checkerboard function, we conducted experiments with $n=9$ and $n=16$. The total number of experiments was 100 , and the average results are shown in Figure 5 and Figure 6. Also, in this case, EBNA-Exact needed a higher number of evaluations than EBNA-Local. Checkerboard is a function with interactions but, at least for the number of variables considered, it can be optimized with very simple models (data not shown).
![img-3.jpeg](img-3.jpeg)

Fig. 4. Time complexity analysis for function OneMax, $n=20$.
![img-4.jpeg](img-4.jpeg)

Fig. 5. Time complexity analysis for function Checkerboard, $n=9$.
![img-5.jpeg](img-5.jpeg)

Fig. 6. Time complexity analysis for function Checkerboard, $n=16$.

### V-C Convergence reliability

The goal of the following experiments was to find the minimum population size needed by the two different variants of EBNA to find the optimum in 20 consecutive experiments. We investigated the behavior of the algorithms for functions Cuban5 ( $n=13$ ), FourPeaks ( $n \in\{10,12,14\}$ ) and $f_{3 d e c e p t i v e}(n \in\{9,12,15\})$. The algorithm begins with a population size $N=16$ which is doubled until the optimal solution has been found in 20 consecutive experiments. The maximum number of evaluations allowed is $10^{4}$. For each function and value of $n, 25$ experiments are carried out. Table I shows the mean and standard deviation of the critical population size found.

TABLE I
MEAN AND STANDARD DEVIATION OF THE CRITICAL POPULATION SIZE FOR DIFFERENT FUNCTIONS AND NUMBER OF VARIABLES.


Table I shows that for function Cuban5, EBNA-Exact requires a slightly higher population size than EBNA-Local. The picture is drastically changed for functions FourPeaks and $f_{3 d e c e p t i v e}$, for which EBNA-Exact needs a much smaller population size. This difference is particularly evident for function FourPeaks. Another observation is that the standard deviation of EBNA-Local is always higher than that of EBNA-Exact. Since the only difference between EBNAExact and EBNA-Local is in the class of algorithm used to learn the models, the difference of behaviors is due to the ability of EBNA-Exact to learn a more accurate model of the dependencies. Therefore, at least for functions FourPeaks and $f_{3 d e c e p t i v e}$, learning a more accurate model determines a better performance of EBNA.

## D. Analysis of the Bayesian network structures

We go deeply into the analysis of the dependencies learned by the two learning algorithms. The objective of this section is to show how the evolution of the dependencies in both variants of EBNA is and to investigate the way in which the problem structure is encoded in the probabilistic model.

First of all, and in order to illustrate the behavior of EBNAExact, Figure 7 shows a typical example of a run of EBNAExact for function FourPeaks. In the first generation, the pattern of the interactions is not clear. However, as the evolution advances, there is a clear path of dependencies between adjacent variables.

To investigate, the type of dependencies learned by EBNAExact and EBNA-Local, we saved the structures of the Bayesian networks learned by both variants of the algorithm in the first and last (population where the optimum was
![img-6.jpeg](img-6.jpeg)

Fig. 7. Evolution of the dependencies learned by EBNA-Exact for function FourPeaks.
reached) for functions FourPeaks, and $f_{3 d e c e p t i v e}$. We chose 30 experiments in which the optimum was found by the algorithms and where they did not converge in the first generation. The frequency in which each arc appeared in the Bayesian network was calculated. Since we are not interested in the direction of the dependencies, we add the frequency of the two arcs that involves the same pair of variables. Frequencies are represented using matrices where lighter colors indicate a higher frequency.

Figures 8 and 9 show the matrices obtained. The first fact that can be observed is the strong relationship between the structure of the functions and the structure of the Bayesian network. This relationship is specially evident in the networks learned at the last generation of EBNAExact for function FourPeaks for which the interactions between adjacent variables are clearly captured. For function $f_{3 d e c e p t i v e}$, both algorithm exhibit a similar behavior. In general, the approximate learning algorithm misses dependencies that are relevant to the search. Therefore, research on more accurate, still computationally simple search strategies is an area worthy of further research.

## VI. Related work

Our work is part of an ongoing research trend that investigates the relationship between the problem structure and the class of structure learned during the search by the probabilistic models. A different but related issue is the effect that the application of EDAs which use probabilistic models

![img-7.jpeg](img-7.jpeg)

Fig. 8. Matrices of the frequencies of the arcs learned by EBNA-Exact and EBNA-Local for function *FourPeaks*. (a) EBNA-Exact, first population. (b) EBNA-Exact, last population. (c) EBNA-Local, first population. (d) EBNA-Local, last population.

![img-8.jpeg](img-8.jpeg)

Fig. 9. Matrices of the frequencies of the arcs learned by EBNA-Exact and EBNA-Local for function *f3deceptive*. (a) EBNA-Exact, first population. (b) EBNA-Exact, last population. (c) EBNA-local, first population. (d) EBNA-Local, last population.

with different representation capabilities (e.g. no interactions, bivariate models, Bayesian networks, mixtures of probability distributions, etc.) has for one prespecified problem.

In [31], the question of the necessary conditions for learning good dependencies (those determined by the interactions in the fitness function) and avoiding bad interactions (those due to the selection operator) are theoretically and empirically investigated. This work is extended in [14], where the probabilistic models learned by hBOA for a separable deceptive function and the spin glasses problem are analyzed. For the spin glasses problem, most of the dependencies found by hBOA are short dependencies between neighbors in the grid but some long range interactions also appear. We point out that the approximate learning algorithm may produce models that are only an approximate representation of the actual dependencies that arise in the population. The error introduced by the learning method in the estimation of the dependencies should be taken into account.

The relationship between problem structure and dependencies is analyzed from two different perspectives in [32]. First, using Pearson's chi-square statistics as a measure of the strength of the interactions between pairs of variables in EDAs, the arousal of dependencies due to the selection operator is shown. Second, it is shown that for some problems, only a subset of the dependencies (those associated to malign interactions [33]) may be needed to solve the problem. It is an open question to investigate which is the composition of the dependencies represented by exact Bayesian networks in terms of malign and benign interactions.

Other researchers have studied the most frequent dependencies learned by the probabilistic models in EDAs and analyzed their mapping with the function structure [9], [10], [13], [34], [35]. Interesting related ideas are the use of the dependency relationships represented by the probabilistic model to define functions with desired degree of interactions [36] and the comparison between different classes of factorizations [37], [38] used for solving a particular function.

## VII. CONCLUSIONS

We have proposed the use of exact learning of the Bayesian network structure in the study of EDAs. Although the results presented in this paper are still preliminary, we have shown that the type of learning algorithm (whether exact or approximate) may produce significant differences in the class of models learned and the performance of the EBNA. This fact is important because usually Bayesian models learned using approximate algorithms are thought to accurately reflect the dependencies that arise in the population. Whenever the size of the problem is manageable, exact learning of Bayesian networks is a more appropriate option for theoretical analysis of the probabilistic dependencies. Finally, we emphasize that the study of the relationship between the problem structure and the dependencies captured by the probabilistic model should provide answers for the fundamental question of how to select appropriate probabilistic models to optimize a given problem in the framework of EDAs.

## ACKNOWLEDGMENT

This work was supported by the SAIOTEK-Autoinmune (II) 2006 and Etortek research projects from the Basque Government. It has been also supported by the Spanish Ministerio de Ciencia y Tecnología under grant TIN 2005-03824.
