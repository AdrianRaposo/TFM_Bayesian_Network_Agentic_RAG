# Bayesian network structure learning based on the chaotic particle swarm optimization algorithm 

Q. Zhang, Z. Li, C.J. Zhou and X.P. Wei<br>Key Laboratory of Advanced Design and Intelligent Computing, Dalian University, Ministry of Education, Dalian, China<br>Corresponding author: Q. Zhang<br>E-mail: zhangq@dlu.edu.cn<br>Genet. Mol. Res. 12 (4): 4468-4479 (2013)<br>Received February 2, 2013<br>Accepted August 15, 2013<br>Published October 10, 2013<br>DOI http://dx.doi.org/10.4238/2013.October.10.12


#### Abstract

The Bayesian network (BN) is a knowledge representation form, which has been proven to be valuable in the gene regulatory network reconstruction because of its capability of capturing causal relationships between genes. Learning BN structures from a database is a nondeterministic polynomial time (NP)-hard problem that remains one of the most exciting challenges in machine learning. Several heuristic searching techniques have been used to find better network structures. Among these algorithms, the classical K2 algorithm is the most successful. Nonetheless, the performance of the K2 algorithm is greatly affected by a prior ordering of input nodes. The proposed method in this paper is based on the chaotic particle swarm optimization (CPSO) and the K2 algorithm. Because the PSO algorithm completely entraps the local minimum in later evolutions, we combined the PSO algorithm with the chaos theory, which has the properties of ergodicity, randomness, and regularity. Experimental results show that the proposed method can improve the convergence rate of particles and identify networks more efficiently and accurately.


Key words: Bayesian network structure learning; Convergence; Particle swarm optimization; Chaos theory; Ergodicity

# INTRODUCTION 

In the 1950s, the discovery of the double helix structure of DNA unveiled a new era of molecular biology. Since then, the study of genes and gene expression at the molecular level promoted the development of biology. As basic building blocks of life, genes as well as their products do not work independently. They interact with each other and form a complicated network. That is, some genes can activate or inhibit the expression of another gene. It is possible to infer gene regulatory relationships between genes from the gene expression levels measured from experimental data of the cell cycle. Based on these relationships, a gene regulatory network can be constructed that can facilitate biomedical research, such as cancer research, drug discovery, and disease prevention.

At present, through the analysis of gene expression microarray data, many methods and models have been developed and applied to infer gene regulatory networks. These studies contributed to insight into gene functions, gene regulation, cell biological functions, and working mechanisms through the development of tools such as weight matrices (Weaver et al., 1999), Boolean networks (Akutsu et al., 1999), differential equations (Chen et al., 1999), and Bayesian networks (BNs) (Friedman et al., 2000).

The BN is one of the most promising models for learning genetic regulatory networks because of its ability to deal with the noise in experimental measurements and because it can handle missing data and incomplete knowledge about the biological system. However, learning BNs is a nondeterministic polynomial time (NP)-hard problem.

## Bayesian networks and particle swarm optimization

## Bayesian networks and structure learning

BNs, known as directed acyclic graphs (DAGs), can be used to represent causal relationships among a large number of random variables in a graph. This is essentially a model of the pattern of an uncertain inference network that is based on probability. The BN was first proposed by Pearl Judea in 1987 (Judea, 1987). BN learning includes structure learning and parameter learning. The network structure, which is the qualitative part of the model, is used to describe the probability dependencies between variables. The DAG consists of two parts: nodes and directed arcs, where the nodes represent random variables and arcs represent statistical dependence relations among the variables in the problem areas. The conditional probability table indicates the dependence degree between the variables. If $X$ is a non-root node, its conditional probability distribution can be expressed as $P(X \mid P a(X))$, where $P a(X)$ is the parents set of node $X$; if $X$ is a root node, its marginal distribution is $P(X)$. The conditional probability distribution and the marginal distribution of all nodes form the conditional probability table.

Assume that the network has $N$ nodes, marked as $X_{i} \ldots X_{N}$, and $P$ is the conditional probability of the node $X_{i}$ that can be calculated as follows:

$$
P\left(X_{1}, \ldots X_{N}\right)=\prod_{i=1}^{N} P\left(X_{i} \mid P a\left(X_{i}\right)\right)
$$

Definition 1: Let $G=(V, E)$ be any of a DAG and $P$ is the joint probability distribution defined on the set $V$ of random variables that satisfy the Markov condition. Then, $B=(G, P)=$ $(V, E, P)$ is defined as the BN (Neapolitan, 2002).

Definition 2: Let $G=(V, E)$ be a DAG with a node $X \in V$ that is defined as the following:

$$
a_{i j}=\left\{\begin{array}{l}
1,\left(X_{1}, X_{j}\right) \in E \\
0,\left(X_{1}, X_{j}\right) \in E
\end{array}\right.
$$

Then, $\mathrm{A}=\left(a_{i j}\right)$ is the adjacency matrix of graph G (Liu, 2001).
BN structure learning is used to find the best DAG match to the data set. Usually, the structure learning method is used to evaluate whether the DAG is a good match of this data set by defining a score function. Then, the structure graph is identified using the optimal score. There are common scoring criteria, such as the maximum likelihood score, Bayesian information criterion (BIC) score, minimum description length (MDL) score, and Bayesian Dirichlet equivalence (BDe). This paper intends to use the BDe score criteria, which can be used to calculate the posterior probability P of the structure G under the premise of a given data set to evaluate the BN.

So far, many people have presented different approaches to learning the structures of BNs. In 1992, the classical K2 algorithm proposed by Cooper and Herskovits (Cooper and Herskovis, 1992) was found to be the most successful algorithm, but it is heavily dependent on a prior order. In 2003, Chickering presented the greedy search (GS) algorithm (Chickering, 2002), which easily falls into the local optimal value. In 2007, Heng et al. proposed the discrete particle swarm optimization (PSO) (Heng et al., 2007). Subsequently, Sahina et al. introduced the distributed discrete PSO (Sahina et al., 2007). In 2010, T Wang et al. first proposed BN learning based on binary PSO (Wang and Yang, 2010), and J Zhao et al. presented the discrete binary quantum-behaved PSO algorithm (Zhao et al., 2009). This paper explored the combination of the chaotic theory with the PSO algorithm (CPSO) for learning BN structure.

# Particle swarm optimization 

PSO, which was first proposed by Eberhart and Kennedy in 1995 (Kennedy and Eberhart, 1995), is an evolutionary computing technology based on swarm intelligence. This algorithm is inspired by the social behavior of flocking birds. In PSO, each single solution is a "bird" in the search space. The PSO algorithm has the advantages of simple program design, few adjustable parameters, and a fast convergence rate at the early stage of the search. However, it easily falls into the local optimum later. The population of PSO is called a swarm, and each individual in the population of PSO is called a particle. Each particle's position is denoted as a D-dimensional vector $X_{i}=\left(x_{i 1} x_{i 2} \ldots x_{i D}\right)$. The $i_{i h}$ particle's velocity is represented by $V_{i}=\left(v_{i 1}\right.$ $\left.v_{i 2} \ldots v_{i D}\right)$. In every search iteration, each particle is updated by following the two best values. The first value is the best solution (fitness) that the model has achieved so far. The fitness value is also stored. This value is denoted as $p_{i}=\left(p_{i 1} p_{i 2} \ldots p_{i D}\right)$. Another best value that is tracked by the particle swarm optimizer is the best value that is obtained so far by any particle in the population. This best value is the global best and is denoted by $P_{g}=\left(p_{g 1} p_{g 2} \ldots p_{g D}\right)$. After finding the two best values, the particle updates its velocity and positions with the following formulas:

$$
\begin{gathered}
\dot{v}_{a t}^{k+1}=\omega \dot{v}_{a t}^{k}+c_{1} r_{1}\left(p_{a t}^{k}-x_{a t}^{k}\right)+c_{2} r_{2}\left(p_{p t}^{k}-x_{a t}^{k}\right) \\
x_{a t}^{k+1}=x_{a t}^{k}+v_{a t}^{k+1}
\end{gathered}
$$

Here, $p_{i}$ is the best previous position of the $i_{i 0}$ particle (also known as pbest), and $p_{p}$ is the best position among all of the particles in the swarm (also known as gbest). $k$ represents the iterative number, $i=1,2, \ldots, N$ and $d=1,2, \ldots, D$. The variables $c_{1}$ and $c_{2}$ are learning factors, where usually $c_{1}=c_{2}=2$, and $r_{1}$ and $r_{2}$ are random values in the range of $[0,1] . \omega$ is the inertia weight in the equation of velocity updating. A larger inertia weight facilitates global exploration, and a smaller inertia weight tends to facilitate local exploration to fine-tune the current search area. The termination criterion for the iterations is determined according to whether the max generation or a designated value of the fitness of $p_{p}$ is reached.

Currently, the PSO algorithm has been used to develop calculation models in the form of position-speed, such as the inertial weight-PSO model, convergence factors-PSO model, and discrete and binary-PSO models. The performance of PSO models is different when solving different optimization problems because inertia weight can effectively regulate global and local searches. The design of the inertia coefficient has become the focus. This paper will design an inertia weight coefficient to improve the PSO models and gain the optimum network structure.

# Structure learning algorithm based on chaotic PSO 

## Chaos theory

It is well recognized that chaos theory can be applied as a very useful technique in practical applications. The chaotic system can be described by a phenomenon in which a small change in the initial condition will lead to a nonlinear change in future behavior. Chaos optimization is a new search algorithm; its basic idea is to transform the variables from the chaos space to solution space. It searches optima by means of regularity, ergodicity, and intrinsic stochastic properties of chaotic motion, and it can identify the global optimum. The chaos optimization algorithm has the advantages of global asymptotic convergence and a fast convergence rate. Besides, it is easy to skip the local minima. These advantages can overcome the drawback of the standard PSO algorithm. When particles get into a local extremum, the chaos search strategy is introduced into PSO (Meng et al., 2004) to guide the particle swarm toward the best solution.

The chaotic map has a determinate form and does not contain any random factors. However, it can produce a dynamic change phenomenon that seems completely random, and it is extremely sensitive and dependent on the parameters.

One of the simplest maps, the logistic map proposed by May in 1976 (May, 1976), can be described by the following equation:

$$
\omega_{i+1}^{*}=\mu^{*} \omega_{i}^{*}\left(1-\omega_{i}\right) \quad i=1,2, \cdots, N
$$

Here, $\mu>3.57$ and $\omega_{i} \notin\{0.0,0.25,0.5,0.75,1.0\}$. When $\mu=4$, system (5) iteratively produces a status of the pseudo-random distribution, which is a completely chaotic state.

Tian and Zhao (2010) improved the algorithm so that the tent-PSO has not only the powerful ability to search the global optimum but also effectively avoid the premature convergence in time. The tent map that was proposed (Shan et al., 2005) is given as the following:

$$
\varrho_{\mathrm{Pr} 4}= \begin{cases}2^{*} \varrho_{1}, 0 \leq \varrho_{2} \leq 0.5 \\ 2^{*}\left(1-\varrho_{2}\right), 0.5 \leq \varrho_{2} \leq 1\end{cases}
$$

An arbitrary initial value $\omega_{0} \in[0.0,1.0]$ can iterate a certain sequence $\omega_{1}, \omega_{2}, \omega_{3}$, etc. Because of the sensitive dependence on the chaotic initial value, we take the experienced value $\omega=0.7298$, which iteratively produces a certain sequence $\omega_{1}, \omega_{2}, \omega_{3}$, etc. Finally, the chaotic sequence replaces the linear decreasing weight to identify the optimal particle.

The chaotic sequence is generated in $[0.0,1.0]$ by (6). This paper intends to limit the inertia weight value in $[0.4,0.9]$, so we selected the improved tent map (Zhang et al., 2008) to limit the range in $[0.4,0.9]$. The chaotic sequence is generated by the following formula:

$$
\varrho_{\mathrm{Pr} 4}= \begin{cases}\varrho_{1} / a, 0.4 \leq \varrho_{2} \leq a \\ \left(1-\varrho_{2}\right) /(1-a), a \leq \varrho_{2} \leq 0.9\end{cases}
$$

In summary, we can use the chaotic characteristics to effectively improve the diversity of the population and the ergodicity of the particle search, create a better balance between the global and local optimization search, and avoid premature convergence.

# Coding scheme 

Because of the special form of the initial particle, we encoded the BN structure utilizing the coding scheme introduced by Poza (Larrañaga et al., 1996). A BN structure B with $N$ nodes is represented by an $N * N$ adjacent matrix where any dimension is dispersed as 0 or 1 . In the model of PSO, every particle is a BN structure, and each adjacent matrix is one solution of the problem. An example is shown in Figure 1:
![img-0.jpeg](img-0.jpeg)

$$
X=\left[\begin{array}{llll}
0 & 1 & 1 & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & 0 & 1 \\
0 & 0 & 0 & 0
\end{array}\right]
$$

Figure 1. The structure of BN and its adjacent matrix.
It can be seen from the adjacent matrix in Figure 1 that $x_{i j}$ represented the relationship between node $i$ and node $j$ : if node $i$ is a parent of node $j$, then the matrix element $x_{i j}$ $=1$; otherwise $x_{i j}=0$. In the vector set $x_{i}=\left(x_{1 i} x_{2 i} \ldots x_{n i}\right), x_{i}$ is the parent vector of node $i$ and represents the edges from other nodes to node $i$ in the network. The velocity, $v_{i j}$, represented the variation between node $i$ and node $j$. This is a special probability parameter

to change the particle position. A transfer function $\sigma\left(v_{i j}{ }^{k+1}\right)$ is expressed by the following equation (Wang and Yang, 2010):

$$
\sigma\left(\boldsymbol{v}_{i j}^{k+1}\right)=\frac{1.0}{1.0+e^{-v_{i j}^{k+1}}}
$$

Equation (3) is used to update the velocity vector of the particle, and equation (8) can obtain a $\sigma$ value of the velocity. The new position of the particle is obtained using the following equation:

$$
\boldsymbol{v}_{i j}^{k+1}=\left\{\begin{array}{l}
1, i f \boldsymbol{v}_{i j}^{k+1}>\rho \\
0, \text { otherwise }
\end{array}\right.
$$

In this equation, $\rho$ is a uniform random number in the range $[0.0,1.0]$.
The fitness is calculated using the BDe Bayesian score function mentioned above, and the equation is given below:

$$
F=\lg \left(\prod_{i=1}^{n} \prod_{j=1}^{q_{i}} \frac{\left(r_{i}-1\right)!}{\left(N_{i j}+r_{i}-1\right)!} \prod_{k=1}^{r_{i}} N_{i j k}!\right)
$$

Here, $r_{i}$ is the number of states of node $i$, the first product $N$ is over the nodes in the network, the second product $q_{i}$ is over the set of permutations of the parents of node $i$, and the third product $r_{i}$ is over the states of the node. Also $N_{i j}$ is defined as:

$$
N_{i j}=\sum_{k=1}^{r_{i}} N_{i j k}
$$

Here, $N_{i j k}$ is the elements of node $i$ in the conditional probability table (CPT), which contains occurrences of joint instantiations of the parents where each permutation is indexed with $j$ of node $i$, which is in state $k$. Hence, the sum $N_{i j}$ is the total of a column of the conditional probability table where each column enumerates occurrences of node $i$ in each state for a specific instantiation set of parents.

The function value obtained by equation (10) represents the score of the network structure learning and the degree of fit with the known network structure. The higher the value is, the greater the degree of similarity fitting.

# Novel learning algorithm: BN-CPSO 

In this paper, we used the proposed CPSO algorithm to identify the global best position $p_{g}$, which is a network structure, and to obtain the ordering of the nodes. Then, the K2 algorithm uses the node ordering as an input parameter to obtain the optimal network structure. The following steps show the CPSO and ordered K2 algorithm.

1) Initialize the particle swarms, the parameters containing the number of swarms,

iterations, $c_{1}, c_{2}$, and $\omega$.
2) Encode according to the BN structure and its adjacent matrix. Adopt the maximum weight spanning tree algorithm (MWST) to get the initial DAG.
3) Obtain all adjacency graphs of the DAG using the mk_dag_topo algorithm and select a certain n umber as the initial particle swarm.
4) Calculate the fitness value through the function $F$ of each particle at its current position and find the best value as the global optimal particle.
5) Compare the performance of each particle to its best performance:
if $F\left(\chi_{i}(t)\right)<F\left(p_{i}\right)$
then, $F\left(p_{i}\right)=F\left(\chi_{i}(t)\right)$ and $p_{i}=\chi_{i}(t)$.
6) Compare the performance of each particle to the global performance:
if $F\left(\chi_{i}(t)\right)<F\left(p_{i}\right)$
then, $F\left(p_{i}\right)=F\left(\chi_{i}(t)\right)$ and $p_{i}=\chi_{i}(t)$.
7) Use the tent map equation (7) to obtain the chaotic sequence $\omega_{i}$, and limit the sequence in the range of $[0.4,0.9]$.
8) Calculate a new velocity using equation (3) to change each particle, and discretize it into 0 or 1 according to equations (8) and (9).
9) Change each particle to a new position using equation (4).
10) Go to step (3), repeat the process until convergence or the maximum number of iterations have been reached, and record the global optimal particle $p_{g}$.
11) Transfer the encoding to a matrix and obtain the node ordering from the DAG constructed in the previous step.
12) Run the K2 algorithm to obtain the network structure using the ordered nodes as the input of the K2 algorithm.

# MATERIAL AND METHODS 

## Experiment

In this section, the implementation of the algorithm was written in MATLAB and compiled using MATLAB 2009b. Our algorithm is based on the BN Toolbox (BNT) (Murphy et al., 1997-2002) and its structure learning package (BNT_SLP). The code is completely free to the public. In addition, the system has good scalability, which makes our learning and improvement algorithm more convenient than previous algorithms.

## Parameters

In order to quantitatively evaluate the authenticity of the reconstructed network, this paper used a number of evaluation criteria. Above all, the Bayesian score was adopted. The higher the Bayesian score is, the better the obtained network structure will be. A previous report (Kim et al., 2004) mentioned two criteria: sensitivity and specificity. The following formulas are for the sensitivity and specificity calculation, respectively.

$$
P_{24}=\frac{E_{s}}{E_{22}}
$$

Here, $E_{t}$ represents the correctly estimated edges and $E_{p t}$ indicates all edges in the target network. $P_{s p}$ is the sensitivity, which represents the proportion of the edges that were correctly estimated by the algorithm compared to the real regulation relationships in the network.

$$
P_{s p}=\frac{E_{t}}{E_{a}}
$$

Here, $E_{t}$ represents the correctly estimated edges and $E_{a}$ indicates all estimated edges. $P_{s p}$ is the specificity, which denotes the proportion of the correct estimations in the network.

We defined D as the sum of the removed edges, the added edges, and the reversed edges. We averaged the results from ten experiments.

For the purpose of comparison, all of the simulations used the same parameter settings for the algorithm except the inertia weight $\omega$. Table 1 shows the parameter values for the three algorithms.

Table 1. Parameter values for three algorithms .


$k=$ number of particle; $V_{\max }=$ limit exploration of velocity; $\omega=$ additional inertia weight; $c_{1}=$ local learning factors; $c_{2}=$ global learning factors.

Here, max-parents is the upper boundary of the number of parents a node may have to compute efficiency, $k$ is the number of particles, $V_{\max }$ is the limit exploration of velocity. $\omega$ is an additional inertia weight in the updated equation of velocity and $c_{1}$ and $c_{2}$ are local and global learning factors, respectively.

# RESULTS AND DISCUSSION 

In order to assess the performance of CPSO_BN, we compared with classic K2 algorithm (Leray and François, 2004), the BPSO algorithm (Wang and Yang, 2010), and the chaos hybrid genetic algorithm (CHGA) (Shen et al., 2012) by using data sets that were generated from a known BN that used a probabilistic logic sampling known as ASIA. The Asia network was initially presented by Lauritzen and Spiegelhalter (Lauritzen et al., 1988) and is a small network (eight nodes) that is used in the domain of medical knowledge. The training set with 2000 samples is generated from the original network.

We also applied these algorithms to gene expression data to infer genetic regulatory networks. The microarray dataset we employed is from a previous study on yeast cell-cycle gene regulation (Spellman et al., 1998) and is publicly available. We chose eight histone genes - HHT1, HHT2, HHF1, HHF2, HTA1, HTA2, HTB1, and HTB2 - as our experimental data set. In this paper, we used 77 data samples for these eight genes and compared our results with those from Chen et al. (Chen et al., 2006). The two original networks were shown in Figure 2, and the experimental comparison results were shown in Figure 3 and Figure 4.

From Figure 3, we know that the proposed CPSO and the CHGA (Shen et al., 2012) algorithms both can reconstruct the network efficiently. The proposed method can better predict the initial particle swarm by computing all of the adjacent matrices for the graph of the MWST algorithm.

![img-1.jpeg](img-1.jpeg)

Figure 2. Standard ASIA and gene network of histones.
![img-2.jpeg](img-2.jpeg)

Figure 3. Comparison of ASIA network structure learning.

According to the DAG, we get the 2nd, 3rd, and 4th column data in Table 2 by using the formulas (12) and (13). The data in the 5th column are obtained through the Bayesian scoring function (9).

![img-3.jpeg](img-3.jpeg)
order K2 DAG
![img-4.jpeg](img-4.jpeg)

CPSO DAG

Figure 4. Comparison of gene network of histones structure learning.

Table 2. Comparison of the various algorithms.


From Table 3, we can see that, for all data sets, the Bayesian score of our CPSO algorithm is higher than that from the K2 and BPSO algorithms, which indicates that our algorithm can identify networks that are close to the optimal structures.

Table 3. Comparison of BDe with various datasets.


As illustrated in Figure 4, compared with the results from Chen et al. (Chen et al., 2006), the CPSO method uncovered $93 \%$ (13 out of 14 ) of the currently known interactions among them. The dashed line predicts the unsupported edge, and the green line indicates the reversed edge. Experimental evidence may support some currently unsupported edges of the

constructed network in the future. Therefore, these unsupported edges are not necessarily false ones. The interaction between HTA1 and HTB1 may be a mutual regulatory relationship; we will study the relationship in equivalence class space.

# CONCLUSIONS 

This paper presented a new method for BN learning. The proposed method identifies the ordering of nodes for the K2 algorithm using CPSO. We used the chaotic map to update the particles, and the proposed method improved the quality of the obtained network structure and enhanced the convergence of the particle. Although the algorithm uncovered some interactions that were novel and currently unknown, the validation of the new interactions is beyond the scope of this article. The possibility of mutual regulatory relationships provides a future research direction.

## ACKNOWLEDGMENTS

Research supported by the National Natural Science Foundation of China (\#31370778, \#31170797, \#30870573, \#61103057), the Program for Changjiang Scholars and Innovative Research Team in University (\#IRT1109), the Program for Liaoning Excellent Talents in University (\#LR201003), and the Program for Liaoning Science and Technology Research in University (\#LS2010179).
