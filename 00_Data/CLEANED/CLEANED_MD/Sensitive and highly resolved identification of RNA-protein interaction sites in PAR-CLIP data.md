# Sensitive and highly resolved identification of RNA-protein interaction sites in PAR-CLIP data 

Federico Comoglio ${ }^{1 *}$, Cem Sievers ${ }^{1,2,3 *}$ and Renato Paro ${ }^{1,4}$


#### Abstract

Background: PAR-CLIP is a recently developed Next Generation Sequencing-based method enabling transcriptome-wide identification of interaction sites between RNA and RNA-binding proteins. The PAR-CLIP procedure induces specific base transitions that originate from sites of RNA-protein interactions and can therefore guide the identification of binding sites. However, additional sources of transitions, such as cell type-specific SNPs and sequencing errors, challenge the inference of binding sites and suitable statistical approaches are crucial to control false discovery rates. In addition, a highly resolved delineation of binding sites followed by an extensive downstream analysis is necessary for a comprehensive characterization of the protein binding preferences and the subsequent design of validation experiments.


Results: We present a statistical and computational framework for PAR-CLIP data analysis. We developed a sensitive transition-centered algorithm specifically designed to resolve protein binding sites at high resolution in PAR-CLIP data. Our method employes a Bayesian network approach to associate posterior log-odds with the observed transitions, providing an overall quantification of the confidence in RNA-protein interaction. We use published PAR-CLIP data to demonstrate the advantages of our approach, which compares favorably with alternative algorithms. Lastly, by integrating RNA-Seq data we compute conservative experimentally-based false discovery rates of our method and demonstrate the high precision of our strategy.
Conclusions: Our method is implemented in the R package wavCluster 2.0. The package is distributed under the GPL-2 license and is available from BioConductor at http://www.bioconductor.org/packages/devel/bioc/html/ wavClusterR.html.

Keywords: PAR-CLIP, RNA, RNA binding proteins, Bayesian statistics

## Background

RNA-binding proteins (RBPs) play a fundamental role in virtually all aspects of RNA metabolism, including the regulation of RNA localization, stability, translation or degradation [1]. These proteins extensively contribute to the control of gene expression by regulating the life cycle of microRNAs, where the RBP-RNA interaction is mediated by specific RNA sequence motifs or secondary structures [2]. Interestingly, recent studies showed that deregulation of RBP expression or mutation of cognate

[^0]binding sites are causally related to several human diseases including cancer [3-6]. Many of these studies have been made possible by the development of new methods mapping interaction sites in a comprehensive and systematic manner [7]. Particularly, the Photo-Activatable Ribonucleoside-enhanced CrossLinking and ImmunoPrecipitation (PAR-CLIP) method made it possible to identify highly specific RBP-RNA interactions by generating a distinct imprint in the bound RNA [8-10]. In this method, cells are cultured with a ribonucleoside analogue, e.g. 4-thiouridine (4SU), which becomes incorporated into nascent RNA molecules. Then, in vivo UV crosslinking at a specific wavelength is performed to stabilize the RNARBP interaction, resulting in a covalently linked RNARBP complex. Next, the complex is isolated, the protein


[^0]:    *Correspondence: federico.comoglio@bsse.ethz.ch; csievers@mgh.harvard.edu
    ${ }^{1}$ Department of Biosystems Science and Engineering, Swiss Federal Institute of Technology Zurich, Mattenstrasse 26, 4058 Basel, Switzerland
    ${ }^{2}$ Department of Pathology and Center for Cancer Research, Massachusetts General Hospital and Harvard Medical School, Boston, USA Full list of author information is available at the end of the article

digested, the RNA molecules recovered and reverse transcribed to cDNA. Next-Generation Sequencing is then used to determine the identity of these molecules.

Importantly, the reverse transcription induces specific base transitions at the original cross-linked sites, which can be used to identify high-confidence RBP-RNA binding interactions in PAR-CLIP data [11]. Based on the induction of transitions, different strategies have been developed for the identification RNA-RBP interactions in PAR-CLIP data. CLIPZ [12], a widely adopted method for PAR-CLIP data analysis, ranks protein binding sites, referred to as clusters, based on their total number of observed transitions. PARalyzer [13], in contrast, utilizes transitions to fit a Gaussian kernel density estimate classifier in order to discriminate signal from noise at interaction sites with the aim to infer the protein binding sites. The cluster boundaries are determined by extending the interaction sites using a fixed threshold on the coverage or by applying an arbitrary window size. PIPE-CLIP [14], a very recent tool designed for CLIP-seq data analysis, employs a binomial model and performs comparably to PARalyzer in identifying binding sites in PAR-CLIP data. However, these methods fall short on important aspects of PAR-CLIP data analysis. (i) As experimental validation of RNA-RBP interactions is laborious and only feasible on small scale, statistically rigorous approaches are needed to rank clusters and identify high-confidence subsets amenable to experimental testing. (ii) PAR-CLIP data allows for a highly resolved identification of the RBP binding sites. However, to delineate cluster boundaries accurately, a sensitive peak caller tailored to this problem is needed. (iii) Not every observed transition is induced by cross-linking, i.e. by PAR-CLIP. Rather, sequencing errors, RNA contaminants and cell type-specific SNPs represent additional sources of transitions which can lead to the detection of a considerable number of false positives [11]. Attempts to limit the false discovery rate (FDR) by requiring a minimum number of interaction sites per cluster, as recommended by $[13,15]$, can largely reduce sensitivity as it will inevitably miss all true clusters containing less interaction sites. In fact, given that the nucleotide composition of protein binding sites can greatly vary, clusters exhibiting a few PAR-CLIP induced transitions can still correspond to bona fide interaction sites.

In this work, we specifically address the three points outlined above. We introduce a Bayesian model to identify PAR-CLIP induced high-confidence transitions extending our recent work in [11]. We detail a new, coveragebased algorithm for the identification of cluster boundaries termed Mini-Rank Norm (MRN) and show that it substantially improves resolution of binding sites over other methods. We test our algorithm on published data and compare its performance with PARalyzer. We demonstrate that wavClusteR outperforms alternative
algorithms both in detection and resolution of clusters. By using a transition frequency-based strategy our method overcomes the reduction in sensitivity and specificity which characterizes hard thresholding approaches such as PARalyzer. Lastly, we evaluate the performance of our algorithm by integrating matched RNA-Seq data to compute conservative FDR estimates, confirming that high-confidence transitions identified by our approach are PAR-CLIP specific.

## Methods

## Model

Let $i$ be a genomic position spanned by a number of reads after the short read alignment. The relative substitution frequency (RSF) $x$ at position $i$ is the ratio between the number of base substitutions $y$ within the reads (e.g. $\mathrm{T} \rightarrow \mathrm{C}$ ) aligned at $i$ relative to the total coverage $z$ at the site, and can be interpreted as an estimate of the corresponding transition probability. We recently introduced a non-parametric, two-component mixture model to discriminate PAR-CLIP-specific from non-experimentallyinduced transitions [11]. In our model, the first and second component represent non-experimental and PAR-CLIP-induced transitions, respectively.

Here, we developed a model that integrates information over the entire RSF range. For this purpose, we consider a Bayesian network representation of our mixture model (Figure 1) corresponding to a chain of three random variables $(\Theta, X, Y)$. Here $\Theta \in\{1,2\}$ encodes the source of transition (non-experimental $[\Theta=1]$ or experimental $[\Theta=2]), X \in(0,1]$ represents a relative substitution frequency (RSF) value and $Y$ is the number of observed transitions at a given position. According to this model all observed substitutions are thought to be generated as follows. First, a binary random number $\Theta$ is drawn from a Bernoulli distribution $\operatorname{Bern}(\lambda)$ with $p(\Theta=1)=\lambda$. The value of $\Theta$ determines the component used to sample the base substitution probability $x$. Second, the number of observed transitions $Y$ is obtained from a binomial distribution $\operatorname{Bin}(z, x)$, where the sample size $z$ corresponds to the total number of aligned reads at a given position. According to our model, $p(Y, X, \Theta)$ factorizes as:

$$
p(Y, X, \Theta)=p(Y \mid X) p(X \mid \Theta) p(\Theta)
$$

Therefore, the posterior probability that a given number of transitions was induced by either source can be computed as:

$$
p(\Theta=\theta \mid Y)=\frac{p(Y, \theta)}{p(Y)}=\frac{\int_{0}^{1} p(Y \mid x) p(x \mid \theta) p(\theta) d x}{p(Y)}
$$

The resulting posterior probability marginalizes out $X$ and thereby integrates information over the entire RSF range. Using $p(\Theta=\theta \mid Y)$, we then compute the log-odds ratio for each transition as $\log (p(\Theta=2 \mid Y) / p(\Theta=1 \mid Y)$ and define

![img-0.jpeg](img-0.jpeg)

**Figure 1** Graphical representation of the Bayesian network employed to discriminate PAR-CLIP-specific from extrinsic transitions. The data generating process is modeled hierarchically, where i) Θ encodes the unobserved source of the transition (PAR-CLIP-specific or -independent), ii) *X* represents the relative substitution frequency and iii) *Y* is the number of observed transitions at the position, which exhibits a coverage of *z* reads.

The relative log-odds ratio for a cluster as the sum of all log-odds within a cluster, normalized to the total number of bases susceptible to cross-linking.

### Cluster boundaries identification

Let *C*(*i*) be the coverage at position *i* and *C*(*i*, *j*) be the sequence of coverage values (*C*(*i*), *C*(*i*+1), ..., *C*(*j*)), *i* ≤ *j*. Similarly, let *S*(*i*), *E*(*i*) be the positive and negative differences in the coverage function, i.e. the number of read alignments starting or ending at position *i*, respectively, and *S*(*i*, *j*) = (*S*(*i*), *S*(*i*+1), ..., *S*(*j*)), *E*(*i*, *j*) = (*E*(*i*), *E*(*i*+1), ..., *E*(*j*)), *i* ≤ *j* be the extended notation to intervals. We then consider the set *T* of all genomic positions corresponding to high-confidence transitions (hcTs) of a given type (e.g. T→C). In the following paragraphs, we detail the steps performed by the MRN algorithm.

### Estimate local background threshold

For each *i<sub>t</sub>* ∈ *T*, we consider the largest non-zero coverage window *w* containing *i<sub>t</sub>* and compute all putative cluster start *C<sub>s</sub>* = (*S*(*i*) ≥ *δ*)<sub>*i*∈*w*;*i*≤*i<sub>t</sub>* and cluster end *C<sub>e</sub>* = (*E*(*i*) ≥ *δ*)<sub>*i*∈*w*;*i*≥*i<sub>t</sub>* positions therein, where *δ* is an integer background threshold (Figure 2A). To account for large variations in coverage between distinct genomic regions, we estimate noise levels in the coverage function at positions proximal to hcTs and use this estimate to compute a window-specific threshold *δ<sub>w</sub>* as follows. We draw a random sample *U* ⊆ *T* of size *N* (here *N* = 1000) and consider *Ŵ* = ((*i<sub>t</sub>* − *n*, *i<sub>t</sub>* + *n*))<sub>*t∈U*</sub>, i.e. a sequence of genomic intervals centered on each *i<sub>t</sub>*. By default, *n* = 25. Then, we compute normalized non-zero coverage differences *D*<sup>+</sup> within *Ŵ*. Let

$$D = \left(\frac{\mathcal{S}(\tilde{w})}{\max(\mathcal{S}(\tilde{w}), \mathcal{E}(\tilde{w}))}, \frac{\mathcal{E}(\tilde{w})}{\max(\mathcal{S}(\tilde{w}), \mathcal{E}(\tilde{w}))}\right)_{\tilde{w} \in \tilde{W}}.$$

be the sequence of all normalized coverage fluctuations observed within *Ŵ*. We model the distribution of nonzero fluctuations *D*<sup>+</sup> as a mixture of two Gaussian components with unequal variance. The first component (*k* = 1) models noisy fluctuations, while the second component (*k* = 2) models sharp jumps in the coverage function. Model parameters are estimated using expectation-maximization and responsibilities are used to compute the coefficient *c* = min{*x* ∈ *D*<sup>+</sup> : *p*(*k* = 2|*x*) ≥ *p*(*k* = 1|*x*)}, which along with max(*S*(*w*)) and max(*E*(*w*)) determines *δ<sub>w</sub>* within each window. Alternatively, the user can define a global threshold, e.g. by selecting a fraction of the minimum coverage requirement *m*<sub>1</sub> at hcTs or of the mode *m*<sub>2</sub> of the coverage distribution at these sites. A choice *δ* = ⌊0.1 · max(*m*<sub>1</sub>, *m*<sub>2</sub>), where ⌊*x*⌋ is the largest integer not greater than *x*, empirically works well on all analyzed PAR-CLIP datasets.

### Identify candidate cluster boundaries

The width *W* = (*l* − *k* + 1)<sub>(*k*,*l*)∈*C<sub>s</sub>*×*C<sub>e</sub>*</sub> of each candidate cluster and signal levels at *C<sub>s</sub>* and *C<sub>e</sub>*, namely *n<sub>s</sub>* = (*S*(*i*))<sub>*i*∈*C<sub>s</sub>*</sub> and *n<sub>e</sub>* = (*E*(*i*))<sub>*i*∈*C<sub>e</sub>*, respectively, are computed (Figure 2A).

### Represent candidate clusters as rank vectors

We represent each candidate cluster characterized by the vector (*n*<sub>*s<sub>s</sub>*</sub>, *n*<sub>*e<sub>l</sub>*</sub>, *w*<sub>*kl*</sub>) as a rank vector **r**<sub>*kl*</sub> = (*r*<sub>*s<sub>k</sub>*</sub>, *r*<sub>*e<sub>l</sub>*</sub>, *r*<sub>*w<sub>*kl*</sub>*) (Figure 2A), where *r<sub>s</sub>* is the ranking of start positions (with ties resolved 5'→3', i.e. with increasing values at each index set of ties), *r<sub>e</sub>* = π(*n<sub>e</sub>*) is the ranking of end positions (with ties resolved 3'→5') and *r<sub>w</sub>* = π(−*W*) is the ranking of candidate cluster widths (with ties resolved by minimum ranking).

### Identify the optimal solution

The expected coverage of a RBP binding site corresponds to a sharply peaked rectangle function [12], represented by the rank vector *O* = (0, 0, 0). We identify the optimal solution as the candidate cluster that is closest to *O* in terms of the euclidean norm of its rank vector **r**<sub>*kl*</sub>. Although multiple optimal solutions can occur, the choice of the euclidean norm strongly disfavors large clusters by construction. Therefore, in case of ties, the shortest cluster is reported, as it corresponds to the binding site with higher signal at the cluster boundaries as compared to any other optimal solution.

![img-1.jpeg](img-1.jpeg)

**Figure 2 Outline of the MRN algorithm and examples. (A)** A non-zero coverage window w containing two high-confidence transitions (hcTs, denoted by white circles and dashed gray lines) located in close proximity but marking two distinct protein binding sites is shown (gray rectangle). In this window, the observed total coverage of aligned PAR-CLIP reads is indicated by the solid black line, which exhibits two proximal peaks corresponding to the interaction sites. The MRN algorithm aims at resolving these binding sites by discriminating binding-dependent coverage fluctuations from noise and by subsequently using geometric properties of RBP binding sites to refine the cluster boundaries. First, all coverage fluctuations, i.e. positive and negative coverage differences (blue and orange triangles, respectively, with heights proportional to the magnitude of the coverage fluctuations) within w are computed and stored in the two vectors n<sup>s</sup> and n<sup>e</sup>, respectively. These values are then used to learn a local threshold *δ*<sub>w</sub> (see Methods) that is applied to remove noise from the coverage function. Coverage fluctuations smaller than *δ*<sub>w</sub> (solid gray line) are discarded. Next, each hcT is processed separately. The values of all retained positive and negative coverage differences localizing upstream and downstream to the analyzed transition, respectively, are ranked. Rankings are stored in the rank vectors r<sup>s</sup> and r<sup>e</sup>. Finally, all putative cluster boundaries (rectangles) are identified and their length is ranked. Each candidate cluster, represented by a rank vector summarizing coverage and cluster length rankings (e.g. (0, 2, 0)), is then evaluated and the optimal cluster (light blue) is identified (see Methods). **(B)** Clusters (blue rectangles) identified by the MRN algorithm within a complex coverage region of length 1.6 kb of chromosome 10, MOV10 data set. Positive and negative coverage differences are shown in red and blue, respectively. hcTs are indicated by vertical dashed lines. Cyan lines correspond to hcTs that solely localize within clusters identified by the MRN algorithm. Clusters identified using the CWT-based algorithm do not contain these sites. **(C)** AGO2 clusters identified within the 3'-UTR of the KLHL20 transcript. Each cluster contains ≥ 1 microRNA seed sequences of microRNAs expressed in HEK293 cells. The color scheme is the same as in B. **(D)** Same as C, but for the 3'-UTR of the RAB5A transcript.

## Comparison with PARalyzer

## Data processing

All PAR-CLIP data sets were processed as previously described [11]. Briefly, adapter sequences were removed. Reads of length $\geq 15$ passing the Illumina quality filter were aligned to the human reference assembly 'hg19' using Bowtie [16], allowing at most one mismatch. The following Bowtie parameters were specified: -best -chunkmbs $512-\mathrm{n} 1-\mathrm{S}-\mathrm{M} 100$.

## Parametrization

While our method depends on few parameters - essentially the minimum required coverage at transitions and the posterior probability cutoff - PARalyzer contains a more extensive parametrization. To allow for a fair comparison we selected mainly default and recommended parameter values. Both methods differ on what constitutes the minimum required evidence for a binding site. While wavClusteR poses a cutoff $c$ on the strand-specific coverage at hcTs, PARalyzer applies a threshold on the number of reads forming a read group. To compare the performance of the two methods, we first learn the PARCLIP specific RSF interval by fitting the mixture model using $c=20$ and then exhaustively identify binding sites with wavClusteR starting from hcTs with RSF values within the Bayes classifier and $c=1$. We run PARalyzer using two different values for the minimum conversion locations for clusters $n$, namely $n=1$ (default value) or $n=2$ (recommended value), respectively. The choice of this parameter crucially determines sensitivity and recall of the algorithm. The full set of PARalyzer parameters used for the comparison is provided in Additional file 1, Section 1.1. Only clusters exhibiting at least one T to C transition with a strand-specific coverage of 10 are retained for the comparison, with no requirement on its RSF value to enable a fair comparison between algorithms.

## microRNA seed mapping

We considered a set of microRNAs (miRNAs) previously shown to be expressed in HEK293 cells [17] and computed the enrichment of miRNA seeds within each set of cluster sequences relative to a random control. The latter was obtained by generating $10^{4}$ samples of dinucleotide shuffled microRNA sequences and the mean relative seed count was used as background estimate. To allow for a fair comparison PARalyzer-specific clusters were extended to the median length of wavClusteR-specific clusters.

## Computing false discovery rates

To provide experimentally-based estimates of the False Discovery Rate (FDR) of our method, we analyze the MOV10 PAR-CLIP data set and a matched total RNA-Seq profile from the same HEK293 cells used to perform the PAR-CLIP experiment [11].

## FDR of high-confidence interaction sites

We estimated a highly conservative FDR upper bound and a FDR lower bound as a function of the RSF as follows. Let $\mathcal{G}$ be the set of genomic positions with a minimum coverage of 20 within the PAR-CLIP and the RNA-Seq data set and at least one transition within PAR-CLIP. Each element of $\mathcal{G}$ is associated with a specific PAR-CLIP RSF value. We partition the RSF interval $(0,1]$ into ten equally spaced intervals and for each range we identify the genomic positions $\mathcal{P} \subseteq \mathcal{G}$ such that the associated RSF values fall into the RSF interval. We compute a conservative FDR upper bound by regarding as FPs all genomic positions $\mathcal{U} \subseteq \mathcal{P}$ showing at least one transition in the RNA-Seq data, irrespective of their RSF values. The FDR upper bound is therefore $|\mathcal{U}| /|\mathcal{P}|$. Similarly, we compute the FDR lower bound by considering FPs all genomic positions $\mathcal{L} \subseteq \mathcal{P}$ exhibiting an RNA-Seq-based RSF within the same interval, and compute the FDR lower bound as $|\mathcal{L}| /|\mathcal{P}|$.

## FDR clusters

We rank clusters by decreasing values of relative logodds and consider the resulting top $n$ clusters. For each cluster in the ranking, we identify the set $\mathcal{T}$ of genomic positions with hcTs localizing therein and compute the RNA-Seq-based RSF $x_{t}, t \in \mathcal{T}$. To compute conservative FDR estimates, we regard a cluster as FP if there exist at least one $t \in \mathcal{T}$ such that $a \leq x_{t} \leq b$, where $[a, b]$ is the PAR-CLIP-specific RSF support resulting from applying a given posterior probability cutoff. This condition is highly conservative, as a single true hcT within a cluster with multiple detected hcT suffices to correctly identify the binding site. Similarly, we compute less conservative FDR values by regarding a binding site as FP if every $t \in \mathcal{T}$ satisfies $a \leq x_{t} \leq b$.

## Implementation

The algorithms described above are implemented in version 2.0 of our R package wavClusteR [11]. The MRN algorithm is implemented using parallelization, as binding sites are independent of each other. A graphical outline of the data analysis workflow offered by wavClusteR is illustrated in Additional file 1, 2.1.

## Results and discussion

First, we show that the MRN algorithm provides sensitive and highly resolved identification of clusters. We then apply our method to published PAR-CLIP data sets and demonstrate part of our post-processing pipeline. We compare our algorithm to PARalyzer [13] using published AGO2 PAR-CLIP data. Finally, we report estimates of FDRs of high-confidence transitions (hcTs) and of inferred protein binding sites by integrating matched RNA-Seq data.

## Sensitive delineation of clusters at high resolution

We previously proposed an algorithm to resolve cluster boundaries by computing the continuous wavelet transform (CWT) of the coverage function around hcTs. However, this method is prone to false negatives, i.e. hcTs that are not assigned to a cluster, when genomic regions with complex coverage geometry and high variance of local signal-to-noise ratios are encountered. To address this issue and increase the sensitivity of our peak calling procedure, we developed a CWT-independent algorithm which we termed mini-rank norm (MRN). The MRN algorithm (see Methods and Figure 2) solves an optimization problem in which hcTs are first employed to reduce the search space. Signal and noise in the coverage function are locally separated by modeling coverage fluctuations and integrating knowledge of the geometric properties of RBP binding sites. By assuming that the expected coverage of a cluster corresponds to a sharply peaked rectangle function [12], all candidate cluster boundaries spanning a high-confidence PAR-CLIP signal are then exhaustively evaluated and ranked accounting for this prior knowledge. By design, our algorithm favors sharp boundaries and short cluster widths, and, thus, accurately resolves clusters even when multiple binding sites localize within close proximity (Figure 2B). In order to test whether the highly volatile coverage function of PAR-CLIP data reflects complex RBP binding profiles or is an artifact of the procedure, we analyzed published AGO2 PAR-CLIP data [18] for which we can readily evaluate identified binding sites by considering expressed microRNA sequences. Our sequence analysis of $3^{\prime}$-UTRs exhibiting multiple clusters resulted in a large number of transcripts $(n=928)$. Each cluster localized within the $3^{\prime}$-UTR could be assigned to one or more microRNA seed sequences of microRNAs expressed in HEK293 cells, suggesting that these clusters correspond to biologically relevant AGO2 binding sites. Two exemplary regions are illustrated in Figure 2C-D. In addition, our hcT-centered strategy resulted on average in a $\sim 10 \mathrm{x}$ speed up over the CWT-based peak calling on all tested PAR-CLIP data sets (Additional file 1, 1.2).

## Application to published PAR-CLIP data sets

In order to place the binding preference of the RBP within the biological context, post-processing of identified binding sites is required. PARalyzer returns all identified clusters and read groups, and optionally seed-matches for supplied microRNA sequences within the resulting clusters as text files. In contrast, wavClusteR makes use of the R environment to provide extensive post-processing functions supporting i) export of the coverage function, hcTs and clusters for visualization in the UCSC genome browser; ii) export of cluster sequences in FASTA format for de novo motif discovery and motif analysis; iii) strandspecific cluster annotation across different functional
transcriptome compartments in sense and antisense orientations, including normalization of observed frequencies to the overall compartment length and iv) generation of metagene profiles of clusters and their statistics to assess the protein-specific distribution of binding sites across genes. Furthermore, most BioConductor packages can directly use R objects returned by wavClusteR as an input.
For illustration, we provide examples of cluster annotations and metagene profiles obtained from PAR-CLIP data sets of MOV10 and QKI, which are characterized by different binding preferences. Annotation of MOV10 clusters shows that MOV10 preferentially binds to $3^{\prime}$-UTRs of transcripts [11] (Figure 3A), whereas binding sites of QKI, which regulates pre-mRNA splicing, mRNA export and stability, and protein translation [19], are enriched in $3^{\prime}$ UTRs, coding sequences and introns (Figure 3A). Notably, the distinct binding preferences of the two proteins are neatly reflected in their metagene profiles (Figure 3B).

## Comparison with PARalyzer

Using published AGO2 PAR-CLIP data sets, we compared the performance of wavClusteR with PARalyzer [13]. Our comparison revealed that the largest fraction of clusters is similarly identified by both methods (Figure 4A, see Additional file 1, 2.2 for cluster size distributions). However, depending on the parameter settings, the clusters specifically called by either method can represent a substantial fraction. Therefore, we decided to analyze method-specific clusters in more detail. The distribution of RSF values within these clusters revealed that PARalyzer-specific clusters contained almost exclusively extreme RSF values. These values are unlikely to be caused by experimental induction, as the PAR-CLIPspecific enrichment of T to C transitions is missing when compared with other substitutions exhibiting similar RSF values (Additional file 1, 2.3). In contrast, wavClusteRspecific clusters covered the entire RSF range (Figure 4B and Additional file 1, 2.4) and mostly localized within the high-confidence RSF support. In addition, analysis of the read count distribution of PARalyzer-specific clusters (Additional file 1, 2.5) ruled out that the observed extreme RSF values result from clusters with low read count, which could be otherwise filtered out using more stringent parameter cutoffs. Annotation of clusters to the transcriptome shows that PARalyzer-specific AGO2 clusters preferentially localize within intergenic regions or introns (Figure 4C). In contrast, wavClusteR-specific binding sites mainly fall into 3'UTRs, which agrees well with the known biological function of the AGO2 protein [20,21]. Furthermore, we integrated RNA-Seq data derived from the same cell line to independently assess expression of the identified clusters. PARalyzer-specific clusters show significantly reduced expression levels (Figure 4D). This analysis

![img-2.jpeg](img-2.jpeg)

**Figure 3** Post-processing of binding sites identified in the MOV10 and QKI data sets. (**A**) Annotation of MOV10 and QKI clusters with respect to the sense and antisense strand, respectively (top). The distribution of different transcript features in the human transcriptome (hg19, bottom left) is used to compute the normalized annotation profile for clusters mapping on the sense strand (bottom right). (**B**) Corresponding metagene profiles of MOV10 and QKI clusters.

suggests that the largest proportion of PARalyzer-specific clusters corresponds to false positives, possibly caused by RNA contamination during the experimental procedure, as most of the cluster-containing transcripts show no detectable expression.

An additional criterion to determine whether an AGO2 cluster, identified by either PARalyzer or wavClusteR, corresponds to a *bona fide* binding site is whether the site can be assigned to any expressed miRNA. Therefore, we decided to evaluate the quality of the methodspecific clusters by considering the presence of seeds of miRNAs known to be expressed in HEK293 cells. Since miRNAs target AGO2 proteins by complementary base pairing [20], we searched for corresponding seed sequences within the identified AGO2 binding sites (see Methods). Our analysis revealed that wavClusteR-specific clusters were substantially more enriched (>2 folds) for miRNA seeds than PARalyzer-specific ones, suggesting that these clusters more accurately reflect AGO2 binding sites. In addition, we repeated the analyses using PARCLIP datasets from mir-124 miRNA transfection experiments [8] to quantify the fraction of the PARalyzer- and wavClusteR-specific clusters that could be assigned to the transfected miRNA. Figure 4F shows an enrichment of mir-124 seeds within wavClusteR-specific clusters, which is missing in clusters exclusively called by PARalyzer. Finally, these results are further supported by the analysis of a previously published Pumilio-2 (PUM2) PAR-CLIP data set [8]. This RNA-binding protein recognizes a well characterized UGUAHAUA motif [22], which we found

![img-3.jpeg](img-3.jpeg)

**Figure 4 Comparison of wavClusteR with PARalyzer on publicly available PAR-CLIP data. (A)** Barplot representing overlapping or exclusive clusters identified by PARalyzer (with parameters *n* = 1 (left) and *n* = 2 (right)) and wavClusteR on AGO2 PAR-CLIP data. Note that the number of overlapping clusters called by either method differ as there is no one-to-one correspondence between them. **(B)** Distribution of RSF values for *T* → *C* transitions localizing within clusters exclusively identified by PARalyzer (*n* = 1) and wavClusteR (*n* = 2). **(C)** Annotation of method-specific clusters to distinct features of the human transcriptome. Blue and orange circles denote clusters exclusively identified by wavClusteR and PARalyzer, respectively. **(D)** Normalized number of RNA-Seq reads from transcripts overlapping with clusters exclusively identified by either method. **(E)** Seed enrichments over randomized background for microRNA seeds of microRNA expressed in HEK293 cells within clusters exclusively identified by PARalyzer and wavClusteR. **(F)** Same as E, but for the mir-124 seed in AGO2 PAR-CLIP from cells transfected with this microRNA.

to be strongly enriched in wavClusteR-specific clusters (20.2%, *n* = 1777) with respect to PARalyzer-specific ones (0.9%, *n* = 219 and standard parameters).

### Experimentally-based estimation of false discovery rates

We assessed the FDR of our high-confidence transitions by integrating matched total RNA-Seq data from HEK293 cells [11]. We reason that no cross-linking induced transitions are present in RNA-Seq. Hence, if our model correctly identifies PAR-CLIP induced RSF value, a transition classified as PAR-CLIP-specific and equally found in RNA-Seq data is likely to correspond to a false positive (FP). We partitioned the entire RSF interval (0, 1] into different subsets and used transitions identified in both PAR-CLIP and RNA-Seq data to compute a highly conservative FDR upper bound, treating all

observed RNA-Seq transitions as FPs irrespective of their RSF values (see Methods). Our analysis shows that the RSF interval [0.2, 0.7], which we previously reported as PAR-CLIP-specific [11], is bounded by the lowest FDRs values (Figure 5A), thus demonstrating the high precision of our approach. Furthermore, the distribution of RNA-Seq RSF values within the central partitions of the RSF interval (Figure 5B) are mainly dominated by low RSF values compatible with sequencing errors, indicating that our FDR estimates are highly conservative.

Next, we assessed the FDR of clusters, which potentially contain multiple interaction sites. We considered increasing posterior probability cutoffs δ and computed highly conservative FDR estimates of clusters (see Methods) obtained for each threshold (Table 1). At δ = 0.9, our method identified 66,837 MOV10 clusters (of which 20% contained a single hcT) at a ≤ 3% FDR for

![img-4.jpeg](img-4.jpeg)

**Figure 5 False Discovery Rate of high-confidence transitions. (A)** Posterior probability of PAR-CLIP induced RSF values (top) and corresponding lower and upper bounds of the FDR (bottom) over the RSF interval. The normalized fraction of positives is shown in orange. **(B)** Distribution of RNA-Seq RSF values over the RSF interval considered above.


FDR values in parenthesis refer to more relaxed FDR estimates.


the top 250 clusters ranked by relative log-odds (Table 1). Notably, the FDR values dropped substantially from δ = 0.7 to δ = 0.9 without a major effect on the total number of reported clusters, thus showing that stringency of the analysis can be effectively tuned by this parameter. This property is desirable for experimental validation, which is generally performed on few top ranked candidates only.

### Conclusion

We presented a sensitive and comprehensive framework for PAR-CLIP data analysis, which provides statistically grounded and biologically interpretable results. In our approach, not the total number of interaction sites or observed transitions are considered, but rather the frequency at which expected transitions occur. This transition-based strategy outperforms hard thresholding-based approaches and achieves higher sensitivity and specificity.

### Availability and requirements

- **Project name:** wavClusteR
- **Project home page:** https://github.com/FedericoComoglio/wavClusteR
- **Operating system(s):** Platform independent
- **Programming language:** R
- **Other requirements:** R?>?= 3.0.0
- **License:** GPL-2
- **Any restrictions to use by non-academics:** none

### Additional file

**Additional file 1: Supplementary methods and results.** PARalyzer parameters, graphical outline of wavClusteR 2.0 and analysis of publicly available PAR-CLIP data sets.

### Competing interests

The authors declare that they have no competing interests.

## Authors' contributions

FC and CS developed, implemented and tested the method; RP guided this research. All authors participated in the design of the project. FC and CS wrote the manuscript. All authors read and approved the final manuscript.

## Acknowledgements

This work was supported by the ETH Zurich. F.C. is a member of the Life Science Zurich Graduate School, PhD program in Systems Biology. We are thankful to Moritz Gerstung and Maurizio Rinaldi for helpful discussion, to Martin Morgan for support with the package implementation, and to Hind Hashwah and Tommy Schlumpf for feedback on the package.

## Author details

${ }^{1}$ Department of Biosystems Science and Engineering, Swiss Federal Institute of Technology Zurich, Mattenstrasse 26, 4058 Basel, Switzerland. ${ }^{2}$ Department of Pathology and Center for Cancer Research, Massachusetts General Hospital and Harvard Medical School, Boston, USA. ${ }^{3}$ Broad Institute of MIT and Harvard, Cambridge, USA. ${ }^{4}$ Faculty of Science, University of Basel, Klingelbergstrasse 50, 4056 Basel, Switzerland.

Received: 28 July 2014 Accepted: 15 January 2015
Published online: 01 February 2015

## Submit your next manuscript to BioMed Central and take full advantage of:

- Convenient online submission
- Thorough peer review
- No space constraints or color figure charges
- Immediate publication on acceptance
- Inclusion in PubMed, CAS, Scopus and Google Scholar
- Research which is freely available for redistribution

Submit your manuscript at www.biomedcentral.com/submit
(1) BioMed Central