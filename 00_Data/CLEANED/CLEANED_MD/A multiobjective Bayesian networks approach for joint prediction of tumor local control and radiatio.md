Article type: Research Article
Title: A Multi-Objective Bayesian Networks Approach for Joint Prediction of Tumor Local Control and Radiation Pneumonitis in Non-Small-Cell Lung Cancer (NSCLC) for ResponseAdapted Radiotherapy

Authors list: Yi Luo ${ }^{\mathrm{a}^{*}}$, Daniel L. McShan ${ }^{\mathrm{a}}$, Martha M. Matuszak ${ }^{\mathrm{a}}$, Dipankar Ray ${ }^{\mathrm{a}}$, Theodore
S. Lawrence ${ }^{\mathrm{a}}$, Shruti Jolly ${ }^{\mathrm{a}}$, Feng-Ming Kong ${ }^{\mathrm{b}}$, Randall K. Ten Haken ${ }^{\mathrm{a}}$, Issam El Naqa ${ }^{\mathrm{a}}$

Affiliations list: ${ }^{\text {a }}$ Department of Radiation Oncology, the University of Michigan, Ann
Arbor, Michigan, 48103 United States
${ }^{\text {b }}$ Department of Radiation Oncology, Indiana University, Indianapolis, Indiana, 46202
United States

# * Full address for corresponding author: 

Yi Luo, PhD
Department of Radiation Oncology, Physics Division, University of Michigan
519 W. William St, Argus Bldg.1, Ann Arbor, MI 48103-4943
E-mail: yiyiLuo@med.umich.edu
Phone: (734) 936-8882.


#### Abstract

Purpose: Individualization of therapeutic outcomes in NSCLC radiotherapy is likely to be compromised by the lack of proper balance of biophysical factors affecting both tumor local control (LC) and side effects such as radiation pneumonitis (RP), which are likely to be intertwined. Here, we compare the performance of separate and joint outcomes predictions for response-adapted personalized treatment planning.


This is the author's manuscript of the article published in final edited form as:
Luo, Y., McShan, D. L., Matuszak, M. M., Ray, D., Lawrence, T. S., Jolly, S., ... Naqa, I. E. (n.d.). A Multi-Objective Bayesian Networks Approach for Joint Prediction of Tumor Local Control and Radiation Pneumonitis in Non-Small-Cell Lung Cancer (NSCLC) for Response-Adapted Radiotherapy. Medical Physics, 0(ja). https://doi.org/10.1002/mp. 13029

Methods: 118 NSCLC patients treated on prospective protocols with 32 cases of local progression and 20 cases of RP grade two or higher (RP2) were studied. 68 patients with 297 features before and during radiotherapy were used for discovery and 50 patients were reserved for independent testing. A multi-objective Bayesian network (MO-BN) approach was developed to identify important features for joint LC/RP2 prediction using extended Markov blankets as inputs to develop a BN predictive structure. Cross-validation (CV) was used to guide the MO-BN structure learning. Area under the free-response receiver operating characteristic (AU-FROC) curve was used to evaluate joint prediction performance.

Results: Important features including single nucleotide polymorphisms (SNPs), micro RNAs, pre-treatment cytokines, pre-treatment PET radiomics together with lung and tumor gEUDs were selected and their biophysical inter-relationships with radiation outcomes (LC and RP2) were identified in a pre-treatment MO-BN. The joint LC/RP2 prediction yielded an AUFROC of 0.80 ( $95 \%$ CI: $0.70-0.86$ ) upon internal CV. This improved to $0.85(0.75-0.91)$ with additional two SNPs, changes in one cytokine and two radiomics PET image features through the course of radiotherapy in a during-treatment MO-BN. This MO-BN model outperformed combined single-objective Bayesian networks (SO-BNs) during-treatment ( 0.78 (0.67-0.84)). AU-FROC values in the evaluation of the MO-BN and individual SO-BNs on the testing dataset were 0.77 and 0.68 for pre-treatment, and 0.79 and 0.71 for during-treatment, respectively.

Conclusions: MO-BNs can reveal possible biophysical cross-talks between competing radiotherapy clinical endpoints. The prediction is improved by providing additional duringtreatment information. The developed MO-BNs can be an important component of decision support systems for personalized response-adapted radiotherapy.

Keywords: Non-small-cell lung cancer, multi-objective Bayesian networks, joint prediction of LC and RP2, response-adapted radiotherapy.

# 1. INTRODUCTION 

The treatment outcomes of lung cancer patients who undergo radiation therapy are recognized to be multi-factorial and may depend on radiation dose, and their clinical, biological, imaging, and genomic characteristics before and during a course of radiotherapy ${ }^{1,2}$. For instance, the relationship between different clinical/physical features and radiation outcomes in non-small-cell lung cancer (NSCLC) can be analyzed prior to radiation treatment ${ }^{3-5}$. It has been reported that the release of cytokines in response to radiation is an important predictor of subsequent radiation-induced lung toxicities (RILT) ${ }^{6,7}$ and tumor growth/metastasis ${ }^{8}$. Through the presence of advanced high-throughput biotechnologies for measurement of patient's molecular profile such as single nucleotide polymorphisms SNPs and micro RNAs (miRNAs), research has shown that taking variations in gene structures/expression levels into consideration when planning radiotherapy can help identify patients susceptible to risks and improve their treatment outcomes ${ }^{9}$. Moreover, imaging information before and during the course of radiation treatment has been shown to help physicians reduce radiation risks and identify whether the tumor can be controlled locally $(\mathrm{LC})^{10-12}$. However, the above technologies have generated mixed results when applied independently and are not yet realizing their potentials in routine radiotherapy practice ${ }^{13}$.

Furthermore, although radiation dose escalation can generally improve patients' tumor LC, it may also increase the risks of RILTs such as radiation pneumonitis with grade $\geq 2$ $(\mathrm{RP} 2)^{14,15}$. These endpoints are typically modeled separately for each outcome compromising their predictive value for personalizing treatment. Treating these clinical endpoints separately may also overlook any potential intercrossing biophysical relationships when optimizing their competing risks/benefits. Therefore, the intent of this study is to attempt to fill this gap by developing an interpretable and efficient joint LC and RP2 prediction model from pre- and

during-treatment high dimensional datasets for personalized response-adapted NSCLC radiotherapy.

The purpose of personalized radiotherapy in NSCLC is to develop an appropriate treatment plan for an individual patient by maximizing LC while minimizing RILTs. Several modeling approaches can be employed for NSCLC treatment outcomes including analytical and data-driven methods ${ }^{16}$. Among these that would allow for good prediction while unveiling relationships between variables are Bayesian networks (BNs), which can achieve competitive performance compared to traditional statistics and other machine learning methods while remaining transparent and interpretable ${ }^{17,18}$. Moreover, given its graph-based nature, this approach can effectively handle multiple objectives simultaneously and deal with missing, imbalanced or uncertain input data. Thus, the BN modeling approach has been employed to explore possible biophysical interactions influencing radiation outcomes in a variety of cancers ${ }^{19-21}$. But these studies, including our previous work ${ }^{22,23}$, have focused on single outcome predictions instead of simultaneously considering the possible trade-offs of multiple competing radiation outcomes necessary to support clinical decision making. Hence, a multi-objective Bayesian network (MO-BN) model is developed in this paper to identify signaling cross-talks and predict LC and RP2 simultaneously before or during radiotherapy. Towards this goal, the development of a robust MO-BN would require the ability to overcome the difficulty of interrogating a large number of heterogeneous variables in small clinical datasets, which is a common challenge in cancer treatment predictive modeling. This is demonstrated in this study by utilizing prior knowledge as constraints and statistical resampling for robust model building and rigorous evaluation.

# 2. MATERIALS AND METHODS 

## 2.A. Study participants and data collection

To demonstrate our approach, we conducted a secondary analysis of 68 non-small cell lung cancer (NSCLC) patients who were treated in and before year 2009 including 20 cases of local progression and 17 cases of RP2 for discovery and model building, and 50 additional patients who were treated after year 2009 with 12 cases of progression and 3 cases of RP2 for model testing. All the patients underwent conventional fractionated radiotherapy using 3D conformal techniques. These techniques were the same prior to 2009 and after 2009. Thus, this data splitting follows the TRIPOD type $2 b$ criteria ${ }^{24}$. The median follow-up was 61 and 65 months for surviving patients in the discovery and validation datasets, respectively. If patients' clinical, radiographic, or biopsy evidence of progression were observed with a minimum follow-up of six months, they were considered to have local progression. A patient's RP was classified from five grades (CTCAE 3.0) based on clinical assessment and imaging findings, and the level of RP was defined by the maximal RP grade during followup. Here, RP2 was used to represent a complication from radiation treatment.

The patients had been treated on prospective protocols under IRB approval as described previously ${ }^{22}$. The first three protocols treated patients to standard doses (60-66 Gy) and the fourth protocol was a dose escalation study intensifying doses to persistent positron emission tomography (PET)-avid target volumes during treatment with 2.1-2.85 Gy per fraction up to a total dose of 85.5 Gy over 30 fractions ${ }^{25-27}$. Due to different doses per fraction to the tumors and varying doses per fraction across the lungs, all tumor and lung 3D total dose values were converted into their 2 Gy equivalents (EQD2) ${ }^{28}$ by an in-house software tool using the linearquadric model with an $\alpha / \beta$ of 10 Gy and 4 Gy , respectively. Generalized equivalent uniform doses (gEUDs) with various " $a$ " parameters were calculated for gross tumor volumes (GTVs) and uninvolved lungs (lung volumes exclusive of GTVs).

This article is protected by copyright. All rights reserved.

FDG-PET/CT images were acquired using clinical protocols and the pre-treatment and intra-treatment PET images were registered to the treatment planning CT using rigid registration. Radiomics image analysis for extracting global and texture-based metrics (Table 1) was performed on the GTV using customized routines in MATLAB ${ }^{29}$. Since the protocols associated with our data involved dose escalation based on avid FDG-PET regions, we opted to utilize radiomics features extracted from PET images. However, we also recognize the complementary value of $\mathrm{CT}^{30}$, which we would like to incorporate in future studies with larger sample size. Blood samples were obtained at baseline and after approximately $1 / 3$ and $2 / 3$ of the scheduled radiation doses were completed. Pre-treatment blood samples were analyzed for cytokine levels, micro RNAs (miRNAs), and single nucleotide polymorphisms (SNPs), which have been identified as candidates from the literature related to lung cancer response. The slopes of cytokine changes and the relative differences of PET tumor features (delta radiomics) from before to during treatment were also analyzed. All the features considered are summarized in Table 1 and their pre-processing steps can be described as follows.

# 2.B. Data pre-processing 

Each patient in the discovery dataset had 297 features from eight categories including 15 common dosimetric parameters (e.g., Tumor_gEUD, Lung_gEUD, D5, D90, and D95 for tumor) extracted from EQD2-corrected dose-volume histograms, 14 clinical factors (e.g., age, stage, KPS), 30 pre-treatment cytokines (e.g., pre_IL_4), the slopes (SLP) of 30 cytokine changes during the treatment course (e.g., SLP_IP_10), 62 miRNAs (e.g., miR_20a_5p), 60 SNPs (e.g., cxcr1_Rs2234671), 43 pre-treatment PET radiomics information (e.g., pre_MTV) from the tumor region, and the relative differences (RD) of 43 PET information during the treatment course (e.g., RD_GLRLM_ZSV).

This article is protected by copyright. All rights reserved.

While continuous variables, such as pre_IL_10, miR_191_5p, GLSZM_LZLGE, were discretized into three categories using the Hartemink's pairwise mutual information method, categorical variables such as Gender, COPD, SNPs, were pre-processed based on interval discretization. In general, characters are employed to describe SNPs' three different genotypes including wild type homozygote, minor allele homozygote, and heterozygote. After identifying each SNP's ancestral allele, numbers " 0 ", " 1 ", " 2 " were assigned to the homozygotes with it, the heterozygote, and the homozygotes without it, respectively. The MO-BN approach was implemented based on the "bnlearn" package in the R environment.

# 2.C. Multi-objective Bayesian network (MO-BN) development 

An appropriate MO-BN for joint prediction of LC and RP2 was established via the following two main steps:

Step 1: Large-scale feature selection: This is a variable reduction step by identifying separate extended Markov blankets (MBs) for LC and RP2 from the high-dimensional dataset. An MB of LC (or RP2) is an inner family found by the Hiton algorithm ${ }^{31}$ containing all variables carrying information about LC (or RP2) that cannot be obtained from any other variables. Then, for each member in the MB of LC (or RP2), a next-of-kin MB for this member was also derived. An extended MB includes both the inner family and its next-of-kin MB.

Step 2: Network structure learning: The main purpose of this step is to combine the important features from the LC's and RP2's extended MBs and search for the best stable MO-BN structure for joint prediction based on them. The details of Step 2 can be described as follows.

Let $N$ be the total number of candidate features from LC's plus RP2's extended MBs (Step 1) for joint prediction of these radiation outcomes, $N+2$ represents the maximum number of nodes in the MO-BN including outcome nodes LC and RP2, $n$ be the index of possible pruned variables from the candidate features (nodes) $(n=0,1,2,3 \ldots N)$. After accommodating biophysical rules (i.e., radiobiologically plausible relationships based on reported literature), Tabu Search ${ }^{32}$ is employed to generate a stable MO-BN structure from 300 randomly generated bootstrap samples. The Bayesian Dirichlet equivalent (BDe) that provides an inherent penalty for model complexity is used as a scoring function to obtain the best BN structure. The stable BN may not be the best MO-BN for joint LC and RP2 prediction, since the features were selected according to LC and RP2 separately. Then the process of finding the best MO-BN is equivalent to identifying the most important features and their strong relationship with both LC and RP2.

Suppose $t_{n}$ be the threshold for minimum edge strength connecting any two nodes in the stable MO-BN $(n=0,1,2,3 \ldots N)$, and its associated BN can be denoted as $M O_{-} B N\left(t_{n}\right)$. In a generated MO-BN, a node that has no direct or indirect connection to nodes LC and RP2 is considered as a leaf node of the BN. Clearly, in order to find the best MO-BN, it has the first priority to be eliminated due to its unimportant or redundant property. The edge strength of two nodes in the MO-BN was obtained from the retrospective dataset, and edge direction is determined from which direction has a larger probability. Then the initial threshold $t_{n}$ of edge strength is considered as 0.5 . In our study, the threshold is increased in steps of 0.02 before finding a leaf (marginal) node, and the $M O_{-} B N\left(t_{n}\right)$ can be updated accordingly.

Let $F\left(t_{n}\right)$ be the prediction performance AU-FROC of the $M O_{-} B N\left(t_{n}\right)$ based on the internal cross validation and its value can be recalculated after eliminating a leaf node from the BN. Then an optimal threshold $\left(t_{n}^{*}\right)$ of edge strength can be obtained accordingly from the

maximal $F\left(t_{n}^{*}\right)$ and its corresponding optimal $M O \_B N\left(t_{n}^{*}\right)$. This process is repeated until a stable $M O \_B N\left(t_{n^{*}}^{*}\right)$ with the best number $n^{*}$ of pruned nodes and its associated optimal threshold $t_{n}^{*}$ that maximal overall performance is achieved. This process of learning the optimal MO-BN for joint prediction of LC and RP2 is summarized in Figure 1.

Statistical re-sampling by cross-validation was used to prevent over-fitting by assessing how a statistical model will generalize to an independent dataset (internal validation). For prediction evaluation of multiple endpoints simultaneously (LC/RP2), a free-response receiver operating characteristic (FROC) curve was employed, which is an extension of the conventional ROC used with single endpoints ${ }^{33}$. In this case, a score of " 0.5 " represents a joint prediction situation that either LC or RP2 prediction is wrong, while " 1 " and " 0 " describe the conditions that both LC and RP2 predictions are correct and wrong, respectively. The FROC curve was plotted from evaluating joint prediction as its threshold is varied. The value of area under the FROC (AU-FROC) was calculated to summarize the prediction power of the generated MO-BN model using $k$-fold cross-validation, where 0.5 presents a random signal and 1.0 denotes a perfectly discriminate signal. The best pre-treatment and during-treatment MO-BNs were obtained from the structures yielding the highest AU-FROC values. The biophysical pathways between patients' important characteristics and radiation outcomes in terms of radiation dose were evaluated from the resulting MO-BNs.

# 2.D. Single-objective Bayesian network (SO-BN) approach 

The objective for evaluating single-objective BNs (SO-BNs) in this study is to compare the performance of the two separate SO-BNs (LC/RP2) to MO-BNs in terms of joint biophysical relationship discovery and the prediction power of joint radiation outcomes. The methodology for generating SO-BN, including extended MBs for feature selection, the best BN structure learning based on bootstrap samples, followed our previous work on RP2 ${ }^{22}$ and

$\mathrm{LC}^{23}$. For the sake of fair comparisons, both the SO-BNs and the MO-BNs were developed based on the whole discovery dataset, and they are also referred to as "biophysical MO-BNs" and "biophysical SO-BNs" respectively in this paper. The information related to SO-BNs obtained from our previous research for the implementation of the SO-BN approach are described as follows.

Figure 2(a) shows a stable pre-treatment SO-BN with an edge strength $\geq 0.68$ for local control (LC) prediction based on our previous research ${ }^{23}$, where 9 important biophysical predictors are identified. Their relationships in terms of radiation outcome prediction are indicated by directed edges, and the thickness of an edge represents the strength of a connection. While the green and red lines represent positive and negative influences between the connected predictors, respectively. The gray lines indicate a mixed effect between predictors, where their relationship is not necessarily monotonic (positive or negative only) and depends on the variable status and other involved variables' state. For example, in Figure $2(a)$, if pre-IL4 is below a certain threshold, it will have a negative relationship with LC. However, if it is above that threshold, the relationship would be positive. 7-fold crossvalidation was conducted to evaluate the pre-treatment SO-BN, and its AUC value is 0.81 with a $95 \%$ confidence interval (CI) of $0.74-0.88$ based on 2000 stratified bootstrap replicates. Figure 2(b) shows a stable pre-treatment SO-BN with an edge strength $\geq 0.65$ for RP2 prediction from our previous work ${ }^{22}$. Based on 7 -folds cross validation, the AUC value is 0.82 with a $95 \%$ CI of $0.72-0.87$.

The extended MBs to obtain pre-treatment SO-BNs for LC and RP2 prediction based on pre-treatment training data are shown in Figure 3, where the inner family and the extended family of the radiation outcomes were obtained from the first and the second layers of their extended MB neighborhoods. An example to illustrate the extended MBs of RP2 can be found in our previous work ${ }^{22}$.

During the course of radiotherapy, the slopes of cytokine levels from before to during treatment (SLP) and the relative changes of PET tumor radiomics before and during treatment (RD) were incorporated into the BN model building process. Figure 4(a) shows a during-treatment SO-BN with an edge strength $\geq 0.7$ for LC prediction, and the AUC of 7fold cross-validation is 0.84 with a $95 \%$ CI of $0.78-0.91$ based on 2000 stratified bootstrap replicates. Figure $4(b)$ shows a stable during-treatment SO-BN with an edge strength $\geq 0.65$ for RP2 prediction from our previous work ${ }^{22}$, and its AUC value is 0.87 with a $95 \%$ CI of $0.80-0.91$ based on 7 -folds cross validation. The extended MBs to obtain during-treatment SO-BNs for LC and RP2 prediction based on during-treatment training data are shown in Figure 5.

During the internal $k$-fold cross-validation, the predicted LC or RP2 from corresponding SO-BNs before and during radiation treatment was evaluated, and the joint prediction in each patient was obtained by reference to his/her observed events using AU-FROC scoring as in the MO-BN approach. These results were compared to those of pre- and during-treatment MO-BNs.

# 2.E. External model testing 

As stated previously, an additional 50 patients with 12 cases of local progression and 3 cases of RP2 were reserved for external testing. As these patients had some data missing from one or more categories (first column of Table 1), they were not considered in the discovery phase of the BNs. After marginalizing the missing data from the obtained biophysical MOBNs, these patients were treated as validation dataset in our study. This also allows for the evaluation of another important advantage of BNs, which is their ability to perform reliably with missing/imbalanced information by inherent imputing of such data.

This article is protected by copyright. All rights reserved.

# 3. RESULTS 

## 3.A. Pre-treatment MO-BN model building and internal validation

The extended MBs to obtain pre-treatment SO-BNs for LC and RP2 prediction are shown in Figure 3, and all members of the two extended MBs were considered as potential variables of pre-treatment MO-BN. Note that the gEUDs of GTV-Composite with $a=-10$ and $\alpha / \beta=10$ Gy, which approaches minimum GTV dose, and Lungs-GTV with $a=1$ and $\alpha / \beta=4 \mathrm{~Gy}$, which corresponds to mean lung dose, were selected from the LC and RP2's extended MBs, and they are described by "Tumor_gEUD" and "Lung_gEUD", respectively.

Figure 6(a) shows a stable pre-treatment MO-BN with edge strength $\geq 0.75$ for joint prediction of LC and RP2, where one SNP (cxcr1-Rs2234671), two miRNAs (miR-191-5p and miR-20a-5p), three pre-treatment cytokines (IL-15, IL-4, IL-10), one pre-treatment PET radiomics (metabolic tumor volume (MTV)) and two kinds of dosimetric information (lung and tumor gEUDs) are selected. The figure also may reveal that given the radiation outcomes, a patient is likely to receive a radiation dose that is associated with his/her bio-profile in this particular cohort. Figure 6(b) shows the pre-treatment MO-BN FROC curve based on internal cross-validation during structure learning from the discovery dataset, with an AU-FROC value of 0.80 and a $95 \%$ CI of $0.70-0.86$. In contrast, using the two separate pre-treatment SO-BNs has an $\mathrm{AU}-\mathrm{FROC}=0.75$ with a $95 \%$ CI of $0.65-0.80$.

For comparison, conventional clinical factors (age, gender, stage, smoking, COPD, location, chemo, KPS) were combined with dosimetric (tumor and lung doses) to build a conventional (dose/clinical) BN for LC/RP2 prediction. The resulting SO-BNs and MO-BN achieved AU-FROCs of only 0.65 ( $95 \%$ CI: $0.57-0.72$ ) and 0.72 ( $95 \%$ CI: $0.60-0.77$ ), respectively.

# 3.B. During-treatment MO-BN model building and internal validation 

All members of the two extended MBs to obtain during-treatment SO-BNs for LC and RP2 prediction as shown in Figure 5 were considered as potential variables of duringtreatment MO-BN. Figure 7(a) illustrates a stable during-treatment MO-BN with edge strength $\geq 0.75$ developed via the MO-BN structure learning, and Figure 7(b) shows the internal validation FROC curve of the during-treatment MO-BN from 7-fold cross validation. It turns out that the structure learning AU-FROC of the MO-BN with errc2-Rs238406, ercc5Rs1047768 and additional during-treatment information such as the SLP of IP-10 and the RD of radiomics PET image features GLSZM-LZLGE and GLSZM-SZV improved to 0.85 (95\% CI: $0.75-0.91$ ) based on the internal cross-validation, which is better than that of pretreatment MO-BN mentioned in section 3.A. The during-treatment MO-BN performs better than the corresponding combined SO-BNs ( $0.78[95 \%$ CI: $0.67-0.84]$ ).

The conditional probability tables (CPTs) of during-treatment biophysical MO-BN for LC and RP2 prediction are summarized in Appendix A. It is noted that the CPT also reveals cases where prior knowledge could be modified by conditional probabilities connected nodes and cases where it cannot (e.g., cases where the prediction is $50 \%$ due to lack of sufficient representative information in the discovery dataset).

## 3.C. External model testing of the MO-BN and the SO-BN approaches

The FROC curves of the biophysical MO-BNs based on validation dataset before and during the treatment are illustrated in Figures 6(c) and 7(c), respectively. With additional duringtreatment information, the performance AU-FROC of the MO-BN increase from 0.77 to 0.79 on external testing. We also found out that two SO-BNs had AU-FROCs of only 0.68 or 0.71 before or during radiation treatment. In comparison, with conventional (dose/clinical) BNs

for LC/RP2 prediction, the resulting SO-BNs and MO-BN achieved AU-FROCs of only 0.62 and 0.66 , respectively. A summary of AU-FROC values is provided in Table 2.

# 4. DISCUSSION 

The manuscript presents a novel approach based on Bayesian network for combining multiple radiation outcomes for personalized response-adapted decision making in radiotherapy for NSCLC. The focus of the study was to present this methodology and analyze its performance in comparison with more frequent single output approaches using a population of 118 NSCLC patients treated on prospective protocols with competing clinical endpoints of LC and RP2.

## 4.A. Feature selection and biophysical MO-BNs building

There are many constraint-based, score-based, and hybrid learning algorithms for Bayesian network learning. However, they either handle a small dimensional dataset or act as a feature selection tool. There is no specific BN learning algorithm to obtain a stable BN structure from a dataset with a large number of features and a limited discovery sample size, which is quite common in clinical datasets. To overcome this under-powered challenge, the current novel BN model building process is decomposed into two steps to find the appropriate number of nodes and strength of edges from a retrospective dataset. First, MB features are selected for LC or RP2 separately, which reduces the number of variables to about 50. Second, a BN structure learning is conducted by balancing trade-offs between prediction noise and information loss for optimal prediction.

The purpose of this data-driven approach is to capture knowledge patterns from a retrospective dataset. How well the patterns represent the dataset was measured by the resulting prediction performance based on internal cross-validation within the discovery dataset. In an MO-BN, while the nodes represent important predictors for radiation outcomes prediction, the edges are used to indicate their connections, and the strength of an edge denotes how strong a node will affect another node. The importance of a predictor for an outcome mainly depends on its connection strength to the radiation outcome nodes directly or indirectly.

Since data noise may still impact prediction after the first step, an edge threshold was employed in the BN structure learning process to capture the most efficient BN structure to represent the dataset under study. If the strength of an edge is greater than or equal to the threshold, this edge will be kept in the MO-BN; otherwise, it will be eliminated, which may result in leaf nodes. Since the leaf nodes have no potential connection with LC and RP2, they were identified as nodes with relatively less impact on the radiation outcomes. However, whether to eliminate the leaf nodes or not depends on the prediction performance of the resulting MO-BNs. During the iterative process of increasing edge threshold and eliminating leaf nodes, the resulting AU-FROC values could increase initially and decrease after a certain point, and the optimal MO-BN with the appropriate edge strength can be identified from all the possible BNs. Figures 6(a) and 7(a) show the best knowledge discovered from the retrospective dataset based on the current MO-BN approach before and during the radiotherapy, respectively. Moreover, a naive MO-BN architecture could be derived from the general MO-BN through the marginalization of the grandparent nodes, and the MO-BN has the potential to achieve a better performance than that of a Naive MO-BN due to additional biophysical information and interaction.

# 4.B. Internal and external biophysical MO-BN models' validations 

FROC was used here to evaluate the joint BNs for LC and RP2 predictions, and the value of AU-FROC was employed to measure its performance. FROC allows for simultaneous evaluation of multiple objectives. However, alternative approaches also exist ${ }^{34}$. The optimal threshold cutoffs for prediction can be derived from these FROC curves using the Youden index $^{35}$.

Given the nature of our unique and heterogeneous datasets, we followed a TRIPOD level $2 b$ approach for model evaluation. That is, we built the MO-BN models with the most complete dataset in the discovery stage and evaluated performance using internal crossvalidation re-sampling. Then, additional NSCLC patients who had missing information were allocated to a separate cohort comprising of 50 patients, which were imputed (marginalized) using the biophysical MO-BNs. This highlights another strength of the proposed BN methodology, which is its ability to perform well in such clinically practical situations. Moreover, if the uncertainties of each measurement are known, they could be incorporated into estimating the resulting conditional probabilities using Bayes' rule.

However, there are limitations associated with our evaluation, such as the characteristics of the discovery and testing datasets were not similar for comprehensive assessment; while the LC rate was similar in both datasets, the event rate of RP2 was lower in our testing dataset compared to the discovery dataset. Therefore, further validation on complete external datasets would still be needed (TRIPOD levels 3, 4).

### 4.C. Comparison of SO-BNs and MO-BN for multiple radiation outcomes prediction

Competing radiation outcomes for NSCLC treatments are intuitively expected to be associated with each other, as would be their selected variables to predict treatment response. For personalized NSCLC radiation treatment, an individual patient's characteristics,

This article is protected by copyright. All rights reserved.

treatment plans, and radiation outcomes should be treated as a whole biophysical system. If a patient's characteristics changes, the related radiation treatment plan may be modified accordingly to achieve the same treatment outcomes. While it is possible to combine separate conventional (dose/clinical) SO-BNs or biophysical SO-BNs to create composite utilities for decision making by applying subjective heuristics, optimality is not guaranteed as in the case of MO-BN, which also would account for cross-talks among competing outcomes.

Although the extended MBs for LC and RP2 used to find the biophysical SO-BNs and MO-BNs are the same, the radiation outcomes (objectives) to guide the structure learning of these BNs are different. For each SO-BN approach, the variables and their biophysical interactions were obtained from network structure learning by maximizing the performance of a single radiation outcome prediction. Due to the relaxation of multi-objectives in a BN, the joint prediction performance of separate SO-BNs would only provide a lower bound to that of a MO-BN, and this relationship is supported by the AU-FROC results shown in Table 2. The idea could be further extended to include other outcomes besides LC and RP2. On the other hand, if a MO-BN is employed to predict either LC or RP2 alone, the prediction performance may be less in some instances than using an SO-BN to predict that single outcome due to numerical instabilities with optimization of larger number of variables in such a utility approach.

# 4.D. Identification of important features and "cross-talk" from biophysical MOBNs 

The use of separate SO-BNs may provide better predictions in some instances, but has a limited capacity to reveal the interaction between individual patients' characteristics and multiple radiation outcomes in terms of radiation treatment plans before and during a course of the radiotherapy, but a MO-BN can achieve this. Our MO-BNs analyses revealed that

cxcr1-Rs2234671, errc2-Rs238406, ercc5-Rs1047768, miR-20a-5p, miR-191-5p, pretreatment cytokines IL-10, IL-15, and IL-4, pre-treatment PET radiomics MTV, tumor and lung gEUDs, the SLP of cytokine IP-10, and the RD of PET radiomics GLSZM-ZSV and GLSZM-LZLGE are important features for both LC and RP2 prediction over the course of the radiotherapy. Moreover, the inter-relationship of these features may reveal relevant biophysical pathways impacting radiation outcomes with different treatment planning conditions. These biophysical interactions can be used to explore an in-depth understanding of underlying LC and RP2 radiobiology, which is essential for the development of molecularly targeted intervention adjuvant to radiotherapy (sensitizing the tumor while protecting uninvolved normal tissue).

The biophysical MO-BNs shown in Figures 6(a) and 7(a) can also be displayed in another manner to unravel their overlapping relationships as illustrated in Figures 8(a) and 8(b), respectively. For instance, MO-BN reveals that a cxcr1 SNP (Rs2234671) plays a dual role in RP2 and LC responses. This is corroborated by literature where it was reported that the cxcr1 SNP mediates inflammatory response through IL-8 ${ }^{36}$, and it was also found to predict tumor response ${ }^{37}$. Moreover, miRNAs in our MO-BNs act as master regulators of biophysical pathways. For instance, mir-20a can impact both RP2 and LC signaling, where it is involved in lung cancer progression through oncogenic processes like cellular proliferation, and apoptosis ${ }^{38}$ and it was also shown in ${ }^{39}$ to sustain T cell response in favor of an antitumor activity impacting cytokines changes (e.g., IP-10), which are associated with higher grade toxicities ${ }^{40}$ as could be inferred from our network. Moreover, both LC and RP2 were also affected by the interaction of different cytokines. For example, IL-10 is able to favor tumor growth both directly by affecting the tumor cells and indirectly by inhibiting immune cells ${ }^{41}$. Interleukin-15 (IL-15), a key pro-inflammatory cytokine ${ }^{42}$, can induce NK cell activation and cytotoxic T-lymphocyte responses leading to tumor regression ${ }^{43}$.

PET tumor radiomics can help predict response in NSCLC ${ }^{44}$. Yang et al. found that GLSZM-LZLGE exhibited significant temporal changes in partial metabolic responders ${ }^{45}$. Cheng et al. showed that texture parameters (GLSZM-ZSV) can help predict the survival in NSCLC patients ${ }^{46}$. These findings corroborate the interaction between PET information and the radiation outcomes found in our MO-BNs. Further details on the biophysical interpretations of the MO-BNs and their supporting literature are summarized in Appendix B. The Markovian property of a MO-BN reveals that given a set of parents' nodes, the children nodes are independent from the rest of the nodes, which can be explored from the discovery dataset by using our BN approach. Considering that the parents of these "parent" nodes can also be discovered, the biophysical MO-BNs with hierarchical Parents-Children relationships can improve our understanding of radiobiological signaling pathways. However, caution should be used in interpreting these results despite their promise, and additional external validation of the biophysical MO-BNs described here using multi-institutional data and in vitro and in vivo experimentation are still necessary.

# 4.E. Utilization of biophysical MO-BNs in clinical practice 

Patients may have their own preferences to trade-off between tumor LC and possible risks of RILT to achieve their own therapeutic ratio contentment. While a pre-treatment MO-BN helps a practitioner choose an initial plan to reach a desired treatment outcome, a duringtreatment MO-BN can refine this relationship based on early patient's response and guide decisions to maximize satisfaction, which is the underlying idea of our personalized adaptive radiotherapy decision support system (PARDSS). Based on the FROC curves from the discovery and validation datasets as shown in Figures 6 and 7, here we found that the duringtreatment MO-BN has the potential to improve RP2 and LC prediction with additional during-treatment information.

This article is protected by copyright. All rights reserved.

Our approach is primarily data-driven and in this NSCLC population, the radiation dose could be predicted by the biological characteristics, which are likely influencing conventional clinical factors. As summarized in Table 2, the conventional (dose/clinical) only models under-perform compared to biophysical BNs highlighting the need to include such biophysical factors in developing more informative PARDSS. By tracing the path entering nodes "Tumor_gEUD" and "Lung_gEUD" in Figures 6(a) and 7(a), appropriate radiation doses could be tuned to increase the predicted probability of local control and reduce RP2 risk given certain patient's characteristics (SNPs, miRNAs, cytokines, and PET information). For instance, a patient with following genetic characteristics (heterozygote allele for errc2Rs238406 and ercc5-Rs1047768, homozygotes without ancestral allele for cxcr1-Rs2234671, middle level expressions of miR-191-5p and miR-20a-5p) is selected as an example to demonstrate how pre- and during-treatment MO-BNs can be used in the clinic for responseadapted radiation treatment based on the patient's personal molecular profile. The patient's pre- and during-treatment MO-BNs from Figures 6(a) and 7(a) can also be represented by Figures 9(a) and 9(b)/9(c) using Netica (Norsys Software Corp, Vancouver, BC, Canada) as an interactive user-interface for BNs, respectively.

In the example of Figure 9, a patient is presented with low expression of cytokines (IL15, IL-4, IL-10), and medium MTV size prior to starting radiotherapy. Then, a medium tumor and lung gEUDs doses specified by red arrows in Figure 9(a) were prescribed for the first portion of the treatment, which is estimated to achieve $83.2 \%$ LC and $20.1 \%$ RP2. After the initial portion of the treatment was delivered, the patient's changes in cytokines and PET radiomics features were measured. Assuming the patient had presented a medium SLP of IP10 and high RDs of PET textures (GLSZM-LZLGE and GLSZM-ZSV), then this would indicate that this patient was possible not as sensitive to radiation dose as originally projected with an updated very low RP2 risk estimate, but with a modest updated LC estimate (62.5\%)

This article is protected by copyright. All rights reserved.

as achieved with the medium tumor gEUD as illustrated by Figure 9(b). Then, the optimal treatment plan for the rest of the radiotherapy course can be adapted by escalating the tumor gEUD to the high level range in this population while maintaining the medium lung gEUD level range as indicated by red arrows in Figure 9(c). This response-adaptation would result in an estimated $99.9 \%$ LC and $0.17 \%$ RP2. This simple example presents a proof-of-principle on how such pre- and during-treatment MO-BNs can be applied to customize and guide prescribed radiation dosage to an individual patient and potentially improve their outcomes compared to receiving a non-adaptive population-based treatment.

The impact of the limited dataset on the performance of the current data-driven BN approach is acknowledged. Since the radiation outcomes are random before knowing patients' characteristics, the prior probabilities of their radiation outcomes can be represented by 0.5 . If there is no representative patient(s) in the dataset falling into a scenario defined by a certain combination of different categories, the posterior probabilities of LC or RP2 will follow their priors and remain 0.5 as shown in some scenarios in Appendix A. Otherwise, the previous patients' radiation outcomes can help identify the posterior probabilities of LC or RP2 in a given scenario and shift their estimates upwards or downwards, accordingly. Moreover, it is possible that some outlier type patients, who had unexpected relationship between their biophysical characteristic and radiation outcomes, exist in certain scenarios creating false predictions that should be cautiously flagged too.

# 5. CONCLUSIONS 

A MO-BN structure learning approach has been developed to identify the probabilistic interrelationship among the different (genetic, cytokines, imaging) factors and their potential relationships with both LC and RP2 estimates before and during the course of NSCLC radiotherapy for the joint prediction of competing radiation outcomes. The MO-BN approach

treats individual patient's biophysical properties, treatment plan, and radiation outcomes as an integrated biophysical system. Compared to conventional dose/clinical factors only models or separate SO-BNs, MO-BN not only may provide a deeper understanding of the biophysical pathways underlying the radiation outcomes, but also could help improve the prediction of multiple radiation outcomes simultaneously. Future work will include consideration of more radiation outcomes in the MO-BN architecture, incorporation of CT radiomics, and clinical preferences, and the validation of the MO-BN prediction model with larger external datasets to advance adaptive radiation treatment planning.

Disclosure of Conflicts of Interest: The authors have no relevant conflicts of interest to disclose.

Acknowledgments: This work was supported in part by the National Institutes of Health P01 CA059827 and R01-CA142840.

# Supplemental Material 

## Appendix $A$

## Appendix $B$

## Biophysical interactions interpretation of MO-BNs in the section of Results

Based on our study of genetic variants, ercc2_Rs238406, cxcr1_Rs2234671, and ercc5_Rs 1047768 were identified as specifically prominent SNPs in our dataset. The protein encoded by ercc2_Rs238406 is involved in transcription-coupled nucleotide excision repair of damaged DNA ${ }^{47}$. Lee et al. found that this ercc2 SNP contributes to additional risk of death

and disease progression in chemoradiation therapy of esophageal cancer ${ }^{48}$. Rs2234671 is a SNP in CXCR1 gene, which overlaps both LC and RP2, it has been reported that the protein encoded by this gene is a specific receptor for the interleukin 8 (IL-8), which is chemoattractant for neutrophils and has an important role in the inflammatory response ${ }^{36}$. On the other hand, Khan et al. demonstrated that cxcr1 gene is upregulated in lung cancer patients ${ }^{49}$. Moreover, while investigating germline polymorphisms in genes involved in VEGF dependent and independent angiogenesis pathways to predict clinical outcome and tumor response in metastatic colorectal cancer patients (mCRC), Gerger et al. found that CXCR1 Rs2234671 G>C predicted tumor response in a significant level in multiple testing 50

The role of miRNAs was also demonstrated in the early stages of the disease progression and metastasis ${ }^{51}$ and an excellent biomarker for cancer diagnosis and prognosis ${ }^{52,53}$. Mir-20a was found to be associated with lung cancers, and is encoded by a gene located on chromosome 13q31, and is involved in several oncogenic processes like cellular proliferation, angiogenesis and apoptosis ${ }^{38}$. O'Donnell et al. mentioned that the transcription factor E2F1, which is involved in cell cycle progression is regulated by two miRNAs of this family, miR20 and miR-17-5p ${ }^{54}$. Mir-191 has been reported to be abnormally expressed in several cancers ( $>20$ ) and various other diseases, and it regulates important cellular processes such as cell proliferation, differentiation, apoptosis, and migration by targeting important transcription factors, chromatin remodelers, and cell cycle associated genes ${ }^{55}$. Taken together, these findings support the relationships between genetic variants and radiation outcomes LC and RP2 in our BNs.

Both LC and RP2 are also affected by the interaction of different cytokines. IL-10 is able to favor tumor growth both directly by affecting the tumor cells and indirectly by inhibition of immune cells ${ }^{41}$. Lung cancers are known to produce Th2 polarization by releasing

cytokines, besides IL-10, IL-4, IL-5, IL-6, and IL-13 may work in concert with other immunosuppressive agents or suppressor cells to produce pro-tumorgenesis effects ${ }^{56}$. Previous studies have demonstrated that human lung tumor cell lines express interleukin 4 (IL-4) receptors, and IL-4 can mediate modest to moderate anti-proliferative activity in vitro and in vivo in animal models of human lung tumors ${ }^{57}$. Vokes et al. also reported that IL-4 showed only minimal antitumor activity in lung cancer patients ${ }^{58}$. Interleukin-15 (IL-15) is a pro-inflammatory cytokine that stimulates the differentiation and proliferation of T, B, and NK cells. Over expression of IL-15 has been shown to induce NK cell activation and cytotoxic T-lymphocyte (CTL) responses leading to tumor regression ${ }^{43}$. Also, IL-15 has been hypothesized to sit at the apex of a pyramid of pro-inflammatory cytokines that includes TNF $\alpha$, IL-1 $\beta$, IL-6, IL-8, granulocyte-macrophage colony stimulating factor (GM-CSF), macrophage inflammatory protein-1 alpha (MIP-1 $\alpha$ ), and MIP-1 $\beta^{42}$. Cytokine changing during radiation treatment can also help the joint prediction of LC and RP2. Siva et al. investigated the kinetics of RT induced plasma inflammatory cytokines in order to identify clinical predictors of toxicity, and they found that early changes in levels of IP-10, MCP-1, Eotaxin, IL-6 and TIMP-1 were associated with higher grade toxicity ${ }^{40}$.

PET tumor radiomics can help identify the status of tumor response. In a multi-institutional analysis that included 101 patients with stage I-III NSCLC, MTV, disease stage, and another tumor PET heterogeneity information were deemed to provide complementary prognostic information with regards to $\mathrm{OS}^{44}$. Yang et al. performed texture analysis for the primary tumors as delineated on PET scans at each time point to examine how the extracted texture features evolved during the course of disease, and they found that GLSZM-LZLGE exhibited significant temporal changes in patients of partial metabolic responders during the course of disease ${ }^{45}$. Cheng et al. compared attenuation correction of PET images with helical CT (PET/HCT) and respiration-averaged CT (PET/ACT) in patients with non-small-cell lung

cancer (NSCLC) to investigate the impact of respiration-averaged CT on ${ }^{18} \mathrm{~F}$ FDG PET texture parameters, and they showed that texture parameters from PET/ACT such as GLSZM-ZSV are clinically useful in the prediction of survival in NSCLC patients ${ }^{46}$. These findings confirm the interaction between PET information and the radiation outcomes shown in our BNs. Table B summarizes supporting literature for the important determinants of LC and RP2 in the biophysical MO-BNs.

# Figure Legends 

Figure 1. The process of learning the best MO-BN for joint prediction of LC and RP2 from a high dimensional dataset.

Figure 2. Pre-treatment SO-BN for LC (a) and RP2 (b) prediction.
Figure 3. Extended MBs for LC and RP2 prediction before radiation treatment including the radiation outcome's inner family and the next-of-kin of each inner family member.

Figure 4. During-treatment SO-BN for LC (a) and RP2 (b) prediction.
Figure 5. Extended MBs for LC and RP2 prediction during radiation treatment including the radiation outcome's inner family and the next-of-kin of each inner family member.

Figure 6. (a) Pre-treatment MO-BN for joint prediction of LC and RP2. (b) The FROC curve of pre-treatment MO-BN based on internal cross-validation. (c) The FROC curve of pretreatment MO-BN for the independent external validation based on the testing dataset.

Figure 7. (a) During-treatment MO-BN for joint prediction of LC and RP2; (b) The FROC curve of during-treatment MO-BN based on internal cross-validation; (c) The FROC curve of during-treatment MO-BN for the independent external validation based on validation dataset.

Figure 8. Biophysical MO-BNs can reveal the interaction of important biophysical features based on the LC's and RP2's extended MBs for joint prediction of these radiation outcomes before $(a)$ and during $(b)$ the radiotherapy. Green and red nodes in the figures represent the

features selected from the LC and RP2 extended MBs, respectively, and yellow nodes indicate the predictors originating from both of them.

Figure 9. An example application of pre- and during-treatment MO-BNs for personalized response-adapted radiotherapy. (a) Identification of an individual patient's best treatment plans (indicated by red arrows) before the treatment based on pre-treatment MO-BN using Netica as an interface, where single full-size black bars in shadowed boxes indicate a patient's characteristics, and the black bars in un-shadowed boxes show the probability distribution of the radiation outcomes based on the retrospective dataset analysis; (b) Estimated patient's treatment outcomes (LC/RP2) with the best pre-treatment plan based on during-treatment MO-BN, note the changes in the estimates of LC/RP2 by incorporating the during information; (c) Adjustment of tumor dose in the during-treatment plan following estimate changes to improve LC by increasing dose noting that RP2 risk is smaller than what was originally projected in this case (specified by red arrows).

Table 1. Biophysical data description.


${ }^{a} \mathrm{D} 0.5 \mathrm{cc}$ is the dose to 0.5 cc , which indicates a maximal lung dose here.
${ }^{\mathrm{b}}$ Heart gEUD represents mean heart dose $(a=1)$.
${ }^{\text {c }}$ PET features were extracted included widely used global, gray level co-occurrence matrix (GLCM), neighborhood gray-tone difference matrix (NGTDM), run-length matrix (RLM), and gray-level size-zone matrix (GLSZM).

Table 2. Pre- and during-treatment concurrent prediction performances (AU-FROC) of both LC and RP2 from conventional (dose/clinical) SO-BNs, and from combined biophysical SOBNs, and corresponding MO-BNs on the discovery and validation datasets.


${ }^{a}$ The numbers in the parentheses represent the $95 \%$ CIs of AU-FROC.
${ }^{\mathrm{b}} \mathrm{NA}=$ not applicable.

Table $\boldsymbol{A}$. The table of conditional probabilities $P$ (LC| Tumor_gEUD, RD_GLSZM_ZSV, cxcr1-Rs2234671) and $P$ (RP2|Lung_gEUD, SLP_IP_10, cxcr1-Rs2234671).


This article is protected by copyright. All rights reserved.

Table B. Supporting literature for the important determinants of LC and RP2 in the biophysical MO-BNs


![img-0.jpeg](img-0.jpeg)

This article is protected by copyright. All rights reserved.

![img-1.jpeg](img-1.jpeg)


This article is protected by copyright. All rights reserved.

![img-2.jpeg](img-2.jpeg)


This article is protected by copyright. All rights reserved.


![img-3.jpeg](img-3.jpeg)


This article is protected by copyright. All rights reserved.

![img-4.jpeg](img-4.jpeg)

This article is protected by copyright. All rights reserved.


This article is protected by copyright. All rights reserved.

![img-5.jpeg](img-5.jpeg)

This article is protected by copyright. All rights reserved.

![img-6.jpeg](img-6.jpeg)

This article is protected by copyright. All rights reserved.

![img-7.jpeg](img-7.jpeg)
(a)
![img-8.jpeg](img-8.jpeg)
(b)


(b)

This article is protected by copyright. All rights reserved.

![img-9.jpeg](img-9.jpeg)

This article is protected by copyright. All rights reserved.

![img-10.jpeg](img-10.jpeg)

This article is protected by copyright. All rights reserved.

![img-11.jpeg](img-11.jpeg)

This article is protected by copyright. All rights reserved.