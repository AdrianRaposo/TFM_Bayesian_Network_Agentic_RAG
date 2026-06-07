# A nucleosomal approach to inferring causal relationships of histone modifications 

Ngoc Tu Le ${ }^{1 *}$, Tu Bao $\mathrm{Ho}^{1}$, Bich Hai $\mathrm{Ho}^{2}$, Dang Hung Tran ${ }^{3}$<br>From The Twelfth Asia Pacific Bioinformatics Conference (APBC 2014)<br>Shanghai, China. 17-19 January 2014


#### Abstract

Motivation: Histone proteins are subject to various posttranslational modifications (PTMs). Elucidating their functional relationships is crucial toward understanding many biological processes. Bayesian network (BN)-based approaches have shown the advantage of revealing causal relationships, rather than simple cooccurrences, of PTMs. Previous works employing BNs to infer causal relationships of PTMs require that all confounders should be included. This assumption, however, is unavoidably violated given the fact that several modifications are often regulated by a common but unobserved factor. An existing non-parametric method can be applied to tackle the problem but the complexity and inflexibility make it impractical.


Results: We propose a novel BN-based method to infer causal relationships of histone modifications. First, from the evidence that nucleosome organization in vivo significantly affects the activities of PTM regulators working on chromatin substrate, hidden confounders of PTMs are selectively introduced by an information-theoretic criterion. Causal relationships are then inferred from a network model of both PTMs and the derived confounders. Application on human epigenomic data shows the advantage of the proposed method, in terms of computational performance and support from literature. Requiring less strict data assumptions also makes it more practical. Interestingly, analysis of the most significant relationships suggests that the proposed method can recover biologically relevant causal effects between histone modifications, which should be important for future investigation of histone crosstalk.

## Background

Genomes of higher organisms are organized into chromatin, a condensed structure of nucleosome units. Each of these units comprises a short piece of DNA wrapping around an octamer histone, containing two proteins of each type: H2A, H2B, H3, and H4 [1]. The histone protein is subject to various biochemical modifications, a.k.a. posttranslational modifications (PTMs), which have been shown to play crucial roles in many cellular processes, such as transcription and replication [2]. Defects of PTMs have also been implicated in determining cell fate and oncogenesis [3,4]. The facts that PTMs may cause combinatorial effects on downstream events, and, by forming stable chromatin domains, properly pass modified states

[^0]to the next generation [5,6] suggest the existence of "histone codes" [7]. Therefore, revealing genome-wide PTM patterns and related functional implications would help increase our understanding of different DNA-mediated processes. For example, [8] discovered a common modification module of 17 modifications in human, suggesting their critical roles in gene regulation.

Advances in profiling techniques, such as ChIP-Chip and ChIP-Seq, have enabled the availability of genomescale PTM data $[8,9]$, thus providing an unprecedented opportunity to decipher histone codes and their associated cis-regulatory elements. However, it also poses a great requirement for methods to understand such data. Many methods, ranging from clustering- to Hidden Markov Model (HMM)- to Bayesian network (BN)based, have been developed to identify histone modifications patterns from ChIP-Chip and ChIP-Seq data

[^1]
[^0]:    ${ }^{1}$ Japan Advanced Institute of Science and Technology, 1-1 Asahidai, Nomi, Ishikawa 923-1292, Japan
    Full list of author information is available at the end of the article

[^1]:    (c) 2014 Le et al.; licensee BioMed Central Ltd. This is an Open Access article distributed under the terms of the Creative Commons Attribution License (http://creativecommons.org/licenses/by/2.0), which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited. The Creative Commons Public Domain Dedication waiver (http:// creativecommons.org/publicdomain/zero/1.0/) applies to the data made available in this article, unless otherwise stated.

[10-14]. Among them, BN-based approaches may help discover not only the cooccurrence but also the causal relationships of histone modifications [15]. This is especially important to understand histone crosstalk, a phenomenon that often occurs among different PTM events [16-18].

Bayesian network is a family of graphical models representing conditional independence of multiple variables [19]. First introduced to model gene regulatory networks (GRNs) from expression data [20], it has been widely used in reconstructing various biological networks, such as protein-protein interactions, protein signaling networks [21-23]. Likewise, there have been attempts to employ BNs to analyze histone modification data, in which compelled edges of the resulting models were considered causal relationships between PTMs [14,24,25]. Though useful, these works have a significant drawback: they require causal sufficiency assumption, i.e., all confounders of PTMs should be observed [26,27]. This assumption, however, is unavoidably violated given the fact that some modifications can be regulated by enzymatic activity of a common but unobserved modifier [2].

Therefore, in order to reveal causal relationships of PTMs the existence of hidden confounders should be taken into account. Basically, there are two choices for network topology containing hidden confounders: overlapping and hierarchical [28]. In the overlapping (Figure 1a), each hidden variable is a parent of several observed variables, and several hidden variables can share a common observed variable as their child. In the hierarchical (Figure 1b), hidden variables form a tree structure, in which each of them is a parent of several other variables (either observed or hidden) and serves to capture the dependencies among its children and between its children and other nodes in the network. Biological evidences have showed that some modifications can be regulated by a common regulator and vice versa [2,29]. Overlapping topology, therefore, is more suitable to describe the relationships between PTMs and their hidden regulators. Thus, the problem of learning network models representing causal relationships of PTMs can be formulated as learning two adjacency matrices, one
representing the relationships among observed variables (PTMs), denoted as $X$, and the other representing the relationships between PTMs and their hidden causes, denoted as $Z$, as proposed by [30]. However, their nonparametric approach to learning the models requires strict data assumptions and employs a time-consuming procedure to infer $Z$. These drawbacks make it inflexible and inefficient in practice.

In this work, we propose a novel BN-based method to infer causal relationships of PTMs that accounts for the existence of hidden confounders. First, an informationtheoretic criterion is proposed to selectively introduce a pairwise hidden confounder (PHC) for each pair of PTMs. General hidden confounders (GHCs) are then derived from PHCs. The idea of deriving GHCs from PHCs has been presented in [31] to learn two-layer BNs with hidden variables. Differently, we based our approach on the evidence that chromatin in vivo imposes regulatory effects on the activities of PTM regulators. Thus, the criterion is proposed exploiting information about chromatin structure, i. e., nucleosome positioning. Matrix $X$ is separately learned by a BN structure learning method. Compelled edges, i.e., causal relationships, are then derived from a network model of both PTMs and GHCs. Application on human epigenomic data of 38 histone modifications and histone variant H 2 A .Z , shows that the proposed method outperformed the non-parametric ( $N p$ ) and the traditional one, which does not account for hidden confounders (noHidden), in terms of computational performance and literature support. Moreover, analysis of the most significant relationships shows that the proposed method can recover biologically relevant causal effects between histone modifications, such as $H 3 K 27 M e 3 \rightarrow H 3 K 9 M e 3, H 3 K 4 M e 3 \rightarrow$ $H 2 A K 5 A c, H 4 K 8 A c \rightarrow H 2 A Z$. This is important for future investigation of histone crosstalk.

## Methods

## Information theory

Mutual information (MI) has been increasingly used in reverse engineering, especially to reconstruct GRNs [32-35]. It is a more general measure compared to correlation in estimating the dependency between two
![img-0.jpeg](img-0.jpeg)

variables. Given two random variables, $x$ and $y$, MI is computed by:

$$
M I(x, y)=\iint p(x, y) \log \frac{p(x, y)}{p(x) p(y)} d x d y
$$

where $p(x, y), p(x)$, and $p(y)$ are joint density function and marginal density functions of $x$ and $y$, respectively.
Likewise, conditional mutual information (CMI) is introduced to measure conditional dependency between two variables given the other(s). CMI of $x$ and $y$ given $\mathbf{z}$ (uni- or multi-variate) is computed by:

$$
\operatorname{CMI}(x, y \mid \mathbf{z})=\iiint p(x, y, \mathbf{z}) \log \frac{p(x, y \mid \mathbf{z})}{p(x \mid \mathbf{z}) p(y \mid \mathbf{z})} d x d y d \mathbf{z}
$$

If $x, y, \mathbf{z}$ are discrete variables, the integrals are replaced by the sum over all of their values. It is, however, difficult to compute the integrals given the limited number of samples in general cases. Thus, in practice, probability density functions are often approximated by density estimation methods. Given N samples of a variable $\mathbf{x}$, density function can be approximated by:

$$
\hat{p}(\mathrm{x})=\frac{1}{N} \prod_{i=1}^{N} \delta\left(\mathrm{x}-\mathrm{x}_{i}, h\right)
$$

where $\delta($.$) is the Parzen window function, \mathbf{x}_{i}$ is the $i$ th sample, and $h$ is the window width. In our work, $\delta($.$) was chosen as Gaussian function:$

$$
\delta(\mathbf{z}, h)=\exp \left(-\frac{\mathbf{z}^{T} \Sigma^{-1} \mathbf{z}}{2 h^{2}}\right) /\left\{(2 \pi)^{d / 2} h^{d}|\Sigma|^{1 / 2}\right\}
$$

where $\mathbf{z}=\mathbf{x}-\mathbf{x}_{i}, d$ is the dimension of $\mathbf{x}$, and $\Sigma$ is the covariance matrix of $\mathbf{z}$. When $d=1$, equation (3) returns the estimated marginal density. When $d=2$, it can be used to estimate the joint density function of bivariate variable $(x, y)$. In our work, MI and CMI values were computed using a software package provided by [36].

## Bayesian networks

## Definition

A Bayesian network is a directed graph representing conditional independence of multiple variables by a set of conditional probability distributions [19,37]. Joint
probability distribution of a variable set $\mathbf{x}$ encoded by the model can be factorized as:

$$
p(\mathrm{x})=\prod_{i=1}^{n} p\left(x_{i} \mid \mathbf{P a}_{i}\right)
$$

in which $p\left(x_{i} \mid \mathbf{P a}_{i}\right)$ corresponds to the local probability distribution of variable $x_{i}$, and $\mathbf{P a}_{i}$ are $x_{i}$ 's parents.

## D-separation property

In a BN, there are three fundamental local structures, namely serial, diverging, and converging connections (Figure 2). These structures are associated with a set of rules, which is independent of any particular calculus for certainty, to assess how a change of certainty in one variable may change the certainty for other variables in the networks. These rules form d-separation property of a BN. If two variables are d-separated, change in the certainty of one variable has no impact on the other. Two variables are called d-connected if they are not d-separated [19]. Thus, d-separation property can be used as a general assessment of the dependencies among nodes of a BN.

## BN structure learning

BN structure can be learned by score-based methods, aiming to identify the structure(s) that "best" describe the data. In this work, BDe score [37,38] with uniform prior was used to measure the fitness of a candidate network. Because it is infeasible to search though all possible structures [39], greedy hill-climbing search combined with simulated annealing algorithm to avoid local maxima was employed.

## Criterion for introducing PHCs

It has been widely shown that the binding of chromatin modifiers, and the large multiprotein complexes in which they reside, to chromatin is greatly affected by chromatin structure, i.e., nucleosome organization [7,40-44]. From this observation, the relationships among two PTMs, their hidden regulator(s), and NucPos can be described by two local causal structures, illustrated in Figure 3. The following results can be easily proved based on d-separation properties:

Proposition 1 Consider two PTMs, if each has its own (hidden) regulator, they will be d-separated given evidence on nucleosome positioning.
![img-1.jpeg](img-1.jpeg)

![img-2.jpeg](img-2.jpeg)

Figure 3 Causal structures when two PTMs share a hidden confounder (regulator) (a) or not (b).

Proposition 2 Consider two PTMs, if they share a hidden regulator (in other words, a confounder), their dseparation property does not change upon the availability of nucleosome positioning evidence.

The results suggest that, given evidence on NucPos, the dependency level between two PTMs would not change if they share a hidden confounder, and would change (becoming "less" dependent) if each has its own (hidden) regulator. Using MI and CMI as the measures of dependency levels between two PTMs, we derive the following criterion for introducing a PHC for a pair of modifications, ptm1 and ptm2:

Define Mutual Information Gain (MIG) of two PTMs as:

$$
M I G\left(\text { ptm1, ptm2 }\right)=\left|\text { MI }\left(\text { ptm1, ptm2 }\right)-\text { CMI }\left(\text { ptm1, ptm2 } \mid \text { NucPos }\right)\right|
$$

Then, a PHC is introduced if the following conditions are satisfied:

$$
\left\{\begin{array}{l}
M I G\left(\text { ptm1, ptm2 }\right) \leq \alpha \\
\text { MI }\left(\text { ptm1, ptm2 }\right) \leq \beta
\end{array}\right.
$$

where $\alpha, \beta>0$ are significant thresholds. These criteria will be used to derive PHCs for all pairs of PTMs.

## Derivation of GHCs

From a set of PHCs derived in previous step, we define hidden confounder graph, an undirected graph whose nodes correspond to PTMs and edges to PHCs, implying that two nodes are connected if they share a PHC. Maximal clique algorithm is then applied on this graph, resulting in a set of maximal cliques, each corresponding to a GHC.

## Causal relationship inference

To derive causal relationships of PTMs, we first combine BN received from structure learning step with GHCs, forming a network of PTMs and their hidden confounders. The edges among PTMs that share a GHC are then removed. Finally, the algorithm for finding compelled edges [26] is applied to the resulting structure, producing a set of compelled edges representing causal relationships of PTMs.

## Data

Chromatin modification. CD4+ T cell data containing 20 methylations, 18 acetylations, and histone variant H2A.Z were retrieved from [9] and [8].

Nucleosome positioning data of resting CD4+ T cell was obtained from [45].

Gene set. UCSC Known Genes were retrieved from UCSC Genome Browser [46]. After removing genes with duplicated or without U133P2 probe IDs, 12456 genes were kept for analysis.

## Results

## Derivation of hidden confounders

Tag count profiles of 38 PTMs and histone variant H2A. Z, taken at the promoters (TSS $\pm 1 k b$ ) of 12456 selected genes, were first discretized into 3-category values. Tag count profiles of NucPos were transformed into logarithm scale. Then, all were used to compute MI and MIG values for all pairs of modifications. In Figure 4, the distributions of these values are illustrated in red. Permutation method [47] was employed to evaluate the significance of these distributions. By which, PTM profiles were permuted 1000 times and the distributions of the new MI and MIG values for all pair of PTMs were computed for each permutation. The averages of 1000 permuted MI and MIG distributions are illustrated in blue (Figure 4). The result showed that when MIG $\leq$ 0.0007 and $M I \geq 0.002$, permutation was unable to create any association with the original MIG and MI distributions. The significant thresholds $\alpha$ and $\beta$ were thus assigned to 0.0007 and 0.002 , respectively. This resulted in a hidden confounder graph of 39 nodes and 63 edges. 50 maximal cliques were derived from this graph, corresponding to the same number of GHCs. The list of GHCs and their belonging modifications is given in supplementary information (http://www.jaist.ac.jp/ $\sim$ s1060011/SI.zip). Although it is hard to show that all GHCs are biologically relevant, we did find supporting evidences for some, whose child nodes are well-characterized modifications. For example, CBP is known to have enzymatic activity on both lysines 14 and 27 of histone H3 [2,48], thus may play the role of confounder for H3K14Ac and H3K27Ac. The same observations were also reported for histone acetyltransferase GCN5, which may be the confounder of H3K14Ac and H3K36Ac [2,49], or of H3K4Ac and H3K14Ac [2,50]. Also, JMJD2C/GASC1 or JMJD2A/JHDM3A may be confounder of H3K9 and H3K36 methylation, though histone methyltransferases often target to specific residues [2].

![img-3.jpeg](img-3.jpeg)

## Inference of PTM causal relationships

## General scheme

BN structures were learned by Banjo (http://www.cs. duke.edu/ amink/software/banjo/), limited to 1, 300, 000 iterations because no significant improvement was achieved in further iteration (data not shown). The resulted structures were combined with 50 GHCs derived in previous step to produce a set of causal relationships. Significance scores were evaluated by bootstrapping method [20]. By which, original data was randomly bootstrapped $N$ times, generating $N$ bootstrapped datasets, and a set of causal relationships was derived for each. Significance score of each relationship was defined as the frequency of its appearance in $N$ bootstrapped sets. In our experiment, $N$ was set to 100 .

For comparison, the implementation of $N p$ by [30] was run on the same data. Because it only works with binary variables, the data were discretized into binary values by three schemes, using 70 (Scheme 1), 80 (Scheme 2), and 90 (Scheme 3) percentiles as thresholds. After receiving hidden confounders, the above procedure was employed to generate three sets of causal relationships, corresponding to each scheme.

## Comparison

## Performance

Table 1 presents the running time and number of hidden confounders derived by the two methods when running on a server machine (Intel Xeon X5570 2.93GHz (4 CPUs), 6GB RAM, Windows Server 2008 OS). It shows that, our method (denoted as hidden) worked faster than $N p$ (converged after $\approx 200$ iterations, data not shown) no matter what discretization scheme was employed. Moreover, to compute MIs and MIGs, it does not require any additional assumption on input data, thus more flexible and practical.

## Literature-based comparison

Because it does not exist a list of confirmed causal relationships that could be used as a "gold standard", we resorted to literature to compare the results given by different methods. Biomedical literature represents almost all of our existing knowledge about biological entities and their relationships. For the analysis presented here, we employed a simple but effective way to derive potential associations between PTMs from literature, the cooccurrence approach, which was previously applied for GRN reconstruction [51-53]. Simply, if two PTMs appear in an article abstract indexed in PubMed, we assume an association between them. However, in addition to the associations extracted based on direct cooccurrence, we also assume an association between two PTMs if they share some directly associated biomedical concepts. This assumption is based on the fact that PTMs often functionally interact with each other

Table 1 Performances of Np and our method.


#Confounders is the number of hidden confounders.

through intermediary proteins [2,54]. To extract these indirect "associations" we employed FACTA+ [55], a state-of-the-art biomedical text mining system which supports both directly and indirectly related (pivot and target, respectively, so called in FACTA+) biomedical term search. Thus, two kinds of literature-based PTM associations were derived with the association weight defined as following. Regarding cooccurrence-based association, we took the weight definition from [52]:

$$
w_{C_{o}}\left(p t m_{1}, p t m_{2}\right)=\frac{\operatorname{freq}\left(p t m_{1}, p t m_{2}\right)}{\max \left\{\operatorname{freq}\left(p t m_{1}\right), \operatorname{freq}\left(p t m_{2}\right\}\right\}}
$$

in which freq $(p t m 1, p t m 2)$ is the frequency that both PTM terms appear together in PubMed abstracts, and freq $\left(p t m_{i}\right)$ is the frequency of each individually.

Regarding indirect association based on shared pivot concepts, i.e., proteins/genes in this case:

$$
w_{I_{o}}\left(p t m_{1}, p t m_{2}\right)=N \times \frac{1}{\sqrt{\sum_{i=1}^{N}\left(s i g_{1_{i}}-s i g_{2_{i}}\right)^{2}}}
$$

in which $N$ is the number of the most significant shared concepts between two PTMs, $\operatorname{sig}_{1 i}$ and $\operatorname{sig}_{2 i}$ are the significant levels, assigned as point-wise mutual information values, of the associations between the ith shared concept and the two PTMs. All of these were retrieved through FACTA+ search with the list of the search terms given in supplementary information.

We define a measure, named literature support, for comparison purpose. It is the sum of literature-derived weights of $N$ most significant associations (edges) of a resulting model $M$ :

$$
L S_{M}(N)=\sum_{i=1}^{N} w\left(e_{i}\right)
$$

where $w\left(e_{i}\right)$ is the literature-derived weight of the edge $e_{i}(i=1 \cdots N)$. Figure 5 illustrates literature supports for the top 50 significant relationships given by three methods. It shows that, in case of both direct (left figure) and indirect (right figure) associations, the most significant relationships given by our method have comparable literature support to the ones given by noHidden, and both are better than the result given by $N p$.

An alternative way for comparison is to assess the significance scores of PTM pairs previously reported as highly correlated [52]. [11] developed a biclustering method to search for combinatorial patterns of PTMs on the same data. From the resulting bilusters, they found three most frequently cooccurred PTM pairs: (H3K27Ac, H3K4Me3), (H2AZ, H2BK120Ac), and (H3K9Ac, H3K36Ac). Also, we selected 10 most correlated PTM pairs $(r \geq 0.7)$ reported by [8] in their pairwise correlation analysis on the data. Comparison on these two sets of highly correlated PTM pairs shows that the confidence scores assigned by our method are significantly higher than or at least equal to the ones assigned by the other two methods (Tables 2, 3, and
![img-4.jpeg](img-4.jpeg)

Figure 5 Literature supports for the top 50 significant relationships given by our method (red), $N p$ (green) (scheme 3), and noHidden (blue).

Table 2 Comparison on the significance scores of three highly correlated PTM pairs reported in [11].


nd means no difference.

Table 3 Comparison on the significance scores of 10 most correlated PTM pairs reported in [8].


nd means no difference. supplementary information). This means, taking into account the existence of hidden confounders significantly increases our ability to recover highly correlated pairs of histone modifications.

## Analysis and discussions

Finally, we assessed whether the proposed method can produce biologically meaningful causal relationships by deriving a network model consisted of the most confident relationships (significance score $\geq 0.7$ ). At this threshold, a network of 49 relationships was created (Figure 6). We investigated biological characteristics of the resulting network by assessing its dominant modifications and the most significant Markov relations employing the method described in [20]. By which, dominance score of each modification $X$ is calculated by $d S \operatorname{core}(X)=\Sigma C_{0}(X$, $Y)^{k}$, where $C_{0}(X, Y)$ denotes the significance score of $X$ being an ancestor of $Y, k$ is the constant to reward highly significant features. Table 4 shows 10 most dominant modifications ( $k=2$, for other values of $k$ only the orders were changed) and significant Markov relations, with the corresponding scores given by our method. Analyzing the top dominant modifications, we found that 8 out of 10 PTMs, ${H 3 K 4 M e 3, H 3 K 27 A c,}$ $H 2 B K 120 A c, H 4 K 8 A c, H 4 K 5 A c, H 4 K 91 A c, H 3 K 4 M e 1$, $H 3 K 9 A c}$, have been reported in the original research as important marks that appeared in the modification back-bone at promoters [8]. For the other two, $H 3 K 27 M e 3$ is known as an important repressive mark, and $H 3 K 27 M e 1$ as an active mark at promoters [9]. Interestingly, the result suggested the significant role of $H 2 B K 120 A c$ and its regulatory effect on $H 3 K 4 M e 3$, an important modification mark of active promoters, through the chain $H 2 B K 120 A c \rightarrow H 3 K 18 A c \rightarrow$ $H 3 K 4 M e 3$. For a long time, the functions of $H 2 B$ modifications, particularly $H 2 B K 120 A c$, have remained obscure compared to other modifications [56]. Just recently there has been an indication that $H 2 B K 120 A c$ appears as an early modification mark in TSS regions and affects $H 2 B K 120$ Llb [57], a modification that regulates $H 3 K 4 M e 3[58,59]$, providing support for our finding. Investigation of the most significant Markov relations revealed that well-characterized modifications are mostly functionally related. For example, the

![img-5.jpeg](img-5.jpeg)

Figure 6 A network model of highly significant causal relationships given by our method. 10 most dominant modifications and highest confidence Markov relations are illustrated by filled nodes and purple edges, respectively.

Table 4 The top dominant histone modifications and significant Markov relations with corresponding dominance and significance scores (dScore and $C_{0}$, respectively) given by our method.


N-terminal tail of histone H 4 has four acetylated lysines: K5, K8, K12, K16, of which H4 K5Ac/K8Ac/K12Ac play a non-specific, cumulative regulatory role different from that of H4K16Ac [60]. In consistence with this observation, these modifications were predicted to be closely linked and separated from $H 4 K 16 A c$ in the resulting model: $H 4 K 5 A c \rightarrow H 4 K 8 A c, H 4 K 5 A c \rightarrow H 4 K 12 A c$, and $H 4 K 8 A c \rightarrow H 4 K 12 A c$ (one of the top 10 Markov relations). For other less well-known modifications, such as H3R2 methylations or H3K27 mono-methylation, the links might suggest novel biological understanding. While the relationship between H3R2Me1 $\rightarrow$ H3R2Me2 might reflect a directional equilibrium between monoand di-methyl H3R2, the one between H3K27Me1 $\rightarrow$ H3K27Me3 might reflect their functional association through G9a methyltransferase, as recently reported by [61]. More interestingly, 4 out of 10 most significant Markov relations have already been reported to be causal in literature. [14] have shown evidences for causal relationships of $H 3 K 27 M e 3 \rightarrow H 3 K 9 M e 3$ and $H 3 K 4 M e 3$ $\rightarrow H 2 A Z$. In [62], H3K9Me1/2 was shown to be demethylated by $P H D$ finger protein 8 ( $P H F 8$ ), whose catalytic activity is in turn stimulated by H3K4Me3, suggesting the causal effect of $H 3 K 4 M e 3$ on H3K9Me1, represented by the link H3K4Me3 $\rightarrow$ H3K9Me1. Also, the deposition of histone variant $H 2 A . Z$ by $S W R 1$ complex is known to be triggered by $N u A 4$-mediated acetylation of histone $H 4[63,64]$. Our model supported this observation with the relationship $H 4 K 8 A c \rightarrow H 2 A Z$. Additionally, causal effects have also been observed to support other relationships of the resulting model. For example, [14] have given evidence for the relationship $H 3 K 4 M e 3 \rightarrow H 3 K 36 M e 3$. [65] have reported that the recruitment of MLL1, a histone methyltransferase responsible for H3K4 methylation, is required for the binding of TIP60 histone acetyltransferase, which catalytically acetylates H2AK5. In agreement, our model predicted the relationship $H 3 K 4 M e 3 \rightarrow H 2 A K 5 A c$, suggesting causal effect of $H 3 K 4 M e 3$ on $H 2 A K 5 A c$.

## Conclusion

Elucidation of functional relationships among histone modifications is crucial to understanding important chromatin-mediated processes. Previous BN-based approaches, however, have not taken into account the existence of hidden regulators when inferring causal relationships of PTMs. We tackled the problem by proposing a novel approach that exploits chromatin organizational information to capture the effect of PTM hidden regulators. Application on human epigenomic data showed the advantage of the proposed method over the previous ones. Moreover, it could recover biologically relevant causal relationships between histone modifications, which may be useful for future investigation of histone crosstalk.

## Competing interests

The authors declare that they have no competing interests.

Authors' contributions NTL and TBH defined the research problem and proposed the solution. NTL, BHH, and DHT designed and implemented the experiment. All authors contributed to and approved the final version of the manuscript.

## Acknowledgements

This work was supported by Vietnam's National Foundation for Science and Technology Development (NAFOSTED Project No.102.01-2011.05).

## Declarations

The publication costs for this article were funded by Vietnam's National Foundation for Science and Technology Development (NAFOSTED Project No.102.01-2011.05). This article has been published as part of BMC Genomics Volume 15 Supplement 1, 2014: Selected articles from the Twelfth Asia Pacific Bioinformatics Conference (APBC 2014): Genomics. The full contents of the supplement are available online at http://www.biomedcentral.com/ bmcgenomics/supplements/15/51.

Authors' details ${ }^{1}$ Japan Advanced Institute of Science and Technology, 1-1 Asahidai, Nomi, Ishikawa 923-1292, Japan. ${ }^{2}$ Vietnam Academy of Science and Technology, 18 Hoang Quoc Viet, Hanoi, Vietnam. ${ }^{3}$ Hanoi National University of Education, 36 Xuan Thuy, Cau Giay, Hanoi, Vietnam.

Published: 24 January 2014

## Submit your next manuscript to BioMed Central and take full advantage of:

- Convenient online submission
- Thorough peer review
- No space constraints or color figure charges
- Immediate publication on acceptance
- Inclusion in PubMed, CAS, Scopus and Google Scholar
- Research which is freely available for redistribution

Submit your manuscript at www.biomedcentral.com/submit
(3) BioMed Central