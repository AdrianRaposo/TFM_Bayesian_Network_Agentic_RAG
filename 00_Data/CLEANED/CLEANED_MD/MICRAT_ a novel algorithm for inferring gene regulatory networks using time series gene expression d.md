# MICRAT: a novel algorithm for inferring gene regulatory networks using time series gene expression data 

Bei Yang ${ }^{1,2 *}$, Yaohui Xu ${ }^{1}$, Andrew Maxwell ${ }^{3}$, Wonryull Koh ${ }^{3}$, Ping Gong ${ }^{4}$ and Chaoyang Zhang ${ }^{3 *}$


#### Abstract

Background: Reconstruction of gene regulatory networks (GRNs), also known as reverse engineering of GRNs, aims to infer the potential regulation relationships between genes. With the development of biotechnology, such as gene chip microarray and RNA-sequencing, the high-throughput data generated provide us with more opportunities to infer the gene-gene interaction relationships using gene expression data and hence understand the underlying mechanism of biological processes. Gene regulatory networks are known to exhibit a multiplicity of interaction mechanisms which include functional and non-functional, and linear and non-linear relationships. Meanwhile, the regulatory interactions between genes and gene products are not spontaneous since various processes involved in producing fully functional and measurable concentrations of transcriptional factors/proteins lead to a delay in gene regulation. Many different approaches for reconstructing GRNs have been proposed, but the existing GRN inference approaches such as probabilistic Boolean networks and dynamic Bayesian networks have various limitations and relatively low accuracy. Inferring GRNs from time series microarray data or RNAsequencing data remains a very challenging inverse problem due to its nonlinearity, high dimensionality, sparse and noisy data, and significant computational cost, which motivates us to develop more effective inference methods.


Results: We developed a novel algorithm, MICRAT (Maximal Information coefficient with Conditional Relative Average entropy and Time-series mutual information), for inferring GRNs from time series gene expression data. Maximal information coefficient (MIC) is an effective measure of dependence for two-variable relationships. It captures a wide range of associations, both functional and non-functional, and thus has good performance on measuring the dependence between two genes. Our approach mainly includes two procedures. Firstly, it employs maximal information coefficient for constructing an undirected graph to represent the underlying relationships between genes. Secondly, it directs the edges in the undirected graph for inferring regulators and their targets. In this procedure, the conditional relative average entropies of each pair of nodes (or genes) are employed to indicate the directions of edges. Since the time delay might exist in the expression of regulators and target genes, time series mutual information is combined to cooperatively direct the edges for inferring the potential regulators and their targets. We evaluated the performance of MICRAT by applying it to synthetic datasets as well as real gene expression data and compare with other GRN inference methods. We inferred five 10-gene and five 100-gene networks from the DREAM4 challenge that were generated using the gene expression simulator GeneNetWeaver (GNW). MICRAT was also used to reconstruct GRNs on real gene expression data including part of the DNA-damaged response pathway (SOS DNA repair network) and experimental dataset in E. Coli. The results showed that MICRAT significantly improved the inference accuracy, compared to other inference methods, such as TDBN, etc.
(Continued on next page)

[^0]
[^0]:    * Correspondence: iebyang@zzu.edu.cn; chaoyang.zhang@usm.edu
    ${ }^{1}$ School of Information \& Engineering, Zhengzhou University, Zhengzhou 450000, China
    ${ }^{2}$ School of Computing, University of Southern Mississippi, Hattiesburg, MS 39406, USA
    Full list of author information is available at the end of the article

## Conclusion

In this work, a novel algorithm, MICRAT, for inferring GRNs from time series gene expression data was proposed by taking into account dependence and time delay of expressions of a regulator and its target genes. This approach employed maximal information coefficients for reconstructing an undirected graph to represent the underlying relationships between genes. The edges were directed by combining conditional relative average entropy with time course mutual information of pairs of genes. The proposed algorithm was evaluated on the benchmark GRNs provided by the DREAM4 challenge and part of the real SOS DNA repair network in E. Coli. The experimental study showed that our approach was comparable to other methods on 10-gene datasets and outperformed other methods on 100-gene datasets in GRN inference from time series datasets.

Keywords: Gene regulatory networks, Maximal information coefficient, Conditional relative average entropy, Time-series mutual information

## Background

Reconstruction of gene regulatory networks (GRNs), also known as reverse engineering [1] of GRNs, aims to infer the potential relationship between genes using gene expression data. Sometimes the expression of a gene is affected by others (named as its regulators) and meanwhile regulates its downstream target genes. Reconstruction of gene regulatory networks can help people understand the mechanism of gene interactions in the cell and reveal the mystery of life. The discovering of the regulation relationship between genes was initially achieved by biological experiments [2]. However, this approach was costly and progressed slowly in research, thus becoming a bottleneck that restricted the development of biological systems. With the development of biotechnology, such as gene chip microarray, the high-throughput data generated provides us with more opportunities to understand the potential regulatory relationships of genes. In recent years, developing machine learning and data mining algorithms and applying them to reconstruction of gene regulatory networks has become an active research topic in bioinformatics.

Different computational methods have been proposed to tackle the gene regulatory networks identification problems. The typical methods include regression models [3, 4], Bayesian networks [5-10], state space models [11-14] and information theory models [15-20], etc.

Several existing methods formulate gene regulatory networks as regression problems which are based on the assumption that all regulatory interactions are linear, meaning that the gene expression level of a target gene is a combination of the expression levels of its transcriptional factors. However, biological networks are known to exhibit multiple regulation mechanisms including non-linear interactions.

The Bayesian network model employed the joint probability distribution of gene expression data to construct a directed acyclic graph to represent the relationship between genes. A relative change ratio (RCR) method was proposed by Li et al. to preprocess the null-mutants steady state data in order to find the key genes and build GRNs, in which these selected key genes have a higher potential than other genes to play very critical roles [10]. The LBN algorithm (local Bayesian network) [21] was designed by Liu et al. to improve the accuracy of GRN inference from gene expression data by exploring advantages of Bayesian network (BN) and conditional mutual information (CMI) methods. The LBN algorithm first uses CMI to construct an initial network or GRN. Then, the BN method is employed to generate a series of local BNs by selecting the k-nearest neighbors of each gene as its candidate regulatory genes. Integrating these local BNs forms a tentative network by performing CMI. The final network, or GRN, can be obtained by iteratively performing CMI and local BN on the tentative network. TDBN [7] was used to infer GRNs from time series trajectory data which were combined with the previous knowledge gained in the above step. Wang et al. developed the pLasso [22] method from a Bayesian perspective for the reconstruction of gene networks. This method assigns different prior distributions to different edge subsets according to a modified Bayesian information criterion that incorporates prior knowledge on both the network structure and the pathway information. It used information from the Pathway Commons (PC) and the Kyoto Encyclopedia of Genes and Genomes (KEGG) as prior information for the network reconstruction. However, in reality there is no prior knowledge while inferring the interaction relationship between genes. Moreover, signaling pathways are dynamic events that take place over a given period of time. In order to identify these pathways, expression data over time is required. Dynamic Bayesian network (DBN) is an important and widely used approach for predicting the GRNs from time series expression data but has high computational costs and may not be able to infer a large GRN.

Furthermore, other methods for inferring GRNs have been proposed. Patrilia et al. proposed a new algorithm, namely iRafNet [23], which integrated different data types under a unified random forest framework. The key idea of iRafNet is to introduce a weighted sampling scheme within random forest to incorporate information

from other sources of data. Specifically, the model considers the expression of each gene as a function of the expression of other genes. In literature [24], a fast method was developed for inferring gene regulatory relationships from just knockdown data. It used a simple linear regression model focusing on single regulator-target gene pairs based on knockdown data, and allowed the incorporation of prior knowledge about the relationships and generates posterior probabilities.

Mutual information (MI) is another measurement of the dependence of two variables and is often used to assess the relationship between genes. Margolin [16] and Sales [17] employed MI between two genes to measure their associations in order to reconstruct gene regulatory networks. But they could not tackle the problem that one gene is regulated by multiple genes. PCA_CMI [18] was proposed by Zhang et al. for inferring GRNs from gene expression data considering the non-linear dependence and topological structure of GRNs by employing path consistency algorithm based on conditional mutual information (CMI). It discovered the associations between related genes without identifying the regulators and their targets.

Reshef et al. presented a measure of dependence for two-variable relationships, named the maximal information coefficient (MIC) [25], which captures a wide range of functional and nonfunctional associations. MIC has better performance on measuring the dependence of two-variable relationships in comparison with other methods. Thus, we concentrate our effort on identifying the interactions between genes based on this method.

In this paper, we developed a novel algorithm, MICRAT (Maximal Information coefficient with Conditional Relative Average entropy and Time series mutual information), for inferring GRNs from time series gene expression data. This approach employed MIC as measurement for assessing the correlation between each pair of genes while constructing an undirected graph to represent the underlying relationship between genes. It subsequently combined conditional relative average entropy with time series mutual information to determine the potential regulator and its target genes.

## Methods

Information theory has been used to reconstruct GRNs from gene expression data. Mutual information is generally used as a useful criterion for measuring the dependence between variables (genes) $X$ and $Y$ [18]. For gene expression data, variable $X$ is a vector, in which the element $x$ denotes gene expression value in different conditions (samples/time points). In this section, we introduced several basic concepts of information theory and graph theory which will be used in the proposed method.

## Mutual information and conditional mutual information

For two random variables (genes) $X$ and $Y$, the mutual information of $X$ and $Y$ is defined as:

$$
I(X, Y)=H(X)+H(Y)-H(X, Y)
$$

where $H(X)$ and $H(Y)$ are the entropy of the random variables $X$ and $Y$, respectively; $H(X, Y)$ is the joint entropy of $X$ and $Y$.

For a discrete variable $X$, the entropy $H(X)$ measures the average uncertainty of variable $X$, and can be computed by

$$
H(X)=-\sum_{x \in X} p(x) \log p(x)
$$

where $p(x)$ is the probability that the variable $X$ takes $x$;
The joint entropy of $X$ and $Y$ is denoted by

$$
H(X, Y)=-\sum_{x \in X, y \in Y} p(x, y) \log p(x, y)
$$

where $p(x, y)$ is the joint probability of $X$ and $Y$.
The mutual information of $X$ and $Y$ is calculated by

$$
I(X, Y)=\sum_{x \in X, y \in Y} p(x, y) \log \frac{p(x, y)}{p(x) p(y)}
$$

The conditional mutual information [16] of $X$ and $Y$ given $Z, I(X, Y \mid Z)$ is defined as

$$
I(X, Y \mid Z)=\sum_{x \in X, y \in Y, z \in Z} p(x, y, z) \log \frac{p(x, y \mid z)}{p(x \mid z) p(y \mid z)}
$$

where $p(x, y, z)$ is the joint probability of variables $X, Y$ and $Z ; p(x \mid z)$ is the conditional probability that the variable $x$ holds under the condition that the variable $z$ is established; similarly, $p(x, y \mid z)$ is the conditional probability that the variable $x$ and the variable $y$ are established under the condition that the variable $z$ is satisfied.

In this paper, the probability of a variable (gene) is estimated with the Gaussian kernel probability density estimator [26] as follows [18].

$$
P\left(X_{i}\right)=\frac{1}{n} \sum_{i=1}^{n} \frac{1}{(2 \pi)^{m / 2}|C|^{n / 2}} \exp \left(-\frac{1}{2}\left(X_{i}-X_{i}\right)^{T} C^{-1}\left(X_{i}-X_{i}\right)\right)
$$

where $C$ is the covariance matrix of variable $X,|C|$ is the determinant of matrix $C, n$ is the number of samples (time points), and $m$ is the number of variables (genes).

Then the entropy of variable $X$ can be computed by using (2) and (6).

$$
H(X)=\log \left[(2 \pi e)^{\frac{m}{2}}|C|^{\frac{1}{2}}\right]=\frac{1}{2} \log (2 \pi e)^{m}|C|
$$

With formulas (1) and (7), the mutual information of variables $X$ and $Y$ can be obtained as given in Eq. (8).

$$
I(X, Y)=\frac{1}{2} \log \frac{|C(X)| \cdot|C(Y)|}{|C(X, Y)|}
$$

Similarly, the conditional mutual information of variables $X$ and $Y$ given variable $Z$ can be calculated by Eq. (9).

$$
I(X, Y \mid Z)=\frac{1}{2} \log \frac{|C(X, Z)| \cdot|C(Y, Z)|}{|C(Z)| \cdot|C(X, Y, Z)|}
$$

MI can be used for measuring the dependence of two variables (genes) and CMI can help determine the dependence between two variables given another variable. Generally speaking, a higher MI (or CMI) indicates closer relationship between variables.

## Maximal information coefficient

The maximal information coefficient (MIC) is an effective measurement of interesting relationship between pairs of variables. MIC captures a wide range of functional and nonfunctional associations, and has two heuristic properties: generality and equitability. The generality ensures that with sufficient sample size MIC captures a wide range of interesting relationships, not limited to specific function types, or even to all functional relationships; and the equitability means that MIC gives similar scores to equally noisy relationships of different types. These two heuristic properties of MIC indicate that it is suitable to infer various underlying relationships.

The Maximal Information Coefficient of a set $D$ of two-variable data with sample size $n$ and grid size less than $B(n)$ is given by literature [25].

$$
M I C(D)=\max _{X Y<B(n)} M(D)_{X, Y}=\max _{X Y<B(n)} \frac{I^{*}(D, X, Y)}{\log (\min (X, Y))}
$$

where the dataset $D$ is composed of the pairs of values $\langle x, y\rangle$, and $x \in X, y \in Y ; M(D)_{X, Y}$ is the characteristic matrix of dataset $D$ of variable $X$ and $Y$ with entries

$$
M(D)_{x, y}=\frac{I^{*}(D, x, y)}{\log (\min (x, y))}
$$

where $\Gamma(D, x, y)$ is the maximum mutual information achieved by $x$ and $y ; n$ is size of $D ; \log (\min (x, y))$ is used to normalize the maximum mutual information; $B(n)$ is the grid size, and $B(n)=n^{0.6}$, which was found to work well in practice [25].

## Conditional relative average entropy

The conditional relative average entropy (CRAE) [27] is defined as:

$$
\operatorname{CRAE}(X \rightarrow Y)=\frac{H(Y \mid X)}{H(Y) \cdot|Y|}
$$

where $|Y|$ is the number of values of variable $Y$, and
$H(Y)$ is the entropy of the variable $Y ; H(Y \mid X)$ is the conditional entropy of the variable $Y$ under the condition of the given variable $X$.

## Time series mutual information

In most cases, there is a time delay during the gene regulations or at least the gene expressions change simultaneously for regulatory and target genes. Thus the time series mutual information could contribute to the orientation of the regulation.

Suppose that we have $T$ time points and the expression levels of $N$ genes are measured at each time point. The time series gene expression data can be summarized as a $T \times N$ matrix $X=\left(x_{1}, x_{2}, \ldots, x_{T}\right)^{T}$ whose $i^{\text {th }}$ row vector $x_{i}=\left(x_{i 1}, x_{i 2}, \ldots x_{i N}\right)^{T}$ corresponds to a gene expression level vector measured at timepoint $i$.

For given genes $X$ and $Y$, the time series mutual information from $X$ to $Y$ during time points 1 to $T$ is defined as

$$
I_{T}(X \rightarrow Y)=I\left(X_{1 \rightarrow(T-t d e l a y)}, Y_{1+t d e l a y \rightarrow T}\right)
$$

where $\operatorname{tdelay}(0 \leq \operatorname{tdelay} \leq T)$ represents the time delay for gene $X$ regulating gene $Y ; X_{1 \rightarrow(T-t d e l a y)}$ is a vector representing the gene expression level of $X$ from timepoint 1 to timepoint ( $T$-tdelay). Similarly, $Y_{1+t d e l a y \rightarrow T}$ represents the gene expression level of $Y$ from timepoint $1+t d e l a y$ to timepoint $T$. In this paper, we set the time delay to 1 since from the observation of our experiments there is no significant improvement to the accuracy with different settings.

## Gene regulatory networks

In this work, a gene regulatory network is described by a directed graph (digraph). A graph $G$ is defined by the pair $(V(G), E(G))$, where $V(G)$ denotes the set of vertices (nodes) and $E(G) \subseteq V(G) \times V(G)$ denotes the set of edges. In a digraph, an edge is defined by an ordered pair of vertices $(x, y)$ denoting the edge direction, from vertex $x$ pointing to vertex $y$. Here, the nodes represent genes while the edges describe the gene regulatory interactions. A directed edge $(x, y)$ indicates that gene $x$ regulates gene $y$, while an undirected edge $(x, y)$ only indicates that there is an association between gene $x$ and gene $y$.

## Algorithm of MICRAT

We propose a novel algorithm called MICRAT for reconstructing gene regulatory networks using time series gene expression profiles. The algorithm mainly consists of two procedures: First, an undirected graph is generated representing the associations between genes based on the maximal information coefficient (MIC) of each pair of genes. Then, the conditional relative

average entropy combining with time series mutual information is used to determine the directions of the edge in the undirected graph. The flowchart of the method for reconstructing GRN is shown in Fig. 1, and more details are described in the following subsections.

### Generating an undirected gene interaction graph

The types of relationship between genes vary diversely. It is difficult, even impossible to identify the gene associations with only one function. The maximal information coefficient could capture a wide range of dependence of two variables, both functional and nonfunctional. Thus it is suitable for measuring the associations between genes.

We refer to two gene expression data *G<sub>X</sub>* and *G<sub>Y</sub>* as variables *X* and *Y*, respectively. The association between them is measured by

$$I_D(X, Y) = MIC(X, Y) \tag{14}$$

where *MIC(X, Y)* denotes the maximal information coefficient of *X* and *Y*. A higher value of *I<sub>D</sub>(X, Y)* indicates a closer relationship between *X* and *Y*, vice versa. The edges in the undirected graph are added based on a given threshold *θ* of *I<sub>D</sub>(X, Y)*.

The generation of an undirected gene interaction graph includes the following five steps:

1. Initialize the gene regulatory network, *G<sub>D</sub>*, as an undirected graph with no vertices and no edges. There are *n* genes in the dataset *D*.
2. For a given time series gene expression dataset *D*, calculate *I<sub>D</sub>(X, Y)* for each pair of genes (*x, y*).

![img-0.jpeg](img-0.jpeg)

**Fig. 1** Reconstruction of GRN flowchart

3. Rank the pairs of genes by descending order of *I<sub>D</sub>(X, Y)* obtained by step (2) to a list called *RLI*.
4. From the top of *RLI*, check each pair of genes (*x, y*), add an undirected edge between vertices *x* and *y* if *I<sub>D</sub>(X, Y)* ≥ *θ* where *θ* is a threshold and will be discussed in the experiment section.
5. Delete redundant edges. There might be some redundant edges in the undirected graph especially when there are triangle cycles. Conditional mutual information of genes is used to determine whether to delete edges or not. For example, there is a triangle cycle including three genes *X*, *Y* and *Z* in the graph since *I<sub>D</sub>(X, Y)*, *I<sub>D</sub>(X, Z)* and *I<sub>D</sub>(Y, Z)* are not lower than *θ* and three edges between *X*, *Y* and *Z* are included. We calculated three conditional mutual information values of *I(X, Y| Z)*, *I(X, Z| Y)* and *I(Y, Z| X)*, and deleted edge (*Y, Z*) if *I(Y, Z| X)* = 0, which indicates that gene *Y* has no relationship with gene *Z*.

### Data discretization and edge-orientation

In our algorithm, the edges in the undirected graph are oriented by combining the conditional relative average entropy with time series mutual information of each pair of nodes. From the observation of our experiments, better performance was obtained on discretized data. Therefore, the gene expression data were discretized before being used for edge orientation.

The gene expression data are first normalized by standard fraction *Z-Score* and then discretized according to a given threshold. The standard fraction *Z<sub>score</sub>* of the gene *X* at the time point *t<sub>j</sub>* is defined as:

$$Z_{x,j} = \frac{|x_j - \mu|}{\sigma} \tag{15}$$

where *µ* denotes the mean value of the gene expression data at all time points of gene *X*, *σ* is the standard deviation, and *x<sub>j</sub>* denotes the expression value of the gene *X* at the time point *t<sub>j</sub>*. Given a threshold *k*, if *Z<sub>x<sub>j</sub></sub><sup>j</sup>* ≥ *k*, then the gene expression data at time *t<sub>j</sub>* is denoted as 1; otherwise the gene expression data is denoted as 0.

All edges in the undirected graph are oriented by the following procedure: Given two vertices *X* and *Y* of an edge in the undirected graph, if *CRAE(X → Y) + I<sub>T</sub>(X → Y) > CRAE(Y → X) + I<sub>T</sub>(Y → X)*, then the orientation is *X → Y*, indicating that gene *X* regulates gene *Y*; While if *CRAE(X → Y) + I<sub>T</sub>(X → Y) < CRAE(Y → X) + I<sub>T</sub>(Y → X)*, then the orientation is *Y → X*, which means gene *Y* regulates gene *X*. In the case of *CRAE(X → Y) + I<sub>T</sub>(X → Y) = CRAE(Y → X) + I<sub>T</sub>(Y → X)*, the higher value of *I<sub>T</sub>(X → Y)* (or *I<sub>T</sub>(Y → X)*) indicates *X → Y* (or *Y → X*). The pseudo code of algorithm MICRAT is given in Fig. 2.

Input: Time series gene expression dataset $D$ including $n$ genes and each gene profile composed of $T$ time points, MIC value threshold $\theta$
Output: Gene regulatory network $G_{D}$
$1 G_{D} \leftarrow \emptyset$.
for $i \leftarrow 1$ to $n-1$
for $j \leftarrow i+1$ to $n$
$4 \quad \operatorname{mic}_{i, j}=\operatorname{mic}\left(\mathrm{D}(:, \mathrm{i}), \mathrm{D}(:, \mathrm{j})\right)$;
$5 \quad$ if $\operatorname{mic}_{i, j}>\theta$ and $I(i, j \mid \alpha)!=0$ then
$6 \quad \operatorname{dir}(i, j)=\operatorname{CRAE}(D(i, j))+I_{T}(i \rightarrow j)$;
$7 \quad \operatorname{dir}(j, i)=\operatorname{CRAE}(D(j, i)+I_{T}(j \rightarrow i)$;
$8 \quad$ if $\operatorname{dir}(i, j)>\operatorname{dir}(j, i)$ then
$9 \quad G_{D}(i, j)=1$;
$10 \quad$ elseif $\operatorname{dir}(i, j)<\operatorname{dir}(j . i)$ then
$11 \quad G_{D}(j, i)=1$;
$12 \quad$ elseif $I_{T}(X \rightarrow Y)>=I_{T}(Y \rightarrow X)$ then
$13 \quad G_{D}(i, j)=1$;
$14 \quad$ else
$15 \quad G_{D}(j, i)=1$;
16 return $G_{r}$
Fig. 2 Pseudo code of algorithm MICRAT

## Results and discussion

In this section, we evaluate the performance of algorithm MICRAT by applying it to synthetic datasets as well as a real gene expression dataset for inferring GRNs. Several experiments were carried out to demonstrate the performance of our approach by comparison with other related methods.

For synthetic datasets, five 10 -genes and five 100 -genes time series expression datasets from the DREAM4 challenge were used, respectively [28]. The real life gene expression dataset involves an eight-gene subnetwork, part of a DNA-damage response pathway (SOS pathway) in the bacteria E. Coli.

Generally, there are several measurements for evaluating the performance of GRN inference methods, including Precision, Recall, Accuracy (ACC), F_score, Matthews correlation coefficient (MCC), etc. They are defined as follows:

$$
\begin{aligned}
& \text { Precision }=\frac{T P}{T P+F P} \\
& \text { Recall }=\frac{T P}{T P+F N} \\
& A C C=\frac{T P+T N}{T P+F P+T N+F N} \\
& \text { F_score }=\frac{2 \times \text { Precision } \times \text { Recall }}{\text { Precision }+ \text { Recall }} \\
& M C C=\frac{T P \times T N-F P \times F N}{\sqrt{(T P+F P)(T P+F N)(T N+F P)(T N+F N)}}
\end{aligned}
$$

where $T P, F P, T N, F N$ are the numbers of true positives, false positives, true negatives and false negatives, respectively. In this study, true positives indicate correctly
inferred edges which exist in golden standard networks, while false positives denote wrongly inferred edges which do not exist in golden standard networks, and so on for true negatives and false negatives, respectively. Usually, there exists an inverse relationship between precision and recall. It is possible to increase one at the cost of reducing the other. Therefore, Accuracy, $F_{-}$score and Matthews correlation coefficient are widely used as balanced evaluation measures. Here we use $A C C, F_{-}$score and $M C C$ as measurements for evaluating the performance of our method.

In order to set the best value of $\theta$, the threshold of MIC of two gene expression data while measuring the independence between genes, we test MICRAT by varying $\theta$ from 0 to 1 with interval of 0.01 on both 10 -gene expression datasets and 100 -gene expression datasets. Empirical results showed that with the increase of $\theta$, the precision of the model becomes higher while the recall goes down. According to the experimental results, the comparatively good performance of MICRAT could be obtained while the thresholds were set to 0.43 for 10 -gene datasets and 0.15 for 100 -gene datasets, respectively.

## Experiments on simulation datasets

We first evaluated MICRAT on simulation datasets which were generated based on benchmarking networks. Many tools have been developed for assessing the effectiveness of GRN inference methods. The DREAM4 challenge introduced a critical performance assessment framework of methods for GRN inference and presented an in silico benchmark suite as a blinded, community-wide challenge within the context of the DREAM project. In this challenge, the gene expression datasets with noise and their golden standard (benchmark) networks were given. The golden standard networks were selected from source

Table 1 Experimental results for three methods on both 10-gene datasets and 100-gene datasets


networks of real species [28]. They are widely used as a benchmark for the evaluation of GRN inference methods. Here, we tested our algorithm on the DREAM4 challenge time series gene expression data in networks of size 10 and 100 genes, respectively.

As mentioned above, MICRAT found the associations between pairs of genes in the beginning. Then the conditional relative average entropy in cooperation with time series mutual information was used to orient the edges in the undirected graph and obtain the GRN. For evaluating the performance of our approach, we compared our algorithm with TDBN [7, 10] and NARROMI [19]. TDBN is a typical method with significant impact on inferring GRNs from time series gene expression data. NARROMI is quite related to our method and it significantly outperformed other methods, such as LP [29], LASSO [30, 31], ARACNE [16] and GENIE3 [32]. This procedure was tested on DREAM4 time series gene expression datasets with 10-gene networks and 100-gene networks, respectively. Experimental results were given in Table 1. First, we carried out MICRAT on five

10-gene datasets. There are $21 \times 5=105$ time points in each of the datasets. We computed $A C C, F_{-}$score and $M C C$ on each of the five datasets as evaluation measures for the compared methods. Here, we chose 0.43 as the threshold value of MIC to determine the dependence between genes in the inferred network for our method, and the threshold of $Z_{-}$score was set to $k=1.2$ for discretization of gene expression data when the edge is oriented. For NARROMI, the threshold is set to 0.05 which is the default value given in literature [19]. For TDBN, all the parameters were chosen as default in their literature. The accuracy of our approach is higher than those of the other methods in four datasets and slightly lower than that of NARROMI for dataset 5. The left part of Fig. 3 shows the average accuracies on five 10-gene datasets for three methods. It can be observed that MICRAT performed better than the others. For the $F_{-}$score measurement, MICRAT has the best performance on two datasets, but the worst performance on one dataset. Figure 4 shows that the average $F_{-}$scores on five 10-gene datasets is somewhat inferior to NARROMI but

Comparison of Three Methods for Average Accuracy 1

![img-1.jpeg](img-1.jpeg)

Fig. 3 Comparison of three methods for average ACC on 10-gene and 100-gene datasets

![img-2.jpeg](img-2.jpeg)

**Fig. 4** Comparison of three methods for average F_score on 10-gene and 100-gene datasets

superior to TDBN. From Table 1 it can be observed that MICRAT is only slightly inferior to NARROMI on one dataset but has better performance on others for MCC. Figure 5 gives the average Matthews correlation coefficients of the three methods on five 10-gene datasets and five 100-gene datasets, respectively. We can see that MICRAT is superior to NARROMI and significantly outperforms TDBN.

We also applied our algorithm to the five DREAM4 100-gene datasets. Each dataset has 21 × 10 = 210 time points. We also computed ACC, F_score and MCC on each of the five datasets as evaluation measures for MICRAT and the other two methods. Experimental results were showed in Table 1 and the right part of Figs. 3, 4 and 5. In these experiments, we chose 0.15 as the threshold of MIC to determine the regulation relationship between genes in the inferred network. For NARROMI, the threshold is also set to 0.05, the same value as in literature [19]. As shown in Table 1 and the right part of Figs. 3, 4 and 5, all the three measures of ACC, F_score and MCC in our method are superior to NARROMI and TDBN on each of the five 100-gene time series dataset. The results show that our approach has better performance than other methods on the 100-gene datasets. Thus MICRAT has the potential to infer large GRNs using time series expression data with a large number of genes.

#### Experiments on real gene expression dataset

To validate our method on a real biological gene regulatory network, we analyzed the well-known SOS DNA repair network in E. Coli. This GRN is well known for its responsibility of repairing the DNA if it gets damaged. It is the largest, most complex and best understood DNA damage-inducible network to be characterized to date [33]. We applied our MICRAT algorithm to an eight-gene network, part of the SOS DNA repair network in the bacteria E. coli [34–36]. The expression data sets of the network were obtained from Uri Aron Lab [36]. These data are kinetics of 8 genes namely uvrD, lexA,

![img-3.jpeg](img-3.jpeg)

**Fig. 5** Comparison of three methods for average MCC on 10-gene and 100-gene datasets

![img-4.jpeg](img-4.jpeg)

**Fig. 6** The target SOS DNA repair network

umuD, recA, uvrA, uvrY, ruvA and polB. Four experiments were done at various UV light intensities (Exp.1 and 2: 5*J**m*^{-2}, Exp. 3 and 4: 20*J**m*^{-2}). In each experiment, the 8 genes were monitored at 50 instants which are evenly spaced by 6 min intervals. In order to assess the effectiveness of our algorithm, we compared the inferred network with the known interactions between these eight genes. In our experiment, the threshold of MIC was set to *θ*=0.1 for measuring the dependence of the pair of genes, and the threshold of *Z*_*score* was also set to *k* = 1.2 for discretization of gene expression data while the edge is oriented. Figure 6 gives the real SOS DNA repair network. Figure 7 shows part of inferred GRN inferred by our approach. In this Figure, one can see that our method finds 6 out of the 9 edges in the target network and identifies lexA as the 'hub' gene for this network. The exact ground truth for this network is not precisely known, hence it is not possible to calculate well-known performance measures [33]. By using the known interactions obtained from literature [33, 37, 38], Table 2 showed the comparison of our algorithm with other methods such as Perrin [39], BANJO [40], GlobalMIT [41] and Morshed [33] for correct predictions on the regulatory relationships between these eight genes. From Table 2, it could be observed that our method identified most interactions except lexA→ruvA, lexA→lexA and recA→lexA, where the latter two are not inferred since our method does not consider the double regulation between two genes and the gene that is self-regulated. That is the limitation of our method, which motivates us to continue further study for improvement.

![img-5.jpeg](img-5.jpeg)

### Conclusions

In this work, a novel algorithm, MICRAT, for inferring GRNs from time series gene expression data was proposed by taking into account dependence and time delay of expressions of a regulator and its target genes. This approach employed maximal information coefficients for reconstructing an undirected graph to represent the

genes | MICRAT | Perrin
[39] | BANJO
[40] | GlobalMIT
[41] | Morshed
[33]  |

**Table 2** Comparison of interactions inferred by MICRAT with other methods on SOS DNA dataset

underlying relationships between genes. The edges were directed by combining conditional relative average entropy with time course mutual information of pairs of genes. The performance of our proposed algorithm was evaluated using synthetic datasets from benchmark GRNs provided by the DREAM4 challenge and the real, experimental dataset SOS DNA repair network in E. Coli. Experimental study showed that our approach was comparable to other methods on 10-gene datasets and outperformed other methods on 100-gene datasets in GRN inference from time series datasets. In the follow-up study, we plan to test the algorithm on large-scale datasets, including time course mRNA-Seq, human gene expression data, etc. and compare our approach with more recently proposed algorithms so as to evaluate its robustness and improve its performance.

## Abbreviations

ACC: Accuracy; CMI: Conditional mutual information; CRAE: Conditional relative average entropy; GRN: Gene regulatory network; MCC: Matthews correlation coefficient; MI: Mutual information; MIC: Maximal information coefficient

## Funding

This work was partially supported by a subaward of the National Science Foundation EPS 0903787 and the U.S. Army Environmental Quality/ Installation (EQI) Basic Research Program. Permission was granted by the Chief of Engineers to publish this information. It was also partially supported by the Key Research Projects of Universities in Henan Province of China under grant number 17AS20015. The publication cost of this article was funded by the U.S. Army Environmental Quality/Installation (EQI) Basic Research Program.

## Availability of data and materials

The datasets used and/or analysed during the current study are available at http://dreamchallenges.org/project/dream4-in-silico-network-challenge/. The codes of the algorithm of MICRAT are available from the corresponding author on reasonable request.

## About this supplement

This article has been published as part of BMC Systems Biology Volume 12 Supplement 7, 2018: From Genomics to Systems Biology. The full contents of the supplement are available online at https://bmcsystbio1.biomedcentral.com/ articles/supplements/volume-12-supplement-7.

## Authors' contributions

BY, CZ and PG conceived the project. YX and BY developed and implemented the MICRAT algorithms and conducted the experimental study. BY and CZ wrote the paper. PG, AM and WK participated in the analysis and provided suggestions for the document. All authors read and approved the final manuscript.

## Ethics approval and consent to participate

Not applicable.

## Consent for publication

Not applicable.

## Competing interests

The authors declare that they have no competing interests.

## Publisher's Note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## Author details

${ }^{1}$ School of Information \& Engineering, Zhengzhou University, Zhengzhou 450000, China. ${ }^{2}$ Center of Precision Medicine, Zhengzhou University, Zhengzhou 450000, China. ${ }^{3}$ School of Computing, University of Southern Mississippi, Hattiesburg, MS 39406, USA. ${ }^{4}$ Environmental Lab, US Army Engineer Research and Development Center, Vicksburg, MS 39180, USA.

Published: 14 December 2018

## Ready to submit your research? Choose BMC and benefit from:

- fast, convenient online submission
- thorough peer review by experienced researchers in your field
- rapid publication on acceptance
- support for research data, including large and complex data types
- gold Open Access which fosters wider collaboration and increased citations
- maximum visibility for your research: over 100M website views per year

At BMC, research is always in progress.
Learn more biomedcentral.com/submissions