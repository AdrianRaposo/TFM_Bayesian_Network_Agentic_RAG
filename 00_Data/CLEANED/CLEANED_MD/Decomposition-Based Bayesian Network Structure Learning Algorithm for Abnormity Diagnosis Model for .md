# Article 

## Decomposition-Based Bayesian Network Structure Learning Algorithm for Abnormity Diagnosis Model for Coal Mill Process

Yuqing Chang ${ }^{1}$, Leyuan Liu ${ }^{1, * *}$, Xiaoyun Kang ${ }^{1}$ and Fuli Wang ${ }^{1,2}$<br>check for updates<br>Citation: Chang, Y.; Liu, L.; Kang, X.;<br>Wang, F. Decomposition-Based<br>Bayesian Network Structure<br>Learning Algorithm for Abnormity<br>Diagnosis Model for Coal Mill<br>Process. Electronics 2022, 11, 3870.<br>https://doi.org/10.3390/<br>electronics11233870<br>Academic Editor: Fabio Postiglione<br>Received: 12 October 2022<br>Accepted: 21 November 2022<br>Published: 23 November 2022<br>Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## 0

Copyright: (c) 2022 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 College of Information Science and Engineering, Northeastern University, Shenyang 110819, China
2 State Key Laboratory of Synthetical Automation for Process Industries, Northeastern University, Shenyang 110819, China

* Correspondence: liuleyuan_neu@163.com

Abstract: In the structure learning of the large-scale Bayesian network (BN) model for the coal mill process, taking the view of the problem that the decomposition-based method cannot guarantee the sufficient learning of abnormal state node neighborhood in the diagnosis model, this paper proposes a new BN structure learning method based on decomposition. Firstly, a sketch is constructed based on an improved Markov blanket discovery algorithm and edge thickening and thinning. Second, the node centrality of $k$-path is used to search the important nodes, and the subgraph decomposition is realized by extracting these important nodes and their neighborhoods from the sketch. Then, through the targeted design of subgraph de-duplication, subgraph learning, and subgraph reorganization methods, the learning of large-scale BN is realized. This method is applied to public data sets, and its advantages and disadvantages are analyzed by comparing them with other methods. The advantage of the BN structure learning method of the abnormal condition diagnosis model is further verified by applying the method to the coal mill process, which is consistent with the original design intention.

Keywords: coal mill process; Bayesian network; structural learning; abnormal condition diagnosis

## 1. Introduction

The coal mill is the core equipment of the pulverizing coal system in the thermal power plant, which grinds the coal into pulverized coal. The pulverized coal is blown into the boiler for combustion by the primary air. In the actual production process, the coal mills are subject to a poor operating environment and longtime high load operation, so abnormal working conditions occur from time to time. Suppose the abnormities are not detected in time. In that case, they may affect the industrial production process, reduce production efficiency, and pose a significant safety risk to the future production process. Therefore, it is of great significance for the safe operation of the system to identify and diagnose abnormities at the beginning of abnormal working conditions [1,2].

With the development of modern industry and the continuous progress of data acquisition technology in the industrial process, the amount and variety of data have significantly increased, and researchers have focused extensively on data-driven methods in fault diagnosis and monitoring. Taking the coal mill process as an example, Li et al. [3], Jian et al. [4] and Han et al. [5] realized coal mill condition monitoring and fault diagnosis based on a deep neural network and fuzzy decision clustering, respectively. Yang et al. [6] investigated the prediction of coal mill process variables based on the least squares support vector machine (LSSVM) algorithm through a hybrid modeling approach. Hong et al. [7] proposed a method of abnormity monitoring and diagnosis for coal mills based on the support vector machine. In comparison to other machine learning methods, Bayesian networks (BN) have been widely used in the field of abnormity diagnosis due to their excellent data learning capability and high utilization rate of expert knowledge and work experience. Yan et al. [8] and Li et al. $[9,10]$ used BN to identify the abnormal condition for the electro-fused magnesia smelting process and designed the corresponding safety control scheme. Wu et al. [11]

proposed a framework for fault diagnosis based on BN and verified the method's feasibility in a pressurized water reactor model of a nuclear power plant. Agrawal et al. [12] realized an intelligent decision support system for coal mills to conduct a root cause analysis of faults. Andrade et al. [13] proposed a hybrid framework for automated fault detection and diagnosis based on Moving Window Principal Component Analysis and BN. They applied it to the analysis of a simplified model of a hydrogenator unit.

It is worth noting that the scale of BN constructed in the above applications is relatively small. In the actual coal mill process, multiple coal mills operate simultaneously, and the operating conditions of the coal mill may affect each other. Therefore, the above approaches have limitations when dealing with large-scale BNs with more nodes and complex structures (e.g., the coal mill process). Recently, studies have confirmed that learning BN structure from data is an NP-hard problem. As the number of nodes increases, the algorithm easily falls into the local optimum, and the model accuracy and algorithm efficiency cannot be guaranteed. As a result, scholars have begun introducing the idea of decomposition-fusion into the large-scale BN structure learning process and have proposed a series of hybrid methods.

The BN learning method based on the hybrid method comprises four steps: drafting, decomposition, subgraph learning, and reunion. Specifically, the large-scale sketched BN is decomposed into a series of simple BN or even moral graphs. The structure of the subgraph is learned on these smaller BNs, and then the learned subgraphs are combined to achieve faster BN learning. Xie et al. [14] proposed a BN decomposition method based on a D-separation tree, which decomposes a large BN into a series of subgraphs with less than or equal to 4 nodes, adds or deletes edges and assigns directions for each subgraph based on independence judgment. Liu et al. [15] proposed a Separation and Reunion (SAR) method that extends the q-partial graph theory. The construction and separation of an undirected independent graph are accomplished by combining the improved prioer-p-paritial graph method with the suboptimal minimum node separator. Dai et al. [16] improved the sketching performance of the algorithm by improving the Markov blanket search method and proposed a subgraph decomposition method based on the $k$-path node centrality. Guo et al. [17] proposed a two-stage reunion method based on the heuristic search for the reunion step.

However, for the abnormity diagnosis BN model, the model construction aims to achieve the inference and diagnosis for the important nodes, such as abnormity nodes. The abnormity node is the node that can reflect the operating condition in the process of equipment operation. In the case of coal mill systems, powder blocking, coal blocking, and spontaneous combustion are abnormity nodes. Naturally, the whole model should be built around these important nodes. However, although the above BN structure learning methods based on decomposition can obtain good results in public data sets, the necessity of important nodes in the BN network for abnormal working condition diagnosis is not considered in the algorithm design. At the same time, the neighborhoods of these important nodes are often the main split objects in the process of subgraph decomposition, so subgraph learning cannot reflect the expected needs of important nodes, such as abnormity nodes. There is no guarantee that the neighborhoods of these nodes can be sufficiently and reasonably learned, which affects the inference performance of the BN model for important nodes.

Based on the above motivation, a new BN structure hybrid learning algorithm based on decomposition is proposed to solve the problem that the existing decomposition-based BN structure learning algorithm does not apply to abnormal working conditions identification. The algorithm consists of four stages: drafting, subgraph decomposition, subgraph learning, and subgraph reunion. By improving the decomposition method, the $k$-path node centrality is introduced to filter important nodes. Then, the learning of large-scale BN is realized through the targeted design of subgraph de-duplication, subgraph learning, and subgraph reunion methods.

The innovation of this paper is reflected in two aspects. On the one hand, the demand for abnormal working condition identification BN is considered in the algorithm design, and the adequate learning of important and neighboring nodes in BN is ensured in the structure learning process. On the other hand, the proposed learning algorithm maintains high accuracy in large-scale BN structure learning and has good adaptability and superiority in abnormal working condition diagnosis.

The contributions of this article are stated as follows.
(1) A new decomposition-based structure learning method for large-scale BN is proposed, which is suitable for abnormal condition diagnosis;
(2) An improved subgraph decomposition method that combines subgraph extraction and subgraph de-duplicating is proposed, which could ensure the adequate learning of important nodes and their neighborhood nodes in BN;
(3) A reunion method based on the maximum benefit principle of the local BIC score is proposed to obtain the final BN structure;
(4) The effectiveness of the proposed method was verified on public data sets and abnormity data sets under the real coal mill process.
The remainder of the paper is organized as follows. Section 2 presents the main concepts used in this paper and a brief review of the related work. Section 3 gives a complete hybrid learning algorithm based on model decomposition, which mainly consists of four stages: drafting, subgraph decomposition, subgraph learning, and subgraph reunion. The corresponding flow chart and pseudo-code are respected, and the details are expounded. In Section 4, the algorithm is first tested by simulation based on public data sets and compared with other BN structure learning methods to analyze its advantages and disadvantages. Then, based on the abnormity data under the actual coal mill process, it was verified whether the method conformed to the original design intention by comparing the abnormity diagnosis performance of the final model obtained by different methods. Section 5 summarizes the works of this paper.

# 2. Preliminary Knowledge 

### 2.1. Bayesian Network

BN, also known as the belief network and probability dependency graph, is one of the most influential models in uncertain knowledge expression and reasoning. BN is a probabilistic graphical model representing a set of random variables and their conditional dependencies via a directed acyclic graph. BN consists of qualitative and quantitative parts. The qualitative part is a directed acyclic graph (DAG), in which nodes represent system variables, whereas arcs symbolize dependencies or cause-and-effect relationships among variables. The quantitative part consists of the conditional probabilistic table, which represents the relationship between each node and its parents [18].

In particular, BN encodes the probabilistic relationships among different random variables $\boldsymbol{X}=\left\{X_{i}\right\}_{i=1,2, \ldots, n}$ in the domain, which consists of a graph structure $G$ and a set of distribution parameters $\boldsymbol{\theta}=\left\{\theta_{i}\right\}_{i=1,2, \ldots, n}$ [16]. $G=(\boldsymbol{X}, \boldsymbol{E})$ is a DAG in which there are $n$ nodes corresponding to the random variables $\boldsymbol{X}$. A directed edge $E_{i j} \in \boldsymbol{E}$ from $X_{i}$ to $X_{j}$ represents the direct dependency between these two variables. $X_{i}$ is one of the "parent nodes" of $X_{j}$ and $X_{j}$ is "child node" of $X_{i}$. The node without any parent node is the "root node", the node without a child node is the "leaf node" and other nodes are "intermediate nodes". The Basic BN structure is shown in Figure 1. There is a directed edge $E_{13}$ from $X_{1}$ to $X_{3}$, which means $X_{1}$ is one of the parent nodes of $X_{3}$ and $X_{3}$ is a child node of $X_{1} . X_{1}$, without the parent node, is a root node. $X_{4}$, without a child node, is a leaf node.

![img-0.jpeg](img-0.jpeg)

Figure 1. Basic BN structure.
In BN, except for the root node, other nodes only depend on their parent nodes conditionally, so that it can be assumed that

$$
P\left(X_{i} \mid X_{1}, X_{2}, \ldots, X_{i-1}, X_{i+1}, \ldots, X_{n}\right)=P\left(X_{i} \mid p a\left(X_{i}\right)\right), i=1,2, \ldots, n
$$

where, $p a\left(X_{i}\right)$ presents the parent node set of the node $X_{i}$. Therefore, the joint probability density distribution $P(\boldsymbol{X})$ between BN node sets $\boldsymbol{X}=\left\{X_{1}, X_{2}, \ldots, X_{n}\right\}$ can be expressed as

$$
P(\boldsymbol{X})=\prod_{i=1}^{n} P\left(X_{i} \mid p a\left(X_{i}\right)\right)
$$

BN can perform backward or diagnostic analyses with various inference algorithms based on Bayes' theorem, which means BN can conduct probabilistic reasoning after inputting evidence. When a new formation is given as evidence $e, \mathrm{BN}$ can obtain the posterior probability under the condition of evidence occurrence through the reasoning mechanism,

$$
P(\boldsymbol{X} \mid \boldsymbol{e})=\frac{P(\boldsymbol{X}, \boldsymbol{e})}{P(\boldsymbol{e})}=\frac{P(\boldsymbol{X}, \boldsymbol{e})}{\sum_{\boldsymbol{X}} P(\boldsymbol{X}, \boldsymbol{e})}
$$

Equation (3) can be used for probability prediction or probability update. In the field of fault identification, based on providing evidence, fault identification can be performed according to the posterior probability of faulty nodes. The corresponding fault has a higher probability of occurrence with increasing posterior probability.

# 2.2. Bayesian Network Structure Learning 

Recently, many BN learning algorithms based on data have been proposed. There are three main approaches: constraint-based, scored-based, and hybrid. The constraint-based method typically uses statistical tests to identify conditional independence (CI) relations from data. A BN structure is then built that best fits these independence relationships. For instance, the PC algorithm [19] and the MMPC algorithm [20].

The scored-based method treats the BN structure learning problem as a combinatorial optimization problem. The scoring function and search algorithm find the highest-scoring network structure in all possible structures. Typical scoring functions are the Akaike information criteria (AIC), the Bayesian information criteria (BIC), and the Bayesian Dirichlet equivalence uniform (BDeu) scores. The search strategy generally adopts heuristic algorithms, such as the K2 [21], the TABU [22], and HC [23] algorithms.

The hybrid method combines the advantages of the above methods. Statistical tests reduce the size of the network structure space, and then the optimal network structure is obtained by scoring searches, such as the CB algorithm [24] and the MMHC [25] algorithm.

### 2.3. Concept Introduction

Some concepts have been repeatedly mentioned in the constraint-based BN structure learning method. Here is a brief introduction.

Let $\boldsymbol{U}, \boldsymbol{V}, \boldsymbol{Z}$ be three sets of random variables. We say that $\boldsymbol{U}$ and $\boldsymbol{V}$ are conditionally independent over $\boldsymbol{Z}$ in a probability distribution $\boldsymbol{\theta}$, denoted as $(\boldsymbol{U} \perp \boldsymbol{V} \mid \boldsymbol{Z})_{\theta}$, if for each $u \in \boldsymbol{U}$ and $v \in \boldsymbol{V}, \boldsymbol{\theta}$ satisfies $p(\boldsymbol{U} \perp \boldsymbol{V} \mid \boldsymbol{Z})=p(u \mid \boldsymbol{Z}) p(v \mid \boldsymbol{Z})$. In this paper, we use the notation $(U \perp V \mid Z)$ for conditional independence.

Maximum mutual information coefficient (MIC) is a function to measure the correlation between nodes based on mutual information (MI) and grid division:

$$
M I\left(X_{i}, X_{j}\right)=\sum_{k_{j}=1}^{r_{i}} \sum_{k_{j}=1}^{r_{j}} P\left(x_{k_{i}}, x_{k_{j}}\right) \log \frac{P\left(x_{k_{i}}, x_{k_{j}}\right)}{P\left(x_{k_{j}}\right) P\left(x_{k_{j}}\right)}
$$

$P\left(x_{k_{i}}, x_{k_{j}}\right)$ is the joint probability of events $X_{i}$ in state $k_{i}$ and event $X_{j}$ in state $k_{j}$. It is assumed that there is meshing, an ordered set of pairs composed of current data. The values of the $x$-axis and $y$-axis of the ordered pair set can be divided into $x$ groups and $y$ groups, respectively. For the grid N of this row $x$ and column $y$, it is defined as $N_{(x, y)}$. Further, $M I\left(X_{i}, X_{j}, D \mid N_{(x, y)}\right)$ is defined as the MI of the event $X_{i}$ and $X_{j}$ on the grid $N_{(x, y)}$.
$m i_{(x, y)}$ is defined as normalized maximum MI on grid $N$ of row $x$ and column $y$ under any grid, MIC is defined as maximum $m i_{(x, y)}$ on a grid of any row $x$ and column $y$ under data set $D$.

$$
\begin{gathered}
m i_{(x, y)}=\max \left(M I\left(X_{i}, X_{j}, D \mid N_{(x, y)}\right)\right) / \log (\min (x, y)) \\
M I C\left(X_{i}, X_{j} \mid D\right)=\max \left(m i_{(x, y)}\right), x y<B
\end{gathered}
$$

$B$ is a function of the total number $m$ of samples in data set $D$, usually $B=m^{0.6}$.

# 3. Method 

In the research field of BN structure learning, the hybrid learning algorithm combines the advantages of the constraint-based method and the search score algorithm. However, this method tries to find the optimal network structure directly in large-scale solution space during the learning process, which leads to the high computational expense and low learning accuracy. Therefore, a new hybrid structure learning algorithm based on decomposition is proposed in this paper. As shown in Figure 2, there are four steps in this new hybrid structure learning algorithm.
![img-1.jpeg](img-1.jpeg)

Figure 2. The flowchart of the proposed hybrid learning algorithm.

The first step is to establish the sketch. A preliminary sketch is constructed by calculating the MIC between nodes based on the improved Markov blanket search algorithm. Then, a preliminary undirect independent graph is completed by global edge thickening and thinning based on the CI test.

In the second step, subgraph decomposition is performed. First, the importance of the nodes in the sketch is scored according to the centrality of the path node. The central node and its neighborhood are extracted from the sketch as a subgraph following the principle from highest to lowest. The central node is defined as the identifier between the subgraphs. Afterward, the similarity between the subgraphs is calculated by the designed similarity function, and the subgraphs with high similarity will be deleted. Finally, the subgraph repair algorithm is used to repair nodes that have disappeared in subgraph de-duplication.

In the third step, subgraph learning is performed. The edge direction of these subgraphs is learned independently using a genetic algorithm (GA) based on Bayesian information criterion (BIC) scores.

In the fourth step, the subgraphs are recombined. Considering that different subgraphs may have the same edge with conflicting orientations, an approach is proposed based on the maximum benefit principle of a local BIC score to accomplish conflict edge coordination. After the coordination of conflicting edges has been completed, the subgraphs are reconnected to obtain the final BN.

# 3.1. Draft 

Aiming at the construction of an undirected independent graph, Dai et al. [16] proposed a construction method of a fast Markov blanket discovery algorithm (Fast-MBD). Combining MIC with CI test allows the correlation between nodes to be learned, and the initial sketch can be drafted according to the learned connection relationship. However, it is found that there are still some parts that can be improved in practical application. Therefore, following a brief description of the method, some improvements are also given in this paper.

Step 1: Preprocessing is conducted to reduce the search space of the Malkov search algorithm. Therefore, after the initialization of network learning shown in Figure 3, the matrix MIC is defined to store the calculation results based on the correlation between nodes (events) calculated by MIC. Then, the maximum MIC of the event is defined as $M M I C$, and the constraint conditions are given. For example, the coefficient of the value in Equation (7).

$$
M I C\left(X_{a}, X_{b}\right) \geq \alpha_{M I C} M M I C\left(X_{a}\right) \text { or } M I C\left(X_{a}, X_{b}\right) \geq \alpha_{M I C} M M I C\left(X_{b}\right)
$$

![img-2.jpeg](img-2.jpeg)

Figure 3. The initialization of drafting.

When the nodes satisfy the above equation, it is considered that there is a strong correlation and connection relationship between the nodes. After traversing all nodes in the network, a sketch is drawn based on the obtained connections. The process is shown in Figure 4.
![img-3.jpeg](img-3.jpeg)

Figure 4. Draft based on constraint.
Step 2: The neighborhood connection of each node is obtained by a CI test under a relatively loose constraint. A CI test is a typical method to evaluate the independent relationship between two nodes in the case of a given subset. Using hypothesis testing, the likelihood ratio test statistic is defined and compared to the chi-square distribution to obtain a $p$-value. Then, conditional independence is judged according to the set threshold. Dai et al. [16] use a large number of high-order subsets as condition sets in the process of the CI test. However, this method causes inaccurate high-order independence tests, the actual edge-adding effect is not very obvious, and the amount of calculation is large in practical application. Therefore, the process of the CI test has been simplified in this paper. Only the empty set and first-order subset will be selected as the condition set for the CI test. The pseudocode for this step is shown in Algorithm 1.

Distant nodes in a network are unlikely to impact each other. We assume that two nodes are said to be distant if the length of the shortest path connecting them is more extended than $k$ edges, where $k$ is a path length parameter dependent on the network itself. Then define $n b\left(X_{i}\right)$ and $n b_{\text {cand }}\left(X_{i}\right)$ to denote the set of neighbor nodes of $X_{i}$ and the set of candidate neighbor nodes of $X_{i}$, respectively. $\operatorname{sep}_{\text {cand }}\left(X_{i}, Y_{j}\right)$ is the candidate separation set. For each node $X_{i}$ in $G_{1}$, given the path length parameter $k$, the nodes which belong to the $k$-path neighborhood of $X_{i}$ will be found and put in a node set $n b_{\text {cand }}\left(X_{i}\right)$. Then sort $\left\{n b_{\text {cand }}\left(X_{i}\right) / Y_{j}\right\}$ based on the MIC in descending order and save them in node set $\operatorname{sep}_{\text {cand }}\left(X_{i}, Y_{j}\right)$. Next, CI tests for $X_{i}$ and $Y_{j}$ given the null set and condition set $\boldsymbol{Z} \subseteq \operatorname{sep}_{\text {cand }}\left(X_{i}, Y_{j}\right)$ will be conducted to detect the dependence relations between $X_{i}$ and $Y_{i}$. Once there is a $\boldsymbol{Z}$ which makes $X_{i} \perp Y_{j} \mid \boldsymbol{Z}$ hold and $Y_{j}$ will be deleted from $n b_{\text {cand }}\left(X_{i}\right)$, and if there is no $\boldsymbol{Z}$ that can make $X_{i} \perp Y_{j} \mid \boldsymbol{Z}$ hold then $Y_{j}$ will be added into $n b\left(X_{i}\right)$.

Step 3: The high-order CI test further determines the neighborhood structure of the node. In this phase, a parameter $N_{Z}$ has been set to limit the maximum-order CI test to avoid calculating high-order CI tests. If the order of the CI test condition set is over $N_{Z}$, the condition set will be reset. The pseudocode for this step is shown in Algorithm 2.

```
Algorithm 1 Edge Thickening algorithm
Input: sample data \(D\), an undirected graph \(G_{1}=\left(\boldsymbol{X}, E_{1}\right)\)
Output: an undirected graph \(G_{2}=\left(\boldsymbol{X}, E_{2}\right)\)
    Calculate the value of the path length parameter \(k\);
    FOR each node For each node \(X_{i} \in X\) DO
        Find nodes that belong to the \(k\)-path neighborhood of \(X_{i}\) and put them in a node set \(n b_{\text {cand }}\left(X_{i}\right)\);
        FOR each node \(Y_{j} \in n b_{\text {cand }}\left(X_{i}\right)\) DO
            Conduct a CI test for \(X_{i}\) and \(Y_{j}\) given the null set;
            IF the assertion \(X_{i} \perp Y_{j}\) holds DO
                Delete \(Y_{j}\) from \(n b_{\text {cand }}\left(X_{i}\right)\);
            ELSE
                \(\operatorname{Sort}\left\{n b_{\text {cand }}\left(X_{i}\right) / Y_{j}\right\}\) based on the MIC in descending order and save them in node set \(\operatorname{sep}_{\text {cand }}\left(X_{i}, Y_{j}\right)\);
            FOR each condition set \(\boldsymbol{Z} \subseteq \operatorname{sep}_{\text {cand }}\left(X_{i}, Y_{j}\right)\) DO
                Conduct a CI test for \(X_{j}\) and \(Y_{j}\) given \(\boldsymbol{Z}\);
                IF the assertion \(X_{i} \perp Y_{j} \mid Z\) holds THEN
                    Delete \(Y_{j}\) from \(n b_{\text {cand }}\left(X_{i}\right)\);
                ENDIF
                ENDFOR
                ENDIF
                IF there is no \(\boldsymbol{Z}\) that can make \(X_{i} \perp Y_{j} \mid \boldsymbol{Z}\) hold THEN
                    Add \(Y_{j}\) to \(n b\left(X_{i}\right)\);
                ENDIF
                ENDFOR
    ENDFOR
    21 ENDFOR
    22 Return \(G_{2}=\left(\boldsymbol{X}, E_{2}\right)\).
```

Sort $\boldsymbol{X}$ based on the elements number of $n b\left(X_{i}\right)$ in ascending order and save them in the node set $\boldsymbol{X}_{\text {sort }}$ firstly. For each node $X_{i} \in \boldsymbol{X}_{\text {sort }}$, we check the conditional independence relationship between $X_{i}$ and $Y_{j} \in n b\left(X_{i}\right)$ given the conditioning set $\boldsymbol{Z} \subseteq \operatorname{sep}\left(X_{i}, Y_{j}\right)$. If $N\left(n b\left(X_{i}\right) / Y_{j}\right)>N_{\boldsymbol{Z}}$, i.e., the elements number of $\left\{n b\left(X_{i}\right) / Y_{j}\right\}$ exceeds $N_{\boldsymbol{Z}}$, the $N_{\boldsymbol{Z}}$ order subset of $\left\{n b\left(X_{i}\right) / Y_{j}\right\}$ will all be saved in node set $\operatorname{sep}\left(X_{i}, Y_{j}\right)$. If not, $\left\{n b\left(X_{i}\right) / Y_{j}\right\}$ will be saved in $\operatorname{sep}\left(X_{i}, Y_{j}\right)$ as is. In addition, if there are multiple subsets in $\operatorname{sep}\left(X_{i}, Y_{j}\right)$, not all condition sets will be calculated to reduce the chance of unnecessary tests. A random selection of parts is calculated and these results are summed to serve the following process. If the statement $X_{i} \perp Y_{j} \mid \boldsymbol{Z}$ holds with the minimum likelihood ratio test statistic, the corresponding edge that connects $X_{i}$ and $Y_{j}$ should be removed. Then, we continue to take CI tests for $X_{i}$ and another node in $n b\left(X_{i}\right)$ until there exists a node in the $n b\left(X_{i}\right)$ that is conditional independent on $X_{i}$.

# 3.2. Decomposition 

Abnormity diagnosis BN is a network built to realize abnormity events (nodes) diagnosis. Every step of BN construction and learning should serve the ultimate goal of abnormity nodes' reasoning. Therefore, aiming at the undirected graph, this section proposes a BN decomposition method that combines subgraph extraction based on $k$-path node centrality and subgraph de-duplicating based on graph similarity calculation. The method is divided into three steps: subgraph extraction, de-duplication, and subgraph repair.

```
Algorithm 2 Edge Thinning algorithm
Input: sample data \(D, G_{2}=\left(\boldsymbol{X}, E_{2}\right)\)
Output: an undirected graph \(G_{3}=\left(\boldsymbol{X}, E_{3}\right)\)
    Calculate the value of condition set \(\boldsymbol{Z}\) 's maximum elements number parameter \(N_{\boldsymbol{Z}}\);
    Sort \(\boldsymbol{X}\) based on the elements number of \(n b\left(X_{i}\right)\) in ascending order and save them in the node set \(\boldsymbol{X}_{\text {sort }}\);
    FOR each node \(X_{i} \in \boldsymbol{X}_{\text {sort }}\) DO
        Stop \(=0 ;\)
        WHILE stop \(=0\) DO
            FOR each node \(Y_{j} \in n b\left(X_{i}\right)\) DO
            IF \(N\left(n b\left(X_{i}\right) / Y_{j}\right) \leq N_{\boldsymbol{Z}}\)
                Save \(\left\{n b\left(X_{i}\right) / Y_{j}\right\}\) as a subset in node set \(\left.\operatorname{sep}\left(X_{i}, Y_{j}\right)\right)\)
            ELSE
                Save all the \(N_{\boldsymbol{Z}}\) order subset of \(\left\{n b\left(X_{i}\right) / Y_{j}\right\}\) in node set \(\left.\operatorname{sep}\left(X_{i}, Y_{j}\right)\right)\)
            ENDIF
            \(I\left(X_{i}, Y_{j}\right)=0, L\left(X_{i}, Y_{j}\right)=0 ;\)
            FOR a few random conditioning set \(\boldsymbol{Z} \subseteq \operatorname{sep}\left(X_{i}, Y_{j}\right)\) DO
                Conduct a CI test for \(X_{i}\) and \(Y_{j}\) given \(\boldsymbol{Z}\),
                \(I\left(X_{i}, Y_{j}\right)=I\left(X_{i}, Y_{j}\right)+\left(X_{i} \perp Y_{j} \mid \boldsymbol{Z}\right) ;\)
                Compute the likelihood ratio test statistic \(L\left(X_{i}, Y_{j} \mid \boldsymbol{Z}\right)\)
                \(L\left(X_{i}, Y_{j}\right)=L\left(X_{i}, Y_{j}\right)+L\left(X_{i}, Y_{j} \mid \boldsymbol{Z}\right) ;\)
            ENDFOR
            Find \(Y_{\min }=\underset{Y_{j} \in n b\left(X_{i}\right)}{\operatorname{argmin}} L\left(X_{i}, Y_{j}\right) ;\)
            IF \(I\left(X_{i}, Y_{j}\right) \neq 0\), means the assertion \(X_{i} \perp Y_{j} \mid \boldsymbol{Z}\) holds THEN
                Remove \(Y_{j}\) from \(n b\left(X_{i}\right)\);
            ELSE
                Stop \(=1 ;\)
            ENDIF
            ENDFOR
        ENDWHILE
    ENDFOR
    Return \(G_{3}=\left(\boldsymbol{X}, E_{3}\right)\).
```

Step 1: Subgraph extraction based on the $k$-path node centrality. The pseudocode for this step is shown in Algorithm 3.

Node centrality is an index used to evaluate the relative importance of each node in the network. Assuming that the information traverses along a random path, then for any node in the graph, the centrality of the path node is defined as the sum of the probabilities from each node $X_{u}=\boldsymbol{X} \backslash\left\{X_{i}\right\}$ through the node.

Because the original calculation method takes a long time and has less than $1 \%$ effective calculation, this paper uses the improved RA- $k$ path (Randomized-Approximate $k$ path) algorithm to calculate the $k$-path node centrality. The RA- $k$ path algorithm uses a random iteration to calculate. In each iteration, the starting node $X_{u} \in \boldsymbol{X}$ of the path is randomly selected, the path length $l \in[1: k]$ is randomly defined, and a path is randomly traversed according to the principle of a random path. The specific calculation method of $k$-path node centrality is as follows:

$$
C_{k}\left(X_{i}\right)=k n \frac{\operatorname{count}\left(X_{i}\right)}{T}
$$

In the equation, $n$ is the number of nodes in the undirected graph, $T$ is the maximum number of iterative cycles, and $\operatorname{count}\left(X_{i}\right)$ is the number of random paths to access the node $X_{i}$ in the whole iterative period.

Combined with the study of the relevant nodes of the central node in the Markov blanket theory, this paper selects $k=2$;

Combined with Equation (8), the $k$-path node centrality of all nodes in the graph is calculated, and the vector $k_{-} c$ is defined to store the calculation results. After that, the extraction of subgraphs is implemented based on $k_{-} c$. The basic principle is to select the nodes with high node centrality and combine relevant expert knowledge of the application domain, then take these nodes as the central nodes of the subgraph. Extract each central node and part of its neighborhood as a subgraph, and the details are as follows:

Firstly, the stop judgment condition of subgraph extraction based on graph $G_{3}$ is given: (1) All the nodes of the graph $G_{3}$ are included in the extracted subgraphs; (2) The number of nodes that have not been extracted to subgraphs is less than $5 \%$ of the total number of nodes. If any of the above conditions are met, the extraction stops.

Based on the node centrality storage vector $k_{-} c$, the node $X_{\text {maxk_c }}$ with the highest node centrality is found, and its 1-path neighborhood is searched and stored to $n b\left(X_{\max k_{-} c}\right)$. The maximum number of nodes in the 1-path domain is defined as $N_{-} n b_{-} 1$. When the number of nodes in the 1-path domain is over or equal to $N_{-} n b_{-} 1$, the neighborhood search stops. In this paper, the central node of the subgraph is also a critical identification among subgraphs. Therefore, define $s u b G\left(X_{\max k_{-} c}\right)$ as a new subgraph whose central node is $X_{\max k_{-} c}$ and whose subgraph node set is $s u b V\left(X_{\max k_{-} c}\right), s u b V\left(X_{\max k_{-} c}\right)=\left[X_{\max k_{-} c}, n b\left(X_{\max k_{-} c}\right)\right]$. The connection relationship of the subgraph is extracted from the graph $G_{3}$ and saved in $s u b E\left(X_{\max k_{-} c}\right)$, followed by $s u b G\left(X_{\max k_{-} c}\right)=\left(s u b V\left(X_{\max k_{-} c}\right), s u b E\left(X_{\max k_{-} c}\right)\right)$. If it is less than $N_{-} n b_{-} 1$, continue searching for the remaining nodes in its 2-path neighborhood. It must be explained that the 2-path domain node is a node set of a 2-path from the center node, which naturally includes the nodes in the 1-path domain. Therefore, it is represented here as a search for the remaining nodes of the 2-path domain, i.e., the 1-path domain nodes of their respective 1-path domains. Based on the ascending order of node centrality in the 1-path domain (excluding 0-node centrality), the neighborhood is added to $n b\left(X_{\max k_{-} c}\right)$ from the node with the smallest node centrality. Until the number of nodes in $n b\left(X_{\max k_{-} c}\right)$ is $N_{-} n b_{-} 2$ or all the nodes in the 1-path domain are traversed, and the subgraph of the current central node is extracted.

When the extraction of the subgraph with $X_{\max k_{-} c}$ as the central node is completed, we could set the $k_{-} c\left(X_{\max k_{-} c}\right)$ to zero to continue the following extraction process. However, in the actual process, when a large number of nodes in the center of high nodes are distributed in the neighborhood of one path or two paths to each other, it is not possible to avoid a large number of subgraphs with highly overlapping structures in the extraction results by simply setting zero. Therefore, when an extraction is completed, reduce the frequency of the extracted neighbors in other subgraphs, or reduce the chance that nodes in the subgraphs are extracted as central nodes. Based on the above analysis, the parameter $\alpha_{k_{-} c}$ is designed:

$$
\begin{gathered}
k_{-} c\left(s u b V\left(X_{\max k_{-} c}\right)\right)=\alpha_{k_{-} c} * k_{-} c\left(s u b V\left(X_{\max k_{-} c}\right)\right) \\
k_{-} c\left(X_{\max k_{-} c}\right)=0
\end{gathered}
$$

where $\alpha_{k_{-} c} \in(0,1)$, and the exact value needs to be set concerning the application environment and the requirements of the experimental effect. After completing the processing of the $k$-path node centrality storage vector $k_{-} c$, the judgment is made based on the given extraction stop condition. If the stop condition is not satisfied, the subgraph is extracted based on $k_{-} c$; else, step 2 is conducted to remove the weight of the subgraph.

Step 2: The subgraph is de-duplicated based on the subgraph similarity. The pseudocode for this step is shown in Algorithm 4.

Due to a large number of coincidence nodes and structures between the extracted subgraphs, this section proposes an improved method based on the cut distance to measure the similarity between subgraphs. Firstly, the similarity calculation method is introduced.

```
Algorithm 3 Subgraph extraction algorithm
Input: \(G_{3}=\left(\boldsymbol{X}, E_{3}\right), k, T, N_{-} n b_{-} 1, N_{-} n b_{-} 2, a_{k_{-} c}\)
Output: a series of subgraphs subG
    Compute the k-path node centrality \(C_{k}\left(X_{i}\right)\) of every node \(X_{i}\) and save in save set \(k_{-} c\);
    flag \(=\) true;
    WHILE flag = true DO
        Find \(X_{\max k_{-} c}=\underset{X_{i} \in \mathbf{X}}{\operatorname{argmax}} k_{-} c\) as the Center for the new subgraph \(\operatorname{subG}\left(X_{\max k_{-} c}\right)\);
        Find nodes that belong to the 1-path neighborhood of \(X_{\max k_{-} c}\) and save them in node set \(\operatorname{subV}\left(X_{\max k_{-} c}\right)\);
        IF \(N\left(\operatorname{subV}\left(X_{\max k_{-} c}\right)\right)<N_{-} n b_{-} 1\)
            Find nodes that belong to the 2-path neighborhood of \(X_{\max k_{-} c}\) but not to 1-path neighborhood, sort them based on
\(k_{-} c\) in ascending order, and the nodes whose \(k_{-} c \neq 0\) will be saved in node set \(s u b V_{\text {temp }}\);
            Add the first \(N_{-} n b_{-} 2-N\left(\operatorname{subV}\left(X_{\max k_{-} c}\right)\right)\) nodes in the \(s u b V_{\text {temp }}\) into \(\operatorname{subV}\left(X_{\max k_{-} c}\right)\);
            ENDIF
            Get the connect relationship from \(G_{3}\) based on \(\operatorname{subV}\left(X_{\max k_{-} c}\right)\) and save them as \(\operatorname{subE}\left(X_{\max k_{-} c}\right)\), THEN
\(\operatorname{subG}\left(X_{\max k_{-} c}\right)=\left(\operatorname{subV}\left(X_{\max k_{-} c}\right), \operatorname{subE}\left(X_{\max k_{-} c}\right)\right)\);
            Set \(k_{-} c\left(\operatorname{subV}\left(X_{\max k_{-} c}\right)\right)=a_{k_{-} c} * k_{-} c\left(\operatorname{subV}\left(X_{\max k_{-} c}\right)\right)\);
            Set \(k_{-} c\left(X_{\max k_{-} c}\right)=0\);
            IF the components satisfy the stop condition DO
                Set flag = false;
            ENDIF
    END WHILE
    Return a series of subgraphs subG.
```

For two graphs $G_{a}, G_{b}$ defined on the same vertex set $V, G_{a}=\left(V, E_{a}\right), G_{b}=\left(V, E_{b}\right)$. Randomly selecting two subsets $U, W \subset V$. Define $e_{G}(U, W)$ to denote the number of edges between $U$ and $W$ in $G$, the cut distance between $G_{a}$ and $G_{b}$ is calculated as follows:

$$
d\left(G_{a}, G_{b}\right)=\max \frac{\operatorname{sum}\left|e_{G_{a}}(U, W)-e_{G_{b}}(U, W)\right|}{|V|^{2}}
$$

The equation measures the similarity of a graph defined on two vertex sets-the similarity increases as the value decreases. However, the vertex sets in the subgraphs may be different. This paper improves the cut distance to measure the degree of similarity between the two subgraphs to solve this problem. For the graph $G_{a}$ and $G_{b}$ defined on the different vertex set $V_{a}$ and $V_{b}, G_{a}=\left(V_{a}, E_{a}\right), G_{b}=\left(V_{b}, E_{b}\right)$, the similarity equation is calculated as follows:

$$
\begin{gathered}
d_{\text {com }}\left(G_{a}, G_{b}\right)=\left\{\begin{array}{l}
N\left(V_{\text {com }}\right)<N_{-} V_{\min }\left\|N\left(E_{\text {com }}\right)<N_{-} E_{\min }, d_{\text {inf }}\right. \\
\text { else, } \max \frac{\operatorname{sum}\left\|\varphi_{G_{a}}\left(U_{\text {com }}, W_{\text {com }}\right) E_{a}\left(U_{\text {com }}, W_{\text {com }}\right)-\varphi_{G_{b}}\left(U_{\text {com }}, W_{\text {com }}\right) E_{b}\left(U_{\text {com }}, W_{\text {com }}\right)\right\|}{\left|V_{\text {com }}\right|^{2}} \\
d\left(G_{a}, G_{b}\right)=\frac{\log _{u c} V_{\text {com }}}{\log _{u c} V_{a}} * \frac{1}{d_{\text {com }}\left(G_{a}, G_{b}\right)} \\
V_{\text {com }}=V_{a} \cap V_{b}
\end{array}\right.
$$

In the equation, $V_{\text {com }}$ is the intersection of $V_{a}$ and $V_{b}, N\left(V_{\text {com }}\right)$ represents the number of nodes in the intersection. Random subsets $U_{\text {com }}$ and $W_{\text {com }}$ are selected over $V_{\text {com }} . E_{\text {com }}$ represents the $[0,1]$ matrix of the edge connection relation of $G_{a}$ and $G_{b}$ in the intersection $V_{\text {com }} . N\left(E_{\text {com }}\right)$ represents the number of connected edges in the connection relation matrix, i.e., the number of 1 in the matrix. Because $G_{a}$ and $G_{b}$ are extracted from the graph $G_{3}$, $E_{a}\left(V_{\text {com }}, V_{\text {com }}\right)=E_{b}\left(V_{\text {com }}, V_{\text {com }}\right)=E_{\text {com }}, E_{a}\left(U_{\text {com }}, W_{\text {com }}\right)=E_{b}\left(U_{\text {com }}, W_{\text {com }}\right)$. Set $N_{-} V_{\min }$ and $N_{-} E_{\min }$ as the node and edge number of lower bound intersection. When the intersection of two graphs is less than the setting values, it is considered that the similarity between the two graphs is low. Then, a more significant set value $d_{\text {inf }}$ is assigned. Subgraph extraction is performed around several nodes with high $k$-path node centrality, meaning that the subgraphs' extraction, construction, and learning process are centered around the central

node. Therefore, in the subgraph, the nodes with different distances from the central node have different effects on the central node. A hierarchical approach is used to classify nodes with different path distances from the central node. The shorter path equals the higher level. The weight $\psi_{G_{a}}\left(U_{c o m}, W_{c o m}\right)$ is the measure of the level of the edge in $E_{a}\left(U_{c o m}, W_{c o m}\right)$ in the subgraph $G_{a}$. The edge level is taken from the weighting of the node level at both ends. The higher the node level at both ends, the higher the edge lever and the greater the weight value. Based on the symmetry of $d_{c o m}\left(G_{a}, G_{b}\right), d_{c o m}\left(G_{a}, G_{b}\right)=d_{c o m}\left(G_{b}, G_{a}\right)$ can be obtained. For two subgraphs of different sizes, $d_{c o m}$ based on $V_{c o m}$ cannot accurately measure the global similarity of the two subgraphs. The coefficient $\log _{w} V_{c o m} / \log _{w} V_{a}$ is introduced to correct while making $d\left(G_{a}, G_{b}\right) \neq d\left(G_{b}, G_{a}\right)$.

```
Algorithm 4 subgraph de-duplication algorithm
Input: a series of subgraphs subG, \(\delta_{d}\)
Output: A list of the subgraphs to delete delG
    Compute the subgraph similarity \(d\left(G_{a}, G_{b}\right)\) and save them in matrix \(M(d)\)
    flag \(=\) true;
    WHILE flag \(=\) true DO
        Take the column sum of the matrix \(M(d)\), find the maximum \(d\left(G_{\max }\right)\) and \(G_{\max }\);
        IF \(d\left(G_{\max }\right) \geq \delta_{d}\)
            Add \(G_{\max }\) into the list of the subgraphs to delete delG;
            Delete row and column which mean the similarity about \(G_{\max }\) in \(M(d)\);
            ELSE
                Flag \(=\) false;
            ENDIF
    END WHILE
    return delG.
```

Through traversing all subgraphs, we can get an asymmetric subgraph similarity relation matrix $M(d)$. By summing the column vectors of the matrix, we can get the comprehensive similarity between each subgraph and all other subgraphs. By setting the sum of the similarity threshold $\delta_{d}$, we can filter out the subgraph that currently exceeds the threshold and find its corresponding central node. Then, define the storage vector $d e l G$ to store the central node of the subgraph as the distinguishing identification of the subgraph, and add the center node to the vector delG. After that, delete the rows and columns that represent the similarity of the subgraph in $M(d)$. Repeat the calculation of the sum of similarity and filter the added operation until the maximum sum of similarity in the matrix $M(d)$ are less than the threshold $\delta_{d}$, then end the filtering operation. After that, the similarity between the whole subgraphs can be reduced by deleting these subgraphs. If the node is missing eventually, it needs to be repaired with the parent graph $G_{3}$, and the related process is shown in step 3.

Step 3: Subgraph repair. The pseudocode for this step is shown in Algorithm 5.
Firstly, all the corresponding subgraphs are deleted based on the delG. Then, based on the parent graph $G_{3}$, the storage vector $V_{-}$miss and storage matrix $E_{-}$miss are defined to store all the missing nodes and edges caused by subgraph de-duplication. The storage form is to store the two end nodes of the missing edges based on the parent graph $G_{3}$. After that, the missing edges and nodes are repaired based on $V_{-}$miss and $E_{-}$miss.

The missing edge set $E_{-}$miss based on the missing node set $V_{-}$miss can be divided into three types. Type I: both ends of the missing edge are non-missing nodes; type II: only one missing node at both ends of the missing edge; type III: both ends of the missing edge are missing nodes. Then, based on the classification, the missing edges and nodes are repaired according to types I, II, and III. The method is as follows.

For the edges in type I, they have been added to the target subgraph by traversing the first category of edges in $E_{-}$miss. The target subgraph is a subgraph with the lowest number of edges among the subgraphs containing any endpoint of the current edge. Specifically, add another node in the two endpoints that are not included by the target subgraph to the

node set of the target subgraph at first. Then use the new node set to update the connection of the edges of the target subgraph based on the graph $G_{3}$. When the addition is complete, remove the current edge from the $E_{-} \operatorname{miss}$ and continue traversing until the first category of edge does not exist in the $E_{-}$miss.

After traversing the edges in type I, the $E_{-}$miss should only contain edges in type II and III.

Continue traversing the edges in $E_{-}$miss in turn. Determine if the current edge is a type III edge at first. If true, put it at the end of the $E_{-}$miss, and move the position of the other edges forward one bit in turn, then continue to traverse. If the front edge is the type II edge or the type I edge (the reason type I edge appears here will be explained below), the previous edge is added to the target subgraph according to the adding way of the type I edge. The current edge is deleted from the $E_{-}$miss, and the nodes belonging to the missing nodes in the two endpoints of the current edge are deleted from the $V_{-}$miss. Then continue to traverse until the $E_{-}$miss is an empty set, traversal is over, i.e., step 3 subgraph repair is over.

In the process of repairing the type II and III edges, due to the completion of the repair of type II missing edges, the missing nodes contained in the edges are added to the subgraph, so the node is no longer missing. Therefore, the type II and III edges containing the node in the $E_{-}$miss will be updated to the type I and II edges, respectively. This explains why the type I edge appears in the "type II and III edge repair" step above and why the repair for the type III edge does not appear in this step.

```
Algorithm 5 subgraph repair algorithm
Input: a series of subgraphs subG, delG
Output: a series of subgraph subG after repairing;
    Delete subgraphs that have the higher subgraph similarity based on delG;
    Count the missing nodes in the remaining subgraphs based on \(G_{3}\) and save them in node set \(V_{-}\)miss;
    Count the missing edges in the remaining subgraphs based on \(G_{3}\) and save them by recording their two endpoints in node
set \(E_{-}\)miss;
    Divide the edges in \(E_{-}\)miss into three categories;
    FOR each type I edge from \(E_{-}\)miss DO
        Find all the subgraphs which include one or more nodes belonging to the edge;
        Select the most appropriate target subgraph subG arg according to the design rules;
        Add related node and edge into subG arg;
        Remove the edge from E_miss;
    ENDFOR
    FOR each edge from E_miss DO
        IF the edge belongs to the type III
            Move the edge to the end of E_miss;
        ELSE
            Add the edge into the target subgraph as the rule of type I edge;
            Remove the edge from E_miss, remove the related nodes from \(V_{-}\)miss;
            ENDIF
    ENDFOR
    Return a series of new subgraphs subG.
```


# 3.3. Subgraph Learning 

After the split of the large-scale network, this paper uses a hybrid method of traversal based on the BIC score and genetic algorithm to complete the sub-network learning.

Through extensive experiments, it was found that the proposed method above in this paper has an excellent effect on learning connection edges under the test of public data sets. Compared with the standard public data sets network, most connections can be learned with low error rates. Therefore, this paper only learns the direction of the connection in subgraph learning based on the BIC score.

For the subgraphs with a small number of nodes and fewer connected edges, learning optimal directional combinations can be accomplished by traversing all possibilities. For the graphs with more nodes and more connected edges, the genetic algorithm is still used to complete the search for the optimal direction combination with BIC as the score function. At the same time, to reduce the time consumption caused by a large number of BIC score calculations, this paper makes a simple optimization of the calculation process to accelerate this process.

# 3.4. Reunion 

After all the subgraph learning, it will appear that different subgraphs may have the same edge but conflicting directions. It is necessary to coordinate the conflicting edges before combining the subgraph. This section designs a method based on the maximum benefit principle of the local BIC score to complete the work of conflict-edge coordination. When the coordination of the conflicting edges is complete, the subgraphs are reconnected to get the final BN. The pseudocode for this step is shown in Algorithm 6.

Define two storage spaces $M_{\text {subV }}$ and $M_{\text {subE }}$ with dimensions $(N(s u b G) \times N(s u b G))$. Put all the subgraphs together and mark them with sequence numbers from 1 to $N(s u b G)$. $M_{\text {subV }}(i, j)$ represents the coincident nodes in the $i$ and $j$ subgraphs. $M_{\text {subE }}(i, j)$ stores the conflicting edges in the coincident structure of the $i$ and $j$ subgraphs in the form of a matrix, as shown in Equation (15) below.

$$
M_{\text {subE }}(i, j)=\left[\begin{array}{rrr}
i & i & i & \\
j & j & j & \\
X_{a} & \ldots & \ldots & \\
X_{b} & \ldots & \ldots & \\
-1 & -1 & -1 & \\
s c o_{-1} & \ldots & \ldots & \\
1 & 1 & 1 & \\
s c o_{1} & \ldots & \ldots &
\end{array}\right]
$$

Each column in the equation represents an edge of the coincident part of two subgraphs $i$ and $j$. Specifically, bits 1 and 2 store the sequence number of the two subgraphs in ascending order. Bits 3 and 4 store the sequence number of the nodes at both ends of the edge in the graph $G_{3}$ in ascending order. Bit 5 and bit 7 stores the possible connection direction of the current edge. -1 indicates that the end node $X_{a}$ in the graph points to an edge of the end node $X_{b}$, and 1 represents an edge pointing from the end node $X_{a}$ to the end node $X_{b}$ in the graph. Bits 6 and 8 records the BIC score in the case of two directions.

Some details need to be explained. First, the matrix only stores the score of the coincident edges. The number of columns of the matrix is determined by the number of edges existing in the coincident part of the subgraph $i$ and $j$, so the number of columns of the matrix is constant. Second, because the subgraph learning in the third step of this method only focuses on the direction learning of the existing edges, the current fourth step only coordinates whether the direction is forward or reverse. There is no case of deleting the existing edges, i.e., there is no case of direction $\operatorname{dir}=0$. Third, based on the separability of the BIC score, only the BIC score of the nodes at both ends of the changed direction change in the subgraph when a change in direction occurs. The scores of other nodes remain unchanged. To avoid unnecessary calculation, the BIC score was amended to involve the BIC numerical calculation of two end nodes, not the whole subgraph. After the third-step learning, the learned structure is optimal for the current subgraph. So the BIC score can only be compared from the "global" point of view of the two subgraphs. Here the BIC score is the sum of the BIC scores of the first subgraph and the two end nodes of the first subgraph. This is illustrated by a calculation example of sco $_{-1}$.

$$
\operatorname{sco}_{-1}=\operatorname{sco}_{B I C}\left(\operatorname{subG}(i),\left[X_{a}, X_{b}\right],-1\right)+\operatorname{sco}_{B I C}\left(\operatorname{subG}(j),\left[X_{a}, X_{b}\right],-1\right)
$$

$\operatorname{sco}_{B I C}\left(\operatorname{subG}(i),\left[X_{a}, X_{b}\right],-1\right)$ represents the sum of the BIC scores of the nodes $X_{a}$ and $X_{b}$ when the connection mode is -1 in the subgraph $\operatorname{subG}(i)$.

Because the whole recombination process is performed iteratively, the iterative process can be monitored by recording the direction of the edges of each subgraph after each iteration. The $N(s u b G)$-dimensional vector count_diff is defined. count_diff $f_{i} \in$ count_diff is defined to represent the number of changes in the edge direction of the $i$ element corresponding to the $i$ subgraph at the current iterative time. Furthermore, the termination condition of the iteration is given. The total number of edge direction changes occurring in the current iteration is 0 or less than a certain value.

The body of the specific iteration is the storage space $M_{\text {subE }}$. The BIC score returns of the two subgraphs with different directions are calculated by traversing the storage matrix of each conflict edge in $M_{\text {subE }}$. Then the final direction choice of the conflict edge is further determined. After the best direction is obtained at the current iterative time, the corresponding subgraph is updated according to that direction. After meeting the iterative conditions, i.e., after resolving the edges of the direction conflicts between all the subgraphs, all the subgraphs are spliced together based on the existing connections between nodes to obtain the final BN structure graph $G_{4}$.

To reduce unnecessary operations, a setting based on count_diff is given. When count_diff $f_{i}=0$, it is considered that the reunion of the subgraph with the current sequence number is over and will no longer participate in the subsequent iterations. That means the structure of subgraph $i$ is locked and will not be updated. At the same time, the column $i$ and column $i$ of $M_{\text {subE }}$ will be locked in the storage space $M_{\text {subE }}$, the calculation of BIC score benefits will no longer be performed. With the progress of the iterative process, more and more subgraphs are locked, and the direction conflict edges and the time required for calculation will be significantly reduced. Subsequent experiments have also demonstrated that this setting speeds up the iterative process and partially solves the problem of reciprocating changes in some edge directions for multiple reasons.

There is a problem in that the directions of the conflicting edges of two or more subgraphs change back and forth in the iterative process. The direction changes back and forth and then falls into some category of the endless loop if not take some method to intervene. Although the above count_diff-based setting solves the problem of reciprocating changes of some edge directions to some extent, this problem often occurs when there are conflicting structures in multiple subgraphs. The setting cannot play an influential role in reciprocating changes caused by only two subgraphs. Therefore, define another $N(s u b G)$ dimension vector count_e based on count_diff, count_e is to record the changes of count_diff, the function is as follows.

$$
\operatorname{count}_{-} \varepsilon_{i, k}=\left\{\begin{array}{c}
\text { count }_{\text {diff }_{i, k}} \neq 0 \text { and count }_{\text {diff }_{i, k}}=\text { count_diff }_{i, k-1}, \text { count_ } \varepsilon_{i, k-1}+1 \\
\text { count_diff }_{i, k}=0 \text { or count_diff }_{i, k} \neq \text { count_diff }_{i, k-1}, 0
\end{array}\right.
$$

where count_diff ${ }_{i, k}$ denotes the change of the number of edges of the subgraph $i$ in the $k$ th iteration, and count_diff ${ }_{i, k-1}$ is similar. When the count_diff ${ }_{i}$ changes constantly during the iteration, the count_ $\varepsilon_{i}$ is set to 0 ; when the count_diff ${ }_{i}$ is always kept at a non-zero number of edge changes, it may fall into a situation of reciprocating changes in direction. So some operation needs to intervene to help it escape the situation. After repeated experiments, the method was concluded by interrupting a change in one of the two subgraphs when they were caught in the situation. A subgraph can jump out of the situation by skipping the edge direction change. Therefore, we judge whether there is a reciprocating change of direction by monitoring whether there is a number greater than 0 in the count_e in the iterative process. If so, locate the two abnormal subgraphs and then randomly interrupt the direction change of a particular subgraph by setting a random number to jump out of this situation.

```
Algorithm 6 reunion algorithm
Input: a series of subgraph \(s u b G\) after subgraph learning
Output: a directed graph \(G_{4}=\left(\mathbf{X}, E_{4}\right)\)
1 Find the duplicate nodes among the subgraphs and save them in \(M_{\text {sub } b^{\prime} ;}\);
2 Find the edges with conflicting directions based \(M_{\text {sub } b^{\prime}}\) on and save them in \(M_{\text {subE }}\);
3 Initialization process monitoring variable count_diff, count_e;
4 WHILE true DO
5 FOR each component of \(\boldsymbol{M}_{\text {subE }}\)
6 Follow the designed rules calculate the BIC of direction conflicting edges with different directions and save the
results in \(M_{\text {subE }}\);
7 ENDFOR
8 Select the better direction for these direction conflicting edges based on the BIC result in \(M_{\text {subE }}\);
9 Update count_diff, count_e;
10 IF count_diff, count_e satisfy the stop condition DO
11 break WHILE
12 ENDIF
13 END WHILE
14 Reunion all subgraphs;
15 Return a directed graph \(G_{4}=\left(X, E_{4}\right)\).
```


# 4. Experimental Evaluation 

To verify the performance of the proposed method, the method is first tested by simulation in three numerical environments based on public data sets. Compared with other BN structure learning methods, analyze its advantages and disadvantages. Then, based on the abnormity data under the real coal mill process, it was verified whether the method conformed to the original design intention by comparing the abnormity diagnosis performance of the final model obtained by different methods. The purpose of the first experiment is to evaluate the accuracy and efficiency of the proposed algorithm in general. The purpose of the second experiment is to verify the validity of the method in the field of abnormal working conditions diagnosis, i.e., the inference performance for important nodes (abnormity nodes).

### 4.1. Simulation Verification Process Based on Standard BN

This section uses the public data set as experimental data. The dataset is three networks generated by a tiling algorithm using a Child network containing 20 nodes and 25 edges, namely Child3, Child5, and Child10. These standard BN networks of different scales have been widely used in various experimental studies on BN structure recovery [16,25,26]. At the same time, referring to the method setting of Dai et al. [16] in the simulation process and comparing the method's performance. This section also uses three synthetic data sets of different sizes to test the algorithm in the experiment of each standard network, the specific sizes of the three data sets are 500, 1000, and 5000. Table 1 shows information about the standard BN used for simulation testing.

Table 1. General information about benchmark BNs and data sets.


As to the common platform for fair comparisons, all the experiments below are run on a personal computer with Intel Core i7-10700F, $2.90 \mathrm{GHz}, 64$ bits architecture, 16 GB RAM, and under Windows 10. In addition, the algorithmic programs are all compiled using the Matlab software release R2021a.

In this paper, the statistical method's structural hamming distance (SHD) is introduced as an evaluation index of the accuracy of structural learning. Specifically, compare the learned network with the standard network and calculate the sum of edges added, subtracted, and reversed. At the same time, the algorithm's running time is recorded to compare the methods from the time dimension. This section tests the BN learning in the case of three groups of nine data sets given in Table 1 to compare the advantages and disadvantages of this method. Furthermore, the simulation results of this paper are compared with other methods, two constraint-based methods, and two hybrid learning methods. Recursive algorithm (REC) [27], Modified EEMB algorithm (Mod-EEMB) [28,29], Max min Hill-climbing algorithm (MMHC) [25], Decomposition-based BN Structure Learning Algorithm using Local topology information (Local-DSLA) [16]. Here, the relevant data are shown in Tables 2-4. Due to the different actual simulation environments, the running time is for reference only. At the same time, the best results of SHD and run time in the table are marked in bold font.

Table 2. Results for data Child3.


Table 3. Results for data Child5.


Table 4. Results for data Child10.


From the comparison results of BN structural learning, the accuracy of the method proposed in this paper is gradually improving with increasing dataset size on three networks of different sizes. This means our method has a better learning effect when the number of samples is sufficient (dataset size is 5000). At the same time, with the increase in the number of target BN nodes, the accuracy advantage of this algorithm tends to expand gradually, especially on Child5 and Child10 networks. Of course, the better learning effect also brings

the deficiency in the time dimension. It can be seen that the algorithm's operation in this paper will increase significantly with the amount of data. The impact of the number of BN nodes on the running time is relatively small. This method generally performs well in the case of large-scale nodes and sufficient data.

# 4.2. Application Study on Abnormity Diagnosis in Coal Mill Process 

### 4.2.1. Simulation Settings

This section uses the abnormity data of the actual process of the coal mill unit as the experimental data. The data comes from the actual operation data in the power plant. A unit in the pulverizing system contains five coal mills, of which four are used for industrial production and one for standby. The coal mill prosses is shown in Figure 5. The coal mill process includes a raw coal hopper, coal feeder, coal mill, and regulating valve. Raw coal enters the coal mill from the raw coal hopper through the coal feeder. The built-in grinding roller of the coal mill grinds the raw coal into pulverized coal. The cold and hot primary air is mixed by the regulating valve and blown into the coal mill. The mixed primary air carries the coal powder to the boiler, and the cinder not crushed into coal powder is discharged through the slag discharge valve.
![img-4.jpeg](img-4.jpeg)

Figure 5. Schematic diagram of a simplified coal mill process.
Through the integration of the data to varying degrees, four training sets of different sizes are formed, which are 500, 500, 2000, and 4000, respectively, and an independent test set containing 1000 sample data. Table 5 shows the relevant information for each dataset.

Table 5. General information of coal mill process abnormity diagnosis data sets.


The most common abnormal conditions in the coal mill process are powder blocking, coal blocking, and spontaneous combustion. By analyzing the operating mechanism of the coal mill, 15 variables are selected for each coal mill as learning nodes of the BN network. Table 6 defines the nodes in the abnormity diagnosis BN model, where "powder blocking", "coal blocking" and "spontaneous combustion" of each mill are the abnormity variables.

That is the diagnostic target of the abnormity diagnosis model. Here, the serial numbers of these nodes are marked in bold font.

Table 6. Physical meanings and the grades of nodes.


Furthermore, expert knowledge is defined here to compare the difference between the proposed method and the pure data method. That is, the target of the model is the abnormity node. Therefore, in the process of subgraph decomposition, the preliminarily extracted subgraph must contain the subgraph with the nodes mentioned above as the central node. At the same time, the subgraph with the nodes mentioned above as the central node must be retained first in de-duplicating the subgraph. Further, ensure that the learning process of the subgraph is conducted around the central node given by expert knowledge. Note that this is not a requirement that subgraphs can only be centered on these nodes but that subgraphs with other nodes as central nodes can appear.

# 4.2.2. Learning of Abnormity Diagnosis Model for Coal Mill Process 

The process based on dataset Mill4_train_4000 is taken as an example to illustrate some of the characteristics of the method. First, in the process of subgraph decomposition, the sketch is divided into 14 subgraphs before the introduction of expert knowledge; after the introduction of expert knowledge, the sketch is decomposed into 15 subgraphs. Obviously, because of the particularity of the data, the central nodes of the 15 subgraphs correspond to the 15 central nodes given by expert knowledge. For the specific impact on the decomposition results of the subgraph, see Figure 5.

Only three subgraphs with a central node of 7, 8, 9 are given in Figure 6, and the other subgraphs are not affected, and there is no difference. The upper part of the graph is the result of decomposition before and after the introduction of expert knowledge. Before the introduction, the subgraph with 8 as the central node is segmented due to the need for de-duplication between subgraphs. On the one hand, the structural complexity of the two subgraphs with the central node $7,8,9$ increases significantly; on the other hand, its neighborhood is incomplete for the abnormity node 8 . The reasoning performance of the final model to node 8 cannot be guaranteed. After the introduction, the above problems have been improved obviously.

![img-5.jpeg](img-5.jpeg)

Figure 6. Influence of expert knowledge on subgraph decomposition.
To further test the method's performance, refer to the simulation setting in Section 4.1. Based on the training set Mill4_train_4000 and the test set Mill4_test_1000, by using the proposed method combined with expert knowledge, proposed method without expert knowledge, Local_DSLA and MMHC, ten numerical experiments are conducted, respectively. The final abnormity diagnosis model is obtained, and the reasoning accuracy on the test set is calculated. The detailed data are shown in Table 7.

Table 7. Diagnostic accuracy of different BN.


It can be seen that when the training set is Mill4_train_ 4000, the method proposed in this paper has a better performance in model reasoning accuracy. Specifically, in the comparison of the accuracy of the diagnosis of abnormal working conditions for different BNs, the inference accuracy of the target node is significantly improved compared to the other two methods. At the same time, the average accuracy rate can also clearly reflect its advantages. It is worth noting that the model's performance has been further improved after the introduction of expert knowledge.

# 4.2.3. Comparison of Methods 

Furthermore, to test the performance of the method, based on the given four training sets, using the proposed method combined with expert knowledge, the proposed method without introducing expert knowledge, Local_DSLA and MMHC, ten numerical experiments are conducted, respectively. The reasoning accuracy of the final abnormity diagnosis model on the test set Mill4_test_1000 is counted, and the results are sorted out in Table 8 simultaneously. Use bold fonts to mark the model method with the best reasoning performance under the condition of each dataset.

Table 8. Diagnostic accuracy of different BN.


The following conclusions can be obtained from the data given in Table 8. First, the method proposed in this paper maintains the best reasoning accuracy under the conditions of each training set. The result proves that the method proposed in this paper has advantages in terms of algorithm design and performance in the field of abnormal working conditions diagnosis, which is in line with the original design of this method. Secondly, introducing expert knowledge can improve the model's performance, which is also mentioned in Section 4.2.2 above. Because of the particularity of the dataset, the central node of the decomposed subgraph is entirely consistent with the given expert knowledge. As a result, expert knowledge does not better show the improvement of the methods in this paper. Thirdly, by comparing the changes in reasoning accuracy of different methods under different training sets, we can see that the method proposed in this paper changes less with the change in the number of data. The results illustrate the stability and adaptability of the method proposed in this paper in abnormal working conditions diagnosis.

## 5. Conclusions

As the core equipment of the pulverization system in the thermal power plant, the abnormal working condition of the coal mill will not only affect the industrial production process but also reduce the production efficiency and even bring significant safety risks to the production process. Aiming at the structure learning problem of the abnormity diagnosis model for the coal mill process, a new BN structure hybrid learning algorithm based on model decomposition is designed in this paper, which has better fit and applicability to the research direction of abnormity diagnosis. The algorithm includes four stages: drafting, subgraph decomposition, subgraph learning, and subgraph reunion, and the implementation method is described in detail. The advantages and disadvantages of the algorithm are analyzed by comparing it with other methods based on the public data set. Further, based on the abnormity data of the coal mill process, the abnormity diagnosis model is built. By comparing the anomaly diagnosis performance of models obtained using different methods, it is proved that the method proposed in this paper does have advantages in the field of abnormity diagnosis, which is in line with the original intention of this method.

Author Contributions: Methodology, software, writing-original draft, writing-review and editing, Y.C., L.L. and X.K.; funding acquisition, supervision project administration, validation, Y.C. and F.W. All authors have read and agreed to the published version of the manuscript.

Funding: This research was funded by the National Natural Science Foundation of China (Grant Nos. 62273078 and 61973057) and the National Key R\&D Program of China (Grant Nos. 2019YFE0105000 and 2021YFF0602404).

Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: Not applicable.
Acknowledgments: The authors would like to thank everyone for their help.
Conflicts of Interest: The authors declare no conflict of interest.
