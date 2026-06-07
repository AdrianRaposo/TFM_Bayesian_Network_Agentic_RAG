# Article 

## Modeling the Evolution of Major Storm-Disaster-Induced Accidents in the Offshore Oil and Gas Industry

Gaogeng Zhu ${ }^{1}$, Guoming Chen ${ }^{1, *}$, Jingyu Zhu ${ }^{1}$, Xiangkun Meng ${ }^{2}$ and Xinhong Li ${ }^{3}$

## check for updates

Citation: Zhu, G.; Chen, G.; Zhu, J.; Meng, X.; Li, X. Modeling the Evolution of Major Storm-Disaster-Induced Accidents in the Offshore Oil and Gas Industry. Int. J. Environ. Res. Public Health 2022, 19, 7216. https://doi.org/10.3390/ ijerph19127216

Academic Editors: Xuelong Li, Liming Qiu and Xianfeng Liu

Received: 2 May 2022
Accepted: 6 June 2022
Published: 13 June 2022
Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## 0

Copyright: (c) 2022 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 Centre for Offshore Engineering and Safety Technology (COEST), China University of Petroleum (East China), Qingdao 266580, China; b15040134@s.upc.edu.cn (G.Z.); b18040022@s.upc.edu.cn (J.Z.)
2 Navigation College, Dalian Maritime University, Dalian 116026, China; mxk0117@dlmu.edu.cn
3 College of Resources Engineering, Xi'an University of Architecture and Technology, Xi'an 710055, China; lixinhong@xauat.edu.cn

* Correspondence: gmchen@upc.edu.cn


#### Abstract

Storm disasters are the most common cause of accidents in offshore oil and gas industries. To prevent accidents resulting from storms, it is vital to analyze accident propagation and to learn about accident mechanism from previous accidents. In this paper, a novel risk analysis framework is proposed for systematically identifying and analyzing the evolution of accident causes. First, accident causal factors are identified and coded based on grounded theory (GT). Then, decision making trial and evaluation laboratory (DEMATEL) is integrated with interpretative structural modeling (ISM) to establish accident evolution hierarchy. Finally, complex networks (CN) are developed to analyze the evolution process of accidents. Compared to reported works, the contribution is threefold: (1) the demand for expert knowledge and personnel subjective influence are reduced through the data induction of accident cases; (2) the method of establishing influence matrix and interaction matrix is improved according to the accident frequency analysis; (3) a hybrid algorithm that can calculate multiple shortest paths of accident evolution under the same node pair is proposed. This method provides a new idea for step-by-step assessment of the accident evolution process, which weakens the subjectivity of traditional methods and achieves quantitative assessment of the importance of accident evolution nodes. The proposed method is demonstrated and validated by a case study of major offshore oil and gas industry accidents caused by storm disasters. Results show that there are five key nodes and five critical paths in the process of accident evolution. Through targeted prevention and control of these nodes and paths, the average shortest path length of the accident evolution network is increased by $35.19 \%$, and the maximum global efficiency decreases by $20.12 \%$. This indicates that the proposed method has broad applicability and can effectively reduce operational risk, so that it can guide actual offshore oil and gas operations during storm disasters.


Keywords: storm disasters; offshore oil and gas accidents; causation evolution; DEMATEL-ISM; complex networks

## 1. Introduction

Offshore oil and gas production faces a number of harsh environments. In recent years, the number of weather-related natural disasters has grown sharply as have the costs associated with related losses [1,2]. Storm disasters, such as typhoons, hurricanes, tornadoes, and storm surges, significantly impact offshore oil and gas production, and can cause operational shutdown, facility damage, casualties, ecological crises, and even serious social unrest [3-5]. During Hurricane Harvey (2017), about 25\% of the oil and gas production in the Gulf of Mexico was shut down, and 105 production platforms ( $15 \%$ of the total) were closed, causing a fluctuation in oil and gas prices [6]. To avoid the repeated occurrence of accidents, lessons should be drawn from previous accidents [7-11]. Therefore, it is necessary to analyze the causal factors of major accidents in the offshore oil and gas industry that are caused by storm disasters and explore the accident development process.

To analyze the accident propagation path, it is necessary to carry out an accident investigation and identify causal factors or risk sources. At present, the most commonly used methods for accident analysis in offshore oil and gas operations include RCA, FTA, ETA, barrier analysis, and AcciMap [12]. RCA can identify the root causes of accidents through continuous iteration and improvement [13,14,15]. To ensure the accuracy and integrity of results, RCA requires a certain amount of judgement ability and a relatively exhaustive list of causal factors in advance. FTA is a method for graphically representing the possible causes of top events (i.e., accidents) and their causal relationship through top-down deductive analysis; however, this method cannot consider nonlinear interactions among causal factors [16,17]. ETA is primarily a proactive risk analysis method used for identifying the possible sequence of events after the initial event, but the choice of development paths largely depends on the level of individual knowledge and personal experience [18,19,20]. Through barrier analysis, the risks associated with cascading accidents can be identified to confirm the placement and performance of barriers. Combined with other methods (such as ETA), preventive measures for cascading accidents can be identified for offshore oil and gas operations [21,22]. AcciMap is not only a pure accident investigation tool, but can also capture socio-technical factors and illustrate the interactions among these factors causing corresponding events. With AcciMap, human and organizational factors in offshore oil and gas accidents can be highlighted [23,24,25]. All these methods have advantages but are highly subjective and deductive, thus requiring a strong level of expert knowledge and experience. For the same accident case, researchers with different experience and knowledge levels may obtain completely different results. This is very unfavorable in ensuring the accuracy of identifying the cause factors of accidents.

Complex systems often fail in complex ways, and accidents are usually the result of the interaction of multiple factors. Many methods have been proposed to analyze interactions among factors in accident propagation evaluation, including AHP, ANP, SEM, DEMATEL, and ISM [26,27]. AHP provides a convenient method for multi-objective and multi-criteria decision problems, which derives priority using a nominal scale through paired comparison of elements at the same level. As an extended form of AHP, ANP considers the dependence of elements among different hierarchies; however, the hierarchical structure of both methods is based on subjective expert judgments [28,29,30]. SEM measures the influence of each cause upon the effect, and the regression coefficient can be calculated to express the causal relationships among latent variables (i.e., factors) based on a large number of questionnaires [31,32,33]. By building a structural model containing causal relationships among complex factors, DEMATEL can analyze the interdependences among factors but is limited due to little information [34,35]. ISM is also an effective tool for identifying causal relationships among complex factors, and can help to clarify the hierarchy and priority of factors. Causal relationships are easy to grasp by ISM, but this method requires notable matrix computation resources [36,37]. All the above-mentioned methods have their own application scenarios and functional characteristics. A large number of questionnaires and computing resources are needed to obtain the quantitative interactions among different factors. At the same time, limited information can only judge whether factors are independent. Therefore, a single method cannot achieve efficient and accurate analysis of the interactions among factors in accident propagation evaluation.

To analyze the evolution of accidents, it is necessary to evaluate the propagation path of causative factors. BN has been widely applied for quantitative risk assessment, as forward predictive analysis and backward reasoning diagnosis can be carried out in BN [38,39]. The primary advantage of BN is its probability updating and continuous learning ability. In the field of the offshore oil and gas industry, BN is mainly used to evaluate the dynamic risk evolution of major accidents including blowouts and explosions [40,41], as well as the failure probability and reliability of key equipment and systems; examples are blowout preventer [42], submarine oil and gas pipeline [43,44], drilling riser [45], crude oil separation system [46], and managed pressure drilling system [47,48]. However, it is not easy to obtain the prior probability for BN. Besides, BN focuses on the assessment of the overall risk level

of the network, and cannot deal well with the problems of local risk and single path risk. Although BN can determine the importance of nodes through sensitivity analysis, it is hard to study the importance of different paths using the method of path attack. In addition, if the number of causal factors is large and the interaction relationships are complex, there may be a state explosion problem [49].

The limitations of these methods including strong subjectivity, unclear clarification of interactions among factors, and difficulty in assessing path risks. To address issues in the above-mentioned methods, this paper proposes a novel risk analysis framework for systematic identification and evaluation accident propagation. We start with the identification of the accident causes based on GT. Then DEMATEL is integrated with ISM to analyze interactions among factors. Finally, HADY is incorporated into CN to describe the evolution process of accidents and calculate shortest paths. Compared to reported works, the detailed contributions of the proposed method are summarized as follows:

1. GT is developed to objectively identify accident causal factors from original data, which can reduce personnel subjective influences imposed by their knowledge and skill level.
2. The use of DEMATEL-ISM can compensate for the shortcomings of insufficient information and high computing costs. In addition, the way to establish the direct influence matrix is improved according to the interaction matrix obtained from the objective analysis in the previous step.
3. A hybrid algorithm that can calculate multiple shortest paths of the accident evolution under the same node pair is proposed. Combined with the causal factors and interaction relationships obtained by GT and DETAMEL-ISM, CN can quantitatively describe the evolution process of accidents.

# 2. Methodology 

To analyze the evolution process of major accidents in the offshore oil and gas industry under storm disasters, a method for the systematic identification and analysis of the evolution process of accident causes is proposed and applied in a case study, which includes four main steps:

1. Identification of accident causal factors.
2. Analysis of the hierarchical structure of accident causes.
3. Research on the evolution process of accident causes.
4. Study of the application in a specific case

Firstly, accident causal factors are identified and coded based on GT, and interaction relationships among causal factors are analyzed according to the occurrence frequency of causal factors in the same case. Then, using the DEMATEL-ISM method, the influencing relationships among causal factors are analyzed. When the hierarchy of causal factors is divided, a hierarchy of accident evolution is established. Subsequently, the method of CN is used to determine the evolution model of accident causes, analyze the characteristics of accident evolution, and calculate the shortest paths of accident evolution. Finally, the systematic identification and analysis of the evolution process of accident causes is applied in a case study. The specific process is depicted in Figure 1.

### 2.1. Identification of Accident Causal Factors

As an inductive qualitative research method rooted in original data, GT is an effective tool to identify accident causal factors. So far, there have been three schools: classic GT [50], programmatic GT [51] and constructivist GT [52]. As an objective induction method, the obtained analysis results are more objective and reliable as they are based on accidentrelated data [53]. Considering the standardization and simplicity of programmed language and in line with the method, this paper is based on programmatic GT. The coding process of programmatic GT includes three main steps: open coding, axial coding, and selective coding [54]. The method of GT emphasizes constant comparison and abstraction to form a reliable theory; thus, theoretical saturation tests should be performed after coding.

![img-0.jpeg](img-0.jpeg)

Figure 1. Framework of the proposed methodology.

# 2.2. Analysis of the Hierarchical Structure of Accident Causes 

To analyze complex interaction relationships among accident causes, a suitable and efficient analysis method is needed. As important tools for system analysis and decision making, DEMATEL [55,56] and ISM [57] have been widely used in various fields. Nevertheless, DEMATEL fails to consider the influence of factors on itself, while ISM fails to consider the strength of influence relationships among factors. The integrated DEMATELISM method compensates for the deficiencies of both tools, and the integrated method also reduces the difficulty for effectively calculating the reachability matrix in ISM. By setting the threshold, DEMATEL-ISM eliminates the weak influencing relationship in the system and simplifies the structure of the system.

In this paper, the traditional method of DEMATEL-ISM is improved, by incorporating the following points:

1. When constructing the index system of causal factors, the categories obtained from GT are absorbed, and are put into the set $Y\left(y_{i} \delta y_{j} \in Y, i=1,2, \ldots, n ; j=1,2, \ldots, n\right)$ of causal factors, to reduce the influence of subjectivity and avoid the inconsistency of the index scope.
2. When establishing the matrix $\boldsymbol{F}$, the matrix $\boldsymbol{R}$ is referred based on expert scoring, to obtain more objective analysis results.
3. In the evolutionary hierarchy of accidents obtained from ISM analysis, the category frequency and the strength of influence relationships among factors obtained from GT and DEMATEL are presented simultaneously.
The specific algorithm steps are as follows:
4. Establish the matrix $\boldsymbol{F}=\left[f_{i j}\right]_{n \times n}$, where $f_{i j}$ represents the direct influence of factor $y_{i}$ on factor $y_{j}\left(y_{i} \delta y_{j} \in Y, i=1,2, \ldots, n ; j=1,2, \ldots, n . Y\right.$ is a set of system factors.). $\{0,1$, $2,3\}$ respectively represent $\{$ no influence, weak influence, medium influence, strong influence\} in the matrix $\boldsymbol{F}$.
5. Normalize the matrix $\boldsymbol{F}$ and obtain the matrix $\boldsymbol{C}=\left[c_{i j}\right]_{n \times n}$, where $c_{i j} \in[0,1]$ :

$$
\boldsymbol{C}=\frac{1}{\max _{1 \leq i \leq n} \sum_{j=1}^{n} y_{i j}} \boldsymbol{F}
$$

3. Develop the matrix $\boldsymbol{T}=\left[t_{i j}\right]_{n \times n}$ which is established to couple the direct and indirect influence relationships among factors:

$$
\boldsymbol{T}=\lim _{k \rightarrow \infty}\left(\boldsymbol{C}+\boldsymbol{C}^{2}+\ldots+\boldsymbol{C}^{k}\right)=\boldsymbol{C}(\boldsymbol{I}-\boldsymbol{C})^{-1}
$$

4. Calculate the $b_{i}, d_{i}, c_{i}$ and $a_{i}$ of each factor:

$$
b_{i}=\sum_{j=1}^{n} t_{i j}, d_{i}=\sum_{j=1}^{n} t_{j i}, c_{i}=b_{i}+d_{i}, a_{i}=b_{i}-d_{i}
$$

5. Develop the matrix $\boldsymbol{H}=\left[h_{i j}\right]_{n \times n}$ mainly for the purpose of considering the influence of factors on itself:

$$
\boldsymbol{H}=\boldsymbol{T}+\boldsymbol{I}
$$

6. Develop the matrix $\boldsymbol{K}=\left[k_{i j}\right]_{n \times n}$, which is established to simplify the weak influence relationship between factors and highlight the hierarchy of the system by selecting an appropriate threshold:

$$
\left\{\begin{array}{l}
k_{i j}=1, \quad t_{i j} \geq \lambda \\
k_{i j}=0, \quad t_{i j}<\lambda
\end{array}\right.
$$

7. Calculate the $Q_{i}$ and $P_{i}$ :

$$
\begin{aligned}
& Q_{i}=\left\{y_{i} \mid y_{i} \in Y, \quad k_{j i}=1\right\} \\
& P_{i}=\left\{y_{i} \mid y_{i} \in Y, \quad k_{i j}=1\right\}
\end{aligned}
$$

8. Establish the condition for hierarchical partitioning:

$$
P_{i} \cap Q_{i}=P_{i}
$$

If the above condition is satisfied, it is proved that the corresponding factors in $P_{i}$ can all be found in $Q_{i}$. Therefore, these factors are at a higher level. At the same time, the corresponding row $i$ and column $j$ are deleted from the matrix $\boldsymbol{K}$, and then step 7 and step 8 are repeated until all factors are deleted. The hierarchical structure of all factors is determined according to the order in which the factors are deleted.

# 2.3. Research on the Evolution Process of Accident Causes 

Based on graph theory and statistical mechanics, CN is an important tool for analyzing the structural characteristics and development process of complex systems. CN can describe the process of risk evolution and effectively evaluate dependent relationships among different factors. Many complex systems or processes in nature can be described by CN [58]. CN has been widely used in a variety of fields, such as transportation networks [59,60], power systems [61,62], natural disasters [63], and offshore oil and gas production [49,58].

According to the organization form of network nodes, the four basic models of regular networks, random networks, small-world networks, and scale-free networks can be classified. The small-world network is characterized by a large clustering coefficient and small average path length. The scale-free network reflects node growth and preference dependence based on small-world network characteristics, which are closer to the characteristics of network models in the real world [64,65].

# 2.3.1. Modeling of CN 

The CN graph is a data structure composed of nodes, edges, and weights. The CN graph is usually represented mathematically by $G=(V, E, W)$. The node in $V$ is denoted as $v_{i}$ by its order $i$. The edge linking $v_{i}$ with $v_{j}$ in $E$ is denoted as $e_{i j}$. If $e_{i j}$ and $e_{j i}$ represent the same edge, the graph is an undirected graph; otherwise, it is a directed graph. Each element in $W$ expresses the weight of $e_{i j}$, which is denoted as $w_{i j}$. If each $w_{i j}$ is equal to 1 , the graph is an unweighted graph; otherwise, it is a weighted graph. In this paper, the graph is a weighted network graph. The principal assumptions for the modelling can be summarized as follows: different events in the process of accident evolution can be represented by nodes, and the associations among events can be represented by weighted edges. Causal factors (nodes) are obtained by GT, and influence relationships (weighted edges) among factors obtained by DEMATEL-ISM. The accident evolution model is constructed by CN.

### 2.3.2. Characterization of CN

Every complex network has its unique topological structure and connectivity, and the transmission process of internal information cannot be obtained only by means of observation. Therefore, we need the specific measurement method to evaluate the characteristics of the complex network, so that we can have a deeper understanding of it. Through the discrimination and analysis of network characteristics, the critical nodes, critical paths, propagation modes, and development trends of accident evolution can be obtained. These findings can provide references for accident prevention, control and emergency. The principal models and the presentation of the main measurements for complex network characterization [49,64,65] are as follows:

The $k_{i}$ of $v_{i}$ refers to the number of edges connected to the node in the network. In a directed network, the $k_{i}$ is composed of two components: the $k_{i}^{\text {out }}$, which is equal to the number of outgoing edges or successor nodes, and the $k_{i}^{\text {in }}$, which is equal to the number of incoming edges or predecessor nodes. The $k_{i}$ is the simplest and most effective concept for measuring the importance of a node in a network:

$$
k_{i}^{\text {out }}=\sum_{j} e_{i j}, k_{i}^{\text {in }}=\sum_{j} e_{j i}, k_{i}=k_{i}^{\text {out }}+k_{i}^{\text {in }}
$$

where $e_{i j}$ is a connected edge from $v_{i}$ to $v_{j}$. If this edge exists, $e_{i j}=1$; otherwise, $e_{i j}=0$. Similarly, $e_{j i}$ is a connected edge from $v_{j}$ to $v_{i}$, and if this edge exists, then $e_{j i}=1$; otherwise, $e_{j i}=0$.

$P(k)$ is defined as the probability of selecting a node randomly in the network whose degree is $k$, i.e., the ratio of the number of nodes with $k_{i}=k$ to the number of all nodes in the network. $P(k)$ describes the most basic topological characteristics of the network and is also an important scale used to identify network types:

$$
P(k)=\frac{n_{k}}{n}
$$

where $n_{k}$ is the number of nodes in the network with the degree $k$, and $n$ is the order of the adjacency matrix (i.e., the number of nodes in the network).
$C C_{i}$ represents the connection relationship among all nodes that are adjacent to a node in the network. $C C_{i}$ is defined as the proportion of the actual number of connected edges of these neighboring nodes to the maximum number of possible connected edges. $C C_{i}$ reflects the importance and subsequent growth of this node among neighboring nodes. $C C$ is defined as the mean value of the $C C_{i}$ of all nodes in the network, which is an important index to measure network collectivization and represent the clustering ability of the network:

$$
C C_{i}=\frac{e_{i}}{m_{i}\left(m_{i}-1\right)}, C C=\frac{1}{n} \sum_{i=1}^{n} C C_{i}
$$

where $e_{i}$ is the actual number of connected edges of neighboring nodes for $v_{i}$, and the interconnection between two nodes in a directed network serves as two edges. $m_{i}$ is the number of neighboring nodes of $v_{i}$, which is defined as the sum of successor and predecessor nodes in a directed network (repeated nodes are only counted once).
$B C_{i}$ represents the probability of the shortest paths through this node in the network, and it is defined as the proportion of the number of shortest paths through this node to all shortest paths. $B C_{i}$ reflects the load and influence of a particular node in the network, and network robustness can be assessed by attacking nodes with high $B C_{i}$ :

$$
B C_{i}=\sum_{s \neq i \neq t} \frac{n_{s t}(i)}{N_{s t}}
$$

where $n_{s t}$ is the number of shortest paths from $v_{s}$ to $v_{t}$ that pass through $v_{i}$, and $N_{s t}$ is the total number of shortest paths from $v_{s}$ to $v_{t}$.

The degrees of dispersion of $B C_{i}$ for different nodes are large, thus normalization processing is performed:

$$
B C_{i}^{\prime}=\frac{B C_{i}}{(n-1)(n-2)}
$$

$l_{i j}$ is defined as the sum of edge weights for the shortest path between $v_{i}$ and $v_{j}$ (a pair of nodes) in the network. $l_{i j}$ is used to measure the shortest distance between two nodes in a network, which, in this paper, represents the maximum connectivity between two nodes. The maximum value of $l_{i j}$ between any two nodes $v_{i}$ and $v_{j}$ is denoted as $D$ of the whole network. $L$ reflects the overall connectivity and connection efficiency of the network, which is of great significance. $L$ is defined as the mean value of $l_{i j}$ between two random connected nodes in a directed network:

$$
L=\frac{1}{n_{l}} \sum_{i \neq j} l_{i j}
$$

where $n_{l}$ is the number of connected node pairs in the network.
To avoid divergence in the calculation of $L$ caused by unconnected node pairs, the concept of global efficiency is proposed. $G E$ is negatively correlated with $L$, which can quantify the efficiency of the network in transmitting information between nodes. $G E$ is an important index to measure the connectivity of one network, and is defined as the mean value of the reciprocal of $l_{i j}$ between two random nodes in the network:

$$
G E=\frac{1}{n(n-1)} \sum_{i \neq j} \frac{1}{l_{i j}}
$$

If there is an interconnected path between $v_{i}$ and $v_{j}$ in the directed network, both nodes are strongly connected. If every two nodes in a network are strongly connected, this directed network graph is a strongly connected graph. The subgraph of a directed network graph with the maximum connection strength is called the strongly connected component, and the strongly connected component with the largest scale is called the maximum strongly connected component. $M K$ is defined as the number of nodes in the maximum strongly connected component of the directed network graph, which reflects the robustness of the network under attack.

As the sum of edge weights is needed to calculate the shortest path, the concept of entropy is used to represent edge weights in the network, to meet the needs of studying the network characteristics and searching paths:

$$
e w_{i j}=\ln \left(10^{4-w_{i j}}\right)
$$

# 2.3.3. Shortest Paths of CN 

There are two commonly used algorithms for shortest paths in CN: the Floyd algorithm and the Dijkstra algorithm. The Floyd algorithm [66] adopts the idea of dynamic program-

ming, and it is suitable for solving the shortest path problem between any two nodes. The Dijkstra algorithm [67] adopts a greedy search strategy, and it is suitable for solving the shortest path problem with a single source. The Yen algorithm [68] is currently the most widely used algorithm to solve the problem of K shortest paths. Considering the lower time complexity of the Dijkstra algorithm, the shortest path is calculated by the Dijkstra algorithm. However, the conventional Dijkstra algorithm can only calculate one shortest path for the same initial node and target node. Therefore, the HADY is proposed to calculate all shortest paths of specified node pairs in the network.

The idea of HADY is firstly to obtain a shortest path of the specified node pair in the original network by the Dijkstra algorithm. By constantly removing the edges and their combinations of known shortest paths from the original network, the shortest path network of the specified node pair is obtained, and then, the shortest path network is transformed into an unweighted network. Finally, the Yen algorithm is used to solve K shortest paths of the shortest path network, and multiple shortest paths, sorted by the number of nodes, are obtained. The flow chart of HADY is shown in Figure 2.

![img-1.jpeg](img-1.jpeg)

**Figure 2.** Flow chart of HADY.

The detailed steps of this algorithm are as follows:

1. Set the edge set of shortest paths *SP* = Ø (the initial *SP* is the empty set). The initial node is *v<sub>s</sub>*, and the target node is *v<sub>t</sub>*. The initial *k* is 1.
2. The Dijkstra algorithm is used to obtain a shortest path from *v<sub>s</sub>* to *v<sub>t</sub>* in the original network *G*. All edges of the shortest path are put into the set *SP*. The number of edges is denoted as *sn*, and the length of the path is denoted as *l*.
3. List all combinations of *k* edges taken from the set *SP* and put them into the set *SK*. There are *kn* combinations in total, and the initial *i* is 1.
4. Take the *i*-th combination from *SK* and delete the set of corresponding edges *SK(i)* in the original network *G*. The Dijkstra algorithm is used to find the shortest path from *v<sub>s</sub>* to *v<sub>t</sub>* in the modified network *G<sub>1</sub>*, and all edges of the shortest path are put into the set *ST*. The length of the path is denoted as *d*, and *i* = *i* + 1.
5. Determine whether a new edge of the shortest path is added. If *d* = *l* and *SP* ∪ *ST* ≠ *SP*, a new edge has been added. Then, the logical value *a* = 1, *SP* = *SP* ∪ *ST*, and the number of edges is recalculated and denoted as *sn*. Otherwise, no new edge is added, the logical value *a* = 0, *SP* = *SP*, and the number of edges is denoted as *sn*.

6. Determine whether all combinations have been taken out. If $i \leq k n$, not all combinations are taken out, and step 4 will be taken. Otherwise, if all combinations have been taken out, step 7 will be taken.
7. Determine whether this combination should be carried out again. If $a=1$, this combination should be carried out again, then $k=1$. Otherwise, there is no need to carry out this combination again, then $k=k+1$.
8. Determine whether all combinations have been listed. If $k \leq s n$, not all combinations have been listed, then step 3 will be taken. Otherwise, all combinations have been listed, then step 9 will be taken.
9. The set of all edges of shortest paths $S P$ is used to form the shortest path network graph $G_{2}$. All edge weights in $G_{2}$ are set to 1 (i.e., unweighted network), and $K=1$.
10. $K$ shortest paths from $v_{s}$ to $v_{t}$ in the unweighted shortest path network graph $G_{2}$ are obtained by the Yen algorithm and put into the set $S P_{K}$.
11. Determine whether the combined algorithm has been completed. If $S P_{K}=\varnothing$, step 12 will be taken; otherwise, $K=K+1$ and step 10 will been taken.
12. The sets $S P_{1}$ to $S P_{K}$ are all the shortest paths from $v_{s}$ to $v_{t}$ in the original network $G$, and the length of the shortest path is $l$.

# 3. Case Study 

A case study of major offshore oil and gas industry accidents caused by storm disasters is carried out, applying the proposed method. Firstly, causal factors are identified. Then, the hierarchy structure of the evolution of causes is studied. Finally, the evolution model of the accident causes is constructed to analyze the network characteristics and calculate the shortest path. The flow chart of the case study is shown in Figure 3.
![img-2.jpeg](img-2.jpeg)

Figure 3. Flow chart of the case study.

The selection of original data is the first step of the research, and its accuracy and detail are the foundation of successful research, which also guarantees the reliability of the results. To guarantee the accuracy and reliability of the results, the data selected in this paper are mainly obtained from official accident investigation reports, accident announcements and accident statistics of competent authorities, news reports of mainstream media, and accident databases of authoritative institutions. Meanwhile, we only selected accidents with detailed processes, and we focused on those cases that cause serious structural damage or casualties. In addition, three groups of experts (from university, research institute, and offshore platform) were responsible for the analysis. Each team consisted of three members and performed an independent analysis of the same data. Through comparison and analysis, the final results were extracted to avoid inconsistency of concepts and categories caused by differences in theoretical sensitivity. Through these measures, the accuracy, reliability, and availability of the results are further guaranteed.

# 3.1. Identifying Causal Factors of Offshore Storm Accidents 

### 3.1.1. Coding of Accident Causal Factors

In this paper, a total of 78 major accidents in the offshore oil and gas industry caused by storms were selected, involving 215 different types of data. Details of the accidents are presented in Appendix A [69-74]. Among the selected 78 cases, 72 cases were randomly selected for coding, and the remaining six cases were used for theoretical saturation tests. After coding of the accident-causing factors based on the selected accident cases, the results of three groups of analysis were compared, discussed, and integrated. Subsequently, a total of 63 concepts, 25 categories, nine main categories, and three core categories were obtained, as shown in Table 1. Finally, an experienced researcher was invited to conduct independent coding of the remaining six cases (No.5, No.12, No.18, No.31, No.42, and No.66) based on the same method. It was found that no new coding was generated, proving that the existing coding has covered all the accident cases. This indicated that the results satisfy the theoretical saturation test requirements. If the new coding appears, this indicates that the existing coding does not cover all accident cases. Then more accident cases need to be added and recoded until the verification test is passed. This step can further ensure the accuracy and reliability of the analysis results.

Table 1. Statistics of coding for causal factors.


Table 1. Cont.


Table 1. Cont.


According to Table 1, inclement weather $\left(y_{1}\right)$, loss of watertight integrity $\left(y_{13}\right)$, lack of risk awareness $\left(y_{21}\right)$, poor state of the platform $\left(y_{14}\right)$, damage of support structures $\left(y_{10}\right)$, damage of platform facilities $\left(y_{12}\right)$, and damage of watertight structures $\left(y_{11}\right)$ are the most frequently occurring categories. Attention needs to be focused in those categories.

# 3.1.2. Analyzing Interaction Relationships among Causal Factors 

To analyze interaction relationships among different categories, the matrix $S=\left[s_{i j}\right]_{n \times n}$ is defined, where $s_{i j}(i=1,2, \ldots, n ; j=1,2, \ldots, n)$ represents the interaction value between the two categories. $s_{i j}$ is defined as the ratio of the number of intersection cases to the number of union cases the two categories belong to. After calculating and processing, the matrix $\boldsymbol{R}=\left[r_{i j}\right]_{n \times n}$ is obtained. $\{0,1,2,3\}$ in the matrix represents \{no interaction, weak interaction, medium interaction, strong interaction\}, respectively. The calculation rules are as follows:

$$
\left\{\begin{array}{l}
r_{i j}=0, \quad s_{i j}=0 \\
r_{i j}=1, \quad 0<s_{i j} \leq 0.1 \\
r_{i j}=2, \quad 0.1<s_{i j} \leq 0.4 \\
r_{i j}=3, \quad s_{i j}>0.4
\end{array}\right.
$$

### 3.2. Developing the Hierarchy of Causes of Offshore Storm Accidents

Based on the 25 causal factors (i.e., the categories) extracted by GT, DEMATLE-ISM is used to analyze influencing relationships and establish the hierarchical structure of the accident causation evolution.

### 3.2.1. Analyzing Influence Relationships among Causal Factors

The centrality and causality of accident-causing factors are plotted on a Cartesian coordinate system, as shown in Figure 4.
![img-3.jpeg](img-3.jpeg)

Figure 4. Centrality and causality of factors.

According to Figure 4, factors such as damage to watertight structure (*y*_{11}), damage to platform facility (*y*_{12}), loss of water-tightness (*y*_{13}), and poor state of the platform (*y*_{14}) have higher centrality. This indicates that these factors play an important role in the accident-causing process. Inclement weather (*y*_{1}), lack of risk awareness (*y*_{21}), and inadequate safety training (*y*_{22}) have higher causality, indicating that these factors greatly impact other factors in the process of accident development and are the main causes of accidents.

### 3.2.2. Establishing the Hierarchical Structure of Causal Factors

In the transformation process from the matrix **H** to the matrix **K**, *λ* = 0.09 is chosen as the appropriate threshold. According to the obtained **K**, the system hierarchy is divided, and then, the accident evolution hierarchy is determined. The result is shown in Figure 5, in which only the influencing relationships among factors at adjacent levels are presented. In Figure 5, the circle shape represents the cause factor, while the hexagon shape represents the result factor. The size represents the category frequency obtained in the analysis of GT, which is divided into four levels (the larger the size, the higher the frequency of occurrence). The shading represents the centrality of the factor, which is divided into three levels (the darker the color, the greater the centrality). The thickness of the line between different levels represents the influence relationship between levels (the thicker the line, the stronger the influencing relationship).

![img-4.jpeg](img-4.jpeg)

**Figure 5.** Hierarchical structure of causal factors.

According to Figure 5, the 25 causal factors are divided into six layers. L1 is the surface layer, which is the direct cause of the accident. L2 and L3 form the shallow layer, and represent early signs of the accident. L4 and L5 form the deep layer, and represent the concentrated emergence of accident causes. L6 is the ground layer, which is the root of the accident. In terms of factors, inclement weather (*y*_{1}) and lack of risk awareness (*y*_{21}) are the root causes of accidents. Collision of fixed object at sea (*y*_{4}), collision of floating object at sea (*y*_{5}), and collision of object on the platform (*y*_{6}) have complicated influence relationships with other factors that belong to upper and lower levels. Damage to support structure (*y*_{10}) and loss of water-tightness (*y*_{13}) have high centrality and occurrence frequency, and are key factors in accidents. Damage to platform facility (*y*_{12}) is the only path for the propagation of the causative factors at upper and lower layers. When the watertight structure is damaged (*y*_{11}) and the platform is in poor condition (*y*_{14}), accidents are more likely to happen than usual. At this time, all necessary control measures should be taken, and emergency work should be carried out to mitigate the consequences of the accident.

### 3.3. Analyzing the Evolution Process of Offshore Storm Accidents

Based on the modeling principle of CN, the accident evolution model of the offshore oil and gas industry under storm disasters is established, combining 63 concepts extracted

from GT by analyzing the evolution hierarchy of accidents. Using this model, the accident evolution characteristics are analyzed, and the shortest evolution paths are calculated.

# 3.3.1. Modeling the Evolution Process of Accident Causes 

In line with the construction method of the matrix $\boldsymbol{R}$, the matrix $\boldsymbol{R} \boldsymbol{X}$ is established. In combination with the matrix $\boldsymbol{F}, 63$ concepts are put into the set of $X\left(x_{i} \mathcal{E} x_{j} \in X\right)$ to establish the matrix $\boldsymbol{A}=\left[a_{i j}\right]_{n \times n}$, where $n$ represents the order of $\boldsymbol{A}$, and $a_{i j}$ represents the connectivity from $x_{i}$ to $x_{j}$. In the matrix $\boldsymbol{A},\{0,1,2,3\}$ represents \{no connectivity, weak connectivity, medium connectivity, strong connectivity\}, respectively. According to the matrix $\boldsymbol{A}$, a weighted directed CN graph is plotted, in which $v_{i}$ is represented by $x_{i}$, and $a_{i j}$ is taken as $w_{i j}$. In the established graph, the thickness and length of the line represent the connectivity between two nodes. Corresponding to thicker and shorter lines, a larger weight represents a greater connectivity, as shown in Figure 6.
![img-5.jpeg](img-5.jpeg)

Figure 6. CN model of accident evolution.
In Figure 6, the whole network is obviously divided into two subnetworks, which are the region A centered on $x_{1}$ (strong ocean storm) and huge $x_{2}$ (ocean wave), and the region B centered on $x_{51}$ (inadequate risk perception) and $x_{52}$ (inadequate risk response). The internal connection of these two subnetworks is complex and the average connectivity is high, which means that internal factors are closely related. The region A and the region B are connected through intermediate nodes including lack of $x_{17}$ (watertight subdivision isolation), $x_{47}$ (violation of towing operation), et al. The nodes at the edge of the subnetwork have higher connectivity with intermediate nodes, but the internal nodes of the two subnetworks need to be connected through edge nodes as medium. The average connected path between these nodes is long and the connection relationship between them is sparse. The whole network shows clear community structure characteristics.

### 3.3.2. Analyzing the Evolution Characteristic of Accident Causes

The $k_{i}, k_{i}^{\text {in }}$, and $k_{i}^{\text {out }}$ in the network are calculated, and nodes with high values are: $x_{1}$ (strong ocean storm), $x_{2}$ (huge ocean wave), $x_{8}$ (collision of buildings), $x_{9}$ (collision of vessels), $x_{12}$ (collision of cargos), $x_{13}$ (collision of lifeboats), $x_{37}$ (list of the platform) and $x_{51}$ (inadequate risk perception). At the same time, $P(k)$ in the network is calculated, which presents the characteristics of power law distribution $\left(P(k)-k^{-\beta}\right)$ where $\beta=2.82$, which is consistent with the distribution feature of $\beta=2 \sim 3$ in a scale-free network. The $C C_{i}$ and $B C_{i}$ of all nodes in the network are calculated, as shown in Table 2.

Table 2. Results of *CC* and *BC*.


According to Table 2 and based on Figure 6, the network characteristic graph of the accident evolution is drawn, as shown in Figure 7. The size of the node represents the value of *CC*, and the color shade of the node represents the value of *BC*. A larger size represents greater *CC*, and a darker shade represents greater *BC*.

![img-6.jpeg](img-6.jpeg)

*X*16 *X*17 *X*18 *X*19 *X*20 *X*21 *X*22 *X*23 *X*24 *X*25 *X*26 *X*27 *X*28 *X*29 *X*30 *X*31 *X*32 *X*33 *X*34 *X*35 *X*36 *X*37 *X*38 *X*39 *X*40 *X*41 *X*42 *X*43 *X*44 *X*45 *X*46 *X*47 *X*48 *X*49 *X*50 *X*51 *X*52 *X*53 *X*54 *X*55 *X*56 *X*57 *X*58 *X*59 *X*60 *X*61 *X*62 *X*63 *X*64 *X*65 *X*66 *X*67 *X*68 *X*69 *X*70 *X*71 *X*72 *X*73 *X*74 *X*75 *X*76 *X*77 *X*78 *X*79 *X*80 *X*81 *X*82 *X*83 *X*84 *X*85 *X*86 *X*87 *X*88 *X*89 *X*90 *X*91 *X*92 *X*93 *X*94 *X*95 *X*96

**Figure 7.** Characteristic of the evolution network of accidents.

In Table 2 and Figure 7, the maximum *CC* is 0.5, and the corresponding nodes are *x*15 (improper screws), *x*19 (design defect of single hull tankers), *x*44 (poor performance of protective clothing), and *x*48 (wrong wellhead connection). However, the number of neighboring nodes of these nodes is too small to be representative. Among the other nodes, the maximum *CC* is 0.45, corresponding to *x*55 (insufficient auxiliary vessels), *x*56 (insufficient lifeboats), and *x*57 (insufficient emergency protective equipment), and these nodes have many neighboring nodes, indicating their relatively high collectivization. Therefore, adequate emergency equipment can effectively suspend the rapid escalation of accidents. The *CC* of the network is 0.223, which is far less than 1, but also much more than 1/*n* = 0.016. This is in line with the characteristics of the real-world network, which proves the feasibility of the established network.

In Table 2 and Figure 7, nodes with high *BC* are *x*41 (power system failure), *x*38 (thruster failure), *x*37 (list of the platform), *x*31 (flooding of deck), and *x*33 (flooding of subdivision), indicating that there are multiple shortest paths through these nodes. In other

words, these nodes are where the accident evolution most likely passes. Therefore, the proper functioning of the power system, thrusters, and other equipment should be ensured, as this can effectively reduce the network connectivity and the possibility of accidents. The same applies to the stability and water tightness of the platform.

The $L$ of the network is 12.69 , and the $D$ of the network is 32.24 . $L$ is far less than $D$, indicating that the accident evolution has small-world network characteristics. The $G E$ is $4.01 \times 10^{-2}$, which indicates that the network has strong connectivity ability and efficiency. The $M K$ is 21 , indicating that interconnected paths exist among these 21 nodes in the network, and the overall robustness of the network is strong.

# 3.3.3. Calculating Shortest Evolution Paths of Accident Causations 

According to the evolution hierarchical structure and statistical frequency shown in Figure 5 and Table 1, $x_{1}$ (strong ocean storm), $x_{2}$ (huge ocean wave), $x_{3}$ (rapid ocean current), $x_{51}$ (inadequate risk perception), and $x_{52}$ (inadequate risk response) in the ground layer (L6) are selected as initial nodes, and $x_{31}$ (flooding of decks), $x_{33}$ (flooding of cabins), and $x_{37}$ (list of the platform) in the surface layer (L1) are selected as target nodes. These nodes result in a total of 15 node pairs (i.e., 15 shortest path groups). The proposed HADY is used to obtain the shortest path network graphs, and the thickness of the line represents the connectivity between two nodes, where stronger connectivity corresponds to thicker lines, as shown in Figure 8. The network graphs of shortest paths for different target nodes are presented in Appendix B.
![img-7.jpeg](img-7.jpeg)

Figure 8. Network diagram of shortest paths.
According to the HADY, the shortest paths and lengths are calculated, and a total of 43 shortest paths are obtained. The specific results are shown in Table 3.

In Table 3, a total of five pairs of nodes have the least number of paths (only one path), and the node pair with the largest number of paths is path_3, which has eight shortest paths. For the same node pair, the more paths there are, the more difficult it is to control the evolution process. Because even if one of the paths (i.e., the causative chain) is blocked, there may be other evolution paths. Therefore, attention should be paid to node pairs with multiple shortest paths, and the node or edge with the highest blocking efficiency should be selected as control. For example, if the edge $x_{37} \rightarrow x_{31}$ or the node $x_{37}$ is removed from the eight shortest paths of path_3, the number of shortest paths decreases from eight to two, and the blocking efficiency increases to $75 \%$.

Table 3. Shortest paths of accident evolution.


In addition, the node pair of the minimum shortest path length is $\left(x_{2}, x_{31}\right)$ with a length of 2.30 , while the node pair of the maximum shortest path length is $\left(x_{3}, x_{31}\right)$ with a length of 13.82. The shorter path length represents stronger connectivity and greater possibility of accident occurrence. All shortest paths have at least one edge and five edges at most. For the same path length, more edges represent more nodes, i.e., the development process of accidents involves more causative factors. This also indicates that there are more optional control measures.

In general, the longer the shortest path length of a node pair, the more paths and the more edges there are. However, high risk features (e.g., shorter path length, fewer edges, and more paths) generally do not appear on the same path. Therefore, when controlling the evolution path of accidents, the high risk features of paths should be identified first. Subsequently, appropriate prevention and control measures should be taken.

To quantify the importance of different shortest path groups, according to the 15 shortest path groups listed in Table 3, intentional attacks of two modes are carried out on the original network:

1. Attack only the edges of the shortest path;
2. Attack both the edges and intermediate nodes of the shortest path.

The $l, G E$ and $M K$ under the two attack modes are analyzed, as shown in Figure 9.

![img-8.jpeg](img-8.jpeg)

**Figure 9.** Comparison of (**a**) *l*, (**b**) *GE* and (**c**) *MK* under different attack modes.

In Figure 9a, the *l* of different shortest path groups under the attack mode 1 is consistent with that under the attack mode 2. Compared with the original network, all *l* increase under both attack modes. The average increased proportion of all *l* is 35.19%, indicating that the shortest path length increases and the connectivity reduces under both attack modes, which can reduce the possibility of accidents. In Figure 9b, the average decreased proportion of *GE* is 3.43% under the attack mode 1, and the average decreased proportion of *GE* is 8.94% under the attack mode 2. A comparison of both attack modes shows that the change trend of *GE* is almost identical. In Figure 9c, the average *MK* of the network is 20.73 under the attack mode 1, and the average *MK* of the network is 18.1 under the attack mode 2. Compared with the attack mode 1, the *MK* of the network decreases most when attacking path_3 under the attack mode 2, and the decrease proportion is 42.11%. Compared with the original network, the attack effects of the two attack modes are not ideal. This indicates that the original network has strong robustness. In such a case, attacking a single path or node can hardly reduce the robustness of the network.

The research above treats multiple shortest paths of the same node pair as a whole. To study the influences of different shortest paths of the same node pair on the network, it is necessary to integrate various network characteristics under attack. After normalization and summation, the importance of different shortest paths *PS* for the same node pair is obtained. The calculation formula is as follows:

$$PS = \frac{GE - GE_{\min}}{GE_{\max} - GE_{\min}} + \frac{MK - MK_{\min}}{MK_{\max} - MK_{\min}} + \frac{MS - MS_{\min}}{MS_{\max} - MS_{\min}}\tag{17}$$

where $G E$ and $M K$ are the values after attacking the shortest path. $M S$ is the importance of intermediate nodes for the shortest path. $G E_{\max }, M K_{\max }$, and $M S_{\max }$ are the maximum values of all shortest paths for the same node pair. $G E_{\min }, M K_{\min }$, and $M S_{\min }$ are the minimum values of all shortest paths for the same node pair.

According to Equation (17), the importance of different shortest paths for the same node pair are calculated and sorted in the same node pair, as shown in Table 4.

Table 4. Importance of different shortest paths in the same group.


# 3.4. Results of the Case Study

According to the above analysis results, the shortest path groups that need to be focused on are as follows:

1. The path_3 $\left(x_{3}, x_{31}\right)$, which is the shortest path group hardest to prevent, i.e., the one with the most paths. There are eight shortest paths, and each path contains the initial node $x_{3}$ (rapid ocean current) and the target node $x_{31}$ (flooding of decks). The intermediate nodes are $x_{9}$ (collision of vessels), $x_{10}$ (collision of debris), $x_{11}$ (collision of cantilever deck), $x_{23}$ (fracture of legs), $x_{24}$ (collision of vessels) and $x_{37}$ (list of the platform).
2. The path_2 $\left(x_{2}, x_{31}\right)$, which is the shortest path group most likely to occur, i.e., the one with the minimum shortest path length. The path length is 2.30 and the initial node $x_{2}$ (huge ocean wave) of this path is directly connected to the target node $x_{31}$ (flooding of decks) without passing through any intermediate nodes.
3. The path_5 $\left(x_{32}, x_{31}\right)$ and path_14 $\left(x_{31}, x_{37}\right)$, which are the shortest path groups hardest to block, i.e., the one with the most edges. There are four shortest paths with five edges: the path_5B, the path_5C, the path_14F and the path_14G. According to the attack effect analysis on different shortest path groups, the attack mode 2 achieves the better effects. In other words, to prevent the occurrence of accidents, it is necessary not only to control the occurrence of risk events (i.e., nodes in the network), but also to block the propagation path between risk events. In addition, due to the limitations imposed by cost, it is impossible to guard against all risk events in the production and operation activities. For the same amount of time and manpower spent, safety investments should be skewed towards risky events that are likely to yield higher safety benefits.

Based on the analysis results of $I, G E$ and $M K$ after attacking different node pairs, the risky events in the following shortest path groups deserve more safety investments: (a) path_3, which consists of eight paths; (b) path_5, which consists of three paths; (c) path_14, which consists of seven paths; (d) path_6, which cconsists of four paths; (e) path_15, which consists of two paths.

In line with the results in Table 4, when some shortest paths are attacked, the connectivity and robustness of the network are greatly reduced. Meanwhile, these paths can also interfere with other shortest paths, indicating that they are critical paths of the entire network. In conclusion, the focus should be on preventing and controlling the following risk events and propagation paths:

1. The path_3E, $x_{3}$ (rapid ocean current) $\rightarrow x_{9}$ (collision of vessels) $\rightarrow x_{23}$ (fracture of legs) $\rightarrow x_{37}$ (list of the platform) $\rightarrow x_{31}$ (flooding of decks).
2. The path_5C, $x_{52}$ (inadequate risk response) $\rightarrow x_{53}$ (inadequate preventive measures) $\rightarrow x_{17}$ (lack of watertight subdivision isolation) $\rightarrow x_{33}$ (flooding of cabins) $\rightarrow x_{37}$ (list of the platform) $\rightarrow x_{31}$ (flooding of decks).
3. The path_14G, $x_{51}$ (inadequate risk perception) $\rightarrow x_{52}$ (inadequate risk response) $\rightarrow$ $x_{53}$ (inadequate preventive measures) $\rightarrow x_{17}$ (lack of watertight subdivision isolation) $\rightarrow x_{33}$ (flooding of cabins) $\rightarrow x_{37}$ (list of the platform).
4. The path_6C, $x_{1}$ (strong ocean storm) $\rightarrow x_{9}$ (collision of vessels) $\rightarrow x_{26}$ (fracture of hulls) $\rightarrow x_{33}$ (flooding of cabins).
5. The path_15B, $x_{52}$ (inadequate risk response) $\rightarrow x_{53}$ (inadequate preventive measures) $\rightarrow x_{17}$ (lack of watertight subdivision isolation) $\rightarrow x_{33}$ (flooding of cabins) $\rightarrow x_{37}$ (list of the platform).
In the above five shortest paths, three paths all contain $x_{52} \rightarrow x_{53} \rightarrow x_{17} \rightarrow x_{33} \rightarrow x_{37}$. It is proved that this shortest path plays an important role in the whole accident evolution network. Therefore, controlling the propagation of this path has great significance for preventing the major storm-disaster-induced accidents in the offshore oil and gas industry.

According to the above analysis results of accident evolution path, different measures are proposed for different stages of accidents. Specific measures are as follows:

1. Preventive measures before accidents: accurate storm forecast and early warning; redundant design of structure and equipment; regular detection of structural defects; fixing movable items on the deck; ensuring the strength of towing ropes; ensuring water-tightness; enhancing risk awareness and strengthening safety training; complete operation regulations and emergency plans; adequate emergency equipment.
2. Control measures in accidents: closing sea valves on the platform; timely drainage of cabin and deck; adjusting ballast conditions of the platform; avoiding excessive oscillation and list of the platform; avoiding hot work; disconnecting from the wellhead; ensuring the normal operation of the power system; ensuring the normal operation of the dynamic positioning system; timely strengthening the support structure; stay out of the storm zone by towing or self-propulsion.
3. Emergency measures after getting out of control: activating the alarm system; emergency muster at the designated location; evacuating platform personnel in sequence; calling for outside help; shutting down unessential electrical equipment; distributing personal survival equipment; lowering lifeboats, life rafts and emergency escape ladders; rescue assist of guard ships.

# 4. Discussion 

Compared with the existing literature, on the one hand, the introduction of GT compensates for the shortcomings of the traditional identification of accident causes, which relies too much on the knowledge and experience levels of personnel. GT is characterized by strong objectivity, which can ensure the accuracy and consistency of classification results of accident cause factors. On the other hand, most of the current methods usually divide the causal factors into large categories first and then determine small categories, which leads to the unstable level and content of classification. According to programmatic GT

in this paper, a total of 63 concepts, 25 categories, nine main categories, and three core categories were obtained in turn. The result shows that this inductive method can solve the problem well.

Meanwhile, the method of DEMATEL-ISM is improved in this paper. In the establishment of the direct influence matrix, the interaction matrix obtained from the objective analysis in the previous step is introduced based on expert rating. As a result, the strong subjectivity associated with the traditional establishment of the matrix can be avoided. The combination of these two methods retains the advantages of objective induction and subjective reasoning, respectively.

At the same time, the analysis results of the first two steps provide input for the construction of the CN model, and the three methods form a step-by-step systematic evaluation method. In addition, a hybrid algorithm named HADY is proposed. In previous studies, when calculating the shortest path of CN model, each node pair usually only gets one path. However, the same node pair may have multiple shortest paths. Using HADY, multiple shortest paths under the same node pair can be calculated effectively. We obtained seven shortest paths on the node pair path 14. This is proved that the algorithm is effective and more in line with the actual situation.

Through the actual case study of the proposed method, the importance of different nodes and paths is calculated, and five key nodes and five critical paths are obtained. They are the node $x_{1}$ (strong ocean storm), the node $x_{9}$ (collision of vessels), the node $x_{31}$ (flooding of decks), the node $x_{37}$ (list of the platform), the node $x_{51}$ (inadequate risk perception), the path_3E $\left(x_{3} \rightarrow x_{9} \rightarrow x_{23} \rightarrow x_{37} \rightarrow x_{31}\right)$, the path_5C $\left(x_{52} \rightarrow x_{53} \rightarrow x_{17} \rightarrow x_{33}\right.$ $\left.\rightarrow x_{37} \rightarrow x_{31}\right)$, the path_14G $\left(x_{51} \rightarrow x_{52} \rightarrow x_{53} \rightarrow x_{17} \rightarrow x_{33} \rightarrow x_{37}\right)$, the path_6C $\left(x_{1} \rightarrow x_{9} \rightarrow\right.$ $\left.x_{26} \rightarrow x_{33}\right)$, and the path_15B $\left(x_{52} \rightarrow x_{53} \rightarrow x_{17} \rightarrow x_{33} \rightarrow x_{37}\right)$. Compared with the research results in the existing literature, the proposed method can not only obtain the importance of nodes, but also obtain the importance of different paths through the method of path attack. The results provide more references for accident prevention.

In general, the proposed method contributes to the precise identification of accident causes and the systematic analysis of accident development. Based on the results of the analysis, reasonable and effective control measures can be implemented to interfere with the development process of accidents. This will slow down or even control the evolution process of accidents under storm disasters to the greatest extent and ensure the safety of offshore oil and gas operations. Further, the application of research results will help reduce casualties caused by major accidents. Meanwhile, it is helpful to achieve sustainable development by reducing the impact of oil and gas accidents on the marine environment.

However, the method proposed in this paper also has its limitations. For example, the method requires detailed data and takes a long time to prepare and code. Moreover, the current CN model of accident evolution cannot realize the dynamic adjustment of nodes and connecting edges. Further research can integrate artificial intelligence in the extraction process of accident causal factors to realize intelligent coding of causal factors for many accident cases. How to embody the dynamic changes of CN models is also one of the important tasks of our future research.

# 5. Conclusions 

This paper presents a method for studying the evolution process of accident causes by combining GT, DEMATEL-ISM, and CN. The integrated method covers different stages, including the identification of accident causes, their qualitative analysis, and quantitative assessment, which can be applied for systematically studying the development process of accidents. The application of the proposed method is illustrated by a case study. The results show that inclement weather and lack of risk awareness are the root causes of accidents. Moreover, the damage of support structures and the loss of water-tightness are key nodes of the accident development. Furthermore, the damage of platform facilities is the inevitable path of accident evolution. The constructed accident evolution network model conforms to the characteristics of small-world network and scale-free network. The overall connectivity

and robustness of the network are high, and it is difficult to reduce the robustness of the network by attacking a single path or node. Results show that there are five key nodes and five critical paths in the process of accident evolution. Through targeted prevention and control of these nodes and paths, the average shortest path length of the accident evolution network is increased by $35.19 \%$, and the maximum global efficiency decreases by $20.12 \%$. Thus, more attention should be focused on the paths with higher importance as identified by the evaluation results of the attack effect under the limitations imposed by cost, time, and manpower.

Author Contributions: Conceptualization, G.Z.; methodology, G.Z. and X.M.; validation, G.Z. and J.Z.; formal analysis, X.L.; resources, G.Z. and J.Z.; data curation, G.C.; writing—original draft preparation, G.Z. and J.Z.; writing—review and editing, G.Z. and G.C.; visualization, J.Z.; supervision, G.C.; project administration, G.C.; funding acquisition, G.C. and X.M. All authors have read and agreed to the published version of the manuscript.
Funding: This work was funded by the Technological Projects of CNPC under Grant (No. ZD2019-184-004), the National Natural Science Foundation of China (No. 52004142), the National Natural Science Foundation of China (No. 52104016) and the Postdoctoral Science Foundation of China (No. 2021M700644).
Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: Not applicable.
Conflicts of Interest: The authors declare no conflict of interest.

# Abbreviations 

GT, Grounded theory; DEMATEL, Decision making trial and evaluation laboratory; ISM, Interpretative structural modelling; CN, Complex networks; RCA, Root cause analysis; FTA, Fault tree analysis; ETA, Event tree analysis; AHP, Analytic hierarchy process; ANP, Analytic network process; SEM, Structural equation modelling; BN, Bayesian network; HADY, Hybrid algorithm of Dijkstra and Yen; GOM, Gulf of Mexico; UKCS, United Kingdom continental shelf; NCS, Norwegian continental shelf; WP, Western Pacific.

## Annotations

$X$-the set of concepts; $Y$-the set of categories; $\boldsymbol{F}$-the direct influence matrix; $\boldsymbol{C}$-the normal matrix; $\boldsymbol{T}$-the comprehensive influence matrix; $\boldsymbol{I}$-the identity matrix; $\boldsymbol{H}$-the overall influence matrix; $\boldsymbol{K}$-the reachable matrix; $\lambda$-the threshold value; $b_{i}$-the influencing degree; $d_{i}$-the influenced degree; $c_{i}$-the centrality; $a_{i}$-the causality; $Q_{i}$-the antecedent set; $P_{i}$-the reachable set; $m_{i}$-the factor degree; $\boldsymbol{S}$-the direct interaction matrix; $\boldsymbol{R}$-the interaction matrix of categories; $\boldsymbol{R} \boldsymbol{X}$-the interaction matrix of concepts; $\boldsymbol{A}$-the adjacency matrix; $G$-the CN graph model; $V$-the set of nodes; $E$-the set of edges; $W$-the set of weights; $k_{i}$-the node degree; $k_{i}^{\text {out }}$-the out-degree; $k_{i}^{\text {in }}$ - the in-degree; $P(k)$-the degree distribution; $C C_{i}$-the clustering coefficient; $C C$-the network clustering coefficient; $B C_{i}$-the betweenness centrality; $B C_{i}^{\prime}$-the normalized betweenness centrality; $I_{i j}$-the shortest path length; $D$-the network diameter; $L$-the average shortest path length; $G E$-the global efficiency; $M K$-the maximum strongly connected component scale; $e w_{i j}$-the entropy weight.

# Appendix A 

Table A1. Statistics of major accidents in the offshore oil and gas industry.


![img-9.jpeg](img-9.jpeg)

Figure A1. Network diagram of shortest paths targets (a) $x_{31}$, (b) $x_{33}$ and (c) $x_{37}$.
