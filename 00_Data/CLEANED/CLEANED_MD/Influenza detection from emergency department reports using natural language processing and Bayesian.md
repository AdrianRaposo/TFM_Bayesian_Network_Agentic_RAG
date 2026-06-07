# Influenza detection from emergency department reports using natural language processing and Bayesian network classifiers 

Ye Ye, ${ }^{1,2}$ Fuchiang (Rich) Tsui, ${ }^{1,2}$ Michael Wagner, ${ }^{1,2}$ Jeremy U Espino, ${ }^{1}$ Qi Li ${ }^{3}$

- Additional material is published online only. To view please visit the journal online (http://dx.doi.org/10.1136/ amiajnl-2013-001934).
${ }^{1}$ Real-time Outbreak and Disease Surveillance Laboratory (RODS), Department of Biomedical Informatics, University of Pittsburgh, Pittsburgh, Pennsylvania, USA ${ }^{2}$ Intelligent Systems Program, University of Pittsburgh, Pittsburgh, Pennsylvania, USA ${ }^{3}$ Division of Biomedical Informatics, Cincinnati Children's Hospital Medical Center, Cincinnati, Ohio, USA


## Correspondence to

Dr Fuchiang (Rich) Tsui, Real-time Outbreak and Disease Surveillance Laboratory (RODS), Department of Biomedical Informatics, University of Pittsburgh, 5607 Baum Blvd, 4th floor, Pittsburgh, PA 15206-3701, USA; tsui2@pitt.edu

Received 16 April 2013
Revised 25 September 2013
Accepted 11 December 2013
Published Online First
9 January 2014

## Abstract

Objectives To evaluate factors affecting performance of influenza detection, including accuracy of natural language processing (NLP), discriminative ability of Bayesian network (BN) classifiers, and feature selection. Methods We derived a testing dataset of 124 influenza patients and 87 non-influenza (shigellosis) patients. To assess NLP finding-extraction performance, we measured the overall accuracy, recall, and precision of Topaz and MedLEE parsers for 31 influenza-related findings against a reference standard established by three physician reviewers. To elucidate the relative contribution of NLP and BN classifier to classification performance, we compared the discriminative ability of nine combinations of finding-extraction methods (expert, Topaz, and MedLEE) and classifiers (one humanparameterized BN and two machine-parameterized BNs). To assess the effects of feature selection, we conducted secondary analyses of discriminative ability using the most influential findings defined by their likelihood ratios.
Results The overall accuracy of Topaz was significantly better than MedLEE (with post-processing) ( 0.78 vs $0.71, \mathrm{p}<0.0001$ ). Classifiers using human-annotated findings were superior to classifiers using Topaz/MedLEEextracted findings (average area under the receiver operating characteristic (AUROC): 0.75 vs 0.68 , $\mathrm{p}=0.0113$ ), and machine-parameterized classifiers were superior to the human-parameterized classifier (average AUROC: 0.73 vs $0.66, \mathrm{p}=0.0059$ ). The classifiers using the 17 'most influential' findings were more accurate than classifiers using all 31 subject-matter expertidentified findings (average AUROC: $0.76>0.70$, $\mathrm{p}<0.05$ ).
Conclusions Using a three-component evaluation method we demonstrated how one could elucidate the relative contributions of components under an integrated framework. To improve classification performance, this study encourages researchers to improve NLP accuracy, use a machine-parameterized classifier, and apply feature selection methods.


## OBJECTIVE

This study evaluated factors affecting performance of influenza detection, including accuracy of natural language processing (NLP), discriminative ability of Bayesian network (BN) classifiers, and feature selection. Utilizing free-text emergency department (ED) medical reports as input, our influenza detection system comprises a finding-extraction componentthe Topaz ${ }^{1}$ and MedLEE ${ }^{2}{ }^{3}$ NLP parsers-and a BN classifier. Our evaluation measured the classification performance over different finding-extraction
methods, over different parameterizations of the BNs, and over different sets of findings.

## BACKGROUND AND SIGNIFICANCE

There is a growing interest in leveraging routinely collected electronic health records (EHRs) for patient cohort identification to facilitate biomedical research. ${ }^{4-9}$ However, many cohorts-or 'phenotypes'-of interest are defined in part by information that is often (though not always) recorded in clinical notes. This constraint is especially true in early detection of epidemics and in the elucidation of yet-to-be-named diseases. The semi-structured free text of clinical notes must be transformed into structured representations prior to phenotype detection.

The earliest attempt to leverage free-text EHR data to detect phenotype dates to the work of Hripcsak et al, ${ }^{10}$ who used MedLEE and a rulebased classifier to detect tuberculosis cases from chest radiograph reports, obtaining positive predictive values (PPVs) in the range $0.03-0.96$ and sensitivity in the range $0.36-0.93$. Aronsky and Haug made the first use of a probabilistic classifier in conjunction with NLP to detect community-acquired pneumonia from data in an EHR. In that study, which showed discriminative ability as measured by area under the receiver operating characteristic (AUROC) curve of $0.98,{ }^{11}$ six findings were parsed from clinical documents.

The combination of NLP and classification algorithms have subsequently been applied to the automatic detection of additional phenotypes from EHR data, including inhalational anthrax (AUROC: 0.677 ), ${ }^{12}$ cataracts (PPV: 0.93 ), ${ }^{7}$ peripheral arterial disease (precision: $0.67-1$; recall: $0.84-1$ ), ${ }^{13}$ and rheumatoid arthritis (PPV: 0.94). ${ }^{14}$

Automatic influenza detection from EHR data is of particular importance because of the threat of pandemic influenza. Elkin measured the discriminative ability of an NLP parser (in the Multithreaded Clinical Vocabulary Server system at Mayo Clinic) and a regression classifier on Mayo Clinic records, obtaining an $\mathrm{AUROC}=0.764^{15}$ to discriminate between PCR or culture-positive influenza cases and PCR or culture-negative non-influenza controls.

As part of a larger system ${ }^{16}{ }^{17}$ that detects and characterizes outbreaks in the Real-time Outbreak and Disease Surveillance Laboratory (RODS) at University of Pittsburgh, we developed a Bayesian Case Detector (BCD) that uses an NLP parser to extract the influenza-related findings from ED reports and a BN classifier to compute the probability that a patient has influenza given the set of NLP

extracted findings. ${ }^{18} 19$ Tsui demonstrated high discrimination between influenza cases and non-influenza controls drawn from a low-influenza summer period (AUROC: $0.973 ; 95 \%$ CI 0.955 to $0.992) .^{18}$

In this study, we evaluated the individual components along a processing pipeline that starts with free-text ED reports and ends with a probability estimation of the presence of influenza. These components are an NLP parser used for extracting influenzarelated findings from free-text, a BN classifier utilized for performing probability estimation, and the findings selected for inferring the presence of influenza.

## MATERIALS AND METHODS

In this section, we describe the NLP parsers, the BN classifiers, the testing dataset, and the experiments.

## Natural language processing parsers

Topaz
Topaz was developed by Chapman, Chu, and colleagues in our laboratory for use in influenza and shigellosis related finding extraction from ED reports. For this reason, the output of Topaz can be used to directly set the values of nodes in the BNs that we studied. Topaz uses a pipeline of processing components to (1) find and annotate targeted clinical findings, (2) determine whether a finding is mentioned as being present or absent; historical, recent, or hypothetical; and experienced by the patient or someone else, ${ }^{20}$ and (3) assign a single value of 'present', 'absent', or 'missing' (not mentioned) to each finding taking into account synonyms and multiple possibly contradictory mentions of the finding in the report. Topaz's heuristic resolution of contradictory mentions of a clinical finding within a report includes the following rules: labeling a finding as 'present' in summary when Topaz identified at least one positive mention in a report, labeling a finding as 'absent' for a report when all mentions identified by Topaz were negative, and labeling 'missing' otherwise (when it found no mentions positive or negative).

## MedLEE

MedLEE was developed by Friedman and colleagues at Columbia University. It has a pipeline of programming components, each of which is guided by a corresponding knowledge component such as lexicon and grammar. MedLEE's pre-processor component and phrase regularization component execute tasks similar to Topaz's first step. MedLEE's parser assigns element modifiers (eg, certainty, severity) that are similar to Topaz's second step. However, the version (64-bit, 2012 release) of MedLEE that we used does not resolve contradictory mentions of findings that it extracts from a report. Since our BN classifiers require features to be 'present', 'absent', or 'missing' in summary, we applied Topaz's heuristic resolution rules to MedLEE output. In addition, we mapped some MedLEE output, which was represented by Unified Medical Language System Concept Unique Identifiers (UMLS CUIs) to a few influenza-related findings without corresponding UMLS CUIs (CUIs). For examples, we mapped C0021400 (influenza) to a 'suspected flu' finding.

## BN classifiers

A BN classifier represents probabilistic knowledge related to a classification task in the form of an acyclic graph whose structure represents dependent and independent relationships between random variables and a set of conditional probability tables (CPTs). A BN structure is the set of nodes and arcs between nodes denoting the probabilistic dependencies among the represented variables. The set of CPTs comprises a table for
each random variable in the BN structure conditioned on its parents. The structure and CPTs of a BN can be manually elicited from an expert ${ }^{21}$ or automatically estimated from training data by machine learning algorithms. ${ }^{22} 23$ We will refer to the process of specifying CPTs for a BN as parameterization in the following sections.

## Three BN classifiers

To study the effects of different parameterization methods for BN classifiers (expert, machine-parameterization) on influenza detection performance, we created three BN classifiers that differed only in how their CPTs were determined.

Author FT and two physicians defined a simple BN structure for all three classifiers (figure 1). They first identified a set of 31 clinical findings used by clinicians in diagnosing influenza. One physician is a board-certified infectious disease specialist who has over 40 years' clinical experience and more than 5 years' research experience in biomedical informatics.

They defined a near naïve BN, assuming that all of the influenza-related findings were conditionally independent given influenza status, with the exception of the 'lab confirmed flu' finding that depended on both influenza status and whether the report mentioned a nasal swab order. Naïve BN has been shown to have reasonable discriminative ability ${ }^{25} 26$ and its CPTs were easier for physicians to estimate than CPTs of a more complicated model.

## Expert-defined BN classifier

Author FT elicited conditional probabilities for each finding given its parent node(s) in the network from the infectious disease physician mentioned above. He elicited 64 conditional probabilities, including two conditional probabilities for each of 30 nodes that are assumed to be conditionally independent and four conditional probabilities for the 'lab confirmed flu' node. For example, two questions during elicitation for the 'cough' node were 'what is the probability that an influenza patient has cough?' and 'what is the probability that a non-influenza patient has cough?' We refer to the resulting classifier as the expert-defined-BN classifier.

## Machine-learned classifiers

We created a set of training data with which to parameterize another two classifiers.

## Training data for machine-learned classifiers

Influenza cases: We obtained 468 ED reports of PCR-positive influenza patients from the period January 1, 2008 to August 31, 2010. The reports were de-identified by the De-ID tool. ${ }^{27}$

Non influenza controls: We obtained 29004 de-identified ED reports of patients whose visits were not associated with a positive influenza PCR test from the period July 1, 2010 to August 31, 2010.

Using these reports, we created two training sets to parameterize the BN classifiers. One training set contained findings that were extracted using Topaz and the other training set contained findings that were extracted using MedLEE. Both training sets comprised 29472 instances where a single instance had 31 influenza-related findings.

Expectation-Maximization maximum a posteriori (EM-MAP) algorithm: Besides the expert-defined-BN classifier, we created two additional BN classifiers-both initially parameterized by expert and further trained using the Topaz training set (BN-EM-Topaz) or the MedLEE training set (BN-EM-MedLEE). We used the EM-MAP algorithm ${ }^{28}$ as the machine learning method with a stopping criterion of $|\Delta(\mathrm{P}($ model $\mid$ data $))|<0.01$.

![img-0.jpeg](img-0.jpeg)

Figure 1 Bayesian network for influenza detection (GeNle ${ }^{24}$ visualization).

We selected the EM-MAP algorithm because it can handle missing features in the training instances (eg, findings that an NLP parser labels as 'missing') and it can use CPTs elicited by experts as prior knowledge. These BN classifiers are parameterized using both expert's knowledge and training data, and are especially useful when the occurrence of certain findings is rare.

## Testing dataset

The testing dataset comprised reports for both ED patients with influenza and ED patients without influenza (shigellosis). This testing dataset was used in all experiments described in the remaining sections of Methods.

Influenza cases: We obtained 124 de-identified ED reports of all PCR-positive influenza patients seen in four EDs in Allegheny County, Pennsylvania between December 1, 2010 and June 30, 2011.

Non-influenza (shigellosis) controls: We used a convenience sample of 87 shigellosis cases from the same EDs for the period January 1, 2010 to June 30, 2010. This set represents all ED patients that have positive culture results for shigellosis. In using this non-representative sample, we recognized that shigellosis and influenza have symptomatic overlap (eg, both diseases can cause fever and diarrhea) and our BN classifier did not represent special shigellosis-related findings (eg, rectal bleeding and stool order) that might help to discriminate between the diagnoses.

Annotation method: Three board-certified physicians annotated the 211 ED reports in the testing dataset. To ensure that all physicians could reach a similar annotation baseline standard, we first asked them to review 10 sample reports together, and then we measured Cohen's к value, a measure of inter-annotator agreement. When Cohen's к value reached 0.8 or greater, we considered each physician to have reached the annotation standard. Then, each physician was assigned overlapping subsets of the reports. To ensure annotation quality, $12 \%$ of reports were reviewed by at least two annotators and their agreement was measured during the annotation process. If there was discrepancy between two physicians' annotations, the third physician would review the discrepancy and make the final decision after discussion with the other two physicians.

Using this testing dataset, we measured the NLP parsers' finding-extraction performance and classifiers' influenza-detection performance. Our primary analyses used 31 findings mentioned in the section introducing BN classifiers (figure 1), while the secondary analyses used the 17 most influential findings as we will discuss later.

## Metrics of NLP-finding-extraction performance

We measured the performance of Topaz and MedLEE using accuracy, recall, and precision. We calculated CIs using bootstrap percentiles with SAS V.9.3. ${ }^{29}$

## Measurement of the classification performance

We used the AUROC as a measure of classification performance. Since we had three finding-extraction methods (expert, Topaz, or MedLEE) and three BN classifiers (expert-defined-BN, BN-EMTopaz, or BN-EM-MedLEE), we performed nine experiments. The 'true' disease status (gold standard) was defined by laboratory test results. To compare AUROCs, we calculated p values using DeLong's two-sided comparisons ${ }^{30}$ as implemented in the $\mathrm{pROC}^{31}$ package of the R statistical software. To elucidate the relative contribution of the finding-extraction method (humanannotated findings vs Topaz/MedLEE-extracted finding) and parameterization method (human-parameterized classifier vs machine-parameterized classifiers) on classification performance, we compared AUROCs in groups using Friedman's two-way nonparametric analysis of variance model (ANOVA) ${ }^{32}$ with SAS V.9.3.

## Secondary analyses: measurement of the effect of feature selection on performance

To determine the effect of feature selection on influenza detection, we studied a subset of influenza-related findings. In a naïve BN , the posterior odds (eg, $\mathrm{P}($ disease $=$ True $\mid$ findings $) / \mathrm{P}$

(disease $=$ False $\mid$ findings)) equals the product of prior odds (ie, P (disease $=$ True $) / P($ disease $=$ False $)$ ) and the likelihood ratios (LR) of each finding. Therefore, we defined a subset of influential findings as those findings (in the BN-EM-Topaz classifier) that had LR positive ( $\mathrm{LR}^{+}$) greater than three or LR negative ( $\mathrm{LR}^{-}$) less than 0.33 (one third).

We then measured the accuracy, precision, and recall of Topaz and MedLEE for each of these findings. We further assessed AUROCs of classifiers only using these influential findings and compared them with classifiers leveraging the complete finding set using a one-sided paired Wilcoxon signed-rank test.

## RESULTS

## Inter-annotator agreement

The $\kappa$ values measuring inter-annotator agreement for each pairwise comparison of annotations of three physicians were $0.8346,0.8592$, and 0.8933 , indicating reliable agreement.

## Influenza-related findings in the testing dataset

Figure 2 shows the frequency at which the treating clinicians documented 31 influenza-related findings in the influenza and non-influenza (shigellosis) patients in the testing dataset. The most frequently documented positive finding in the influenza cases was cough $(77.42 \%)$, while the most frequently documented negative finding was cervical lymphadenopathy $(44.35 \%)$. The most frequently documented positive finding in the shigellosis cases was diarrhea ( $60.48 \%$ ), while the most frequently documented negative finding was sore throat ( $37.90 \%$ ). On average, the clinicians documented about 11 influenza-related findings (six positive findings and five negative findings) in the influenza cases and about seven influenza-related findings (three positive findings and four negative findings) in the shigellosis controls.

## NLP accuracy for influenza-related findings

Table 1 shows the overall accuracy, recall, and precision of Topaz and MedLEE for the entire set of influenza-related findings (left-hand side). The right-hand side of table 1 presents the results for a subset of influential findings and will be described in the secondary analyses section.

Because we post-processed the MedLEE output, the following evaluation results only reflect the accuracy of MedLEE for influenza findings when coupled with the post-processing that we employed.

We found that Topaz was more accurate than MedLEE at identifying influenza-related findings documented by treating clinicians in their reports (accuracy: 0.78 vs $0.71, \mathrm{p}<0.0001$ ).

Figure 2 Percentages of influenza cases and shigellosis cases with targeted influenza-related findings.
![img-1.jpeg](img-1.jpeg)

Table 1 Summary of performance measures for Topaz and MedLEE


Topaz and MedLEE had similar recall (ie, sensitivity) for positive findings ( 0.80 vs $0.79, \mathrm{p}=0.7499$ ), but Topaz had better recall for negative findings (specificity) ( 0.76 vs 0.62 , $\mathrm{p}<0.0001$ ). MedLEE's precision for positive findings (positive predictive values) was significantly better than Topaz ( 0.90 vs $0.85, \mathrm{p}=0.0002$ ), while its precision for negative findings (negative predictive value) was similar to Topaz ( 0.90 vs 0.87 , $\mathrm{p}=0.0852$ ).

## Classification performance for nine combinations

Table 2 shows the classification performance for all nine combinations of the finding-extraction method (expert, Topaz, or MedLEE) and classifier (expert-defined BN, BN-EM-Topaz, or BN-EM-MedLEE), with the upper half of the table showing for classifier using 31 findings and the lower half listing for classifier using 17 influential findings. Table 3 shows the $p$ values for each two-sided comparison of AUROCs of two combinations of finding-extraction method and classifier.

The combination of the finding-extraction method and classifier with the highest performance was the combination of expert findings with BN-EM-Topaz (AUROC: 0.79; 95\% CI 0.73 to 0.85 ), suggesting that NLP misclassification contributed to less accurate influenza case identification. The pairing with the lowest performance was the pairing of Topaz findings with expert-defined BN (AUROC: 0.64; 95\% CI 0.57 to 0.71 ), suggesting that parameters in expert-defined $B N$ may not well represent correlations between NLP extracted clinical findings and the disease.

## Effect of the finding-extraction method on classification performance

In the primary analyses, all three classifiers achieved better discriminative ability when associated with expert findings than with NLP (Topaz/MedLEE) findings (average AUROC: 0.75 vs

0.68, $\mathrm{p}=0.0113$ ). Specifically, expert-defined $B N$ classifier using expert findings was better than the same classifier using Topaz findings (AUROC: 0.70 vs $0.64, \mathrm{p}=0.0044$ ) or MedLEE findings (AUROC: 0.70 vs $0.64, \mathrm{p}=0.0083$ ). This pattern also held for the secondary (influential findings) analyses.

## Effect of classifier on classification performance

In the primary analyses, all three finding-extraction methods worked best when the classifier was BN-EM-Topaz, followed by $B N-E M$-MedLEE, then expert-defined $B N$. The machine-learned classifiers had greater discriminative ability than the expertdefined BN classifier (average AUROC: 0.73 vs 0.66 , $\mathrm{p}=0.0059$ ). For example, associated with expert findings, expertdefined $B N$ classifier (AUROC: 0.70 ) did not perform as well as either the BN-EM-Topaz classifier (AUROCs: $0.79, \mathrm{p}<0.0001$ ) or the BN-EM-MedLEE classifier (AUROCs: $0.77, \mathrm{p}=0.0042$ ). However, these differences largely disappeared in the secondary analyses using the most influential findings.

When comparing the two machine-learned classifiers in the primary analyses, we found that the BN-EM-Topaz classifier yielded greater accuracy than the BN-EM-MedLEE classifier: $\mathrm{AUROC}_{\text {expert-findings }+B N-E M-T o p a z}=0.79$ vs $\mathrm{AUROC}_{\text {expert- }}$ findings $+B N-E M-M e d L E E=0.77, \mathrm{p}=0.0195 ; \mathrm{AUROC}_{\text {Topaz-findings }+B N-}$ EM-Topaz $=0.73$ vs $\mathrm{AUROC}_{\text {Topaz-findings }+B N-E M-M e d L E E}=0.70$, $\mathrm{p}=0.0012 ; \quad \mathrm{AUROC}_{\text {MedLEE-findings }+B N-E M-T o p a z}=0.71$ vs $\mathrm{AUROC}_{\text {MedLEE-findings }+B N-E M-M e d L E E}=0.66, \quad \mathrm{p}<0.0001$. The superiority of BN-EM-Topaz over BN-EM-MedLEE remained in the secondary analyses.

Secondary analyses of NLP and classifier performance for 17 influential findings
The 17 influential findings indicated in BN-EM-Topaz were arthralgia, cervical lymphadenopathy, chill, cough, fever, hoarseness, influenza-like illness, lab confirmed influenza, lab order (nasal

Table 2 AUROCs ( $95 \%$ CIs) of nine possible combinations of finding-extraction method and BN classifier


*The 17 influential findings indicated in BN-EM-Topaz were arthralgia, cervical lymphadenopathy, chill, cough, fever, hoarseness, influenza-like illness, lab confirmed influenza lab order (nasal swab), malaise, myalgia, rhinorrhea, sore throat, suspected flu, viral infection, viral syndrome, and wheezing.
AUROC, area under the receiver operating characteristic; BN, Bayesian network.
swab), malaise, myalgia, rhinorrhea, sore throat, suspected flu, viral infection, viral syndrome, and wheezing (figures 3 and 4).

The right-hand side of table 1 compares the finding-extraction accuracy of Topaz and MedLEE for these findings. Topaz still had a significantly higher accuracy than MedLEE for these 17 findings with value of being either present or absent ( 0.75 vs 0.70 , $\mathrm{p}=0.0047$ ). Similarly, Topaz's recall for negative findings was still significantly higher than MedLEE's ( 0.81 vs $0.58, \mathrm{p}<0.0001$ ). However, Topaz's recall for positive findings became significantly lower than MedLEE's ( 0.72 vs $0.77, \mathrm{p}=0.0453$ ). The accuracy, recall, and precision of Topaz and MedLEE for each finding are listed in online supplemental table S1.

The lower half of table 2 lists AUROCs of nine combinations of finding-extraction method and BN classifier. Comparing
them with the upper half, we found that classifiers that only used the 17 influential findings had significantly better performance (average AUROC: $0.76>0.70, \mathrm{p}=0.004$ ).

## DISCUSSION

## Effects of finding-extraction on classification performance

The accuracy of NLP extraction of influenza-related findings from ED reports varies by finding and differs for the determination of positive and significant negative findings. The Topaz and MedLEE parsers accurately determined $71-78 \%$ of the findings. Topaz performed significantly better than MedLEE on mentions of absent findings (significant negatives) ( 0.76 vs $0.62, \mathrm{p}<0.0001$ ), and MedLEE had significantly better precision for positive findings ( 0.90 vs $0.85, \mathrm{p}=0.0002$ ). The accuracy of MedLEE could be

Table 3 Paired two-sided DeLong tests for comparison among AUROCs of Bayesian case detectors with different combinations of finding-extraction method and Bayesian network (BN) classifier


Primary analyses: BN classifiers using 31 influenza-related findings


Each combination of finding-extraction method and BN classifier is represented as a lower case letter plus a upper case letter. The lower case letters are abbreviations of finding-extraction methods: e, expert findings; t, Topaz findings; m, MedLEE findings. The upper case letters are abbreviations of BN classifiers: E, expert-defined BN; T, BN-EM-Topaz; M, BN-EM-MedLEE.
Each p value was calculated with a DeLong two-sided comparison of AUROC. The * $p<0.05$.
The 17 influential findings indicated in BN-EM-Topaz were arthralgia, cervical lymphadenopathy, chill, cough, fever, hoarseness, influenza-like illness, lab confirmed influenza lab order (nasal swab), malaise, myalgia, rhinorrhea, sore throat, suspected flu, viral infection, viral syndrome, and wheezing.
AUROC, area under the receiver operating characteristic.

Figure $3 \log _{10} \mathrm{LR}^{+}$(likelihood ratios) of features in expert-defined BN, BN-EM-Topaz, and BN-EM-MedLEE.
![img-2.jpeg](img-2.jpeg)
biased because of the post-processes mentioned in the method section (ie, applying Topaz's heuristic resolution rules and mapping some UMLS CUIs to influenza-related findings).

Both primary and secondary analyses suggested that all three classifiers achieved greater discrimination when combined with expert findings, followed by Topaz findings, then MedLEE findings. This correlation was present even when there was a mismatch between NLP parser and BN classifier. These results suggested the importance of finding-extraction accuracy for influenza detection and encouraged the use of the highest performing NLP system available regardless of the NLP system used to train the classifier.

## Effects of classifier on classification performance

Usually, it is not easy for an expert to accurately quantify the correlations between findings and the disease, and using an NLP parser as finding-extraction method could further complicate the situation. In this study, the machine-learned classifiers were shown to have better discriminative abilities than the expertdefined classifier across all finding-extraction methods, indicating the benefit of turning data into knowledge. Starting the machine learning process from BN classifiers that are initially
parameterized by experts, the EM-MAP algorithm is especially useful when the occurrences of certain findings are rare.

## Effects of feature selection on classification performance

In this study, feature selection based on likelihood ratio values that were calculated with CPTs in a machine-learned BN classifier significantly improved the performance of influenza detection, suggesting that feature selection could be an efficient way to improve classification performance.

## Limitations

Although the research has reached its aims, one major limitation is the use of a non-representative sample of non-influenza (shigellosis) controls in the testing dataset. This decision was pragmatic as we did not have the resources to develop additional expert-annotated ED charts. In addition, our use of PCR tests as a gold standard may have biased the testing set with positive cases that are more severe symptomatically and thus easier to distinguish than average influenza cases in EDs. Therefore, the AUROC in the range $0.64-0.82$ should not be taken as an indication of the performance of influenza detection that we would

Figure $4 \log _{10} \mathrm{LR}^{-}$(likelihood ratios) of features in expert-defined BN, BN-EM-Topaz, and BN-EM-MedLEE.
![img-3.jpeg](img-3.jpeg)
expect in an operational ED setting; further evaluation with a randomly selected testing dataset would be more informative.

## Significance

Influenza detection is important in both clinical care and public health practice. Automatic influenza detection from EHR data still depends on the ability to extract symptoms and signs from unstructured data. The present paper described a systematic approach for evaluating the relative contributions of the components in a process of extracting symptoms and signs, feature selection, and classification for the disease influenza. Although using a biased control may limit the interpretation of the results of the present study, the three-component evaluation could be applied more generally to a broader problem of detection of any disease phenotype that involves clinical information that is stored in free-text reports.

## CONCLUSION

Using a three-component evaluation method we demonstrated how one could elucidate the relative contributions of components under an integrated framework. To improve classification performance, this study encourages researchers to improve NLP
accuracy, use a machine-parameterized classifier incorporating both expert knowledge and data patterns, and apply feature selection methods. This study addresses the concern of using one NLP system to train a classifier and another NLP system in production-using the highest performing NLP system available regardless of the NLP system used to train the classifier is advised.

Acknowledgements The authors wish to thank Drs John Dowling, Paul Thyvalikakath, and Tatiana Bogdanovich for annotating the reports used in our study. We acknowledge Dr Wendy Chapman, David Chu, Dr Henk Harkema, and Lee Christiansen for developing Topaz software when they worked in the RODS laboratory. We acknowledge Dr Carol Friedman for providing MedLEE software that is partly supported by Grants R01 LM010016 and R01 LM008635 from the National Library of Medicine. We would like to thank Howard Su for medical record retrieval and de-identification, Dr Gregory F Cooper and Dr Shyam Visweswaran for their helpful discussions, and Kevin Bui for his programming skills.
Contributors YY and FT analyzed data, drafted the article, and took the responsibility for accuracy of data analysis and result formatting. MW and JUE brought insight into study design, data analysis and interpretation, and went through many drafts and revisions. QL did annotator training and gathered the expert findings for shigellosis reports.
Funding This work is supported in part by Grants P01-HK000086 and U38HK000063 from the Centers for Disease Control and Prevention, Grant SAP

\#40000012020 from the Pennsylvania Department of Health, and Grant R01LM011370-01A1 from the National Library of Medicine.
Competing interests None.
Ethics approval University of Pittsburgh.
Provenance and peer review Not commissioned; externally peer reviewed.
