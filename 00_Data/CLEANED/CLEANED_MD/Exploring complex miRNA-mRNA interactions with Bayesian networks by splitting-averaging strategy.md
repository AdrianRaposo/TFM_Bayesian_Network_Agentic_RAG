# Exploring complex miRNA-mRNA interactions with Bayesian networks by splitting-averaging strategy 

Bing Liu* ${ }^{1}$, Jiuyong $\mathrm{Li}^{1}$, Anna Tsykin ${ }^{2}$, Lin $\mathrm{Liu}^{1}$, Arti B Gaur ${ }^{3}$ and Gregory J Goodall ${ }^{2,4}$


#### Abstract

Address: ${ }^{1}$ School of Computer and Information Science, University of South Australia, Adelaide, SA 5095, Australia, ${ }^{2}$ Centre for Cancer Biology, Hanson Institute, Adelaide, SA 5000, Australia, ${ }^{3}$ Norris Cotton Cancer Center, Dartmouth Medical School, Lebanon, New Hampshire 03755, USA and ${ }^{4}$ Department of Medicine, The University of Adelaide, Adelaide, SA 5005, Australia


Email: Bing Liu* - Bing.Liu@unisa.edu.au; Jiuyong Li - Jiuyong.Li@unisa.edu.au; Anna Tsykin - anna_tsykin@yahoo.com; Lin Liu - Lin.Liu@unisa.edu.au; Arti B Gaur - Arti.B.Gaur@dartmouth.edu; Gregory J Goodall - greg.goodall@health.sa.gov.au

* Corresponding author

Published: 10 December 2009
BMC Bioinformatics 2009, 10:408 doi:10.1186/1471-2105-10-408
Received: 22 June 2009
Accepted: 10 December 2009
This article is available from: http://www.biomedcentral.com/1471-2105/10/408
(c) 2009 Liu et al; licensee BioMed Central Ltd.

This is an Open Access article distributed under the terms of the Creative Commons Attribution License (http://creativecommons.org/licenses/by/2.0), which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.


#### Abstract

Background: microRNAs (miRNAs) regulate target gene expression by controlling their mRNAs post-transcriptionally. Increasing evidence demonstrates that miRNAs play important roles in various biological processes. However, the functions and precise regulatory mechanisms of most miRNAs remain elusive. Current research suggests that miRNA regulatory modules are complicated, including up-, down-, and mix-regulation for different physiological conditions. Previous computational approaches for discovering miRNA-mRNA interactions focus only on down-regulatory modules. In this work, we present a method to capture complex miRNA-mRNA interactions including all regulatory types between miRNAs and mRNAs.


Results: We present a method to capture complex miRNA-mRNA interactions using Bayesian network structure learning with splitting-averaging strategy. It is designed to explore all possible miRNA-mRNA interactions by integrating miRNA-targeting information, expression profiles of miRNAs and mRNAs, and sample categories. We also present an analysis of data sets for epithelial and mesenchymal transition (EMT). Our results show that the proposed method identified all possible types of miRNA-mRNA interactions from the data. Many interactions are of tremendous biological significance. Some discoveries have been validated by previous research, for example, the miR-200 family negatively regulates ZEB1 and ZEB2 for EMT. Some are consistent with the literature, such as LOX has wide interactions with the miR-200 family members for EMT. Furthermore, many novel interactions are statistically significant and worthy of validation in the near future.

Conclusions: This paper presents a new method to explore the complex miRNA-mRNA interactions for different physiological conditions using Bayesian network structure learning with splitting-averaging strategy. The method makes use of heterogeneous data including miRNAtargeting information, expression profiles of miRNAs and mRNAs, and sample categories. Results on EMT data sets show that the proposed method uncovers many known miRNA targets as well as new potentially promising miRNA-mRNA interactions. These interactions could not be achieved by the normal Bayesian network structure learning.

## Background

MicroRNAs (miRNAs) belong to a group of singlestranded, non-coding RNAs that are 21-23 nucleotides in length [1]. miRNAs target protein coding mRNAs through complementary base-pairing that results in repressing translation and causing mRNA degradation [2,3]. Hundreds of miRNAs have been identified and sequenced in plants, animals, and viruses since the first miRNA, lin-4, was discovered in 1993 [4]. As a growing class, it is estimated that miRNAs directly regulate at least $30 \%$ of the genes in the human genome [5].

Increasing evidence suggests that miRNAs play important roles in cell differentiation, proliferation, growth, mobility, and apoptosis [6-8]. miRNAs regulate target mRNAs [9], and act as rheostats to make fine-scale adjustments to protein output [10]. Consequently, dysregulation of miRNA function may lead to human diseases, including cancers [11]. However, the functions of most miRNAs and their precise regulatory mechanisms remain elusive. Thus, great efforts have been made to elucidate miRNA functions in recent years.

Extensive studies have proposed the diverse features of miRNA regulation. Mature miRNAs target the 3' untranslated regions ( $3^{\prime}$ UTR) of genes by complementary basepairing. Furthermore, mature miRNAs can alter the expression of genes by binding to the coding regions as well as the $5^{\prime}$ UTR [12,13]. Other regions, known as extended seed and delta seed regions, also contribute to the target selection [14]. miRNAs down-regulating target mRNAs has been widely observed [15,16]. Recent experiments also show that miRNAs up-regulate target mRNAs in some cases [17-20]. In addition, miRNAs may up-regulate target mRNAs in one condition, but repress translation in another condition. For example, let7 and the synthetic microRNA miRcxcr4-likewise induce translation up-regulation of target mRNAs upon cell-cycle arrest; yet, they repress translation in proliferating cells [17]. The diversity and abundance of miRNA targets result in a large number of possible miRNA regulatory mechanisms. It would be infeasible to test all the possibility with biological experiments in large scale. Alternatively, computational approaches can facilitate experimental validation by producing valid hypotheses from existing data.

Several computational methods have been proposed to study miRNA regulatory mechanisms. Yoon et al. [21] proposed a prediction method for miRNA regulatory modules (MRMs) in which weighted bipartite graphs are adopted to model the binding structures of miRNAs and mRNAs at the sequence level. However, predictions only based on sequence may not be sufficient to determine the complex interactions of miRNA-mRNA pairs. Huang et al. [22] applied Bayesian network parameter learning to infer
miRNA-mRNA interactions, while Joung et al. [23] utilized a biclustering approach to discover MRMs. Their methods integrate both sequence information and expression profiles of miRNAs and mRNAs to identify the relevant miRNA-mRNA pairs, thus potentially reduce false discovery rate. Furthermore, Tran et al. [24] applied a rule based method to explore MRMs based on an assumption that miRNAs and mRNAs of a module have similar expression patterns. Similarly, their method uses both sequence information and expression profiles of miRNAs and mRNAs. However, no information of sample categories has been utilized. Considering most biological experiments are designed to compare samples from different phenotypes, conditions, or treatment groups, the sample categories are important for exploring subtle but useful differences. All of the above mentioned methods have not utilized this critical characteristic of comparative design of biological experiments so far. In this study, we will show that without using the information of sample categories, subtle miRNA-mRNA interactions are missed out. In previous work, Liu et al. [25] associated miRNA-mRNA pairs with specific conditions to discover the functional miRNA-mRNA regulatory modules (FMRMs). However, only down-regulation patterns were considered. In this work, we will explore all the possible miRNA-mRNA interactions by taking into account sample categories of comparative designs of biological experiments.

Considering the complexity and diversity of miRNAmRNA interactions, Bayesian Network (BN) structure learning has the privileges to discover statistically significant miRNA-mRNA interactions from data. It has been used widely for discovering gene regulatory networks [26], but not often for finding miRNA-mRNA interactions yet. In the scenario of BN structure learning, the interactions between miRNAs and mRNAs are defined as dependencies of their states encoded in a graphical representation. In the graph, miRNAs and mRNAs are denoted as nodes and interactions are directed edges. The presence or absence of a directed edge from a miRNA to a mRNA indicates the states of the mRNA are dependent or independent on that of a miRNA. This implies their regulatory relationship. Thus, the dependencies in the graph encode various types of miRNA-mRNA interactions. When the expression data of miRNAs and mRNAs are given, we can use the BN structure learning to capture miRNA-mRNA interactions.

This model-based approach starts by defining the possible structure space, and then followed by a learning procedure to evaluate each structure with a scoring function on the given data [27]. The structure with the maximum score is the one that best depicts the interactions of miRNAs and mRNAs. As a simple example, consider the expression observations of miRNA $A$ and mRNA $B$ given in Figure 1-

![img-0.jpeg](img-0.jpeg)

Figure 1
An example of Bayesian Network structure learning. (a) Observations of expression of miRNA $A$ and mRNA $B$ have been discretized to binary values, where 0 denotes under-expressed, and 1 stands for over-expressed. (b) Two possible structures are hypotheses of their relationship. (c) The one that received highest score supported by the data is used to represent the interaction of miRNA $A$ and mRNA $B$.
(a), where 0 denotes under-expressed and 1 stands for over-expressed. The possible interactions between miRNA $A$ and mRNA $B$ are no interaction (no edge between $A$ and $B$ ) and miRNA $A$ regulates mRNA $B$ (a directed edge from $A$ to $B$ ) (Figure 1-(b)). The BN structure learning algorithm calculates a score for each structure against the given expression observations. The one with the highest score, which is best supported by the observations, is chosen to represent the relationship between miRNA $A$ and mRNA $B$ (Figure 1-(c)). More complex interactions among multiple miRNAs and mRNAs can be factorized to the individual ones according to the probability theory.

However, under the comparative design of microarray experiments, subtle interactions are unrevealing to a normal BN structure learning method. Demonstrated in Figure 2, six cases represent three observed miRNA-mRNA interactions in different conditions: i) miRNAs down-regulate mRNAs ( $a, b$ ); ii) miRNAs up-regulate mRNAs ( $c, d$ ); and iii) miRNAs down-regulate mRNAs in one category, but up-regulation appears in another category ( $e, f$ ). The normal BN structure learning is able to capture the interactions showed in cases of $(a)-(d)$, but not $(e)$ and $(f)$. In the cases of $(a)-(d)$, the sample correlation within one category (local correlations), either negative or positive, is consistent with the correlation in the other categories. However, the local correlation is inconsistent with the others in the cases of $(e)$ and $(f)$. In $(e)$, the samples in category $c_{1}$ are positively correlated, while negatively correlated in category $c_{2}$. Similarly, in $(f)$ the samples show negative correlation in category $c_{1}$, while positive correlation in category $c_{2}$. Without considering the sample categories, the normal BN structure learning fails to capture the interactions, even when there is a strong interaction within a category. Therefore, the subtle interactions among miRNAs and mRNAs remain unrevealing.

In this paper, we present a method to capture complex miRNA-mRNA interactions with BN structure learning for specific conditions. This method discovers the dependency relationship between miRNAs and mRNAs which implies their complex interactions on heterogeneous data sets: miRNA-target binding information, expression profiles of miRNAs and mRNAs. In order to capture all possible interactions, we split expression profiles of miRNAs and mRNAs according to sample categories, and then build Bayesian networks on separate data sets. Interaction networks identified on individual data sets are then integrated by BN averaging procedure. To avoid statistically insignificant results due to small data sets, we employ bootstrapping to achieve reliable inference and integration. We call this strategy splitting and averaging of Bayesian networks (SA-BNs).

To test the SA-BNs approach, we used microRNA and mRNA expression data from the NCI-60 panel of cell lines and focused on miRNA-mRNA interactions potentially involved in the biological process of epithelial to mesenchymal transition (EMT). A number of miRNAs and mRNAs are known to be involved in this process and several miRNA-mRNA interactions have been experimentally verified [28,29]. Compared to the results from a normal BN structure learning, SA-BNs uncover more known miRNA targets as well as promising miRNA-mRNA interactions.

## Methods

In this section, we present a model of SA-BNs to discover miRNA-mRNA interactions. The scheme of SA-BNs is shown in Figure 3. After the normalization of expression profiles of miRNAs and mRNAs, differential gene expression analysis identifies a set of miRNAs and mRNAs which are differentially expressed in different conditions under the investigation. Then, we split the expression profiles of identified miRNAs and mRNAs according to categories of samples. Expression profiles of miRNAs and mRNAs have different scales since they are usually profiled with different techniques and platforms. We use discretization as a standardization means for data from different platforms. miRNA and mRNA expression profiles are then integrated for Bayesian network structure learning.

For each sample category, Bayesian network structure learning is used to learn the dependency structures of miRNAs and mRNAs on the discretized profiles. The individual structures learned from data of each category are then integrated into an overall miRNA-mRNA interaction network by the designed BN averaging procedure. In order


Figure 2
Various miRNA-mRNA interactions in comparative study. Three types of observed miRNA-mRNA interactions are: i) miRNAs down-regulate mRNAs (a, b); ii) miRNAs up-regulate mRNAs (c, d); and iii) miRNAs down-regulate mRNAs in one category, but up-regulation appears in another category (e, f). Subtle interactions in (e) and (f) are unrevealing if the analysis ignores the sample categories. Our designed method is able to uncover all types of interactions.

![img-1.jpeg](img-1.jpeg)

**Figure 3**

**A flowchart of the design of SA-BNs.** miRNA-target binding information, expression profiles of miRNAs and mRNAs, and sample categories are used to discover the complex miRNA-mRNA interactions.

To control the false discovery, we make use of miRNA-targeting information in the learning process.

We note that the sample size of miRNA or mRNA is usually small in practice. Bootstrapping [30], that is, resampling with replacement, is applied to above procedures for robust inference. The belief confidences of inferred interactions are estimated by a statistic model. This model is to approximate frequency distributions of miRNA-mRNA interactions from bootstrapping. Significant miRNA-mRNA interactions and their confidence scores are thus achieved.

#### *Annotation*

Consider two expression data sets profiling *N* miRNA and *M* mRNA transcripts across *S* samples, respectively. Those samples belong to *C* different categories, either phenotypes, conditions, or treatment groups. Let *i*, *j*, where 1 ≤ *i* ≤ *N* and 1 ≤ *j* ≤ *M*, be the indices denoting the particular miRNA and mRNA. Let **x** = {*x*<sub>*i*</sub>} and **y** = {*y*<sub>*j*</sub>} be the vectors

of miRNAs and mRNAs, and $S_{k}$ be the number of samples of category $k$, where $1 \leq k \leq C$.

According to the sample categories, we reconstruct the two data sets of miRNA and mRNA to $C$ data sets $\left\{D_{k}\right\}$. Each reconstructed data set $D_{k}$ is composed by $S_{k}$ samples profiling miRNAs $\mathbf{x}$ and mRNAs $\mathbf{y}$ for category $k$. That is, $D_{k}$ has $S_{k}$ vectors, and each contains $N+M$ variables, $\{\mathbf{x}, \mathbf{y}\}$, denoting miRNAs and mRNAs. We are interested in interactions between $\mathbf{x}$ and $\mathbf{y}$ supported by the experiment data. Assume miRNAs are independent to each other, and so as to mRNAs. The miRNA-mRNA interactions are represented as directed bipartite structures. Thus, we shall explore the relationships between $\mathbf{x}$ and $\mathbf{y}$ given data sets $\left\{D_{k}\right\}$ under the constraint of miRNA-targeting information.

## Design of SA-BNs

The above question can be modeled as learning Bayesian network structures of miRNAs and mRNAs under topology constraints given the observed data sets. That is, to identify a graph $G^{h}$ depicting the miRNA-mRNA interactions which are best supported by the given data sets $\left\{D_{k}\right\}$. We use $h$ to denote a hypothesis. A graph $G^{h}=\{\mathbf{x}$, y, $E\}$ encodes the dependencies between vertices $\mathbf{x}$ and $\mathbf{y}$ with directed edges $E$, whereas no edges mean independence between vertices. We denote the event of presence of an edge between variables $x_{i}$ and $y_{i}$ with $F_{i j}$. Our objective is to find the probability $p\left(F_{i j}\right)$ from the inferred graph $G^{h}$ given data $\left\{D_{k}\right\}$.
$\left\{D_{k}\right\}$ are mutually exclusive to each other after splitting, we have $\sum_{k} p\left(D_{k}\right)=1$. According to the total probability theorem, the probability $p\left(F_{i j}\right)$ is expressed as

$$
p\left(F_{i j}\right)=\sum_{k} p\left(F_{i j} \mid D_{k}\right) p\left(D_{k}\right)
$$

It indicates that the inference of an edge between two variables is decomposable by averaging its probabilities deduced from individual data sets. By introducing the graph $G^{h}$ learned from data set $D_{k}$, Equation (1) can be further extended to

$$
\begin{aligned}
p\left(F_{i j}\right)= & \sum_{k} p\left(F_{i j} \mid G^{h}, D_{k}\right) p\left(G^{h} \mid D_{k}\right) p\left(D_{k}\right) \\
& \sum_{k} p\left(F_{i j} \mid G^{h}\right) p\left(G^{h} \mid D_{k}\right) p\left(D_{k}\right)
\end{aligned}
$$

where
$p\left(F_{i j} \mid G^{h}\right)=\left\{\begin{array}{l}1 \text { if the edge between } x_{i} \text { and } y_{j} \text { is present in } G^{h} \\ 0 \text { if the edge between } x_{i} \text { and } y_{j} \text { is absent in } G^{h}\end{array}\right.$
By Bayesian theorem, the posterior probability $p\left(G^{h} \mid D\right)$ is calculated by multiplying the prior probability $p\left(G^{h}\right)$ with the likelihood $p\left(D \mid G^{h}\right)$ as

$$
p\left(G^{h} \mid D\right)=\frac{p\left(G^{h}\right) p\left(D \mid G^{h}\right)}{p(D)}
$$

Substitute Equation (4) into Equation (3), we have

$$
p\left(F_{i j}\right)=\sum_{k} p\left(F_{i j} \mid G^{h}\right) p\left(D_{k} \mid G^{h}\right) p\left(G^{h}\right)
$$

The prior probability $p\left(D_{k}\right)$ in Equation (3) is eliminated in Equation (5). It indicates that the presence of an edge is independent of the data set conditioned on the graph learned from the data set.

We adopt the BNs averaging procedure for each data set in order to alleviate the overfitting which results from the small sample size of available data. $l$ graphs with the highest confidence inferred from the data set are averaged at the local level. We further extend Equation (5) to

$$
p\left(F_{i j}\right)=\sum_{k} \sum_{l} p\left(F_{i j} \mid G_{l}^{h}\right) p\left(D_{k} \mid G_{l}^{h}\right) p\left(G_{l}^{h}\right)
$$

Thus, the stable inference of interactions between miRNAs and mRNAs given multiple data sets can be achieved. We summarize the procedure of computing $p\left(F_{i j}\right)$ in the following algorithm.

Algorithm I: Calculating the interaction belief confidence $\mathrm{p}\left(\mathrm{F}_{i j}\right)$ of two sets of variables given data sets
Function: Cal_InteractionBelief()
Input:
$C$ - number of data set
$D_{k}$ - data sets
$l$ - number of candidate graphs from data set $D_{k}$
$I$ - index of parents (miRNAs)
$J$ - index of descendants (mRNAs)
$p$ - prior probability of a graph
Output:
$p\left(F_{i j}\right)$ - the interaction belief set of parent $i$ to descendant $j$

Cal_InteractionBelief $\left(C, D_{k}, I, I, J, p\right)$

for $k$ in 1 to $C$

$$
G_{l}^{h}=\text { graph_search }\left(D_{k}, I, J\right) ; / * \text { Given } D_{k}, \text { search for } l
$$

graphs with the maximum likelihood $p\left(D \mid G^{h}\right)$ within the constrained graph space. The graph space is constrained by miRNA-targeting information coded by index $I$ and $J$. Discussed in section Learning BN structures with constraints of domain knowledge.*/
end
for $i$ in $I$
for $j$ in $J$

$$
p\left(F_{i j}\right)=\Sigma_{k} \Sigma_{l} p\left(F i j \mid G_{l}^{h}\right) p\left(D_{k} \mid G_{l}^{h}\right) p\left(G_{l}^{h}\right)
$$

end
end
\}
In Algorithm 1, we constrain the structure learning with miRNA-targeting information. In the following two sections, we discuss the constraints, then present a statistical model to estimate the confidences of inferred interactions.

## Learning BN structures with constraints of domain knowledge

The learning procedure of BNs is computationally consuming. The exhaustive search for the structure that best fits the observations is feasible only when there are a few genes. The space of possible structures grows hyper-exponentially with the number of genes. It has been shown that learning the global optimal BN is NP-complete [31]. Heuristic algorithms, such as hill climbing, can be used to search the state space efficiently. However, heuristic methods usually find a local optimal solution instead of the global one. This largely limits applications of BNs in real world.

An alternative solution to this problem is to constrain the searching space by integrating domain knowledge. It has been suggested that the utilization of domain knowledge can bias the searching space and lead to near optimal solutions [32]. Some methods have been proposed to explore gene regulatory networks by combining prior domain knowledge [33-36]. To a specific research question, the domain knowledge provides the problem-solv-
ing preferable constraints to the state space of the particular problem by knocking out obviously unreasonable states without losing the coverage. It may lead to improved network structures in short time [37].

We are interested in the regulatory relationship between miRNAs and mRNAs. The assumption of miRNAs regulating mRNAs constrains the topologies of miRNA-mRNA interactions to be directed bipartite graphs. This constraint reduces the searching space greatly. Furthermore, miRNA target information based on sequence complementary base-pairing provides another biological constraint to the topology. Many targeting databases can be used to construct the topology, for example, miRBase [38], PicTar [39], and TargetScan [40].

We use the miRNA target information from the target database to constrain the searching space of BNs. The putative target relation of miRNAs and mRNAs deduced from the target database is used as an initial structure of miRNA-mRNA interaction network. In Algorithm 1, this structure is given by variable $I$ and $J . I$ denotes the index of parents (miRNAs), and $J$ denotes the index of descendants (mRNAs). Function graph_search $\left(D_{k}, I, J\right)$ searches bipartite graphs defined by $I$ and $J$ for the graphs that have maximum likelihood. Remove operation only is used in this function. It removes the edges one by one in the graph space constrained by $I$ and $J$. By this way, we can constrain the searching space within the given putative targeting space. Generally, this space is relatively sparse, and hence the computational complexity is reduced. Therefore, we are able to use an exhaustive searching algorithm to discover the optimal solutions within the given space.

## Generating highly confident interactions by integrating knowledge through bootstrapping

Unstable estimation caused by small number of samples is another challenge to BNs. A typical microarray experiment usually includes a large amount of genes and a small number of samples. The small number of samples rarely support statistically significant discoveries. BNs implement a model averaging procedure to average over several candidate solutions to obtain the optimal one. The confidence is estimated by bootstrapping. Averaging and bootstrapping provide BNs a reliable way to analyze data sets with the small size of samples. In our methods, we innovatively improve the methods for belief estimation. We use bootstrapping in the above procedures to estimate the confidence of discovered interactions. Let $n$ be the number of bootstrapping, $q_{i j k}$ be the event of learning the interaction between miRNA $i$ and mRNA $j$ on the local data set $D_{k}$. Assuming each learning process $q_{i j k}$ is a stochastic process, we approximate the whole learning process as a Bernoulli experiment where $q_{i j k}=1$ when miRNA $i$ targets mRNA $j$ learned from $D_{k}$, otherwise $q_{i j k}=0$. Thus,

$q_{i j k}$ follows a binomial distribution $q_{i j k} \sim B(n, p)$, where $p$ is the probability of $q_{i j k}=1$. With a reasonable assumption, $p\left(q_{i j k}=1\right)=p\left(q_{i j k}=0\right)=0.5$ is used in the design.

At the integration stage by averaging, the interactions from local data set $D_{k}$ are aggregated. The interaction of miRNA $i$ and mRNA $j$ learned through multiple data sets, denoted as $Q_{i j}=\sum_{k} q_{i j k}$, also follows a binomial distribution $Q_{i j} \sim B(\ln n, p)$. Adopting this statistical model, we are able to extract the learned interactions at significant levels.

## Results

In this section, we provide an analysis of miRNA-mRNA interactions for EMT data with the SA-BNs method.

EMT is part of processes of tissue remodeling during embryonic development, wound healing, and an essential early step in tumor metastasis [41]. Several molecular and cellular functions are involved in turning an epithelial cell into a mesenchymal cell. It requires alterations in morphology, cellular architecture, adhesion, and migration capacity [42]. In this work, we use the proposed computational method to discover miRNA-mRNA interactions for EMT.

## Data sources

Our method integrates heterogeneous data to discover the interactions of miRNAs and mRNAs. These data include miRNA targeting information and expression profiles of miRNAs and mRNAs.

Several databases provide the putative targets of miRNAs [38-40]. We use miRBase [38] in this work because it gives more target predictions compared with experimentally supported databases. It allows our methods to produce relatively more hypotheses in a reasonable range. miRNA expression profiles for the NCI-60 panel of 60 cancer cell lines were from Gaur et al. [43]. They are available at the NCI/DTP database http://dtp.nci.nih.gov/mtweb/ search.jsp. The mRNA expression profiles for NCI60 were downloaded from ArrayExpress http://www.ebi.ac.uk/ arrayexpress, accession number E-GEOD-5720. Cell lines categorized as epithelial (11 samples) and mesenchymal (36 samples, one is not available) were used for this work.

## Identifying differentially expressed miRNAs and mRNAs

We focus on the differentially expressed miRNAs and mRNAs in epithelial and mesenchymal samples. Applying the Welch $t$-test with 10, 000 times permutation, we identified 8 miRNAs (Table 1) that are differentially expressed at significant levels ( $p$-value $<0.05$, adjusted by Benjamini \& Hochberg (BH) method). Using a similar method, 3556 probes of mRNAs (Additional file 1) are differentially expressed at significant levels ( $p$-value $<0.05$ without adjustment).

Table I: Differentially expressed miRNAs for EMT


Applying the Welch $t$-test with 10, 000 times permutation, we identified 8 miRNAs that are differentially expressed at significant levels ( $p$-value $<0.05$, adjusted by Benjamini \& Hochberg (BH) method). miRBase target V5.0 [38] is used to build the putative target pairs between the differentially expressed miRNAs and mRNAs. 1030 pairs of miRNA-mRNA are linked, comprising 6 miRNAs (miR-200c, miR-141, miR-200b, miR-200a, miR-155, and miR-203) and 610 probes for 460 unique mRNAs.

Figure 4 is the clustered heat map for the differentially expressed miRNAs across the epithelial and mesenchymal samples. The heat map indicates that the identified miRNAs show distinct patterns between epithelial and mesenchymal samples.

## Discovering and validating miRNA-mRNA interactions with SA-BNs

To integrate miRNA and mRNA data profiled by different platforms, we discretized the data sets to binary values standing for up-regulation and down-regulation. We use the median of each array as the cut-off. The two discretized data sets were merged together sample wise, and then split to two data sets by sample categories, such as epithelia and mesenchymal. It is corresponding to the constant $C$ in Algorithm 1. SA-BNs are then used to investigate the miRNA-mRNA interactions on the discretized EMT data sets with 1000 times bootstrapping. Confidences of interactions are estimated accordingly. As a result, we identified 231 statistically significant interactions which comprise 127 unique mRNAs and 6 miRNAs for EMT (Additional file 2).

## Correlation test suggests both direct and indirect regulations discovered

The discovered interactions can be categorized to negatively and positively correlated miRNA-mRNA pairs. Figure 5 shows the Pearson's correlation of miRNA-mRNA pairs vs. significant confidences of interaction discovered by SA-BNs. It shows that the discovered miRNA-mRNA pairs are largely correlated, either negatively or positively. The negatively correlated miRNA-mRNA pairs suggest

![img-2.jpeg](img-2.jpeg)

**Figure 4**

**The heatmap of differentially expressed miRNAs.** The differentially expressed miRNAs are clustered by sample groups and p-values. The identified miRNAs show distinct patterns between epithelial and mesenchymal samples.

Direct interactions, while the positively correlated ones suggest indirect interactions.

Several miRNAs have recently been described as crucial regulators of EMT and metastasis. Apart from the up-regulatory mechanism of miRNAs, down-regulations have also been identified in several works. For example, Gebeshuber et al. [20] found up-regulation of miR-29a in mesenchymal, metastatic RasXT cells relative to epithelial EpRas cell. Liu et al. [19] found that miRNA-146a was up-regulated in human bronchial epithelial cells. The results from SA-BNs suggest that more up-regulation of miRNAs could be in EMT. In the 231 statistically significant interactions, there are 145 interactions are down-regulation, while 86 interactions are up-regulation (Figure 6).

We first focus on negatively correlated miRNA-mRNA pairs. Figure 7-(a) is the significant miRNA-mRNA interaction network for EMT with only down-regulated interactions.

### *Validating targets with TarBase and miRecords*

We validate the results of SA-BNs against two experimentally supported databases, TarBase V5.0 [44] and miRecords [45]. As shown in Table 2, the number of experimentally validated targets for the identified miRNAs is very small. In total, 16 target relationships consisting of 6 miRNAs and 12 mRNAs have experimental supports from TarBase and miRecords. Among them, 5 target relationships are supported by our experimental data sets and also predicated by SA-BNs.

It is worth noting that SA-BNs are mainly designed to identify the miRNA-mRNA interactions for specific conditions. In the analysis, it has been used to discover the miRNA-mRNA interactions for EMT. Table 2 shows that 5 out of 7 identified miRNA-mRNA interactions by SA-BNs have been confirmed experimentally for EMT. It suggests that SA-BNs are promising to discover the miRNA-mRNA interactions for specific conditions. In the following, we will discuss the interactions for EMT in detail.

### *SA-BNs discover the miR-200 family target ZEB1 and ZEB2 for EMT which have been experimentally validated*

The miR-200 family has been identified to play a central role in the regulation of the epithelial to mesenchymal transition [28,29,46]. In the interaction network, SA-BNs identified experimentally validated targets of *miR-200* family. The results of SA-BNs show that *ZEB1* is co-targeted by *miR-200b* and *miR-200c*, and *ZEB2* is co-targeted by *miR-200a* and *miR-200b* in EMT module at statistically significant level. Correlation tests show that miR-200 negatively correlates with *ZEB1* and *ZEB2* at significant level (*p*-value < 0.005, adjusted by BH method). The discovery

![img-3.jpeg](img-3.jpeg)

Figure 5
Pearson's correlation of miRNA-mRNA pairs vs. significant confidences of their interactions discovered by SA-BNs. The x-axis shows the confidence of interactions, ranging from 0 (the least confident) to 1 (the most confident), while only the statistical significant scale remains ( $p$-value $<0.05$ ). The $y$-axis shows the sample correlations of identified miRNA-mRNA pairs. The red and blue points are miRNA-mRNA pairs which are correlated at the significant level ( $p$-value $<0.05$ ). It shows that the identified interactions are largely correlated, either negatively or positively, suggesting direct interactions and indirect interactions correspondingly.
![img-4.jpeg](img-4.jpeg)

Figure 6
Percentage of down- and up- regulatory interactions identified by SA-BNs. In the 231 statistically significant interactions, 145 are down-regulatory interactions, and 86 are up-regulatory interactions.
indicates that the miR-200 family negatively regulates ZEB1 and ZEB2, in agreement with previous experimental work showing that the miR-200 family regulate EMT by directly targeting ZEB1 and ZEB2 [28,29,46]. This discovery of SA-BNs is consistent with the validated results.

SA-BNs discover LOX has wide interactions with miR-200 family for EMT which is also supported by literature
SA-BNs show that LOX is negatively co-regulated by all miR-200 family members inducing EMT. Higgins et al. have suggested that LOX regulates EMT [47]. This is consistent with our results and suggests that LOX has wide interactions with the miR-200 family members for EMT.

A significant number of mRNAs identified by SA-BNs participate in the biological processes of EMT
The functions of identified mRNAs and the molecular pathways they potentially constitute were assessed by using Ingenuity Pathway Analysis (IPA) software. The regulated targets are significantly enriched for several biological functions. The top five functions listed by IPA are known to be critical for EMT. They are cellular development, cell-to-cell signaling and interaction, cellular movement, gene expression, and cellular growth and proliferation. Specifically, sub-categories of cellular movement, migration, invasion, and scattering, have been identified as the functional markers of EMT [42]. In the results identified by SA-BNs, a significant number of mRNAs associate with these EMT functional markers (Table 3), details in Additional file 3). It suggests that SA-BNs captured many mRNAs and their interactive miRNAs participating in EMT.

Molecular networks participated in by identified mRNAs are highly relevant to EMT, suggesting that the pathways of identified mRNAs may also be regulated by the miR-200 family
IPA identified 8 molecular networks constituted by the 88 predicted targets which are down-regulated by miRNAs, exemplified by three networks which are highly relevant to EMT in Figure 8, 9 and 10. The network in Figure 8 suggests functions in cancer, cellular movement and gastrointestinal disease. 18 out of 34 mRNAs in this network are identified by SA-BNs. In the network, FN1 is a hub interacting with many other molecules involved in functions associated with EMT, including migration, adhesion, cell spreading, apoptosis, proliferation, formation, attachment, quantity, assembly, and invasion. SA-BNs suggest that miR-200b and miR-200c co-regulate FN1 for EMT. In addition, LOX, which was identified to interact with miR200 family by SA-BNs, is involved in this network by interacting with many other molecules, including FN1. Figure 9 shows the network has functions in cell morphology, skeletal and muscular system development, and connective tissue development. 16 out of 35 molecules in this

![img-5.jpeg](img-5.jpeg)

Figure 7
Discovered miRNA-mRNA interaction networks. miRNA-mRNA interaction networks discovered by (a) SA-BNs and (b) normal BNs for EMT, rendered in Cytoscape [49]. In these modules, the miRNA-mRNA pairs are negatively correlated. miRNA are colored by red. The mRNAs co-targeted by same miRNAs are grouped and shown in the same color.

Table 2: Validating targets against TarBase and miRecords


16 target relationships consisting of 6 miRNAs and 12 mRNAs have experimental supports from TarBase and miRecords. Among them, 5 out of 7 identified miRNA-mRNA interactions by SA-BNs have been confirmed experimentally for EMT (denoted by *).

Table 3: Identified mRNAs are significantly involved in the functional markers of EMT


In the results identified by SA-BNs, a significant number of mRNAs associate with these EMT functional makers.

![img-6.jpeg](img-6.jpeg)

Figure 8
A molecular network with functions in cancer, cellular movement, and gastrointestinal disease. 18 out of 34 mRNAs (colored in grey) in this network are identified by SA-BNs. Highlighted in graph, FN1 is a hub interacting with many other molecules involved in functions associated with EMT. SA-BNs suggest that miR-200b and miR-200c co-regulate FN1 for EMT. In addition, LOX, which was identified to interact with miR-200 family by SA-BNs, also involves in this network by interacting with many other molecules, including FN1.

![img-7.jpeg](img-7.jpeg)

Figure 9
A molecular network with function in cell morphology, skeletal and muscular system development and function, connective tissue development and function. 16 out of 35 mRNAs (colored in grey) in this network are identified by SA-BNs, including one of the validated targets of miR-200 family, ZEB1 (highlighted). In addition, JUN, regulated by miR-200b according to SA-BNs, interacts with many other molecules involved in apoptosis, proliferation, growth, transformation, cell death, morphology, cell cycle progression, survival, colony formation, and motility.

![img-8.jpeg](img-8.jpeg)

**Figure 10**

**A molecular network with function in cellular growth and proliferation, cellular function and maintenance respiratory system development and function.** 15 out of 35 mRNAs (colored in grey) in this network are identified by SABNs, including one of the validated targets of miR-200 family, ZEB2 (highlighted).

The network is identified by SABNs, including one of the validated targets of miR-200 family, ZEB1. Furthermore, JUN, regulated by miR-200b according to SABNs, interacts with many other molecules involved in apoptosis, proliferation, growth, transformation, cell death, morphology, cell cycle progression, survival, colony formation, and motility. Figure 10 is the network with functions in cellular growth and proliferation, cellular function and maintenance. 15 out of 35 mRNAs in this network are identified by SABNs, including one of the validated targets of miR-200 family, ZEB2. Mechanisms mediated by these molecules have been implicated in EMT. Figure 8, 9 and 10 suggest that these pathways may also be regulated by miR-200 family.

## Comparing Networks Identified by SA-BNs and Normal BNs

We compared the miRNA-mRNA interactions discovered by SA-BNs to those identified by normal Bayesian networks under the same settings. With normal BNs, 98 miRNA-mRNA interactions were identified at statistically significant level. They comprise 6 miRNAs and 84 mRNAs (Additional file 4). The significant interaction network with only negatively correlated modules is given in Figure 7-(b). In this network, normal BNs identified only one validated miR-200 target, ZEB1.

The topology of interaction network identified by SA-BNs is more biologically appropriate than that of normal BNs
In comparison with the network identified by SA-BNs (Figure 7-(a)), the network identified by traditional BNs is more sparse. SA-BNs capture more mRNAs that are potentially co-targeted by multiple miRNAs, which is a biological expectation when the miRNAs are known to contribute to the same biological process, as is the case for the multiple members of the miR-200 family [29]. Furthermore, based on their sequence similarity in the "seed region", miR-200a and miR-141 are predicted to interact with the same target sites. miR-200b and miR-200c, which share identical $5^{\prime}$ ends, are predicted to recognize another set of targets in common [29]. However, in the network discovered by normal BNs, only one mRNA is co-targeted
by miR-200a and miR-141, and only 2 by miR-200b and miR-200c. In contrast, 16 mRNAs are co-regulated by miR-200a and miR-141, and 19 mRNAs are co-regulated by miR-200b and miR-200c in the network discovered by SA-BNs. Thus the network from SA-BNs gives a more expected result than the one from normal BNs.

SA-BNs discover more relevant miRNA-mRNA interactions for EMT Figure 11 shows the number of interactions for each miRNA and the total number of interactions discovered by SA-BNs and normal BNs. SA-BNs discovered more statistically significant miRNA-mRNA interactions than normal BNs.

To determine whether the unique set of interactions discovered by SA-BNs has different patterns which are specific to SA-BNs, we reviewed the correlations of miRNAmRNA samples for each category, that is, epithelial and mesenchymal. It shows that a large number of miRNAmRNA pairs show inconsistent correlation patterns across sample categories. For example, SA-BNs captured that miR-200c interacts with FN1 while the normal BNs did not. At the data level, miR-200c and FN1 show positive correlation in epithelial samples, but negative correlation in mesenchymal samples. The inconsistent patterns of local correlations prevent the normal BNs from discovering subtle interactions between miRNAs and mRNAs. SA-
![img-9.jpeg](img-9.jpeg)

Figure II
Number of miRNA-mRNA interactions discovered by SA-BNs and a normal Bayesian network method. The number of statistically significant interactions for each miRNA and the total number of interactions discovered by SA-BNs and normal BNs. SA-BNs discovered more statistically significant interactions than a normal BN.

BNs are able to discover both strong and subtle interactions while the data show inconsistent patterns through available samples.

To determine whether the unique set of mRNAs discovered by SA-BNs is biologically relevant to EMT, we inquired IPA the different sets of mRNAs discovered by SA-BNs and normal BNs. It shows that the number of mRNA uniquely discovered by SA-BNs is more than that of the normal BNs in terms of EMT relevant functions, including the EMT functional markers (Table 4). It suggests that SA-BNs capture more EMT relevant miRNAmRNA interactions compared with normal BNs.

## Discussion

In the past few years, the identification of miRNAs and their targets has made significant progress. Current focus is shifting to the elucidation of miRNA functions. However, some specific features of miRNAs, for example their small size, abundance of repetitive copies and mode of action, pose several challenges in studying of miRNA functions [48]. miRNAs show diverse regulatory mechanisms with mRNAs. They have been known to down-regulate target mRNAs in the majority of cases. The up-regulation of miRNA also has been reported recently [17,18], and even down- and up-regulations depending on physiological conditions [17]. The various observations of miRNA regulation make it difficult to generalize simple rules for miRNA-mRNA interactions, especially under different physiological conditions. Most previous work has studied the discovery of down-regulatory modules of miRNAs and mRNAs by computational methods [22,25]. The up-regulatory and mix-regulatory mechanisms of miRNAs have not been identified from existing data. However, the discovery of up- and mix-regulatory mechanisms reveal the complex interactions of miRNAs and mRNAs, such as indirect regulations. Considering that most biological experiments have been designed for a comparative study, such as normal versus malignant, down- and up-regulatory mechanisms, especially featuring in the different phe- notypes, conditions, or treatment groups, are of great interest to medical researchers.

In this work, we propose a new Bayesian network structure learning method to explore all types of miRNAmRNA interactions by using heterogeneous information. Much research has been done to discover the gene regulatory networks with BNs on homogeneous data, for instance, microarray data or protein data, but not much work has been done to discover the interactions between miRNAs and mRNAs. Apart from making use of heterogeneous information such as miRNA-target binding, expression profiles of miRNAs and mRNAs, and sample categories, an innovation of the proposed method is to design a splitting and averaging scheme for Bayesian structure learning to discover up- and down-regulatory mechanisms of miRNAs. In addition, small sample size is a problem for reliable discoveries. We use bootstrapping and a statistical model to obtain reliable probability estimation of interactions discovered by SA-BNs.

Bootstrapping alleviates the overfitting problem which is common for machine learning on small size of data sets. The false discovery is well controlled by bootstrapping and the constraint of miRNA-target prediction.

The proposed method finds many regulatory mechanisms that have been supported by previous research. For example, the discovery of the miR-200 family targeting ZEB1 and ZEB2 for EMT has experimentally validated in previous research [28,29,46]. Other discoveries are also very promising. For instance, the results of SA-BNs show LOX widely interacts with the miR-200 family for EMT. It is consistent with previous research which suggests LOX regulates EMT [47]. In addition, the significant number of identified mRNAs have biological functions in EMT, especially the marker functions of EMT like migration, invasion, and scattering. It suggests that SA-BNs have captured many mRNAs and their interactive miRNAs participating in EMT. Furthermore, many molecular networks participated in by identified mRNAs are highly relevant to EMT,

Table 4: Comparison of results between SA-BNs and normal BNs


The number of mRNA uniquely discovered by SA-BNs is more than that of the normal BNs in terms of EMT relevant functions, including the EMT functional markers denoted by *.

suggesting that the pathways of identified mRNAs may also be regulated by the miR-200 family.

The regulatory networks from our method reveal more mRNAs co-regulated by multiple miRNAs than a normal Bayesian network does. Multiple interactions are consistent with the current view of complex regulatory mechanism of miRNAs. Though there is no direct evidence to support the discovered up-regulatory and mix- regulatory mechanisms for EMT from previous research, this work indicates that there are many of such interactions supported by data at statistically significant levels. One reason is that little research has been conducted on this new area yet. These differentially regulatory mechanisms among different conditions are of great interest. We expect they can be validated by biological experiments in the near future.

## Conclusions

In this study, we have proposed a method to explore the complex miRNA-mRNA interactions with Bayesian networks by a splitting-averaging strategy. It is designed to discover both strong and subtle interactions from expression profiles of miRNAs and mRNAs under the constraints of a putative targeting database. Several issues of BNs have been addressed, including integration of heterogeneous data, constraints of the BNs structures with prior knowledge, overfitting, and model integration with splitting and averaging. The analysis of EMT data sets shows that SABNs discover more biologically relevant miRNA-mRNA interactions compared to normal BNs. Some discoveries have been validated by previous research. Some are consistent with the literature. Some are statistically significant interactions that are novel and worthy of validation by biological experiments in the near future.

## Authors' contributions

BL and JYL conceived of this research. BL designed and performed the experiments. AT, AG, and GG provided the miRNA data and validated the results. LL verified the mathematical model. BL and JYL drafted the manuscript. All authors read and approved the final manuscript.

## Additional material

## Additional file 1

Differentially expressed miRNAs and mRNAs. Welch t-statistics with 10,000 times permutation is used to identified differentially expressed miRNAs and mRNAs. The selected miRNAs and mRNAs are highlighted. Probe names, miRNA names, test statistic, p-values and Benjamini and Hochberg adjusted p-values are listed.
Click here for file
[http://www.biomedcentral.com/content/supplementary/1471-2105-10-408-S1.XLS]

## Additional file 2

Significant miRNA-mRNA interactions identified by SA-BNs. SA-BNs identify 231 statistically significant interactions which comprise 127 unique mRNAs and 6 miRNAs for EMT. miRNA-mRNA pairs, confidence, Pearson's correlation coefficients of miRNA-mRNA pairs within and across sample categories are listed.
Click here for file
[http://www.biomedcentral.com/content/supplementary/1471-2105-10-408-S2.XLS]

## Additional file 3

The biological functions participated in by identified mRNAs. In the results identified by SA-BNs, a significant number of mRNAs associate with these EMT functional makers (highlighted in the table). It suggests that SA-BNs captured many mRNAs and their interactive miRNAs participating in EMT.
Click here for file
[http://www.biomedcentral.com/content/supplementary/1471-2105-10-408-S3.XLS]

## Additional file 4

Significant miRNA-mRNA interactions identified by normal BNs. Normal BNs identify 98 statistically significant interactions which comprise 84 unique mRNAs and 6 miRNAs for EMT. miRNA-mRNA pairs, confidence, Pearson's correlation coefficients of miRNA-mRNA pairs within and across sample categories are listed.
Click here for file
[http://www.biomedcentral.com/content/supplementary/1471-2105-10-408-S4.XLS]

## Acknowledgements

This research has been supported by ARC DP0559090.

## Publish with Bio Med Central and every

scientist can read your work free of charge
"BioMed Central will be the most significant development for disseminating the results of biomedical research in our lifetime."

Sir Paul Nurse, Cancer Research UK
Your research papers will be:

- available free of charge to the entire biomedical community
- peer reviewed and published immediately upon acceptance
- cited in PubMed and archived on PubMed Central
- yours - you keep the copyright

Submit your manuscript here:
http://www.biomedcentral.com/info/publishing_adv.asp
BioMedcentral