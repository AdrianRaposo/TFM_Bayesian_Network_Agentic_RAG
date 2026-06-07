# OPEN A novel constraint-based structure learning algorithm using marginal causal prior knowledge 

Yifan Yu ${ }^{1,2}$, Lei Hou ${ }^{1,2}$, Xinhui Liu ${ }^{1,2}$, Sijia Wu ${ }^{1,2}$, Hongkai Li ${ }^{1,2} \square$ \& Fuzhong Xue ${ }^{1,2} \square$


#### Abstract

Causal discovery with prior knowledge is important for improving performance. We consider the incorporation of marginal causal relations, which correspond to the presence or absence of directed paths in a causal model. We propose the Marginal Prior Causal Knowledge PC (MPPC) algorithm to incorporate marginal causal relations into a constraint-based structure learning algorithm. We provide the theorems of conditional independence properties by combining observational data and marginal causal relations. We compare the MPPC algorithm with other structure learning methods in both simulation studies and real-world networks. The results indicate that, compare with other constraintbased structure learning methods, MPPC algorithm can incorporate marginal causal relations and is more effective and more efficient.


Keywords Directed acyclic graphs, Constraint-based structure learning, Marginal prior causal knowledge, Indirect causal relation

Causality discovery has been used in many fields, such as medicine ${ }^{1,2}$, sociology ${ }^{3}$ and bioinformatics ${ }^{4}$. In practice, causal structures are usually represented by Directed Acyclic Graphs (DAGs) ${ }^{5-9}$. In a DAG, a directed edge between two vertices represents a direct causal relation; a marginal causal relation between two vertices is denoted by a directed path, which is a sequence of consecutively directed edges ${ }^{5}$. However, using constraintbased structure learning methods, it is possible to acquire solely a completely partially directed acyclic graph (CPDAG), which represents a group of Markov equivalent DAGs ${ }^{10}$.

In order to improve these learning algorithms, incorporating background knowledge such as expert knowledge has drawn increasing amounts of attention ${ }^{11-13}$. In practical scenarios, researchers often possess a preexisting understanding of the causal system. For instance, in the field of medicine, previous studies may indicate that drinking causes liver cancer ${ }^{14}$. In the field of biology, it is reasonable to assume that genetic variables, such as single nucleotide polymorphisms (SNPs), are not affected by phenotypes ${ }^{15}$. Several methods that address prior knowledge for causal discovery have appeared in the literature. These methods can incorporate knowledge on the presence or absence of direct causal relations ${ }^{16,17}$, on a total ordering of the variables ${ }^{18}$, or the complete structure of the network ${ }^{19}$. However, such prior knowledge may not be direct causal relations in large causal systems containing hundreds of variables ${ }^{12}$. A direct causal relation can be treated as a marginal causal relation between two adjacent variables. Thus, marginal relations are more accessible than direct causal relations in practical terms ${ }^{13}$.

However, incorporating marginal causal knowledge into causal discovery is challenging. Most causal structures cannot be directly inferred from observational data. An intuitive method is to learn a CPDAG, then check the marginal causal relations in all possible graphs represented by the CPDAG. This approach is inefficient, however, when the learned Markov equivalence class contains a large number of DAGs ${ }^{20}$. Previous study of Borboudakis and Tsamardinos extended the causal model to address cases with prior marginal causal relations ${ }^{12}$. PC-PDAG method proposed by Borboudakis and Tsamardinos consists of two steps. The first step uses the PC algorithm to compute the PDAG, and the second step incorporates causal prior knowledge to obtain the maximal partially directed acyclic graph (MPDAG) ${ }^{12}$. The main drawback of this method is that if the PDAG obtained in the first step is incorrect due to statistical errors, it will lead to the second step failing to correctly incorporate the marginal causality or producing an incorrect MPDAG. Researchers have also proposed several score-based structure learning algorithms to address the problem of marginal causal relations. Chen et al. ${ }^{21}$ tackled marginal causal relations using an equivalence class tree (EC-Tree). Wang et al. ${ }^{22}$ proposed an exact search algorithm (ACOG) based on order graph to handle structure learning in the presence of incorrect marginal causal relations.

[^0]
[^0]:    ${ }^{1}$ Department of Epidemiology and Health Statistics, School of Public Health, Cheeloo College of Medicine, Shandong University, 44 Wenhua West Road, Jinan, Shandong Province 250000, People's Republic of China. ${ }^{2}$ Institute for Medical Dataology, Cheeloo College of Medicine, Shandong University, Jinan, People's Republic of China 250000. ${ }^{1 \mathrm{~cm}}$ email: lihongkaiyouxiang@163.com; xuefzh@sdu.edu.cn

However, these methods are computationally demanding and are therefore unable to manage networks with more than 35 nodes^{22,23}. Li and van Beek^{24} proposed a constraint-based hill-climbing method, MINOBSx, to integrate direct and marginal causal relations relatively quickly. However, it still requires significant computation time compared to algorithms that do not consider marginal causal relations, especially when dealing with networks with more than 40 nodes.

In this paper, we examine incorporating marginal causal knowledge into a constraint-based structure learning algorithm. We characterize the conditional independence properties of marginal causal relations. Based on the proposed theorems, we propose an effective algorithm, the Marginal Prior Causal Knowledge PC (MPPC) algorithm, to learn the MPDAG given observational data and a set of causal prior knowledge. We then compare the performances of the MPPC algorithm with those of PC-stable algorithm, MMHC algorithm, PC-PDAG method proposed by Borboudakis and Tsamardinos and MINOBSx method proposed by Li using simulated networks and real networks.

The remainder of the paper is structured as follows: section “Methods” introduces the notation and definitions. Then, we propose theorems for indirect marginal causal prior knowledge and the MPPC algorithm. Next, in section “Results” we evaluate the proposed MPPC algorithm on both simulations and real networks. We discuss the advantages and limitations of this study in section “Discussion”.

## Methods

## Causal DAG models

Let G(V, E) be a DAG with a vertex set V and an edge set E. The undirected graph obtained from replacing all directed edges of G with undirected edges is the skeleton of G. When there is an edge (undirected or directed) between two variables A and B in a graph G, A and B are adjacent. When there is a directed edge A → B in a graph G, A is a parent of B; equivalently, B is a child of A. The parents, children, and adjacent vertices of variable A in a DAG G are denoted by pa(A, G),ch(A, G) and adj(A, G), respectively. If there is a directed (undirected) edge between any two consecutive vertices (X_{i}, X_{i+1}, X_{i+2}, ..., X_{j}), then it is a directed (undirected) path. A is a cause of B if there is a directed path from A to B. For simplicity, we use X_{i} → X_{j} and X_{i} → X_{j} to denote a directed edge and a directed path, respectively. We use X_{i} ≠ X_{j} to denote there is no directed path from X_{i} to X_{j}. If there is a directed path from X_{i} to X_{j}, X_{i} is an ancestor (indirect cause) of X_{j} and X_{j} is a descendant of X_{i}, denoted by X_{i} ∈ an(X_{j}, G) and X_{j} ∈ de(X_{i}, G). A v-structure is a structure of A → B ← C with constraint that A is not adjacent to C, and the vertex B is called a collider.

A DAG encodes the conditional independence (CI) relations induced by d-separation^{25}. When two DAGs are Markov equivalent, their conditional independence relations are the same^{26,27}. According to Pearl et al.^{28}, if two DAGs have the same skeleton and colliders, then they are equivalent. An equivalence class can be represented by a CPDAG G*. Given a consistent background knowledge set K with respect to G*, it is possible that some undirected edges in G* can be oriented, resulting in a partially directed graph H. A maximal PDAG (MPDAG)^{13} can be constructed by orienting some undirected edges in H using Meek's criteria^{16}.

Let P_{G} be the joint distribution of a given DAG G. The causal Markov assumption indicates that P_{G} can be decomposed as $P\left(x_{1},\ldots,x_{n}\right) = \prod_{i=1}^{n} P\left(x_{1} \mid pa\left(x_{1},G\right)\right)$. If the conditional independencies in P_{G} and in DAG G are the same, we say that P_{G} is faithful to G. In this paper, we also assume that there is no hidden variable or selection bias.

## PC algorithm

PC (Peter and Clark) algorithm can find the global structure of high-dimensional CPDAG^{10}. The PC algorithm utilizes CI tests to determine the skeleton and then employs Meek rules to establish the direction of edges. The PC-stable algorithm improved the oracle PC algorithm by removing part of its order-dependence^{4}. The PC-stable algorithm, outlined in Algorithm 1, includes three main steps. Step 1 uses CI tests to ascertain the skeleton of DAG and separation sets between vertices. Then, Step 2 and 3 orient the remaining undirected arcs. The PC-stable algorithm is able to take prior knowledge into consideration. The PC algorithm is computationally efficient and is capable to learn large CPDAG of hundreds of variables^{29--31}.

## Require: The results of CI tests between all pairs of variables

1: Find the skeleton C;

2: Find and orient v-structure based on skeleton and separation sets;

3: Orient undirected edges in C.

4: return C and the separating set between all pairs of variables.

Algorithm 1. The PC PC-stable algorithm

# Conditional independence conditions for marginal causal relation 

Prior knowledge constitutes a set of constraints during structure learning. In this study, we take both positive marginal causal knowledge and negative marginal causal knowledge into consideration. A positive marginal causal relation between two vertices $A$ and $B$ indicates that there exists a directed path from $A$ to $B$ (i.e., $A \in a n(B)$ ), denoted by $A \rightarrow B$. Similarly, a negative marginal causal relation indicates no directed path from $A$ to $B$ (i.e., $A \notin a n(B)$ ), denoted by $A \neq B$. In structure learning algorithms, we use whitelist marginal prior causal knowledge and blacklist marginal prior causal knowledge to denote a positive marginal causal relation and a negative marginal causal relation, respectively. In this section, we will show several properties of marginal prior causal knowledge. First, the concept of the minimal separating set is introduced.

Definition 1 (minimal separating set). Given a directed graph $\mathcal{G}(\boldsymbol{V}, \boldsymbol{E})$, a pair of vertices $X, Y \in \boldsymbol{V}$, and a set $S \subset \boldsymbol{V}$ such that $X, Y \notin S$ and $X \perp Y \mid S$. We say that $S$ is a minimal separating set of $X$ and $Y$ if there is no subset of it $S^{\prime} \subset S$ such that $X \perp Y \mid S^{\prime}$, represented by $m s e p(X, Y)$.

Definition 1 means that a separating set is minimal if and only if none of its subsets separates the target node pair. Note that, the separation sets outputted from PC-based algorithms are the minimal separating sets of node pairs. PC-based algorithms subsequently increase the number of vertices in a separating set during the adjacency phase and output the minimal separating set. Minimal separating sets are important for linking marginal prior causal knowledge with statistical conditional independence tests, as stated in the following lemma by Pearl ${ }^{52}$.

Lemma 1 Given a directed graph $\mathcal{G}(\boldsymbol{V}, \boldsymbol{E})$, a pair of nodes $X, Y \in \boldsymbol{V}$, and a set $S$ is a minimal separating set of $X$ and $Y$ if $S \cap(a n(X) \cup a n(Y))=S$.

With Lemma 1 and the pairwise independencies provided by Koller and Friedman ${ }^{53}$, we can efficiently find a minimal separating set of node pair $X$ and $Y$ if we have the marginal causal relation between $X$ and $Y$, and obtain the following theorems.

Theorem 1 Let $\mathcal{G}$ be a DAG. For any two distinct non-adjacent vertices $X$ and $Y$ in $\mathcal{G} . X$ is an ancestor of $Y$ (marginal causal relation $X \rightarrow Y$ ) in $\mathcal{G}$ if every variable in the minimal separating set of $X$ and $Y$ is an ancestor of $Y$. Specifically, when the number of nodes in the minimal separation set $S$ is 1 , then node is an ancestor of $Y$ and a descendant of $X$.

Theorem 2. Let $\mathcal{G}$ be a DAG. For any two distinct non-adjacent vertices $X$ and $Y$ in $\mathcal{G} . X$ is not an ancestor of $Y$ (marginal causal relation $X \neq Y$ ) in $\mathcal{G}$ if every variable in the minimal separating set of $X$ and $Y$ is not a descendant of $X$.

Theorems 1 and 2 indicates that the marginal causal relations can be transformed into a necessary causal relation set based on the minimal separating sets, and minimal separating sets can be found using the conditional independence tests of observational data. Thus, we can incorporate marginal causal relations with observational data before learning the whole PDAG. With Theorems 1 and 2, we can iteratively decompose the marginal causal relations into necessary causal relations.

Example 1 Figure 1 is an example of Theorem 1. Figure 1a is the underlying true $D A G \mathcal{G}$. Given the complete undirected graph $\mathcal{C}$ in Fig. 1b and prior knowledge that $A$ is an ancestor of $E(A \rightarrow E)$, we would like to find the corresponding necessary causal relations. Note that, the true DAG is unknown. Suppose that we also have conditional independence, which states that $A$ and $E$ are independent with respect to separating set $\{C, D\}$ and that $A$ and $E$ are dependent with respect to only $C$ or $D$ or $\emptyset$, i.e., $\{C, D\} \in m s e p(A, E)$. As shown in Fig. 1c, based on Theorem 1, the necessary causal relation of prior knowledge $A \rightarrow E$ is that $E$ is a descendant of $C$ and $D(C \rightarrow E$ and $D \rightarrow E)$.

Example 1 shows that we can transform marginal prior causal knowledge into necessary causal relations. In addition to leveraging the conditional independence property of marginal causal relations, we also utilize the topological order property ${ }^{53}$ inherent in marginal causal relations. By applying Causal Relation Scanning Algorithm (Algorithm 2) to the positive and negative marginal causal relations obtained through the conditional independence property, we derive a new topological order relation among the nodes.

![img-0.jpeg](img-0.jpeg)

Figure 1. An example to illustrate Theorem 1.

Require: the set of causal relations $\mathbf{P K}$.
1: for each causal relation $X_{i} \rightarrow X_{j}$ in $\mathbf{P K}$ do
2: if exists another causal relation $X_{j} \rightarrow X_{k}$ in PK, then
3: $\quad$ add $X_{i} \rightarrow X_{k}$ to PK
4: end if
5: end for
6: for each causal relation $X_{i} \nrightarrow X_{j}$ in PK do
7: if exists another causal relation $X_{k} \rightarrow X_{j}$ in PK, then
8: $\quad$ add $X_{i} \nrightarrow X_{k}$ to PK
9: end if
10: end for
11: return the extended set of causal relations PK.

Algorithm 2. Causal Relation Scanning Algorithm

# Marginal Prior Causal Knowledge PC (MPPC) algorithm 

We now propose the Marginal Prior Causal Knowledge PC (MPPC) algorithm. MPPC algorithm can be treated as a modification of the PC-stable algorithm with marginal prior causal knowledge. The main modification of the MPPC algorithm is in the adjacency phase, which is encoded in the pseudo-code of Algorithm 3, lines 1-24.

Originally, the adjacency phase consisted of creating a complete undirected graph and testing conditional independence of every pair of vertices based on a threshold $\alpha$. The skeleton graph is estimated after the adjacency

search phase. We modified the adjacency phase by adding the testing procedure of marginal causal relations based on the prior knowledge set K = {K}_{i=1}^{M} and Theorem 1 and 2, where each K_{i} is of the form X_{i} - → X_{j} or X_{j} ≠ X_{j}, X_{i}, X_{j} ∈ V. This means that for every variable-pair in K, we record the minimal separating set according to the conditional independence test and add new marginal causal relations to K based on Theorems 1 and 2. After the adjacency phase, we orient the edges in skeleton to the direction of causal relation set K according to the acyclic assumption, that is, for any X_{i} - → X_{j} in K, if X_{i} - X_{j} in the skeleton, then we orient X_{i} - X_{j} as X_{i} → X_{j}.

It is worth noting that Algorithm 3 applies not only to marginal prior causal knowledge, but also to a mixture of marginal prior causal knowledge and direct prior knowledge, since direct prior knowledge can be treated as marginal prior causal knowledge between adjacent vertices. If prior knowledge set K includes a subset of direct prior knowledge, there will be directed arcs reflecting this direct prior knowledge in the final graph.

For the v-structure phase, we find every unshielded triple X_{i} - X_{j} - X_{k} in the skeleton and test whether X_{j} is in the separating set of X_{i} and X_{k}. If X_{j} does not exist in every separating set of X_{i} and X_{k} we obtained from adjacency phase, then X_{i} - X_{j} - X_{k} is marked as a v-structure X_{i} → X_{j} ← X_{k}. Finally, we apply Meek rules in the orientation phase, which is similar to the oracle PC-stable algorithm. These rules are applied repeatedly until no additional edges can be oriented, resulting in a MPDAG^{16,27}.

Example 2 Figure 2 is an example of how MPPC works. Figure 2a shows the true DAG Ω. Suppose that we have background knowledge that states that A is an ancestor of E (A - → E). The background knowledge and complete undirected graph C are shown in Fig. 2b. Figure 2c--e shows the adjacency step of MPPC algorithm, where l is the number of vertices in the separating sets. From Fig. 2c to d, three edges are removed, and two causal relations (A - → B and B - → E) are added based on prior knowledge A - → E and conditional independence A ⊥ E|B. From Fig. 2d to e, two additional causal relations are added similarly based on Theorem 1. Figure 2f shows the maximal partial directed graph resulting from orienting the skeleton in Fig. 2e. In addition to {A → B, C → E, D → E}, B - C and B - D are oriented as B → C and B → D, respectively, since A → B - C and A → B - D are not

(a) (b) (c) Graph C (d) (e) (f) (g) (h) (i) (j) (k) (l) (m) (n) (o) (p) (q) (r) (s) (t) (u) (v) (vi) (x) (y) (z) (x) (y) (z) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x) (x

$v$-structure based on separating sets. Thus, Fig. 2f and the causal relations in Fig. 2e are the outputs of the MPPC algorithm.

Require: The observational data of all variables, significance parameter $\alpha$ and the set of prior causal relations $\mathbf{K}$.
1: From the complete undirected graph $\mathcal{C}$ on the vertex set $\mathbf{V}$
2: Let $l=-1$;
3: repeat
4: Let $l=l+1$;
5: repeat
6: $\quad$ Select a new pair of adjacent vertices $\left(X_{i}, X_{j}\right)$ satisfy $\left|a d j\left(X_{j}, \mathcal{C}\right) \backslash\right.$ $\left.\left\{X_{i}\right\}\right| \geq l$
7: if exists causal relations of $X_{j} \rightarrow X_{i}$ or $X_{i} \nrightarrow X_{j}$ then
8: continue
9: end if
10: repeat
11: $\quad$ Choose a (new) set $S \subseteq a d j\left(X_{j}, \mathcal{C}\right) \backslash\left\{X_{i}\right\}$ with $|S|=l$
12: if $X_{i}$ and $X_{j}$ are conditionally independent given $S$ then
13: $\quad$ Remove edge $X_{i}-X_{j}$ from $\mathcal{C}$
14: $\quad$ Let $\operatorname{sepset}\left(X_{i}, X_{j}\right)=\operatorname{sepset}\left(X_{j}, X_{i}\right)=S$
15: if exists causal relation $X_{i} \rightarrow X_{j}$ (or $X_{j} \nrightarrow X_{i}$ ) then
16: $\quad$ for every vertex $v \in S$ do
17: $\quad$ add $v \rightarrow X_{j}$ (or $X_{j} \nrightarrow v$ ) to causal relation set $\mathbf{K}$
18: checking causal relation set $\mathbf{K}$ by calling Algorithm 2
19: end for
20: end if
21: end if
22: until there is no edge between $X_{i}$ and $X_{j}$ or there is no $S \subseteq$ $a d j\left(X_{j}, \mathcal{C}\right) \backslash\left\{X_{i}\right\}$ with $|S|=l$
23: until all pairs of adjacent vertices $\left(X_{i}, X_{j}\right)$ have been considered
24: until all pairs of $\left(X_{i}, X_{j}\right)$ satisfy $\left|a d j\left(X_{j}, \mathcal{C}\right) \backslash\left\{X_{i}\right\}\right|<l$
25: Orient undirected edges in the skeleton $\mathcal{C}$ with causal relations in $\mathbf{K}$;
26: Find and orient v-structure and separation sets;
27: Orient remaining undirected arcs (See Algorithm 4 in Supplement S.3)
28: return $\mathcal{C}$, sepset, the set of causal relations $\mathbf{K}$.

Algorithm 3. MPPC algorithm

# Simulations 

In the experimental simulations, we use the random.graph function in R package bnlearn to randomly generate the structure of DAGs and randomly choosing $p \in\{10,20,30\}$ percent of marginal causal relations according to the generated DAGs. For real-world networks, we use ECOLI70, MAGIC-IRRI and ARTH150 in the Bayesian Network Repository ${ }^{24}$. Then, we use linear structural equation models to generate synthetic data sets based on

the structures. We compare the MPPC method with PC-stable^{9} (with only directed prior knowledge, denoted by PC(d_exp)) algorithm, PC-stable (with marginal and directed prior knowledge, denoted by PC(all_exp)), the PC-PDAG algorithm proposed by Borboudakis and Tsamardinos^{12} (denoted by PC-PDAG), and Max--Min Hill-Climbing algorithm^{35} (denoted by MMHC). We also use the MINOBSx^{34} method as a comparative approach in the instance analysis based on the ALARM network. Note that, PC-PDAG algorithm needs PDAG as input, thus we use the PDAG learned from PC-stable algorithm without prior knowledge as suggested by Borboudakis and Tsamardinos^{12}. In all experiments, PC-stable algorithm and MMHC algorithm is called from R-package bnlearn and PC-PDAG algorithm is called from MATLAB function provided by Borboudakis and Tsamardinos^{12}.

We generate random DAGs G with n nodes and mean in-degree d, where n is chosen from {50, 100, 150, 200, 250} and d is chosen from {1, 2, 3, 4}. For a sampled G(n, d) graph, we draw an edge weight β_{ij} from a Uniform distribution, U(0.8, 1.6), for each directed edge X_{i} → X_{j} in G. We use the following linear structured equation model to simulate data,$$X_{j}=\sum_{X_{i}\in p a\left(X_{j}\right)}{p_{ij} X_{i}+ \epsilon_{j}, j=1,\ldots , \mathrm{n},}$$where ∈_{1}, ..., ∈_{n} are independent N(0, 1) noises^{36}. We then generate N = 2000, 10000 samples for every simulated DAG. The marginal prior causal knowledge set K with respect to G was generated by randomly choosing p ∈ {10, 20, 30} percent of marginal causal relations according to G, i.e. variable pairs such as (X, Y), where X is an ancestor of Y (X → Y) or X is not an ancestor of Y (χ ∈ Y). For each situation, we generated 100 (G, K) pairs.

We use precision, recall, F1 score, Structural Hamming Distance (SHD) and Constraint Satisfaction Rate^{22} (CSR) to evaluate and compare the performances of different methods. For each (G, K) pair in the simulation and experimental studies, we computed the corresponding MPDAG and used the MPDAG as the gold standard for comparison with the estimated network. Given that the outputs of MMHC algorithm and MINOBSx algorithm are DAGs, we also reformulated the criterion for True Positive: for an undirected edge in an MPDAG, an edge in the estimated network with any direction is considered a True Positive. Precision is defined as Precision = $\frac{\text{True Positives}}{\left(\text{True Positives} + \text{False Positives}\right)}$ and recall is defined as Recall = $\frac{\text{True Positives}}{\left(\text{True Positives} + \text{False Negatives}\right)}$. F1 score is defined as F1 = 2 × $\frac{\text{precision} \times \text{recall}}{\text{precision} + \text{recall}}$. The SHD between two PDAGs, as implemented in bnlearn^{35}, measures the distance between the underlying true graph and the learned graph. The CPU time and the total number of statistical tests (number of calls to test conditional independence) are used to evaluate the algorithm efficiency.

## Evaluation with real-world networks and dataset

In addition to the randomized networks, three large real-world Gaussian BN taken from the bnlearn repository were also utilized: ECOLI70^{37}, MAGIC-IRRI^{38} and ARTH150^{39}. ECOLI70 is a network with 46 nodes and 70 arcs, representing the protein-coding genes of E. coli. MAGIC-IRRI is a large network with 64 nodes and 102 arcs, modeling multiple traits in plant genetics. The third network is a large network, ARTH150, with 107 nodes and 150 arcs, capturing gene expression and proteomics data of Arabidopsis thaliana. The BN was used to generate data, with the sample size set to 2000. The marginal prior causal knowledge set K with respect to the networks was generated by randomly choosing p ∈ {10, 20, 30} percent of the marginal causal relations. We generated 100 (observational data, knowledge) pairs from each of the three networks.

We utilize the datasets provided by Beinlich^{40} to compare the effectiveness and efficacy of various structure learning methodologies including MINOBSx algorithm. ALARM is a medium network with 37 nodes and 46 arcs. The marginal prior causal knowledge set K with respect to the networks was generated by randomly choosing p ∈ {5, 10, 20} percent of the marginal causal relations. To evaluate the performance of different methods, we calculate the CSR, SHD and running time.

## Ethics approval and patient consent statement

Ethical approval was not sought, because this study only involved public networks and data.

## Results

## Evaluation with random DAGs

Figures 3 and 4 show the experimental results for randomly generated causal models, with 10,000 samples, p = 10, 20, 30 and n = 50, 100, 150, 200, 250 (Fig. 3), and p = 10, 20, 30 and d = 1, 2, 3, 4 (Fig. 4). The average F1 score (Figs. 3A and 4A), SHD (Figs. 3B and 4B) and CSR (Figs. 3C and 4C) of five methods (PC-stable with only directed prior knowledge, PC-stable with all knowledge, MMHC, PC-PDAG and MPPC) are reported. The results of precision and recall, and results on randomly generated graphs with 2000 samples can be found in Supplement S.2.

We first compare the effectiveness of MPPC algorithm with other methods. Clearly, the F1 score of the MPPC algorithm is statistical significantly higher than that of the other methods (Supplement Table S2), and the SHD of the MPPC algorithm is statistical significantly lower than that of the other methods (Supplement Table S1), especially when the number of vertices is large. The CSR results indicate that the MPPC algorithm consistently achieves a high CSR, close to 1, in all cases. This demonstrates that the MPPC algorithm is more effective at incorporating prior knowledge compared to other structure learning methods. While PCPDAG method has poorer CSR and SHD than MPPC. This is because PC-PDAG needs to learn the PDAG using PC without knowledge and then incorporate marginal prior causal knowledge with the learned PDAG. If the PDAG is wrong, PC-PDAG algorithm can hardly incorporate marginal prior causal knowledge since the knowledge may conflict with the learned wrong graph. When the number of vertices or edge degree is large, the probability

![img-1.jpeg](img-1.jpeg)

**Figure 3.** Experiments results on randomly generated causal models, with *N* = 10, 000, *p* = 10, 20, 30 and *n* = 50, 100, 150, 200, 250. The F1 score, SHD and CSR of different methods are reported.

of an incorrect PDAG being learned from PC is larger. The performance of MPPC is usually better than other methods since it directly incorporates marginal prior causal knowledge with observational data and statistical tests during structure learning.

We next compare the efficiency of MPPC algorithm with other methods. The average number of statistical tests (Fig. 5A) and CPU time (Fig. 5B) are reported in Fig. 5. The CPU time of PC-PDAG method is the total time needed to learn the PDAG and incorporate the prior knowledge. The results show that it takes significantly longer to estimate the maximal PDAG when the number of vertices is large. The figure suggests that the MPPC method is faster than other constraint-based methods and is similar to MMHC method. The number of CI tests of MPPC is smaller than that of other methods. Besides, the running time of PC-PDAG significantly increases but that of MPPC is stable when the percentage of prior knowledge increases. This is because PC-PDAG needs to learn a PDAG and then recurrently incorporate each prior knowledge, while MPPC can decrease the number of statistical tests using prior knowledge.

### Evaluation with real networks

The results of the real-world networks are given in Fig. 6. Similar to the simulation results of randomly generated graphs. The F1 score (the first row of Fig. 6) of MPPC algorithm is higher than that of other methods and the

![img-2.jpeg](img-2.jpeg)

**Figure 4.** Experiments results on randomly generated causal models, with *N* = 10, 000, *p* = 10, 20, 30 and *d* = 1, 2, 3, 4. The F1 score, SHD and CSR of different methods are reported.

SHD (the second row of Fig. 6) of MPPC is lower. The CSR results indicate that the MPPC algorithm consistently achieves a high CSR. The F1 score of MPPC increases significantly when prior knowledge increases. On the other hand, the CPU time and the number of statistical tests of the MPPC algorithm are lower than those of the other methods in large networks (Supplement S.3).

### Evaluation with real dataset

We apply the methods to ALARM dataset of Beinlich^{40}. The results of MPPC, PC-PDAG and MINOBSx method are presented in Table 1, which provides a summary of the CSR, SHD and CPU time. The results indicate that the MPPC method exhibits better performance than PC-PDAG, but a slight inferiority to the MINOBSx method in ALARM network. However, MPPC algorithm has significantly faster computational speed compared to MINOBSx algorithm.

![img-3.jpeg](img-3.jpeg)

Figure 5. The number of statistical tests and CPU time of different methods on randomly generated causal models.

## Discussion

Causal discovery from observational data has been used in numerous fields. In certain scenarios, researchers may possess prior knowledge in the form of marginal causal relations. We propose a constraint-based algorithm to estimate the maximal PDAG from observational data with marginal prior causal knowledge. We provide conditional independence properties to utilize marginal causal relations. Based on these properties, we propose a constraint-based structure learning algorithm with marginal prior causal knowledge, the MPPC algorithm, to estimate the maximal PDAG. The experiment results show that the network structure estimated by the MPPC algorithm in large networks is closer to the real structure, with a lower SHD compared to other structure learning algorithms. The MPPC algorithm reduces the number of conditional independence tests compared to the PC-PDAG algorithm, thereby lowering the computational burden. Additionally, the MPPC algorithm effectively incorporates marginal causal relations, resulting in estimated networks that satisfy a higher proportion of prior knowledge. For small and medium networks, the MINOBSx algorithm achieves higher accuracy in the estimated network structure but requires significantly more computational time, which can be up to tens of times more than that required by the MPPC algorithm. The proposed MPPC algorithm offers a trade-off between accuracy and efficiency. In the context of practical studies, researchers can select more applicable structure learning algorithms according to their specific requirements.

Our study has limitations. Firstly, we considered only directed marginal causal relationships in this study, including positive marginal causal relations (*X* → *Y*) and negative marginal causal relationships (*X* ≠ *Y*). However, undirected marginal relations without clear direction (*X* → *Y*) may exist in practice. These marginal undirected relations might arise from directed causal relations or confounding paths between nodes. Additionally, in the presence of unmeasured variables, such associations could result from selection bias. Integrating marginal undirected relations with structure learning algorithms remains a direction for future research. Furthermore, we have only considered continuous or discrete variables in our study and have not addressed the case of mixed-type data. Adapting the algorithm for mixed-type data requires modifying the conditional independence test. In addition, our proposed MPPC algorithm does not account for latent variables or selection bias. A possible future work is to examine statistical properties of marginal causal relations under the framework of Maximal Ancestral Graphs^{41} (MAGs) and incorporating marginal prior causal knowledge with the FCI^{41,42} algorithm to

![img-4.jpeg](img-4.jpeg)

Figure 6. Experimental results on ECOLI70, MAGIC-IRRI and ARTH150 network.


Table 1. The results of different methods on ALARM dataset.

deal with hidden variables and selection bias. In our experiments, we randomly select the marginal prior causal knowledge from all possible variable pairs, which may cause a waste of knowledge. It is worth considering the amount of information of different causal relations to improve the efficiency of algorithm^{43}. Another possible extension is to consider the degree of belief in each causal prior knowledge^{44}.

## Data availability

All the data are publicly available at https://github.com/YuYF97/MPPC and https://doi.org/https://doi.org/10.1126/science.1105809. All the code is availability at https://github.com/YuYF97/MPPC.

Received: 21 March 2024; Accepted: 23 July 2024
Published online: 20 August 2024

# Acknowledgements 

We want to acknowledge the investigators of the bnlearn repository.

## Author contributions

FX and HL conceived the study. YY, LH and XL contributed to the simulation analysis. SW a contributed to figures. YY, HL and FX wrote and modified the manuscript. All authors reviewed and approved the final manuscript.

## Funding

FX was supported by the National Key Research and Development Program of China under Grant 2020YFC2003500.

## Competing interests

The authors declare no competing interests.

## Additional information

Supplementary Information The online version contains supplementary material available at https://doi.org/ 10.1038/s41598-024-68379-7.

Correspondence and requests for materials should be addressed to H.L. or F.X.
Reprints and permissions information is available at www.nature.com/reprints.
Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/ licenses/by-nc-nd/4.0/.
(c) The Author(s) 2024