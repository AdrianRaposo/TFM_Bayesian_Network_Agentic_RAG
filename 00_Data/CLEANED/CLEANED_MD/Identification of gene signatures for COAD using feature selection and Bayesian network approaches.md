# Identification of gene signatures for COAD using feature selection and Bayesian network approaches 

Yangyang Wang ${ }^{1}$, Xiaoguang Gao ${ }^{1 \boxtimes}$, Xinxin Ru ${ }^{1}$, Pengzhan Sun ${ }^{1}$ \& Jihan Wang ${ }^{2 \boxtimes}$


#### Abstract

The combination of TCGA and GTEx databases will provide more comprehensive information for characterizing the human genome in health and disease, especially for underlying the cancer genetic alterations. Here we analyzed the gene expression profile of COAD in both tumor samples from TCGA and normal colon tissues from GTEx. Using the SNR-PPFS feature selection algorithms, we discovered a 38 gene signatures that performed well in distinguishing COAD tumors from normal samples. Bayesian network of the 38 genes revealed that DEGs with similar expression patterns or functions interacted more closely. We identified 14 up-DEGs that were significantly correlated with tumor stages. Cox regression analysis demonstrated that tumor stage, STMN4 and FAM135B dysregulation were independent prognostic factors for COAD survival outcomes. Overall, this study indicates that using feature selection approaches to select key gene signatures from high-dimensional datasets can be an effective way for studying cancer genomic characteristics.


Cancer is a major public health burden around the world, and it is the second leading cause of death in the United States ${ }^{1}$. According to the most recent American Cancer Society statistics for 2021, colon and rectum cancer (CRC) ranks the third in incidence and the third leading cause of cancer-related death worldwide. CRC remains one of the most common malignant tumors in the digestive system, and the type of colon adenocarcinomas (COAD) accounting for $95 \%$ of all cases of colon cancer ${ }^{2}$.

Cancers are well understood to be caused by genetic abnormalities in the target cells. In general, acquired mutations and epigenetic changes can influence tumor cell chromatin architecture and gene expression levels. As a result, identifying specific genetic markers that will promote molecular diagnosis and precision medicine in cancer is one of the most important aspects of cancer research. The Cancer Genome Atlas (TCGA, https://www. cancer.gov/tcga) program, an invaluable resource of cancer genomics, provides publicly available datasets for the development of improved methods for cancer diagnosis, treatment, and prevention ${ }^{3,4}$. The TCGA program molecularly characterizes over 20,000 primary cancer and matched normal samples spanning 33 cancer types, including COAD. Another human genomics project, the Genotype-Tissue Expression (GTEx, http://commo nfund.nih.gov/GTEx), establishes a reference resource of gene expression from 'normal', disease-free tissues ${ }^{5,6}$. The GTEx project was established to characterize human transcriptomes within and across individuals for a wide range of primary tissues and cell types, including colon tissue ${ }^{6}$. Thus, combing the datasets from TCGA as tumor resources and GTEx as normal sample resources expands opportunities for data mining and deeper understanding of gene signatures in cancer research ${ }^{7-9}$.

Clinical diagnosis or prognosis prediction of cancer patients based on the high-throughput gene expression data depends greatly on the accuracy of disease classification. This necessitates the development of best classification models for cancer samples with high accuracy and low risk of misclassification. Gene expression data, such as RNA-sequencing or microarrays, usually suffer from the dimensionality problem: too many gene features and relative few samples. It is usually impractical to go through all of the features during the gene expression analysis. As a result, feature selection tends to be a prominent approach for disease classification, especially in datasets with a large number of features. It can eliminate relatively unimportant variables and improve classification accuracy and performance ${ }^{10}$. Wu et al. ${ }^{11}$ selected 300 biomarkers from 13,990 features with the combination of seven algorithms, including logistic regression and feature selection methods. A hybrid feature selection algorithm also has been used for searching optimal tumor biomarkers with significant performance for distinguishing tumor and normal samples ${ }^{12}$. The wavelet kernel ridge and radial basis kernel ridge regression were proposed to select

[^0]
[^0]:    ${ }^{1}$ School of Electronics and Information, Northwestern Polytechnical University, 1 Dongxiang Road, Xi'an 710129, Shaanxi, China. ${ }^{2}$ Xi'an Key Laboratory of Stem Cell and Regenerative Medicine, Institute of Medical Research, Northwestern Polytechnical University, 127 West Youyi Road, Xi'an 710072, Shaanxi, China. ${ }^{3 \text { email: }}$ xggao@ nwpu.edu.cn; jihanwang@nwpu.edu.cn

![img-0.jpeg](img-0.jpeg)

Figure 1. Overview of the study design.

The most relevant features which can be used for classification of microarray medical datasets^{13}. Using a random forests model for feature selection, researchers identified a six-gene signature for predicting survival status in patients with head and neck squamous cell carcinoma (HNSCC) from the TCGA-HNSCC dataset^{14}. Another five-gene signature (including RGS11, RGS10, RGS13, RGS4, and RGS3) has been identified as independent prognostic factors for ovarian cancer patients by using Lasso cox analysis^{15}. In a study of melanoma, the feature selection approach was applied to discover and validate metastasis-related biomarkers based on single cell gene expression datasets^{16}.

The current study aimed to identify gene signatures that could be used to classify COAD samples and normal colon tissues. Specifically, we established a feature selection model, SNR-PPFS, by combining the signal-to-ratio (SNR) ranking algorithm^{17,18} with the predictive permutation feature selection (PPFS) algorithm, a Markov blanket (MB) based feature subset selection method. The PPFS algorithm considers features both individually and collectively in order to provide the best set of features. Bioinformatic and biological analysis were also carried out to investigate the potential biological significance of the candidate genes identified through feature selection approaches. We anticipate that our research will provide a novel methodological foundation for the identification of COAD biomarkers as well as other cancer types.

## Methods and materials

### Data acquisition

Figure 1 depicted an overview of the study design. The datasets for a combined cohort of TCGA, TARGET, and GTEx samples were obtained from the UCSC xena website^{19}. Firstly, the total RSEM expected_count (DESeq2 standardized) dataset was downloaded as the total gene expression profiling, which containing 19,039 bio-samples from both tumors and normal tissues (https://toil-xena-hub.s3.us-east-1.amazonaws.com/download/TCGA-GTEx-TARGET-gene-exp-counts.deseq2-normalized.log2.gz). We then chose samples of COAD tumor and normal colon tissue (selection criteria: for tumor tissue, primary_disease_or_tissue = “Colon Adenocarcinoma”; for normal tissue, primary_site = “Colon”) from the total gene expression dataset for the current study. Finally, 637 samples were recruited for research, including 289 COAD tumor samples (resourced from TCGA) and 348 normal samples. The 348 normal samples further contained 41 normal samples from the TCGA-COAD cohort and 307 normal colon tissues from GTEx. We also downloaded TCGA-COAD cohort's phenotype and survival data for bioinformatic and biological analysis (phenotype data: https://gdc-hub.s3.us-east-1.amazonaws.com/download/TCGA-COAD.GDC_phenotype.tsv.gz; survival data: https://gdc-hub.s3.us-east-1.amazonaws.com/download/TCGA-COAD.survival.tsv). The clinicopathological characteristics of the 289 COAD tumor samples were summarized in Table 1.

### Gene feature selection using SNR-PPFS algorithms

After obtaining the gene expression dataset of 637 samples, we subsequently performed feature selection to identify gene signatures as classifier between tumor


Table 1. Clinical characteristics of COAD cases (data from the TCGA database), as well as Cox regression analysis of the clinical parameters. BMI body mass index, OS overall survival, HR hazard ratio, CI confidence interval. Significant values are in bold. and normal groups. As shown in Fig. 1, the gene feature selection process consisted primarily of two steps, gene screening using the SNR algorithm and related gene selection using the PPFS method. All the steps were performed based on Python 3.8.

Screening genes using the SNR algorithm. SNR is an effective screening method that can quickly filter out genes that are unrelated to classification attributes. The expression is as follows. The numerator of the formula contains the average values of gene expression of the gene gi in the tumor and normal groups, and the denominator contains the standard deviations of the gene gi in the two groups. The higher the signal-to-noise ratio, the more important the gene is for classification.

$$ S N R\left(g_{i}\right)=\frac{\left|u_{+}\left(g_{i}\right)-u_{-}\left(g_{i}\right)\right|}{\delta_{+}\left(g_{i}\right)+\delta_{-}\left(g_{i}\right)} $$

Obtaining the Markov blanket genes using PPFS. The definition of Markov blanket. Markov blanket is a widely used feature selection approach, which can be described as the following definitions and Fig. 2. It has already contained all the information related to the target node, and the non-Markov blanket nodes can be discarded safely to achieve the purpose of feature selection.

![img-1.jpeg](img-1.jpeg)

**Figure 2.** The diagram of an example of Markov blanket in a casual network. The T node with yellow color in the red rectangle is a target node, the other nodes form a Markov blanket of T node, and T node is independent of any node outside the rectangle.

**Definition 1** (*Markov condition*) Any variable (node) in a Bayesian network is independent of its non-descendants given its parents.

**Definition 2** (*Faithfulness*) Let *G* denote a Bayesian network. Let *P* denote a joint probability. *G* and *P* are said to be faithful to one another if all the conditional independencies entailed by *G* and the Markov condition is present in *P*.

**Definition 3** (*Markov blanket*) Under the faithful condition, *MB (Y)* is the minimal set conditioned on which all other variables are independent of *Y*, i.e., (*X*|*MB(Y)* ⊥ *Y*|*MB(Y)*).

*Predictive permutation feature selection.* The *PPFS*<sup>20</sup> is a Markov blanket theory-based feature selection algorithm that selects a subset of features based on their performance both individually and as a group. It can automatically decide how many features to take and try to find the optimal combination of features, especially it performs well on high-dimensional data. In this case, we combined the SNR and PPFS to obtain the final gene signatures for classifying tumor and normal samples; the procedures were detailed in Algorithm 1.

```
Algorithm 1 The procedure of gene selection
Input: Feature Matrix \(\boldsymbol{X} ;\) Target Variable \(\boldsymbol{Y} ;\) Number of subsets \(\boldsymbol{K}\) for cross-validation; Sig-
    nificance threshold \(\epsilon\) and \(\boldsymbol{\alpha}\).
Output: The best MB
    initialize: \(\boldsymbol{X}^{\prime}=\varnothing\), all \(M B=\varnothing, Z=\varnothing\).
    for each feature \(x \in \boldsymbol{X}\) do
        \(S N R(x) \leftarrow\left|\mu_{+}(x)-\mu_{-}(x)\right| /\left(\delta_{+}(x)+\delta_{-}(x)\right)\)
        if \(S N R(x) \geq \epsilon\) then
            \(\boldsymbol{X}^{\prime} \leftarrow x\)
        end if
    end for
    new \(X\), new \(Y \leftarrow \operatorname{split}\left(\boldsymbol{X}^{\prime}, \boldsymbol{Y}, \boldsymbol{K}\right)\)
    for \(k \leftarrow 1\) to \(\boldsymbol{K}\) do
        \(X, Y \leftarrow\) new \(X[k]\), new \(Y[k]\)
        \(M B, P \_v a l u e s, j \leftarrow[]\), 0
        for \(i \leftarrow 1\) to \(d\) do
            \(p \leftarrow P P I\left(X_{i} \perp \boldsymbol{Y} \mid \varnothing\right)\)
            if \(p \leq \alpha\) then
                \(M B \leftarrow M B \cup X_{i}\)
                \(p \_v a l u e s[j] \leftarrow p\)
                \(j++\)
            end if
        end for
        \(M B \leftarrow \operatorname{sort}(M B, p \_v a l u e s)\)
        for \(i \leftarrow 1\) to \(m\) do
            if \(P P I\left(X_{i} \perp \boldsymbol{Y} \mid M B \backslash\left\{X_{i}\right\}\right) \geq \boldsymbol{\alpha}\) then
                \(M B \leftarrow M B \backslash\left\{X_{i}\right\}\)
            end if
        end for
        all \(M B[k] \leftarrow M B\)
    end for
    for each feature \(x \in\) all \(M B\) do
        for \(i \leftarrow 1\) to \(\boldsymbol{K}\) do
            if \(x \in M B_{i}(\boldsymbol{Y})\) then
                \(\operatorname{freq}(x) \leftarrow \operatorname{freq}(x)+1\)
            end if
        end for
        \(z_{i} \leftarrow \operatorname{freq}(x) /\left|M B_{i}(\boldsymbol{Y})\right|\)
        \(Z \leftarrow z_{i}\)
    end for
    index \(\leftarrow \arg \max (Z)\)
    return all \(M B[\operatorname{index}]\)
```

Bioinformatic and biological analysis. Bayesian network and gene functional annotation. Following the feature selection, we will identify candidate genes in tumors. We then used the Bayesian structure learning algorithm of PCStable ${ }^{23}$ to construct a gene regulatory network, based on the expression profiles of the candidate genes. Furthermore, the protein-protein interaction (PPI) network and functional annotation were carried out using the online platform STRING: functional protein association networks (https://www.string-db.org/).

PCA, PLS-DA and heatmap analysis. We conducted principal component analysis (PCA), partial least squares discriminant analysis (PLD-DA) and heatmap analysis to illustrate the performance of classification between tumor and normal groups. Specifically, the PCA, PLS-DA and heatmap analysis were carried out in R using the pca function in "FactoMineR" package, the plsda function in "mixOmics" package, and the pheatmap function in "pheatmap" package, respectively, based on the candidate gene expression profiling of 637 samples.

Differential expression and ROC analysis of candidate genes. The R package "limma" was used to compare the expression of candidate genes in tumor and normal samples. To evaluate the performance of candidate genes in

the diagnosis of COAD, the specificity, sensitivity, and area under the curve (AUC) values were obtained using receiver operator characteristic (ROC) analysis in MedCalc software.

### Correlation analysis of candidate genes with the clinicopathological characteristics of COAD patients

We used Pearson correlation in R to examine the relationship between gene expression and clinicopathological characteristics of COAD patients, particularly tumor stage status. For survival analysis, R packages “survival” and “survminer” were applied. Both univariate and multivariate Cox regression analysis were performed to estimate the simultaneous effects based on the clinical parameters and candidate gene expression signature in COAD patients, with P < 0.05 as the statistically significant level. Kaplan--Meier survival curves of candidate genes were also visualized.

## Results

### Feature selection identified a 38 gene signatures for classifying COAD tumor and normal samples

We found some genes with an expression value of “0” during the pre-processing, and we filtered out those genes with the expression of “0” in more than two-thirds of the 637 samples to reduce the noise. Following data pre-processing, we obtained expression profiling of over 50,000 gene symbols for each of the 637 samples. We then conducted feature selection to determine the most valuable gene features in classifying tumor and normal groups. The SNR approach identifies expression patterns with the greatest difference in average expression between two groups and the least variation in expression within each group; genes can be ranked according to their expression levels using the SNR test statistic. In this study, we first screened a total of 430 gene signatures by SNR method. Further, the 430 genes were matched by PPFS algorithm. Finally, the best set of gene features containing 38 genes was identified for classification.

### Expression profiling analysis of the candidate 38 genes

Previously, 38 genes were identified as classifiers between tumor and normal samples through feature selection approach. To investigate the expression patterns of these 38 genes in COAD tumors and normal samples, differential expression analysis was performed using Limma method. Table 2 displayed the fold change and statistical level of the candidate genes in tumor versus normal groups, as well as the specificity, sensitivity, and AUC values in ROC analysis. The majority (30 out of 38 genes) of the differentially expressed genes (DEGs) were up-regulated in tumors, as shown in Table 2 and the heatmap in Fig. 3. In particular, all these 38 genes demonstrated promising discrimination power in distinguishing tumors from normal samples (specificity range: 90.5--99.7, sensitivity range: 90.0--99.7, AUC range: 0.954--0.998).

The heatmap, PCA and PLS-DA model of samples based on the 38 gene signatures were performed to visualize the clustering performance. As expected, fully separated models between tumor and normal samples were observed when performing PCA and PLS-DA (Fig. 4). In the current study, the normal group was further subdivided into two subgroups according to the sample source databases: normal-TCGA and normal-GTEx. Thus, we also took into account the information of subgroups when performing the clustering analysis. As shown in Figs. 3 and 4, the two subgroups of normal samples overlapped to a small extent, and both sets of normal samples could be completely separated with tumor samples.

### Using Bayesian network constructing gene regulatory network

In this study, we proposed using Bayesian network to construct gene regulatory networks for the 38 candidate genes based on their expression profiles. The 38 DEGs interacted with each other to some extent (Fig. 5A). Specifically, in this connected network, the eight down-DEGs interacted with the up-DEGs in relatively separate ways. Furthermore, we discovered that the Bayesian network aids in the discovery of biological gene-regulatory interactions. For instance, we identified seven up-DEGs interacting with each other in the Bayesian network (as shown in circle in Fig. 5A). Further, a complete protein--protein interaction (PPI) network was obtained from the STRING online platform based on the seven up-DEGs (Fig. 5B). Functional annotation of the PPI network was primarily involved in biological process related to cell cycle and nuclear division, as well as gastric cancer disease (Fig. 5C). These findings indicated that in a Bayesian network, genes with similar expression patterns and functions are tend to be closer in the connections, which will help bridge the gap between an individual gene and a system biological interpretation in the high throughput bioinformatics research.

### Correlation analysis of candidate genes and clinicopathological characteristics of COAD patients

The TCGA database contains relatively comprehensive clinicopathological information on tumor samples. We then investigated whether the candidate genes were related to the clinicopathological characteristics of COAD patients. As summarized in Table 1, the tumor samples could be divided into different subgroups based on basic clinical information such as age, gender, race, and body mass index (BMI). According to the PLS-DA model (Fig. S1), the 38-gene expression signature could not well distinguish different subgroups of tumor samples based on the above basic clinical information. While, from the 38 gene signatures, we identified 14 candidate genes that were positively related to tumor stage status (P < 0.05 in Pearson correlation). Figure 6 illustrated the relative expression of the 14 stage-positive related genes in tumor samples of different stages, and Table S1 and Fig. S2 summarized the correlation scatter plots, coefficient values and statistical levels of the Pearson correlation. What's more, we found that the 14 DEGs were up-regulated in tumors compared to normal samples (Tables 1 and S1), implying that the stage related genes may help reflecting the tumor progression of COAD.

To investigate the prognostic factors for COAD, the Cox regression model for survival analysis was conducted. The risk score (HR > 1) was significantly positively correlated with tumor stage in both univariate and multivariate Cox regression analysis, indicating that it could be recognized as an independent risk factor for patients'


Table 2. Differential expression and ROC analysis of the 38 candidate DEGs. The differential analysis was performed by limma "package" in R. ROC analysis was carried out using MedCalc software. Genes with "*"showed the tumor stage-positive related genes ( $P<0.05$ ). Gene with "\#"showed the survival-related genes $(P<0.05)$. prognosis (Table 1 and Fig. S3). We also evaluated the effects of the 38 DEGs on survival outcomes. Overall, the expression pattern of 38 DEGs was not significantly correlated with the survival outcomes $(P>0.05)$ in univariate Cox regression analysis, as shown in Table S2. When we set the screening criteria to $0.05<P<0.1$ as having an influential trend, then TRIB3, STMN4 and FAM135B were found to have survival correlations in univariate Cox regression analysis. The risk score was significantly correlated with the differential expression of STMN4 (HR $>1$, $P<0.05$ ) and FAM135B (HR $<1, P<0.05$ ) in multivariate Cox regression analysis of the three candidate genes, as summarized in Table S2 and Fig. 7A. The Kaplan-Meier survival curves also revealed that high TRIB3 and STMN4 expression was associated with a lower overall survival probability, whereas high FAM135B expression was a better survival outcome (Fig. 7B-D). Taken together, our suggested that STMN4 and FAM135B dysregulation are independent prognostic factors for COAD patients.

![img-2.jpeg](img-2.jpeg)

Figure 3. Bi-clustering analysis of the 38 genes that were screened using feature selection. The analysis was carried out in R using the "pheatmap" package. All of the samples were mainly divided into two groups: tumor and normal, with the latter including normal_TCGA and normal_GTEx subgroups. The samples and genes were represented by the horizontal and vertical axis, respectively.

## Discussion

With the development of high-throughput techniques in biology and life sciences, more and more omics datasets are being generated, particularly in the field of cancer research. In recent years, the application of GTEx project has greatly improved the ability to study the genomics of normal tissues or cell lines^{22,23}, providing invaluable reference data for cancer studies of the corresponding tissues/organs. The feature selection approach helps to locate important and representative indicators from high-dimensional datasets, which is important for the advancement of precision medicine, such as cancer diagnosis and treatment. In our study, we utilized both SNR and PPFS methods before and after, and finally discovered a set of 38 genes with promising performance in distinguishing COAD tumors from normal colon tissues, based on the combining dataset from both the TCGA-COAD cohort and GTEx normal colon samples.

The Bayesian network (also known as causal network) is a directed acyclic graphical model developed in the late 1970's. The nodes represent the variables and the linkages represent informational or causal dependencies among the variables in a Bayesian network. Bayesian networks are widely used for modeling and inferring gene regulatory networks in biological applications, which provides an efficient way to study functional genomes. Here we constructed a Bayesian network based on the 38-gene expression profiles and classification labels (tumor or normal). The differential analysis revealed that the majority of the 38 DEGs were up-regulated, with only eight DEGs being down-regulated in COAD tumors compared to normal colon tissues. Interestingly, the gene nodes in the Bayesian network tended to be initially clustered according to the expression pattern. Based on this hypothesis, we may be able to predict the expression changes of novel genes since DEGs with similar expression patterns are tend to cluster together in a Bayesian network. It's also worth mentioning that Bayesian networks have been applied for inferring the structure of biological modules that reflect causal molecular mechanisms or statistical associations of the underlying system^{24}. In this study, for example, a biologically meaningful STRING

![img-3.jpeg](img-3.jpeg)

**Figure 4.** PCA and PLS-DA plot based on the expression pattern of the 38 genes. The analysis was performed using the "FactoMineR" package for PCA and the "mixOmics" package for PLS-DA in R. Each dot, triangle, and square represent a sample.

![img-4.jpeg](img-4.jpeg)

**Figure 5.** Bayesian network of the 38 candidate genes as well as the PPI network analysis. (**A**) Bayesian network of the 38 candidate genes. The red and green eclipses represent the up-regulated and down-regulated DEGs in COAD tumors, respectively. (**B**) PPI network of the seven up-DEGs [the seven genes in circle of (**A**) from STRING functional database. (**C**) Functional annotation of the genes in the PPI network.

![img-5.jpeg](img-5.jpeg)

**Figure 6.** Relative gene expression plot of the 14 stage-positive related DEGs. GraphPad Prism was used to create the scatter plot, and each dot represents a sample.

PPI network involving seven up-DEGs was identified in the 38-gene Bayesian network. The seven DEGs in the PPI-network were all up-regulated in COAD tumor samples and were mainly enriched in cell cycle and division-related functions. Cell cycle deregulation is well known to be one of the most frequent alterations during tumorigenesis and development^{25,26}. Thus, the findings above support the theory that using Bayesian networks not only provides useful information for disease classification, diagnosis and prediction, but also guides in inferring the structure of biological meaningful modules. However, Bayesian network model is not that perfect when imitating gene regulatory network. Gene regulatory networks are bipartite, since two genes can regulate each other in a network. In response to causality, the Bayesian network only forms a unidirectional mode rather than a bidirectional mode, which does not accurately reflect the actual gene regulation situation. What's more, when the number of features (for example, genes) is relatively large, it is difficult to construct a Bayesian network, which further supports the significance of gene feature selection when studying the high-throughput dataset.

ROC analysis of the 38 DEGs showed ideal diagnostic accuracy, specificity, and sensitivity for COAD tumor samples, supporting our hypothesis that feature selection aids in obtaining effective gene features in cancer research. More importantly, parts of the candidate genes were found to be significantly correlated with tumor stage and survival outcomes in COAD patients. Studies have shown that TOP2A played important roles in the tumorigenesis of many types of cancer, including colon cancer, and knockdown of TOP2A suppressed the proliferation and invasion of colon cancer cells^{27}. Previously, DNA microarray and two-color FISH detection revealed that the ubiquitin-conjugating enzyme E2C gene (UBE2C) was significantly overexpressed in both primary tumors and liver metastases of colon cancer^{28}. TOP2A and UBE2C were also found to be up-regulated in COAD tumors when compared to normal tissues in this study. Meanwhile, the two genes were found to be positively correlated with tumor stage and to be functionally enriched in the gastric cancer network, implying that they may function as oncogenes in gastrointestinal tumors. Similarly, other stage-related up-DEGs discovered in our study have also been reported in colon cancer researches. A recent bioinformatic analysis, for example, revealed that key genes such as GRIND, KRT80, and SPTBN2 have high diagnosis values in CRC patients^{29}. Furthermore, high levels of KRT80 mRNA were also observed in CRC cell lines^{30}. INHBA promoted the proliferation, migration, and invasion of colon cancer cells^{31}, and has been shown to be a prognostic predictor for COAD patients^{32}. SALL4 mRNA has been identified as a marker for the diagnosis of several cancers^{33,34}. The anti-cancer effects of chrysin on tumor cells in colon cancer included induction of apoptosis and attenuation of the SALL4 expression^{35}. It has also been proposed that SERPINB5 in CRC is associated with tumor location, poor histological differentiation, microsatellite instability, and poor prognosis^{36}. TMEM206 was demonstrated to promote CRC malignancy by interacting with AKT and extracellular signal-regulated kinase signaling pathways^{37}. A study showed that TOMM34 expression was elevated in the majority of human colon cancer samples, and the siRNA-TOMM34 approach effectively suppressed gene expression and significantly inhibited cell growth in colon cancer HCT116 cells^{38}. Researchers identified several candidate cancer driver genes, including TOMM34, in both mRNA and protein levels in a proteogenomic study of human CRC samples^{39}. NOTUM, one of the Wnt target genes, was found to be up-regulated in clinical specimens of colon cancer^{40}. Similarly, immunohistochemistry detection confirmed WDR43 overexpression in CRC patient specimens^{41}. What's more, several studies have reported the oncogenic role of TRIB3 in CRC^{42}. In intestine cells, TRIB3 interacts with β-catenin and TCF4 to increase the expression of genes associated with cancer stem cells and promote CRC tumorigenesis^{43}. Approaches

![img-6.jpeg](img-6.jpeg)

**Figure 7.** Multivariate Cox regression and Kaplan–Meier survival curves of three candidate DEGs. The analysis was carried out in R using the "survival" and "survminer" packages. (**A**) Multivariate Cox regression forest plot of the three candidate genes. HR: hazard ratio; CI: confidence interval. (**B**–**D**) Kaplan–Meier survival curves for TRIB3, STMN4, and FAM135B, respectively. The cut-off points divided gene expression values into high (high) and low (low) groups.

To inhibit TRIB3 activity, we developed a model for cancer therapy. In this research, we discovered a positive relationship between TRIB3 expression and tumor stage, and high levels of TRIB3 indicating a poorer survival. Furthermore, we discovered that the gene FAM135B, which had not previously been described in colon cancer, was down-regulated and served as a prognostic factor for COAD. Overexpression of FAM135B has been reported in esophageal squamous cell cancer (ESCC)^{44}. The FAM135B/AKT/mTOR feedforward loop promoted ESCC progression, and silencing FAM135B improved the radiosensitivity of esophageal carcinoma cell. This phenomenon contradicts our findings that FAM135B was significantly down-expressed in COAD samples, which needs to be confirmed further. Despite this, we may conclude that feature selection can greatly help to identify key candidate genes in cancer research. The majority of the candidate genes have previously been reported, with the same alteration trend as our findings. While another relatively novel gene feature can be obtained for specific cancer types, this will broaden the field of biomarker discovery service for tumor diagnosis and treatment, both technically and theoretically.

### Conclusions

In summary, we identified a 38 gene signature with ideal performance when classifying COAD tumor from normal samples by using feature selection methods in this study. The majority of the 38 DEGs were significantly up-regulated in tumor samples compared to normal samples. In the Bayesian network, we found that genes with

similar expression patterns or functions interacted more closely. Moreover, some of the candidate genes, such as TRIB3, KRT80, and FAM135B, were found to be correlated with tumor stage or survival outcomes, implying that these candidate genes could serve as promising prognostic biomarkers for COAD patients. Taken together, our study highlights the necessity and importance of feature selection approaches in cancer research, especially for high-dimensional datasets, which will significantly advance the development of precision medicine.

## Data availability

The raw data of this study have been deposited in FigShare (https://figshare.com/) with the link: https://doi.org/10.6084/m9.figshare.19093307.

Received: 17 January 2022; Accepted: 3 May 2022
Published online: 24 May 2022

## Acknowledgements

This work was supported by the National Natural Science Foundation of China (No. 61573285).

## Author contributions

Y.W wrote the main manuscript text. X.R. and P.S. prepared datasets and constructed models. X.G. and J.W revised paper. All authors reviewed the manuscript.

## Competing interests

The authors declare no competing interests.

## Additional information

Supplementary Information The online version contains supplementary material available at https://doi.org/ 10.1038/s41598-022-12780-7.

Correspondence and requests for materials should be addressed to X.G. or J.W.
Reprints and permissions information is available at www.nature.com/reprints.
Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.
(c) The Author(s) 2022