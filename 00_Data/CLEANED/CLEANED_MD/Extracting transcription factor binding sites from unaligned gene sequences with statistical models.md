# Extracting transcription factor binding sites from unaligned gene sequences with statistical models <br> Chung-Chin Lu ${ }^{1}$, Wei-Hao Yuan ${ }^{2}$ and Te-Ming Chen* ${ }^{1}$ 


#### Abstract

Address: ${ }^{1}$ Department of Electrical Engineering, National Tsing Hua University, Hsinchu 30013, Taiwan and ${ }^{2}$ Alpha Imaging Technology Corp., Jubei City, Hsinchu 302, Taiwan Email: Chung-Chin Lu - cclu@ee.nthu.edu.tw; Wei-Hao Yuan - whyuan@a-i-t.com.tw; Te-Ming Chen* - dmchen@abel.ee.nthu.edu.tw * Corresponding author


from Asia Pacific Bioinformatics Network (APBioNet) Seventh International Conference on Bioinformatics (InCoB2008)
Taipei, Taiwan. 20-23 October 2008
Published: 12 December 2008
BMC Bioinformatics 2008, 9(Suppl 12):S7 doi:10.1186/1471-2105-9-S12-S7

This article is available from: http://www.biomedcentral.com/1471-2105/9/SI2/S7
(c) 2008 Lu et al; licensee BioMed Central Ltd.

This is an open access article distributed under the terms of the Creative Commons Attribution License (http://creativecommons.org/licenses/by/2.0), which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.


#### Abstract

Background: Transcription factor binding sites (TFBSs) are crucial in the regulation of gene transcription. Recently, chromatin immunoprecipitation followed by cDNA microarray hybridization (ChIP-chip array) has been used to identify potential regulatory sequences, but the procedure can only map the probable protein-DNA interaction loci within $1-2 \mathrm{~kb}$ resolution. To find out the exact binding motifs, it is necessary to build a computational method to examine the ChIP-chip array binding sequences and search for possible motifs representing the transcription factor binding sites.


Results: We developed a program to find out accurate motif sites from a set of unaligned DNA sequences in the yeast genome. Compared with MDscan, the prediction results suggest that, overall, our algorithm outperforms MDscan since the predicted motifs are more consistent with previously known specificities reported in the literature and have better prediction ranks. Our program also outperforms the constraint-less Cosmo program, especially in the elimination of false positives.

Conclusion: In this study, an improved sampling algorithm is proposed to incorporate the binomial probability model to build significant initial candidate motif sets. By investigating the statistical dependence between base positions in TFBSs, the method of dependency graphs and their expanded Bayesian networks is combined. The results show that our program satisfactorily extract transcription factor binding sites from unaligned gene sequences.

## Background

Understanding transcription is central to understanding genetic regulatory mechanisms. The transcription of a gene is generally dependent on the presence of specific signals located at upstream regions of the core-promoter.

These specific signals derive from their use as binding sites by transcription factors (TFs), and are therefore termed transcription factor binding sites (TFBSs). Recently, chromatin immunoprecipitation followed by cDNA microarray hybridization (ChIP-chip array) has been used to

identify potential regulatory sequences, but the procedure can only map the probable protein-DNA interaction loci within 1-2 kilobases resolution [1]. To find out the exact binding motifs, it is necessary to build a computational method to examine the ChIP-chip array binding sequences and search for possible motifs representing the TFBSs (motif discovery).

There are many computational TFBS motif finding tools available [2-4]. The traditional approach for finding TFBSs is to collect and align a set of promoter sequences of coregulated genes from either the literature or systematic experiments. Numerous computational tools, such as CONSENSUS [5], EM [6], MEME [7] and the Gibbs sampler [8], have utilized the approach to identify short DNA sequence motifs which are statistically over-represented in the promoter sequences.

Other than the alignment-based motif finding algorithms in above, many approaches have tried to extend to the use of evolutionary conservation information such as phylogenetic footprinting or the detection of combinations of binding sites (termed as cis-regulatory modules; CRMs) [2,3]. Phylogenetic footprinting methods [9-11] is an approach that seeks to identify conserved regulatory elements by comparing genomic sequences between related species. However, due to the statistical nature of the approach, e.g., a small amount of closely related species, not all transcription binding sites can be found by using phylogenetic footprinting. Hence, some algorithms have emerged to combine the alignment-based motif prediction with phylogenetic footprinting such as PhyloGibbs [12] and MY sampler [13]. On the other hand, by the detection of CRMs due to the cooperative interactions between TFs, algorithms like those in [14-16] can produce predictions of substantially better specificity than those of isolated sites.

Recently, more effective motif finders, e.g., MDscan [1], ANN-Spec [17], DMOTIFS [18], DME [19] and Cosmo [20], have taken the advantage of a background set, serving as a negative control. The goal of these discriminant motif finders is to search only for motifs that are most discriminating, that is, only those enriched in the foreground set relative to the background set [2]. Although these motif finders have improved the performance of TFBS prediction, it is still a trouble to have a satisfactory solution. How to find out accurate binding motifs may require much attention in the computational biology community. In this study, an improved sampling algorithm is proposed to incorporate the binomial probability model to build significant initial motif sets. By investigating the statistical dependence between base positions in TFBSs, it appears feasible to use statistical models to formulate the structural dependence of a motif in the identification of

TFBSs. In light of this observation, the method of dependency graphs and their expanded Bayesian networks [21] is combined and prediction results show that our algorithm is able to find out motifs more consistent with previously known evidence.

## Methods

Let $T F$ be one of the transcription factors to be investigated. The binding dataset of the transcription factor $T F$, denoted as $B_{T F}$, consists of the sequences with low binding $p$-value $(<0.001)$ to the $T F$ in the ChIP-chip array data [22]. A sliding window of size $w$ is used to extract segments of length $w$ when sliding through each of the sequences in $B_{T F}$.

Let $S_{T F}$ be the collection of all extracted segments from $B_{T F}$, $M$ the number of sequences in the binding dataset $B_{T F}, L_{i}$ the length of the $i$ th sequence in the binding dataset $B_{T F}$, and $T_{T F}$ the total number of segments in $S_{T F}$. Then

$$
T_{T F}=\sum_{i=1}^{M}\left(L_{i}-w+1\right)
$$

To discover the binding motifs of the transcription factor $T F$, a number of initial candidate motif sets for $T F$ is subsequently built from the collection $S_{T F}$ of extracted segments. Note that the contents of segments, called patterns, in $S_{T F}$ may not be distinct.

Most of early motif finding algorithms, such as Gibbs sampler [8] and MEME [23], have a weakness, where initial candidate motif sets are built by randomly extracting segments from sequences in the binding dataset $B_{T F}$ (i.e. randomly selecting segments from the set $S_{T F}$ ). To improve the deficiency, the binomial probability distribution model is firstly utilized in the establishment of a number of initial candidate motif sets in our algorithm.

Then in the process of iterative sampling in our algorithm to expand and/or trim each of the initial candidate motif sets, the method of dependency graphs and their expanded Bayesian networks [21] is used to develop a statistical model for the background motif set identified as the union $S \approx \cup_{T F} S_{T F}$ of segments extracted from all transcription factor binding datasets.

The basic procedure to find the binding motifs of the transcription factor $T F$ is as follows:

1. Build $N$ initial candidate motif sets.
(a) Take $N$ distinct patterns from the set $S_{T F}$ with the most highest significance scores as the candidates by the binomial distribution model (see the Binomial probability distribution model subsection).

(b) Then for each of the significant binding site candidates for the transcription factor, in view of evolution, collect all segments in whose patterns have no more than $d$ Hamming distance matching to the candidate pattern to form an initial candidate motif set.

At this stage, $N$ initial candidate motif sets for the transcription factor $T F$ are built.
2. Iteratively sample through the binding dateset $B_{T F}$ to expand and/or trim each of the $N$ initial candidate motif sets so that their approximate maximum a posteriori (AMAP) scores $[1,24]$ can keep increasing until the $N$ candidate motif sets are invariant in $K$ consecutive iterations (see the Iterative sampling subsection).
(a) In the calculation of AMAP scores in this stage, the background model for the background motif set $S=\cup_{T F^{-}}$ $S_{T F}$ is established under the method of dependency graphs and their expanded Bayesian networks (see the Method of dependency graphs and their expanded Bayesian networks subsection).
3. Refine each of the $N$ candidate motif sets by re-examining all the segments already included in the motif set. A segment is removed from the motif set if doing so increases the AMAP score.

A simple flowchart for our algorithm is shown in Figure 1. The following subsections will expatiate on each stage of our algorithm. As an illustration of the dynamics of the PWM and the rank of different candidate motif sets at different stages of our algorithm, a summary of the prediction process for the motif of the transcription factor CBF1 is given in Figure 2.

## Initial motif sets building

Our method begins by enumerating those patterns in $S_{T F}$ that appear most often in the binding dataset $B_{T F}$ than in others. What we want to do first is to calculate the appearance probability of a pattern in $S_{T F}$, which is the probability that the pattern appears no less than $n$ times in the binding dataset $B_{T F}$. If a pattern $b$ appears more often than other patterns in $S_{T F}$ and its occurrence probability in a generic intergenic region is comparatively low, the calculated significance score of $b$ would be relatively high. We will take patterns with the most highest significance scores as the candidates to build a number of initial candidate motif sets.

## Binomial probability distribution model

The probability to observe exactly $j$ occurrences of pattern $b$ in the collection $S_{T F}$ of segments extracted from the binding dataset $B_{T F}$ is estimated by the binomial distribution
![img-0.jpeg](img-0.jpeg)

Figure I
A flowchart of our algorithm.


Figure 2
An illustration of the dynamics of the PWM and the rank of five candidate motif sets at different stages of our algorithm in the motif prediction of the transcription factor CBFI.

$$
P_{T F}(\operatorname{occ}(b)=j)=\binom{T_{T F}}{j} \times(f(b))^{j} \times(1-f(b))^{T_{T F}-j}
$$

where $\operatorname{occ}(b)$ is the occurrence times of pattern $b$ in $S_{T F}$ and $f(b)$ is the probability that pattern $b$ occurs in the intergenic region and is estimated as the relative frequency of pattern $b$ in the union $S=\cup_{T F} S_{T F}$ of segments extracted from all transcription factor binding datasets. The probability to observe $n$ or more occurrences of the pattern $b$ in $S_{T F}$ is

$$
P_{T F}(\operatorname{occ}(b) \geq n)=1-\sum_{j=0}^{n-1} P_{T F}(\operatorname{occ}(b)=j)
$$

We define the significance score $\operatorname{sig}_{T F}(b)$ of a pattern $b$ to $T F$ as

$$
\operatorname{sig}_{T F}(b)=-\log _{10}\left(P_{T F}(\operatorname{occ}(b) \geq n)\right)
$$

The less probable pattern $b$ in $S$ appears more than $n$ times in $S_{T F}$, the more probable will it be a binding site candidate for the transcription factor $T F$. We will take $N$ distinct patterns with the most highest significance scores as the candidates.

For each of the $N$ significant binding site candidates for the transcription factor $T F$, in view of evolution, collect all segments in $S_{T F}$ whose patterns have no more than $d$ Hamming distance matching to the candidate pattern to form an initial candidate motif set. Thus $N$ initial candidate motif sets for the transcription factor $T F$ are built at the end of this stage. As an example, the PWM and the rank of five initial candidate motif sets for the motif prediction of the transcription factor CBF1 are shown in Figure 2.

## Iterative sampling

In this stage, a sampling method is used to expand and/or trim each of the $N$ initial candidate motif sets $M_{1}, M_{2}, \ldots$, $M_{N}$. For our purpose, a false motif set $M_{N+1}$ is created by randomly selecting $e_{0}\left(e_{0}\right.$ is equal to the maximum size of the $N$ initial candidate motif sets) segments from the collection $S_{T F}$ such that $M_{i} \cap M_{N+1}=\varnothing$, for all $i=1,2, \ldots, N$. In addition, let the collection $S=\cup_{T F} S_{T F}$ of segments extracted from all transcription factor binding datasets represent the intergenic background and here be denoted as $M_{B C}$.

## Approximate maximum a posteriori (AMAP) measure

The score $\operatorname{amap}_{M_{i}}$ of the approximate maximum a posteriori (AMAP) measure of the candidate motif set $M_{i}$ is defined as $[1,24]$
$\operatorname{amap}_{M_{i}}=\frac{1}{w}\left\{\sum_{s=0}^{s \rightarrow 1} \sum_{p_{s, i}, t, z, z, t, p_{s, j}} p_{s, j} \log \left(p_{s, j}\right)-\frac{1}{n_{i}} \sum_{m \in M_{i}} \log \left(P\left(m \mid M_{B G}\right)\right)\right\}$,
where $p_{s, j}$ is the frequency of nucleotide $j$ at base position $s$ in the candidate motif set $M_{i}$ (which can be retrieved from the position specific scoring matrix (PSSM) of $M_{i}$ ), $n_{i}$ is the number of segments in $M_{i}$, and $P\left(m \mid M_{B G}\right)$ is the probability of the pattern of segment $m$ in the motif set $M_{i}$ under an expanded Bayesian network (EBN) model [21] developed from the background motif set $M_{B G}$ (EBN model will be discussed shortly).

The first part of the AMAP score is a negative entropy, which is higher if there are more similar patterns in the candidate motif set $M_{i}$. A motif set $M_{i}$ with all identical patterns has the maximum negative entropy 0 , whereas equal nucleotide frequencies at every position in the PSSM of $M_{i}$ has the minimum negative entropy. And a segment $m$ in the candidate motif set $M_{i}$ which has a pattern much different from the background motif model built from $M_{B G}$ would have lower appearance probability $P$ $\left(m \mid M_{B G}\right)$ and hence increases the score $\operatorname{amap}_{M_{i}}$ of the AMAP measure of $M_{i}$.

## Sampling strategy

In each iteration, there are two steps for the sampler, the S-step and the M-step.

In the S-step, the sampler samples a site by randomly selecting a sequence from $B_{T F}$ and then randomly picking up a site in the selected sequence to extract a segment $m_{s}$ of length $w$. For $1 \leq i \leq N$, if the sampled segment $m_{s}$ appears in $M_{i}$, segment $m_{s}$ will be removed from $M_{i}$ if the AMAP score $\operatorname{amap}_{M_{i}}$ of the candidate motif set $M_{i}$ increases after its removal; otherwise, segment $m_{s}$ will be kept in $M_{i}$. Note that the PSSM of the motif model $M_{i}$ should be retrained if the sampled segment $m_{s}$ is removed from $M_{i}$.

Which one of the $N+1$ motif sets would be the best motif set for the sampled segment $m_{s}$ will depend on the
appendant score $a p p_{M_{i}}$ that the segment $m_{s}$ is derived from $M_{i}[24,25]$

$$
a p p_{M_{i}}=\log \left(\frac{P\left(n_{i}\right)}{1-P\left(n_{i}\right)} \frac{P\left(m_{s} \mid M_{i}\right)}{P\left(m_{s} \mid M_{B G}\right)}\right), 1 \leq i \leq N+1
$$

where $n_{i}$ is the size of current motif set $M_{i}, P\left(n_{i}\right)$ equals $\frac{n_{i}}{T_{T F}}, P\left(m_{s} \mid M_{i}\right)$ and $P\left(m_{s} \mid M_{B G}\right)$ are the probabilities of the content of the sampled segment $m_{s}$ under the PSSM model developed from the current motif set $M_{i}$ and under an EBN model developed from the background $M_{B G}$, respectively. The sampled segment $m_{s}$ will be considered to append into the motif set $M_{i}$ with the highest appendant score $a p p_{M_{i}}$. If $a p p_{M_{N+1}}$ is the highest score, then the sampled segment $m_{s}$ is appended into the false motif set $M_{N+1}$ unless $m_{s}$ is already there and the current iteration stops here. If for some $i, 1 \leq i \leq N, a p p_{M_{i}}$ is the highest score, the sampled segment $m_{s}$ will be further checked in the M-step to see if we really want to append $m_{s}$ into $M_{i}$ unless we have processed $m_{s}$ for $M_{i}$ at the beginning of this S-step as in above and the current iteration stops here.

In the M-step, the sampler has to decide whether the newly sampled segment $m_{s}$ should be appended into the candidate motif set $M_{i}$ or not. The AMAP measure again will be used to evaluate our decision. The sampled segment $m_{s}$ is appended into the candidate motif set $M_{i}$ if and only if the score $\operatorname{amap}_{M_{i}}$ of the motif model $M_{i}$ is increased once the sampled segment $m_{s}$ is appended to $M_{i}$. Note that the PSSM of the motif model $M_{i}$ should be retrained after the sampled segment $b_{s}$ is appended to $M_{i}$. Now the M-step is done and the current iteration stops here.

The sampler will iteratively sample through the binding dataset $B_{T F}$ to expand and/or trim the $N$ candidate motif sets $M_{1}, M_{2}, \ldots, M_{N}$ so that their AMAP scores $\operatorname{amap}_{M_{i}}$ will keep increasing. The $N$ candidate motif sets will tend to be invariant after a (larger) number of iterations. The stopping criterion of the sampling process is that all the $N$ candidate motif sets are invariant in $K$ consecutive iterations. The parameter $K$ is usually set to be $1 \%$ of the size of $S_{T F}$.

#### Alternative sampling strategy

There is an alternative sampling strategy as follows.

In the S-step, the new sampler also randomly samples a site from a sequence in *B*_*TF* to extract a segment *m*_*s* of length *w*. For 1 ≤ *i* ≤ *N*, if the pattern of the sampled segment *m*_*s* appears in *M*_*i*, all the segments in *M*_*i* whose pattern is the same as that of *m*_*s* will be removed if the AMAP score *a**map*_*M*_*i* of the motif set *M*_*i* increases after their removal. Otherwise, these segments will be kept in *M*_*i*.

Also in the S-step, if *a**pp*_*M*_*N*+1* is the highest among all *a**pp*_*M*_*i*, 1 ≤ *i* ≤ *N* + 1, then all segments in the set *S*_*TF* having the same pattern as that of the sampled segment *m*_*s* will be appended into the false motif set *M*_*N*+1 unless these segments are already there and the current iteration stops here. If *a**pp*_*M*_*i* is the highest for some *i*, 1 ≤ *i* ≤ *N*, the sampled segment *m*_*s* will be further checked in the M-step to see if we really want to append those segments in the set *S*_*TF* having the same pattern as that of the sampled segment *m*_*s* into *M*_*i* unless we have already processed those segments for *M*_*i* at the beginning of this S-step as in above and the current iteration stops here.

In the M-step, all the segments in the set *S*_*TF* having the same pattern as that of the sampled segment *m*_*s* are decided to append to the candidate motif set *M*_*i* if and only if the AMAP score *a**map*_*M*_*i* of *M*_*i* increases after these segments are appended into *M*_*i*.

#### Method of dependency graphs and their expanded Bayesian networks

Considering the binding mechanism of transcription factors to specific DNA sites (motifs), there must be distinctive features for the specific motif regions from other intergenic regions which represent the background DNA sequence. Hence, it is conceivable that we can use a statistical model to capture the feature of a specific DAN site (motif) or a generic DNA intergenic region (background). Since the size of a candidate motif set *M*_*i* is often small, a PSSM model is commonly used for *M*_*i* instead of any other more sophisticated statistical model. However, the size of the background motif set *M*_*BG* is usually large enough to be equipped with a more sophisticated one.

As reported in [21], a dependency graph model is used to fully capture the intrinsic interdependency between base positions in a motif or region. The establishment of dependency between two positions is based on a χ²-test from known sample data. An edge is established between two nodes (a node represents a base position) in the graph if the two corresponding base positions of the motif or region are dependent. After all dependent edges have being established completely, a dependency graph for the motif or region is constructed. An example of a dependency graph with 7 nodes is shown in Figure 3.

As reported in [21], although the dependency graph can fully capture the intrinsic interdependency between base positions in a motif or region, it is difficult, if not impossible, to perform statistical inference based on the dependency graph. To resolve the dilemma, the dependency graph is expanded to form a Bayesian network (which is a directed acyclic graph that facilitates statistical reasoning) by allowing a base position in the dependency graph to appear more than once in the Bayesian network as nominally distinct nodes. Figure 4 shows an example of an expanded Bayesian network of the dependency graph in Figure 3. For the detailed procedure of constructing an expanded Bayesian network (EBN) from a dependency graph, please see [21]. In this paper, we use EBNs to model the background motif set *M*_*BG*.

Continued with the same example of the motif prediction of the transcription factor CBF1, the PWM and the rank of the five candidate motif sets at the end of the iterative sampling stage are also shown in Figure 2, together with the final results at the end of the refinement stage.

# Results and discussion

## Data

In order to search for the transcription factor binding sites that regulate gene expressions, we collected binding proteins.

![img-1.jpeg](img-1.jpeg)

Figure 3 An example of dependency graph.

![img-2.jpeg](img-2.jpeg)

Figure 4
An example of expanded Bayesian network.
motor sequences from the cDNA microarray hybridization (ChIp-chip array) of yeast genome [22]. Each of the binding sequences may contain some unknown motifs that are implanted at unknown positions. These data represent the binding affinity of a target transcription factor to the promoter region of a gene in vivo. The experiment protocol assigns a binding $p$-value to each binding promoter sequence of the corresponding transcription factor. A sequence with binding $p$-value less than 0.001 is considered to be bound by the corresponding transcription factor. The threshold of 0.001 is set up to reduce the false positive identification in yeast genome-wide screening.

We collected the ChIp-chip array sequence data from the "Motif discovery results - Discovered motifs, version 24" at [26]. For a transcription factor TF to be investigated, we collected all sequences with binding $p$-value less than the threshold 0.001 to $T F$ into the binding dataset $B_{T F}$. There are 65 binding datasets $B_{T F}$ being able to be collected from Harbison's website.

## Accuracy measurement and comparison

To evaluate the performance of our program, we collected known specificities from many famous websites, such as YPD, SCPD, Transfac and from the literature with experimental evidence [27] to compare with the discovered specificities predicted by our program.

Among the 65 binding datasets $B_{T F}$ collected from Harbison's website, we chose 36 transcription factor binding datasets which have known specificities with experimental evidence to evaluate the performance of our program. The results of our program for the 36 transcription factor binding datasets are listed in Figure 5. It is deserved to be mentioned that the specificity reported for transcription factor PHO2 in Harbrison et al's website is "GTGCGsyGCG", while the predicted result of our program is "ATTATC". In this case, the newly found motif by our program is more consistent with the results reported by Barbaric et al [28] that PHO2 binds to an AT-rich region than the specificity reported in Harbrison et al's website.

In this study, we compared our program with two online programs, MDscan [29] and Cosmo [30]. MDscan is a famous program that can be used to examine the ChIParray selected sequences and search for DNA sequence motifs representing the protein-DNA interaction sites. It takes the advantage of combining two widely adopted motif search strategies, word enumeration and positionspecific weight matrix updating, and incorporates the ChIP enrichment information to accelerate the search and enhance its success rate. The comparison of MDscan with our program is shown in Table 1. Also reported in Table 1 is the performance of our algorithm when the the PSSM model [8] instead of the EBN model [21] is used to model the background motif set $M_{B C}$ in the calculation of the AMAP scores of the $N$ candidate motif sets and the appendant scores of the $N+1$ motif sets. In Table 1, for each transcription factor, the number in each 'Rank' column indicates the rank of the predicted motif which is most consistent with the known evidence from the top ten predicted candidate motifs.

As shown in Table 1, our approach with EBN background model outperforms the other two methods. Our approach with EBN background model gives 30 out of the 36 most predicted motifs for the corresponding 36 transcription factors with the 1st rank, while MDscan and our approach with PSSM background model give only 20 out of 36 and 15 out of 36 most predicted motifs with the 1st rank, respectively. Moreover, MDscan fails in discovering a motif for three transcription factor binding datasets, while our approach in this study is still able to predict a motif consistent with the known evidence.

Cosmo (constrained search for motifs) is a general purpose algorithm for conserved motif detection that allows the search to be supervised by specifying a set of constraints that the PWM of the unknown motif must satisfy. Such constraints may be formulated derived from prior biological knowledge about the structure of the transcription factor, such as the length of the motif intervals. Although Cosmo is based on the same two-component


Figure 5
Predicted results of our program compared with known evidence. The letter symbols used in the 'Known specificity' column have the following mapping: aA: a tT: t gG: g cC: c wW: at rR: ag mM: ac kK: tg yY: tc sS: gc dD: atg hH: atc vV: agc bB: tgc nN : atgc

Table I: Comparison of MDscan and our program.


* N means that the program predicts no motif.
multinomial mixture model used in MEME, it employs the likelihood principle instead of the $E$-value criterion in MEME. In addition, three model types (OOPS, ZOOPS, or TCM) can data-adaptively be selected in Cosmo to achieve better performance. Since there is no prior knowledge used in our program, we compared it to the constraint-less version of the Cosmo program. On the other hand, since the Cosmo program reports only one motif PWM for a dataset, instead of a list of ranked candidate motif PWMs as in MDscan, we adopted only the rank 1 results of our program in this comparison. To evaluate the performance of both programs, we used the statistics proposed by Tompa et al. [4]. For a (computational) tool at the site level, the performance statistics on a dataset are defined as follows:

$$
\begin{aligned}
\text { Sensitivity } & : \quad S n=T P /(T P+F N) \\
\text { Positive predictive value } & : \quad P P V=T P /(T P+F P) \\
\text { Average site performance } & : A S P=(S n+P P V) / 2
\end{aligned}
$$

where $T P$ is the number of known sites overlapped by predicted sites, $F N$ is the number of known sites not overlapped by predicted sites, and $F P$ is the number of predicted sites not overlapped by known sites. To summarize the performance of a given tool over a collection $C$ of datasets, we compute the "combined" statistics as though $C$ were one large dataset by adding $T P, F P$ and $F N$ respectively over the datasets in $C$. Then the combined statistics of our program are $S n=0.6698, P P V=0.8206$, and $A S P=0.7452$, while those of Cosmo are $S n=0.6573$, $P P V=0.5134$ and $A S P=0.5854$. For the detailed Cosmo prediction results and the comparison of the two programs, please see Figure S1 (see Additional file 1). The comparison shows that our program can offer better performance than Cosmo, especially in the elimination of false positives.

The parameters used in our program include the sliding window size $w$ used to extract segments from binding datasets $B_{T F}$ to form $S_{T F}$, the Hamming distance $d$ used to collect segments from $S_{T F}$ to establish initial candidate motif sets, the number of most dependent edges used to form a dependency graph for the background motif model and the number of parents used in the construction of an expanded Bayesian network from the dependency graph [21]. The parameters used in our program to give the best predicted motifs for each of the 36 transcription factors are listed in Table S1 (see Additional file 2). Comparing the performance of the two sampling strategies discussed in the Method section, as shown in Figure S2 (see Additional file 3), we found that the alternative sampler is faster and has almost identical best predicted motifs with those by the primary sampler, except that transcription factors GCN4, HAP4 and PHO4 have the best predicted motifs one nucleotide position shift from those by the primary sampler. In addition, the alternative sampler is slightly better than the primary sampler in the sense that the best predicted motif for the transcription factor DIG1 promotes its rank from the 2nd place by the primary sampler to the 1st place by the alternative sampler.

## Conclusion

In this study, we employed the binomial probability model to establish a number of initial candidate motif sets, and used the method of dependence graphs and their expanded Bayesian networks to model the background motif set as a control to predict TFBSs (motifs) from a set

of unaligned DNA sequences. The prediction results suggest that, overall, our algorithm outperforms MDscan since the predicted motifs are more consistent with previously known specificities reported in the literature and have better prediction ranks. And when compared with the constraint-less Cosmo program, our algorithm has a slightly higher combined sensitivity $S n$, a much higher positive predictive value $P P V$ and a higher average site performance $A S P$. However, the performance of our algorithm is not much better if the length of possible binding sites are too long (more than 12 bps ). Further research is needed to discover long motifs.

Furthermore, variable spacing within binding sites is legitimate for some transcription factors while this study focuses on ungapped motif discovery. Programs such as BIPAD [31] and spaced dyad [32] have investigated into such a bipartitie sequence element discovery problem. Therefore another direction for our future research is to investigate into gapped motifs.

## Competing interests

The authors declare that they have no competing interests.

## Authors' contributions

CL and WY developed and implemented the method. All authors participated in discussions and writing of the paper.

## Additional material

## Additional file 1

Figure S1 - Predicted results of the constraint-less Cosmo program and the comparison with our program.
Click here for file
[http://www.biomedcentral.com/content/supplementary/1471-2105-9-S12-S7-S1.pdf]

## Additional file 2

Table S1 - Parameters used in our program to give the best predicted motifs for the 36 transcription factors.
Click here for file
[http://www.biomedcentral.com/content/supplementary/1471-2105-9-S12-S7-S2.pdf]

## Additional file 3

Figure S2 - Comparison of the predicted results with the primary and alternative samplers.
Click here for file
[http://www.biomedcentral.com/content/supplementary/1471-2105-9-S12-S7-S3.pdf]

## Acknowledgements

We thank Yi-Sian Liao for helping the execution of our prediction program. We also thank the reviewers for their valuable suggestions which improve
the presentation of this paper. This work was supported by the National Science Council, Taiwan, under Contracts NSC 93-3112-B-007-004 and NSC95-3114-P-002-005-Y.

This article has been published as part of BMC Bioinformatics Volume 9 Supplement 12, 2008: Asia Pacific Bioinformatics Network (APBioNet) Seventh International Conference on Bioinformatics (InCoB2008). The full contents of the supplement are available online at http://www.biomedcentral.com/ 1471-2105/\#Issue=S12.

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