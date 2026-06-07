# BMC Bioinformatics 

## Proceedings

## Identification of temporal association rules from time-series microarray data sets

Hojung Nam ${ }^{1}$, KiYoung Lee ${ }^{2}$ and Doheon Lee* ${ }^{1}$


#### Abstract

Address: ${ }^{1}$ Department of Bio and Brain Engineering, KAIST, 373-1 Guseong-dong, Yuseong-gu, Daejeon, Korea and ${ }^{2}$ Department of Bioengineering University of California at San Diego, La Jolla, California 92093, USA Email: Hojung Nam - hjnam@kaist.ac.kr; KiYoung Lee - kiylee@bioeng.ucsd.edu; Doheon Lee* - dhlee@kaist.ac.kr * Corresponding author


[^0]
## Abstract

Background: One of the most challenging problems in mining gene expression data is to identify how the expression of any particular gene affects the expression of other genes. To elucidate the relationships between genes, an association rule mining (ARM) method has been applied to microarray gene expression data. However, a conventional ARM method has a limit on extracting temporal dependencies between gene expressions, though the temporal information is indispensable to discover underlying regulation mechanisms in biological pathways. In this paper, we propose a novel method, referred to as temporal association rule mining (TARM), which can extract temporal dependencies among related genes. A temporal association rule has the form [gene $A^{\mathrm{T}}$, gene $B \downarrow$ ] $\rightarrow(7 \mathrm{~min})$ [gene $C^{\mathrm{T}}$ ], which represents that high expression level of gene $A$ and significant repression of gene $B$ followed by significant expression of gene $C$ after 7 minutes. The proposed TARM method is tested with Saccharomyces cerevisiae cell cycle time-series microarray gene expression data set.
Results: In the parameter fitting phase of TARM, the fitted parameter set [threshold $= \pm 0.8$, support $\geq 3$ transactions, confidence $\geq 90 \%$ ] with the best precision score for KEGG cell cycle pathway has been chosen for rule mining phase. With the fitted parameter set, numbers of temporal association rules with five transcriptional time delays ( $0,7,14,21,28$ minutes) are extracted from gene expression data of 799 genes, which are pre-identified cell cycle relevant genes. From the extracted temporal association rules, associated genes, which play same role of biological processes within short transcriptional time delay and some temporal dependencies between genes with specific biological processes are identified.
Conclusion: In this work, we proposed TARM, which is an applied form of conventional ARM. TARM showed higher precision score than Dynamic Bayesian network and Bayesian network. Advantages of TARM are that it tells us the size of transcriptional time delay between associated genes, activation and inhibition relationship between genes, and sets of co-regulators.


[^0]:    (c) 2009 Nam et al; licensee BioMed Central Ltd.

    This is an open access article distributed under the terms of the Creative Commons Attribution License (http://creativecommons.org/licenses/by/2.0), which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.

## Background

The genome of an organism plays a central role in the control of cellular processes such as genetic regulation, metabolic pathway, and signal transduction. Because these processes are very complex and comprised of many genetic interacting elements, it is hard to discover those interacting elements in the complex biological regulations. Since microarray technique allows researchers to simultaneously observe the expression levels of thousands of genes in a single experiment, there have been many studies to discover global genetic regulation from microarray gene expression data by using various computational methods to uncover the hidden roles of genetic elements, such as clustering techniques to identify clusters of co-expressed genes [1-3], network inference techniques to construct the genome-wide regulatory network models [4-9].

One of the most challenging problems in analyzing gene expression data is to determine how the expression of any particular gene might affect the expression of other genes. To find the relationships among different genes, an association rule mining (ARM) method has been applied to gene expression data set because the method can identify associations among genes even when the genes are not coexpressed [10-14]. An association rule has the form LHS (Left Hand Side) $\rightarrow$ RHS (Right Hand Side), where LHS and RHS are sets of items, and it represents that the RHS set being likely to occur whenever the $L H S$ set occurs. In case of analyzing gene expression data, the items in an association rules are represented as genes, which are highly expressed or highly repressed. An example of an association rule from gene expression data might be [gene $A \uparrow$, gene $B \downarrow] \rightarrow[$ gene $C \uparrow]$, which represents that when gene $A$ is measured as highly expressed and gene $B$ is highly repressed then it is also likely to observe and gene $C$ is highly expressed. From the result of the ARM method, it is possible to discover interactions between correlated expressions of genes in microarray experiments. Despite of the usefulness of ARM [12], the time dependency between associated genes cannot be extracted by using the conventional ARM method even though the temporal information is indispensable to discover regulation mechanisms.

Previous studies, which identify time-dependent regulatory relations among genes can be grouped into two general categories. The first approach constructs cellular dynamic models to observe the response of cells by using dynamic Bayesian network (DBN) [15-18] and ordinary differential equation (ODE). However, these approaches have fundamental problems: They need a huge amount of computational time to infer the temporal dependency among genes and show relatively low accuracies analyzing in microarray gene expression data $[16,18]$. These draw-
backs are mainly caused by the fact that the currently available time-series microarray data is not suited for such complex models of genetic regulation. Most of microarray gene expression data sets have relatively small number of experiments compared to the number of genes and they have relatively large regular time intervals between experiment time points. The second approach identifies pairwise temporal dependency between genes by clustering with local patterns of gene expression [19], by measuring the Pearson correlation coefficient of two genes, by detecting the major changes in expression level [20], by scoring the expression patterns with several defined events [21], and by matching the expression patterns with shifted patterns [2,3]. Although such methods can identify pair-wise temporal relations, it cannot identify combinatorial temporal relations which are regarded an important characteristic of regulation [22,23]. For example, the meaning of [gene $A$, gene $B] \rightarrow(7 \mathrm{~min})$ [gene $C]$, and [gene $A] \rightarrow(7$ min ) [gene C] 'AND' [gene B] $\rightarrow(7 \mathrm{~min})$ [gene C] is completely different: In the case of [gene $A$, gene $B] \rightarrow(7 \mathrm{~min})$ [gene C], gene $A$ and gene $B$ play a role as combinatorial regulators in a single regulation. On the other hand, [gene $A] \rightarrow(7 \mathrm{~min})$ [gene $C]$ AND [gene $B] \rightarrow(7 \mathrm{~min})$ [gene $C]$, gene $A$ and gene $B$ are independent regulators.

Even though there are some previous studies related to extraction of association rules from time series data in other application domains [24,25], they do not provide temporal dependencies among items within different time (e.g. time shifted, time delayed). To address the problem, we propose a new mining method for gene expression data sets, which can extract temporal dependency among genes by applying temporal association rule mining (TARM) method. The temporal association rules represent various transcriptional time delays between associated genes. An example of a temporal association rule is [gene $A \uparrow$, gene $B \downarrow] \rightarrow(7 \mathrm{~min})$ [gene $C \uparrow]$, which represents that high expression level of gene $A$ and significant repression of gene $B$ followed by significant expression of gene $C$ after 7 minutes. Hence, the temporal association rule can tell us the size of transcriptional time delay ( 7 minutes) between associated genes (gene $A$, gene $B$ and gene $C$ ), activation and inhibition relationship (gene $A \uparrow \rightarrow$ gene $C \uparrow$ ), and sets of co-regulators (gene $A \uparrow$, gene $B \downarrow$ ).

The overall process of the proposed method is depicted in Figure 1. The proposed method consists of two main phases. First, temporal association rule mining phase. With an obtained fitted parameter set, the steps of temporal association mining method is applied to time-series gene expression data: (i) converting gene expression values into discrete values, (ii) generating temporal transaction sets with various sizes of transcriptional time delay $\Delta$, (iii) generating temporal frequent item sets, (iv) and finally, extracting temporal association rules. The pro-

![img-0.jpeg](img-0.jpeg)

Figure I
Method overview. (a) The overall phase of proposed method. (b) Parameter fitting phase.
posed method is tested with public microarray experiments of Saccharomyces cerevisiae cell cycle alpha factor arrest synchronization data set. Second, parameters fitting phase. In this phase, external known regulation information (KEGG cell cycle regulation information) is used to choose the best parameter set from all possible combinations of parameter sets. Three parameters are selected for the proposed temporal association rule mining (TARM) method. Among every possible combination of three parameter values, the best parameter set that has the highest overlap degree with previously known biological regulation relationships is selected as the fitted parameter set.

## Methods

## Conventional association rule mining (Apriori algorithm)

To explain the basic concepts of association rule mining, we use the definitions and the examples of supermarket data shown in [26]. Consider a small store that sells the following set of items: [Bagels, Bread, Butter, Cereal, Juice, Milk]. List of items bought by six hypothetical customers
are shown in Table 1. This table will be used to illustrate the concepts presented in this section.

## Definition I

(1) An association rule is a pair of disjoint item sets. If $L H S$ (Left Hand Side) and $R H S$ (Right Hand Side) denote the two disjoint item sets, the association rule is written as $L H S \rightarrow R H S$.

Table I: List of items bought by six customers. Each row of the table is referred to as a transaction.


(2) The support of the association rule $L H S \rightarrow R H S$ with respect to a transaction set $T$ is the support of the item set $L H S \cup R H S$ with respect to $T$.
(3) The confidence of the rule $L H S \rightarrow R H S$ with respect to a transaction set $T$ is the ratio support $(L H S \rightarrow R H S) / \mathrm{sup}-$ $\operatorname{port}(L H S)$.

## Example

Consider the item sets $\mathrm{A}_{1}=$ [Juice, Milk] and $\mathrm{A}_{2}=$ [Cereal]. Since $A_{1}$ and $A_{2}$ are disjoint, $A_{1} \rightarrow A_{2}$ (or equivalently, [Juice, Milk] $\rightarrow$ [Cereal]) is an association rule. Let $R_{1}$ denote this association rule. The support of $R_{1}$ is the support of the item set [Juice, Milk, Cereal]. From Table 1, it can be seen that this support value is 4 . Also from Table 1, the support of the item set [Juice, Milk] is 6 . Therefore, the confidence of Rule $R_{1}$ is $4 / 6$ or $66.67 \%$.

## Temporal association rule mining (TARM)

In this work, we propose a temporal association rule mining (TARM) method, which is based on Apriori algorithm. Following two sub-sections will explain the detailed methodology of temporal association rule mining phase (Figure 1(b)), and parameter fitting phase (Figure 1(a)).

To explain the concept of the proposed TARM method, we first define new terminologies.

## Definition 2

(1) A temporal item is an item, which has a time stamp.
(2) A temporal item set $\overline{\mathrm{I}}$ is a non-empty set of temporal items.
(3) Given a temporal item set $\overline{\mathrm{I}}$, a set T of transactions on $\overline{\mathrm{I}}$, and a positive integer $\alpha, \overline{\mathrm{I}}$ is a temporal frequent item set with respect to T and $\alpha$ if support $\mathrm{T}(\overline{\mathrm{I}})>=\alpha$. ( $\alpha$ is the support threshold.)
(4) A temporal association rule is a pair of disjoint temporal item sets. If $L H S$ and $R H S$ denote the left and right temporal item sets respectively, then the time stamp of each temporal item in LHS is ahead of those of all temporal items in RHS. A temporal association rule is written as $L H S>(\Delta) R H S$, where $\Delta$ is the interval of different two time stamps.

Figure 2 shows an illustration of temporal association rule mining process. First, continuous gene expression values are converted into discrete values (up, down, and none) (Figure 2(a)). Second, to find temporally associated genes, we first assume that all related genes may have various sizes of transcriptional time delay. Therefore, our method searches associated genes in all possible sets of different time point experiments where the time interval is from 0 to $n$ (Figure 2(b)). In this illustration, $\Delta$ is 2 . For example, Temporal transaction set $t_{0}+t_{2}=\left[g_{1 L}{ }^{\dagger}, g_{2 L} \downarrow\right.$, $\left.g_{1 R}{ }^{\dagger}, g_{2 R}{ }^{\dagger}, g_{3 R} \downarrow\right]$ consists of up or down regulated genes at time stamps $t_{0}$ and $t_{2}$ with the size of transcriptional time delay $\Delta=2$. Note that, for $g_{1}$, it is up regulated in both cases of $t_{0}$ and $t_{2}$, but we marked them as two different genes like $g_{1 L}\left(g_{1}\right.$ in Left hand side) and $g_{1 R}\left(g_{1}\right.$ in Right hand side). Third, Figure 2(c) indicates the extracted temporal frequent item sets with support threshold $50 \%$. And finally, two temporal association rules are discovered with confidence threshold $50 \%$ as shown in Figure 2(d). In this manner, TARM can find (1) various sizes of transcriptional time delay between associated genes, (2) activation and inhibition relationship, (3) sets of co-regulators for the target genes.

## Parameter extraction

This section shows the phase for obtaining three different parameters which are necessary when mining temporal association rules: (1) a cutoff value for binning transcriptional expression values, (2) a support value for mining temporal frequent item sets, and (3) a confidence value for extracting temporal association rules. Since the performance of the proposed method is dependent on the parameter set, the parameter set should be chosen very carefully. If the ground truths of cell cycle regulation are known, the regulation information can be used to fit the


(a) Binned time-series data, with 3 genes and 6 time points

$$
\begin{aligned}
& t_{0}+t_{1}=\left\{g_{1 L}{ }^{\dagger}, g_{1 L} \downarrow, g_{1 R}{ }^{\dagger}, g_{1 R}{ }^{\dagger}, g_{3 R} \downarrow\right\} \\
& t_{1}+t_{2}=\left\{g_{1 L} \downarrow, g_{1 R} \downarrow, g_{1 R} \downarrow\right\} \\
& t_{2}+t_{3}=\left\{g_{1 L}{ }^{\dagger}, g_{1 L} \uparrow, g_{2 L} \downarrow, g_{1 R}{ }^{\dagger}, g_{1 R}{ }^{\dagger}\right\} \\
& t_{3}+t_{5}=\left\{g_{1 L} \downarrow, g_{2 L} \downarrow, g_{3 R} \downarrow\right\} \\
& t_{4}+t_{6}=\left\{g_{1 L}{ }^{\dagger}, g_{2 L}{ }^{\dagger}, g_{3 R}{ }^{\dagger}\right\}
\end{aligned}
$$

(b) Temporal transaction sets, transcriptional time delay $\Delta=2$

$$
\left\{g_{1 L}{ }^{\dagger}\right\},\left\{g_{1 L} \downarrow\right\},\left\{g_{1 R}{ }^{\dagger}\right\},\left\{g_{3 R} \downarrow\right\}
$$

(c) Temporal frequent item sets, support $=50 \%$

$$
g_{1} \uparrow \rightarrow(2) g_{2} \uparrow
$$

(d) Temporal association rules, confidence $=50 \%$

Figure 2
An illustration of temporal association rule mining process. An illustration of temporal association rule mining process with transcriptional time delay $\Delta=2$, support $\geq 50 \%$, confidence $\geq 50 \%$.

Table 2: A summary of precision scores of 70 different parameter sets.


parameters. However, absence of such kinds of information, alternative information source is used. In this study, we utilize KEGG cell cycle regulation path as known information set to find the best parameter set which can extract the most number of accurate temporal association rules. The KEGG cell cycle regulation path is a collection of manually drawn pathway maps representing the regulation knowledge on the molecular interaction, and the pathway contains interaction information which are relevant to cell cycle of yeast [27,28].

The KEGG regulation information is used for a measure of correctness of the extracted candidate rules with various combinations of parameters. If an extracted temporal association rule is matched with KEGG regulation information, then we regard the rule as a correctly extracted rule. Namely, the validation score is calculated by the following equation:

$$ \text { precision }=\frac{(\# \text { of matched rules })}{(\# \text { of extracted rules })} $$

To select a fitted parameter set among the various combinations, we select a parameter set which shows the highest validation score.

## Results and discussion

## Data sets

To check the performance of the proposed method, we used S. cerevisiae cell cycle alpha factor arrest synchronization microarray data set [29]. This time-series microarray data set has 18 time points with relatively small regular time intervals ( 7 minutes) between every sampling time point.

## Fitted parameters

In the parameter fitting phase, combination sets of parameters are generated within binning cutoff values from 0.2 to 1.4 , support cutoff values from 2 to 6 transaction, and confidence cutoff values from 80 to $100 \%$. With these parameter sets, TARM method is applied on cell cycle expression data of 57 genes, which are nodes of KEGG yeast cell cycle regulation pathway. Extracted temporal association rules with every parameter set are validated with KEGG cell cycle regulation information. The precision scores of parameter sets are summarized in Table 2. To determine the best parameter set, extracted rules with several sets of parameters, which show relatively high precision scores are examined (precision scores with 0.25 , 0.28 , and 0.38 ). The temporal association rules extracted with three selected parameter sets are listed in Figure 3. Finally, [threshold $=\pm 0.8$, support $\geq 3$, confidence $\geq 90 \%$ ] set is selected as the fitted parameter set which shows the highest precision score ( 0.38 ). Although the precision score of the fitted parameter set seems not significant, the score is satisfactory in the case of microarray analysis. Because it is reported that when inferring linkages of regulatory proteins in KEGG pathway only from microarray gene expression data set, the accuracy of inferred results were not high owing to the property of microarray itself [30]. Furthermore, we compared the results with Dynamic Bayesian Network (DBN) and Bayesian Network (BN) inference methods. We used the 'G1DBN' package implemented in R for DBN, and we used the 'deal' package implemented in R for BN inference. The result of DBN is optimized for the precision score after exploring possible combinations of parameters. The precision and recall scores of BN are obtained after model averaging. The results of proposed method, DBN, and BN are summarized in Table 3. When comparing precision scores, the proposed method achieved the best performance. However, the proposed method still shows poor recall score like recall scores from two previous methods.

Table 3: A summary of precision and recall scores of three methods.


![img-1.jpeg](img-1.jpeg)

$=0.25$ | 7 / 18
$=0.38$  |
$=0.070$ | 7/99
$=0.070$  |

Figure 3 Extracted temporal association rules with the selected three parameter sets. Best three parameter sets are selected to compare results of extracted rules on cell cycle expression data of 57 genes with association delay $0 \sim 28$ minutes. Set $A=$ [threshold $= \pm 0.8$, support $\geq 3$ transactions, confidence $\geq 80 \%$ ], set $B=[t h r e s h o l d= \pm 0.8$, support $\geq 3$ transactions, confidence $\geq 90 \%$ ], set $C=$ [threshold $= \pm 1.0$, support $\geq 3$ transactions, confidence $\geq 80 \%$ ]. The intersection area of a Venn diagram stands for the commonly extracted rules with different parameter sets. Rules written in Italic font denote known regulation relations in KEGG Cell cycle pathway data.

## Extracted temporal association rules with fitted parameters

Using the selected parameter set, we applied TARM method to 799 genes which are pre-identified as cell cycle relevant genes in [29] and extracted numbers of temporal association rules with various sizes of transcriptional time delay. To test the significance of the temporal association rules, TARM is also applied to random shuffled cell cycle expression data of 799 genes. Figure 4 is the comparison result of both the real cell cycle data set and the shuffled cell cycle data set. As the Figure shows, the extracted numbers of rules from real cell cycle data set and random data set are comparably different. The results indicate that temporal association rules extracted by our proposed method are more significant than random rules.

From the extracted temporal association rules, rules with significant support ( $S \geq 5$ ) are chosen for further Gene Ontology (GO) term [31] analysis and represented in a directed graph structure (Figure 5). By this analysis, interesting features are found. First, associated genes, which play same role of biological phase with relatively short transcriptional time delay are identified. For example, HTB2, HTA2, HHF1, HHT1, HTB1, HTA1, HHF2, and HHT2 those who share same annotation term (Organelle organization and biogenesis, DNA metabolic process) are complexly associated with one another within $0 \sim 7$ min-
![img-2.jpeg](img-2.jpeg)

Figure 4
The number of extracted temporal association rules from cell cycle data set and random data set. The graph shows the number of extracted temporal association rules in five transcriptional time delays ( $0,7,14,21,28$ minutes) from time-series gene expression of 799 cell cycle relevant genes and random shuffled cell cycle data set [threshold $= \pm 0.8$, support $\geq 3$ transactions, confidence $\geq 90 \%$ ]. Black bar indicates the number of extracted rules in real data set and gray bar stands for the average number of extracted rules of 100 times of random tests.
utes and these associated genes are known as having protein interactions with each other. HTA1 interacts with HTA2 [32], HTB1 [33], HTB2 [34,35], HFF1[33], HHT1 [34-36]. HTA2 interacts with HHF1 [37], HHT1[32], HHT2 [32], HTA1 [32], HHF2 [32]. Second, some temporal dependencies between genes with specific biological processes are detected. Like POL30, YLR183C (RNA metabolic process, Transcription, Cell cycle) and HTA1, HTA2, HTB1, HHF2 (Organelle organization and biogenesis, DNA metabolic process) have temporal association with $\Delta=14$ minutes. PIR1, PIR3 (Cell wall organization and biogenesis) and HTB2 (Organelle organization and biogenesis, DNA metabolic process) are temporally associated with $\Delta=21$ minutes.

## Conclusion

We developed the TARM method that can extract temporal association rules in time-series gene expression data, and validated the proposed method with yeast cell cycle gene expression data set. A temporal association rule can describe how the expression of one gene might be associated with the expression of other genes with the related temporal dependency.

In the parameter fitting phase, the best parameter set (threshold $= \pm 0.8$, support $\geq 3$ transactions, confidence $\geq$ $90 \%$ ), which extracted the most number of correct associations in KEGG cell cycle pathway among 70 combinations of parameters, has been chosen for rule mining. Furthermore, when comparing the precision scores between TARM (0.38), Dynamic Bayesian network (0.045) and Bayesian network (0.16), TARM method showed the best performance. With the best parameter set, numbers of temporal association rules are extracted among pre-identified 799 cell cycle relevant genes. From the extracted temporal association rules, temporally associated genes, which play same role of biological processes (Organelle organization and biogenesis, DNA metabolic process) with short transcriptional time delay, and some temporal dependencies between genes with specific biological processes are detected. The strong points of our method are the detection abilities of (1) various sizes of transcriptional time delay between associated genes, (2) activation and inhibition relationship, (3) sets of co-regulators for the target genes.

## Competing interests

The authors declare that they have no competing interests.

## Authors' contributions

HN designed the study, implemented the application, performed experiments, and wrote the manuscript. KL participated in the design of the study and performed the result analysis. DL conceived of the study, and participated in its design and coordination and helped to draft

![img-3.jpeg](img-3.jpeg)


Figure 5
Validation of the extracted temporal association rules. Extracted temporal association rules with high support (support $\geq 5$ ) are represented in network structure (upper). A solid pointed arrow edge indicates 'up $\rightarrow$ up' relation; a solid blunt arrow indicates 'down $\rightarrow$ up'; a dashed pointed arrow indicates 'down $\rightarrow$ down'; a dashed blunt arrow indicates 'up $\rightarrow$ down' relation. Nodes in grey denote genes whose biological function is known. Nodes in white stand for genes whose biological function is not discovered yet. The numeric value on each edge stands for transcriptional time delay $(\Delta)$ between genes. Biological process annotation terms of genes represented in network are summarized in Table.

the manuscript. All authors read and approved the final manuscript.

## Acknowledgements

This work was supported by the Korean Systems Biology Program (No. M10309020000-03B5002-00000) and the National Research Lab. Program (No. 2006-01508) from the Ministry of Education, Science and Technology through the Korea Science and Engineering Foundation. We would like to thank CHUNG Moon Soul Center for BioInformation and BioElectronics for providing research facilities.

This article has been published as part of BMC Bioinformatics Volume 10 Supplement 3, 2009: Second International Workshop on Data and Text Mining in Bioinformatics (DTMBio) 2008. The full contents of the supplement are available online at http://www.biomedcentral.com/1471-2105/10?issue=S3.
