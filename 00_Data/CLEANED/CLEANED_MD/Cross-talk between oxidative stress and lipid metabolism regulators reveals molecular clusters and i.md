# Cross-talk between oxidative stress and lipid metabolism regulators reveals molecular clusters and immunological characterization in polycystic ovarian syndrome 

Cuiyu Tan ${ }^{1 \dagger}$, Shuqiang Huang ${ }^{1 \dagger}$, Liying Xu ${ }^{1}$, Tongtong Zhang ${ }^{1}$, Xiaojun Yuan ${ }^{1}$, Zhihong Li ${ }^{1}$, Miaoqi Chen ${ }^{1}$, Cairong Chen ${ }^{1,2 *}$ and Qiuxia Yan ${ }^{1,2 *}$


#### Abstract

Background Changes in the oxidative stress and lipid metabolism (OSLM) pathways play important roles in polycystic ovarian syndrome (PCOS) pathogenesis and development. Consequently, a systematic analysis of genes related to OSLM was conducted to identify molecular clusters and explore new biomarkers that are helpful for the diagnostic of PCOS.


Methods Gene expression and clinical data from 22 PCOS women and 14 normal women were obtained from the GEO database (GSE34526, GSE95728, and GSE106724). Consensus clustering identified OSLM-related molecular clusters, and WGCNA revealed co-expression patterns. The immune microenvironment was quantitatively assessed utilizing the CIBERSORT algorithm. Multiple machine learning models and connectivity map analyses were subsequently applied to explore potential biomarkers for PCOS, and nomograms were employed to develop a predictive multigene model of PCOS. Finally, the OSLM status of PCOS and the hub genes expression profiles were preliminarily verified using TUNEL, qRT-PCR, western blot, and IHC assays in a PCOS mouse model.
Results 19 differential expression genes (DEGs) related to OSLM were identified. Based on 19 DEGs that were strongly influenced by OSLM, PCOS patients were stratified into two distinct clusters, designated Cluster 1 and Cluster 2. Distinct differences in the immune cell proportions existed in normal and two PCOS clusters. The random forest showed the best results, with the least cross-entropy and the utmost AUC (cross-entropy: 0.111 AUC: 0.960). Among the 19 OSLM-related genes, CXCR1, ACP5, CEACAM3, S1PR4, and TCF7 were identified by a Bayesian network and had a good fit with PCOS disease risk by the nomogram (AUC: 0.990 CI: 0.968-1.000). TUNEL assays revealed more severe DNA damage within the ovarian granule cells of PCOS mice than in those of normal mice ( $P<0.001$ ). The RNA and protein expression levels of the five hub genes were significantly elevated in PCOS mice, which was consistent with the results of the bioinformatics analyses.

[^0]
[^0]:    ${ }^{\dagger}$ Cuiyu Tan and Shuqiang Huang contributed equally to this study as co-first authors.
    *Correspondence:

    Cairong Chen
    cairong1222@163.com
    Qiuxia Yan
    yanqiuxia1982@163.com
    Full list of author information is available at the end of the article

## Conclusion

A novel predictive model was constructed for PCOS patients and five hub genes were identified as potential biomarkers to offer novel insights into clinical diagnostic strategies for PCOS.

## Keywords

Polycystic ovarian syndrome, Oxidative stress, Lipid metabolism, Machine learning, PCOS mouse model

## Introduction

Polycystic ovarian syndrome (PCOS) is a prevailing endocrine disease that seriously affect females' reproductive health [1, 2]. PCOS patients typically experience irregular menstruation, ovulatory disorders, hyperandrogenism, and obesity. The Rotterdam criteria are broadly recognized as the predominant diagnostic standards for identifying PCOS [3] and include the following three characteristics: dilute or anovulatory ovulation, hyperandrogenic clinical manifestations or hyperandrogenaemia, and polycystic changes in the ovaries. PCOS can be diagnosed when the above two criteria are met.

Oxidative stress occurs when there is an overproduction of oxidants under limited antioxidant defences. A notable association has been observed between oxidative stress and PCOS-related obesity, with several studies indicating that elevated levels of reactive substances or oxidation products are increased in obese individuals [4]. Oxidative stress further exacerbates PCOS-related obesity by reducing insulin sensitivity, blocking glucose uptake [5, 6], and inducing the growth and differentiation of fat cells. Furthermore, oxidative stress promotes ovarian dysfunction by promoting apoptosis and long-term chronic inflammation [7].

PCOS patients frequently exhibit aberrant abnormal lipid metabolism [8--10]. Excessive low-density lipoprotein (LDL) and insufficient high-density lipoprotein (HDL) lead to mitochondrial dysfunction, which increases the release of ROS, disrupts the ovarian microenvironment and contributes to infertility [11, 12].

In conclusion, the pathogenesis of PCOS is believed to be associated with oxidative stress and lipid metabolism (OSLM). OSLM typically interact with each other in PCOS, thereby impairing the ovarian granulosa cells' physiological state and altering the ovarian microenvironment. However, no existing studies have investigated the pathogenesis of PCOS from this perspective. In this study, multiple bioinformatics methods were combined to search for pivotal genes from the perspective of OSLM and a novel predictive model was construct using these genes, which could function as a cornerstone for the clinical identification of PCOS.

## Materials and methods

## Acquisition and processing of datasets

The expression profiles of three microarray datasets for PCOS (GSE34526, GSE95728, and GSE106724) were acquired from the Gene Expression Omnibus (GEO) databaset. 22 PCOS and 14 normal samples of human granulosa cells were included (Supplementary Table 1). By utilizing the Sva package [13], three sets of expression profile data were incorporated and debatched. From MSigDB [14] and GeneCards websites [15], 1399 oxidative stress-related genes and 1996 lipid metabolism-related genes were respectively extracted (Supplementary Table 2). In addition, using the R package “limma” [16], the differential expression genes (DEGs) related to OSLM were identified in view of a |log2-fold change|> 1 and a P value < 0.05.

## Analysis of immune microenvironment

The expression patterns of 22 distinct immune cell types were estimated by the CIBERSORT algorithm [17]. Samples with P values > 0.05 and cells with all infiltration scores = 0 were filtered out. The associations between DEGs related to OSLM and these immune cells were evaluated via Spearman correlation analysis.

## Identification of molecular clusters

Based on the DEGs of OSLM, subgroups of PCOS patients were identified via the “ConsensusClusterPlus” package [18]. Furthermore, the “Rtsne” package was utilized to graphically represent the effect of unsupervised clustering.

## Weighted gene co-expression network analysis (WGCNA) for the selection of target genes

The construction of a co-expression network was performed based on the “WGCNA” package [19]. First, the top 5000 genes exhibiting the greatest variance were subjected to subsequent WGCNA analysis. Then, by estimating the "soft" threshold power, a scale-free network of biological significance was constructed. Finally, gene significance and modular significance metrics of gene modules were calculated to evaluate the associations between the identified modules and clinical features.

## Screening of important genes by machine learning algorithms

Four representative machine learning models were established via the R package “mlr3”, including the

Random Forest (RF), Support Vector Machine (SVM), Decision Tree, and k-nearest neighbour (KNN) models. These models were validated by twofold cross-validation. To visualize the area under the curves of different models and the importance of the genes in the best model, the R package “ggplot2” was utilized.

## Protein--protein interaction (PPI) network construction

To visualize the known PPI networks, the STRING database was utilized. In addition, the “CBNplot” package [20] was used to predict the potential correlations between DEGs. An interaction strength > 0.5 was set as the screening criterion. The five hub genes of this network were selected for subsequent analysis.

## Drug prediction and molecular docking

On the basis of the DSigDB website [21], the five hub genes were used to perform drug prediction. The topranked drugs were selected based on adjusted P values for molecular docking, executed utilizing AutoDock Vina 1.2.0 software.

## Nomogram model construction

The R package “rms” was instrumental in developing a nomogram model of the five hub genes. A calibration plot was deployed to compare the actual standard values with the predicted outcomes. In addition, an approach of decision curve analysis (DCA) was adopted to estimate the clinical applicability of model-derived decisions, with a focus on the potential gains for patients.

## Establishment of a PCOS mouse model

Thirty 21-day-old clean-grade C57BL/6 female mice were obtained from Guangdong Provincial Medical Laboratory Animal Centre. The animal experiments were approved by the ethics committee of Qingyuan People's Hospital (LAEC-2023-030).

The mice were assigned randomly to the normal or PCOS groups. Dehydroepiandrosterone (DHEA, D106380, Aladdin, Shanghai, China) was dissolved in sesame oil (S905724, Maclean, Shanghai, China). The PCOS group mice were injected subcutaneously in the neck and back with 6 mg/100 g DHEA combined with a 60 kcal% high-fat diet for 21 days, whereas the normal group mice were daily injected with equivalent sesame oil, in conjunction with a normal diet [22].

## Body weight measurement

Body weight measurements of the mice in all groups were conducted every three days from the first day of grouping. By recording the fluctuations in body weight across all groups and drawing weight change curves, the differences in body weight change trends between the two groups were compared.

## Detection of serum testosterone

With the aim of isolating the serum (the supernatant), the orbital venous blood was applied to perform a centrifugation process at 3000 rpm for 10 min. Mouse serum testosterone was quantified using a mouse ELISA kit (E-OSEL-M0003, Elabscience, Wuhan, China).

## Observation of the estrous cycle in mice

From the 15th day after grouping, vaginal cell smears were obtained to observe the changes in vaginal cells and determine the estrous cycles of the mice. The mouse vagina was rinsed with 5 µl of phosphate-buffered saline (PBS) and a 200 µl pipette tip. The rinse solution was dropped onto glass slides, which were then stained with Giemsa stain (G1007, Servicebio, Wuhan, China).

## Histology of ovaries

The collected ovaries were placed in neutral formalin and fixed for 24 h. After rinsing three times under running water, a series of treatments were performed to produce tissue slices of approximately 5 µm, including ethanol dehydration, xylene clearing, wax dipping, embedding, and sectioning. Then, haematoxylin and eosin (G1076, Servicebio, Wuhan, China) were used to stain tissue sections. The sections were applied to evaluate the effect of PCOS-like alterations in the ovaries by quantifying the number and size of the cystically dilated follicles, assessing the frequency of atretic follicles, and observing the cellular arrangement.

## TUNEL assay

TUNEL assays were employed to detect apoptotic events in ovarian granulosa cells. The paraffin sections were subjected to a series of steps: dewaxing, hydration, incubation in TUNEL reaction solution, incubation in a DAPI dye box, sealing, and photo scanning. TUNEL working solution was purchased from Servicebio (G1504-50 T, Servicebio, Wuhan, China).

## Ovarian granulosa cell isolation and culture

Preovulatory follicles were carefully punctured from the ovaries under a stereomicroscope, and the follicle contents were released, after which the ovarian granulosa cells were meticulously separated utilizing a 200-mesh cell sieve. After the cells were confluent, RNA or protein extraction was performed.

## Quantitative real-time PCR (qRT--PCR)

The ovarian granulosa cells in each group were collected, and TRIzol was subsequently added to lyse the cells. The

RNA precipitate was successfully obtained by separating the chloroform phase, precipitating with isopropanol, washing with ethanol, and allowing it to air dry. The RNA precipitate was resuspended by adding DEPC water, shaken well and centrifuged, and the RNA purity was assessed. Total RNA was transformed into first-strand cDNA via an RT‒PCR kit (HY-K0511A, MedChemExpress, New Jersey, America). cDNA was amplified in the CFX-Connect System using SYBR (HY-K0501, MedChemExpress, New Jersey, America). The specific primers employed in the present investigation are detailed in Supplementary Table 3.

## Western blot

The expression of CXCR1, S1PR4, CEACAM3, TCF7, and ACP5 was detected using western blot. The specific operation followed the previously described steps [23]. Comprehensive details regarding the antibodies utilized are shown in Supplementary Table 4.

## Immunohistochemistry (IHC)

According to the previously described steps [24], IHC was performed on the sections. The antibodies utilized are shown in Supplementary Table 4.

## Statistical analysis

The data are presented as the mean ± SEM and were statistically analysed via GraphPad Prism 9. An independent t-test was utilized to estimate the statistical significance of the disparities.

## Results

## Collection and integration of transcription datasets from PCOS ovarian granulosa cells

The flow chart which identified the key targets of OSLM in PCOS was shown in Fig. 1. Three datasets of PCOS patients (GSE34526, GES95728, and GES106724) were obtained for further analysis. The GEO platform served as the basis for all three microarray datasets (Supplementary Fig. 1A). The three datasets were consolidated and processed through batch correction methodologies to mitigate batch-related discrepancies (Supplementary Fig. 1B). To facilitate observation, standardized data were visualized as plots via principal component analysis (PCA) (Supplementary Fig. 1C-D).

## Relationship between DEGs and OSLM

Through differential expression analysis, a cohort of 315 genes was discerned, with 288 significantly upregulated genes and 27 significantly downregulated genes (Fig. 2A). The 315 DEGs were intersected with 1399 oxidative stress-related genes and 1996 lipid metabolism-related genes obtained from the MSigDB and GeneCards databases (Fig. 2B), and a total of 19 intersecting genes were obtained and used in subsequent analyses. Notably, compared to the normal group, 19 intersecting genes were significantly upregulated in the PCOS group (Fig. 2C-D).

## Changes in immune-infiltrating cells

The utilization of the CIBERSORT algorithm facilitated the generation of a rainbow plot, which effectively depicts the proportional distribution of 19 distinct immune cell types (three immune cells with no proportion were filtered) in each sample, and it was found that activated mast cells accounted for a larger proportion in the PCOS samples than in the normal samples (Fig. 3A). Compared with those in the normal group, B cells naïve and resting memory CD4 T cell were significantly reduced, whereas the numbers of neutrophils and activated mast cells were notably greater in the PCOS group (Fig. 3B). The correlation heatmap revealed a direct association between mast cells activated and eosinophils among the infiltrating immune cells in PCOS patients. Gamma delta T cells showed a positive correlation with neutrophils, as were plasma cells and CD4 naive T cells (Fig. 3C). The correlation heatmap for 19 DEGs and 19 immune cells further highlighted a notable negative relationship between NOD2 and B cells naïve, alongside a marked positive relationship between IL1B and activated mast cells. (Fig. 3D). Thus, abnormal infiltration of these immune cells might have an important impact on the progression of PCOS.

## Co-expression network of the normal and PCOS groups

To study the gene association patterns among PCOS patients, all of the samples from the abovementioned datasets (GSE34526, GSE95728, and GSE106724) were subjected to WGCNA. The sample clustering tree was shown in Supplementary Fig. 2A. The scale-free network was established by employing the soft-threshold power of 5 (R^{2}>0.8) (Supplementary Fig. 2B). There were 12 gene modules identified by hierarchical clustering (Supplementary Fig. 2C-D), and the module of turquoise had the strongest relevance with both the normal and PCOS groups (correlation value = 0.74).

## Identification of molecular clusters in PCOS.

On the basis of the 19 genes mentioned above, a consensus clustering algorithm was used to further categorize the PCOS patient samples. Through converging similar modules, k = 2 was determined to be the most stable grouping method, and the result of the sample square matrix heatmap was ideal (Supplementary Fig. 3A). After dimensionality reduction analysis, some significantly different relationships were revealed by the distributions

![img-0.jpeg](img-0.jpeg)

**Fig. 1** Flowchart of the study

of Cluster 1 and Cluster 2 (Supplementary Fig. 3B). In Cluster 1, the transcriptional levels of the 19 overlapping genes generally manifested as low, whereas they exhibited marked upregulation in Cluster 2, suggestive of a more distinct variation in OSLM being evident within the latter cluster. (Supplementary Fig. 3C-D).

### Different immune microenvironments of the two clusters in PCOS

A previous research has revealed high immune-inflammatory levels in PCOS patients [25]. Thus, CIBERSORT was employed to further estimate the level of immune cellular infiltrates in PCOS patients (Fig. 4A). Notably, naive B cells and Macrophages M2 have obviously increased in Cluster 1, whereas gamma delta T cells and eosinophils significantly increased in Cluster 2 (Fig. 4B). Compared with that of Cluster 1, the immune score of Cluster 2 was more centralized and higher (Fig. 4C). In general, it suggested that Cluster 2 had higher levels of immune infiltration, and the condition of the PCOS patients might have been more severe.

### Construction of gene modules between the two clusters of PCOS patients

Aim to study the gene association pattern between Cluster 1 and Cluster 2, all of the PCOS samples from the

![img-1.jpeg](img-1.jpeg)

![img-2.jpeg](img-2.jpeg)

**Fig. 2** Identification of OSLM-related genes. **A** Volcano plot of three expression datasets of PCOS patients. **B** Venn figure showing the commonalities among DEGs and oxidative stress-related and lipid metabolism-related genes. **C** Boxplots of the varying expression of the 19 genes between the two groups. **D** Heatmap of the 19 overlapping genes correlated with OSLM in the two groups

abovementioned datasets (GSE34526, GSE95728, and GSE106724) were clustered, and the sample clustering tree was shown in Supplementary Fig. 4A. A scale-free network was established to perform WGCNA by employing a soft-threshold power of 5 (R^{2}>0.8) (Supplementary Fig. 4B). There were 18 gene modules identified by hierarchical clustering (Supplementary Fig. 4C-D). Among these correlation analyses, the salmon module had the strongest correlation (correlation value=0.77) with the two clusters. The salmon module was used for subsequent analysis.

### Construction and exploration of machine learning algorithms to screen genes

Some machine learning algorithms have been used to search for PCOS biomarkers. Seventy-six overlapping DEGs were detected from the intersection between the DEGs of the normal and PCOS groups and the DEGs of the two clusters (DEGs were obtained from WGCNA) (Fig. 5A). Four distinct machine learning techniques (RF, SVM, Decision Tree, and KNN) were employed for the identification of the hub genes. RF had the best adaptation (with the least cross-entropy and utmost AUC value) in twofold cross-validation (Fig. 5B-C). Therefore, RF was eventually used to screen the genes, and 23 important genes with MeanDecreaseGini>0.25 were identified (Fig. 5D). These results suggest the potential correlation between identified genes and the pathogenesis of PCOS.

### Identification of the hub genes

Comprising of 23 nodes and 13 edges, a PPI network was meticulously assembled using the String database

![img-3.jpeg](img-3.jpeg)

Fig. 3 The landscape of the immune microenvironment. A Prediction of the percentage of immune cell composition within the PCOS groups. B Box plots of the variations in the expression levels of 19 immune cell types in the normal group and PCOS group. C Heatmap of correlations between 19 immune cell subsets. D Heatmap of correlations

(Fig. 6A). More potential contacts among these proteins are still unrecognized. To explore more potential interactions among the genes encoding these proteins, a Bayesian network was constructed. A visualization of the Bayesian network model was shown in Fig. 6B. The genes encoding TCF7, CXCR1, and S1PR4 had more potential connections with other genes, and it was estimated that ACP5 and CEACAM3 also significantly influenced the co-expression network. In particular, all of the top five hub genes identified by the Bayesian algorithm were significantly differentially expressed between the normal group and the two clusters of PCOS patients (Fig. 6C). In general, these genes might play important roles in PCOS.

### Drug prediction and molecular docking

The known or potential drug molecules of the five hub genes were searched from the DsigDB database and sorted by *P* value. The top-ranked drug molecules, including thalidomide, dexbrompheniramine, ibuprofen, AH23848, and 3-acetyl-7-hydroxy-2H-chromen-2-one, were chosen for molecular docking with the corresponding proteins via AutoDock software. The outcomes of the molecular docking by visualization as shown in Supplementary Fig. 5A-E.

![img-4.jpeg](img-4.jpeg)

**Fig. 4** The immune microenvironment across the two distinct PCOS clusters. **A** Prediction of the percentage of immune cell composition. **B** Boxplots of the varying expression of 19 immune cell types between the two clusters. **C** The estimated immune score between the two clusters

ACP5-Thalidomide (binding energy = -6.13), CEACAM3-Dexbrompheniramine (binding energy = -5.21) and CXCR1-Ibuprofen (binding energy = -6.27) had excellent binding activity, and the binding effects of TCF7-AH23848 (binding energy = -4.06) and S1PR4-3-acetyl-7-hydroxy-2H-chromen-2-one (binding energy = -4.91) were slightly inferior. The results of the above molecular docking studies provide the basis for targeted therapy for PCOS.

### Nomogram for disease assessment

Integrating the contributions of multiple influences to the outcome variable facilitates the construction of nomograms with greater scientific predictive power. A nomogram of the five hub DEGs was constructed to assess the severity of PCOS (Fig. 7A). Overall, the bias-corrected curve coincided with the ideal curve (Fig. 7B). Compared with a single gene, the nomogram model that combined the five hub genes showed the best predictive value (Fig. 7C). The ROC curve of the nomogram model displayed the most excellent diagnostic value (AUC: 0.990 CI: 0.968–1.990 CI: 0.968–1.000), whereas ACP5 (AUC: 0.916 CI: 0.821–1.000), TCF7 (AUC: 0.938 CI: 0.862–1.000), CEACAM3 (AUC: 0.968 CI: 0.918–1.000), S1PR4 (AUC: 0.955 CI: 0.894–1.000), and CXCR1 (AUC: 0.977 CI: 0.941–1.000) displayed slightly lower diagnostic performances (Fig. 7D-E). Thus, the construction of a nomogram model might be helpful for the diagnosis of PCOS.

### Animal model construction and evaluation

Based on a high-fat diet, the mouse model of PCOS was created using DHEA. The body weights of the PCOS mice increased significantly on the fourth day compared to the normal group (Fig. 8A). The testosterone in PCOS group mice were markedly elevated, similar to those in PCOS patients with hyperandrogenaemia (Fig. 8B). Vaginal smears were used to evaluate alterations in the estrous cycle. It exhibited a regular

![img-5.jpeg](img-5.jpeg)

**Fig. 5** Identification of the best machine learning model. **A** Venn diagram of the two WGCNA. **B** Cross-entropy values of the four machine learning algorithms. **C** Interplay between the sensitivity and specificity metrics for the four machine learning algorithms. **D** Key genes were obtained via the RF model

four-day estrous cycle, including pre-estrus, estrus, metestrus, and diestrus of the normal mice. The PCOS mice were in estrus for a prolonged period, suggesting that they had disorders of the estrous cycle and ovulation disorders (Fig. 8C-D). In the normal group of mice, the follicles in each period had a regular morphology. In contrast, in the group of mice with PCOS, a noticeable decrease of follicles present during various stages, and large, severely swollen cystic follicles with fewer layers of granulosa cells were observed, which could be caused by inflammation (Fig. 8E-F). These results demonstrated that a PCOS mouse model was successfully established.

### Detection of ovarian granulosa cell apoptosis via the TUNEL assay

The TUNEL assay can reflect DNA damage in cells, and three fields of view under 100× magnification were utilized to determine the proportion of TUNEL (+) cells

![img-6.jpeg](img-6.jpeg)

**Fig. 6** Identification of the hub genes. **A** The PPI network of the RF analysis results. **B** Bayesian network of the RF analysis result. **C** Distinct expression patterns of the five hub genes in the normal group and the two PCOS clusters

for statistical analysis, which helps us to evaluate the extent of apoptosis in ovarian granulosa cells in mice. The PCOS group presented a notably higher percentage of TUNEL-positive (red) granulosa cells when compared with the normal group (*P* < 0.001), indicating that OSLM in PCOS cells might be more intense (Fig. 9).

### Experimental validation of the five hub genes

Compared with the normal group, qRT‒PCR and western blot analyses indicated that expression of the five hub genes in the PCOS group (ACP5, TCF7, CEACAM3, S1PR4, and CXCR1) was substantially elevated (Fig. 10A‒B). IHC results were similar to qRT‒PCR and western blot. Notably, ACP5 and S1PR4 were predominantly located in the cytoplasm of ovarian granulosa cells. TCF7 was primarily found in the nuclei of granulosa cells. The subcellular localization of CECAM3 and CXCR1 within ovarian granulosa cells encompassed both the cytoplasmic and nuclear compartments (Fig. 10C‒M). The expression of the five hub genes showed same conditions as the transcriptome chip data did, suggesting that they might possess diagnostic potential for PCOS. However, more experimental results are needed to verify the five hub genes as biomarkers for the diagnosis of PCOS.

### Discussion

The rapid development of clinical predictive models offers the possibility of early diagnosis of PCOS, prediction of patient outcomes, and prediction of the probability of complications [26]. In this study, a multigene predictive model was developed for the prediction of PCOS from the perspective of OSLM, which might help promote the development of precision treatment for PCOS.

![img-7.jpeg](img-7.jpeg)

**Fig. 7** Nomogram for disease assessment. **A** Nomogram of five key DEGs. **B** Curves of bias-corrected and ideal results. **C** Decision curve of five key DEGs. **D** ROC curves of the nomogram. **E** ROC curve analysis of ACP5, TCF7, CEACAM3, S1PR4 and CXCR1. (AUC represents the area under the curve)

![img-8.jpeg](img-8.jpeg)

**Fig. 8** PCOS model construction and evaluation. **A** Trends of body weight gain in normal and PCOS mice. **B** Serum testosterone levels in normal and PCOS mice. **C** Trends of estrous cycle changes in normal mice. **D** Changes in the estrous cycle in PCOS mice. 1 implies pre-estrus, 2 implies estrus, 3 implies metestrus and 4 implies diestrus. **E** HE staining of the ovaries of normal mice with follicles at different time points. **F** HE staining of the ovaries of PCOS mice with swollen cystic follicles

![img-9.jpeg](img-9.jpeg)

**Fig. 9** Increased apoptosis of ovarian granulosa cells in PCOS mice. **A** Observation of apoptosis in ovarian granulosa cells of normal mice. **B** Observation of apoptosis in ovarian granulosa cells of PCOS mice. **C** Comparative analysis of the percentage of TUNEL (+) cells among the granulosa cells in the follicles between the normal and PCOS groups. Blue indicates the nucleus (DAPI), and red indicates TUNEL (+) cells

Aberrations in OSLM can exacerbate the evolution and progression of PCOS. Studies have shown that reactive oxygen species and reactive nitrogen species levels are significantly elevated in ovaries, serum, and urine of PCOS patients [27]. Additionally, those with PCOS also present severe conditions such as hyperlipidaemia, increased levels of LDL cholesterol, and a decrease in HDL cholesterol levels [28]. A deteriorated antioxidant system coupled with irregular lipid metabolism can disrupt the ovarian microenvironment and induce a chronic inflammatory response, which further leads to poor oocyte quality and ovarian dysfunction and affects endometrial tolerance in individuals with PCOS [29–31].

Oxidative stress and apoptosis form a vicious cycle: oxidative stress can induce ovarian cell apoptosis through external and internal pathways, and endoplasmic reticulum stress, leading to a direct reduction in the number of germ cells [7, 32]. Oxidative stress activates the proinflammatory transcription factor κB through lipid peroxidation, protein oxidation, and DNA damage, promotes the inflammatory cascade [30, 33], causes long-term chronic inflammation, and directly stimulates ovarian androgen overdose [34]. Throughout the TUNEL assay, a significantly higher percentage of TUNEL (+) granulosa cells was observed in the PCOS group, suggesting OSLM might be more pronounced in PCOS patients versus those without the condition.

The activation and degranulation of mast cells play crucial roles during the progression of chronic inflammation in adipose tissue [35]. These processes are notably increased in PCOS patients, potentially exacerbating chronic ovarian inflammation. Neutrophilism is linked to persistent ovarian infiltration and elevates the risk of cardiovascular disorders in PCOS patients [36, 37]. Research has shown that in PCOS patients, CD4+ T-cell activation is suppressed, a condition that is significantly linked to the occurrence of anovulation and follicular cysts [38]. However, the question of whether naive B-cell levels are suppressed in PCOS patients remains a contentious issue [23]. In this study, a comparison between the PCOS and normal groups revealed a substantial elevation in mast cells and neutrophils within the PCOS group, whereas the numbers of CD4+ T cells and naïve B cells experienced a noticeable reduction. Clarifying these immunophenotypic properties might pave the way for new directions in the immunotherapy of PCOS [39].

Different immune microenvironments in PCOS patients have different clinical and prognostic characteristics [40]. On the basis of 19 OSLM-related genes, two distinct clusters were delineated, with Cluster 1 representing the low-expression cohort and Cluster 2 denoting the high-expression cohort, which have distinct characteristics in terms of immune infiltration. Cluster 1 demonstrated a significant increase in naive B cells and M2 macrophages, whereas gamma delta T cells and eosinophils were notably increased in Cluster 2. B cells promote chronic inflammatory processes by producing higher levels of TNF-α [41, 42]. M2-phenotype macrophages can aggravate chronic ovarian inflammation and insulin resistance (IR) by releasing several proinflammatory cytokines [43]. Gamma-delta T cells typically reside in adipose tissue and are a significant source of the proinflammatory cytokine interleukin (IL)-17a [44]. IL-17a is a proinflammatory factor that exacerbates chronic inflammation in individuals with PCOS [45]. However, the contribution of eosinophils to PCOS has yet to be fully elucidated.

After a variety of machine learning models and Bayesian algorithm analyses, five hub genes (ACP5, TCF7, CEACAM3, S1PR4, and CXCR1) were ultimately identified as biomarkers for PCOS. ACP5 (Acid Phosphatase 5) encodes an iron-containing glycoprotein.

![img-10.jpeg](img-10.jpeg)

**Fig. 10** Experimental verification of five hub genes. **A** Relative expression of five hub genes in ovarian granular cells of the mouse. **B** Protein expression in mouse ovarian granular cells. **C**-**D** Negative control results. **E**-**N** IHC of five hub genes in mouse ovary tissue between the normal and PCOS groups

tartrate-resistant acid phosphatase (TRAP). The macrophage-derived monomer TRAP not only facilitates the proliferation and differentiation of adipocytes by promoting IGF-1 signalling but also promotes the occurrence of low-grade inflammation within adipose tissue, thus inducing the occurrence of proliferative obesity [46, 47]. TCF7 encodes transcription factor 1, a highly expressed gene that suppresses transcription and impacts T-cell

function [48, 49]. Research indicates that TCF7 can promote oxidative stress and metabolic dysfunction in islet β cells, leading to apoptosis via the GIPR-TCF1 axis and potentially contributing to an IR phenotype [50, 51]. CEACAM3 serves as a critical sensor in the innate immune defense mechanism to detect pathogenic threats [52]. When pathogens invade the body, CEACAM3 can promote the phagocytosis of neutrophils, driving a violent inflammatory response [53]. As a lipid signal receptor, S1PR4 participates in a diverse array of biological functions and immune regulation [54, 55]. Additionally, it has an impact on oxidative stress. Studies have shown that S1PR4 can accelerate inflammatory stress and fibrosis in hepatocytes by activating the NLRP3 inflammasome [56]. CXCR1 is closely linked to chronic inflammation. Inhibiting CXCR1/2 expression can effectively improve IR and obesity progression [57, 58]. However, additional research is required to fully understand the role of these genes in the pathogenesis of PCOS.

To provide some help for future targeted therapy in PCOS, five hub genes were applied to the DSigDB database for drug prediction and molecular docking with AutoDock. Notably, some of these drugs have been implicated in processes associated with PCOS. Ibuprofen can ameliorate hyperandrogenaemia in PCOS patients by inhibiting androgen production. The mechanism of this process involves the nonselective inhibition of COX-1 and COX-2 cyclooxygenases in ovarian membrane mesenchymal stromal cells [59]. AH23848, a prostaglandin E receptor 4 antagonist, inhibits adipose tissue macrophage migration and aggregation, attenuates systemic inflammatory responses, and modulates insulin sensitivity [60]. Dexbrompheniramine is an H1 receptor antagonist [61], and thalidomide is an organic compound with significant immunomodulatory and anti-inflammatory effects [62]. These drugs might be helpful in PCOS treatment. However, research on the application in the treatment of PCOS still lacks experimental studies and literature support.

## Strengths and limitations

First, two OSLM-related molecular clusters were identified in patients with PCOS. The different immune environments of the clusters indicate prospective implications for disease management. Second, a novel nomogram based on five hub genes was established for PCOS assessment to offer novel insights into the clinical diagnostic strategies of PCOS.

It is essential to acknowledge the limitations of the research. First, a small number of samples were included in this study, so the results still need to be validated with more PCOS patient samples. Furthermore, the validation experiment was based on a mouse model, which might differ from human characteristics. Therefore, it is anticipated that further analysis of a broader range of data types and the collection of more clinical samples will be undertaken to validate the findings.

## Conclusion

The study demonstrated that OSLM is significantly correlated with the progression of PCOS and constructed a novel model of five hub genes for PCOS risk assessment, which may lay the foundation for the early clinical diagnosis and management of PCOS.

## Abbreviations

OSLM Oxidative stress and lipid metabolism
PCOS Polycystic ovarian syndrome
IR Insulin resistance
LDL Low-density lipoprotein
HDL High-density lipoprotein
GEO Gene Expression Omnibus
DEGs Differential expression genes
DCA Decision curve analysis
RF Random forest
SVM Support vector machine model
KNN K-nearest neighbour
DHEA Dehydroepiandrosterone
IHC Immunohistochemistry
qRT-PCR Quantitative real-time PCR
WGCNA Weighted gene co-expression network analysis
PPI Protein--protein interaction

## Supplementary Information

The online version contains supplementary material available at https://doi. org/10.1186/s12944-024-02237-3.

Additional file 1. Supplementary Fig. 1. Acquisition and collation of transcription data (A) Before eliminating the batch effect. (B) Subsequent to the removal of the batch effect. (C) Prior to the data were corrected. (D) After the data were corrected
Additional file 2. Supplementary Fig. 2. WGCNA between the normal and PCOS groups. (A) Clustering dendrogram for PCOS sample. (B) The relationship between the scale-free fit index and the soft-threshold power. (C) Correlation analysis between modules and the two PCOS clusters. (D) The results of hierarchical clustering analysis
Additional file 3. Supplementary Fig. 3. Classification of 19 genes related to OSLM. (A) The square matrix heatmap of PCOS patients. (B) Dimensionality reduction analysis based on t-SNE. (C) Heatmap of the 19 overlapping genes correlated with OSLM in the two clusters. (D) Boxplot representation of the differential expression levels of 19 genes in the two clusters
Additional file 4. Supplementary Fig. 4. WGCNA between the two clusters of PCOS patients. (A) Clustering dendrogram for PCOS sample. (B) Determination of the soft-threshold power. (C) The results of hierarchical clustering analysis. (D) Heatmap of salmon module gene expression
Additional file 5. Supplementary Fig. 5. Drug prediction and molecular docking. (A) ACP5-Thalidomide. (B)TCF7-AH23848. (C) CEACAM3-Dexbrompheniramine. (D) S1PR4-3-acetyl-7-hydroxy-2H-chromen-2-one. (E) CXCR1-Ibuprofen
Additional file 6. Supplementary Table 1. Descriptive statistics of the chip data utilized in this research
Additional file 7. Supplementary Table 2. Information on genes related to OSLM
Additional file 8. Supplementary Table 3. The primers used in this study
Additional file 9. Supplementary Table 4. The dilutions used in this study

## Authors' contributions

Conceptualization: CT, SH, QY; Data curation and methodology: CT, TZ, LX, ZL, MC; Data analysis: SH, CT, XY; Funding acquisition: QY, XY, ZL; Writing the draft: CT, SH; Reviewing \& editing: QY, CT; SH; Supervision: CC, QY; All of the authors have read and approved the final manuscript.

## Funding

This research was funded by the National Natural Science Foundation of China (82002671, Qiuxia Yan), Guangdong Basic and Applied Basic Research Foundation (2023A1515220129, 2019A1515010249, Qiuxia Yan), Scientific Research Project of Guangdong Provincial Bureau of Traditional Chinese Medicine (20241387, Qiuxia Yan), Plan on enhancing scientific research in Guangzhou Medical University (2024SRP195, Qiuxia Yan), Open Research Funds from the Sixth Affiliated Hospital of Guangzhou Medical University, Qingyuan People's Hospital (202301-306, Qiuxia Yan), and Plan on enhancing innovation capacity in Guangzhou Medical University (240603131129, Xiaojun Yuan; 240603131131, Zhihong Li).

## Availability of data and materials

The datasets of this study are available in GEO database.

## Data availability

The authors confirm that the data supporting the findings of this study are available within the article and its materials or from the corresponding authors upon reasonable request.

## Declarations

## Ethics approval and consent to participate

This study was approved by the animal ethics committee of Qingyuan People's Hospital (LAEC-2023-030). The mouse handling procedures of this study adhered to the tenets of the ARRIVE guidelines.

## Consent for publication

Not applicable.

## Competing interests

The authors declare no competing interests.

## Author details

${ }^{1}$ Center for Reproductive Medicine, the Affiliated Qingyuan Hospital (Qingyuan People's Hospital), Guangzhou Medical University, Qingyuan, Guangdong 511518, China. ${ }^{2}$ Guangdong Engineering Technology Research Center of Urinary Continence and Reproductive Medicine, the Affiliated Qingyuan Hospital (Qingyuan People's Hospital), Guangzhou Medical University, Qingyuan, Guangdong 511518, China.

## Received: 16 June 2024 Accepted: 5 August 2024 Published online: 15 August 2024

## Publisher's Note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.