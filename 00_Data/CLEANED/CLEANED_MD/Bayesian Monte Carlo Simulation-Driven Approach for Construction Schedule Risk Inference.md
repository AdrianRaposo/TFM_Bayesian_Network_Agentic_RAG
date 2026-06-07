This item was submitted to Loughborough's Research Repository by the author.
Items in Figshare are protected by copyright, with all rights reserved, unless otherwise indicated.

# Bayesian Monte Carlo simulation-driven approach for construction schedule risk inference 

PLEASE CITE THE PUBLISHED VERSION
https://doi.org/10.1061/(asce)me.1943-5479.0000884
PUBLISHER
American Society of Civil Engineers (ASCE)
VERSION
AM (Accepted Manuscript)
PUBLISHER STATEMENT
This material may be downloaded for personal use only. Any other use requires prior permission of the American Society of Civil Engineers. This material may be found at https://doi.org/10.1061/(asce)me.19435479.0000884.

## LICENCE

All Rights Reserved

## REPOSITORY RECORD

Chen, Long, Qiuchen Lu, Shuai Li, Wenjing He, and Jian Yang. 2020. "Bayesian Monte Carlo Simulationdriven Approach for Construction Schedule Risk Inference". Loughborough University. https://hdl.handle.net/2134/14317466.v1.

# Bayesian Monte Carlo Simulation Driven Approach for Construction 

## Schedule Risk Inference

Long CHEN ${ }^{1}$, Ph.D. A.M.ASCE; Qiuchen LU ${ }^{2 *}$, Ph.D. A.M.ASCE; Shuai LI ${ }^{3}$, Ph.D.; Wenjing $\mathrm{HE}^{4}$; Jian YANG ${ }^{5}$, Ph.D.
${ }^{1}$ Lecturer, School of Architecture Building and Civil Engineering, Loughborough University, Loughborough LE11 3TU, UK. Email: 1.chen3@1boro.ac.uk
${ }^{2}$ Lecturer, The Bartlett School of Construction and Project Management, University College London, London WC1E 6BT, UK. Email: qiuchen.lu@ucl.ac.uk
${ }^{3}$ Assistant Professor, Department of Civil and Environmental Engineering, University of Tennessee, Knoxville, TN 37996, USA. Email: sli48@utk.edu
${ }^{4}$ Master student, School of Naval Architecture, Ocean and Civil Engineering, Shanghai Jiao Tong University, Shanghai, 200240, China. Email: qzclwenj@sjtu.edu.cn
${ }^{5}$ Professor, School of Naval Architecture, Ocean and Civil Engineering, Shanghai Jiao Tong University, Shanghai, 200240, China. Email: j.yang.1@sjtu.edu.cn

## ABSTRACT

As the construction of infrastructures becomes increasingly complex, it has been often challenged by construction delay with enormous losses. The delivery of complex infrastructures provides rich source of data for new opportunities to understand and address schedule issues. Based on these data, many efforts have been made to identify key construction schedule risks and predict the probability of risk occurrence. Bayesian network is one of the most useful tools for risk inference. However, there are still two obstacles preventing the Bayesian network from being adopted popularly in construction schedule risk management: (1) the development of directed acyclic graph (DAG) and associated conditional probability tables (CPTs); (2) the lack of observation data to trigger risk inference as evidence at the planning stage. This research aims to develop a novel Bayesian Monte Carlo simulation driven approach for construction schedule risk inference of infrastructures, where the Bayesian network model can be developed in a more convenient way and be used without observation data required. It firstly constructs the key risk network with key risks and links through network theory-based analysis. Then the DAG structure of Bayesian network is developed based on the topological structure of key risk network using deep-first search (DFS) and adapted maximum-weight spanning tree (A-MWST) algorithms. The CPTs are further developed using the leaky-MAX model. Finally, the Bayesian Monte Carlo simulation driven risk inference method is developed for predicting and quantifying the probability of construction schedule risk occurrence. A real

[^0]
[^0]:    * Corresponding Author, Qiuchen Lu, Email: qiuchen.lu@ucl.ac.uk

infrastructure project is selected as case study to verify this developed approach. The results show that the developed approach is more appropriate to deal with risk inference of infrastructures considering its reliability, convenience, and flexibility. This research contributes a new way to construction schedule risk management and provides a novel approach for quantifying and predicting risk occurrence probability.

Keywords: Construction schedule risks; Network theory-based analysis; Bayesian Monte Carlo simulation

# 1. Introduction 

The construction industry, especially the infrastructure sector, has been rapidly developing in the past decades, where the average annual growth of global built-up areas is $28 \%$ between 1990 and 2015 (UN-Habitat, 2016). The construction of infrastructures has attracted many attentions due to the extreme complexity, high risks and long lead time (Fiori and Kovaka, 2005), multiple stakeholders involved (Mok et al., 2017; Valentin et al., 2018), and considerable impacts to the society, economy and natural environment (Zhai et al., 2009). It is thus significant to manage infrastructure projects properly not only for the project itself but for the region concerned (Wang and Yuan, 2016).

As a major objective of infrastructure management, the schedule has been regarded as a vital parameter of the planning and construction of projects (Al-Momani, 2000; Liu et al., 2014). However, the construction schedule delay of infrastructures is not rare but a 'business as usual' with enormous losses and damages to project delivery (Flyvbjerg et al., 2004, 2005). For example, Al-Momani (2000) found that $81.5 \%$ of 130 public complex construction projects involved in Jordan had suffered time delay. Ellis and Thomas (2002) found that $55 \%$ of highway projects in the US had experienced an average time delay of $44 \%$ in excess of the original time specified in the contract. The construction schedule and risk management should be improved to help the delivery of infrastructures within time and budget.

Such complex infrastructures are becoming rich sources of data from multidisciplinary models and systems, raising new opportunities to understand and address schedule issues (Whyte et al., 2016; Chen and Whyte, 2020). Based on these data, many efforts have been made to manage the construction schedule and associated risks of infrastructures. Building information modelling (BIM) has been adopted as a powerful management tool for schedule planning (Liu et al., 2015; Tallgren et al., 2020), control (Moon et al., 2015) and risk management (Sami Ur Rehman et al., 2020). Based on that, extended reality (XR) has been further proposed to assist schedule control (Alizadehsalehi et al., 2020; Fu and Liu, 2018). However, such technologies

only focused on pre-defined schedules and risks while ignored the risk impacts on construction schedule. Other methods more focusing on the risk impacts have been also proposed, such as line of balance (LOB), critical path method (CPM), program evaluation and review technique (PERT) and correlated schedule risk analysis model (CSRAM) (Ökmen and Öztaş, 2008). However, they only focused on the diversity of risks or effect of risk on the schedule while ignored the complexity of correlations between risks and uncertainty of risk occurrence, where risk impacts that appear to be minor lead to rippled disruption to the project delivery (Abotaleb and El-adaway, 2018). Bayesian network has been proposed as a useful tool to handle complexity and uncertainty and been adopted in the construction schedule risk management of infrastructures (Nasir et al., 2003; Luu et al., 2009; Khodakarami et al., 2007). It provides a reliable approach to (1) modelling complex risk correlations by cause-effect relationships, and (2) modelling uncertainty of risk occurrence by conditional probability. However, given the richer data, there are still two obstacles preventing the popular adoption of Bayesian network in the practice of construction schedule risk management: (1) it is often impossible in practice to define and use a unified classification code for risk identification and data template for Bayesian network development, especially for the development of directed acyclic graph (DAG) and associated conditional probability tables (CPTs); (2) the observation data is often required as evidence to trigger risk inference which is inapplicable at the project planning stage.

This paper aims to solve these problems through developing a novel Bayesian Monte Carlo simulation driven approach for construction schedule risk inference of infrastructures. This developed approach enables Bayesian network to be developed in a more convenient way and be used without observation data required in practice. It starts with a review of construction schedule risks identified in the past research and theoretical basis of network theory and Bayesian network in construction schedule risk analysis. Then the methodology is explained in terms of strategies of case study and focus group discussions for case data collection. The construction of key risk network is demonstrated using network theory-based analysis, followed by the development of Bayesian network model through DFS and A-MWST algorithms and leaky-MAX model. Finally, the Bayesian Monte Carlo simulation driven risk inference approach is developed for predicting and quantifying the probability of construction schedule risk occurrence. A real underground railway project is selected as case study to verify the developed approach. The results are discussed in terms of reliability, convenience and flexibility, followed by conclusions.

# 2.1 Construction schedule risks of infrastructure project 

As the beginning of the risk management, risk identification is a process through which a series of potential risks are identified according to their frequency of occurrence and possible influence, either positively or negatively, on principal project objectives (Perrenoud et al., 2015). Many efforts have been made to identify risks or causes for the construction delay in infrastructures (Table 1). For instance, Lo et al. (2006) investigated the 30 significant factors from seven categories, and further provided corresponding risk mitigation measures in Hong Kong. 'Inadequate resources due to contractor/lack of running capital', 'Unforeseen ground conditions', and 'Exceptionally low bids' have been identified as the three most significant causes for delay in civil engineering projects in Hong Kong. Sambasivan and Soon (2007) also explored the construction delay factors and associated impact on the schedule of large construction project in Malaysia through questionnaire survey and identified 10 most important causes for delay (e.g., contactor's improper planning, poor site management, and inadequate contractor experience.

Some research has been further conducted to reveal insights of construction delay of specific infrastructure project. Han et al. (2009) analysed the construction schedule delay of Korea Train Express (KTX) project in South Korea, and identified five major delay causes for KTX project, including 'Lack of owner's abilities and strategies to manage hi-tech oriented mega project', 'Frequent changes of routes', 'Inappropriate project delivery system', 'Lack of proper scheduling tool' and 'Redesign and change orders of main structures and tunnels'. The time overruns of six FIFA World Cup stadia in South Africa have been investigated by Baloyi and Bekker (2011), examining 11 main factors causing the construction schedule delay. These identified risks in previous research provide a list of potential construction schedule risks for infrastructures both in practice and in this research.
[Insert: Table 1 Schedule risks for the construction delay of infrastructure project identified in previous research]

### 2.2 Network theory in risk analysis

Network theory is a view of regarding the dependent elements as the complex network with multiple correlations between them, which is concerned with the 'structure and patterning' of these correlations and seeks to identify both their causes and effects (Yang and Zou, 2014). Evolving from the network theory, the network theory-based analysis can provide an effective way to identify the correlations between system elements and analyse the features and implications of these relational fabrics by integrating mathematical and computational

applications (Mok et al., 2017; Dogan et al., 2013). Within the network structure, elements (nodes) of a system are joined by multiple correlations (links) in various manners. The network theory-based analysis accentuates network and relational measures rather than the individual attributes of each element on account of the conception that: (1) the existence of an element can yield effects on or be affected by the presence of other interrelated elements within the system; and (2) the correlations between system elements can the system's strength and behaviours (Fang et al., 2012; Mok et al., 2017).

The network theory-based analysis has been initially applied in the sociometry, and then adopted in construction management. Fang and Marle (2012) developed a simulation-based risk network model for decision support in project risk management (PRM), which defined risks as nodes and correlated influences as links. Furthermore, Fang et al. (2012) analysed the risk network in a large engineering project to distinguish key risks and correlations affecting the project objectives. Yang and Zou (2014) investigated stakeholder-associated risks and their relationships in green building projects to facilitate risk management. Mok et al. (2017) studied stakeholders concerns and intricate interdependencies between them for identifying key challenges in major public engineering projects (MEPs).

Although previous research has showed the viability of network theory-based analysis in analysing the complexity of correlations between risks, it cannot deal with the uncertainty of risk occurrence.

# 2.3 Bayesian network in risk analysis 

The Bayesian Network provides a probabilistic approach to determine the likelihood of occurrence of certain variable conditions (i.e., conditional probability) and can model the uncertainty of risk occurrence (Nasir et al., 2003; Wang and Zhang, 2018). It firstly introduced in the 1970s (McCabe et al., 1998), is a graphical representation of conditional dependence among a group of variables. A Bayesian network model usually consists of two parts: (1) a directed acyclic graph (DAG), which represents the network structure, and (2) an associated set of conditional probability tables (CPTs), which is the network parameter and represents the conditional probability distribution among the variables (Hu et al., 2013). Specifically, the nodes represent variables of the domain, while the arcs represent dependence relationships between the nodes (McCabe et al., 1998). The network is thus constructed by a series of nodes where the nodes are connected by the arcs according to the reasoning direction of decision makers (Kjaerulff, 2008). Based on the Bayes' theorem (Equation (1)), the relationship between each pair of connected nodes is expressed in the form of probability distribution that

encapsulates the decision makers' experience (Kjaerulff, 2008). Therefore, for a Bayesian network model, $B=(V, E)$, where $V$ denotes a set of nodes (i.e., variables), and $E$ denotes a set of directed links between pairs of the nodes, a joint probability distribution that can be factorized as:

$$
\begin{gathered}
P(B / A)=\frac{P(A / B) P(B)}{P(A)} \\
P(V)=P\left(X_{1}, X_{2}, \cdots X_{i}, \cdots, X_{n}\right)=\prod_{X_{i} \in V} P\left(X_{i} \mid X_{p a\left(X_{i}\right)}\right)
\end{gathered}
$$

where $X_{p a\left(X_{i}\right)}$ is the set of parent nodes for $X_{i}, X_{p a\left(X_{i}\right)} \in V$. Each conditional probability distribution for $i$ th variable, $P\left(X_{i} \mid X_{p a\left(X_{i}\right)}\right)$, consists of a series of conditional probability $p_{i}$ :

$$
p_{i}=P\left(x_{i} \mid x_{p a\left(X_{i}\right)}\right), i=1,2, \cdots, l
$$

where $x_{i}$ and $x_{p a\left(X_{i}\right)}$ are the values assigned to $X_{i}$ and $X_{p a\left(X_{i}\right)}$ respectively, and $p_{i}$ is the probability of $X_{i}=x_{i}$ given the condition $X_{p a\left(X_{i}\right)}=x_{p a\left(X_{i}\right)}$.

The Bayesian network has been adopted in addressing the complex problems under uncertainty in the real world, such as fault diagnosis (Lin et al., 2018), ecosystem assessment (Liu et al., 2014), decision support (Xie and Thomas, 2013), and of course risk analysis of infrastructures. Specifically, many Bayesian network-based studies have been conducted to evaluate the construction schedule risks for infrastructures. For example, Luu et al. (2009) applied the Bayesian network to quality the construction schedule risks and the probability of construction project delays in Vietnam. Nasir et al. (2003) developed an Evaluating Risk in ConstructionSchedule Model (ERIC-S) through integrating the PERT technique and Bayesian network model, which could be adopted to determine the lower and upper activity duration values for schedule risk analysis of infrastructure projects. Furthermore, Khodakarami et al. (2007) mapped the CPM to Bayesian networks to provide the prediction for the construction schedule under uncertainty.

Through applying Bayesian network, the complexity of risk correlations and uncertainty of risk occurrence can be modelled properly in construction schedule risk analysis of infrastructures. However, the development and application of Bayesian network is not easy which usually require large amount of data and time for (1) DAG and CPTs development; and (2) risk inference. Unfortunately, there are usually limited time and data provided for Bayesian network development and application in practice, preventing the popular implementation of Bayesian network in the risk analysis of infrastructures. It is time to develop a novel approach for

# 3. Research Methodology 

The novel approach has been developed and validated in this four-stage research for construction schedule risk inference through integrating network theory-based analysis and Bayesian Monte Carlo simulation (Figure 1).

The network theory-based analysis is firstly conducted to identify key risks (nodes) and correlations (links) and construct the key risk network for construction schedule. The topological structure of key risk network is similar to that of DAG in Bayesian network model, where the nodes represent risks and links represent the cause-effect relationships. The development of DAG in Bayesian network model can then be developed based on the constructed key risk network using DFS and A-MWST algorithms. The CPTs of Bayesian network model can be further worked out using the leaky-MAX model. Based on the developed Bayesian network model, the Bayesian Monte Carlo simulation is conducted for generating reliable probability of each possible state of risk occurrence (i.e., 'Better than expected', 'Expected' or 'Worse than expected'). Finally, the case study is conducted according to a real underground project for approach validation.
[Insert: Figure 1 Overall flowchart for research]
In this research, the main structure for tunnelling of underground railway project in Greater Bay of China was chosen for case study with the considerations: (1) the project is representative for its type (transportation), complexity, importance and size, (2) the data was accessible to conduct this research, (3) construction schedule delay has already happened or is highly possible to occur in the construction process, and (4) researchers have built a good relationship with the project team, which helped secure the access to the project for further study. Two focus group discussions have been organized with five senior members from the project management team. Although ideally all stakeholders should participate in discussion to achieve a consensus, it is more efficient in practice to have only senior members from the project management team involved to provide enough information (Yang and Zou, 2014). All participants in focus group discussions were selected based on the idea of 'Applicability', in which participants should have rich knowledge and something to say on the discussion topic, have similar sociocharacteristics, and be comfortable talking to each other. The data generated based on the synergy of group interactions could thus be applied to the development of hybrid approach.

# 3.1 1st round focus group discussion 

The $1^{\text {st }}$ round focus group discussion was designed for developing key risk network of case project. It lasted for around 2 hours and mainly focused on two aspects: (1) the identification and verification of construction schedule risks within the context of case project; (2) the identification and assessment of links among schedule risks within the context of case project. Before the 1st round focus group discussion, a brief introduction about network theory-based analysis has been presented to the participants, and a list of potential construction schedule risks from literature review (Table 1) has also been provided to participants as a reference to break their cognitive limitations.

The post-discussion log and notes were kept well, which recorded the information related to the double-check of whether the recording is functioning properly, the researcher's reflections and elaborations about the focus group discussion, and the learning from the discussions. The post-discussion notes coupled with the main data collected from the discussion notes ensure the quality and reliability of the data for analysis.

## $3.22^{\text {nd }}$ round focus group discussion

The $2^{\text {nd }}$ round focus group discussion was designed for developing Bayesian network model according to the case project, which also involved the same five senior members participating in the $1^{\text {st }}$ round focus group discussion. It lasted for around 2 hours and mainly focused on two topics: (1) verification and examination of developed DAG structure of Bayesian network model; and (2) development of CPTs of Bayesian network model. The post-discussion log and notes were also kept well with those from the $1^{\text {st }}$ round focus group discussion.

## 4. Development of Key Risk Network

### 4.1 Identification of the network boundary

As the foundation of developing key risk network, the boundary (i.e., specific risks) should be identified and examined at first.

The classical experience-based method is one of the most popular methods for risk identification. It includes only core stakeholders to perform the risk identification process, which is conducted based on a stakeholder's or a small group of stakeholders' experiences on 'what are the risk categories' and 'what are the risks' by interviews, surveys or focus group discussions. It is convenient and highly efficient to provide insights into risks according to the rich experience of core stakeholders, but it is difficult for the core stakeholders to break the cognitive limitations and draw the whole set of boundaries (Chen, 2019; Yang and Zou, 2014).

In this research, the classical experience-based method was adopted to identify risks for constructing risk network through the $1^{\text {st }}$ round focus group discussion. Before this focus group discussion, a list of potential construction schedule risks from literature review (Table 1) was also provided to participants as a reference to help them break their cognitive limitations and draw comprehensive boundaries.

# 4.2 Establishment and assessment of links 

After defining the risk network boundary, the links between risks in this research are considered between each pair of risks (Fang et al, 2012). The risk structure matrix (RSM) method is commonly adopted to analyse risk links, which was also adopted in this research.

The RSM (i.e., adjacency matrix) is defined as a square matrix with entry $R S M_{i j}=S_{i j}=$ $I_{i j} \times P_{i j}$ when there is a relationship from $i$ th risk, $R_{i}$, to $j$ th risk, $R_{j}$, otherwise, $R S M_{i j}=$ Null, where $S_{i j}$ is the strength of link, $I_{i j}$ is the intensity of impact from this one risk to the other paired, and $P_{i j}$ is the likeliness of this impact to happen (Mok et al., 2017; Yang and Zou, 2014). The five-point Likert scales are adopted to measure $I_{i j}$ (from $1=$ 'No impact' to $5=$ 'Extraordinarily significant impact') and $P_{i j}$ (from $1=$ 'Never happen' to $5=$ 'Always happen').

In order to moderate the confusion and divergence of links establishment and assessment, the $1^{\text {st }}$ round focus group discussion was held to develop the RSM with quantitative assessment (Yang and Zou, 2014). The outcomes can identify and quantify the links between risks.

### 4.3 Visualisation of network

Once the nodes and links have been identified and assessed, a construction schedule risk network for the target infrastructure project can be developed and mapped as a graph $G(N, K)$, where the identified risks are mapped as $N$ nodes connected by $K$ weighted arrows.

In this research, the NetMiner 4 was used to visualise the risk network for its high competence in the processing and exploratory analysis of huge networks (Furht, 2010). In the network graph $G(N, K)$ presented, nodes represent the risks where different shapes and colours of them indicate different risk categories and sub-categories respectively. The arrows are the links between risks, of which the thicknesses indicate the strength of links.

### 4.4 Topological analysis of risk network

With risk network mapped as $G(N, K)$, the structural configuration is explored and explained by the metrics of topological analysis (Table 2).

This analysis consists of three levels. Firstly, through the network-level analysis, the network density and cohesion are calculated out to unravel the network structure quantitatively. The value of density indicates how closely the risks are situated in a network, and the value of cohesion implies the complicated of network configuration in terms of node reachability. Then the node-level analysis is further conducted to determine the key risks through examining the direct and/or propagating impacts of nodes, as well as their functions and properties in the influence network. Five node-level metrics were calculated and analysed in this research, namely, degree difference, ego network size, node betweenness centrality, out-status centrality, and total brokerage (Table 2). Finally, the link-level analysis is conducted to measure the extent that a risk link plays a gatekeeper role in governing the influences passing through it based on betweenness centrality (Chen, 2019; Yang and Zou, 2014). A greater centrality value implies a more critical link.
[Insert: Table 2 Definition of metrics for topological analysis]

# 4.5 Interpretation of the results 

Based on the results of analysis at three levels, the key risks and key risk links can be identified. The key risks are distinguished from the risk network with high values in one or more of nodal metrics, including degree difference $\left(D_{d}\right)$, ego network size $(E)$, betweenness centrality $(B)$, out-status centrality $(S)$, and brokerage. Meanwhile, the key risk links are identified with high values in betweenness centrality at the link-level.

The key risk network thus consists of (1) key risks, (2) key risk links, (3) non-key risks involved in key risk links, and (4) non-key risk links involving key risks. This developed key risk network provides essential information of construction schedule risks for infrastructures but with more concise and manageable structure (Chen, 2019).

## 5. Development of Bayesian Network

### 5.1 The construction of DAG structure

The construction of DAG can provide a network structure for Bayesian network model, where two kinds of methods have been commonly adopted, namely the expert knowledge driven structure construction method (Hu et al., 2013; Luu et al., 2009), and the observational data driven structure learning method (Lee et al., 2009). However, the structure learning method is not appropriate to be applied in the field of infrastructures due to (1) the uniqueness and uncertainty of construction schedule risks for infrastructures; and (2) the data provided for training process. Although the structure construction method conforming to the verified

causalities is more suitable for risk analysis of infrastructures, it can be time-consuming for construction process and inevitably introduce subjective bias from experts (Hu et al., 2013).

Due to limited time and data, it is reasonable to use the key risk network from network theorybased analysis as basis to generate the DAG structure considering that the topological structure of key risk network is similar to that of DAG in Bayesian network model, where the nodes represent risks and links represent the cause-effect relationships. This novel approach integrating the network theory and Bayesian network is not only more convenient and resourcesaving but also reliable for incorporating both expert knowledge and analysis metrics (Table 2).

In order to transform the network from directed cyclic graph (DCG) to DAG properly, it is the key to find the directed cycles in network and eliminate these cycles without essential information loss, where the directed cycles are formed through 'starting at any vertex $v$ and following a consistently-directed sequence of edges that eventually loops back to $v$ again'. In this research, there are two steps developed to construct DAG from key risk network, including (1) searching cycles by DFS algorithm, and (2) constructing DAG by A-MWST algorithm.

# 5.1.1 Searching cycles by DFS algorithm 

The DFS algorithm is adopted as the searching strategy on account of its convenience and rapidity to traverse or search the tree or graph data structures as far as possible (Cormen et al., 2001). The pseudocode of recursive DFS algorithm is as follows (Goodrich and Tamassia, 2006):

```
1 DFS \((G, v)\)
2 label \(v\) as discovered
3 for all edges from \(v\) to \(w\) in \(G . a d j a c e n t E d g e s(v)\) do
4 if vertex \(w\) is not labeled as discovered then
5 recursively call DFS \((G, w)\)
```

Based on recursive DFS algorithm, the process of applying DFS algorithm in searching cycles within the key risk network is developed as follows: (1) Define the key risk network as the graph $G$ with vertices $v,(G, v)$, and define weight $==B\left(R_{i} \rightarrow R_{j}\right)$; (2) Select an unvisited node $v$ with $D_{i n}(v)=0$ as the root node; define $[v]==0,[w]==0$, label $v$ as 'visited', and begin the searching procedure; (3) Check whether G.adjacentEdges $(v)==$ $\}$ or not, and if the answer is yes, then go to step 6; otherwise, go to step 4; (4) For all the available edges (i.e., links) in G.adjacentEdges $(v)$, select the edge with the maximum

weight $e$ which directs to the vertex $w$; define $[w]==[w]+1$, G.adjacentEdges $(v)==$ G.adjacentEdges $(w) \backslash\{e\} ;(5)$ Define $[v]==[w]$, and check whether the $w$ (or $v$ ) has been labelled or not; if the answer is yes, then go to the step 6 ; otherwise, label $w$ as 'visited' and go to the step 3; (6) Define $[v]==[v]-1$; check whether $[v]==0$ (i.e., the root node), if the answer is no, go to step 3 ; otherwise, further check whether all the nodes have been visited or not, if the answer is no, go to step 2, otherwise, stop the searching procedure; (7) Transform the key risk network $(G, v)$ into spanning tree through integrating the visited nodes and traversed edges (Cormen et al., 2001).

There are usually four types of edges (i.e., links) in the spanning tree (Cormen et al., 2001): (1) the tree edges which belong to the spanning tree itself, (2) the forward edges which point from a node of the tree to one of its nonadjacent descendants, (3) the back edges which point from a node to one of its ancestors, and (4) the cross edges which do neither. The cycle must be existed if the back edge is existed, through which the cycles can be identified in the risk network.

# 5.1.2 Constructing DAG by A-MWST algorithm 

With the cycles identified, the spanning tree transformed from key risk network need to be redeveloped to construct DAG structure through eliminating the identified cycles without essential information loss.

The MWST algorithm can highly reserve the structure properties and provide the associated probability distribution closest to the probability distribution of the original network, as measured by the Kullback-Leibler divergence (KLD) (Pearl, 1988). Based on the MWST algorithm, the A-MWST algorithm has been developed in this research to re-developed DAG model from spanning tree:

```
A-MWST DAG \((G, v)\)
    \(S:=\{ \}\)
    Loop \(:=\{ \}\)
    for each vertex \(v\) in \(G\)
        do \(v \rightarrow S\)
    \(\operatorname{sort}(G . E d g e s(v \rightarrow w), B(v \rightarrow w)^{\prime} \operatorname{descend}^{\prime})\)
    for each edge from \(v\) to \(w\) in \(G . E d g e s(v \rightarrow w)\)
            do \(S:=S \cup\{(v \rightarrow w)\}\)
            if Loop \(:=\{ \}\)
                then \(S:=S\)
                else \(S:=S \backslash\{(v \rightarrow w)\}\)
            recursively call \(G . E d g e s(v \rightarrow w)\)
```

In this A-MWST algorithm, the betweenness centrality of link, $B\left(R_{i} \rightarrow R_{j}\right)$, is a reliable metric for mutual information $I\left(R_{i} \rightarrow R_{j}\right)$ of corresponding edge and has been defined as the

weight of corresponding edge. The process of applying A-MWST algorithm to constructing DAG based on spanning tree is designed as follows: (1) starting from the empty tree over all variables (i.e., nodes); (2) inserting the largest-weight edge (i.e., link); (3) finding the next largest-weight edge and adding it to the tree if no cycle is formed; otherwise, discarding the edge and repeating this step; and (4) repeating the third step until all edges have been selected and an associated DAG is finally constructed whose weight has the maximum value of $\sum_{(v \rightarrow w), v, w e G} B(v \rightarrow w)$.

# 5.2 The development of CPTs 

The development of CPTs is another obstacle preventing the adoption of Bayesian network in the practice of construction schedule risk management with limited time and data, whose complexity increases exponentially with the number of parent nodes and possible values (or states) of nodes (Xie and Thomas, 2013; Zagorecki and Druzdzel, 2013). For example, in a multi-valued Bayesian network with $m$ possible values, there can be $m^{n+1}$ conditional probabilities in the CPT for a node with $n$ parent nodes. Apart from the huge amounts of time and data it requires to assess all the probabilities for CPTs, it can also be problematic to what extent experts can be expected to coherently provide the probabilities at the level of detail required (Wisse et al., 2008).

In order to relieve the elicitation task for developing the CPTs, there are two kinds of ways commonly adopted (Wisse et al., 2008). The first one is to provide an easier way for experts to deliver CPTs. For instance, Van Der Gaag et al. (1999) transcribed the CPTs using the scale of both numerical and verbal anchors. However, the efforts to deliver the full CPTs though reduced is still exponential in the number of variables. The second way to reduce these efforts is to reduce the number of probabilistic assessments to be made, for example, reducing the number of variables (e.g., Luu et al., 2009) or limiting the number of possible values (or states) (e.g., Xie and Thomas, 2013). However, such a way will lead to the unavoidable loss of information (Wisse et al., 2008).

Considering both the efforts reduction and information reservation, the canonical probabilistic model was adopted in this research for reducing the number of probabilities to be specified through delivering approximate probabilities (Xie and Thomas, 2013; Wisse et al., 2008). One of the most widely used technique among canonical probabilistic models is the noisy-MAX model introduced by Diez (1993), the generalization applied in addressing multi-valued variables of the noisy-OR model. In this noisy-MAX model, the CPT is derived from the 'marginal conditional' probability distributions specified for each parent using the max

function (Diez, 1993). The noisy-MAX model just requires a small number of parameters to specify the entire CPTs, which is linear in the number of conditioning variables rather than exponential (Wisse et al., 2008). It significantly reduces the efforts in knowledge elicitation from experts (Wisse et al., 2008), improves the quality of distributions learned from data (Oniśko et al., 2001), and reduces the special and temporal complexity of algorithms for Bayesian networks (Diez and Galán, 2003).

However, in practice, it is neither feasible nor desirable to model all variables influencing a certain node $Y$ (Diez and Druzdzel, 2006). According to Diez and Druzdzel (2006), in this case, assuming that there is a large Bayesian network that properly represents the real-world domain defined over a set of variables $V^{R}$, the reduced model exploited can be defined as $V\left(V \subset V^{R}\right)$, and the rest of the variables, $V_{I}=V^{R} \backslash V$, are not explicit in the model where the index $I$ means 'implicit' (Figure 2(a)). The leaky model only models the explicit variables to provide useful information for constructing CPTs with reduced efforts.
[Insert: Figure 2 The example of leaky model: (a) The relationship among the real-world domain $V^{R}$, reduced model $V$, and implicit model $V_{I}$; (b) The internal structure of a leaky

ICI model, where variable $Z_{L}$ summarises the effect of $V_{I}$ ]
Before applying the leaky-MAX model, there are two assumptions (i.e., assumption of independence of causal influence (ICI)) for all cause-effect relationships involved: (1) each parent node $X_{i}$ has a probability $p_{i}$ of being sufficient to produce an impact $Z_{i}$ on the child node $Y$ in the absence of all other causes; and (2) the ability of each cause being sufficient is independent of the presence of the other causes (Figure 2(b)). Then the CPT, $P(y \mid X)$, of leakyMAX model can be obtained through (Diez and Druzdzel, 2006):

$$
\begin{gathered}
P(Y \leq y \mid X)=\sum_{z \mid f_{M A X}(Z) \leq y} \prod_{i \mid X_{i} \in X} P\left(z_{i} \mid x_{i}\right) \sum_{z_{l} \mid f_{M A X}\left(z, z_{L}\right) \leq y} P\left(z_{L}\right)= \\
\prod_{i}\left(\sum_{z_{l} \leq y} c_{z_{l}}^{x_{i}}\right)\left(\sum_{z_{L} \leq y} c_{z_{L}}^{1}\right) \\
C_{y}^{L}=\sum_{z_{L} \leq y} c_{z_{L}}^{L} \\
C_{y}^{x_{i}}=\sum_{z_{i} \leq y} c_{z_{i}}^{x_{i}} \\
P(Y \leq y \mid X)=C_{y}^{L} \cdot \prod_{i} C_{y}^{x_{i}} \\
P(y \mid X)=\left\{\begin{array}{c}
P(Y \leq y \mid X)-P(Y \leq y-1 \mid X), y \neq y_{\min } \\
P(Y \leq y \mid X), y=y_{\min }
\end{array}\right.
\end{gathered}
$$

where $z_{i}$ are the explicit causes and $z_{L}$ are the inexplicit causes.

Although the leaky-MAX model is applied under the ICI assumptions, it is good enough to provide the approximation of the CPTs compared with the reduction of efforts (Wisse et al., 2008; Diez and Druzdzel, 2006). Zagorecki and Druzdzel (2006) fitted the noisy-MAX model (i.e., the specification of leaky-MAX model) to existing CPTs of three Bayesian networks and found that the model can provide a good fit for as many as $50 \%$ of CPTs, which is powerful enough in practice.

In this research, the leaky-MAX model was thus applied to develop the CPTs $P(y \mid X)$ under the ICI assumptions for reasonable simplification. The identified key construction schedule risks are taken as the variables in Bayesian network model, while three possible states are assigned to each variable, i.e., 'State 1: Better than expected (B)' defining that the condition is better than expected when risk happens, 'State 2: Expected (E)' defining that the condition is exactly as expected when risk happens, and 'State 3: Worse than expected (W)' defining that the condition is better than expected when risk happens. Ordinal comparison among these states can be defined by the influence degree of each state on construction schedule. Assuming that the 'Expected' state has already considered a certain influence degree of each risk on construction schedule, the states are ordinal according to the influence degree, where ' $\mathrm{B}<\mathrm{E}<$ W'.

# 6. Monte Carlo Simulation Driven Risk Inference 

The general problem of computing probabilities of interest from a joint probability distribution is probabilistic inference. With Bayesian network model developed, it provides the basis to predict the probability of risk occurrence where the probabilistic inference can be executed dynamically with two facts (Neil et al., 2005): (1) the effects of observations entered into one or more nodes can be propagated throughout the Bayesian network, in any direction, and the marginal distributions of all nodes are updated; and (2) only relevant inferences can be made in the Bayesian network; The Bayesian network uses conditional dependency structure and current knowledge base to determine those inferences that are valid. According to these two facts, the Junction Tree (JT) algorithm has been developed and commonly adopted in the exact inference of multiply connected networks. Details of JT algorithm can be found in the work of Lauritzen and Spiegelhalter (1988).

In order to start this risk inference process with JT algorithm, the Monte Carlo simulation (MCS) is adopted for simulating the occurrence of risk as evidence according to the updated 'risk sate probability boundary'. This 'risk sate probability boundary' can demonstrate the probability of occurrence of different risk states (i.e., state 1,2 and 3 ), which is also the marginal probability

of each risk state.

The random number within the scale $[0,1]$ is firstly generated by MCS based on uniform probability distribution, which is the index of determining the state of target risk. The equal chance of getting any stochastic value between 0 and 1 can model the real system more realistically and accurately (Ökmen and Öztaş, 2008).

$$
\begin{gathered}
r_{i} \sim U[0,1] \\
R_{i}=\left\{\begin{array}{c}
B, r_{i} \in\left[0, P_{i B}\right] \\
\left\{E, r_{i} \in\left(P_{i B}, P_{i B}+P_{i E}\right]\right. \\
\left.W, r_{i} \in\left(P_{i B}+P_{i E}, 1\right]\right.
\end{array}\right.
\end{gathered}
$$

where the $r_{i}$ is the random number generated to determine the state of $i$ th risk; $P_{i B}, P_{i E}$ and $P_{i W}$ are the risk state probability boundaries of $i$ th risk.

In this Bayesian Monte Carlo simulation process, states of risks are simulated in a chain to introduce evidence in risk inference (Figure 3). This chain is defined according to the time sequence, where the priority of simulation will be given to the risks being predecessors or risks will be simulated simultaneously if no predecessor existed. It is reasonable to define this simulation sequence according to the time, which have mirrored the sequence of risk occurrence in practice. For instance, in Figure 3, risks 2 and 4 occurred at the time $t_{1}$ are simulated firstly according to equation (9-10). After determining the risk state of these risks, JT algorithm is adopted to propagate the probability along the Bayesian network and update all other risks (i.e., Bayesian process in Figure 3). Then the simulation of risks occurred at the time $t_{2}$ (e.g., risk 3 in Figure 3) are followed given the evidence of risk states of risks 2 and 4. The JT algorithm is adopted again for probability propagation. The simulation and propagation processes are repeated until the states of all risks are determined, where one iteration of the Bayesian Monte Carlo simulation process is completed. Multiple iterations are usually needed to provide reliable results for risk inference of infrastructure construction schedule. It is usually sufficient to have $1,000-3,000$ iterations for providing reliable results with affordable computational cost (Diaz and Hadipriono, 1993). This research thus had 3,000 iterations and selected the same seed value for generating the same specific sequence of random numbers in every experiment, which makes the simulation become reproducible, and is useful for comparing the results derived from different conditions.
[Insert: Figure 3 Example of one iteration of Bayesian Monte Carlo simulation process]

# 7. Case Study 

### 7.1 Case background

The main structure for tunnelling of an underground railway project in Greater Bay of China was selected for case study. This railway project was designed as part of a comprehensive transportation hub in this area, while this research focused on the construction of central ventilating shaft of the metro project, which is also the starting point of tunnel boring. It is an underground three-span two-story structure, whose length is 130.0 m from YDK46+010.8212 to $Y D K 46+140.8212$, width is 31.8 m , and depth is 20.0 m . The main construction area of it is $8262 \mathrm{~m}^{2}$ and affiliated construction area is $797.86 \mathrm{~m}^{2}$.

This project began on $1^{\text {st }}$ November 2017 and was expected to be completed before $20^{\text {th }}$ June 2018. As part of the transportation hub, the construction schedule should be under control to avoid the occurrence of construction delay. It is thus necessary for this project to conduct the construction schedule risk inference in advance. In the past projects, the project management team mainly relied on experience to manage construction schedule risks, which can identify and classify key risks but cannot quantify probabilities of such risks. The developed approach is needed by the project management team for quantitative risk inference.

### 7.2 Case data collection

Two rounds of focus group discussions have been held in August 2017 and October 2017 separately to collect data for analysis.

In the $1^{\text {st }}$ focus group discussion, the construction schedule risks were firstly provided and verified by five participants from the project management team using the classical experiencebased method. Totally 32 construction schedule risks have been identified as the network boundary of risk network (Table 3). The links between risks were then identified and assessed according to the expert experience and opinions using the RSM method. Totally 262 links between risks have been identified, which constructed the risk network $G(32,262)$ together with 32 risks. The link strength was also provided for each identified link (Table 4).
[Insert: Table 3 Construction schedule risks of case project]
[Insert: Table 4 Example of RSM with link strength of case project]
In the $2^{\text {nd }}$ round focus group discussion held after the construction of DAG structure, the DAG structure was verified and canonical parameters for all risks involved in the DAG were collected to develop CPTs (Table 5 and 6).

[Insert: Table 6 Canonical parameters for Tw-R1]

# 7.3 Results and analysis 

Based on the data collected, the construction schedule risk network can be constructed and visualised as $G(32,262)$ shown in Figure 4(a), where 32 risk (nodes) in different categories (shapes) and sub-categories (colours) were connected by 262 links (arrows). In order to construct the key risk network, the topological analysis has been conducted based on the metrics defined in Table 2.

Based on the results of topological analysis at node-level, it was observed that the top three risks with high values of nodal metrics $\left(D_{d}, E, B, S\right.$ and total brokerage) were highly overlapped and consistent. Totally 7 key risks have thus been identified (Table 7). Meanwhile, according to the results of link-level topological analysis, it was observed that a sharp decline was occurred at 10 in the L-shape curve of link betweenness centrality, where $B\left(R_{i} \rightarrow R_{j}\right)=$ 10 was set as the cut-off point to distinguish key risk links. Totally 20 key risk links have been selected for their values of betweenness centrality $(B)$ were higher than 10 (Table 7).

In order to construct the key risk network with a simple structure but retaining most of essential information, besides key risks and links, other components involving key risks or involved in key risk links are also necessary to be included in the key risk network, where 14 non-key risks involved in the key risk links and 19 non-key risk links between key risks have thus been counted in (Table 7). As shown in Figure 4(b), the key risk network of case project has been constructed as $G(21,39)$, which consisted of 21 risks (nodes) including 7 key risks and 14 non-key risks and 39 links (arrows) including 20 key risk links and 19 non-key risk links.
[Insert: Figure 4 (a) Construction schedule risk network of case project, $G(32,262)$; (b)
Key construction schedule risk network of case project, $G(21,39)$ ]
[Insert: Table 7 Components of key risk network]
After developing the key risk network $G(21,39)$, DFS algorithm was firstly adopted to search for the cycles if existed in the network through transforming the network into a spanning tree. It was observed that five back edges (i.e., links) were existed in the network, including TwR2 $\rightarrow$ S7R4, Tw-R1 $\rightarrow$ Tw-R2, Tw-R1 $\rightarrow$ S7R4, S1R6 $\rightarrow$ S0R2, and S7R4 $\rightarrow$ S1R5, indicating that there were cycles existed in the spanning tree. In order to further transform the cycled spanning tree into DAG structure, the A-MWST algorithm was then applied to eliminating these cycles

and constructing the DAG structure. According to A-MWST algorithm, four risk links have been eliminated from $G(21,39)$ due to their low weights (i.e., the betweenness centrality of link), including Tw-R1 $\rightarrow$ Tw-R2, S1R5 $\rightarrow$ S7R4, S1R6 $\rightarrow$ S0R2, and S7R4 $\rightarrow$ Tw-R2. Finally, the DAG structure $G(21,35)$ consisting of 21 risks and 35 risk links has been developed (Figure 5), which however has no cycle existed compared to the key risk network $G(21,39)$.
[Insert: Figure 5 DAG structure of case project, $G(21,35)]$
Following the development of DAG structure, the leaky-MAX model was further adopted to generate the CPTs based on the determined canonical parameters (Table 5 and 6) under the ICI assumptions. According to the equations (4-8), the CPTs for risks of the case project can be figured out conveniently (Table 8).
[Insert: Table 8 Part of CPTs for Tw-R1]
Finally, the MCS-driven risk inference can be conducted to identify key construction schedule risks and predict the probability of risk occurrence. Based on the construction process (time sequence), the simulation sequence was determined as 'S1R3, S4R5, S4R6, S9R3 $\rightarrow$ S4R4, S1R2 $\rightarrow$ S0R2, S1R6 $\rightarrow$ Tw-R2 $\rightarrow$ Tw-R1 $\rightarrow$ Sp-R4, S6R1, S6R2, S7R4 $\rightarrow$ S1R5, S7R3 $\rightarrow$ S3R1, S7R2 $\rightarrow$ Tr-R3 $\rightarrow$ S4R8, S2R1'. After 3,000 iterations of the simulation, the results provided a good estimation of risk occurrence of case project, quantifying the probability of three states for each risk (Figure 6).

According to the simulated probability of 'State 3: Worse than expected', these 21 risks of case project can be classified into three categories, including high-risky, medium-risky and lowrisky, which require different risk management strategies from the project management team. The high-risky ones represent the nine risks with probability of state 3 higher than $50 \%$ (i.e., $50 \% \leq P_{w} \leq 100 \%$ ) (e.g., Figure 6a-6c), including S7R3 (89.6\%), S7R4 (86.9\%), S7R2 (84.1\%), Tw-R1 (76.7\%), Tw-R2 (72.8\%), Sp-R4 (69.6\%), S1R6 (66.7\%), S4R4 (50.0\%), S6R2 (50.7\%). The management team should focus on these risks to avoid risk occurrence and prepare plans for mitigating the risk impact if happens. The medium-risky ones represent the eight risks with $20 \% \leq P_{w}<50 \%$ (e.g., Figure 6d-6f), including S6R1 (49.1\%), S0R2 (44.2\%), S3R1 (43.4\%), Tr-R3 (37.6\%), S2R1 (36.4\%), S1R5 (35.2\%), S1R2 (27.9\%) and S4R6 (20.2\%), where the team need to pay attention to these risks after the high-risky ones and also prepare plans for risk mitigation. The low-risky ones represent the four risks with $0 \leq$ $P_{w}<20 \%$ (e.g., Figure 6g-6i), including S9R3 (0\%) and S4R8 (9.3\%), S1R3 (13.1\%) and S4R5 (19.4\%) where it is not necessary for the team to pay much attention to them but have

596 Based on the results, the risk management and mitigation for these 21 risks were prioritised for decision-makers to draw a risk management benchmark with four different levels (from 0 to 3) and resources input accordingly. Specifically, the level- 0 indicates that no risk happens, and the construction progresses as expected. The level- 1 indicates that one or more low-risky risks' states are 'Worse than expected', but the construction schedule is just impacted slightly. The level-2 indicate that one or more medium-risky risks' states are 'Worse than expected', and the construction schedule is impacted moderately. The level-3 indicate that one or more high-risky risks' states are 'Worse than expected', and the construction schedule is impacted seriously. This benchmark can help decision-makers understand the risk interdependencies and dynamic nature of risk propagation, and avoid rippled disruption of project construction and delivery.

To verify the results, these probabilities of risks were back to the project team for further discussion, where the five experts participating the focus group discussion before were invited to review the probability of each risk and assess how appropriate these probabilities are based on their rich experience on similar projects. Each expert was asked the same question "How appropriate are these probabilities to be used to predict risk states?" Through using the fivepoint Likert scale (from 1 = "Not appropriate at all" to 5 = "Very appropriate"), the results showed that all the probabilities (of state 1,2 and 3 ) have been scored over 3 averagely, indicating that the simulation results were believed to be appropriate to be used to predict the risk states and occurrence of this case project.
[Insert: Figure 6 Examples for probability of occurrence of risk states $\left(P_{B}, P_{E}, P_{w}\right)$ : (a) S7R2, (b) Sp-R4, (c) Tw-R2, (d) S1R5, (e) S6R1, (f) S3R1, (g) S1R3, (h) S4R8, (i) S9R3.]

# 8. Discussion 

This research contributes to the construction schedule risk inference of infrastructures through developing a state-of-the-art solution, hybrid approach, based on Bayesian Monte Carlo simulation. It outperforms other construction schedule risk analysis methods in its reliability, convenience and flexibility to deal with the complex construction schedule risks.

Firstly, this approach provides more insights into the diversity and interdependency of construction schedule risks, generating more reliable results of risk identification and risk inference. The diversity of and interdependencies between construction schedule risks have been considered as main reasons for complexity of infrastructures (Fang et al., 2012; Chu et al., 2003). It would be necessary and useful to address this complexity for providing reliable

prediction of risk occurrence (Raz and Michael, 2001). Compared with previous construction risk analysis methods, such as correlated schedule risk analysis model (CSRAM) (Ökmen and Öztaş, 2008) and system dynamics approach (Wang and Yuan, 2016), this approach steps further to not only identify risk interdependencies but also clarify how these interdependencies impact the risk inference. Through network theory-based analysis and algorithms (DFS and AMWST), this approach can identify diverse risks and interdependencies which are transformed into DAG structure with essential information preserved. Through Bayesian Monte Carlo simulation, the identified interdependencies are adopted to propagate the impact among risks for risk inference.

Secondly, the developed approach is more convenient in data acquisition and processing for risk inference. Although the data of infrastructure construction is becoming richer recently, it is often impossible in practice to define and use a unified classification code for risk identification and data template for Bayesian network development and training (Lee et al., 2009). The expert knowledge driven structure construction method for Bayesian network development is however time-consuming and will inevitably introduce subjective bias ( Hu et al., 2013; Luu et al., 2009). For example, Nasir et al. (2003) used to adopt pre-screening, testing and semi-supervised survey to save time in Bayesian network development but they still claimed that the risk relationship identification and quantification (i.e., DAG and CPTs development) were difficult and even impractical, which took 6 weeks with 69 risks. This approach can fully leverage a small dataset for network theory-based analysis and deal with the exponential growth of the number of parameters in CPTs using leaky-MAX model. It only took totally 4 hours to collect and process data for Bayesian network development. With the network theory-based analysis and proposed algorithms (i.e., DFS and A-MWST), only the strength of link $S_{i j}$ is required to generate the key risk network and further the DAG structure. With the leaky-MAX model, only $(m n \cdot m)$ canonical parameters are needed to generate reliable CPTs rather than $\left(m^{n} \cdot m\right)$ conditional probabilities for a node in multi-valued Bayesian network with $m$ possible values and $n$ parent nodes, significantly reducing the data requirement and computational complexity.

Finally, the Bayesian Monte Carlo simulation method provides more flexibility for construction schedule risk inference of infrastructures in practice. At the project planning stage, the risk inference of construction schedule has been often conducted using observations to provide the predicted probability of risk occurrence in a one-shot way. For example, Khodakarami et al. (2007) developed a Bayesian network solution based on CPM to predict the construction schedule under uncertainty and conducted the scenario analysis for probability of resources

level based on hypothetic observations. Nasir et al. (2003) and Luu et al. (2009) both developed a Bayesian network model for quantifying the probability of risk occurrence given the CPTs and hypothetic observations. Compared to previous research, the simulated data are introduced as soft evidence in this research to trigger risk inference at the project planning stage, which enables variables to be simulated individually or simultaneously according to CPTs rather than hypotheses if the observation data are not available. This developed approach is however compatible with the observation data and other datasets (e.g., real-time sensor/visual data informing the risk states) when they are available to trigger risk inference and update the risk network in near real-time. Moreover, by adopting the same seed value, the simulation process can be reproducible and useful for comparing the results derived from different conditions.

# 9. Conclusions 

The construction of complex infrastructures has provided rich data for construction schedule risk management which however has still been challenged by construction delay with enormous losses. This research developed a novel Bayesian Monte Carlo simulation driven approach to predict and quantify the probability of construction schedule risk occurrence. The developed approach efficiently addresses two problems through fully leveraging the dataset from construction schedule risks: (1) the lack of data template for Bayesian network development in practice, and (2) the lack of observation data for triggering risk inference in project planning. It addressed the first problem through developing a data transformation approach based on DFS and A-MWST algorithms and leaky-MAX model and converting a risk network into Bayesian network. It then resolved the second problem by designing a Bayesian Monte Carlo simulation driven risk inference method. The developed approach has been validated by a case study, where the results enabled the project team to prepare look-ahead risk mitigation strategies.

This research makes theoretical contributions to the body of knowledge through analysing the diversity and interdependency of construction schedule risks from a network perspective (i.e., network theory and Bayesian network). This network-oriented approach handles construction schedule risks of complex projects (e.g., infrastructures) in a system engineering approach to avoid rippled disruption of project delivery (Whyte, 2016). The new view and rethinking to manage such risks of complex projects provide deeper insights into the complexity and uncertainty of construction of infrastructures. The practical contributions of this research mainly include: (1) a novel approach developed to construct Bayesian network and conduct Bayesian Monte Carlo simulation for construction schedule risk inference. Compared to

traditional methods, it can outperform in reliability of results, convenience of data acquisition and processing and flexibility in practice; and (2) the findings from case study. The constructed key risk network $G(21,39)$ can help decision-makers to identify construction schedule risks and understand risk propagation of infrastructures. The prediction of probabilities of risk occurrence can further help decision-makers prioritise the construction schedule risks and make a risk management benchmark. These findings however are not limited to the case project but can be applied to other similar projects. They can also assist researchers and practitioners in understanding the practicability of this hybrid approach.

There are also some limitations needed to be addressed in the future research. Firstly, the data transformation approach is semi-automatic which requires many efforts to transform key risk network to DAG structure. Secondly, this research only considers the states of risks in time sequence while ignores the dynamic nature of risk states in the longitude. Thirdly, more case studies and more objective assessment methods are needed to validate this developed approach. Future research should be conducted to address these limitations through: (1) developing an automatic approach and system to integrate network theory-based analysis and Bayesian network; (2) developing a dynamic Bayesian network based approach for analysing risk dynamics in the longitude; (3) conducting more case studies of infrastructures both in China and overseas to validate and further improve this developed approach; and (4) integrating the probabilities of risk occurrence with impacts on construction schedule to predict the construction schedule under uncertainty and also to verify this developed approach quantitatively.

# Data Availability Statement 

All data (network theory-based analysis, canonical parameters and CPTs) and codes (Bayesian Monte Carlo simulation) that support the findings of this study are available from the corresponding author upon reasonable request.
