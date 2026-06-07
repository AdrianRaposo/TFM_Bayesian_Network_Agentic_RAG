# RESEARCH ARTICLE 

## A Computational Approach to Identifying Gene-microRNA Modules in Cancer

Daeyong Jin ${ }^{1}$, Hyunju Lee ${ }^{1 *}$<br>1 School of Information and Communications, Gwangju Institute of Science and Technology, Gwangju, South Korea<br>* hyunjulee@gist.ac.kr

## Abstract

MicroRNAs (miRNAs) play key roles in the initiation and progression of various cancers by regulating genes. Regulatory interactions between genes and miRNAs are complex, as multiple miRNAs can regulate multiple genes. In addtion, these interactions vary from patient to patient and even among patients with the same cancer type, as cancer development is a heterogeneous process. These relationships are more complicated because transcription factors and other regulatory molecules can also regulate miRNAs and genes. Hence, it is important to identify the complex relationships between genes and miRNAs in cancer.

In this study, we propose a computational approach to constructing modules that represent these relationships by integrating the expression data of genes and miRNAs with gene-gene interaction data. First, we used a biclustering algorithm to construct modules consisting of a subset of genes and a subset of samples to incorporate the heterogeneity of cancer cells. Second, we combined gene-gene interactions to include genes that play important roles in cancer-related pathways. Then, we selected miRNAs that are closely associated with genes in the modules based on a Gaussian Bayesian network and Bayesian Information Criteria. When we applied our approach to ovarian cancer and glioblastoma (GBM) data sets, 33 and 54 modules were constructed, respectively. In these modules, $91 \%$ and $94 \%$ of ovarian cancer and GBM modules, respectively, were explained either by direct regulation between genes and miRNAs or by indirect relationships via transcription factors. In addition, $48.4 \%$ and $74.0 \%$ of modules from ovarian cancer and GBM, respectively, were enriched with cancer-related pathways, and $51.7 \%$ and $71.7 \%$ of miRNAs in modules were ovarian cancer-related miRNAs and GBM-related miRNAs, respectively. Finally, we extensively analyzed significant modules and showed that most genes in these modules were related to ovarian cancer and GBM.

## Author Summary

A microRNA (miRNA) is a small RNA molecule that regulates the expression of mRNA genes. A miRNA can regulate multiple genes, and a gene can be regulated by multiple miRNAs. The regulation of genes by miRNAs may vary from patient to patient, even if they suffer from the same type of cancer. In this study, we identify the relationships

between genes and miRNAs in cancer patients using expression data. Because these relationships are complicated by the involvement of transcription factors, which are among the most influential regulators of genes, we also attempt to explain the triple relationship among genes, miRNAs, and transcription factors. We constructed modules consisting of a set of genes and miRNAs, in which the expression levels are highly correlated. In most of these modules, genes and miRNAs are related to specific cancer types; their relationships are explained both by direct regulation of genes by miRNAs and by indirect relationships via transcription factors.

# Introduction 

Cancer is one of the leading causes of death worldwide. Although remarkable progress has been achieved in cancer therapies, the molecular mechanisms of cancer have not yet been fully identified. Among various regulations of cancer-related genes and pathways in several stages, the regulation of genes by microRNAs (miRNAs) in cancer cells has drawn particular attention, because many miRNAs are located in chromosomal regions that are frequently altered in cancer [1]. MiRNAs are small RNAs, known as important regulators of genes through binding to 3' UTR regions of target genes [2]. In many cancer types, miRNAs have been studied as important biomarkers for diagnosis and prognosis of cancer, as many miRNAs function as oncogenes or tumor suppressors by regulating other oncogenes or tumor suppressor genes [1, 3].

Because miRNAs regulate genes by binding to the 3' UTR regions of genes, many methods were developed to identify conserved sequence regions between miRNAs and mRNAs [4]. However, sequence-based approaches generate many false positive bindings sites and cannot identify functional changes of genes. Hence, the expressions of genes and miRNAs were also integrated to address possible negative correlations between the two sets of expression data [5, 6]. With the advances in high throughput technologies, large-scale mRNA expression and miRNA expression data sets from the same tumor samples have become available, due to collaborative efforts such as The Cancer Genome Atlas (TCGA) project. [7, 8]. These data sets enable researchers to apply computational approaches to identify relationships between mRNAs and miRNAs and help understand their effects in cancer.

Another important approach to understanding relationships between mRNAs and miRNAs is to analyze multiple genes and miRNAs simultaneously by constructing modules of them rather than analyzing each gene-miRNA pair separately [5, 9, 10]. It is widely known that a miRNA can regulate multiple genes [11], and a gene can be targeted by multiple miRNAs [12]. Changes in these numerous relationships can significantly alter the biological functions or signaling pathways associated with a specific cancer [13]. Although it is known that several pathways, such as the p53 and TGF-beta signaling pathways, are related to ovarian cancer [14, 15], the functions of miRNAs in these pathways have not yet been fully explained.

Although a few algorithms for finding gene-miRNA modules have been proposed, improvements are still needed. Peng et al. [5] proposed a bi-clique approach based on a gene-miRNA correlation matrix; however, most of the modules contained only one miRNA, and a few modules contained at most three miRNAs. Hence, it may be difficult to address multiple relationships between genes and miRNAs. Zhang et al. [6] integrated miRNAs, gene expression and gene-gene interactions based on a non-negative matrix factorization (NMF) framework [16]. The decomposed matrix components were considered as gene-miRNA regulatory modules. Although many modules were enriched with known pathways, the relationships between genes and miRNAs were not explained.

Relationships between genes and miRNAs become even more complicated because molecules such as transcription factors or signal transducers regulate genes and miRNAs. For example, p53, the most frequently mutated gene in cancer, regulates hundreds of genes and a set of miRNAs, including miR-24 family, miR-145, miR-107, and miR-192 [17, 18]. In [19], the authors constructed modules that contain highly correlated genes and miRNAs in their expression levels and found that miR-200a regulates the transcription factor ZEB1, which regulates genes contained in the same module as miR-200a.

To enhance the understanding of relationships between genes and miRNAs, we propose a framework that combines a biclustering approach and a Gaussian Bayesian network. Using the biclustering approach, gene-sample modules are first constructed based on gene expression and gene-gene interaction data sets. Here, a subset of genes that are correlated with each other in a subset of samples is clustered, because gene aberrations are different among patients, even if cancer occurs in the same organ or tissue type [20]. Next, using a Gaussian Bayesian network, gene-miRNA modules are constructed to identify miRNAs that regulate genes in gene-sample modules. Here, we use the expression data on genes and miRNA. When we applied our approach to ovarian cancer data sets and glioblastoma (GBM) data sets from TCGA, we identified several modules consisting of genes and miRNAs related to ovarian cancer and GBM. In many modules, relationships between genes and miRNAs were explained either by direct regulations of genes by miRNAs or by indirect relationships via transcription factors. In addition, functional pathway enrichment tests using several biological and signaling pathways demonstrated that these modules were biologically coherent. Based on ratios of cancer-related genes and cancer-related miRNAs, we extensively analyzed several significant modules and performed network analyses of these modules to demonstrate the regulation of genes by miRNAs.

# Materials and Methods 

## Materials

Ovarian cancer. We collected mRNA expression and miRNA expression data sets for 587 tumor samples and 8 unmatched normal samples for ovarian cancer from TCGA [8]; mRNA and miRNA expression data were generated using an Affymetrix HG-U133A microarray and an Agilent H-miRNA_8X15K microarray, respectively. We normalized the expression levels of 12,042 genes using log2 ratios between tumor samples and the average of normal samples for each gene, and then selected 2,933 differentially expressed genes using a $t$-test ( $p$-value $<0.001$ ). Similarly, we normalized the expression levels of 479 miRNAs using the log2 ratios between tumor samples and the average of normal samples for each miRNA (Fig. 1 (A)).

Glioblastoma. We collected mRNA expression and miRNA expression data sets for 482 tumor samples and 10 unmatched normal samples for GBM [7]. These data sets were generated using the same microarray platforms used in the ovarian cancer study. After normalization, we selected 4,059 differentially expressed genes using a $t$-test (Bonferroni corrected $p$-value $<0.05$ ). We used the expression levels of 423 miRNAs normalized using normal samples.

Selecting a p-value threshold for a t-test. The degree of expression changes depending on the cancer type. In this study, the number of differentially expressed genes was small in ovarian cancer compared to GBM. Hence, we used a less strict threshold for ovarian cancer.

Gene-gene interactions. We collected gene-gene interaction data from the HPRD database [21].

## Constructing gene-sample modules

In this study, we first hypothesized that if a group of genes has similar expression tendencies in a subset of samples, and they are differentially expressed in these samples, then these genes

![img-0.jpeg](img-0.jpeg)

Figure 1. Overview of the proposed approach. (A) Collect gene expression and miRNA expression data sets from paired tumor samples, and calculate $\log 2$ ratios between tumor samples and normal samples. (B) Construct gene-sample modules (GSM) from a differentially expressed gene expression matrix using a biclustering algorithm, which allows duplications of genes and samples in multiple modules. (C) Add genes to GSM using gene-gene interactions, if the included genes increase the average PCC values among genes in the module. (D) Construct gene-miRNA modules (GMM) by selecting gene-regulating miRNAs in GSM. Use a Gaussian Bayesian network and the BIC score to evaluate the relationship between genes and miRNAs. (E) To determine the functional relevance of the modules, test whether the genes from the modules are enriched for specific biological functions or signaling pathways. To validate that modules are related to a specific cancer, check that the genes and miRNAs are related to the specific cancer.
doi:10.1371/journal.pcbi. 1004042 . g001
might be related to similar functions or pathways in the development of cancer. We also hypothesized that a gene might have multiple functions and could function in several pathways. To incorporate these hypotheses, we use a biclustering algorithm to allow the duplication of genes and samples in multiple clusters. First, we construct a matrix of differentially expressed genes and samples, and then we normalize the expression values for each gene using a z-score to determine the tendency toward changes of gene expression in the samples. Next, we apply a SAMBA biclustering algorithm [22] to the normalized matrix to construct modules in which genes and samples are highly correlated (Fig. 1 (B)). The SAMBA biclustering algorithm models gene expression data in a bipartite graph $G=(U, V, E)$, where genes in $V$ are represented as nodes on one side and samples in $U$ on the other side. There is an edge in $E$ between a gene $v$ in

$V$ and a sample $u$ in $U$ if the expression value of gene $v$ changes significantly in sample $u$, having high absolute expression values. The biclustering algorithm generates subgraphs from the bipartite graph, in which most of the genes are connected to most of the samples as edges. These subgraphs represent highly correlated gene-sample clusters, where the tendency toward gene expression changes is similar for a subset of samples. Additional details are provided in Fig. S1. We calculate the statistical significance of each module based on a null hypothesis that the expression level of a gene is independent of the expression level of other genes for samples in a module, assessing that the average Pearson correlation coefficients (PCCs) of gene expression levels for genes in the module are higher than the ones from random modules for selected samples. For each module, we conduct the following test.
(Step 1) Construct a random module by randomly selecting the same numbers of genes and samples from the normalized matrix.
(Step 2) Calculate the PCC matrix of expression level values of genes in the module across a subset of samples. Then, calculate the average value of the PCC matrix, excluding diagonal elements.
(Step 3) Repeat Steps 1 and $2 N$ times, letting the average value from the $i$-th permutation serve as the random ${ }_{a v g}(i)$.
(Step 4) Let the average PCC value of genes in the observed module be the module ${ }_{a v g}$.
(Step 5) Calculate the $p$-value of the observed module using the following equation, where I is an indicator function.

$$
p-\text { value }=\frac{\sum_{i=1}^{N} I\left(\text { module }_{\text {avg }}<\text { random }_{\text {avg. }}(i)\right)}{N}
$$

When we calculate the $p$-value, we try to take into account that observed modules are not independent of each other as genes overlap among modules. Hence, we construct random modules where genes in the modules share the same overlap ratio as the observed modules.

Recent research has shown that not all of the genes in cancer-related pathways undergo expression or genomic changes [23]. Consequently, certain genes that play important roles in cancer-related pathways might not be differentially expressed. To include functionally related genes in the gene-sample modules, we expand the gene-sample modules using a gene-gene interaction network. If a gene interacts directly with at least one gene in a module, then this gene can be regarded as a candidate gene for the module. For each module, we collect candidate genes and calculate the average PCC values of expressions between a candidate gene and the genes in the module. We add candidate genes to the module in descending order from the gene having the highest PCC value until the average PCC values of the expressions of genes in the module do not increase.

# Constructing gene-miRNA modules 

Because a set of genes with similar expression changes might be regulated by common miRNAs, we construct gene-miRNA modules by including regulating miRNAs in the gene-sample modules. For this task, we employ a Bayesian network model. Bayesian networks have been extensively used for analyzing gene expression patterns [24]. They are useful in modeling local dependencies and causal influences among variables. Hence, we estimate dependencies between expression values of genes and expression values of miRNAs based on a Bayesian network model. A joint distribution of genes $X=\left\{X_{1}, X_{2}, \ldots, X_{n}\right\}$ and miRNAs $Y=\left\{Y_{1}, Y_{2}, \ldots Y_{m}\right\}$

is represented by a Gaussian Bayesian network. If $X_{i}$ is normally distributed around a mean that linearly depends on its parents, then the conditional probability of $X_{i}$ given its parents $P a^{G}\left(X_{i}\right)=\left\{Y_{j}, \ldots Y_{k}\right\}$ can be represented by

$$
P\left(X_{i} \mid P a^{G}\left(X_{i}\right)\right)=P\left(X_{i} \mid Y_{j}, \ldots, Y_{k}\right) \sim N\left(a_{0}+\sum_{j^{\prime}} a_{j^{\prime}} \cdot Y_{j^{\prime}}, \sigma^{2}\right)
$$

Then, the likelihood of $X$ and $Y$ can be represented by

$$
L(X, Y)=P\left(X_{1}, X_{2}, \ldots, X_{n}, Y_{1}, Y_{2}, \ldots Y_{m}\right)=\prod_{i=1}^{n} P\left(X_{i} \mid P a^{G}\left(X_{i}\right)\right)
$$

To determine which sets of miRNAs explain the expression levels of genes in gene-sample modules, we use a Bayesian information criterion (BIC) as a measure for determining a Bayesian network structure between genes and miRNAs, which can be represented by

$$
B I C=\log (L)-\frac{\log M}{2}+O(1)
$$

where $M$ is the sum of the number of genes and miRNAs. To determine the parents $P a^{G}\left(X_{i}\right)$ of a gene $X_{i}$ yielding the optimal BIC score, we should consider all combinations of miRNAs; however, this approach is highly time-consuming. To reduce the search space, we select candidate miRNAs whose average of absolute Spearman's rank correlation coefficient (SCC) values for genes in a given module are within the top $T \%$ among all miRNAs. Note that we use SCC values for selecting candidate miRNAs to reduce the effects of possible outliers in the PCC. From candidate miRNAs, we first add a miRNA with the highest SCC value as a regulator and calculate the BIC score. Then, we add miRNAs with the next highest SCC values, until adding more miRNAs no longer improves the BIC score. After adding miRNAs to gene-sample modules using the above approach, modules with fewer than two miRNAs are filtered out because these modules cannot represent the combinatorial effects of genes and miRNAs. Finally, genemiRNA modules are obtained.

# Module validation 

To validate the relationships between genes and miRNAs in the modules, we consider four cases of gene regulations. In the first case, genes are directly bound and regulated by miRNAs. To validate this case, we select gene-miRNA pairs from miRTarbase [25] and MicroCosm (http://www.ebi.ac.uk/enright-srv/microcosm/htdocs/targets/v5/). Interacting pairs in miRTarbase are validated by various molecular experiments. Among them, reporter assays and western blot analysis confirm direct interactions. We compare the gene-miRNA pairs in our modules with these direct interactions in miRTarbase. MicroCosm provides computationally predicted binding sites for miRNAs in genomic sequences. Among these pairs, we select only gene-miRNA pairs with a negative correlation in expression values. From this process, we collect target genes for each miRNA, which we use for validation. Then, we perform a hypergeometric test for each miRNA in the modules to check for enrichment of genes in a module against the target genes of a miRNA.

However, certain genes in the modules are not directly regulated by miRNAs, even though the expressions of the genes and the miRNAs are highly correlated. To investigate this indirect relationship, we introduce transcription factors (TFs). We confirm relationships between miRNAs and TFs by manually searching the literature for evidence of cases where miRNAs are

regulated by TFs or TFs are regulated by miRNAs. In the second case, we consider a relationship in which the miRNAs in a module regulate TFs, and these TFs regulate genes in the module. Here, it is not necessary that TFs be members of the module. We identify relationships between TFs and genes using the ChIP-X database [26]. For each TF in the database, we perform a hypergeometric test to determine if there is enrichment of genes in a module against the target genes of the TF. Here, the correlation of expression values between the miRNA and the TF must be negative, and the correlation values between the TF and the mRNA can be either positive or negative.

In the third case, genes and miRNAs are regulated by a common TF. In this case, correlations of expression values between gene-TF and miRNA-TF should be both positive or both negative.

In the fourth case, interacting pairs in miRTarbase [25], experimentally validated by the coexpression of miRNA and mRNA, are used to validate gene-miRNA pairs in our module. Molecular experiments for this case include quantitative real-time PCR (qPCR), microarrays, stable isotope labeling with amino acids in culture (SILAC) and pulsed SILAC.

To determine the functional relevance of the modules, we test whether the genes from the modules are enriched for specific biological functions or signaling pathways. We perform a pathway enrichment test using gene ontology (GO) biological process terms [27], KEGG pathways [28], and BioCarta pathways (http://www.biocarta.com). First, we download these pathways from GSEA (http://www.broadinstitute.org/gsea) and apply a hypergeometric test to each module, obtaining the $p$-values. We exclude biological functions or signaling pathways containing more than 300 genes, as such functions are too general. Supplementary Fig. S2 shows the distribution of GO biological functions as well as KEGG and BioCarta pathways. It can be seen that 51 of 825 GO terms contain more than 300 genes. To address any issues with multiple comparisons, we compute the $q$-values from the $p$-values based on a Benjamini \& Hochberg correction. Then, we use a $q$-value $<0.05$ for the enrichment threshold.

To validate that modules are related to the specific cancer, we first examine whether enriched pathways are related to the cancer being evaluated. For this task, we collect 2,032 cancer genes from the allOnco database (http://www.bushmanlab.org/links/genelists), which is a collection of list of cancer genes from several databases [29-32], 379 ovarian cancer genes from the Dragon Database for Exploration of Ovarian Cancer Genes (DDOC [33]), and 98 GBM genes from the literature ([34, 35]). Then, we calculate the ratios of these cancer genes in the modules. We also collect 100 ovarian cancer miRNAs and 92 GBM miRNAs from the Human miRNA \& Disease Database (HMDD [36]). Then, we calculate the ratios of ovarian cancer-related miRNAs in the modules.

# Associating modules with cancer subtype 

Genes involved in the development of cancer vary depending on cancer subtypes. In several papers [8,37-39], the expression levels of marker genes are used to determine the subtype. For example, GBM samples were classified as a proneural subtype if marker genes DLL3, NKX2-2, SOX2, ERBB3, and OLIG2 were overexpressed [8]. Similarly, we check whether modules identified by our approach are related to a specific subtype of cancers using marker genes.

For this task, we perform the following two steps. In the first step, we cluster all samples into subtypes using hierarchical clustering with a dynamic tree cut [40]. For clustering, we use genes with high variability across the samples. Then, we assign each cluster to a subtype of cancers if known marker genes of cancer subtypes are overexpressed or underexpressed. If a cluster is not related to any subtype or is related to more than one subtype, that cluster is not assigned to any subtype. In the second step, for each module, we use marker genes of the subtype to

compare the expression levels of the marker genes of samples in a module to the expression levels of samples in the other subtype clusters using the $t$-test. If the $p$-values of markers genes of the subtype are significant, we consider the module to be related to the given subtype.

# Results 

## Gene-Sample modules for ovarian cancer and GBM

To construct gene-sample modules, we applied the SAMBA biclustering algorithm to the gene expression matrix, allowing duplication of genes and samples in modules using an overlap factor of 0.5 in $[0,1]$, where 1 represents non-overlap. For ovarian cancer and GBM, we identified 90 and 135 modules, respectively, that represent similar tendencies of gene expression changes for a subset of samples. After performing 1000 permutation tests, we selected 58 and 88 modules with a $q$-value $<0.05$ for ovarian cancer and GBM, respectively. Then, we enlarged these modules by adding genes using gene-gene interactions. On average, we added 15 and 33 genes to each module for ovarian cancer and GBM, respectively.

## Gene-miRNA modules for ovarian cancer and GBM

We constructed gene-miRNA modules from gene-sample modules by including miRNAs. As described in the Methods section, we pre-selected the candidate miRNAs based on the SCC values between the genes and the miRNAs and then added miRNAs to the module, which increased the BIC score. As shown in Fig. 2, we applied 20 different SCC thresholds ( $T \%$ in [1\%, 20\%] of candidate miRNAs among all miRNAs) to reduce the search space. In Fig. 2 (A), the number of modules for ovarian cancer decreased as the thresholds decreased. We observed similar trends when the PCC was used instead of the SCC or when we did not integrate the gene-gene interaction data. Fig. 2 also shows that the ratios of cancer genes, ovarian cancer genes, and ovarian cancer miRNAs were similar for various SCC thresholds $>5 \%$, and that these ratios increased when SCC thresholds decreased. Fig. S3 shows similar results for GBM. Note that we filtered out modules with fewer than two miRNAs, as such modules cannot represent the combinatorial effects of genes and miRNAs.

Among the various thresholds for candidate miRNAs, we selected a value of $3 \%$ (SCC value $=0.157$ for ovarian cancer and 0.194 for GBM) for further analysis and constructed 33 and 54 modules for ovarian cancer and GBM, respectively. Tables S1, S2, S3, and S4 present lists of genes and miRNAs for the modules. For ovarian cancer, the average size of the modules was 34 genes and 10 miRNAs. On average, $19.1 \%$ of genes were cancer genes, $5.7 \%$ were ovarian cancer genes, and $51.7 \%$ of miRNAs were ovarian cancer-related miRNAs in the ovarian cancer modules. When combining genes and miRNAs from all modules, 18.6\% (145 out of 777) of genes were cancer genes, $6.0 \%$ ( 47 out of 777 genes) were ovarian cancer genes, and $43.5 \%$ ( 47 out of 108) of miRNAs were ovarian cancer-related miRNAs. Based on the pathway enrichment test, $48.4 \%$ of the modules were enriched with biological functions or signaling pathways, and most of the modules contained at least one ovarian cancer gene. Table 1 shows ovarian cancer genes and miRNAs for the selected modules. Table S5 presents lists of cancer genes, ovarian cancer genes, and ovarian cancer miRNAs for all of the ovarian cancer modules. For GBM, the average numbers of genes and miRNAs for each module were 66 genes and 14 miR NAs. In the GBM modules, on average, $23.2 \%$ of the genes were cancer genes, $1.2 \%$ were GBMrelated genes, and $71.7 \%$ of the miRNAs were GBM-related miRNAs. For all genes and miRNAs in the GBM modules, $20.6 \%$ ( 386 out of 1867 ) of the genes were cancer genes, $1.7 \%$ ( 32 out of 1867 genes) were GBM-related genes, and $48.4 \%$ ( 46 out of 95 ) of the miRNAs were GBM-related miRNAs. Table S6 presents lists of cancer genes, GBM genes, and GBM miRNAs

A
![img-1.jpeg](img-1.jpeg)
![img-2.jpeg](img-2.jpeg)
C
![img-3.jpeg](img-3.jpeg)
![img-4.jpeg](img-4.jpeg)
D
![img-5.jpeg](img-5.jpeg)

Figure 2. Performance comparison of gene-miRNA modules for ovarian cancer. For ovarian cancer, we compared the performance of gene-miRNA modules generated from four cases: SCC with GGI information, SCC without GGI information, PCC with GGI information, and PCC without GGI information. For all cases, the $x$-axis presents different percentages of candidate miRNAs ( $7 \%$ ) among all miRNAs when constructing gene-miRNA modules. For each case, the number of modules (A), the ratios of cancer genes (B), the ratios of ovarian cancer genes (C), the ratios of ovarian cancer miRNAs (D), the average number of enriched pathways (E), and the ratios of modules enriched with at least one pathway (F) are shown.
doi:10.1371/journal.pcbi. 1004042 . g002
for all of the GBM modules. Based on the pathway enrichment test, $74.0 \%$ of the modules were enriched in biological functions or signaling pathways.

Because our approach includes genes belonging to multiple modules, we calculated the overlap ratios of genes and miRNAs among the modules. The overlap ratio is defined as $\left|m_{1} \cap m_{2}\right| /$ $\left|m_{1} \cup m_{2}\right|$, where $m_{1}$ and $m_{2}$ are the number of genes or miRNAs in module 1 and module 2,

Table 1. Cancer genes, ovarian cancer genes and ovarian cancer miRNAs for selected modules.


${ }^{a}$ Num1 represents the number of cancer genes / the number of all genes in a module,
${ }^{b}$ Num2 the number of ovarian cancer genes / the number of all genes in a module, and
${ }^{c}$ Num3 the number of ovarian cancer miRNAs / the number of all miRNAs in a module.
doi:10.1371/journal.pcbi. 1004042 .0001
respectively. Figs. S4 and S5 show the overlap ratios among the modules. The average overlap ratios of genes were $1.6 \%$ and $2.0 \%$ for ovarian cancer and GBM, respectively, and the average overlap ratios of miRNAs were $7.3 \%$ and $14.2 \%$ for ovarian cancer and GBM, respectively. The overlap ratios of miRNAs are higher than the overlap ratio of genes, indicating that a miRNA regulates many genes involved in several pathways.

# Relationship among genes, miRNAs and TFs in modules 

As described in the Methods section, we examined the direct relationships between genes and miRNAs and their indirect relationships through TFs in the identified modules, as well as experimentally validated interactions between genes and miRNAs. For the ovarian cancer modules, we tested the direct relationship based on whether potential targets of a miRNA in the module were enriched for the genes in the same module using MicroCosm. Table 2 shows 8 miRNAs and their target genes in 12 ovarian cancer modules. For example, in Table 2, let-7b

Table 2. miRNAs regulate genes in ovarian cancer modules.


${ }^{a} m$,
${ }^{b} k$, and
${ }^{c} x$ represent the number of genes regulated by the miRNA collected from MicroCosm, the number of genes in the module, and the number of genes regulated by the miRNA in the module, respectively. The significant numbers of genes in each module are regulated by the miRNA, and the significances are shown in
${ }^{d} p$-value.
doi:10.1371/journal.pcbi. 1004042 . t002
may directly regulate several genes (ESPL1, DEPDC1, BUB1B, AURKB and UBE2C) in module 33. Additionally, 19 gene-miRNA direct interaction pairs that were experimentally confirmed in miRTarbase are shown in Table 3. Previously, it was confirmed using a luciferase reporter assay and the western blot method that miR-93 targets E2F1. Also, it was confirmed using a luciferase reporter assay that miR-125b targets BCL3 in ovarian cancer cell [41]. All 156 genemiRNA interaction pairs experimentally validated in miRTarbase are shown in Table S7, which includes both direct and coexpression based interactions.

Table S8 shows the indirect relationships in 19 ovarian cancer modules, where genes and miRNAs are co-regulated by the same TF. Note that some TFs are not members of the modules. Regulation of miRNAs by TFs is validated by literature evidence (PubMed IDs are shown in the table), and the significance of the regulations of the genes in the modules by TFs was demonstrated using $p$-values that were obtained based on the ChIP-X database [26]. In many modules, one TF regulates multiple miRNAs and multiple genes. For example, Fig. 3 (A) shows ovarian cancer module 22, in which the TF EGR1 positively regulates several genes (AEBP1, COL1A1, COL5A1, COL5A3, COL6A1, ITGA5, LOXL2, MMP11, MMP2 and THBS2) and miRNAs (miR-214 and miR-152). Fig. 3 (B) shows ovarian cancer module 8, in which EGR1 positively regulates several genes (AQP1, BGN, CALB2, CEND1, COL1A1, COMP, HNT, IRX5, ITGA5 and ITGB1) and miRNAs (miR-214, miR-152, miR-199a and miR-199b) in the module at the same time. In both cases, we can infer that the genes and miRNAs are indirectly related via EGR1.

Table S9 shows another type of indirect relationship in ovarian cancer, where miRNAs regulate TFs, and the TFs regulate genes in 14 ovarian cancer modules. Regulation of TFs by miRNAs was found in the literature, and is shown in the third column of the table. One example of this relationship is shown in Fig. 3 (C): let-7b directly regulates the TF BACH1, and BACH1 regulates several genes (BUB1, CCNA2, CENPF, MCM10, BIRC5, TK1, OIP5, KIF11, RRM2 and CENPA); miR-156b and let-7b regulate the TF E2F1, which regulates several genes and

Table 3. Experimentally validated gene-miRNA interactions with strong evidence from miRTarbase in ovarian cancer modules.


doi:10.1371/journal.pcbi.1004042.t003
other miRNAs in the modules; and miR-101, miR-29a, miR-29b and miR-29c regulate the TF MYCN, which regulates genes in the module. This module is related to ovarian cancer-related pathways such as those involved in mitosis and the cell cycle.

Similarly, relationships among genes, miRNAs, and TFs in GBM modules are shown in Fig. 4 and in Tables S10, S11, and S12. Table S10 shows 8 miRNAs and their target genes in 12 GBM modules. Genes targeted by miRNAs were highly enriched in these modules. In addition, Tables S11 and S12 show indirect relationships between genes and miRNAs through TFs. Fig. 4 (A) shows one example of an indirect relationship in GBM module 11, where even though genes might not be directly regulated by miRNAs, they are indirectly related via two TFs: RUNX1 and TCF4. For ease of reference, the genes in module 11 were divided into three groups $\left(G_{A}, G_{B}\right.$ and $\left.G_{C}\right)$ : the TF RUNX1 positively regulates miR-221, miR-222, and genes in $G_{A}$ and $G_{B}$; miR-155 negatively regulates the TF TCF4; and TCF4 positively regulates genes in $G_{B}$ and $G_{C}$. Similarly, Fig. 4 (B) shows that miR-29a regulates the TF MYCN, which regulates several genes and miR-93 in GBM module 5. Experimentally validated 438 gene-miRNA interactions from the miRTarbase are shown in Table S13, including 112 direct interactions. In addition, we verified in the literature that miR-21 interacts with BMPR2 and miR-222 interacts with ICAM1 in GBM cell [42].

Fig. S6 summarizes these direct and indirect relationships in the ovarian cancer and GBM modules. These analyses show that, in total, $91 \%$ ( 30 out of 33 ) of ovarian cancer modules and $94 \%$ ( 51 out of 54 ) of GBM modules can be explained by direct regulations or indirect relationships, which allows us to understand how genes are regulated in modules.

# Pathway enrichment tests and network analysis for ovarian cancer 

To determine the functional relevance of modules identified in ovarian cancer, we performed pathway enrichment tests for GO biological processes, KEGG pathways, and BioCarta

![img-6.jpeg](img-6.jpeg)

Figure 3. Regulations among genes, miRNAs, and TFs in ovarian cancer modules. For three ovarian cancer modules-22 (A), 8 (B), and 33 (C)-the expression values of genes, miRNAs, and TFs are shown. Arrows represent genes and miRNAs regulated by TFs or other miRNAs. Genes and miRNAs are members of each module, but TFs do not belong to the modules.

![img-7.jpeg](img-7.jpeg)

Figure 4. Regulations among genes, miRNAs, and TFs in GBM modules. For two GBM modules, 11 (A) and 5 (B), the expression values of genes, miRNAs, and TFs are shown. Arrows represent genes and miRNAs regulated by TFs or other miRNAs. Genes and miRNAs are members of each module, but TFs do not belong to the modules.
doi:10.1371/journal.pcbi.1004042.g004
pathways. We found that 16 out of 33 modules ( $48.4 \%$ ) were enriched in at least one function. Table 4 presents enriched functions or signaling pathways for selected modules. Several modules have many enriched functions or pathways related to ovarian cancer, such as the p53 signaling pathway [43], ECM receptor interactions [44], and cell cycles [45]. Tables S14, S15, and S16 present lists of all enriched pathways. As mentioned previously, on average, $19.1 \%$ of genes in our modules were cancer genes and $5.7 \%$ were ovarian cancer genes. Our further manual literature search revealed that most of the cancer genes in several modules are also ovarian can-cer-related genes, suggesting that cancer genes in the modules have a high potential to be ovarian cancer-related genes. In addition, most of the enriched modules had at least one ovarian cancer gene, supporting the idea that all enriched modules might be related to ovarian cancer. Therefore, we extensively analyzed modules 22 and 8 because module 22 has a relatively high fraction of ovarian cancer genes ( $12.8 \%$ ) and cancer genes ( $28.2 \%$ ) and is enriched for important pathways in ovarian cancer, and module 8 also contains a high fraction of ovarian cancer genes ( $18.5 \%$ ), cancer genes ( $33.3 \%$ ), and three enriched pathways related to ovarian cancer.

Fig. 5 shows a network representation of module 22, where 25 genes ( 2 genes are not shown) and 6 miRNAs are presented as nodes. In this module, 5 genes (FN1, MMP2, MMP1, PLAU, and SPARC), colored in green, were identified as ovarian cancer-related genes in the DDOC database. Moreover, the literature showed that 14 genes (ITGA5, COL6A1, THBS2, COL1A1, MMP19, MMP11, CTSK, ECM1, GREM1, VCAN, LOXL2, ADAM12, FAP, and INHBA), colored in pink, are ovarian cancer genes (shown in Table S17) and that these genes have high-average SCC values with at least one miRNA colored in sky blue. Most of the genes enriched in ECM receptor interaction, focal adhesion and proteolysis pathways are green or pink nodes, suggesting that these pathways are closely related to ovarian cancer. The literature

Table 4. Ovarian cancer modules with enriched pathways.


Table 4. (Continued)


${ }^{a}$ Several ovarian cancer modules are shown with enriched
${ }^{b}$ pathways and
${ }^{c}$ cancer genes. We selected these modules based on the importance of terms and the ratios of cancer genes and ovarian cancer genes.
doi:10.1371/journal.pcbi.1004042.t004
![img-8.jpeg](img-8.jpeg)

Figure 5. Network presentation of module 22 in ovarian cancer. In this network, diamonds represent miRNAs: sky-blue nodes for ovarian cancer miRNAs from the HMDD database, pink nodes for ovarian cancer miRNAs supported by the literature, and yellow nodes for the remaining miRNAs. Genes are represented by circles: pink nodes for ovarian cancer genes validated by the literature, green nodes for ovarian cancer genes validated by the DDOC database, orange nodes for cancer genes, and white nodes for the remaining genes. A blue solid line indicates that the MCC value between a gene and a miRNA is larger than 0.3. A purple line indicates that the linked genes are enriched together with at least one function. For example, COL6A1, COL5A3, THBS2, FN1, COL1A1, COL5A1, COLA1A, and COL3A1 are enriched with at least one function together (ECM receptor pathway or Focal adhesion pathway). Table S17 presents PubMed identifiers for ovarian cancer genes in pink nodes.
doi:10.1371/journal.pcbi.1004042.g005

confirms that these pathways are related to ovarian cancer [44, 46, 47]. In this module, COL3A1 might be related to ovarian cancer, as it is a known cancer gene targeted by all ovarian cancer miRNAs and belongs to ECM receptor and focal adhesion pathways. COL5A1 and COL5A3 are also likely to be ovarian cancer genes: they are targeted by ovarian cancer miRNAs and enriched in the above pathways, although they are not known cancer genes. Similarly, DPT also might be an ovarian cancer gene, as it is a cancer gene and is targeted by all ovarian cancer miRNAs. Evidence in the literature shows that the previously known ovarian cancer-related miRNAs miR-152, miR-22, and miR-214 are also related to enriched pathways in this module: miR-152 is involved in ECM-receptor-interaction [48, 49], and miR-22 and miR-214 regulate the AKT/PTEN pathway and the p53 signaling pathway [50, 51], which are highly related to the ECM-receptor, focal adhesion and proteolysis pathways [52-55]. These observations support the idea that genes and miRNAs interact with each other and play critical roles at the pathway level.

Fig. 6 illustrates module 8, which contains 34 genes and 8 miRNAs ( 5 genes are not shown). Because several genes and miRNAs are duplicated in module 22, the same pathways (ECM receptor and focal adhesion) are enriched. However, other important pathways in ovarian cancer, such as the TGF-beta signaling pathway and the complement and coagulation cascades pathway, are also enriched [56]. From this module, COL16A1, COL3A1, and COL1A2 are likely to be ovarian cancer genes, as they are cancer genes and are enriched with at least one pathway containing ovarian cancer genes. For miRNAs, several articles support that miR-199a, miR-199b, miR-214, and miR-382 are involved in the TGF-beta signaling pathway [57-60], and that miR-22 regulates the AKT/PTEN pathway [50, 51], which is closely related to the TGF-beta signaling pathway in several cancers [50, 61].
![img-9.jpeg](img-9.jpeg)

Figure 6. Network presentation of module 8 in ovarian cancer. The description of this network is the same as in Fig. 5 except that red lines are used to represent two enriched pathways (complement and coagulation cascades pathway, and TGF signaling pathway).
doi:10.1371/journal.pcbi.1004042.g006

Pathway enrichment tests and network analysis for GBM

We performed pathway enrichment tests for modules identified from the GBM data set. Of 54 modules tested, $40(74 \%)$ were enriched with at least one function. Several modules had many enriched functions or pathways related to GBM, such as the p53 signaling pathway [62], the ERBB signaling pathway [63], and the MAPK signaling pathway [64]. Tables S18, S19, and S20 present lists of enriched pathways. As mentioned above, on average, $23.2 \%$ of genes in the modules were cancer genes, and $1.2 \%$ were GBM genes. A list of GBM genes was extracted from two articles [34, 35]. Similarly to ovarian cancer, the literature results demonstrated that most of the cancer genes in our modules were also GBM-related genes, suggesting that cancer genes in the modules are likely to be related to GBM. We extensively analyzed module 11 because this module contained many GBM-related genes and pathways.

Fig. 7 illustrates a network presentation of module 11, where 74 genes ( 15 genes are not shown) and 7 miRNAs are presented as nodes. In this module, 4 genes (MAPK1, CDKN1A, SHC1, and ERBB2), colored in green, are GBM genes that were validated by the literature. Most of the genes on the left side of Fig. 7 are cancer genes and are enriched with at least one pathway, including the p53, ERBB, and GRNH signaling pathways. CBLC might be involved in the development of GBM because it is a cancer gene and is contained in the ERBB signaling pathway, an important GBM-related pathway that includes four GBM genes in this module. Additionally, the literature shows that miRNAs in this module function together in the enriched pathways: miR-34a, miR-135, miR-21, mi-222, miR-221, miR-27a, and miR-34b are involved in the p53 signaling pathway [65-71] and the MAPK signaling pathway [71-75], and miR-34a, miR-135, miR-21, miR-222, and miR-221 are involved in the ERBB signaling pathway $[76-79]$.
![img-10.jpeg](img-10.jpeg)

Figure 7. Module 11 in GBM. The description of this network is the same as in Fig. 5, except that green nodes indicate GBM genes validated by two articles [34, 35], and pink nodes indicate GBM genes validated by the literature in PubMed. Table S17 presents PubMed identifiers for GBM genes.
doi:10.1371/journal.pcbi.1004042.g007

# Cancer subtypes of modules 

In Bell et al. [8], ovarian cancer was classified into four ovarian cancer subtypes depending on the expression levels of marker genes: "immunoreactive," "proliferative," "differentiated," and "mesenchymal." The immunoreactive subtype was identified by the chemokine receptor CXCR3 and its ligands CXCL11 and CXCL10, indicating that considerable expression changes of these genes are important markers for identifying the subtype. The proliferative subtype was identified by the overexpression of transcription factors HMGA2 and SOX11, proliferation marker genes such as MCM2 and PCNA, and underexpression of MUC1 and MUC16, which are known ovarian tumor marker genes. The differentiated subtype was identified by overexpression of MUC16, MUC1 and SLPI. Finally, the mesenchymal subtype was identified by overexpression of FAP and ANGPTL2.

In this study, we used the marker genes described above to determine which subtype was related to the majority of samples in the modules. First, we calculated the average expression level of the marker gene in the samples belonging to the module. Fig. 8 (A) represents the average expression levels of the 12 subtype marker genes across 33 ovarian cancer modules, showing that the expression levels of marker genes vary depending on the modules. As explained in the Methods section, we identified the cancer subtypes of samples by performing a hierarchical clustering with a dynamic tree cut (minModuleSize $=30$ ) using gene expression data, and then we calculated the $p$-values of marker genes for the identified modules. As shown in Fig. 8 (B), among marker genes in the immunoreactive subtype, CXCL10 is underexpressed in module 5 ( $p$-value: 0.08 ), and all of the marker genes (CXCL10, CXCL11 and CXCR3) are overexpressed in module 18 ( $p$-values: $0.04,0.02$ and 0.67 ). Marker genes of the mesenchymal subtype are overexpressed in module 10 ( $p$-values: 0.0003 and 0.0002 ), module 23 ( $p$-values: 0.03 and 0.66 ), and module 32 ( $p$-values: 0.02 and 0.09 ).

In Verhaak et al. [37], GBM was classified into four subtypes depending on the marker genes: "proneural," "neural," "classical," and "mesenchymal." It was observed that marker genes DLL3, NKX2-2, SOX2, ERBB3, and OLIG2 were overexpressed in the proneural subtype; marker genes FBXO3, GABRB2, SNCG and MBP were overexpressed in the neural subtype; FGFR3, PDGFA, EGFR, AKT2, and NES were overexpressed in the classical subtype; and CASP1, CASP4, CASP5, CASP8, ILR4, CHI3L1, TRADD, TLR2, TLR4, and RELB were overexpressed in the mesenchymal subtype. Note that marker genes of the GBM subtype were overexpressed in samples belonging to that subtype, while marker genes of other GBM subtypes were underexpressed in those samples.

For GBM, we first calculated the average expression levels of marker genes. Fig. 9 (A) presents the average expression levels of the 23 subtype marker genes across 54 GBM modules, and shows the distinct expression levels of marker genes depending on the modules. Fig. 9 (B) shows 6 modules related to GBM marker genes. Marker genes in the proneural subtype (DLL3, NKX2-2, SOX2, ERBB3 and OLIG2) are overexpressed in module 7 ( $p$-values: $0.01,0.001$, $0.0002,0.07$ and 0.004 ) and module 15 ( $p$-values: $0.001,0.00003,0.002,0.017$ and 0.007 ). All of the marker genes in the mesenchymal subtype (CASP1, CASP4, CASP5, CASP8, ILR4, CHI3L1, TRADD, TLR2 and RELB), except TLR4, are overexpressed in module 22 ( $p$-values: $0.001,0.001,0.003,0.022,0.048,0.001,0.036$ and 0.0004 ). Two marker genes (SNCG and MBP) in the neural subtype are overexpressed in module 32 ( $p$-values: 0.07 and 0.0001 ), all of the marker genes in the neural subtype (FBXO3, GABRB2, SNCG and MBP) are overexpressed in module 45 ( $p$-values: $0.02,0.02,0.11$ and 0.02 ), and two marker genes in the neural subtype (FBXO and MBP) are overexpressed in module 51 ( $p$-values: 0.05 and 0.03 ). In addition, we obtained the subtype classification of GBM samples from Carro et al. [80], which shares 162 samples in common with our study (proneural: 62, neural: 22, classical: 35 and mesenchymal: 53).

A
![img-11.jpeg](img-11.jpeg)

B
![img-12.jpeg](img-12.jpeg)

Figure 8. Expression levels of ovarian cancer subtype marker genes. (A) Heat map of the means of marker gene expression levels for 32 ovarian cancer modules. Red indicates overexpression of genes, and green indicates underexpression of genes. (B) Expression levels of marker genes of selected modules. Blue bars represent marker genes that determine the subtype and red bars represent other subtype marker genes.
doi:10.1371/journal.pcbi.1004042.g008

A
![img-13.jpeg](img-13.jpeg)

Figure 9. Expression levels of GBM subtype marker genes. (A) Heat map of the means of marker gene expression levels for 54 GBM modules. Red indicates overexpression of genes, and green indicates underexpression of genes. (B) Expression levels of marker genes of selected modules. Blue bars represent marker genes that determine the subtype, and red bars represent other subtype marker genes.
doi:10.1371/journal.pcbi.1004042.g009

When we used these subtypes of samples for the enrichment of a particular subtype in our modules through a hypergeometric test, we confirmed that modules 32 and 45 are closely related to the neural subtype ( $p$-values: 0.053 and 0.018 ).

# Performance comparisons 

Zhang et al. [6] previously showed that their NMF approach outperformed the bi-clique algorithm proposed by Peng et al. [5]. Hence, we assessed the performance of our approach by comparing it with the NMF approach using TCGA ovarian cancer data. By applying our criteria to the modules generated from their approach, we selected modules having at least one gene and two human miRNAs. As a result, we removed 7 out of 50 modules. Fig. 10 shows that the ratio of modules containing enriched pathways in the NMF approach was slightly higher than the ratios of our modules. However, the average number of enriched pathways in our modules was larger than that in the NMF approach.

When we compared enriched pathways, two approaches had 43 common pathways, including ovarian cancer-related pathways such as the immune response, ECM-receptor, and TGFBeta signaling pathways. In addition, 71 pathways were enriched only in our modules and 67 pathways only in the NMF modules, indicating that the two approaches most likely complement each other and capture different pathways related to ovarian cancer. Table S21 lists the common pathways and pathways enriched in each approach.

Additionally, modules identified by our approach contain more differentially expressed genes and cancer-related genes, because we primarily used differentially expressed genes, which provide more chances to incorporate cancer type-specific genes. In Zhang et al. [6], the modules contain a small fraction of differentially expressed genes and cancer-related genes, because 12,456 genes were used after filtering out genes with small absolute values and little variation. When we computed the overlap ratios of differentially expressed gene, most genes in our modules ( $79.4 \%, 617$ out of 777 genes) were differentially expressed. However, modules generated by Zhang et al. [6] contained $28.3 \%$ ( 462 out of 1630 genes) differentially expressed genes on average. When we compared ratios of cancer genes, ovarian cancer genes, and ovarian cancer miRNAs in modules, our approach outperformed the NMF approach, as shown in Fig. 10.

The difference between the NMF approach and ours from a methodological viewpoint is that our approach can be more flexibly generalized to incorporate other regulatory components. In our approach, gene-sample modules are first constructed, and then miRNAs regulating genes are added to the modules (generating gene-miRNA modules). To demonstrate the range of our approach, we incorporated DNA copy number aberrations (CNAs) as another type of regulators in gene-sample modules. As a result, 23 out of 58 ovarian cancer gene-sample modules were explained by the regulation of CNAs, and 15 ovarian cancer gene-sample modules were explained by both miRNAs and CNAs. A detailed analysis regarding regulations by CNAs is provided in the Discussion section. By contrast, the NMF approach simultaneously incorporates gene-expression, miRNA expression, gene-gene interaction, and gene-miRNA sequence prediction information. Hence, when other regulators are included, they generate modules, where correlations between genes and regulators are simultaneously high. Indeed, in another paper from the same authors [81], they extended their NMF model to incorporate miRNAs, genes, and methylation of genes. In the generated modules, correlations of the expression levels of these three data sets were coordinately high due to a common basis matrix. Although it is a good approach, it omits modules representing the regulation of genes by a single type of regulators when incorporating multiple regulators.

Additionally, we compared our approach with the Context-Specific MicroRNA analysis (COSMIC) algorithm [82] using TCGA ovarian cancer data. COSMIC combines gene-miRNA

![img-14.jpeg](img-14.jpeg)

Figure 10. Performance comparisons. Comparison of modules identified using our approach and the NMF approach using ovarian cancer data. (A) The ratio of modules with at least one enriched function or pathway. (B) The average number of enriched functions in the identified modules. (C) The average ratios of cancer genes, ovarian cancer genes, and ovarian cancer miRNAs in the modules.
doi:10.1371/journal.pcbi.1004042.g010
target prediction information, mRNA expression, and miRNA expression data. The modules constructed by the COSMIC algorithm consisted of a single miRNA and genes, which indicated that several genes are regulated by the miRNA. When we applied a $q$-value threshold of $<$ 0.05 to 479 identified modules, 102 modules were obtained. Since COSMIC generates modules consisting of a single miRNA, it is difficult to directly compare COSMIC with our approach. Hence, we applied pathway enrichment tests using GO biological processes and BioCarta and KEGG pathways with a $q$-value threshold of $<0.05$ to these 102 modules, and observed that $25.5 \%$ ( 27 out of 102) of the modules were significantly enriched. This enrichment ratio is lower than the value obtained using our approach ( $48.4 \%$ ). However, we need to consider that the higher enrichment ratio in our approach is partially because two studies developed algorithms using different data sets and different assumptions. We incorporated gene-gene interactions and indirect interactions among genes and miRNAs based on mRNA expressions and miRNA expressions, while COSMIC incorporated direct interactions using sequence information of genes and miRNAs, which might reduce false positive interactions. In spite of the differences, the two approaches had 26 common pathways, including ovarian cancer-related pathways such as the ECM-receptor, DNA replication, and the G2 pathway. In addition, 88 and 38 pathways were enriched only in our modules and only in the COSMIC algorithm, respectively. Table S22 lists the common pathways as well as the pathways enriched in each approach.

# Discussion 

In this study, we developed an approach to constructing gene-miRNA modules by integrating genes and miRNAs. We applied our approach to ovarian cancer and GBM data sets from the TCGA project. Finally, we constructed 33 modules for ovarian cancer and 54 modules for

GBM. We employed gene-gene interactions to include genes with high absolute correlations with genes in the modules, because some important cancer-related genes might not be clustered together by the biclustering algorithm or might not be differentially expressed. Fig. 2 shows that incorporating gene-gene interactions increased the performance in terms of the average number of enriched terms, the number of modules with at least one enriched pathway, and the ratios of cancer-related genes and cancer-related miRNAs. Although we used genegene interactions to add biologically relevant genes to modules in the proposed approach, gene-gene interactions can be used to filter out biologically irrelevant genes from modules to reduce false positives. However, because the currently available human gene-gene interactions are not complete, closely related but unidentified genes might also be filtered out. It is an important challenge to incorporate gene-gene interactions to reduce false positive genes in modules, while true relevant genes still remain. We will address this issue in our future work.

Because the identified modules might miss relevant interactions, we measured a potential false negative rate using miRTarbase. Let $N_{G}$ be the number of common genes in the modules and miRTarbase, and let $N_{G \_interaction }$ be the number of common genes that interact with the same miRNAs in the modules and miRTarbase. Then, $1-N_{G \_interaction} / N_{G}$ might be a potential false negative rate. As a result, the rates of false negative were $0.789(1-118 / 559)$ for ovarian cancer and $0.775(1-316 / 1405)$ for GBM, respectively. However, the false negative rate should be adjusted when more accurate miRNA-gene interaction data become available, as this ratio is estimated based on all gene-miRNA interactions from miRTarbase and is not based on the specific cancer type and miRTarbase, which itself contains only a fraction of the gene-miRNA interactions.

In the Results section, we described a functional enrichment test of genes in modules using GO terms, KEGG, and BioCarta pathways. Although we employed a widely used approach in the enrichment test, a hypergeometric test followed by a Benjamini \& Hochberg method for multiple comparison correction, several issues that require further improvement still remain. For the first issue, the Benjamini \& Hochberg method hypothesizes independence of the terms, while the biological processes in various ontologies represent a hierarchical structure and intercorrelation. Thus, we performed an additional enrichment test for ovarian cancer and GBM modules using TANGO [83], which considers dependencies among biological pathways. It corrects $p$-values by computing the distribution of enrichment $p$-values in a large number of randomly generated gene sets of the same size. For ovarian cancer, 16 of 33 modules ( $48 \%$ ) were enriched with at least one GO biological process term. For GBM, 28 out of 54 modules ( $48 \%$ ) were enriched with at least one term. Tables S23 and S24 list all pathways enriched in each cancer. Further, Fig. S7 shows a comparison of the two approaches (a Benjamini \& Hochberg method and TANGO) in terms of the ratio of enriched modules and the number of enriched terms. Although there are small differences in the two approaches, both approaches confirm that a large fraction of our identified modules were enriched with biologically relevant terms. For the second issue, because annotated pathways in GO terms, KEGG, and BioCarta pathways are still incomplete, validations on these pathways might miss biologically related sets of genes. An approach to reveal the pathways unannotated in GO, KEGG and BioCarta is to search for evidence about gene functions in the literature, and then to analyze them collectively. As part of such efforts, we manually searched scientific articles on ovarian cancer-related genes and GBM-related genes (Table S17), and relationships among genes, microRNAs, and TFs (Tables S8, S9, S11, and S12). However, this approach only solves the above problem partially so a more systematic approach is called for. Very few efforts, including LitVan (http://www.c2b2. columbia.edu/danapeerlab/html/software.html), have been developed to carry out an automatic literature search to connect genes with over-represented biological terms in millions of scientific articles. Although we attempted to analyze our modules using such tools, either there are

no currently available tools or websites are not connected. Hence, we will further analyze modules for functional enrichments in the future.

Certain oncogenes and tumor-suppressor genes such as P53 and PTEN may play important roles in many cancer types rather than only in specific cancer type. Hence, we examined how many genes in the identified modules were specific to ovarian cancer or GBM. We collected 1393 genes from five cancer type specific databases: the DDOC [33], GBM genes from the literature [34, 35], the Cervical Cancer gene Database (CCDB) [84], the Dragon Database of Genes associated with Prostate Cancer (DDPC) [85], and Lung Cancer Gene Database (LUGEND). We refer to genes contained only in the DDOC as potentially ovarian cancer specific genes. Although these genes are not compared with genes from all types of cancers, it might helpful to remove common cancer genes. Among the 47 DDOC genes included in our ovarian cancer modules, 18 genes were potentially ovarian cancer specific genes. Similarly, among the 32 GBM genes included in our GBM modules, 7 genes were potentially GBM cancer specific genes. Lists of these cancer type specific genes are shown in Table S25.

The accuracy of the identified modules might be largely dependent on the quality of the data sets. In this study, we used TCGA microarray data sets, as in many previous reports they have been used to identify core genes and pathways significantly related to ovarian cancer and GBM. Additionally, when TCGA microarray data sets were compared to RNA-Seq data from the same samples, their expression values were highly correlated in most cases [86] confirming that these data sets are less dependent on a particular platform.

The proposed approach can be generalized to incorporate other regulatory components. To demonstrate the range of applicability of our approach and to provide additional support of biological relevance to the modules, we incorporated somatic DNA copy numbers from the paired patients of gene expression data. For this task, we downloaded TCGA level 3 data sets that provide segmented copy number ratio data compared to normal samples. We first recalculated the copy number aberration ratios for every 1 MB region and filtered out regions whose absolute copy number ratio values are less than 0.2 , corresponding to $99.9 \%$ among all ratio values. Then, CNA regions were incorporated into gene-sample modules based on correlations between genes in modules and CNA regions. As a result, for the ovarian cancer modules, 23 out of 58 gene-sample modules were explained by the regulation of CNAs, and genes in 15 out of 33 gene-miRNA modules ( $45 \%$ ) were also regulated by CNAs, as shown in Table S26. In particular, genes in several modules were located in the regulating CNA regions, indicating that the expression of genes in the modules might be directly affected by CNAs. DNA copy numbers in the chr 1: 32.1 MB - 53.4 MB region were highly correlated with genes in ovarian cancer module 9 with a PCC value of 0.301 , and 13 out of 18 genes in the module (CDCA8, C1orf109, AK2, SNIP1, GNL2, RLF, TRIT1, YRDC, RRAGC, PPIE, PSMB2, MED8 and COL9A2) were located in this CNA region. Similarly, the DNA copy numbers in the chr 1: 180.6 MB - 247.9 MB region were highly correlated with genes in ovarian cancer module 23 with a PCC value of 0.319 , and most of genes ( 14 out of 19 genes) in this module were located in this region. Additionally, for ovarian cancer module 29, DNA copy numbers in chr 1: 31.9 MB - 59.1 MB regions have a high correlation value ( 0.345 ) with gene in the module, and $78.3 \%$ of the genes are located in this region. For GBM, 26 out of 88 gene-sample modules were explained by regulation of the DNA copy numbers shown in Table S27, and 19 out of 54 genemiRNA modules ( $35 \%$ ) were commonly regulated by CNAs and miRNAs.

# Supporting Information 

S1 Fig. The SAMBA biclustering algorithm. In a SAMBA biclustering algorithm, it models gene expression data into a bipartite graph $G=(U, V, E)$. In this graph, $U$ is a set of samples, $V$

is a set of genes and $E$ is a set of edges between $U$ and $V$. Nodes in one side are genes and nodes in the other side are samples. An edge is linked if the expression value of gene for sample is high or low. This means that gene expression level of $v$ significantly changes in sample of $u$. In this model, we try to find a subgraph $G^{\prime}=\left(U^{\prime}, V^{\prime}, E^{\prime}\right)$ of $G$, where expression values of most genes in $V$ significantly change in most of samples in $U^{\prime}$, representing low values or high values. For example, genes $G 3, G 4$, and $G 5$ in $V^{\prime}$ and $S 3$ and $S 4$ samples $U^{\prime}$ are constructed as a module (a circle colored in grey). For gene expression data normalized by a z-score, the SAMBA biclustering algorithm generates highly correlated gene-sample clusters that represent similar tendencies of gene expression changes for a subset of samples.
(TIF)

# S2 Fig. Distribution of the number of pathway terms. 

(TIF)
S3 Fig. Performance comparison of gene-miRNAs modules for GBM. Performances of gene-miRNA modules generated from four cases (SCC with GGI information, SCC without GGI information, PCC with GGI information, and PCC without GGI information) are compared. For all cases, $x$-axis presents different percentages of candidate miRNAs ( $T \%$ ) among all miRNAs when constructing gene-miRNA modules. For each case, ratios of modules enriched with at least one pathway, the average number of enriched pathways, and ratios of cancer genes, GBM genes, and GBM miRNAs are shown.
(TIF)
S4 Fig. Overlap ratio of genes in ovarian cancer modules. For every pairs of ovarian cancer modules, the overlap ratios of genes are defined as $\left|m_{1} \cap m_{2}\right| /\left|m_{1} \cup m_{2}\right|$, where $m_{1}$ and $m_{2}$ are numbers of genes in module 1 and module 2, respectively.
(TIF)
S5 Fig. Overlap ratio of genes in GBM modules. The description of the overlap ratios is the same as in Fig. S4.
(TIF)
S6 Fig. Ratios of modules having four types of gene-miRNA relationships in ovarian cancer and GBM modules. $y$-axis represents the fraction of modules containing at least one corresponding relationship in the modules. 'microCosm' represents gene-miRNA interactions based on gene-miRNA sequences from the microCosm database, and 'miRTarbase' represents experimentally confirmed gene-miRNA relationships from miRTarbase. 'TF regulates genes and miRNAs' represents that genes and miRNAs are co-regulated by the same TF. 'MiRNA regulates genes via TFs' represents that miRNA regulates transcription factors and transcription factors regulates genes. 'Union' represents all four types of relationships.
(TIF)
S7 Fig. Functional enrichment tests using a Benjamini \& Hochberg method and a TANGO tool. GO biological terms were tested for functional enrichment of genes in ovarian cancer and GBM modules. Two multiple comparison correction approaches, a Benjamini \& Hochberg (BH) method and a TANGO tool, were used after a hypergeometric test. GO terms employed in the two approaches were not exactly same, because TANGO, which were included in an EXPANDER software, uses its own collection of GO terms, and filters out redundant terms by computing an intersection between genes in two terms. However, in both approaches, ovarian cancer and GBM modules were enriched with GO terms. (A) and (C) show the ratios of modules enriched with at least one term for ovarian cancer and for GBM, respectively, and (B) and (D) represent the average numbers of enriched terms in identifiied modules for ovarian cancer

and GBM, respectively.
(TIF)
S1 Table. Genes in ovarian cancer modules.
(PDF)
S2 Table. MiRNAs in ovarian cancer modules.
(PDF)
S3 Table. Genes in GBM modules.
(PDF)
S4 Table. MiRNAs in GBM modules.
(PDF)
S5 Table. Cancer genes, ovarian cancer genes and ovarian cancer miRNAs in modules. 'Num' represents the number of ovarian cancer genes (or ovarian cancer miRNAs) / the number of all genes (or all miRNAs) in a module.
(PDF)
S6 Table. Cancer genes, GBM genes and GBM miRNAs in modules. 'Num' represents the number of GBM genes (or GBM miRNAs) / the number of all genes (or all miRNAs) in a module.
(PDF)
S7 Table. Exprementally validated gene-miRNA interactions in ovarian cancers. (PDF)

S8 Table. Genes and miRNAs are co-regulated by the same TF in ovarian cancer modules. (PDF)

S9 Table. MiRNA regulates TFs and the TFs regulate genes in the ovarian cancer modules. (PDF)

S10 Table. MiRNAs regulate genes in GBM modules. The significant numbers of genes in each module are regulated by miRNAs, and the significances are shown in ' $p$-value'. ' $m$ ', ' $k$ ', and ' $x$ ' represent the number of genes regulated by the miRNA collected from microCosm, the number of genes in the module, and the number of genes regulated by the miRNA in the module, respectively.
(PDF)
S11 Table. Genes and miRNAs are co-regulated by the same TF in GBM modules. (PDF)

S12 Table. MiRNA regulates TFs and the TFs regulate genes in GBM modules. (PDF)

S13 Table. Exprementally validated gene-miRNA interactions in GBM.
(PDF)
S14 Table. Ovarian cancer modules with enriched GO terms. The significant numbers of genes in each module are enriched in gene ontology biological process, and the significance is shown in ' $p$-value'. ' $m$ ', ' $k$ ', and ' $x$ ' represent the number of genes in the corresponding GO term, the number of genes in the module, and the number of genes belonging to the GO term in the module, respectively.
(PDF)

S15 Table. Ovarian cancer modules with enriched pathways in KEGG. The significant numbers of genes in each module are enriched in KEGG pathway, and the significance is shown in 'p-value'. ' $m$ ', ' $k$ ', and ' $x$ ' represent the number of genes in the corresponding KEGG pathway, the number of genes in the module, and the number of genes belonging to the pathway in the module, respectively.
(PDF)
S16 Table. Ovarian cancer modules with enriched pathways in BioCarta. The significant numbers of genes in each module are enriched in BioCarta pathways, and the significance is shown in 'p-value'. ' $m$ ', ' $k$ ', and ' $x$ ' represent the number of genes in the corresponding BioCarta pathway, the number of genes in the module, and the number of genes belonging to the BioCarta pathway in the module, respectively.
(PDF)
S17 Table. Literature evidences for ovarian cancer-related genes from ovarian cancer modules 22 and 8, and GBM-related genes from GBM module 22.
(PDF)
S18 Table. GBM modules with enriched GO terms. The significant numbers of genes in each module are enriched in GO biological process, and the significance is shown in 'p-value'. ' $m$ ', ' $k$ ', and ' $x$ ' represent the number of genes in the corresponding GO term, the number of genes in the module, and the number of genes belonging to the GO term in the module, respectively. (PDF)

S19 Table. GBM modules with enriched pathways in KEGG. The significant numbers of genes in each module are enriched in KEGG pathways, and the significance is shown in 'pvalue'. ' $m$ ', ' $k$ ', and ' $x$ ' represent the number of genes in the corresponding pathway, the number of genes in the module, and the number of genes belonging to the pathway in the module, respectively.
(PDF)
S20 Table. GBM modules with enriched pathways in BioCarta. The significant numbers of genes in each module are enriched in BioCarta pathways, and the significance is shown in 'pvalue'. ' $m$ ', ' $k$ ', and ' $x$ ' represent the number of genes in the corresponding pathway, the number of genes in the module, and the number of genes belonging to the pathway in the module, respectively.
(PDF)
S21 Table. Comparisons of enriched pathways from the NMF approach and our approach. (PDF)

S22 Table. Comparisons of enriched pathways from the COSMIC algorithm and our approach.
(PDF)
S23 Table. Ovarian cancer modules enriched with GO terms using a TANGO tool. (PDF)

S24 Table. GBM modules enriched with GO terms using a TANGO tool. (PDF)

S25 Table. Ovarian cancer specific genes and GBM specific genes in identified modules. (PDF)

# S26 Table. DNA copy number aberration regions that regulate gene expressions in ovarian cancer modules. 

(PDF)

## S27 Table. DNA copy number aberration regions that regulate gene expressions in GBM modules.

(PDF)

## Author Contributions

Conceived and designed the experiments: DJ HL. Performed the experiments: DJ. Analyzed the data: DJ HL. Contributed reagents/materials/analysis tools: DJ. Wrote the paper: DJ HL.
