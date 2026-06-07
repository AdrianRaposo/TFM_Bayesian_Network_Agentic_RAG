# Inference of Biological Pathway from Gene Expression Profiles by Time Delay Boolean Networks 

Tung-Hung Chueh ${ }^{1}$, Henry Horng-Shing Lu ${ }^{2 *}$<br>1 Green Energy and Environment Research Laboratories, Industrial Technology Research Institute, Chutung, Hsinchu, Taiwan, Republic of China, 2 Institute of Statistics, National Chiao Tung University, Hsinchu, Taiwan, Republic of China


#### Abstract

One great challenge of genomic research is to efficiently and accurately identify complex gene regulatory networks. The development of high-throughput technologies provides numerous experimental data such as DNA sequences, protein sequence, and RNA expression profiles makes it possible to study interactions and regulations among genes or other substance in an organism. However, it is crucial to make inference of genetic regulatory networks from gene expression profiles and protein interaction data for systems biology. This study will develop a new approach to reconstruct time delay Boolean networks as a tool for exploring biological pathways. In the inference strategy, we will compare all pairs of input genes in those basic relationships by their corresponding $p$-scores for every output gene. Then, we will combine those consistent relationships to reveal the most probable relationship and reconstruct the genetic network. Specifically, we will prove that $O(\log n)$ state transition pairs are sufficient and necessary to reconstruct the time delay Boolean network of $n$ nodes with high accuracy if the number of input genes to each gene is bounded. We also have implemented this method on simulated and empirical yeast gene expression data sets. The test results show that this proposed method is extensible for realistic networks.


Citation: Chueh T-H, Lu HH-S (2012) Inference of Biological Pathway from Gene Expression Profiles by Time Delay Boolean Networks. PLoS ONE 7(8): e42095. doi:10.1371/journal.pone. 0042095
Editor: Frank Emmert-Streib, Queen's University Belfast, United Kingdom
Received February 21, 2012; Accepted July 2, 2012; Published August 31, 2012
Copyright: (C) 2012 Chueh, Lu. This is an open-access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.
Funding: The authors acknowledge support from the National Science Council, National Center for Theoretical Sciences, Shing-Tung Yau Center, and Center of Mathematical Modeling and Scientic Computing at the National Chiao Tung University in Taiwan. The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript.
Competing Interests: The authors have declared that no competing interests exist.

* E-mail: hslu@stat.nctu.edu.tw


## Introduction

In order to understand complex biological networks and pathways, we need to investigate global structures instead of individual behaviors since there are interactions and associations between genes. Due to the invention of high throughput technology, genome-wide expression profiles can be measured simultaneously [1]. However, it is still a great challenge to identify complex biological networks from genome-wide data because the number of gene interactions is huge [2]. In recent years, there has been a significant progress in research concerning genetic network models and network reconstruction problems.

Clustering and dimension reduction are important methods for grouping genes that have similar expression profiles [3,4]. In the framework of clustering, it is important to define the degree of similarity between genes. By the method of clustering, we can group genes that have similar expressions. However, we still cannot find the causal relationship between genes. Hence, apart from the relationship of similarity, we will also have to consider another causal relationship between genes.

There have been many methods proposed in the literature to tackle the problem of genetic regulatory network reconstruction. For instance, the steady state approach have been used to model gene regulatory networks [5]. In addition, the Bayesian network model is an important technique that has been studied extensively in the past two decades [6-11]. A Bayesian network is a directed acyclic graph (DAG) comprised of two components. The first
component is comprised of nodes that correspond to a set of variables and a set of directed edges between variables with Markov properties. The second component describes a conditional distribution for each variable given its parents in the graph. Recently, Bayesian network models have been applied to analyze microarray expression and biological data [12-15]. However, Bayesian network algorithms have limitations when dealing with large-scale gene regulatory networks because of their complex modeling structure [16]. Although algorithms for reconstructing Bayesian networks have already been developed [17,18], the algorithms' computational costs remain a concern for the searching of all potential network structures on the genome-wide expression data.

Therefore, we are considering a simpler model: Boolean networks, which have been studied extensively in a variety of contexts. Boolean networks [19,20] can effectively explain the dynamic behaviors of living systems. Moreover, for large-scale gene regulatory networks, Kim et al. [21] have used Boolean network with chi-square test on the yeast cell cycle microarray gene expression data sets. The chaos and attractors of Boolean network are also discussed widely from the aspect of power spectrum [22-24]. Recently, Boolean network also have been used as a discrete model for the lac operon [25].

Boolean networks were originally introduced by Kauffman, and received attention in the studies of gene regulatory networks because of their simple structures [26]. In a Boolean network

![img-0.jpeg](img-0.jpeg)

Figure 1. Boolean network G(V,F), wiring diagram G(V',F') and its input/output. doi:10.1371/journal.pone.0042095.g001

model, nodes represent the gene expression states. The status of a gene is quantized to one of the two states: on or off, representing a gene as active or inactive respectively. The wiring of rules between nodes in the graph represents a functional link between genes and determines the expressions of target genes after giving a series of input genes. Under the structure of Boolean networks, the target gene is determined by a set of genes with specific rules. For each gene, if the indegree (i.e., the number of input genes to each gene) is bounded by a constant K, only O(log n) pairs of state transition are necessary and sufficient to reconstruct the original network with n nodes [27,28]. However, Boolean networks have been criticized for their deterministic nature. The assumption that every affected gene would be expressed immediately at the next time step may be unsound.

Another point of view of constructing genetic network is to focus on the indication the pairwise relationships between genes. Most of the works is to find the gene-pairs with similarity relationship [29–33]. The similarity of a gene-pair represents the two genes with the same expression or opposite expression. In 2005, Li and Lu proposed directed acyclic Boolean network and the statistical reconstruction method of SPAN to infer the pair wise relations of every element [34]. The proposed method can reconstruct Boolean networks from noisy array data by assigning an s-p-score for every pair of genes. In the study, they proposed another relationship between two genes: relationship of prerequisite under the Boolean network model. If gene A is a prerequisite for gene B, then the "on" status of gene A is necessary for the "on" status of

![img-1.jpeg](img-1.jpeg)


Figure 2. One example of time delay Boolean network and its input/output. doi:10.1371/journal.pone.0042095.g002

gene B. Boolean implication network, with the similar aspect, investigated all Boolean implication between pairs of gene for large scale genome microarray datasets [35]. Following the model, Wang et al.[36] proposed a two step counting approach for constructing biological pathways with Boolean network. However, most of these methods only consider pair wise relationship in order to decrease the time complexity. Therefore, if the structure of network is a combination of a set of genes to affect another gene, the algorithms will lose some information and rules in the genetic network reconstruction.

In this study, we will consider a much more generalized model by combining the structure of the above two models. If a Boolean function with one or several genes is a prerequisite for a target gene, then the induction of the Boolean function with input genes is necessary for the expression of the target gene. Hence, the target will be influenced by the Boolean function with several input genes. However, the induction of the Boolean function may not activate the target gene immediately, but at a future time. Therefore, the target gene may not have been influenced right now and we will treat these relationships as time delay affection. In this study, we will infuse these additional relationships for more generalized systems.

### Boolean Network

Boolean networks were introduced by Kauffman (1969) forty years ago to represent genetic regulatory networks. First, we will review the definition of a Boolean network. A Boolean network G(V,F) is a directed graph consisting of two components: a set of nodes V = {v_{1},v_{2}, . . . ,v_{n}} that corresponds to genes, and a list of Boolean functions F = {f_{1},f_{2}, . . . ,f_{n}} that corresponds to the rule of interaction and combination of several genes. For every node v_{i}∈V, its expression is simplified to two levels: on and off, representing a gene as active or inactive. For every Boolean function f_{i}(v_{i},v_{i1}, . . . ,v_{i}^{i})∈F, k specified input nodes v_{i1},v_{i2}, . . . ,v_{i}^{i} are assigned to the node v_{i} in the graph and represent the rules of regulatory mechanisms between genes. The expression of a gene is determined by the expression of the gene directly affecting it with a Boolean function. Therefore, the state of each node v_{i}∈V is determined by the Boolean function f_{i}(v_{i1},v_{i2}, . . . ,v_{i}^{i}).

For each node v_{i}, the gene expression state at time t is assumed to take either 0 (not-expressed) or 1 (expressed) and is expressed as ψ_{i}(v_{i}). In a Boolean network, every gene expression profile at time t+1 is completely determined by the expression profile of a set of genes v_{i1},v_{i2}, . . . ,v_{i}^{i} at time t and the corresponding Boolean function f_{i}∈F. That is, we can write ψ_{i+1}(v_{i}) = f_{i}(ψ_{i}(v_{i1}),ψ_{i}(v_{i2}), . . . ,ψ_{i}(v_{i}^{i})).

Table 1. Count and probabilities table for $v_{j}, v_{h}$ and $v_{i}^{\prime}$ assuming no misclassification error.


doi:10.1371/journal.pone.0042095.t001

For convenience, we converted the Boolean network $G(V, F)$ to the wiring diagram $G^{\prime}\left(V^{\prime}, F^{\prime}\right)$ (See Figure 1) [37]. For each node $v_{i} \in V$, suppose $v_{i_{1}}, v_{i_{2}}, \ldots, v_{i_{k}}$ are the input nodes assigned to $v_{i}$. Then we construct an additional node $v_{i}^{\prime}$ and connected the edge from $v_{i_{i}}$ to $v_{i^{\prime}}$ for each $1 \leq j \leq k$. That is, the set of $\left{v_{1}, \ldots, v_{n}\right}$ represents the gene expression profile at time $t$ and the set of $\left{v_{1}, \ldots, v_{n}\right}$ corresponds to the gene expression profile at time $t+1$. Hence we can treat the set of $\left{v_{1}, \ldots, v_{n}\right}$ as the input values and the set of $\left{v_{1}^{\prime}, \ldots, v_{n}^{\prime}\right}$ as the corresponding output values. Therefore, the output values of $\left{v_{1}^{\prime}, \ldots, v_{n}^{\prime}\right}$ are determined by $v_{i}^{\prime}=f_{i}\left(v_{i_{1}}, \ldots, v_{i_{k}}\right)$.

## The Structure of Time Delay Boolean Network

In the previous subsection, we found that given the values of the node $(V)$ at time $t$, the expressions at time $t+1$ will be updated immediately by specific Boolean function $(F)$. That is, for every gene $v_{i} \in V$, if the expression profile of a set of genes $\left{v_{i}, v_{i_{1}}, \ldots, v_{i_{k}}\right}$ at time $t$ and the corresponding Boolean function $f_{i}$ is observed, the gene expression of $v_{i}$ at time $t+1$ is determined by $\psi_{t+1}\left(v_{i}\right)=f_{i}\left(\psi_{t}\left(v_{i_{1}}\right), \psi_{t}\left(v_{i_{2}}\right), \ldots, \psi_{t}\left(v_{i_{k}}\right)\right)$. However, in real genetic regulatory situations, the deterministic system has been criticized due to the existence of misclassification error and noise. In addition, some of the gene expression may result in time delay when the gene is influenced by one or several input genes. That is, the induction of Boolean function may not activate the target gene immediately, but in the future. Hence, it would have been much more flexible to use a non-deterministic network system. In this subsection, we will consider two relationships between the Boolean function and the target gene instead of the deterministic relation.

First, we will introduce the structure of time delay Boolean networks. Suppose there are $n$ elements, $v_{1}, v_{2}, \ldots, v_{n}$ in a Boolean network. For any elements $v_{i}$ with specific Boolean function $f_{i}$, we have two kinds of pair wise relationship: prerequisite and similarity. We say that a Boolean function $f_{i}$ with specific $k$ input genes $v_{i_{1}}, v_{i_{2}}, \ldots, v_{i_{k}}$ at time $t$ is the prerequisite for the target gene $v_{i}$ at time $t+1$, if the on-status of Boolean function at time t is necessary for the on-status of gene $v_{i}$ at time $t+1$. This relationship is denoted by $f_{i}\left(\psi_{t}\left(v_{i_{1}}\right), \psi_{t}\left(v_{i_{2}}\right), \ldots, \psi_{t}\left(v_{i_{k}}\right)\right)<\psi_{t+1}\left(v_{i}\right)$. In other words, if the Boolean function $f_{i}$ is not active at time $t$, gene $v_{i}$ will be inactive at time $t+1$. If it does not cause confusion, we will omit the notation of $\psi$ and input genes as denoted by $f_{i}<v_{i}$. Moreover, for every gene $v_{i}$, we use $\bar{v}_{i}$ as its dual (from 0 to 1 , or from 1 to 0 ) in this paper. Therefore, for any Boolean function and target gene with a prerequisite relationship there are a total of two possible relationships: $f_{i}<v_{i}$ and $f_{i}<\bar{v}_{i}$. In this model, we do not consider the situation of a dual of Boolean function prerequisite to the target gene, that is $f_{i}<v_{i}$ and $f_{i}<\bar{v}_{i}$. Since for any Boolean function whose dual is a prerequisite to the target gene, there must exist another Boolean function that is a prerequisite to the target gene. For instance, if $f_{i}\left(v_{1}, v_{2}\right)<v_{3}$, where $f_{i}\left(v_{1}, v_{2}\right)=\left(v_{1}\right.$ and $\left.v_{2}\right)$, then $f_{i}^{\prime}\left(v_{1}, v_{2}\right)<v_{3}$, where $f_{i}^{\prime}\left(v_{1}, v_{2}\right)=\left(\bar{v}_{1}\right.$ or $\left.\bar{v}_{2}\right)$. Therefore, for the prerequisite relationship, we only consider the Boolean function that is a prerequisite to target gene and the dual of target gene.

The other type of relationship between Boolean function and target gene is similarity. We say that the Boolean function $f_{i}$ and

Table 2. Count profiles for the basic eight relationships without misclassification error.


doi:10.1371/journal.pone.0042095.t002

Table 3. Count and probabilities table for $v_{j}, v_{h}$ and $v_{f}$ with misclassification error.


doi:10.1371/journal.pone.0042095.t003 target gene $v_{i}$ are similar if the status of the Boolean function and the status of the target gene are in the same expression, and we denoted this by $f_{i} \sim v_{i}$. In the same way, we do not consider the situation of Boolean function similar to the dual of target gene such as $f_{i} \sim \hat{v}_{i}$ in this study. Since if there is one Boolean function that is similar to the dual of target gene, there must exist another Boolean function that is similar to the target gene.

In the diagram, if a Boolean function $f_{i}$ is a prerequisite to $v_{i}$, we draw a directed arrow from the vertex $f_{i}$ to $v_{i}$ and if $f_{i}$ is similar to $v_{i}$, we use an undirected line to connect $f_{i}$ and $v_{i}$.

In the model of time delay Boolean network we proposed, the output of the gene expression is not completely determined by the input state and Boolean function. The output expression may have more than one possible result in the time delay Boolean network. We illustrate the above construction by an example in Figure 2. It has three elements, one similarity and two prerequisite relationships. The possible outputs for every input state are listed in the right part of the graph. If we knew the network structure, some of the inputs would have more than one possible output expression in the time delay Boolean network.

## Methods

## Identification Algorithm

First, we only consider Boolean networks in which the maximum number of input genes is bounded by a constant $K$ for every target gene, because it has been proven that the number of profiles required grows exponentially if $K$ is not bounded [38]. For simplicity, we only show algorithms for the case of $K=2$. However, the algorithm can be intuitively generalized to any $K$ in a straightforward way. For the inference of genetic network, we need to clarify the following questions for each target gene.

- Which input genes will affect the target gene?
- What kind of Boolean functions will be used for combining those input genes?
- What kind of relationship exists between the Boolean function and the target gene?

In this subsection, we propose an algorithm to clarify the above questions. The algorithm below is conceptually very simple since it simply uses output Boolean functions with input genes and relationships with target genes that are consistent with the data. First, for each output gene expression at time $t+1$ such as $v_{j}$, we consider all the pairs of elements in $V$ at time $t$, for instance $v_{j}$ and $v_{h}$. Then we count the eight incidents of $\left\langle v_{j}, v_{h}, v_{j}^{\prime}\right\rangle$ being $(0,0,0)$, $(0,0,1), \ldots,(1,1,1)$ from the sample and arrange them in a $2 \times 4$ table; see the left part of Table 1. We mark a cell " + " if the count is positive and mark it " 0 " otherwise.

For detecting whether there exists a Boolean function which is a prerequisite to the target gene, we will compare the $2 \times 4$ output table with the left four basic relationships in Table 2. We consider the basic relationships to be consistent with the output table if the position of 0 cell in the basic relationships is also 0 in the output table. By comparing the output table with the four basic relationships, we can find relationships that are consistent with the output tables. If there is more than one relationship that is consistent with the output tables, we would use the Boolean logic gate "and" to combine the Boolean function and transfer the result to another Boolean function. Hence, the final Boolean function is the prerequisite to the target gene. Similarly, by comparing the $2 \times 4$ output table with the right four basic relations in Table 2, we could get another Boolean function which is the prerequisite to the dual of target gene.

Moreover, if only one Boolean function occurred in above relationship, that is, if there is only one Boolean function that is the prerequisite to the target gene or the dual of target gene, we will treat that relationship as our final relationship between the Boolean function and the target gene. However, if both of the two prerequisite relationships happened (i.e. $3 f_{i}$ and $f^{\prime}{ }_{i}$ s.t. $f_{i} \prec v_{i}$ and $f^{\prime}{ }_{i} \prec \hat{v}_{i}$ ), we need to check whether these two relationships are in conflict. If the dual of $f_{i}$ is equivalent to $f^{\prime}{ }_{i}$, our conclusion for inference will be that $f_{i}$ is similar to the target gene (that is, $f_{i} \sim v_{i}^{\prime}$ );

Table 4. Splitting counts caused by misclassification error.


doi:10.1371/journal.pone.0042095.t004

Table 5. The eight basic relationships and their probabilistic hypotheses and $p$-scores.


doi:10.1371/journal.pone.0042095.t005 otherwise, we will treat it as if there is no relationship between the input genes and the target gene because we did not gather enough information to judge true relationships between $\bar{v}_{i}$ and $\left(v_{j}, v_{k}\right)$ at this moment. By the above identification procedure, we can find the corresponding input genes, Boolean function and their relationship for every target gene.

## Identification Algorithm with Noisy Array

In previous subsection, we discussed an identification method for data without noise. In this section we will consider the situation of noisy array data. We assume that every element in the entry of $\left\langle I_{i j}, O_{i j}\right\rangle, j=1,2, \ldots, m$ switches to its reverse status with a misclassification probability $p$ independently; that is

$$
I_{i j}^{*}= \begin{cases}I_{i j} & \text { with probability } 1-p \\ 1-I_{i j} & \text { with probability } p\end{cases}
$$

$$
O_{i j}^{*}= \begin{cases}O_{i j} & \text { with probability } 1-p \\ 1-O_{i j} & \text { with probability } p\end{cases}
$$

Thus, the observed array $\left\langle I_{i j}^{*}, O_{i j}^{*}\right\rangle$ contains misclassification error. Our goal is to reconstruct time delay Boolean network from noisy array of binary data $\left\langle I_{i j}^{*}, O_{i j}^{*}\right\rangle$.

Similar to section 2, we assume that the maximum number of input genes is bounded by 2 for every target gene. We treat the data in the $2 \times 4$ table as a multinomial distribution with eight cells whose probabilities are $q_{000}, q_{001}, \ldots, q_{111}$ as shown in the right part of Table 1, where $q_{000}+q_{001}+\ldots+q_{111}=1$. Similarly, we extract the data with misclassification error for every output gene and each pair of input genes as the $2 \times 4$ table. Now the observed data $n_{000}, n_{001}, \ldots, n_{111}$ are not generated from the multinomial $q_{000}, q_{001}, \ldots, q_{111}$, but from another multinomial $r_{000}, r_{001}, \ldots, r_{111}$ as shown in Table 3, where $r_{000}+r_{001}+\ldots+r_{111}=1$.

Because of the misclassification error, a portion of the samples of $m_{000}$ may change to the other seven cells. We use the notations of $m_{000,000}, m_{000,001}, \ldots, m_{000,111}$ to represent the counts of eight cells changed from $m_{000}$. Analogous notations are defined for $m_{001}, m_{010}, \ldots, m_{111}$. The splitting is shown in Table 4. Consequently, the generated probabilities $\left(q_{000}, q_{001}, \ldots, q_{111}\right)$ are calculated as follows: $q_{i_{1} i_{2} i_{3}, i_{1} i_{2} i_{3}}=p^{I i_{1} j_{3}}(1-p)^{3-I i_{1} j} q_{i_{1} i_{2} i_{3}}$, where $I(i, j)=\sum_{k=1}^{7}\left|i_{k}-j_{k}\right|$. Here, we adopt the notation $q_{i_{1} i_{2} i_{3}, i_{1} i_{2} i_{3}}$ analogous to $m_{i_{1} i_{2} i_{3}, i_{1} i_{2} i_{3}}$. The above parameters and splits are shown in Table 4. In the table, it is easy to find that the correspondence between two sets of counts and probabilities is the following:

$$
\left\{\begin{array}{l}
n_{i_{1} i_{2} i_{3}}=\sum_{i_{1}, i_{2}, i_{3}=0,1} m_{i_{1} i_{2} i_{3}, i_{1} i_{2} i_{3}} \\
r_{i_{1} i_{2} i_{3}}=\sum_{i_{1}, i_{2}, i_{3}=0,1} q_{i_{1} i_{2} i_{3}, i_{1} i_{2} i_{3}}
\end{array}\right.
$$

and

$$
\left\{\begin{array}{l}
m_{i_{1} i_{2} i_{3}}=\sum_{i_{1}, i_{2}, i_{3}=0,1} m_{i_{1} i_{2} i_{3}, i_{1} i_{2} i_{3}} \\
q_{i_{1} i_{2} i_{3}}=\sum_{i_{1}, i_{2}, i_{3}=0,1} q_{i_{1} i_{2} i_{3}, i_{1} i_{2} i_{3}}
\end{array}\right.
$$

For the complete data $\left\{m_{i_{1} i_{2} i_{3}, i_{1} i_{2} i_{3}}\right\}$, the log-likelihood is given by

$$
L=\sum_{i_{1}, i_{2}, i_{3}, i_{1}, i_{2}, i_{3}=0,1} m_{i_{1} i_{2} i_{3}, i_{1} i_{2} i_{3}} \log q_{i_{1} i_{2} i_{3}, i_{1} i_{2} i_{3}}
$$

where $q_{i_{1} i_{2} i_{3}, i_{1} i_{2} i_{3}}$ are those splitting probabilities. Since the complete data $\left\{m_{i_{1} i_{2} i_{3}, i_{1} i_{2} i_{3}}\right\}$ are not observable, we use the EM algorithm to maximize the log-likelihood. In the E-step, the splitting counts of complete data $\left\{m_{i_{1} i_{2} i_{3}, i_{1} i_{2} i_{3}}\right\}$ are evaluated by the conditional expectations using the current values of the parameters by the following formula
$E_{p, q_{000}, q_{001}, \ldots, q_{111}}\left(m_{i_{1} i_{2} i_{3}, i_{1} i_{2} i_{3}}\right) n_{i_{1} i_{2} i_{3}}\right)=\frac{n_{i_{1} i_{2} i_{3}} q_{i_{1} i_{2} i_{3}, i_{1} i_{2} i_{3}}}{\sum_{i^{\prime} 1^{\prime} 2^{\prime} 3}=0,1} q_{i^{\prime} 1^{\prime} 2^{\prime} 3, i_{1} i_{2} i_{3}}}$ (5)
where $i_{1}, i_{2}, i_{3}, j_{1}, j_{2}, j_{3}=0,1$. One probabilities of $q_{000}, q_{001}, \ldots, q_{111}$ are zero in those different hypotheses specified in Table 3. In the M-step, we maximize the conditional expectation of the loglikelihood for the complete data to obtain the maximum likelihood estimates (MLEs) of the parameters. According to the MLEs, we can compute the $p$-score for every pair of input genes and target gene, which are obtained by estimating for the misclassification probability under every prerequisite relationship.

For the first step, we would like to determine the most probable relationships between every pair of input genes and one output gene. Next, we find the most probable Boolean function with pair input genes for every output gene and select candidate pairs of input genes and output gene for the watch list. Finally, we reconstruct a time delay Boolean network by integrating the relationship of those genes selected.

For one output gene $\bar{v}_{i}$ and a pair of input genes $v_{j}$ and $v_{k}$, we define the $p$-scores $p_{\left(v_{i}\right.}$ or $\left.v_{k}\right)<v_{i}$, $p_{\left(v_{i}\right.}$ or $\left.v_{k}\right)<v_{i}$, $p_{\left(v_{i}\right.}$ or $\left.v_{k}\right)<v_{i}$, $p_{\left(v_{i}\right.}$ or $\left.v_{k}\right)<v_{i}$, $p_{\left(v_{i}\right.}$ or $\left.v_{k}\right)<v_{i}$, $p_{\left(v_{i}\right.}$ or $\left.v_{k}\right)<v_{i}$, $p_{\left(v_{i}\right.}$ or $\left.v_{k}\right)<v_{i}$, are, respectively, the maximum likelihood estimates of p under the triangular model: $q_{000}=0, q_{010}=0, q_{100}=0, q_{110}=0, q_{001}=0, q_{011}=0$, $q_{101}=0, q_{111}=0$.

According to the EM algorithm described above, we can evaluate the $p$-score for every output gene. We use the MLE $\hat{p}$ to measure how well each hypothesis fits: the smaller the score is, the more likely that the corresponding hypothesis could be true.

If the samples are generated from a time delay Boolean network, $p$-score are quite useful for the discovery of true

Table 6. By the time delay Boolean network in Figure 1, we generate 100 samples with $\mathrm{p}=0.05$.


doi:10.1371/journal.pone.0042095.t006 relationships. Here we can consider the maximum compatibility criterion: to choose the maximum threshold value so that the selected relationships contain no conflicts [34]. We collect those relationships whose $p$-scores are smaller than a threshold. Known biological results are helpful for the determination of a threshold. For example, if we know the relationship $\left(v_{1}\right.$ or $\left.v_{2}\right)<v_{3}$ is true, then the $p$-scores smaller than $p_{\left(v_{1}\right.}$ or $\left.v_{1}\right)<v_{3}$ should be in our watch list. As more relationships are included in the watch list, the more likely we are to observe incompatible ones. In general, we can choose the threshold that allows the maximum number of relationships with no conflicting relationships. Next we will demonstrate the method by illustration examples.

## Results and Discussion

## Theoretical Results

First, we will analyze the number of input/output pairs required for the network reconstruction of time delay Boolean network to be unique. The theoretical results of classical Boolean networks only consider the similar relationship [27,38,39]. The following results prove the theoretical results time delay Boolean networks that has a more flexible structure and consider both similar and prerequisite relationship.

Proposition 1. For all subsets of $V$ with $2 K$ genes, if all assignments (i.e., $2^{2 K}$ assignments) of Boolean values appear in input expression patterns

![img-2.jpeg](img-2.jpeg)

Figure 3. Network reconstruct from the expression data of yeast Saccharomyces cerevisiae. doi:10.1371/journal.pone.0042095.g003 and all of its possible output expression patterns of the target gene are present, the identification of genetic network is determined to be unique, if it exists. (Proof) Let $z$ be any gene in $V$ and suppose $z$ is controlled by a Boolean function $g\left(x_{i}, \ldots, x_{i_{k}}\right)$ with similarity or prerequisite relationship (i.e., $g \sim z$ or $g<z$ ). If the Boolean function $g$ is similar to $z$, the case is proved for the classical Boolean networks in Akutsu et al. (1998). Next, we consider the case of Boolean function $g$ as a prerequisite to $z$. In this case, there must exist a specific input value $\left{a_{1}, \ldots, a_{k}\right}$ for $\left{x_{i}, \ldots, x_{i_{k}}\right}$ such that $z$ have two possible values 0 and 1 . Hence, any other genes would not control $z$ because all assignments of Boolean values are appearance. Let us illustrate the above statement by the example for the case of $K=1$ and $K=2$. If $K=1$ and $x<z$, when the input of $x$ is 1 , the outcome of $z$ being both 0 and 1 will appearance. Therefore, given the input of $x=1$, the outcome of $z$ is not deterministic no matter the value of any other gene $y$ is 1 or 0 . Hence, any other gene $y$ would not affect gene $z$. If $K=2$ and $g\left(x_{1}, x_{2}\right)<z$ for some Boolean function $g$, there must exist an input $\left(a_{1}, a_{2}\right)$ such that $g\left(a_{1}, a_{2}\right)=1$. Then, for any other pair of gene $\left{y_{1}, y_{2}\right}$ where $\left{y_{1}, y_{2}\right} / \backslash\left{x_{1}, x_{2}\right}=\emptyset$, the outcome of $z$ is not deterministic for any input of $\left{y_{1}, y_{2}\right}$, if the input of $\left{x_{1}, x_{2}\right}$ is $\left{a_{1}, a_{2}\right}$. In a case of $\left{y_{1}, y_{2}\right} / \backslash\left{x_{1}, x_{2}\right} \neq \emptyset$, we can prove that gene $y_{i}$ which does not belong to $\left{x_{1}, x_{2}\right}$ would not affect the gene $z$ in a similar way.

Proposition 2. The probability that one sub-assignment with all of its possible results in the target gene does not appear among $m$ random input expression pattern is at most $2\left(1-\frac{1}{2^{2 K+1}}\right)^{m}$. (Proof) For any fixed set of nodes $\left{v_{i}, v_{i}, \ldots, v_{i \mid K}\right}$, the probability that a sub-assignment $v_{i i}=v_{i i}=\ldots=v_{i \mid K}=1$ does not appear in one random input expression pattern is $1-\frac{1}{2^{2 K}}$. Thus, among the $m$ random input expressions, the probability that $v_{i i}=v_{i i}=\ldots=v_{i \mid K}=1$ appears is $t$ times is equal to $\frac{m!}{t!(m-t)!}\left(\frac{1}{2^{2 K}}\right)^{\prime}\left(1-\frac{1}{2^{2 K}}\right)^{m-t}$, where $t \leq m$. In addition, the probability that all of the possible results in the target gene does not appear among $t$ times input is smaller than $\left(\frac{1}{2}\right)^{t-1}$ for $1 \leq t \leq m$ and equal to 1 for $t=0$. Hence the probability that one sub-assignment and all of its possible results does not appear among $m$ random input expression is smaller than $\left(1-\frac{1}{2^{2 K}}\right)^{m}+\sum_{t=1}^{m} \frac{m!}{t!(m-t)!}\left(\frac{1}{2^{2 K}}\right)^{\prime}\left(1-\frac{1}{2^{2 K}}\right)^{m-t}\left(\frac{1}{2}\right)^{t-1}$, and this can be bounded by $2\left(1-\frac{1}{2^{2 K+1}}\right)^{m}$ by an algebra calculation.

Next we prove the main theorem.
Theorem 1. For the identification of one time delay Boolean network of $n$ nodes with maximum indegree $\leq K, O\left(2^{2 K+1} \cdot(2 K+x) \cdot \log n\right)$ uniformly and randomly sampled input patterns are sufficient for exact inference with probability at least $1-\frac{1}{n^{x}}$.
(Proof) We consider the probability that the condition of Proposition 1 is not satisfied under $m$ random input expression patterns.

By Proposition 2, the probability that $v_{i_{1}}=v_{i_{2}}=\ldots=v_{i_{2 n}}=1$ with all of its possible results in the target gene does not appear among the $m$ random input expression patterns is bounded by $2\left(1-\frac{1}{2^{2 K+1}}\right)^{m}$ for any fixed set of nodes $\left\{v_{i_{1}}, v_{i_{2}}, \ldots, v_{i_{2 K}}\right\}$. Since the number of combinations of $2 K$ nodes from a set of $n$ possibilities is bounded by $2^{2 K} \cdot n^{2 K}$, the probability that the condition of Proposition 1 is not satisfied is at most $2^{2 K} \cdot n^{2 K} \cdot 2\left(1-\frac{1}{2^{2 K+1}}\right)^{m}$. It is not difficult to see that $2^{2 K} \cdot n^{2 K} \cdot 2\left(1-\frac{1}{2^{2 K+1}}\right)^{m}<p$ holds for $m>\ln 2 \cdot 2^{2 K+1} \cdot(2 K+1+$ $\left.2 K \log n+\log \frac{1}{p}\right)$. Hence, we obtain the theorem by letting the non-identification probability $p=\frac{1}{n^{x}}$.

Next we develop an information theoretic lower bound on the number of input/output pairs needed for the identification of a time delay Boolean network.

Theorem 2. If the maximum indegree $\leq K$, at least $\Omega\left(2^{K}+K \log n\right)$ input/output pairs are required for the identification of a time delay Boolean network in the worst case.
(Proof) The number of time delay Boolean networks is given by all the possible combination of Boolean function with $k$ nodes from a set of $n$ possibilities with all possible relations between Boolean functions with target node. Since there are $\Omega\left(n^{K}\right)$ possible combinations of input nodes, $2^{2^{K}}$ possible Boolean functions and 3 possible relations between Boolean function with each node, there are $\Omega\left(\left(2^{2^{K}} \cdot n^{K} \cdot 3\right)^{n}\right)$ Boolean networks whose maximum indegree is at most $K$. On the other hand, there are at most $2^{n}$ possible output patterns with one input expression pattern. Therefore, $\Omega\left(\log _{2^{n}}\left(\left(2^{2^{K}} \cdot n^{K} \cdot 3\right)^{n}\right)\right)$ which is the same as $\Omega\left(2^{K}+K \log n\right)$ input/output pairs are required in the worst case.

## Example with Simulation and Real Data

We will illustrate our method by the example described in Figure 2. For the pair of samples consist of three elements list in the right part of Figure 2, we uniformly generated 100 input samples and their corresponding possible output samples with misclassification probability $p=0.03$. For the prerequisite relationship, if the status of Boolean function with input genes is on, then we allow the output value to have equal probability of on or off. The data can be arranged as input/output sample similar to that obtained from the microarray data with time. Namely, the input of each sample can represent the gene expression at time $t$ and the output can represent the gene expression at time $t+1$. For each pair of input and output genes, we compute the 8 basic $p$ scores that represent the 8 basic hypotheses in Table 5 for all of pair input genes and output genes. After the calculation, the simulation results of every $p$-score are listed in Table 6.

Beside the example with 3 elements, in order to shows the superiority of the proposed method can be applied to a larger network, a more comprehensive example with a larger network is given in Figure S1.

Next, we have to decide the threshold for choosing the relations. When we increase the threshold of the $p$-score, the relations whose $p$-score are smaller than the threshold will be chosen. Moreover, when the number is 0.138 , the conflict occurs, since we have $\left(v_{1}\right.$ or $\left.v_{3}\right)<v_{1}^{\prime}$ and $\left(\bar{v}_{2}\right.$ or $\left.v_{3}\right)<v_{1}^{\prime}$. However, in our model, there are at most two genes that would affect an output gene. Therefore, we can choose 0.138 as our threshold and include relations whose $p$-score is smaller than the threshold. By these procedures, we can reconstruct the time delay Boolean network identical to Figure 2.

In the area of gene regulatory network study, Schuller has summarized regulatory cis-acting elements of structural genes of the nonfermentative metabolism and described the molecular interactions among general regulators and pathway-specific factors [40]. In the gene regulation of gluconeogenesis by $\operatorname{Sip} 4$ and Cat 8 pathway, the carbon source control could be identified for the regulator Cat8; see (Figure 6) in Schuller [40]. In this study, we apply our proposed approach to explore the expression profiles and show some exploratory result on the Cat 8 pathway.

In order to demonstrate the effectiveness of reconstruction, we use the microarray expression dataset of yeast Saccharomyces cerevisiae produced by DeRisi et al. [1] and Spellman et al. [41]. In total, the data is comprised of 41 experiments after filtering out experiments with missing values. By these experimental microarray data sets, we can use our proposed method to reconstruct the biological pathway and the genetic regulation network result is shown in Figure 3. The result is consistent with the genetic network in the literature. That is, the restraint of Mig1 or activation of Snf1 is a prerequisite for the decreasing of Cat8. Moreover, the restraint of Snf1 or Cat8 is a prerequisite for the decreasing of Mls1. However, the negative similarity between Snf1 and Mig1 is undetectable in our current model.

## Conclusions

In this paper, we have introduced the model of time delay Boolean network that generalizes the Boolean network model in order to cope with dependencies that have two kinds of relationships: similarity and prerequisite. The approach for reconstruction of genetic network inference from gene expression data relies on the assumption that the expression of a gene is likely to be controlled by a relatively small number (say $k$ ) of genes. Also, some bounds on the size of data required for the identification of the time delay Boolean networks under constant of indegree are stated and discussed. Moreover, the algorithm of the network reconstruction from noisy array data is developed.

One characteristic of a Boolean network is that all the variables in the graph are binary. If the data we observed is continuous or quantized to have more than two levels, we need to discretize them. For microarray data, the ratios of expression level would be one possible approach of discretization. That is, we can treat the gene as on (active) if the log-ratio of its expression is larger than zero. We treat it as off (inactive) otherwise. In general, biological background knowledge will be helpful for setting thresholds for discretizaion. On the other hand, if the samples are obtained from a time course, then we can consider the gene as on or off by detecting whether the gene is either increasing or decreasing with time.

The work in progress is aimed at evaluating the effectiveness of the described approach for inferring genetic networks from biological gene expression time series data. Besides that, implementation on some other real biological data is also an important task.

For the implement of the network reconstruction algorithm, the greatest complexity is the computation of $p$-score for each of the

$\frac{n!}{k!(n-k)!}$ input elements and $n$ output elements, where $n$ is the number of elements and $k$ is the number of indegree. It is an iterative algorithm to compute the MLE for the $p$-scores by EM procedure while the common practice is to set an upper bound for iterations in numerical implementation. Consequently, this keeps the $O\left(n^{k+1}\right)$ complexity for the computation of MLE. In addition, the sorting algorithm for the $\frac{n!}{k!(n-k)!} n$ data cost $O\left(n^{k+1} \log n\right)$ in terms of time. Hence, the overall time complexity for the network reconstruction is $O\left(n^{k+1} \log n\right)$ for this algorithm.

## Supporting Information

## Figure S1 An example of genetic network with 8 nodes.

(PDF)

## Acknowledgments

We thank the editor and reviewers for their constructive comments.

## Author Contributions

Conceived and designed the experiments: THC HHL. Performed the experiments: THC HHL. Analyzed the data: THC HHL. Contributed reagents/materials/analysis tools: THC HHL. Wrote the paper: THC HHL.
22. Zhang R, de SCavalcante HLD, Gao Z, Gauthier DJ, Socolar JES, et al. (2009) Boolean chaos. Phys Rev E 80: 045202.
23. Socolar JES, Kauffman SA (2003) Scaling in ordered and critical random Boolean networks. Physical Review Letters 90: 68702.
24. Dealy S, Kauffman SA, Socolar JES (2005) Modeling pathways of differentiation in genetic regulatory networks with boolean networks: Research articles. Complex 11: 52-60.
25. Veliz-Cuba A, Stigler B (2011) Boolean models can explain bistability in the lac operon. Journal of Computational Biology 18: 783-794.
26. Kauffman SA (1969) Metabolic stability and epigenesis in randomly constructed genetic nets. Journal of Theoretical Biology 22: 437-467.
27. Akutsu T, Miyano S (1999) Identification of genetic networks from a small number of gene expression patterns under the boolean network model. Proc Pacific Symposium on Biocomputing : 17-28.
28. Meher T, Thoreson V, Karp R (2000) Discovery of regulatory interactions through perturbation: inference and experimental design. Proc Pacific Symposium on Biocomputing : 302-313.
29. Allocco DJ, Kohane IS, Butte AJ (2004) Quantifying the relationship between co-expression, coregulation and gene function. BMC Bioinformatics 5: 18.
30. Boal WJ (2007) Systems biology by the rules: hybrid intelligent systems for pathway modeling and discovery. BMC Systems Biology 1: 13.
31. Jordan IK, Marino-Ramirez L, Wolf VI, Koonin EV (2004) Conservation and coevolution in the scale-free human gene coexpression network. Molecular Biology and Evolution 21: 2058-2070.
32. Lee HK, Hsu AK, Sajdak J, Qin J, Parfidis P (2004) Coexpression analysis of human genes across many microarray data sets. Genome Research 14: 10851094.
33. Opgru-Rhein R, Strimmer K (2007) From correlation to causation networks: a simple approximate learning algorithm and its application to high-dimensional plant gene expression data. BMC Systems Biology 1: 37.
34. Li LH, Lu HH-S (2005) Explore biological pathways from noisy array data by directed acyclic boolean networks. Journal of Computational Biology 12: 170185 .
35. Sahoo D, Dill D, Gendex A, Tibshirani R, Plevritis S (2008) Boolean implication networks derived from large scale, whole genome microarray datasets. Genome Biology 9: R157.
36. Wang H, Lu HH-S, Chueh TH (2011) Constructing biological pathway by a two-step counting approach. Plos one 6: e20074.
37. Somogyi R, Sniegoski CA (1996) Modeling the complexity of genetic networks: Understanding multigene and pleiotropic regulation. Complexity 1: 45-63.
38. Akutsu T, Kuhara S, Maruyama O, Miyano S (1998) Identification of gene regulatory networks by strategic gene disruptions and gene overexpression. Proc 9th ACM-SIAM Symp Discern: Algorithms: 695-702.
39. Akutsu T, Kuhara S, Maruyama O, Miyano S (2003) Identification of genetic networks by strategic gene disruptions and gene overexpressions under a boolean model. Theoretical Computer Science 298: 235-251.
40. Schuller HJ (2003) Transcriptional control of nonfermentative metabolism in the yeast saccharomyces cerevisiae. Current Genetics 43: 139-160.
41. Spellman PT, Sherlock G, Zhang MQ, Iyer VR, Anders K, et al. (1998) Comprehensive identification of cell cycle-regulated genes of the yeast saccharomyces cerevisiae by microarray hybridization. Molecular Biology of Cell 9: 3273-3297.