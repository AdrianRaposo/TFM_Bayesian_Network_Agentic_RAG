# Article 

## Artificial Intelligence Predicted Overall Survival and Classified Mature B-Cell Neoplasms Based on Immuno-Oncology and Immune Checkpoint Panels

Joaquim Carreras ${ }^{1, * *}$ (D), Giovanna Roncador ${ }^{2 *}$ and Rifat Hamoudi ${ }^{3,4 *}$ (D)<br>check for updates<br>Citation: Carreras, J.; Roncador, G.; Hamoudi, R. Artificial Intelligence Predicted Overall Survival and Classified Mature B-Cell Neoplasms Based on Immuno-Oncology and Immune Checkpoint Panels. Cancers 2022, 14, 5318. https://doi.org/ 10.3390/cancers14215318

Academic Editors: Kentaro Inamura and Sam Payabvash

Received: 23 September 2022
Accepted: 24 October 2022
Published: 28 October 2022
Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## (0)

Copyright: (c) 2022 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 Department of Pathology, School of Medicine, Tokai University, 143 Shimokasuya, Isehara 259-1193, Kanagawa, Japan
2 Monoclonal Antibodies Unit, Spanish National Cancer Research Center (Centro Nacional de Investigaciones Oncologicas, CNIO), Melchor Fernandez Almagro 3, 28029 Madrid, Spain
3 Department of Clinical Sciences, College of Medicine, University of Sharjah, Sharjah P.O. Box 27272, United Arab Emirates
4 Division of Surgery and Interventional Science, University College London, Gower Street, London WC1E 6BT, UK

* Correspondence: joaquim.carreras@tokai-u.jp; Tel.: +81-463-93-1121 (ext. 3170); Fax: +81-463-91-1370

Simple Summary: Artificial intelligence (AI) is a field that combines computer science with robust datasets to solve problems. AI in medicine uses machine learning and deep learning to analyze medical data and gain insight into the pathogenesis of diseases. This study summarizes and integrates our previous research and advances the analyses of macrophages. We used artificial neural networks and several types of machine learning to analyze the gene expression and protein levels by immunohistochemistry of several hematological neoplasia and pan-cancer series. As a result, the patients' survival and disease subtype classification were achieved with high accuracy. Additionally, a review of the literature on the latest progress made by AI in the hematopathology field and future perspectives are given.

Abstract: Artificial intelligence (AI) can identify actionable oncology biomarkers. This research integrates our previous analyses of non-Hodgkin lymphoma. We used gene expression and immunohistochemical data, focusing on the immune checkpoint, and added a new analysis of macrophages, including 3D rendering. The AI comprised machine learning (C5, Bayesian network, C\&R, CHAID, discriminant analysis, KNN, logistic regression, LSVM, Quest, random forest, random trees, SVM, tree-AS, and XGBoost linear and tree) and artificial neural networks (multilayer perceptron and radial basis function). The series included chronic lymphocytic leukemia, mantle cell lymphoma, follicular lymphoma, Burkitt, diffuse large B-cell lymphoma, marginal zone lymphoma, and multiple myeloma, as well as acute myeloid leukemia and pan-cancer series. AI classified lymphoma subtypes and predicted overall survival accurately. Oncogenes and tumor suppressor genes were highlighted (MYC, BCL2, and TP53), along with immune microenvironment markers of tumor-associated macrophages (M2-like TAMs), T-cells and regulatory T lymphocytes (Tregs) (CD68, CD163, MARCO, CSF1R, CSF1, PD-L1/CD274, SIRPA, CD85A/LILRB3, CD47, IL10, TNFRSF14/HVEM, TNFAIP8, IKAROS, STAT3, NFKB, MAPK, PD-1/PDCD1, BTLA, and FOXP3), apoptosis (BCL2, CASP3, CASP8, PARP, and pathway-related MDM2, E2F1, CDK6, MYB, and LMO2), and metabolism (ENO3, GGA3). In conclusion, AI with immuno-oncology markers is a powerful predictive tool. Additionally, a review of recent literature was made.

Keywords: non-Hodgkin lymphoma; mature B-cell neoplasms; immune checkpoint; immunooncology; immune microenvironment; 3D macrophages; artificial intelligence; machine learning; artificial neural networks; deep learning

# 1. Introduction 

Lymphoid neoplasms are tumors of the hematopoietic system derived from immature and mature B lymphocytes, T lymphocytes, and natural killer (NK) cells that evoke the normal stages of cell differentiation. Nevertheless, some neoplasms (such as hairy cell leukemia) show lineage heterogeneity and plasticity, and their normal counterparts cannot be found [1-7]. The 2016 revision of the World Health Organization (WHO) classification of lymphoid neoplasms [3] and the International Consensus Classification (ICC) [6] describe around 45 different subtypes of mature lymphoid neoplasms [3,6,7]. In this research, we analyzed the gene expression of some of the most relevant and frequent ones.

Chronic lymphocytic leukemia/small lymphocytic lymphoma (CLL/SLL) develops from small mature CD5+ and CD23+ B-cells with mutated or unmutated IGHV genes [3,8].

Follicular lymphoma (FL) is a neoplasia of the germinal centers of follicles (centrocytes and centroblasts), with a follicular (nodular) pattern, and is frequently associated with the IGH/BCL2 translocation (t14;18)(q32;q21) that occurs in the bone marrow [3,9,10].

Extranodal marginal zone lymphoma of mucosa-associated lymphoid tissue is an extranodal lymphoma (MALT lymphoma) composed of a heterogeneous population of small B-cells [3]. It originates in the marginal zones, but it extends into the interfollicular and follicular regions and infiltrates the epithelium, forming the lymphoepithelial lesions [3,11].

Mantle cell lymphoma (MCL) is characterized by monomorphic small to mediumsized lymphoid cells with irregular nuclei and the CCND1 translocation, originating from peripheral B lymphocytes of the inner mantle zone, CD5+, and SOX11+ in the classical form $[3,12,13]$.

Diffuse large B-cell lymphoma (DLBCL) is a neoplasm of medium or large B lymphoid cells that originate from the germinal center in the germinal center B-cell-like type, or from the post-germinal center in the activated B-cell-like type [3,14,15]. According to the clinical, morphological, and biological features, DLBCL can be subdivided into different subtypes; the remaining ones are not otherwise specified (NOS).

Burkitt lymphoma is a highly aggressive but curable lymphoma that often appears at extranodal sites or as acute leukemia. It is characterized by a monomorphic proliferation of medium-size B-cells, mitotic figures, and the MYC translocation to the immunoglobulin (IG) locus. It originates from the germinal centers. There are three epidemiological variants, with variable association with the Epstein-Barr virus (EBV): endemic, sporadic, and immunodeficiency-associated [3,16-18].

Figure 1 shows the stages of the B-lymphocyte differentiation, and the relationship with the different lymphoma subtypes [19].

Nowadays, there has been rapid advance in the field of artificial intelligence (AI), and its role in medicine is gaining relevance. AI integrates computer science and datasets to make predictions or classifications based on input data.

There are two types of artificial intelligence, weak and strong AI. Weak AI, also known as narrow AI (NAI), is trained to perform specific tasks. Conversely, strong AI includes artificial general intelligence (AGI) or artificial super intelligence (ASI), and it is expected to surpass human abilities in the future [20-26].

In this research, we used weak artificial intelligence to predict the prognosis of the patients and to classify several subtypes of mature B-cell neoplasms (output). Gene expression (transcriptomics) and protein immunohistochemical data were used as predictors (input data). The research focused on artificial neural networks (mainly multilayer perceptron), but also used other neural networks such as the radial basis function and other machine learning techniques. Regarding the neural networks, "basic" but robust and reliable architectures were chosen as an elemental part of the analysis. Then, the "basic" networks were combined in more complex, multivariate analysis algorithms. Figure 2 describes the basic structure of the neural network.

![img-0.jpeg](img-0.jpeg)

Figure 1. Postulated cell of origin of the non-Hodgkin lymphoma subtypes. In the current theory of the pathogenesis of hematopoietic and lymphoid tissues, B-cell neoplasms correspond to various stages of B-cell differentiation. For example, follicular lymphoma, Burkitt lymphoma, and diffuse large B-cell lymphoma develop (or have a stage of differentiation) from mature B lymphocytes from the germinal centers of follicles of peripheral lymphoid tissues. Of note, follicular lymphoma is characterized by the IGH/BCL2 translocation (t14;18)(q32;q21) that occurs in the bone marrow. Nevertheless, this genetic alteration is not sufficient to generate lymphoma, and additional cumulative changes are necessary.

The immune checkpoints are regulators of the immune system that belong to the self-tolerance pathways. Without them, the immune system would attach to cells indiscriminately. Cancer uses several mechanisms to proliferate, including evading the host immune response using immune checkpoint molecules. There are two types of immune checkpoint molecules: stimulatory and inhibitory. Inhibitory checkpoint molecules inhibit the immune response and include several markers such as B7-H3 (CD276), BTLA, CTLA-4, LAG3, PD-1, TIM-3, and VISTA. Nowadays, immune checkpoints are important because they are the basis of cancer immunotherapy. Currently approved checkpoint inhibitors are anti CTLA-4, PD-1, and PD-L1 [19,27,28,29,30,31,32,33,34,35]. In this research, artificial intelligence was used to classify and to predict the overall survival of different lymphoma subtypes using gene expression data, all the genes of the arrays, and specific panels of the immune checkpoint.

This manuscript integrates our previous publications to provide a general view of the results and adds new analysis on tumor-associated macrophages (TAMs).

![img-1.jpeg](img-1.jpeg)

Figure 2. The basic structure of a neural network. The network is a function of predictors (also called inputs or independent variables) that minimize the prediction error of target variables (outputs). In the case of a multilayer perceptron, it is a feed-forward architecture because the connections flow from the input to the output layer without loops. Here, four genes predict the overall survival of patients. The input layer contains these genes. The hidden layer contains the unobservable nodes (units). The output layer contains the responses; the overall survival is a categorical variable (dead vs alive).

# 2. Materials and Methods 

### 2.1. Machine Learning and Neural Networks

This research integrates all the previous analyses that were obtained using conventional biostatistics, machine learning, and artificial neural networks. Machine learning included Bayesian network, C\&R tree, C5 tree, CHAID tree, discriminant analysis, KNN algorithm, logistic regression, LSVM, Quest tree, random forest, random trees, SVM, tree-AS, XGBoost linear, and XGBoost tree. Two types of artificial neural networks were used: the multilayer perceptron and radial basis function. The digital image quantification of markers was performed using the Waikato Environment for Knowledge Analysis (Weka), and the training of the classifier included fast random forest. All the materials and methods were thoroughly described in the previous publications [19,27,28,29,30,31,32,33,34,35].

### 2.2. Multilayer Perceptron Artificial Neural Network

The multilayer perceptron architecture was chosen in most cases. Several parameters were chosen to optimize the neural network. The predictors were included in the input layer, the unobservable nodes or units in the hidden layer, and the responses in the output layer. Scale-dependent variables and covariates were rescaled to improve network training. The method for rescaling of covariates was standardized: subtract the mean and divide by the standard deviation, $(x-\text { mean }) / s$.

The series of cases were randomly partitioned into training ( $70 \%$ ) and testing ( $30 \%$ ) datasets. The best performance was found using one hidden layer. The activation function linked the weighted sums of units in a layer to the values of units in the succeeding layer. The hyperbolic tangent was usually used. This function has the form $\gamma(c)=\tanh (c)=\left(e^{c}\right.$ $\left.-e^{-c}\right) /\left(e^{c}+e^{-c}\right)$. It takes real-valued arguments and transforms them into the range $(-1,1)$. When automatic architecture selection is used, this is the activation function for all units in the hidden layers. The number of units in each hidden layer was determined automatically by an estimation algorithm.

The output layer contained the target (dependent) variables and the activation function was softmax. This function has the form: $\gamma\left(c_{\mathrm{k}}\right)=\exp \left(c_{\mathrm{k}}\right) / \Sigma_{\mathrm{j}} \exp \left(c_{\mathrm{j}}\right)$. It takes a vector of real-valued arguments and transforms it into a vector whose elements fall in the range $(0,1)$ and sum to 1 . Softmax is available only if all dependent variables are categorical.

The training type determines how the network processes the records; the training type was batch. The training options were initial lambda ( 0.0000005 ), initial sigma ( 0.00005 ), interval center ( 0 ), and interval offset $(+/-0.5)$. The network performance was assessed by the classification results, receiver operating characteristic (ROC) curve, cumulative gains chart, lift chart, predicted by observed chart, and residual by predicted chart. Using a sensitivity analysis, the independent variables were ranked according to their importance for predicting the dependent variable and in determining the neural network (Figure 3).

# Sensitivity Analysis 

For each predictor $p$ and each input pattern $m$, compute:
$d_{p m}=\max _{x_{x_{1}}, x_{x_{2}} \in S_{p}}\left\|\hat{Y}_{p}^{(m)}-\hat{Y}_{p_{t}}^{(m)}\right\|$
where $\hat{Y}_{p_{t}}^{(m)}$ is the predicted output vector (standardized if standardization of output variable is used in training) using $\left(x_{1}^{(m)}, \ldots, x_{p-1}^{(m)}, x_{p}, x_{p-1}^{(m)}, \ldots, x_{p}^{(m)}\right)$ as its input, and $S_{p}{ }^{-}$ $\left\{x_{p}^{\min }, x_{p}^{(2)}, x_{p}^{(3)}, x_{p}^{(4)}, x_{p}^{\max }\right\}$ for scale predictors and $\left\{(1,0, \ldots, 0),(0,1,0, \ldots, 0), \ldots,(0,0, \ldots, 1)\right\}$ for categorical predictors.

Then compute:
$d_{p}=\frac{1}{\lambda I} \sum_{m=1}^{M} d_{p m}$
and normalize the $d_{p}$ a to sum to 1 , and report these normalized values as the sensitivity values for the predictors. This is the average maximum amount we can expect the output to change based on changes in the $p$ th predictor. The greater the sensitivity, the more we expect the output to change when the predictor changes.

Figure 3. Sensitivity analysis. Using a sensitivity analysis, the independent variables were ranked according to their importance for predicting the dependent variable and in determining the neural network.

The general architecture for a multilayer perceptron is as follows [34]:
Input layer: $J_{0}=P$ units, $a_{0: 1}, \ldots, a_{0: J 0}$; with $a_{0: j}=x_{j}$.
Hidden layer: $J_{i}$ units, $a_{i: 1}, \ldots, a_{i: J_{i}}$; with $a_{i: k}=\gamma_{i}\left(c_{i: k}\right)$ and $c_{i: k}=\sum_{j=0}^{J i-1} w_{i: j, k} a_{i_{-} 1: j}$ where . $a_{i-1: 0}=1$
Output layer: $J_{1}=R$ units, $a_{I: 1}, \ldots, a_{I: J i}$; with $a_{I: k}=\gamma_{I}\left(c_{I: k}\right)$ and $c_{I: k}=\sum_{j=0}^{J 1} w_{I: j, k} a_{i_{-} 1: j}$ where . $a_{i-1: 0}=1$

Notation [34]:
$I$ Number of layers, discounting the input layer.
$J_{i} \quad$ Number of units in layer i. $J_{0}=P, J_{i}=R$, discounting the bias unit.
$w_{i: j, k}$ Weight leading from layer $i-1$, unit $j$ to layer $i$, unit $k$. No weights connect $a_{i-1: j}^{m}$ and the bias $a_{i-j: 0}^{m}$; that is, there is no $w_{i: j, 0}$ for any $j$.
$\gamma_{i}(c)$ Activation function for layer $i$.
$w \quad$ Weight vector containing all weights $\left(w_{1: 0,1}, w_{1: 0,2, \ldots, w_{I: J I-1, J I}}\right)$.

### 2.3. Differential Gene Expression Using the GEOR2 Software

The GEO2R 1.0 software was used to compare the differential gene expression between subtypes simply. The Benjamini-Hochberg false discovery rate was applied to adjust the $p$ values. Log transformation was applied if necessary. Limma precision weights and force normalization were not applied. The data were visualized using volcano and mean difference (MA) plots, contrasted with a level of cut-off significance set a priori at 0.05 . This software runs in R 3.2.3, Biobase 2.30.0, GEOquery 2.40.0, limma 3.26.8. Webpage: https://www.ncbi.nlm.nih.gov/geo/info/geo2r.html (accessed on 23 July 2022).

# 2.4. Gene Set Enrichment Analysis 

The Gene Set Enrichment Analysis (GSEA) was used to determine if a pathway of interest was associated with a particular biological state (for example, dead vs alive) [36,37]. The pathways were obtained from the Molecular Signatures Database (MSigDB 7.0 and greater) or designed in-house. The software GSEA v4.2.3 was downloaded from the webpage of UC San Diego, Broad Institute: http://www.gsea-msigdb.org/gsea/index.jsp (accessed on 23 July 2022).

### 2.5. Conventional Statistical Analyses

Comparisons between groups were performed using crosstabulation with Pearson Chi-Square and Fisher's exact tests, and with nonparametric Mann-Whitney U (2 groups) and Kruskal-Wallis H ( $\geq 3$ groups) tests. Survival analyses used the Kaplan-Meier and Log-rank tests, and the univariate and multivariate Cox Regression. The criteria of survival and response were the standard [38]. Overall survival was calculated from the time of diagnosis to the last contact with the patient (event recorded as alive vs dead).

### 2.6. Risk Groups

Risk groups were created using the risk score (prognostic index), which was calculated by multiplying the beta coefficients of the Cox model by the gene expression values (Risk score $=\mathrm{B}_{1} \mathrm{X}_{1}+\mathrm{B}_{2} \mathrm{X}_{2}+\ldots+\mathrm{B}_{\mathrm{p}} \mathrm{X}_{\mathrm{p}}$, where $\mathrm{x}_{\mathrm{i}}$ is the expression value and $\mathrm{B}_{\mathrm{f}}$ is the beta value of the Cox table). In the Cox, all the genes are included in a unique model [39].

### 2.7. Hardware

The analyses were performed on a desktop equipped with an AMD Ryzen 51600 and NVIDIA GeForce GTX 1050 Ti [27], Ryzen 73700X and GeForce GTX 1650 [30,33,34], and a Ryzen 9 5900X and GeForce GTX 3060 Ti [35], all with 16.0 GB of RAM.

Appendix A describes all the software that was used to perform the biostatistical analyses, including machine learning and artificial neural networks [19,27,28,29,30,31,32,33,34,35].

### 2.8. Datasets and Immunohistochemical Procedures

We used publicly available datasets downloaded from the Gene Expression Omnibus (GEO) repository, webpage: https://www.ncbi.nlm.nih.gov/geo/ (accessed on 23 July 2022) (Appendix B Table A1) [40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57], and own Tokai University Hospital gene expression (transcriptomic) and immunohistochemical (proteomic) datasets for this research.

Several of the markers that were highlighted in the AI analyses (both machine learning and artificial neural network) were validated by immunohistochemistry at the protein level. The cases were selected from the lymphoma series of Tokai University Hospital. The series of cases ranged from 100 to 293 cases, depending on the project. Immunohistochemistry was performed using a Leica Bond Max autostainer following the manufacturer's instructions (Leica K.K., Tokyo, Japan). Table 1 details the primary antibodies that were used. The review section was made on the basis of PRISMA guidelines: https://prisma-statement.org/ (accessed on 29 September 2022), Carreras, J. (20 October 2022). Systematic review. https://doi.org/10.17605/OSF.IO/436JQ. The manuscripts were selected in PubMed using the keywords "lymphoma" and "artificial intelligence", and were organized according to the type of input data as PET/CT scan, histological images, immunophenotype, clinicopathological variables, and gene expression, mutational, and integrative analysis-based artificial intelligence.

Table 1. Immunohistochemical markers used in lymphoma cases of Tokai University, School of Medicine.


CNIO, Centro Nacional de Investigaciones Oncológicas (Spanish National Cancer Research Center).

# 3. Results 

The different subtypes of hematological neoplasia (mainly non-Hodgkin lymphomas) were predicted using artificial neural networks, machine learning, and conventional biostatistics. The analysis used transcriptomic data and protein levels assessed by immunohistochemistry. The results are summarized as a bulleted list.

### 3.1. Predictive Classification of Non-Hodgkin Lymphomas

- Using the whole array of 20,863 and a cancer transcriptome panel, the lymphoma subtypes were predicted by a neural network with high accuracy [19].
- A set of 30 genes derived from the neural network also predicted the overall survival of an independent series of diffuse large B-cell lymphoma, and a pan-cancer series of 7441 cases of The Cancer Genome Atlas (TCGA) [19] (Figure 4).

![img-2.jpeg](img-2.jpeg)

**Figure 4.** Prediction of lymphoma subtype by a neural network with high accuracy. (**A**) A multilayer perceptron predicted the different non-Hodgkin lymphoma subtypes, including follicular lymphoma, mantle cell lymphoma, diffuse large B-cell lymphoma, Burkitt's lymphoma, and marginal zone lymphoma. The predictors (inputs) were the gene expression values of a pan-cancer transcriptome panel. The architecture of the network had 1769 nodes in the input layer, a hidden layer of 16 nodes, and an output layer with 5 nodes (5 lymphoma subtypes). In this figure, the top 20 most relevant genes for predicting the lymphoma subtype are shown, based on their average normalized importance for prediction. The most relevant gene was *ARG1*, followed by *MAGEA3*, *AKT2*, and *IL1B*. (**B**) This multilayer perceptron had a high performance, as shown in the ROC curve that had an area under the curve near 1. (**C–F**) Interestingly, the top 30 genes of the neural network not only predicted the lymphoma subtype but also managed to predict the overall survival of a large pan-cancer series from the TCGA of 7441 cases. Using a risk score formula, the cases of each series were stratified into high- and low-risk groups. The risk scores were calculated by multiplying the beta values of the Cox regression per gene expression values for each gene. The overall survival was calculated using the Kaplan–Meier and log-rank test and Cox regression analyses. These top 30 genes belonged to a pan-cancer transcriptome panel. Therefore, this may explain why they have predictive value in a pan-cancer series, and points out that there may be common cancer mechanisms in all human neoplasia.

### 3.2. Follicular Lymphoma, Immune Response, and Microenvironment

- An algorithm combined two types of neural networks (multilayer perceptron and radial basis function) to predict the overall survival, in combination with other clinically relevant variables [29].
- These variables were more than 60 years, the number of extranodal sites > 1, LDH-level ratio > 1, stage > 2, IPI score 2-3, with translocation (14;18) positive, immune response ratio 2:1 high (≥0.97), and overall survival up to 5 years vs alive from 10 years [29].
- As a result, new poor and favorable prognostic genes were identified, and were correlated with the immune microenvironment (M2-like tumor-associated macrophages) [29] (Figure 5 and Figure 6).
![img-3.jpeg](img-3.jpeg)

Overall Survival
![img-4.jpeg](img-4.jpeg)

Figure 5. Prediction of the overall survival of follicular lymphoma using an algorithm based on neural networks. The algorithm combined multilayer perceptron (MLP), radial basis function (RBF), and COX regression to highlight 43 genes with prognostic relevance; finally, a correlation with immuno-oncology genes was also performed. This figure shows the algorithm (method) that was used to analyze the gene expression data of follicular lymphoma using artificial neural networks. From an initial set of 22,215 genes, a strategy of dimensionality reduction highlighted 43 genes, of which 18 were associated with poor and 25 with good overall survival of the patients. The first step

consisted of several independent artificial neural networks. The network architecture included the 22,215 genes as predictors (inputs), a hidden layer, and an output layer with the predicted variable. The predicted variables were the overall survival of the patients (outcome dead vs alive), and other relevant clinicopathological variables of follicular lymphoma. The result of the neural network ranked all the genes according to their normalized importance for predicting the target variable. The results of the independent multiple neural networks were pooled resulting in 1005 genes, and the most relevant ones were highlighted using univariate and multivariate Cox regression analyses. The relevance of these genes was confirmed using gene set enrichment analysis (GSEA). Finally, these genes were also correlated with several immuno-oncology genes. The 43 genes were the following: 18 were associated with a poor prognosis (FRYL, KIAA0100, CDC40, MED8, PTP4A2, BNIP2, TMEM70, MED6, SLC24A2, KLK10, RANBP9, PRB1, EVA1B, CBFA2T2, ALDH1L1, KRT19, BTN2A3P, and TRPM4) and 25 were associated with a good prognosis of the patients (HSF2, ATPAF2, SLC7A11, PTAFR, TTLL3, TCP10L, DNAAF1, PRH1, NSDHL, TAF12, TSPAN3, AKIRIN1, ITK, TDRD12, LPP, BTD, SIRT5, ZNF230, ABHD6, TOP2B, ARPC2, ASAP2, IDH3A, PSMF1, and ARFGEF1) (Supplementary Tables S1-S5). LDH, lactate dehydrogenase; IPI, international prognostic index; IR ratio, immune response ratio; 5-y, five years; MLP, multilayer perceptron; RBF, radial basis function.

![img-5.jpeg](img-5.jpeg)

**Figure 6.** Prediction of the overall survival of follicular lymphoma using an algorithm based on neural networks. This figure shows the GSEA results of Figure 4 in detail. Gene set enrichment analysis (GSEA) was performed to confirm the results of the multivariate Cox regression for the overall survival analysis.

The set of 43 was used in addition to genes of the immune response as well as oncogenes and tumor suppressor genes related to the pathogenesis of follicular lymphoma. Of note, genes related to macrophages were highlighted, such as CD163. NOM p--val, nominal p value (the nominal p value estimates the statistical significance of the enrichment score for a single gene set); FDR q--val, false discovery rate.

- Tridimensional (3D) analysis of tumor-associated macrophages (TAMs) of follicular lymphoma and transformation to diffuse large B-cell lymphoma was associated with increased numbers of TAMs, which created a network-like structure (Figure 7).
![img-6.jpeg](img-6.jpeg)

Figure 7. Tridimensional analysis of tumor-associated macrophages (TAMs) in follicular lymphoma. The analysis of M2-like TAMs in follicular lymphoma showed that the progression from low grade to high grade, and the transformation to diffuse large B-cell lymphoma, were associated with increased numbers of TAMs, which created a physical network-like structure. This result points out that TAMs may contribute to the disease pathogenesis. In this figure, the macrophages are highlighted in pale blue (right) and green (left). B and T lymphocytes are in dark blue and red. The images were obtained using a LSM 700 laser scanning confocal microscope from Carl Zeiss (Carl-Zeiss-Strasse 22, 73447 Oberkochen, Germany), and Imaris software (version 8.4, Oxford Instruments, Belfast, United Kingdom). FL, follicular lymphoma; DLBCL, diffuse large B-cell lymphoma.

# 3.3. Follicular Lymphoma, Random Number Generator-Based Strategy 

- The random number generation created 120 independent multilayer perceptron solutions and 22,215 gene probes were ranked according to their averaged normalized importance for predicting the overall survival [35].

- The analysis identified new predictor genes, which were related to cell adhesion and migration, cell signaling, and metabolism. These genes were also correlated to the immuno-oncology markers of CD163, CSF1R, FOXP3, PDCD1 (PD-1), TNFRSF14 (HVEM), and IL10 [35].
- A comparison with other machine learning techniques was also performed. Machine learning included the following techniques: Bayesian network, C\&R tree, C5 tree, CHAID tree, discriminant analysis, KNN algorithms, logistic regression, LSVM, Quest tree, random forest, random trees, SVM, tree-AS, XGBoost linear, and XGBoost tree. A neural network analysis was also made [35] (Figure 8).

![img-7.jpeg](img-7.jpeg)

Figure 8. Prediction of the overall survival of follicular lymphoma taking advantage of the random number generator. (A) By using the random generator, 120 independent and different neural network solutions were calculated, and the averaged normalized importance of each gene for predicting the overall survival was recorded. Then, the minimal number of genes of a neural network with sufficient performance was selected, and a final neural network with 17 genes was defined. (B) This neural network (multilayer perceptron type) included 17 genes in the input layer, a hidden layer of 7 nodes, and an output layer of 2 nodes (overall survival, death vs alive). (C) A new neural network was created with the highlighted 17 genes and known immuno-oncology genes. The resulting model had an acceptable accuracy, with an area under the curve (AUC) of 0.89. The predictors (inputs) were ranked according to their normalized importance in predicting the overall survival.

### 3.4. Mantle Cell Lymphoma, Use of Immuno-Oncology Panels to Predict Survival

- An analysis algorithm included several analysis techniques such as neural networks (both the multilayer perceptron artificial and radial basis function), GSEA, and conventional statistics. In this analysis, 20,862 genes were correlated with 28 prognostic genes of mantle cell lymphoma. After dimensionality reduction, the patients' overall survival was predicted, and new markers were highlighted (Figure 9) [34].

![img-8.jpeg](img-8.jpeg)

Figure 9. Cont.

![img-9.jpeg](img-9.jpeg)

Figure 9. Prediction of the overall survival of mantle cell lymphoma using an algorithm based on neural networks. Two methods (A and B algorithms) were designed. Method 1 used as input 20,862 genes to predict the overall survival outcome (dead vs. alive) and other prognostic markers; because of dimensionality reduction, a final set of 19 genes were highlighted. The analysis also included testing the final 19 genes with other machine learning analysis, and conventional overall survival with log-rank test. Method 2 used as input several gene panels to predict the overall survival. As a result, 125 pan-cancer and immuno-oncology genes were highlighted. The association with the patients overall survival was confirmed by GSEA and conventional overall survival with log-rank test. OS, overall survival; MLP, multilayer perceptron; RBF, radial basis function; GSEA, gene set enrichment analysis; D/A, dead/Alive; AUC, area under the curve; NI, normalized importance.

- The highlighted genes were related to the cell cycle, apoptosis, and metabolism. The genes not only predicted the survival of mantle cell lymphoma, but also of diffuse large B-cell lymphoma and a large pan-cancer series of the TCGA [34].
- A neural network algorithm that combined 10 oncology and immuno-oncology panels predicted overall survival (Figure 9) [34].
- Other machine learning techniques were used. Additionally, a correlation with the MCL35 proliferation assay, which was created by the Lymphoma/Leukemia Molecular Profiling Project, was made [34] (Figure 9).


# 3.5. Diffuse Large B-Cell Lymphoma, Identification of the 25 Genes Set 

- A multilayer perceptron analysis predicted the overall survival of 100 cases using as input 54,614 gene probes, and highlighted 25 genes with prognostic value [27].
- Correlation with known diffuse large B-cell lymphoma markers showed that high expression of MYC, BCL2, and ENO3 was associated with worse outcome [27] (Figures 10 and 11).


## A. I. analysis of gene expression using a multilayer perceptron

![img-10.jpeg](img-10.jpeg)

Figure 10. A neural network predicted the overall survival of diffuse large B-cell lymphoma using gene expression data. (A) A multilayer perceptron predicted the overall survival and highlighted the most important 25 genes. (B) Using a risk score formula and the gene expression of the 25 genes, two groups of patients with different overall survival were found; this figure shows the different gene expression of the 25 genes between the two risk groups. (C) The two risk groups had different overall survival. (D) Among the 25 genes, ENO3, MYC, and BCL2 were the most important, and only with these 3 genes the survival of the patients could be determined.

![img-11.jpeg](img-11.jpeg)

Figure 11. Immunohistochemical staining of ENO3, MYC, and BCL2 in diffuse large B-cell lymphoma. This figure shows six different lymphoma cases, with high or low expression of the 3 markers. Original magnification: $400 \times($ scale bar $=50 \mathrm{um})$.
3.6. Diffuse Large B-Cell Lymphoma, Prognostic Value of the 25 Genes in Hematological Neoplasia, and TNFAIP8 Validation

- The previously identified set of 25 genes not only predicted the prognosis of 741 cases of diffuse large B-cell lymphoma, but also predicted other hematological neoplasia, including chronic lymphocytic leukemia $(n=308)$, mantle cell lymphoma $(n=92)$, follicular lymphoma $(n=180)$, multiple myeloma $(n=559)$, and acute myeloid leukemia $(n=149)$ [28].
- The TNFAIP8 marker was highlighted in this analysis. Because of TNFAIP8's importance in the apoptotic pathway, it was validated by immunohistochemistry (i.e., at protein level) in an independent series of 97 cases from Tokai University. Digital image quantification of TNFAIP8 was performed using an AI-based method. Correlations with the prognosis of the patients showed that high TNFAIP8 is associated with poor survival [28].
- TNFAIP8 correlated positively with high M2-like CD163-positive tumor-associated macrophages (TAMs) and non-GCB cell of origin phenotype [28] (Figure 12).

![img-12.jpeg](img-12.jpeg)

Figure 12. Cont.

![img-13.jpeg](img-13.jpeg)

Figure 12. A set of 25 genes derived from a neural network predicted the overall survival of several lymphoma subtypes and acute myeloid leukemia, and high protein expression of TNFAIP8 correlated with poor survival of diffuse large B-cell lymphoma patients. (A) Using the gene expression values of 25 genes, previously identified using artificial neural networks, and a risk score formula, it was possible to predict the overall survival of several hematological neoplasia (lymphomas and acute myeloid leukemia). All Kaplan-Meier analyses with log-rank tests were statistically significant and had a $p<0.001$. (B) Although all 25 genes were relevant, the strength and direction of the association was different in each subtype of hematological neoplasia. For example, TNFAIP8 was more relevant for the overall survival of diffuse large B-cell lymphoma and chronic lymphocytic leukemia, but less relevant for acute myeloid leukemia and multiple myeloma. Nevertheless, TNFAIP8 contributed to the survival of all these hematological neoplasia. (C) High TNFAIP8 protein expression, evaluated by immunohistochemistry using both conventional digital image analysis and AI-based methods, correlated with poor overall survival of diffuse large B-cell lymphoma patients. This figure shows two cases of diffuse large B-cell lymphoma. The figure at the top express low TNFAIP8. On the left, the hematoxylin (dark blue) and DAB-based (brown) immunohistochemical image is shown. As shown in the inset, the TNFAIP8 staining was cytoplasmic. On the right, the AI-based digital image analysis is shown for the same case and area. TNFAIP8 is highlighted in red, cellular structures (B lymphocytes of the lymphoma, T lymphocytes, and macrophages) in pink, and intercellular tissue in green. The figure at the bottom is characterized by high TNFAIP8 expression. After staining procedures, the immunohistochemical slides were digitalized and visualized (NanoZoomer S360 scanner and NDP.view2 viewing software, Hamamatsu KK.). Original magnification: $200 \times$. High TNFAIP8 correlated with age $>60$ years, high serum IL2RA, non-GCB phenotype, and high infiltration of CD163+ M2-like tumor-associated macrophages (CD163+TAMs). TNFAIP8 also moderately correlated with MYC (Spearman's correlation coefficient $0.389, p=0.009$ ) and Ki67 (proliferation index; Spearman's correlation coefficient $0.48, p=0.001$ ). High TNFAIP8 was also associated (trend) with worse progression-free survival ( $p=0.052$ ). Finally, a multivariate COX analysis between TNFAIP8 (high vs low) and the international prognostic index (IPI) (low+low/intermediate vs high/intermediate + high) showed that only TNFAIP8 retained the prognostic value ( $\mathrm{HR}=3.5$, $p=0.040$ ). CLL, chronic lymphocytic leukemia; DLBCL, diffuse large B-cell lymphoma; FL, follicular lymphoma; MM, multiple myeloma; MCL, mantle cell lymphoma; AML, acute myeloid leukemia.

3.7. Diffuse Large B-Cell Lymphoma, Prediction of Survival by Caspase-8

- The protein expression of caspase-8 (which is inhibited by TNFAIP8) was analyzed by immunohistochemistry in a series of 97 cases of diffuse large B-cell lymphoma, and high expression correlated with a favorable overall and progression-free survival [31].
- Based on an immunohistochemical analysis, caspase-8 was correlated with other markers of its pathway, including BCL2, caspase-3, CDK6, cleaved PARP, E2F1, Ki67, LMO2, MDM2, MYB, MYC, TNFAIP8, and TP53 [31].
- The caspase-8 protein expression was also modeled using several machine learning and artificial neural networks [31] (Figure 13 and Figure 14).
![img-14.jpeg](img-14.jpeg)

Figure 13. High caspase-8 correlated with favorable survival of diffuse large B-cell lymphoma patients. The protein levels of caspase-8 (CASP8) were evaluated by immunohistochemistry, and later correlated with the survival of the patients. Two types of immunohistochemical staining were observed, low and high. In diffuse large B-cell lymphoma, high caspase-8 expression is associated with a favorable overall survival ( $p=0.005$ ). Additionally, other markers of the capsase-8 pathway, including caspase-3, cleaved PARP, BCL2, TP53, MDM2, MYC, Ki67, E2F1, CDK6, MYB, LMO2, and TNFAIP8, were evaluated by immunohistochemistry and quantified using digital image analysis. Caspase-8 was successfully predicted by the pathway markers, both using conventional statistics and several machine learning techniques and artificial neural networks. Of note, after staining procedures, the immunohistochemical slides were digitalized and visualized (NanoZoomer S360 scanner and NDP.view2 viewing software, Hamamatsu KK.). Original magnification: $400 \times$ (scale bar $=50 \mathrm{um}$ ). OS, overall survival; ROC curve, the receiver operating characteristic curve.

![img-15.jpeg](img-15.jpeg)

**Figure 14.** High caspase-8 correlated with favorable survival of diffuse large B-cell lymphoma patients. This figure shows the immunohistochemical expression of active subunit p18 casp-8 (CASP8), which correlated with good prognosis of the patients when high. Other related markers, as shown in the protein–protein interaction analysis, were also analyzed by immunohistochemistry. After staining procedures, the immunohistochemical slides were digitalized and visualized (NanoZoomer S360 scanner and NDP.view2 viewing software, Hamamatsu KK.). All the markers were quantified using digital image analysis. This figure shows examples of low and high expressions for each marker. Original magnification: 400× (scale bar = 50 µm).

### 3.8. Diffuse Large B-Cell Lymphoma, CD274 (PD-L1) and IKAROS

- An algorithm included multilayer perceptron, radial basis function, GSEA, COX regression, and several machine learning techniques to predict the overall survival of 414 cases of diffuse large B-cell lymphoma [30].
- The machine learning techniques were Bayesian network, C5.0 algorithm, chi-squared automatic interaction detection CHAID tree, classification and regression (C&R) tree, discriminant analysis, logistic regression, Quest tree, random trees, and tree-AS. The neural network was the multilayer perceptron [30].
- The association of PD-L1 (CD274) and IKAROS with the overall survival was validated in an independent series of 113 cases by immunohistochemistry. The quantification included an AI-based method [30] (Figure 15).

![img-16.jpeg](img-16.jpeg)

**Figure 15.** An algorithm that included artificial neural networks and machine learning predicted the survival of diffuse large B-cell lymphoma, and highlighted *PD-L1* and *IKAROS* as prognostic markers. (**A**) Algorithm: This algorithm is similar to that one of follicular lymphoma and mantle cell lymphoma. The basic structure

analysis is an artificial neural network (multilayer perceptron). In this analysis, 54,613 gene probes were used as predictors for the overall survival, but also for other relevant clinicopathological variables. The basic neural network was composed of the input layer (predictors, 54,613 gene probes), a hidden layer (automatically computed), and an output layer (predicted variable; for example, the overall survival outcome as a dichotomic variable dead vs alive, or the cell of origin classification (GCB vs ABC), etc.). The dimensionality reduction included additional steps of machine learning, Cox regression, and GSEA. (B) Digital image quantification using AI-based strategy for PD-L1 (CD274) and IKAROS. (C) High protein expression of PD-L1 correlated with poor survival of the patients. Conversely, high IKAROS was associated with favorable survival. (D) AI-based quantification correlated well with conventional digital image quantification. Therefore, both techniques provide comparable results. (E) Modeling of the overall survival using a Bayesian network. The Bayesian network builds a probability model, a graphical model that shows variables (nodes) of the dataset, and the probabilistic (conditional) independences between them. The links of the network are called arcs and represent the relationship between the variables, but do not necessarily mean cause and effect. Original magnification: 200×. OS, overall survival; NCCN IPI, National Comprehensive Cancer Network International Prognostic Index; ECOG PS, Eastern Cooperative Oncology Group Performance Status; LDH, lactate dehydrogenase; R-CHOP, rituximab, cyclophosphamide, doxorubicin hydrochloride, vincristine, and prednisolone; AI, artificial intelligence.

### 3.9. Diffuse Large B-Cell Lymphoma, CSF1R

- The protein expression of CSF1R was analyzed by immunohistochemistry in 198 cases of diffuse large B-cell lymphoma, and it was found that high CSF1R-positive TAMs were associated with poor progression-free survival (Figure 16) [32].
![img-17.jpeg](img-17.jpeg)

Figure 16. Role of CSF1R in the prognosis of diffuse large B-cell lymphoma. CSF1R was analyzed by immunohistochemistry in a series of 198 cases, and two histological patterns were found. A CSF1Rpositive B-cell pattern was characterized by favorable progression-free survival; this pattern was less frequent (around $30 \%$ of the cases). Conversely, the most frequent pattern was of CSF1Rpositive tumor-associated macrophages (TAMs) and was associated with an unfavorable outcome. Additionally, the prediction of the immunohistochemical expression of CSF1R by other CSF1R-related markers was performed using neural networks. The CSF1R-related markers were CSF1, STAT3, NFKB, MYC, and Ki67. All markers were quantified using digital image analysis. Of note, the multilayer perceptron network analyses were performed to predict both the TAM and the B-cell patterns. Our data suggested that the use of a CSF1R inhibitor such as Pexidartinib could be used in the CSF1R + TAM pattern. CSF1R, macrophage colony-stimulating factor 1 receptor; DLBCL, diffuse large B-cell lymphoma; TAM, tumor-associated macrophage, PFS, progression-free survival.

- Using a neural network, CSF1R protein expression was predicted by 10 CSF1R-related markers (CSF1, STAT3, NFKB1, Ki67, MYC, PD-L1, TNFAIP8, IKAROS, CD163, and CD68) (Figure 16) [32].
- The gene expression of CSF1R was predicted by all the genes, and by an immunooncology pattern, and correlated with SIRPA and CD47 [32] (Figure 17 and Figure 18).
![img-18.jpeg](img-18.jpeg)

Figure 17. Correlation between expression levels of CSF1R and SIRPA/CD47 in diffuse large B-cell lymphoma. The immunohistochemical pattern of CSF1R-positive tumor-associated macrophages (TAMs) suggested a relationship with other makers such as SIRPA. SIRPA is a relevant immune checkpoint marker that mediates negative regulation of phagocytosis. The histological pattern of SIRPA was of TAMs, similar to PD-L1, CD85A, and MARCO. A ligand for SIRPA is CD47. In our series, the histological pattern of CD47 was of B lymphocytes of the diffuse large B-cell lymphoma.
![img-19.jpeg](img-19.jpeg)

Figure 18. Gene expression analysis of CD47 and SIRPA in the diffuse large B-cell lymphoma. In the series of the Lymphoma/Leukemia Molecular Profiling Project (LLMPP), when analyzing only the cases with R-CHOP-like treatment, high CD47 but low SIRPA correlated with poor overall survival of the patients, and SIRPA positively correlated with CSF1R. CD47 is a ligand for SIRPA (SIRPα), a protein expressed by macrophages and dendritic cells. These two markers belong to the immune checkpoint pathway, and mediate a negative regulation of phagocytosis. R-CHOP, rituximab, cyclophosphamide, doxorubicin hydrochloride, vincristine, and prednisolone; LLMPP, Lymphoma/Leukemia Molecular Profiling Project; OS, overall survival.

3.10. Diffuse Large B-Cell Lymphoma, Pan-Cancer Immuno-Oncology Panel

- An immuno-oncology panel of 730 genes predicted the overall survival and cell-oforigin phenotype (Lymph2Cx assay) of a series of 106 diffuse large B-cell lymphoma cases, using artificial neural networks and machine learning [33].
- The association of MAPK3 with the GCB phenotype was confirmed by immunohistochemistry [33] (Figure 19).


# Prediction of the overall survival 

![img-20.jpeg](img-20.jpeg)

Figure 19. An artificial neural network predicted the overall survival of the diffuse large B-cell lymphoma patients, and the cell of origin subtype using a pan-cancer immuno-oncology gene expression panel. The analysis consisted of the multilayer perceptron. The cell of origin characterization was assessed with the NanoString Lymph2Cx assay. The performance of the network was high, 0.89 for overall survival and 0.99 for the cell of origin phenotype. GSEA analysis confirmed enrichment toward the survival outcome of the dead and the cell of origin subtype of activated (ABC) + unspecified. Using a risk score formula, with 7 genes it was possible to predict the survival of diffuse large B-cell lymphoma. The association of phospho-MAPK with the germinal center B-cell (GCB) phenotype was also noted and confirmed by immunohistochemistry. GSEA, gene set enrichment analysis. ABC, activated B-cell type; GCB, germinal center B-cell type.

### 3.11. Diffuse Large B-Cell Lymphoma, Integrative Analysis of Macrophage Markers

Gene expression profiling of 233 DLBCL patients treated with chemotherapy plus Rituximab was obtained from the series GSE10846, present in the NCBI Gene Expression Omnibus database. The prognostic value for overall survival of the gene expression of CD163 was first tested and 100 representative cases were selected, which contained high-risk (i.e. high CD163) and low-risk cases (i.e. low CD163) (Figure 20).

![img-21.jpeg](img-21.jpeg)

**Figure 20.** Analysis of macrophages in diffuse large B-cell lymphoma. The overall survival of diffuse large B-cell lymphoma was assessed based on the expression of CD163, which is an M2-like macrophage marker. High expression was associated with a poor prognosis of the patients. Then, a protein–protein functional network association analysis was performed using the macrophage markers of CD68 (pan-macrophages), CD16 (M1-like macrophages), CD163 (M2-like), PTX3 (M2clike), and MITF (M2-like), and the regulatory T lymphocytes (Tregs) marker of FOXP3. The network created a macrophage pathway that was subsequently applied to a gene set enrichment analysis (GSEA). The GSEA confirmed the association of the macrophage pathway with the high-risk group, which was characterized by poor overall survival and high CD163-positive macrophages.

A functional protein association network was created using the five macrophage and one regulatory T lymphocyte (Treg) markers: CD68, CD16, CD163, PTX3, MITF, and FOXP3 as the initial nodes (identifies). Then, the resulting network (i.e., pathway) that contained 57 markers was tested for GSEA analysis in the GSE10846 series of gene expression of diffuse large B-cell lymphoma. We identified the most relevant pathological markers (i.e., genes) that are associated with the prognosis of the patients as follows: high-risk (bad prognosis, and with high CD163 expression) vs low-risk (good prognosis, low CD163). We found that this pathway was enriched in the high-risk phenotype with a NOM p-val < 0.001 and FDR q-val < 0.001. In the enrichment score, we could identify the markers: CD163 (2nd in the list with a rank metric score of 0.515), CD16 (FCGR3B, 4th), CD68 (10th), PTX3 (15th), and MITF (23rd). Of note, FOXP3 was outside the enrichment set of genes so it was not associated with the high-risk group. Importantly, at fifth position, IL10, was identified. GSEA with markers belonging to the immune regulatory M2c-like TAM pathway was also tested with similar results (Figure 20).

The macrophage markers were analyzed at protein level by immunohistochemistry in the series of Tokai University $(n=132)$ (Figure 21). The distribution of the markers in the normal reactive tonsil was also evaluated.
![img-22.jpeg](img-22.jpeg)

Figure 21. Immunohistochemical staining of macrophage markers and regulatory T lymphocytes (Tregs) in diffuse large B-cell lymphoma. The expression of macrophage markers and Tregs was evaluated using immunohistochemical procedures. The staining confirmed that when macrophages are present at a high concentration in the tissues, their shape is more elongated and dendriform-like. CD68 is a pan-macrophage marker, CD16 is macrophage polarization M1-like, and CD163, PTX3, and MITF are M2-like. FOXP3 is a specific marker of Tregs. Original magnification: $400 \times$.

The histological analysis in reactive tonsil, a secondary lymphoid organ, showed a different distribution of the different markers. CD68-positive and MITF-positive macrophages were widely distributed in all areas. CD16-positive cells were scarce and only identified in

the lympho-epithelium, the epithelial barrier. CD163-positive macrophages were mainly present in the interfollicular regions and infrequently in the germinal centers of the follicles. PTX3-positive cells were of macrophage morphology in all areas and in the germinal centers PTX3-positive cells also had a morphology of B lymphocytes (mainly centroblasts). IL10-positive macrophages were scarce but present in all areas. Double IHC showed mutually exclusive distribution between CD163 and CD16 and partially exclusive with MITF.

The multilayer perceptron (MLP) procedure was performed to produce a predictive model for one target variable, using the values of several predictors. The target was the dead or alive variable for overall survival. The predictors were the same categorical variables used in the COX multivariate analysis: CD163, PTX3 Total, MITF, FOXP3, and IL10. The independent variables normalized importance were as follows: PTX3 Total (100\%), IL10 (95.9\%), FOXP3 (48.9\%), MITF (35.8\%), and CD163 (6.3\%) (Figure 22). This result is compatible with COX. The same procedure was performed to predict the Hans classifier and the importance was IL10 (100\%), PTX3 Total (67.1\%), FOXP3 (44.8\%), CD163 (39.8\%), and MITF (32.8\%) (Figure 22).

Additional analysis consisted of validation the macrophage markers in an independent series of cases of diffuse large B-cell lymphoma, from the Lymphoma/Leukemia Molecular Profiling Project (LLMPP), the GSE10846 (webpage: https://www.ncbi.nlm.nih.gov/geo/ query/acc.cgi?acc=GSE10846, accessed on 21 September 2022). Only the cases treated with R-CHOP-like therapy were selected $(n=233)$. Several machine learning and artificial neural networks (multilayer perceptron) were used. The dependent (target) variable was the overall survival (outcome dead vs alive). As predictors, the macrophage genes of CD163, CSF1R, PTX3, CD274 (PD-L1), and IL10 were used. Additional immuno-oncology predictors were markers previously highlighted in the analyses, including MYC, BCL2, TP53, FOXP3, CSF1, IL34, PDCD1 (PD-1), TNFRSF14, TNFAIP8, IKZF1, STAT3, NFKB1, MYD88, RELA, CASP8, CASP3, PARP1, BCL2, MKI67, ENO3, and GGA3. In total, 25 genes were analyzed and the overall survival was successfully predicted. Table 2 shows the machine learning and neural network models, the number of predictors used in the models, and the overall accuracy. Figure 16 shows the most relevant models and the most relevant genes. The models confirmed the importance of the immuno-oncology markers (Figure 23).

Table 2. Machine learning and artificial neural network analysis using gene expression data.


![img-23.jpeg](img-23.jpeg)

**Figure 22.** Prediction of the overall survival of diffuse large B-cell lymphoma by M2c-like macrophages using an artificial neural network. The overall survival of the patients was predicted using an artificial neural network using the histochemical data of the tissue samples. The network confirmed that the most relevant markers were PTX3 and IL10, which characterized the immune regulatory M2c-like macrophages. A conventional survival analysis using the Kaplan–Meier with log-rank test confirmed the association of high M2c-like macrophages with poor overall and progression-free survival of the patients. Original magnification: 400×.

![img-24.jpeg](img-24.jpeg)

Figure 23. Prediction of the overall survival of diffuse large B-cell lymphoma using immune checkpoint and immuno-oncology markers. Using gene expression data of the GSE10846 dataset, the association of markers of immune regulatory M2c-like tumor-associated macrophages and other immune checkpoint markers was assessed. The methodology included several machine learning and artificial neural networks. The overall accuracy of each method is shown in Table 2.

Using the random forest, the markers were ranked according to their significance for predicting the patients' overall survival. The random forest uses a tree model and a bagging method.

The Bayesian network is a graphical model that shows variables (nodes) in a dataset and the probabilistic, or conditional, independences between them. It constructs a probability model by combining observed and recorded evidence. The network's links (arcs) do not always depict cause and effect.

The LSVM method permits the classification of data using a linear support vector machine. With large datasets, or ones with numerous predictor fields, LSVM is an especially adequate method. In this LSVM analysis, the predictors were ranked in order of relevance.

Nearest Neighbor Analysis classifies the cases based on the resemblance to others and patterns; this chart is a lower-dimensional projection of the predictor space, which contains 25 predictors (genes).

# 4. Discussion 

Artificial intelligence (AI) is a recently developed field that integrates computer science with datasets to perform out calculations. In medicine, both machine learning and deep learning analyze medical data and gain insights on diseases. Artificial intelligence has many applications, including diagnosis, disease classification, image analysis, etc. [20-24].

Machine learning is a specialty in artificial intelligence. By using statistics, algorithms are trained to make classifications or predictions [20-23]. An algorithm of machine learning is composed of three parts:
(1) Decision process. Based on the labeled or unlabeled input data, an estimated pattern is produced by the algorithm.
(2) Error function, which evaluates the prediction of the model.
(3) Model optimization process. During the fitting, the weights are adjusted to reduce discrepancy between the known and the estimates, and weights are updated autonomously until a threshold of accuracy is met.
There are three categories of machine learning models:
(1) Supervised, which use labeled datasets, such as linear regression, logistic regression, random forest, and support vector machine (SVM).
(2) Unsupervised, which use unlabeled datasets and discover hidden patterns or data groupings without the need of human intervention, such as principal component analysis (PCA), singular value decomposition (SVD), and k-means clustering.
A linear regression algorithm is used to predict numerical values based on a linear relationship between predictors. Logistic regression is a type of supervised learning that predicts a categorical variable (binary). The clustering analysis uses unsupervised learning and identifies patterns to group the cases. Decision trees can be used to predict numerical values or to classify the data into categories; they use a branching sequence of link decisions that are represented in a tree diagram. Random forests predict a value or category by combining the results of decision trees [20].Artificial neural networks (ANNs) are algorithms that, in essence, mimic the human brain. Many data mining applications use neural networks because they are flexible and powerful for complex processes [25].

A neural network is composed of an input layer, multiple hidden layers (deep neural network), and an output layer. Most neural networks are feed-forward, which means that the flow moves in one direction from the input to the output [20-24]. The "deep" term refers to the number of layers (inclusive of input, hidden, and output layer); more than three layers can be considered in a deep learning algorithm [21]. The multilayer perceptron (MLP) and radial basis function (RBF) are used in predictive applications, and are supervised because the results can be compared with the known values of the target variables [20-26]. The input layer contains the predictors (for example, the genes). The hidden layer contains unobservable nodes (units). The value of each hidden unit is some function of the predictors. The output layer contains the responses (Figure 2).

This research predicted the prognosis (mainly the overall survival) and classified the different subtypes of mature B-cell neoplasms (non-Hodgkin lymphomas) with high accuracy. Therefore, machine learning and artificial neural networks are useful biostatistical tools in biomedical research, and it is expected that the importance of artificial intelligence in medicine will increase in the future.

This research used basic types of neural networks to obtain reliable results. The single neural networks created the basis for more complex algorithms, making the analysis similar to a classical multivariate analysis. The neural networks were also complemented with other conventional biostatistical analyses, such as gene set enrichment analysis (GSEA) and Cox regression. Additionally, other machine learning techniques were used to complement the results. Each type of machine learning has special uses, and in the results, the information that is provided was complementary.

In the different algorithms, the input data comprised all the genes of the array or specific panels. The panels that were used were carefully selected, and included cancer tran-


scriptome, pan-cancer, cancer progression, and metabolic pathways that incorporate many oncogenes and tumor suppressor genes, but also immune-related panels such as immune exhaustion, human inflammation, host response, autoimmune, and immuno-oncology. Nowadays, immuno-oncology panels are particularly relevant. This research highlighted many important immuno-oncology markers such as CD163, CSF1R, CSF1, PD-L1, IL10, TNFRSF14, TNFAIP8, PD-1, and FOXP3 which are markers of tumor-associated macrophages (TAMs), T lymphocytes, and regulatory T lymphocytes (Tregs). A complete discussion can be found in the previous publications [19,27,28,29,30,31,32,33,34,35]. Most of these markers can be targeted using inhibitors. In diffuse large B-cell lymphoma, the use of immunomodulatory drugs and immune checkpoint inhibitors is a new and promising field for treating the patients beyond the classical R-CHOP [58] (Table 3).

Table 3. Immuno-oncology and pathway-related markers that were highlighted in this research.

Interestingly, some of the identified markers were also relevant for the prognosis of nonhematological neoplasia, which suggests that there are common pathogenic mechanisms in all types of neoplasia.

AI analysis combined neural networks such as multilayer perceptron and radial basis function, and several machine learning techniques such as Bayesian network, C\&R tree, C5 tree, CHAID tree, discriminant analysis, KNN algorithm, logistic regression, LSVM, Quest tree, random forest, random trees, SVM, tree-AS, XGBoost linear, XGBoost tree. It is impossible to decide which the best technique is because each method has some strengths

and weaknesses, and its applicability depends on the type of data, number of cases, and number of variables (inputs).

The term neural network refers to a family of loosely related models that are characterized by large parameter spaces and flexible structures, derived from the study of brain function. Neural networks are the tools of choice in many data mining applications because of their power and flexibility, especially if the underlying process is complex [28].

Artificial neural networks used in prediction applications, such as multilayer perceptron (MLP) and radial basis function (RBF) networks, are supervised in the sense that the results predicted by the model are compared to known values of target variables. The choice between the MLP and RBF methods depends on the type of data and the level of complexity of the problem. The MLP method can find more complex relationships, while RBF is generally faster [30]. Deep neural networks have been criticized for being opaque because their predictions are incomprehensible to humans; their multi-layered nonlinear structure is a "black box model" [31].

We recently modeled celiac disease and ulcerative colitis using AI [59,60]. In the case of ulcerative colitis, we analyzed a series of 43 cases, including 13 healthy controls, 8 inactive ulcerative colitis, 7 non-involved active ulcerative colitis, and 15 involved active ulcerative colitis. As input, 734 genes were included. A total of 16 models were used to predict ulcerative colitis. The overall accuracy was as follows: C5 decision tree ( $100 \%, 2$ fields used); logistic regression, discriminant analysis, LSVM, SVM, XGBoost linear, XGBoost tree, and neural network ( $100 \%, 734$ fields); CHAID ( $97.7 \%, 2$ fields); random forest ( $97.7 \%, 734$ ); KNN algorithm ( $95.4 \%, 734$ ); C\&R tree ( $95.4 \%, 12$ ); Quest ( $83.7 \%, 6$ ); Bayesian network $(65.1 \%, 734)$; random trees $(0 \%, 734)$. In this research, most of the machine learning methods and neural networks had accuracy above $85 \%$. Nevertheless, the number of fields that were used was variable. As also observed in the data of mature B-cell neoplasms, decision trees have difficulties in handling a large set of variables. Bayesian networks provide acceptable results, but are not superior to neural networks. Logistic regression accuracy is usually high and uses many variables. In the end, the most practical strategy is to test all methods and select the ones that predict better. In Table 2, the same 16 models are applied to our data of diffuse large B-cell lymphoma. Generally, the machine learning methods successfully predicted the overall survival of patients with diffuse large B-cell lymphoma using immuno-oncology and immune checkpoint markers. In this particular experiment, neural networks did not have high accuracy.

In conclusion, artificial intelligence analysis is a useful tool for analyzing the prognosis and classification of non-Hodgkin lymphomas.

# 5. Review of the Literature and Future Perspective in Hematological Neoplasia Using AI 

Other groups have also used artificial intelligence in the field of hematopathology research. Table 4 provides precise updates on the latest progress made in hematological malignancies using machine learning and neural networks. The manuscripts were selected in PubMed using the keywords "lymphoma" and "artificial intelligence". Among all articles that were found within the past 3-4 years, a selection of the most recent research was made. Because of limited space, not all relevant manuscripts are included in Table 4.

Table 4. Update on the latest progress made in hematological malignancies using artificial intelligence.


Table 4. Cont.


Table 4. Cont.


Table 4. Cont.


Table 4. Cont.


H\&E, hematoxylin and eosin. The publications were selected from PubMed using the keywords "artificial intelligence" and "lymphoma".

The manuscripts were organized according to the type of input data, i.e., PET/CT scan, histological images, immunophenotype, clinicopathological variables, and gene expression, mutational, and integrative analysis-based artificial intelligence [61,62,63,64].

Worth mentioning is the work of Schmitz R et al. published in the New England Journal of Medicine in 2018. The genetics and pathogenesis of diffuse large B-cell lymphoma were analyzed using random forest. The input data from 574 diffuse large B-cell lymphoma cases included exome and transcriptome sequencing, whole-genome copy-number arraybased DNA analysis, and targeted amplicon resequencing of 372 genes to identify genetic subtypes [84].

A similar work was published by Xu-Monette ZY et al. in 2020 in Blood Advances. Based on targeted next-generation sequencing (NGS), a correlation with the cell of origin subtypes was made using AI in diffuse large B-cell lymphoma. The series of 418 cases included immunohistochemical, gene expression, DNA in situ hybridization, array CGH, and NGS sequencing. Using autoencoders and CPH models, the cases were classified according to the cell of origin and the patients' survival (overall survival and progression-free survival) [81].

Li D et al. reported in 2020 in Nature Communications a deep learning diagnostic platform for diffuse large B-cell lymphoma. The method included data from multiple hospitals. This research used histological images of H\&E to classify diffuse large B-cell lymphoma (DLBCL) vs non-DLBCL. Non-DLBCL included cases of metastatic carcinoma, melanoma, and other lymphomas. The lymphoma subtypes were chronic lymphocytic leukemia, mantle cell lymphoma, follicular lymphoma, and classical Hodgkin lymphoma. Seventeen types of convolutional neural networks were used, and the model had an accuracy of $99.7-100 \%$ [74].

In the past five years, there has been a significant increase in the use of artificial intelligence in cancer research, and many applications in hematological neoplasia have been published [85]. Many studies have used convolutional neural networks to classify digitalized histological images. Machine learning and artificial neural networks have also been used to analyze gene expression and mutational data. It is expected that in the future, artificial intelligence techniques will become a standard part of the biostatistical analysis, and complementary to "conventional" bioinformatics.

Supplementary Materials: The following supporting information can be downloaded at: https: //www.mdpi.com/article/10.3390/cancers14215318/s1, Table S1: Multilayer perceptron analysis (MLP). Table S2: Radial basis function analysis (RBF). Table S3: Genes associated to poor prognosis in the multivariate Cox survival analysis. Table S4: Genes associated to good prognosis in the multivariate Cox survival analysis. Table S5: Clinicopathological correlations with the final set of seven prognostic genes.

Author Contributions: Conceptualization, methodology, formal analysis, investigation, and writing, J.C. Resources, G.R. Resources, software, validation, R.H. All authors have read and agreed to the published version of the manuscript.

Funding: Joaquim Carreras was funded by the Ministry of Education, Culture, Sports, Science and Technology (MEXT) and the Japan Society for the Promotion of Science (JSPS) (grant numbers KAKEN 15K19061, 18K15100, and 24590430) and the Tokai University School of Medicine research incentive assistant plan (grant number 2021-B04). Rifat Hamoudi was funded by Al-Jalila Foundation (grant number AJF2018090) and University of Sharjah (grant number 22010902103).

Institutional Review Board Statement: The study was conducted in accordance with the Declaration of Helsinki, and approved by the Institutional Review Board of Tokai University, School of Medicine (protocol code IRB14R-080, and IRB20-156).

Informed Consent Statement: Informed consent was obtained from all subjects involved in the study.
Data Availability Statement: All the data are available upon request to Joaquim Carreras.
Acknowledgments: The authors thank all the colleagues who had previously contributed to the research.

Conflicts of Interest: The authors declare no conflict of interest.

# Appendix A

The analyses used several software applications, including EditPad Lite (version 8.4.0 x64, Just Great Software Co. Ltd.); Fiji (version ImageJ 1.53u, NIH); GSEA (version 4.3.2, Broad Institute); GIMP (version 2.10.8, GNU); IBM SPSS 25 to 27; IBM modeler 18 (IBM); JMP Pro 14 (JMP Statistical Discovery LLC, SAS); Microsoft excel 2016 (version 16.0.5317.1000, Microsoft Corporation); Minitab (version 21.1.0, Minitab, LLC); Morpheus matrix visualization and analysis software (version 1, https://github.com/cmap/morpheus.js, Broad Institute) (accessed date 25 October 2022); NSolver (version 4.0, NanoString); RapidMiner Studio (version 9.10.011, RapidMiner); R (version 4.2.1) (http://cran.r-project.org) (accessed date 25 October 2022); RStudio (version 2022.07.2, Build 576, RStudio, PBC); STRING proteinprotein interaction networks (version 11.5, STRING Consortium 2022); and Xlstat (Premium 2018.1, Build 49320 x64, multilingual, Addinsoft).

## Appendix B

Table A1. Publicly available datasets used in addition to the Tokai University series.


## Appendix C. Comments and Analysis Of breast Cancer Detection Using Deep Neural Networks

Breast cancer is the second most frequent type of cancer in women, just before skin cancer. Worldwide, breast cancer represents the $30 \%$ of all female cancers, and it has a mortality of about $15 \%$, but in emergent countries can reach up to $70 \%$ [86,87]. The worldwide incidence ranges from 27 to 97 cases for 100,000 [87], and in about $10 \%$ of the cases, there is a genetic predisposition or family history [87]. The most frequently associated germline mutations affect the BRCA1 and BRCA2 genes [88,89].

The development of strategies for the early detection of breast cancer is necessary to improve access to treatment and reduce the mortality rate. As described by BasurtoHurtado JA et al. [90], breast cancer detection includes four steps: image acquisition, segmentation and pre-processing, feature extraction, and classification [90].

Image acquisition can be obtained through several methods, such as mammography, ultrasound, magnetic resonance imaging (MRI), and other approaches, including microwave, computed tomography (TC), and positron emission tomography (PET) [90].

The image processing and classification strategies include several steps: region of interest (ROI) estimation, and feature extraction. The classifiers can be both unsupervised

and supervised. Examples of unsupervised classifiers include K-means and hierarchical clustering. Examples of supervised classifiers are decision trees, random forests, AdaBoost, support vector machines, artificial neural networks, and convolutional neural networks [90]. Recently, new image generation techniques have developed, such as infrared thermography (IRT). This technique has been successfully applied to breast cancer; the classification methods included several machine learning and artificial neural networks, and the accuracy ranged from $90 \%$ to $100 \%$ [90-101].

Recently, new classification algorithms have been developed, including autoencoders, deep belief networks, ladder networks, and deep neural network (DNN)-based algorithms such as the deep Kronecker neural network [90,102].

Gene expression profiling is a useful tool in medical research, both for diagnosis and for the elucidation of the disease pathogenesis. Artificial neural networks can handle gene expression profiling data successfully, and we recently described their usability in hematological neoplasia [27,28,29,30,31,32,33,34,35]. In our research, we used conventional machine learning techniques and artificial neural networks because the aim was to identify prognostic factors in a reliable and systematic manner instead of developing new advanced mathematical algorithms. Nevertheless, the performance of the artificial neural networks can be improved with the use of adaptive activation functions (AAFs). Kronecker neural networks (KNNs) are a new type of neural network with adaptive activation functions described by Jagtap AD et al. [103]. Unlike the traditional neural network architecture, in a KNN, the output of the neuron passes to more than one activation function [103]. The use of the Kronecker product in the KNN made the network wide, while at the same time, the number of trainable parameters remained low [103]. Recently, a multi-level KNN approach was used in the analysis of MRI images of brain tumors (glioma) to develop an automated glioma segmentation system [104].

The research in this manuscript focuses on immuno-oncology markers, as we have recently described [85]. In relation to breast cancer, we tested the prognostic value of a set of 718 genes from a pan-cancer immune profiling panel on the overall survival of the patients. A series of 1215 breast cancer patients from The Cancer Genome Atlas (TCGA) was selected. Unfortunately, in this model, a multilayer perceptron analysis failed to properly predict the overall survival of the patients ( $83.7 \%$ overall percent of correct classification, AUC $=0.61$ ). Next, the input was narrowed to 16 genes: macrophage markers (CD68, CSF1R, CD163, CSF1R, CSF1, IL10, CD274 (PD-L1), and TNFAIP8), T helper cells (PDCD1/PD-1), Tregs (FOXP3), apoptosis (BCL2, CASP3, and CASP8), NFKB pathway (STAT3), and metabolism (ENO3, GGA3). The overall survival of breast cancer was predicted using 16 models, namely C5, logistic regression, Bayesian network, discriminant analysis, KNN algorithm, LSVM, random trees, SVM, tree-AS, XGBoost linear, XGBoost tree, CHAID, Quest, C\&R tree, random forest, and neural network (multilayer perceptron). Among all models, only random forest provided suitable modeling (input $=16$ fields, overall accuracy $98.4 \%$ ). The order of predictor importance was CD274, FOXP3, ENO3, IL10, CSF1R, CSF1, BCL2, GGA3, TNFAIP8, CASP8, PDCD1, CASP3, CD163, TNFRSF14, CD68, and STAT3.

Noteworthy, further analysis was performed in the breast series of the TCGA and the pan-cancer immune profiling panel. In addition to the overall survival, other survival variables were tested, including the disease-specific survival, disease-free interval, and progression-free interval. The multilayer perceptron analysis also failed to predict the survival of the patients with good performance. Additional analyses were performed. Different types of training were tested: batch, online, and mini-batch. Two types of optimization algorithms were also tested: scaled conjugate gradient, and gradient descent. The training options for the scaled conjugate gradient were the following: initial lambda ( 0.0000005 ), initial sigma ( 0.00005 ), interval center ( 0 ), and interval offset ( $\pm 0.5$ ). The training options for the gradient descent were initial learning rate ( 0.4 ), momentum ( 0.9 ), interval center ( 0 ), and the interval offset ( $\pm 0.5$ ). Of note, batch training can use both a scaled conjugate gradient and gradient descent. However, online and mini-batch are restricted to gradient descent. The training options of gradient descent in case of online and mini-batch were initial learning rate ( 0.4 ),

lower boundary of learning rate ( 0.001 ), learning rate reduction, in epochs (10), momentum (0.9), interval center (0), and interval offset ( $\pm 0.5$ ). We tried improving the network performance by changing all the training parameters, but no significant improvement in performance was achieved.
