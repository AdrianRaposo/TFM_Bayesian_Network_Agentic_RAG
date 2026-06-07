# Article 

## Optimization of Active Learning Strategies for Causal Network Structure

Mengxin Zhang and Xiaojun Zhang *<br>School of Mathematical Sciences, University of Electronic Science and Technology of China, Chengdu 611731, China; 13086679190@163.com<br>* Correspondence: sczhxj@uestc.edu.cn


#### Abstract

Causal structure learning is one of the major fields in causal inference. Only the Markov equivalence class (MEC) can be learned from observational data; to fully orient unoriented edges, experimental data need to be introduced from external intervention experiments to improve the identifiability of causal graphs. Finding suitable intervention targets is key to intervention experiments. We propose a causal structure active learning strategy based on graph structures. In the context of randomized experiments, the central nodes of the directed acyclic graph (DAG) are considered as the alternative intervention targets. In each stage of the experiment, we decompose the chain graph by removing the existing directed edges; then, each connected component is oriented separately through intervention experiments. Finally, all connected components are merged to obtain a complete causal graph. We compare our algorithm with previous work in terms of the number of intervention variables, convergence rate and model accuracy. The experimental results show that the performance of the proposed method in restoring the causal structure is comparable to that of previous works. The strategy of finding the optimal intervention target is simplified, which improves the speed of the algorithm while maintaining the accuracy.


Keywords: causal networks; structure learning; active learning; optimal design; Markov equivalence class; intervention

MSC: 62D20

## 1. Introduction

Recently, the learning of the causal relationships behind complex systems has become a major topics. Researchers can use the causal relationship to address certain issues, such as identifying the direct cause of a certain instrument's failure or exploring the impact of a new vaccine on a disease. However, in most cases, we cannot determine the complete causal relationship between the variables that we wish to explore through observational data alone; we require more data to support our experiments. Some hybrid algorithms can improve the sensitivity, accuracy and speed of causal structure learning [1]. A common way to improve the identifiability is to design optimal intervention experiments, which aim to fully restore the causal graph with the smallest intervention or pursue some other goal to obtain the causal relationships between random variables.

Directed acyclic graphs (DAGs) are commonly used to represent causal structures, where each node is a random variable. In a DAG, every directed edge has practical meaning. $X \rightarrow Y$ reveals that $X$ is the direct cause of $Y$ [2]. Only a series of Markov equivalence classes (MECs), a set of DAGs that reflect the same conditional independence between random variables, can be obtained by the observational data, while there are still some unoriented edges. One way to improve the identifiability of a causal graph is to use interventional data for estimation. An intervention is realized by forcing the values of one or several random variables of the system to specific values, destroying their original causal dependencies [3]. The realistic costs of intervention experiments are usually high;

for example, in many medical settings, there is a large amount of observational clinical data, and randomized controlled trials are expensive to organize [4]. Thus, we aim to determine the true and complete causal structure with minimal intervention.

In the last fifteen years, a variety of methods have been proposed for the active learning of causal models, all of which take into account the optimization of the sequence of identifiability of causal graphs [5-10]. He and Geng proposed an active learning method to discover causal structures. They first found a Markov equivalence class from observational data and then oriented undirected edges through intervention experiments [6]. After this, they proposed two types of optimal design experiments; the intervention experiment was based on minimax and the maximum entropy criteria to determine the intervention target. Remarkably, their intervention experiments were conducted independently on each chain component. Hauser and Bühlmann extended the concept of essential graphs to the case of intervention and described the nature of the essential graph of intervention [7]. They then elaborated a set of algorithmic operations to efficiently traverse the search space of the intervention essential graph and finally gave the GIES algorithm. After this, Hauser and Bühlmann (2014) proposed active learning strategies to design optimal interventions for two different learning goals [9]. The first was to maximize the number of edges that can be directed after each intervention under the premise of a single vertex intervention. The second method produces a minimum intervention set of any size in polynomial time to guarantee the identifiability of the causal graph. Greenewald et al. proposed an approximation algorithm for tree-structured causal graphs based on the central node concept [4]. They considered the problem of experimental design for the learning of tree-structured causal graphs and thus proposed an adaptive framework that determines the next intervention based on Bayesian a priori updates from previous experimental results. Then, an algorithm using a graph structure in the form of centrality measurement was proposed. Recently, Amirinezhad and Salle Kaleybar proposed a solution to an experimental design problem based on deep reinforcement learning to restore causal networks [8]. In this method, they used a graph neural network to embed an input graph into a vector and feed it to another neural network to output a variable to determine the intervention target at each step. The two networks were trained jointly by a q-iterative algorithm.

This paper mainly discusses the problem of causal inference under the framework of causal networks, summarizes the ideas and theoretical basis of the active learning algorithm of causal graph structures, and compares and analyzes the respective applicable scenarios and their advantages and disadvantages. Then, we identify the key points that can be optimized. The main contributions of this work can be summarized as the following two points.

1. We conduct a priori research on the proposed model, synthesize the data in the real Bayesian network library, and propose the theory and results of the algorithm. Then, we find that there are a large number of similar properties between Bayesian networks and causal networks. Meanwhile, the essence of causal graphs is summarized from the data provided by the Bayesian network library. Therefore, it is considered to determine the causal graph structure orientation process in each chain component after the decomposition of the essential graph, which can ensure that each experiment does not have to be repeated on the entire causal graph, thus reducing the experimental cost.
2. Traditional algorithms search for the optimal intervention node by iterating the Markov equivalence class or the complete structure of the causal graph, and they are not considered in our paper. We directly build the search for the optimal intervention node on a simpler chain component structure. At the same time, the important concept of the center of the tree in graph theory is introduced, which is extended to the undirected graph, and the generalized concept of the center is defined for the experiment performed. For each node in the undirected graph, we find the longest path to other nodes (there is no repeated edge) as its eccentricity; then, the center of the undirected graph is the point with the least eccentricity. If there are two center points, according to the results obtained a priori, the center point with more neighbors is chosen as the

center of the whole undirected graph, which is also the optimal intervention node found by the algorithm. Therefore, a new active learning algorithm for causal network structures is proposed.
In Section 2, we introduce important concepts related to causality research, review some preliminary studies of causal structures, and define experimental design problems in active learning environments. In Section 3, we propose the active learning of causal structures via an intervention optimization design based on central points and describe the training algorithm. In Section 4, we show the experimental results to evaluate the performance and compare our approach with previous work. Conclusions are given in Section 5.

# 2. Causal DAGs and Intervention 

We consider a causal model on $p$ random variables $\left(X_{1}, \ldots, X_{p}\right)$, corresponding to a DAG $G$ on the node set $V=[1, \ldots, p]$, which is a directed graph without any directed cycles. Formally, a graph $G$ is defined to be a pair $G=(V, E)$, and $E$ denotes the edge set of graph $G$. If both ordered pairs $\left(V_{i}, V_{j}\right)$ and $\left(V_{j}, V_{i}\right)$ are in $E$, there is an undirected edge between $V_{i}$ and $V_{j}$. In this case, $V_{i}$ and $V_{j}$ are neighbors to each other. If $\left(V_{i}, V_{j}\right) \in E$ and $\left(V_{j}, V_{i}\right) \notin E$, there is a directed edge from $V_{i}$ to $V_{j}$, denoted as $V_{i} \rightarrow V_{j}$. We call $V_{i}$ the parent node of $V_{j}$, and, correspondingly, $V_{j}$ is the child node of $V_{i}$.

### 2.1. Causal Calculus

The study of causal structures is usually based on a series of assumptions, which we will first list and explain.

Assumption 1 (Causal Sufficiency Assumption). The variable set $V$ is considered causally sufficient when the direct cause variable of any two variables in the variable set $V$ exists in V [10].

Assumption 2 (Causal Markov Assumption). For a set of variables with causal sufficiency, all variables are conditionally independent of their non-descendant nodes when the parent node of the variable is known.

Assumption 3 (Causal Faithfulness Assumption). Variables $v_{i}$ and $v_{j}$ are mutually or conditionally independent given variable set $V$. Then, in the causal network diagram $G$ composed of variables and their causal dependencies, all paths between $v_{i}$ and $v_{j}$ are d-separated by some variable in variable set V [11]. At this time, the independence between variables obtained through the independence test can be directly reflected in the causal graph.

A causal model is a pair $(G, f)$, and the corresponding joint probability density is expressed as

$$
f(x)=\prod_{i=1}^{p} f\left(x_{i} \mid x_{p a_{G}}(i)\right)
$$

where $p a_{G}(i)$ is the parent node set of node $i$ in graph $G$. We say that the probability density $f$ that satisfies the above form is subject to the Markov property.

Two graphs have the same skeleton if they have the same set of nodes and the same set of edges (regardless of the orientation of the edges). Considering the existence of directed edges (which cannot form rings) between the three points $\left(V_{1}, V_{2}, V_{3}\right)$ in graph $G$, there are three types, respectively, $V_{1} \rightarrow V_{2} \rightarrow V_{3}, V_{1} \rightarrow V_{2} \leftarrow V_{3}, V_{1} \leftarrow V_{2} \rightarrow V_{3}$. Among them, we call the node $V_{2}$ a collider [12] and the head-to-head structure $V_{1} \rightarrow V_{2} \leftarrow V_{3}$ is called a v-structure. A Markov equivalence class is a set of DAGs with the same Markov properties, which have the same skeleton and v-structure [13]. Alternatively, we can say that two graphs that have exactly the same sets of conditional independences are Markov-equivalent [14].

Causal structure learning usually requires first learning the skeleton of the causal graph and then orienting the undirected edges. The structure learning methods of causal graphs are the method based on score searching [15] and the method based on dependency statistical analysis. The score search method uses the search algorithm and scoring function to score each searched network structure and finally finds the network structure with the highest score. This type of method can easily fall into local optimal solutions.

According to the dependency relationship between variables, the method based on dependency statistical analysis adds a connecting edge between two nodes with greater dependence to obtain an undirected graph. Then, the direction of the edges in the undirected graph is determined according to the inclusion relation and so on, and the final DAG is obtained. To judge whether there is an undirected edge between two variables in the undirected graph model, we must check the single conditional independence of the conditional variable pairs of all other variables [16]. The PC algorithm [17] is one such method; this type of method can obtain the global optimal solution, but, with the increase in nodes, the time complexity of the algorithm will increase quickly. Constraint-based approaches search for causal structures by using independent relationships in successive test data and use the results to constrain the search space. The convergence results can ensure the consistency of these algorithms, i.e., to ensure that the algorithm can recover as much information about the causal structure as possible when the conditional independence relation is true in a given population.

The PC algorithm restores all the causal relationships that can be identified from the data based on the conditional independence test between variables. The algorithm first determines the dependence relationship between nodes (but not the direction), i.e., it becomes an undirected graph, and then determines the direction of dependence. The undirected graph can be extended to a Completed Partially Directed Acyclic Graph (CPDAG) [18].

# 2.2. Active Learning and Intervention Calculus 

Since the network structures constructed according to the conditional independence determined by d-separation are not unique, the PC algorithm cannot obtain complete causal networks. These network structures are merely the Markov equivalence classes of real causal networks. To further learn the directions of unoriented edges in a CPDAG, interventions can be introduced into the active learning of causal structures. Intervention is achieved by forcing the values of one or more random variables to a particular value, destroying their original causal dependence, which means that the value of the variable is determined by the exogenous distribution of any variable in the system. The combination of observation distribution and intervention distribution can greatly improve the recognition of causal structures in the system. Methods based on active learning have been developed in recent decades, using observational data to estimate the essential graph in the first step, and the intervention data are used in the second step to identify unoriented edges. Besides the PC algorithm, the Greedy Equivalence Search (GES) algorithm [19] is also used to estimate the essential graph. There are two research directions for the orientation problem: one is to find the optimal intervention strategy, i.e., how to choose the node for intervention; the other is to discuss various conditions and restrictions in the intervention process.

We consider stochastic experiments [20] in which one or more random variables $X_{I}$ are set or forced to a specific value, where $I \in V$ is the selected intervention target. In this section, some variables are manipulated from an external intervention that would disconnect the node $V_{i}(i \in I)$ from its parent node $P a\left(V_{i}\right)$ in graph $G$ by assigning individuals probabilistically to certain levels of these variables. Thus, the pre-intervention conditional probability density $f\left(x_{i} \mid x_{p a_{G}}(i)\right)$ is replaced by the post-intervention probability $f\left(x_{i}\right)$. After randomization, the association of the remaining variables with the intervention node provides information about which variables are affected by the intervening node [21]. Specifically, the main assumption that we will make in order to obtain several causal identification results is that the intervention is local and that it does not change the causal

mechanism of any variable other than the intervention variable. Then, the post-intervention joint probability density is

$$
f_{I}(x)=\prod_{i \notin I} f\left(x_{i} \mid x_{p a_{G}}(i)\right) \prod_{i \in I} \hat{f}\left(x_{i}\right)
$$

Assume that $X_{I}$ represents the intervention target of the set of intervention vertices $I \in\{1 \ldots, p\}$ with (univariate or multivariate) intervention. We consider modeling the effect of setting or forcing one or several random variables $X_{I}$ to the value of independent random variable $U_{I}$. We assume that the densities for the intervention values are Gaussian as well [22]:

$$
U_{j} \sim \mathcal{N}\left(\mu_{U_{j}}, \tau_{j}^{2}\right), \quad j=1, \ldots, p
$$

$U_{1}, \ldots, U_{p}$ are independent of each other.
Intervention can determine the direction of causation: if $A$ is the direct cause of $B$ and the intervention is on A , then A and B will appear correlated, and if the intervention is on B, A and B will appear independent. In stochastic experiments, for any variable node $x$ adjacent to intervention node $v$, if, according to the dependent test, $x \Perp v$, then we orient $x \rightarrow v$; otherwise, $x \leftarrow v$ [23]. In any real experimental environment, there will be errors in the conditional independence test. When looking for a causal structure between a set of variables, whether or not there is a particular causal arrow between $X$ and $Y$ depends on some set of conditions that make the two variables independent of each other. In a large dense network, the search may require a large set of conditions to determine adjacency. Therefore, the likelihood that all independent tests will return correct results decreases as the number of tests increases.

# 3. Optimization Design of Stage Intervention Based on Central Point 

If only observational data are available, in most cases, only part of the causal relationship can be identified. If sufficient experiments can be carried out in the system, all causal relationships can be restored. However, in many applications, the cost of intervention systems may be too high. Therefore, it is necessary to design optimal experiments in order to find a set of intervention targets with the smallest scale to adequately identify causality, which is also the key to learning the structure of causal networks.

The local orientation method of causal networks is used to orient the causal network in each chain component. This method has been used to theoretically prove that as long as no v-structure or ring is generated in any chain component, no new v-structure or ring will be generated in the whole after the intervention is over. Based on this theory, this section proposes a staged structural learning algorithm so that the orientation of causal networks is locally performed in each chain component, and the intervention is conducted as a randomized experiment in which some variables are manipulated from external intervention by assigning individuals to certain levels of the variables in a probabilistic manner. At this point, random intervention $V_{i}$ disconnects the node from the parent node $p a\left(V_{i}\right)$. In the post-intervention distribution, the intervention variable $V_{i}$ is independent of its parent variable $p a\left(V_{i}\right)$, and orientation only requires an independent correlation test for the marginal distribution of the variables corresponding to the two endpoints of the undirected edge.

The design of the optimal experiment is based on the prior knowledge that all causal networks are directed acyclic graphs, which contain a large number of structures obtained from the observed data, and therefore corresponding essential graphs are chain graphs. Considering the property of the chain graph, after removing its directed edges, many connected chain branches will be obtained, and a large number of chain branches are tree structures. Therefore, the optimal experimental framework is built on the characteristics of the tree. In addition, in theory, important nodes in the causal network should contain more information and be as related as possible to other nodes. After analyzing the structure of a

Bayesian network in the Bayesian network library, combined with the above analysis, this section puts forth the active learning algorithm of causal network structures based on the central node.

# 3.1. Decomposition of Essential Graph 

The essence of a causal graph is a DAG. The nodes and edges in the graph contain a lot of useful information, which can assist us in finding the best intervention node [4,24,25]. Therefore, we aim to find some key nodes in the graph as the target of intervention. The essential graph obtained by the PC algorithm has both directed and undirected edges; if there is no partially directed cycle, it is called a chain graph, as shown in Figure 1a.
![img-0.jpeg](img-0.jpeg)

Figure 1. Decomposition of essential graph. (a) Essential graph. (b) After removing the v-structure in the essential graph, four interconnected chain components are formed. (c) The optimal intervention target is found in one of the chain components. (d) After removing all directed edges, continue to look for intervention targets in the remaining chain components.

Intervention experiments can be conducted locally in chain components without the need to check for illegal v-structures and cycles [6], as shown in Figure 1. It is assumed that Figure 1a is an essential graph obtained by the PC algorithm through learning observation data, which contains two v-structures. In our structure learning algorithm, all v-structures will be removed to obtain the four chain components in the second stage, as shown in Figure 1b. For each chain component, the optimal intervention target will be found to orient the undirected edges. After this, the above steps will be repeated until all chain components are oriented. We call these steps the decomposition of the essential graph [26].

He and Geng (2008) proposed two intervention criteria: maxmin and maxentropy [6]. Hauser and Bühlmann (2014) proposed two algorithms, namely the sequential intervention algorithm and batch intervention algorithm, to select intervention targets. The goal is to maximize the number of orientable edges after each intervention [9]. Amirinezhad et al. (2022) used graph neural networks to embed input graphs into vectors and calculated the embedding vectors for each node through the embedding network [8]. The scoring network then returns a score to each node according to its embedding vector, and the node with the highest score is selected as the intervention target.

### 3.2. A Priori Analysis of Model

To find the optimal intervention node from a new perspective, it is necessary to conduct an in-depth analysis of the causal network structure to explore its structure. For this purpose, the experimental model is firstly analyzed a priori, and the rules are found from the real data and the existing results. The following two prior methods are proposed.

### 3.2.1. Priors Based on Real Bayesian Networks

There are many similarities between Bayesian networks and causal networks, and some reference Bayesian networks are often used as benchmarks in the literature. They are available in different formats from several sources, the most famous of which is the Bayesian

Network Repository located at the Hebrew University of Jerusalem. More networks are available from various studies that use Bayesian networks to analyze data from various fields. In the process of causal network structure learning, in order to explore the network structure to find a more suitable intervention method, the Bayesian network library is first selected for structural analysis. These Bayesian networks were partly derived from real experiments and partly from the literature, and the causal relationship between variables was explored through a large number of data and experiments. Some examples are the "CANCER" network and "CHILD" network, as shown in Figures 2 and 3.
![img-1.jpeg](img-1.jpeg)

Figure 2. "CANCER" network.
![img-2.jpeg](img-2.jpeg)

Figure 3. "CHILD" network.
With these real Bayesian networks, it can be seen that there are usually a large number of v-structures; after removing these v-structures, a large number of the remaining connected chain branches are tree structures. Given the above conclusions, the active learning algorithm process of the causal network structure is based on the decomposition of the graph, and a large number of chain components satisfying the tree structure have been obtained, thus simplifying the experimental process. Furthermore, the intervention experiment can also be considered to focus on the tree structure and take some key nodes in the tree as the best intervention targets.

# 3.2.2. A Priori Analysis Based on the Results of Existing Algorithms 

The learning to determine the causal network structure will be carried out on each chain component of the chain diagram, and then the method to determine the optimal intervention target will be found from the structure of the chain branch. Firstly, the results of existing algorithms are explored.

In the algorithm proposed by He in 2008 to find the optimal intervention node based on the Markov equivalence class with the maximum entropy, the optimal intervention targets found are all in the center of the causal graph and usually have more neighbor nodes [6]. An example of this algorithm is shown in Figures 4 and 5. Figure 4 uses $X_{2}$ or $X_{3}$ as the optimal intervention node for the diagram. Figure 5 shows $X_{1}$ or $X_{2}$ as the optimal intervention node.

Frederick Eberhardt's nearly optimal intervention set algorithm for causal discovery considers all possible directed acyclic plots over a variable to arrive at the conclusion that the necessary and sufficient number of worst-case experiments can be specified as a function of the largest clique in a Markov equivalence class [14]. The algorithm greedily approximates the optimal selection of the intervention set by considering the order of the size of the largest clique and the order of the number of times that its vertices appear in the clique. As we can see from Figure 6, the best intervention node that the algorithm finds in the example is $W$ or $X$.
![img-3.jpeg](img-3.jpeg)

Figure 4. Algorithm example 1.
![img-4.jpeg](img-4.jpeg)

Figure 5. Algorithm example 2.
![img-5.jpeg](img-5.jpeg)

Figure 6. Algorithm example 3.
Amir Amirinezhad proposed an experimental design problem solution based on deep reinforcement learning in 2022, with the goal of sufficiently determining causal structures with minimal interventions [8]. The scheme uses a graph neural network to embed input graphs in vectors and feed them to another neural network that outputs a variable that is used to perform the intervention at each step.In Figure 7, the optimal intervention node their algorithm finds is $X_{1}$.

![img-6.jpeg](img-6.jpeg)

Figure 7. Algorithm example 4.
To summarize, the following a priori conclusions can be reached.

1. The essential diagram of the causal network structure is a chain diagram. When the directed edge is removed, each connected chain branch obtained has a large number of tree structures. Therefore, the intervention experiment can be carried out in each chain branch to simplify the experimental process and reduce the cost.
2. From the conclusions of existing algorithms, it can be inferred that the optimal intervention target selected by structural learning is usually a special node in the causal graph, which is in the central position of the graph and has more neighbor nodes. Therefore, the causal network outcome active learning algorithm based on the central node is proposed.

# 3.2.3. Active Learning Algorithm Design 

In this paper, We first explore the characteristics of the intervention nodes found by various methods in previous studies, and we find that the intervention targets found by these methods have some special properties within the whole causal graph. Thus, some key nodes in the DAG are considered as intervention targets based on the graph structure of the causal graph. Our purpose is to simplify the selection rules of intervention targets and improve the algorithm's speed without a loss of accuracy. We do not need to traverse all possible Markov equivalence classes, but, according to the relationships between nodes and the position of each node in the DAG, we can determine the intervention target, thus introducing an important concept in graph theory: the "center point". In general, a center point is a special node in a "tree" graph, where the concept of eccentricity is illustrated. Let $v$ be a node in a tree; then, $e(v)$ is the eccentricity of point $v$ in tree $T$.

$$
e(v)=\max \{d(u, v) \mid u \in v\}
$$

Each point in the graph has a corresponding eccentricity, and the magnitude of the eccentricity is equal to the maximum value of the shortest distance between this point and the other points. The radius of the tree is defined as the minimum value of eccentricity of all the vertices, which is

$$
r(T)=\min \{e(v) \mid v \in V\}
$$

Now, we define the concept of the center: for a point $v$, if $e(v)=r(T)$, then $v$ is a central point, and the set of all central points is called the center of the tree.

The leaf node of the tree cannot be the center. If we delete the leaf node and the edge of the tree and the remaining node is not a leaf, then this point is the center. There can only be one or two such points. By extending the concept of the center to the general graph $G$, the center point of graph $G$ can also be found. For example, Figure 8 shows the central nodes of different types of graphs. In Figure 8a, after finding the eccentricity of each point, it is easy to see that the point corresponding to the eccentricity of $e(v)=3$ is the central point of the tree. By extending this concept to a general undirected graph, we can also find the center of the graph. At this time, the graph has two central nodes, and the following rules exist in our active learning strategy.

Rule 1 (MaxAdj): If the active learning algorithm generates more than one intervention target in the process of finding the intervention target, the intervention target with the largest number of neighbor nodes will be found as the optimal intervention target.

Rule 1 applies when there are two central nodes in a chain component. In this case, the node with the largest number of neighbor nodes is selected as the optimal intervention target. This is done in order to optimize the number of intervention nodes, which is related to the cost of the experiment. However, a small amount of speed and accuracy may be lost, because it means that more independence testing is required. There are two orientation rules in our algorithm, as follows.
![img-7.jpeg](img-7.jpeg)

Figure 8. The center points of different types of graphs. (a) Center point of a tree. (b) Center point of a undirected graph.

Rule 2: When each chain component is oriented, the remaining undirected edges are further oriented without generating a v-structure.

Rule 3: When each chain component is oriented, the remaining undirected edges are further oriented without generating a directed circle.

Algorithm 1 is a single-vertex intervention algorithm based on the central point. The input is the essential graph and the corresponding adjacency matrix. The final output will be the intervention target set and a fully oriented graph $G_{\text {final }}$. We first use the PC algorithm to obtain the essential graph of the causal graph, and then remove all the directed edges. For each connected component, the central point is found as the alternative intervention target at this stage; then, we chose the optimal intervention target by using Rule 1 and the direction of the unoriented edge is further determined. Then, we judge whether all the existing connected branches still have undirected edges. If so, we return to Step 2 and remove all directed edges from the updated graph, resulting in a smaller set of connected components. We continue to look for the intervention target until all the connected components do not have directed edges, and a completely directed causal graph is obtained finally.

# Revision: 

The time complexity of the algorithm is

$$
\left(\frac{\left\lceil\frac{p}{l}\right\rceil\left\lceil\frac{p}{l}-1\right\rceil}{2}\right)!n^{3} l
$$

For a complete graph with $p$ points, the number of times that it needs to perform independence tests is $\left[\frac{p(p-1)}{2}\right]!$. Assuming that the essential graph has $l$ connected components after decomposition, considering the extreme case, the largest connected component should have $p-l+1$ points; then, at most, $\left[\frac{(p-l+1)(p-l)}{2}\right]!$ conditional independence tests are required. If we consider the almost complete isopartite diagram of part $l$, the largest connected component has $\left\lceil\frac{p}{l}\right\rceil$ points; according to the above analysis, the time complexity of the algorithm is as shown in Equation (6) for the almost complete equal part diagram of part $l$, where $n$ is the size of the sample data corresponding to the variables in the figure, and $l$ is the number of chain components.


# 4. Experimental Evaluation 

In this section, we evaluate the active learning methods and optimize the design through simulation experiments. We first find an essential graph through the PC algorithm and then use the method proposed in this paper to locate the undirected edges. The experimental procedure is as shown in Figure 9: we first generate a DAG under a Gaussian causal model as the real graph and then generate corresponding sample data of size $n$. Then, we find an essential graph using the PC algorithm and obtain an optimal design according to our algorithm. Next, we generate intervention data of size $n$ to orient the undirected edges until a DAG is determined.
![img-8.jpeg](img-8.jpeg)

Figure 9. Intervention experimental procedure.
Our experiment is divided into two parts. The first part tests the performance of our proposed algorithm, and the second part is a comparative experiment. The experiment

is based on a randomized design, and the observational data and experimental data are both of a Gaussian distribution in the first part. Therefore, the independence of the intervention variable and its adjacent variables can be tested with the experimental data through a two-sample $t$-test at the $5 \%$ level, i.e., the direction of the undirected edge can be determined. The proposed algorithm is simulated 1000 times each under the combination of node number $p=\{5,8,10,20,30\}$, sample size $n=\{500,1000,5000\}$, and PC alpha $\alpha=\{0.01,0.05,0.1,0.5\}$. We consider comparative experiments in three directions, and the criteria for the selection of the optimal intervention target are completely different. The maxentropy criterion and maxmin criterion proposed by He and Geng (2008) are based on the Markov equivalence class [6]. The batch intervention algorithm proposed by Alain Hauser (2014) (named OptUN) finds the optimal intervention target of any size without decomposing the CPDAG [9]. "Optimal" means that the proposed intervention target guarantees the maximum number of edges that can be oriented after the intervention. Our algorithm and the random criterion are based on the graph structure itself. The random criterion selects a random point in each chain component. We compare the algorithms from three perspectives: the number of intervention nodes, the algorithm's precision, and the algorithm's speed.

The maxentropy criterion and maxmin criterion both choose a variable $V$ based on the Markov equivalence class, which means that when the number of vertices $p$ increases, the complexity of this algorithm will increase too. For graphs with a large number of vertices, it is very difficult to list all Markov equivalence classes.

We introduce the structural Hamming distance (SHD) to assess the quality of the causal model. The SHD between the real graph $G_{0}$ and the estimated graph $G_{\text {final }}$ is the sum of the false positive and false negative results for the skeleton and the misoriented edge. Formally, if graph $G_{0}$ and graph $G_{\text {final }}$ have adjacency matrices $A$ and $D$, respectively, their similarity can be represented by the SHD expressed by Equation (7) [22]:

$$
\operatorname{SHD}\left(G_{0}, G_{\text {final }}\right):=\sum_{1 \leq i<j \leq p}\left(1-\mathbb{I}_{\left(A_{i j}=D_{i j}\right) \cap\left(A_{j i}=D_{j i}\right)}\right)
$$

# 4.1. Results 

### 4.1.1. Experimental Results of Optimal Intervention Design Algorithm

First, we use the pcalg package in Rstudio 4.2.3 to generate a random DAG and corresponding observation data [27]. We define the average number of intervention nodes (ANI) and simulate 1000 experiments for the number of vertices $p=\{5,8,10,20,30\}$ under the condition of sample size $n=\{500,1000,5000\}$ and PC alpha $\alpha=\{0.01,0.05,0.1,0.05\}$. After every 1000 experiments, we calculate the average value of the required intervention nodes, as shown in Formula (8):

$$
A N I=\frac{\sum_{i=1}^{1000} N_{i}}{1000}
$$

where $N_{i}$ is the number of intervention nodes required for each experiment to fully orient an essential graph, and $i$ is the number of experiments. We use the profiler that is included with R and Matlab R2022b to record the running time of the program.

Table 1 shows the experimental results of our proposed single-vertex intervention algorithm based on the central node. In total, 1000 experiments were conducted for different nodes to randomly generate DAGs obeying the Gaussian causal model under the chosen number of nodes, and we generated samples of three sizes for graph structure learning. Then, intervention data with the same sample size (also subject to a Gaussian distribution) were generated for further orientation. The final result of our experiment is shown below. PCSHD is the difference between the essential graph obtained by the PC algorithm and the true DAG skeleton, which is the sum of false positives (excess edges) and false negatives (underestimated edges). SHD is the difference between the estimated DAG and the real DAG, reflecting the accuracy of the algorithm's estimation; it should be noted that the SHD here

includes the estimation error of the PC algorithm. Each sample size in Table 1 corresponds to four levels of PC alpha. It can be seen from the results that for the vertices of small samples, the PC algorithm has a better estimation effect when $\alpha$ is large, and the estimation accuracy of the PC algorithm is improved with the increase in the sample size. For DAGs with more than 10 nodes, it is more suitable for small alpha values. When $\alpha$ is too large, such as alpha $=0.5$, the algorithm's results will be abnormal. This is because the alpha controls the results of the conditional independence test, and it will lead to errors in the test.

Table 1. The simulation results of the proposed algorithm.


Figures 10 and 11 show the PCSHD and SHD sizes of the causal graph for each vertex number under different sample sizes of experimental data. It can be seen that the most important parameters affecting the accuracy of the algorithm are the parameters of the control conditional independence test in the PC algorithm. For experiments with different numbers of nodes and different sample sizes, the inflection point of the curve line of the algorithm's accuracy shows almost the same trend, i.e., the estimation results of the essential graph have a great impact on the estimation of the overall causal network structure. It can be seen from the results that when the scale of the causal network increases, the influence of the sample size on the experimental results becomes less significant. Since the PC algorithm can generate errors, in order to evaluate the orientation performance of our algorithm, we simply define the orientation capability (OA) as

where $E N$ is the sum of the number of edges of the random true DAG generated for each of the 1000 experiments. This setting is rough, because the PC algorithm will not only recognize the skeleton but also obtain part of the v-structure, so the incorrect edges contained in the SHD may arise from the PC algorithm. Since all experiments used the OA to determine the ability of the algorithm, we believe that the results of the real algorithm are better than the experimental results.

The number of vertices $\boldsymbol{p}=5$
![img-9.jpeg](img-9.jpeg)

The number of vertices $\boldsymbol{p}=8$
![img-10.jpeg](img-10.jpeg)

The number of vertices $\boldsymbol{p}=10$
![img-11.jpeg](img-11.jpeg)

The number of vertices $\boldsymbol{p}=5,8,10$ in different sample sizes.

The number of vertices $\boldsymbol{p}=5$
![img-12.jpeg](img-12.jpeg)

The number of vertices $\boldsymbol{p}=8$
![img-13.jpeg](img-13.jpeg)

The number of vertices $\boldsymbol{p}=8$
![img-14.jpeg](img-14.jpeg)

Figure 10. PC SHD and SHD for $p=5,8,10$ in different sample sizes.

![img-15.jpeg](img-15.jpeg)

Figure 11. PC SHD and SHD for $p=20,30$ in different sample sizes.
Figure 12 shows the correct orientation ratio of the number of different nodes as the sample size increases. For a small number of nodes, the number of correctly oriented edges increases with the increase in the sample size, while, for a large number of nodes, the increase in the sample size has little effect on the result of the orientation.

Table 2 shows the average number of intervention nodes under different sample sizes. In total, 4000 experiments were conducted for each sample size to obtain the average number of intervention nodes. It can be seen that the number of intervention nodes selected by our algorithm for directional experiments with different numbers of nodes remains at about $40 \%$ of the total number of nodes. Another conclusion can be drawn from Figure 13: the sample size essentially does not affect the number of intervention nodes, and, as the number of vertices increases, the ratio of the number of intervention nodes selected by our algorithm to the number of summary points decreases, which is a good result for a large matrix.

Table 2. The number of intervention nodes corresponding to different vertex numbers.


![img-16.jpeg](img-16.jpeg)

Figure 12. The orientation ability of the algorithm under different conditions.
![img-17.jpeg](img-17.jpeg)

Figure 13. The number of intervention nodes with different vertex counts.

# 4.1.2. Comparative Experimental Results 

We selected the two single-vertex intervention criteria proposed by He and Geng (2008) [6], the batch intervention algorithm proposed by Alain Hauser (2012) [7], and random intervention criteria for comparison with our algorithm, and we conducted 1000 simulations under the experimental conditions of $p=\{5,10,20,30\}, n=1000, \alpha=0.15$. Among them, the OptUN algorithm proposed by Alain uses the GES algorithm to estimate the essential graph. For the case of $p=5$, we simulated two cases with different numbers of Markov equivalence classes: the first true DAG had 12 Markov equivalence classes, and the second true DAG had 4 Markov equivalence classes. This was intended to explore the influence of the number of Markov equivalence classes on the different algorithms. In the context of $p=30$, the time for He's method to run 1000 times was more than 3 h , so we do not discuss it here.

Due to the estimation error, the PC algorithm is used to estimate the convergence speed of the essential graph from the finite sample to the real model, and it is slow. For the experiments with the number of vertices $p=20,30$, we use the GES algorithm to generate the essential graph, to avoid the error brought by the PC algorithm, and we assume that all the comparison experiments are oriented from the same essential graph. These graphs, with a large number of vertices, usually have a large number of v-structures, and the essential graphs estimated by the GES algorithm also have a large number of v -structures and a small number of unoriented edges. It can be seen from the experimental results in Table 3 that, in this case, only two intervention targets need to be interfered with on average to be fully oriented for $p=20$, and we only need about three intervention targets for $p=30$.

Table 3. The results of the algorithm comparison.


Figure 14 shows the average number of intervention nodes for the five algorithms with different vertex counts. Combined with the results in Table 3, they show that our algorithm is more proficient in the selection of the number of intervention nodes, the maxmin criterion and maxentroy criterion have similar effects, and the OptUN algorithm has the second-best effect. When $p=10$, the OptUN algorithm achieves a better ANI because the GES algorithm compensates for the estimation error of the PC algorithm. In the case of $p=20, p=30$ (both GES algorithms are used in this situation), we can see that our algorithm still obtains the smallest ANI, the OptUN algorithm is second, and the random criterion has the worst effect. We use SHD to measure the accuracy of the algorithm. As can be seen from Figure 15, as the number of vertices increases, the accuracy of our algorithm begins to surpass that of other algorithms.

The speed comparison results of the algorithm are shown in the Figure 16. In terms of the speed of the algorithm, we specifically test the effect of the number of different Markov equivalence classes on the speed of the algorithm when $p=5$. For a real DAG with 12 Markov equivalence classes (the third column of Table 3, with the number of vertices of " 5 "), our algorithm is four times faster than the maxentropy criterion and 5.6 times faster than the maxmin criterion, taking an average of 0.059 s per experiment. Thus, the average number of intervention nodes (ANI) is also the best among all algorithms, and the algorithm accuracy (SHD) is second, slightly behind that of the maxentropy criterion. For a real DAG of five nodes with only four Markov equivalence classes (the fourth column of Table 3,

the number of nodes is " 5_2"), the speed of the two criteria in finding the intervention target based on the Markov equivalence classes is improved, because the time to traverse the equivalence classes is reduced, while our algorithm is still about four times faster than the two algorithms proposed by He. The time for the OptUN algorithm and random algorithm is better than that of ours, but the ANI and SHD (representing the accuracy of the algorithm) of the random criterion are still the worst. The effect of the OptUN algorithm is equal to that of ours, but it can be found that as the vertex count increases, the performance of our algorithm surpasses that of the other algorithms. The time for the OptUN algorithm and random algorithm is not notably different from that of our algorithm, but the ANI and SHD (representing the accuracy of the algorithm) of the random criterion are inferior. The effect of the OptUN algorithm is equal to that of ours, but it can be found that as the number of vertices increases, the performance of our algorithm surpasses that of the other algorithms.
![img-18.jpeg](img-18.jpeg)

Figure 14. ANI for $p=5,10,20,30$.
As the vertex count increases, the difference in the algorithms' speed becomes more obvious. In the example of vertex number $p=10$, the maxmin criterion and the maxentropy criterion take more than 40 min to carry out 1000 experiments, whereas our algorithm takes only four minutes to complete 1000 experiments, which is 10 times faster than He's algorithm. At the same time, the accuracy of the algorithm does not decrease, and it ranks first. Moreover, the average number of intervention nodes is about 0.5 less than for other algorithms. In real life, intervention experiments have a high cost, and the number of intervention nodes directly determines the cost, so we are more inclined to choose a method that requires fewer intervention nodes to reduce the costs.

![img-19.jpeg](img-19.jpeg)

Figure 15. The exact measurement of the algorithm.

# Algorithm runtime 

![img-20.jpeg](img-20.jpeg)

Figure 16. The exact measurement of the algorithm.
The algorithm time of this type of method based on Markov equivalence classes will double with the increase in the number of nodes. This is because each search for an intervention target traverses all nodes of the chain component, which means traversing all Markov equivalence classes. When the number of Markov equivalence classes is large, the running speed and accuracy of the algorithm will be greatly affected. In addition to this, considering real-life causal structures, which often contain dozens or even hundreds of variables, it is not an easy task to find all Markov equivalence classes for real-world causal graphs. The OptUN algorithm does not need to decompose the graph, nor does it need to find all the existing chain components. Its intervention experiments are always conducted on the CPDAG, which saves some algorithmic time.

For the case of $p=20, p=30$, in order to avoid the error caused by the PC algorithm (with the increase in nodes, the time complexity of the algorithm will increase quickly), we choose the GES algorithm to generate an essential graph, and each algorithm in the comparison experiment starts from the same essential graph. The SHD obtained under this experimental condition directly reflects the orientation ability of each algorithm. In fact, the causal graph in real life also has a large number of v-structures, and the points in the chain branches obtained after removing these v-structures are not numerous. In the experiment with $p=20, p=30$, our algorithm is optimal in terms of efficiency, accuracy, and speed.

Moreover, the significance level of the $t$-test used for directional edges has little correlation with the overall performance of the algorithm, and the change in the significance level will hardly affect the accuracy of the orientation. However, different independence testing methods will also affect the experimental results.

# 5. Conclusions 

This paper proposes an active learning algorithm for causal structures based on graph structures. After understanding the previous work, we found that the choice of intervention target is closely related to the structure of the graph, so we introduced the concept of the tree center and proposed that the central node in the graph should be the target of each intervention experiment. In addition, our experiment was conducted in stages; at each stage, the existing directed edge was removed and the intervention experiment was performed in the new connected component. This type of stage experiment can simplify the process of finding the intervention target, avoiding the need to traverse the entirety of the graph information every time to find the intervention target. Our proposed intervention method based on the central node does not need to be defined by Markov equivalence classes (obtaining all Markov equivalence classes corresponding to a DAG is very time-consuming), which greatly reduces the time required to search for the intervention target and improves the algorithm's speed. The experimental results show that with the increase in the number of vertices, our algorithm has greater advantages without affecting the accuracy. The speed is 5-10 times that of the Markov class algorithm, which is comparable to the speed of the OptUN algorithm, but the overall performance is still better than that of this algorithm, especially in terms of the number of intervention nodes (which is also the optimization purpose of our algorithm). In other words, considering that both the selection of intervention targets and intervention will incur large experimental costs, the average number of intervention nodes selected by our algorithm is also the smallest.

The scalability of the optimal design proposed in this paper depends only on the size of the maximum connected component after the decomposition of the causal graph, and it does not depend on the size of the DAG. In this paper, we assume that there are no latent variables. Although the algorithm can determine the direction of the undirected edges and output DAGs based on single-vertex intervention, the application of the method of learning causality in the real world is very limited, as potential variables are usually present in the real-world data set. In our next experiment, we may consider applying our algorithm to actual data and adding some conditions to make the algorithm more robust.

## 6. Follow-Up Work and Prospects

In the last ten years, research on the active learning direction of causal network structures has made great progress. Based on the research in this paper, there are still several directions worthy of further study.

1. The scalability of the optimized design proposed in this paper depends only on the size of the maximum connected branch after the decomposition of the causal graph, and it does not depend on the size of the DAG. Moreover, no latent variables are assumed in the experiment. Although the algorithm can determine the direction of undirected edges and output DAGs based on single-vertex intervention, it needs

further verification regarding whether the application of the learning method can be generalized.
2. The causal relationship in the real world is very complex, and various potential variables usually exist in the real-world data set that interfere with the analysis of the causal relationship. In future experiments, the algorithm can be applied to actual data, and the constraints and optimization objectives of the model can be modified according to the actual problems to be explored, so as to make the algorithm more robust.
3. The algorithm proposed in this paper is a single-vertex intervention algorithm for the active learning of causal network structures. However, the design of the optimal intervention experiment can also be based on multi-vertex intervention, with the purpose of finding an intervention node set of a certain scale that meets the optimization conditions in the node set to restore the causal structure. Therefore, we can further explore the relationship between the causal graph structure property and the intervention node set and find a multi-vertex intervention algorithm based on the same graph structure.

Author Contributions: Conceptualization, X.Z.; methodology, M.Z.; software, M.Z.; validation, M.Z.; formal analysis, M.Z.; investigation, M.Z.; resources, M.Z.; data curation, M.Z. and X.Z.; writing—original draft, M.Z.; writing—review \& editing, M.Z. and X.Z.; visualization, M.Z.; supervision, X.Z.; project administration, X.Z. All authors have read and agreed to the published version of the manuscript.

Funding: This research received no external funding and The APC was funded by National Natural Science Foundation of China 62371094.

Data Availability Statement: The data presented in this study are available on request from the corresponding author. The data are not publicly available due to all the experimental data in this paper are simulation data.

Conflicts of Interest: The authors declare no conflict of interest.
