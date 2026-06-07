# communications 

## medicine

## Genetic and clinical variables act synergistically to impact neurodevelopmental outcomes in children with single ventricle heart disease

Thomas A. Miller ${ }^{1,19 \boxtimes}$, Edgar J. Hernandez ${ }^{2,19}$, J. William Gaynor ${ }^{3}$, Mark W. Russell ${ }^{4}$, Jane W. Newburger ${ }^{5}$, Wendy Chung ${ }^{6}$, Elizabeth Goldmuntz ${ }^{7}$, James F. Cnota ${ }^{8}$, Sinai C. Zyblewski ${ }^{9}$, William T. Mahle ${ }^{10}$, Victor Zak ${ }^{11}$, Chitra Ravishankar ${ }^{7}$, Jonathan R. Kaltman ${ }^{12}$, Brian W. McCrindle ${ }^{13}$, Shanelle Clarke ${ }^{14}$, Jodie K. Votava-Smith ${ }^{15}$, Eric M. Graham ${ }^{9}$, Mike Seed ${ }^{13}$, Nancy Rudd ${ }^{16}$, Daniel Bernstein ${ }^{17}$, Teresa M. Lee ${ }^{6}$, Mark Yandell ${ }^{2 \boxtimes}$ \& Martin Tristani-Firouzi@ ${ }^{18 \boxtimes}$

## Abstract

Background Recent large-scale sequencing efforts have shed light on the genetic contribution to the etiology of congenital heart defects (CHD); however, the relative impact of genetics on clinical outcomes remains less understood. Outcomes analyses using genetics are complicated by the intrinsic severity of the CHD lesion and interactions with conditionally dependent clinical variables.
Methods Bayesian Networks were applied to describe the intertwined relationships between clinical variables, demography, and genetics in a cohort of children with single ventricle CHD.
Results As isolated variables, a damaging genetic variant in a gene related to abnormal heart morphology and prolonged ventilator support following stage I palliative surgery increase the probability of having a low Mental Developmental Index (MDI) score at 14 months of age by 1.9- and 5.8-fold, respectively. However, in combination, these variables act synergistically to further increase the probability of a low MDI score by 10 -fold. The absence of a damaging variant in a known syndromic CHD gene and a shorter post-operative ventilator support increase the probability of a normal MDI score 1.7- and 2.4-fold, respectively, but in combination increase the probability of a good outcome by 59-fold.
Conclusions Our analyses suggest a modest genetic contribution to neurodevelopmental outcomes as isolated variables, similar to known clinical predictors. By contrast, genetic, demographic, and clinical variables interact synergistically to markedly impact clinical outcomes. These findings underscore the importance of capturing and quantifying the impact of damaging genomic variants in the context of multiple, conditionally dependent variables, such as pre- and post-operative factors, and demography.

## Plain Language Summary

Single ventricle congenital heart disease is a birth defect. In these children, the heart has only one effective blood-pumping chamber instead of two. Surgery can reroute the blood to use only one chamber, but multiple risk factors influence how well a child develops afterwards. Studying these risk factors can be challenging because they are interconnected, i.e. children with a genetic birth defect may be more likely to have a lower birthweight, and hence more likely to spend longer in hospital after surgery. Here, we used a statistical approach not commonly applied to study congenital heart disease and describe that whether a genetic variant (a small difference in a child's DNA) is important for how a child with single ventricle heart disease develops and grows after surgery depends on the presence of other risk factors.

While survival for infants with single ventricle congenital heart disease (SV-CHD) has improved dramatically, significant healthcare utilization, morbidity, and mortality persist ${ }^{1}$. Despite improvements in standardized care, neurodevelopmental and growth outcomes vary substantially in children with SV-CHD ${ }^{2}$. Identifiable syndromes and chromosomal abnormalities are associated with worse outcomes for multiple forms of complex $\mathrm{CHD}^{3-6}$. Predicted damaging genetic variants in genes related to CHD may contribute to poor outcomes, irrespective of whether the patient has syndromic CHD. Outside of aneuploidy and other known syndromes, the genetic architecture of CHD includes high-impact, rare variants across many loci. Thus, many variants that contribute to CHD have a small population-attributable risk (PAR) ${ }^{7,8}$. This low PAR makes determination of the association of variants with outcomes difficult, especially when studying relatively small numbers of individuals with SV-CHD. As a result, the relative contribution of genomic variation to neurodevelopment and growth outcomes remains poorly described, especially in the context of clinical variables and other comorbidities, which can combine with one another in a conditionally dependent manner to create a constellation of influence on any given outcome ${ }^{9}$. Two clinical variables are conditionally dependent if the probability of encountering both variables is not equal to the multiplication of their individual probabilities. For example, sex and bicuspid aortic valve (BAV) are conditionally-dependent, in that the probability of encountering an individual with bicuspid aortic valve is greater for males versus females ${ }^{10}$.

We recently reported the conditionally dependent relationships between genotypes, gene functions, and phenotypes in a large CHD cohort using Bayesian Networks, an Artificial Intelligence (AI) solution ${ }^{8}$. Compared to traditional regression models, Bayesian Networks offer many advantages to risk prediction, as a single network can be used to evaluate multiple outcomes based upon any combination of variables or exposures ${ }^{11,12}$. Moreover, Bayesian Networks provide improved means to quantify the synergistic impacts of demographic, clinical, and genomic variables. In this context, we apply Bayesian Networks in an exploratory, proof-ofprinciple analysis to explore the landscape of damaging genotypes on neurodevelopmental and linear growth outcomes in the Pediatric Heart Network's (PHN) Single Ventricle Reconstruction (SVR) trial and Infant Single Ventricle (ISV) trial participants.

## Methods

Study population. Participants in the PHN's SVR and ISV trials who had blood or saliva collected for DNA extraction were included in this study. The original study design, descriptive characterization of the cohort, and primary results of the SVR (NCT00115934) and the ISV (NCT 00113087) trials have previously been published ${ }^{13-17}$. Both trials excluded participants with known chromosomal abnormalities or syndromic features at the time of enrollment. Institutional Review Boards for all centers participating in the SVR and ISV trials gave ethical approval for the human subjects research in this work and written informed consent was obtained. Data Use Agreements between the PHN and the Pediatric Cardiac Genomics Consortium (PCGC) allowed for the de-identified sharing of genetic and limited clinical data between the two consortia. All SVR and ISV participants who had whole exome sequencing (WES) and neurodevelopmental followup at 14 months of age were included in this cohort. Sub analyses were performed on those who had complete matching clinical and demographic variables.

Clinical outcomes and covariates. Outcomes included the Bayley Scales of Infant Development (BSID-II) and length measurement
(length for age z-score, LAZ) for both the SVR and ISV trials at 14 months of age. BSID-II subdomain scores included the Psychomotor Developmental Index (PDI) and Mental Developmental Index (MDI), wherein the standardized mean scores are 100. While it is true that MDI and PDI are assessed at the same time, we consider these variables within the Bayesian Networks as both outcomes and risk factors, in order to highlight the ability of our approach to capture and quantify synergistic (non-additive) relationships between variables under study. An advantage of our approach is that the use of a Bayesian network allows us to employ a single model to explore the impact of highly correlated variables singly or jointly, as outcomes and as risk factors to generate the results shown here. Additional pre- and postoperative clinical and demographic variables were available for a subset of 179 SVR participants, including birthweight, duration of mechanical ventilation following the Stage I palliation surgery, gestational age, and US census socioeconomic scores.

In order to optimally discretize continuous variables, we used a grid search to evaluate the performance of the nascent Bayesian Network, using receiver operating characteristic (ROC) curves (Supplementary Figure 1). For each value of MDI, PDI, and LAZ, we calculated the joint conditional probability of an individual having low MDI, PDI, or LAZ given the presence or absence of other conditions (variables) for each individual in the cohort given its intrinsic values at each condition. These conditional probability distributions were used to evaluate the accuracy of each candidate network to classify an individual as low or high MDI, PDI, or LAZ score, allowing us to select the optimal score resulting from the highest area under the ROC (AUC). This approach discovered that a score of 70 for both MDI and PDI resulted in an optimal AUC score ( 0.97 for PDI and 0.88 for MDI). A score of 70 corresponds to 2 standard deviations below the mean, consistent with clinical intuition for a desirable cut-off. The optimal value for LAZ score using this approach was -1.6 ( $\mathrm{AUC}=0.72$ ). When considering a favorable outcome, we used a threshold of $>100$ for MDI and PDI, and $>0$ for LAZ. The preand post-operative clinical and demographic variables in the smaller subset of 179 SVR participants were less amenable to optimization using this approach. Therefore, we used previously published cutoffs for dichotomization previously associated with outcomes in this population ${ }^{18,19}$ as follows: birthweight ( $<2500$ gram, low), ventilation following the Stage I palliation surgery ( $>7$ days, prolonged), gestational age ( $<37$ weeks, preterm), and US census socioeconomic score (SES, low score $<-0.3$, Range -11.5 to 17.9 ).

Variant annotation. Raw sequencing data in the form of fastq files (Illumina 101 bp paired-end reads) for each individual were aligned to the human genome reference sequence (GRCh37/hg19, downloaded from http://genome.ucsc.edu) using the BurrowsWheeler Alignment (BWA) Tool and the MEM algorithm (http:// bio-bwa.sourceforge.net/bwa.shtml\#13). Variants were called using the best practice protocol of the Genome Analysis Toolkit (GA2X) pipeline (http://www.broadinstitute.org/gatk/guide/best-practices). All exomes were jointly-genotyped together with $\sim 190$ European individuals (CEU, GBR) from the 1000 Genomes Project. This was followed by Variant Quality Score Recalibration (VQSR), which uses known, high-quality variant sites from HapMap3 and 1000 Genomes to identify and filter potential false positive variant calls. Both variant calling and VQSR were performed separately on INDELs and single nucleotide variants (SNVs). Tranche values were set to 99.5 and 99.0 for SNPs and INDELs, respectively. Variant consequences and annotations were obtained with VEP v. 95 (uswest.ensembl.org/info/docs/tools/vep/script/ vep_download.html) utilizing ENSEMBL transcripts version 95

(excluding non-coding transcripts) and selecting the canonical transcript for analysis. Transcript-specific prediction for evaluating variant deleteriousness was calculated with VVP^{20}, which were also used as input for VAAST (VVP and VAAST: [github.com/Yandell-Lab/VVP-pub])^{21}. Variants were annotated with ClinVar (20200419) ensuring exact position and base match. Gene-conditions were extracted from the Online Mendelian Inheritance in Man (OMIM) catalog (2020_07)^{22} and the Human Phenotype Ontology (HPO) database (obo file, 2020-08-11)^{23}. Gene symbols were harmonized using ENSEMBL and HGNC databases controlling for synonymous gene symbols.

## AI-based scoring of damaging genetic variants

AI-based prioritization and scoring of candidate disease genes and diagnostic conditions were performed using GEM^{24} in the commercially available Fabric Enterprise platform (Fabric Genomics, Oakland, CA; fabricgenomics.com/fabric-gem). GEM inputs are genetic variant calls in VCF format and proband phenotypes in the form of HPO terms. GEM aggregates inputs from multiple variant prioritization algorithms (e.g. VAAST and VVP) with genomic and clinical database annotations, using Bayesian means to score and prioritize potentially damaged genes and candidate diseases. The prior probability for the model is based upon known disease associations in the Mendelian conditions databases OMIM and/or HPO with the gene in question. In order to capture a broad category of genes related to heart development, we selected the HPO term Abnormal Heart Morphology (HP:0001627).

GEM's gene scores are Bayes Factors^{25}, representing the log_{10} ratio between the posterior probabilities of two models, summarizing the relative support for the hypothesis that the prioritized genotype damages the gene in which it resides and explains the proband's phenotype versus the hypothesis that the variant neither damages the gene nor explains the proband's phenotype. We used a Bayes factor of ≥0.69 to represent a likely deleterious genetic variant, based on a recent retrospective analysis of critically ill newborns whereby a Bayes factor threshold ≥0.69 successfully achieved a diagnostic rate of 95% for cases solved using a standard clinical diagnostic approach^{24}. Each variant that passed the 0.69 threshold was evaluated using the graph-based adjudication tool Graphite, which constructs a variant graph that permits the exclusion of false positives due to errors in variant calling (github.com/dillonl/graphite)^{8}. Gene penetrance for GEM calculations was set to 0.95 to enforce strict consideration of known dominant and recessive disorders.

## Bayesian Network analyses

Bayesian Network structure was learned using the R package “bnstruct”^{26} which provides a Bayesian Information Criterion (BIC)-based exact structure search algorithm ([www.r-project.org] (bnlearn, gRain, bnstruct libraries, pROC package))^{27}. The exact search algorithm explores the entire applicable space of conditional dependencies in order to discover the optimal network structure for the data. Parameter learning for this optimal network and multimorbidity risk calculations were accomplished using the loopy belief propagation algorithm from the R gRain package^{28}. The conditional dependencies in the dataset are presented as a directed acyclic graph. Risk estimates derived from Bayesian Networks are maximum likelihood estimates given the optimal structure under the BIC and uniform prior probability. Relative risk was calculated in the following manner: Probability (A=True | B=True, C=True)/Probability (A=True | B=False, C=False). Confidence intervals (CI, ± 95%) for the mean values for these estimates were obtained by creating 1000 nets from bootstrap replicates of the same data.

## Statistical approach

Differences in testing scores (MDI and PDI) and LAZ for those with and without damaging genetic variants in various gene categories were assessed using independent nonparametric Mann-Whitney U Test, correcting for multiple comparisons using a Bonferroni correction.

## Results

Of the original 555 SVR and 230 ISV trial enrollees, survival rates have been previously published (69% and 86%, respectively)^{15,17}. Of those that underwent WES, there were 21 individuals who were enrolled in both SVR and ISV trials. For this study, a total of 304 participants underwent WES, neurodevelopmental assessment, and length measurement at 14 months of age and form the primary study cohort. Patient-parent trio WES was available for 86 participants. Additionally, the selected pre- and post-operative clinical and demographic variables were available for a subset of 179 SVR participants. Distribution of sex, race, ethnicity, cardiac anatomy, gestational age, and birthweight were similar across the various cohorts (Supplementary Table 1). The distribution of neurodevelopmental and growth scores for the cohort undergoing WES (Fig. 1) was similar to that previously reported for the original cohorts and underscore the highly affected nature of these patients^{17,18}.

A potentially damaging genetic variant in a gene related to “Abnormal Heart Morphology” was identified in 137 participants (44% of the study cohort), each harboring a mean of 1.8 damaging variants/proband (range 1--6; Supplementary Data 1). Mean MDI, PDI and LAZ scores were not statistically different between participants with and without a damaging genetic variant in this gene list (Fig. 2a). Forty-four subjects (14%) harbored one or more damaging genetic variants in a subset of the gene list that is associated with syndromic forms of CHD (as defined by OMIM), including autosomal dominant (N = 41), X-linked recessive (N = 4), X-linked dominant (N = 1) and autosomal recessive (N = 1) inheritance modes (Table 1). Eight of these subjects carried variants classified by ClinVar as pathogenic or likely pathogenic. The most commonly damaged genes in the cardiac syndromic subset gene list included KMT2D (N = 5, Kabuki Syndrome), NOTCH1 (N = 4, Aortic Valve Disease 1), ANKRD11 (N = 3 KBG Syndrome), MED12 (N = 2, Opitz-Kaveggia Syndrome), SHANK3 (N = 2, Phelan-Mcdermid Syndrome), and SRCAP (N = 2, Floating-Harbor Syndrome). While there was a trend toward lower MDI and PDI scores for participants with versus without a damaging variant in the syndromic CHD gene list, the differences were not significant after correction for multiple testing (Fig. 2b). We also examined damaging de novo genetic variants in the subset of participants with trio WES data (N = 86). A damaging de novo genetic variant in the HPO-term derived gene list was identified in 10 probands, representing 12% of the cohort with trio WES data (Supplementary Table 2). The small number of de novo variants precluded statistical evaluation.

Next, we sought to investigate the conditional probability of particular outcomes, in the context of genetic, demographic and clinical variables, using Bayesian Networks. The Bayesian Network describing the landscape of genetic, neurodevelopmental, growth, and demographic variables in our cohort of SV-CHD (Fig. 3a) allows for a multitude of queries that support a robust investigation of multiple interactions between conditionally dependent variables. For example, querying the net reveals that a damaging variant in a gene related to abnormal heart morphology increased the risk of a low MDI score by 1.38-fold (1.37 CI-5%, 1.40 CI-95%, N = 1000 bootstrap iterations; Fig. 3b and Supplementary Table 2). Of the variables under consideration, a low PDI score was the strongest single risk factor for a low MDI score (21.2-fold increase). While female sex was associated with a

![img-0.jpeg](img-0.jpeg)

**Fig. 1 Outcomes Distribution for the study cohort.** Outcome distributions of the (**a**) Mental Developmental Index (MDI), (**b**) Psychomotor Developmental Index (PDI), and (**c**) length for age z-score (LAZ) for the study cohort. Red color denotes values below the optimally derived lower cut-off value (MDI, 70; PDI, 70; LAZ, −1.6) and blue those above the respective cut-off. See Methods for details. *N* = 309 subjects.

1.77-fold increased risk of a low MDI score in isolation, when combined with a low PDI score, the risk of a low MDI was further increased 75.8-fold. These results highlight the ability of Bayesian networks to quantify synergistic effects of variables in combination on an outcome of interest.

The contribution of genetics to PDI score was most impactful when considering predictors of a favorable PDI outcome (Supplementary Table 3 and Supplementary Fig. 2). Thus, a participant *without* a damaging variant in a syndromic CHD gene was 4-times more likely to have a normal PDI score (defined as >100). When combined with normal linear growth (LAZ > 0) and MDI (> 100) scores, the absence of a damaging CHD syndromic genetic variant increased the probability of a normal PDI score by 16.5-fold.

![img-1.jpeg](img-1.jpeg)

**Fig. 2 Neurodevelopmental and growth outcomes based on presence of a damaging genetic variant: distribution of Psychomotor Developmental Index (PDI), Mental Developmental Index (MDI), and length for age z-score (LAZ) for those individuals with and without a damaging genetic variant, defined by GEM Bayes Factor ≥0.69. a** Box plots of MDI, PDI and LAZ scores in participants with (+) and without (−) a damaging variant in a gene related to the HPO term "Abnormal Heart Morphology"; *N* = 167 participants without damaging genotype, *N* = 137 participants with damaging genotype. None of the comparisons achieved statistical significance after corrections for multiple testing: *p* = 0.94, MDI; *p* = 0.14, PDI; *p* = 0.94, LAZ. **b** Box plots of MDI, PDI and LAZ scores in participants with a damaging genotype in a known syndromic CHD gene (*N* = 38) and without (*N* = 167). Center horizontal line, mean value; box, 1 standard deviation; whiskers, 5 and 95th percentiles. None of the comparisons achieved statistical significance after corrections for multiple testing: *p* = 0.68, MDI; *p* = 0.15, PDI; *p* = 0.08, LAZ.

Genetic information modestly impacted poor linear growth, with a damaging variant in a gene related to abnormal heart morphology or a syndromic CHD gene increasing the probability of a low LAZ score by 1.12- and 1.34-fold, respectively (Supplementary Table 3). Additionally, demographic and clinical variables interacted synergistically to increase the probability of a low LAZ score. For example, as isolated variables female sex and low MDI score increased the likelihood of a low LAZ score 1.19-fold and 2.13-fold, respectively. However, in combination, female sex and low MDI further increased the probability of a low LAZ score 6.4-fold.

Next, we sought to determine the impact of pre- and post-operative clinical variables, demographic variables such as SES and sex, and genetics both individually and in combination on neurodevelopmental and linear growth outcomes in a subset of 179 participants for whom complete variables were available. A network describing the landscape of clinical, genetic, demographic, length, and neurodevelopmental variable dependencies is depicted in Fig. 4. Data elements for this network include premature birth, birthweight, mechanical ventilation duration following the 1st stage palliation surgery and SES. Similar to the larger cohort, we were underpowered to detect the impact of a

Table 1 Number of probands harboring a damaging variant in a syndromic CHD gene


The genetic signal for poor linear growth was smaller in this cohort, in part due to loss of power in the smaller dataset. The strongest single variable contributing to poor linear growth was a low a SES score, increasing the probability of a low LAZ score by 2.13 -fold (Fig. 4 and Supplementary Table 4). When combined with female sex and a low PDI score, a low SES score increased the probability of a low LAZ score by 7.78 -fold.

## Discussion

Exploring heterogeneity in outcomes following surgery for complex CHD necessitates models capable of quantifying the complex relationships between clinical variables and genetics, and their combined impacts on divergent outcomes. This is because clinical variables often combine with each other in a conditionallydependent manner to impact the probability of any given outcome ${ }^{9}$. Here, we apply AI methodologies as a proof-ofprinciple study of the impact of genetics on neurodevelopmental and linear growth in SV-CHD, using AI-based prioritization of damaging genetic variants and a Bayesian Network approach. Our analyses suggest a modest genetic contribution to neurodevelopmental outcomes as isolated variables, similar to known clinical predictors. By contrast, we discovered that genetic, demographic, and clinical variables interact synergistically to

![img-2.jpeg](img-2.jpeg)

**Fig. 3 Network describing the conditional dependencies among the genetic, demographic and selected clinical variables in a cohort of children with single ventricle CHD. a** Best-fit network for the variables under study. Edges between nodes indicate conditional dependencies. dGV, damaging genetic variant in genes associated with HPO term "Abnormal Heart Morphology". SYNDR, damaging genetic variant in genes associated with syndromic CHD, defined by OMIM. LAZ, length for age Z-score. N = 309 participants. **b-d** Forest plots showing relative risk ratios for low MDI (≤70), PDI (≤70), and LAZ (≤−1.6) scores in the context of the displayed clinical variables alone or in combination. Solid black line denotes 5 and 95% confidence intervals. If not visible, confidence intervals are within the symbol.

markedly impact clinical outcomes. These findings highlight the importance of evaluating genetic data in the context of clinical variables, and the need to employ approaches to capture synergistic relationships between them.

Our analyses reveal a modest genetic contribution to poor neurodevelopmental outcomes in probands harboring a damaging variant in abnormal heart morphology genes versus syndromic CHD genes. In the context of predicting a favorable outcome, absence of a damaging variant in the syndromic CHD gene list was more impactful. Although individuals with known syndromic disorders were excluded from enrollment in the SVR and ISV trials, we found that 14% of the SV-CHD cohort harbored a damaging genetic variant in a gene known to cause syndromic CHD, including *KMT2D*, *NOTCH1*, and *ANKRD11* as the most common recurring damaged genes. Similar to this cohort, the PCGC also reported a higher-than-expected number of participants with damaging genotypes in syndromic genes, despite a known genetic syndrome as an exclusion criterion[^7]. The inherent variable expressivity of cardiac syndromic disorders and/or potential challenges in identifying syndromic features in infancy may, in part, explain these findings. Importantly, our estimates of the impacts of damaging genotypes in syndromic genes (or their absence) are underestimated by the initial exclusion of known syndromic patients. The power of this Bayesian approach is that we can tease apart the contribution of syndromic genes (or other gene classes) to clinical outcomes and thereby predict risk across all patients.

An advantage of Bayesian Networks is the ability to capture and quantify the joint contributions of multiple conditionally dependent variables, all within a single probabilistic graphical model. Traditional techniques, such as regression analyses, have limited ability to capture the conditional dependencies between clinical variables. While mixture and generalized linear models can overcome these weaknesses, they require the design of a new model to address each individual question. Neural nets, while capable of capturing conditional dependencies, lack explainability in that the contributions of different variables on a given output are often unclear. By contrast, Bayesian Networks provide an explainable AI solution[^29].

Our Bayesian Network approach allowed us to start to describe the landscape of clinical, genetic and demographic variables in children with SV-CHD, capturing and quantifying the impacts of

[^7]: Reference for the model described in the text.
[^8]: Reference for the model described in the text.

![img-3.jpeg](img-3.jpeg)

Fig. 4 Network describing the conditional dependencies among pre- and post-operative clinical variables, genetics and demographic features in children with single ventricle CHD. a Best-fit network for the variables under study. Edges between nodes indicate conditional dependencies. BWT birth weight (<2500 grams, low BWT), VENT mechanical ventilator duration after 1st stage single ventricle palliation (>7 days, prolonged VENT), preterm preterm birth (<37 weeks gestation), SES socioeconomic status score; N = 179 participants. b–d Forest plots showing relative risk ratios for low MDI (≤70), PDI (≤70), and LAZ (≤−1.6) scores in the context of the displayed clinical variables alone or in combination. Solid black line denotes 5 and 95% confidence intervals. If not visible, confidence intervals are within the symbol.

synergistic relationships between these variables and outcomes of interest. Genetic variables interacted synergistically with duration of post-operative mechanical ventilation to increase the probability of a poor or favorable MDI score by 10- and 59-fold, respectively. Likewise, genetic variables interacted synergistically with SES to increase the likelihood of a favorable PDI score by 53-fold. Our analyses here were limited to the relatively small number of individuals with complete clinical variables; precluding further exploration of the impact of a damaging genetic variant on pre- and post-operative variables, as well as SES. Expanding the analysis to the wider range of clinical variables associated with this well-phenotyped cohort and increasing the number of genotyped probands will provide greater insight into the genetic contribution to clinical outcomes in SV-CHD. In a broader sense, the current work supplements our efforts using Bayesian Networks as an explainable AI solution for understanding the joint impacts of diagnoses, medications, and medical procedures on cardiovascular health outcomes[^9].

There are several limitations inherent to this study. For example, DNA collection was not a requirement for participation and thus, sample procurement was inconsistent across the cohort. Moreover, DNA samples were not obtained at enrollment, but rather at subsequent time points in these longitudinally followed cohorts, thereby introducing survival bias. Some DNA samples were collected at a few years of age which would have been well after the 14-month clinical endpoints included in these analyses. Thus, patients who died early may have harbored highly damaging genotypes that are not accounted for in this cohort of infants that survived at least until the 14-month endpoint. The later DNA analysis also highlights the limitations of the original exclusion criteria, as some individuals in SVR were later found (during enrollment in SVR extension studies) to have syndromes, such as Kabuki Syndrome, consistent with our variant analysis. Additionally, we recognize the relatively small sample size of patients limited the ability to include all potential peri-operative, clinical, and socio-economic predictors of outcomes in this proof-of-principal analysis. Future efforts by the PHN consortium to sequence more patients with rich clinical datasets as well as by the PCGC to obtain richer clinical data on their sequenced patients, will allow for more robust analyses of the genetic contribution to clinical outcomes in children with complex forms of CHD. The definition of a "damaging" genetic variant is a topic of intense

[^9]: Reference 9
[^10]: Reference 10
[^11]: Reference 11
[^12]: Reference 12
[^13]: Reference 13
[^14]: Reference 14
[^15]: Reference 15
[^16]: Reference 16
[^17]: Reference 17
[^18]: Reference 18
[^19]: Reference 19
[^20]: Reference 20
[^21]: Reference 21
[^22]: Reference 22
[^23]: Reference 23
[^24]: Reference 24
[^25]: Reference 25
[^26]: Reference 26
[^27]: Reference 27
[^28]: Reference 28
[^29]: Reference 29
[^30]: Reference 30
[^31]: Reference 31
[^32]: Reference 32
[^33]: Reference 33
[^34]: Reference 34
[^35]: Reference 35
[^36]: Reference 36
[^37]: Reference 37
[^38]: Reference 38
[^39]: Reference 39
[^40]: Reference 40
[^41]: Reference 41
[^42]: Reference 42
[^43]: Reference 43
[^44]: Reference 44
[^45]: Reference 45
[^46]: Reference 46
[^47]: Reference 47
[^48]: Reference 48
[^49]: Reference 49
[^50]: Reference 50
[^51]: Reference 51
[^52]: Reference 52
[^53]: Reference 53
[^54]: Reference 54
[^55]: Reference 55
[^56]: Reference 56
[^57]: Reference 57
[^58]: Reference 58
[^59]: Reference 59
[^60]: Reference 60
[^61]: Reference 61
[^62]: Reference 62
[^63]: Reference 63
[^64]: Reference 64
[^65]: Reference 65
[^66]: Reference 66
[^67]: Reference 67
[^68]: Reference 68
[^69]: Reference 69
[^70]: Reference 70
[^71]: Reference 71
[^72]: Reference 72
[^73]: Reference 73
[^74]: Reference 74
[^75]: Reference 75
[^76]: Reference 76
[^77]: Reference 77
[^78]: Reference 78
[^79]: Reference 79
[^80]: Reference 80
[^81]: Reference 81
[^82]: Reference 82
[^83]: Reference 83
[^84]: Reference 84
[^85]: Reference 85
[^86]: Reference 86
[^87]: Reference 87
[^88]: Reference 88
[^89]: Reference 89
[^90]: Reference 90
[^91]: Reference 91
[^92]: Reference 92
[^93]: Reference 93
[^94]: Reference 94
[^95]: Reference 95
[^96]: Reference 96
[^97]: Reference 97
[^98]: Reference 98
[^99]: Reference 99
[^100]: Reference 100
[^101]: Reference 101
[^102]: Reference 102
[^103]: Reference 103
[^104]: Reference 104
[^105]: Reference 105
[^106]: Reference 106
[^107]: Reference 107
[^108]: Reference 108
[^109]: Reference 109
[^110]: Reference 110
[^111]: Reference 111
[^112]: Reference 112
[^113]: Reference 113
[^114]: Reference 114
[^115]: Reference 115
[^116]: Reference 116
[^117]: Reference 117
[^118]: Reference 118
[^119]: Reference 119
[^120]: Reference 120
[^121]: Reference 121
[^122]: Reference 122
[^123]: Reference 123
[^124]: Reference 124
[^125]: Reference 125
[^126]: Reference 126
[^127]: Reference 127
[^128]: Reference 128
[^129]: Reference 129
[^130]: Reference 130
[^131]: Reference 131
[^132]: Reference 132
[^133]: Reference 133
[^134]: Reference 134
[^135]: Reference 135
[^136]: Reference 136
[^137]: Reference 137
[^138]: Reference 138
[^139]: Reference 139
[^140]: Reference 140
[^141]: Reference 141
[^142]: Reference 142
[^143]: Reference 143
[^144]: Reference 144
[^145]: Reference 145
[^146]: Reference 146
[^147]: Reference 147
[^148]: Reference 148
[^149]: Reference 149
[^150]: Reference 150
[^151]: Reference 151
[^152]: Reference 152
[^153]: Reference 153
[^154]: Reference 154
[^155]: Reference 155
[^156]: Reference 156
[^157]: Reference 157
[^158]: Reference 158
[^159]: Reference 159
[^160]: Reference 160
[^161]: Reference 161
[^162]: Reference 162
[^163]: Reference 163
[^164]: Reference 164
[^165]: Reference 165
[^166]: Reference 166
[^167]: Reference 167
[^168]: Reference 168
[^169]: Reference 169
[^170]: Reference 170
[^171]: Reference 171
[^172]: Reference 172
[^173]: Reference 173
[^174]: Reference 174
[^175]: Reference 175
[^176]: Reference 176
[^177]: Reference 177
[^178]: Reference 178
[^179]: Reference 179
[^180]: Reference 180
[^181]: Reference 181
[^182]: Reference 182
[^183]: Reference 183
[^184]: Reference 184
[^185]: Reference 185
[^186]: Reference 186
[^187]: Reference 187
[^188]: Reference 188
[^189]: Reference 189
[^190]: Reference 190
[^191]: Reference 191
[^192]: Reference 192
[^193]: Reference 193
[^194]: Reference 194
[^195]: Reference 195
[^196]: Reference 196
[^197]: Reference 197
[^198]: Reference 198
[^199]: Reference 199
[^200]: Reference 200
[^201]: Reference 201
[^202]: Reference 202
[^203]: Reference 203
[^204]: Reference 204
[^205]: Reference 205
[^206]: Reference 206
[^207]: Reference 207
[^208]: Reference 208
[^209]: Reference 209
[^210]: Reference 210
[^211]: Reference 211
[^212]: Reference 212
[^213]: Reference 213
[^214]: Reference 214
[^215]: Reference 215
[^216]: Reference 216
[^217]: Reference 217
[^218]: Reference 218
[^219]: Reference 219
[^220]: Reference 220
[^221]: Reference 221
[^222]: Reference 222
[^223]: Reference 223
[^224]: Reference 224
[^225]: Reference 225
[^226]: Reference 226
[^227]: Reference 227
[^228]: Reference 228
[^229]: Reference 229
[^230]: Reference 230
[^231]: Reference 231
[^232]: Reference 232
[^233]: Reference 233
[^234]: Reference 234
[^235]: Reference 235
[^236]: Reference 237
[^237]: Reference 238
[^238]: Reference 239
[^239]: Reference 239
[^240]: Reference 241
[^241]: Reference 242
[^242]: Reference 243
[^243]: Reference 244
[^244]: Reference 245
[^245]: Reference 246
[^246]: Reference 247
[^247]: Reference 248
[^248]: Reference 249
[^249]: Reference 250
[^250]: Reference 251
[^251]: Reference 252
[^252]: Reference 253
[^253]: Reference 254
[^254]: Reference 255
[^255]: Reference 256
[^256]: Reference 257
[^257]: Reference 258
[^258]: Reference 259
[^259]: Reference 260
[^260]: Reference 261
[^261]: Reference 262
[^262]: Reference 263
[^263]: Reference 264
[^264]: Reference 265
[^265]: Reference 266
[^266]: Reference 267
[^267]: Reference 268
[^268]: Reference 269
[^269]: Reference 270
[^270]: Reference 271
[^271]: Reference 272
[^272]: Reference 273
[^273]: Reference 274
[^274]: Reference 275
[^275]: Reference 276
[^276]: Reference 277
[^277]: Reference 278
[^278]: Reference 279
[^279]: Reference 279
[^280]: Reference 281
[^282]: Reference 282
[^283]: Reference 283
[^284]: Reference 285
[^285]: Reference 286
[^286]: Reference 287
[^287]: Reference 288
[^288]: Reference 289
[^289]: Reference 289
[^290]: Reference 290
[^291]: Reference 291
[^292]: Reference 292
[^293]: Reference 294
[^294]: Reference 295
[^295]: Reference 296
[^296]: Reference 297
[^297]: Reference 298
[^298]: Reference 299
[^299]: Reference 299
[^300]: Reference 291
[^301]: Reference 292
[^302]: Reference 293
[^303]: Reference 294
[^304]: Reference 295
[^305]: Reference 296
[^306]: Reference 297
[^307]: Reference 298
[^308]: Reference 299
[^309]: Reference 291
[^310]: Reference 292
[^311]: Reference 293
[^312]: Reference 294
[^313]: Reference 295
[^314]: Reference 296
[^315]: Reference 297
[^316]: Reference 298
[^317]: Reference 299
[^318]: Reference 291
[^319]: Reference 292
[^320]: Reference 293
[^321]: Reference 294
[^322]: Reference 295
[^323]: Reference 296
[^324]: Reference 297
[^325]: Reference 298
[^326]: Reference 299
[^327]: Reference 291
[^328]: Reference 292
[^329]: Reference 293
[^330]: Reference 294
[^331]: Reference 295
[^332]: Reference 296
[^333]: Reference 297
[^334]: Reference 298
[^335]: Reference 299
[^336]: Reference 291
[^337]: Reference 292
[^338]: Reference 293
[^339]: Reference 294
[^340]: Reference 295
[^341]: Reference 296
[^342]: Reference 297
[^343]: Reference 298
[^344]: Reference 299
[^345]: Reference 296
[^346]: Reference 297
[^347]: Reference 298
[^348]: Reference 299
[^349]: Reference 291
[^350]: Reference 292
[^351]: Reference 293
[^352]: Reference 294
[^353]: Reference 295
[^354]: Reference 296
[^355]: Reference 297
[^356]: Reference 298
[^357]: Reference 299
[^358]: Reference 291
[^359]: Reference 292
[^360]: Reference 293
[^361]: Reference 294
[^362]: Reference 295
[^363]: Reference 296
[^364]: Reference 297
[^365]: Reference 298
[^366]: Reference 299
[^367]: Reference 291
[^368]: Reference 292
[^369]: Reference 293
[^370]: Reference 294
[^371]: Reference 295
[^372]: Reference 296
[^373]: Reference 297
[^374]: Reference 298
[^375]: Reference 299
[^376]: Reference 291
[^377]: Reference 292
[^378]: Reference 293
[^379]: Reference 294
[^380]: Reference 295
[^381]: Reference 296
[^382]: Reference 297
[^383]: Reference 298
[^384]: Reference 299
[^385]: Reference 291
[^386]: Reference 292
[^387]: Reference 293
[^388]: Reference 291
[^389]: Reference 292
[^390]: Reference 293
[^391]: Reference 294
[^392]: Reference 295
[^393]: Reference 296
[^394]: Reference 297
[^395]: Reference 298
[^396]: Reference 299
[^397]: Reference 291
[^398]: Reference 292
[^399]: Reference 293
[^400]: Reference 294
[^401]: Reference 295
[^402]: Reference 296
[^403]: Reference 297
[^404]: Reference 298
[^405]: Reference 299
[^406]: Reference 291
[^407]: Reference 292
[^408]: Reference 293
[^409]: Reference 294
[^410]: Reference 295
[^411]: Reference 296
[^412]: Reference 297
[^413]: Reference 298
[^414]: Reference 299
[^415]: Reference 296
[^416]: Reference 297
[^417]: Reference 298
[^418]: Reference 299
[^419]: Reference 291
[^420]: Reference 292
[^421]: Reference 293
[^422]: Reference 294
[^423]: Reference 295
[^424]: Reference 296
[^425]: Reference 297
[^426]: Reference 298
[^427]: Reference 299
[^428]: Reference 291
[^429]: Reference 292
[^430]: Reference 293
[^431]: Reference 294
[^432]: Reference 295
[^433]: Reference 296
[^434]: Reference 297
[^435]: Reference 298
[^436]: Reference 291
[^437]: Reference 292
[^438]: Reference 293
[^439]: Reference 294
[^440]: Reference 295
[^441]: Reference 296
[^442]: Reference 297
[^443]: Reference 298
[^444]: Reference 299
[^445]: Reference 296
[^446]: Reference 297
[^447]: Reference 298
[^448]: Reference 299
[^449]: Reference 291
[^450]: Reference 292
[^451]: Reference 293
[^452]: Reference 294
[^453]: Reference 295
[^454]: Reference 296
[^455]: Reference 297
[^456]: Reference 298
[^457]: Reference 299
[^458]: Reference 291
[^459]: Reference 292
[^460]: Reference 293
[^461]: Reference 294
[^462]: Reference 295
[^463]: Reference 296
[^464]: Reference 297
[^465]: Reference 298
[^466]: Reference 291
[^467]: Reference 292
[^468]: Reference 291
[^469]: Reference 292
[^470]: Reference 291
[^471]: Reference 292
[^472]: Reference 291
[^473]: Reference 292
[^474]: Reference 291
[^475]: Reference 292
[^476]: Reference 291
[^477]: Reference 291
[^478]: Reference 291
[^479]: Reference 292
[^480]: Reference 291
[^481]: Reference 291
[^482]: Reference 291
[^483]: Reference 292
[^484]: Reference 291
[^485]: Reference 291
[^486]: Reference 291
[^487]: Reference 291
[^488]: Reference 291
[^489]: Reference 291
[^490]: Reference 291
[^491]: Reference 291
[^492]: Reference 291
[^493]: Reference 291
[^494]: Reference 291
[^495]: Reference 291
[^496]: Reference 291
[^497]: Reference 291
[^498]: Reference 291
[^499]: Reference 291
[^500]: Reference 291
[^501]: Reference 291
[^502]: Reference 291
[^503]: Reference 291
[^504]: Reference 291
[^505]: Reference 291
[^506]: Reference 291
[^507]: Reference 291
[^508]: Reference 291
[^509]: Reference 291
[^510]: Reference 291
[^511]: Reference 291
[^512]: Reference 291
[^513]: Reference 291
[^514]: Reference 291
[^515]: Reference 291
[^516]: Reference 291
[^517]: Reference 291
[^518]: Reference 291
[^519]: Reference 291
[^520]: Reference 291
[^521]: Reference 291
[^522]: Reference 291
[^523]: Reference 291
[^524]: Reference 291
[^525]: Reference 291
[^526]: Reference 291
[^527]: Reference 291
[^528]: Reference 291
[^529]: Reference 291
[^530]: Reference 291
[^531]: Reference 291
[^532]: Reference 291
[^533]: Reference 291
[^534]: Reference 291
[^535]: Reference 291
[^536]: Reference 291
[^537]: Reference 291
[^538]: Reference 291
[^539]: Reference 291
[^540]: Reference 291
[^541]: Reference 291
[^542]: Reference 291
[^543]: Reference 291
[^544]: Reference 291
[^545]: Reference 291
[^546]: Reference 291
[^547]: Reference 291
[^548]: Reference 291
[^549]: Reference 291
[^550]: Reference 291
[^551]: Reference 291
[^552]: Reference 291
[^553]: Reference 291
[^554]: Reference 291
[^555]: Reference 291
[^556]: Reference 291
[^557]: Reference 291
[^558]: Reference 291
[^559]: Reference 291
[^560]: Reference 291
[^561]: Reference 291
[^562]: Reference 291
[^563]: Reference 291
[^564]: Reference 291
[^565]: Reference 291
[^566]: Reference 291
[^567]: Reference 291
[^568]: Reference 291
[^569]: Reference 291
[^570]: Reference 291
[^571]: Reference 291
[^572]: Reference 291
[^573]: Reference 291
[^574]: Reference 291
[^575]: Reference 291
[^576]: Reference 291
[^577]: Reference 291
[^578]: Reference 291
[^579]: Reference 291
[^580]: Reference 291
[^581]: Reference 291
[^582]: Reference 291
[^583]: Reference 291
[^584]: Reference 291
[^585]: Reference 291
[^586]: Reference 291
[^587]: Reference 291
[^588]: Reference 291
[^589]: Reference 291
[^590]: Reference 291
[^591]: Reference 291
[^592]: Reference 291
[^593]: Reference 291
[^594]: Reference 291
[^595]: Reference 291
[^596]: Reference 291
[^597]: Reference 291
[^598]: Reference 291
[^599]: Reference 291
[^600]: Reference 291
[^601]: Reference 291
[^602]: Reference 291
[^603]: Reference 291
[^604]: Reference 291
[^605]: Reference 291
[^606]: Reference 291
[^607]: Reference 291
[^608]: Reference 291
[^609]: Reference 291
[^610]: Reference 291
[^611]: Reference 291
[^612]: Reference 291
[^613]: Reference 291
[^614]: Reference 291
[^615]: Reference 291
[^616]: Reference 291
[^617]: Reference 291
[^618]: Reference 291
[^619]: Reference 291
[^619]: Reference 291
[^620]: Reference 291
[^621]: Reference 291
[^622]: Reference 291
[^623]: Reference 291
[^624]: Reference 291
[^625]: Reference 291
[^626]: Reference 291
[^627]: Reference 291
[^628]: Reference 291
[^629]: Reference 291
[^630]: Reference 291
[^631]: Reference 291
[^632]: Reference 291
[^633]: Reference 291
[^634]: Reference 291
[^635]: Reference 291
[^636]: Reference 291
[^637]: Reference 291
[^638]: Reference 291
[^639]: Reference 291
[^640]: Reference 291
[^641]: Reference 291
[^642]: Reference 291
[^643]: Reference 291
[^644]: Reference 291
[^645]: Reference 291
[^646]: Reference 291
[^647]: Reference 291
[^648]: Reference 291
[^649]: Reference 291
[^650]: Reference 291
[^651]: Reference 291
[^652]: Reference 291
[^653]: Reference 291
[^654]: Reference 291
[^655]: Reference 291
[^656]: Reference 291
[^657]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^651]: Reference 291
[^652]: Reference 291
[^653]: Reference 291
[^656]: Reference 291
[^657]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^651]: Reference 291
[^652]: Reference 291
[^653]: Reference 291
[^657]: Reference 291
[^659]: Reference 291
[^651]: Reference 291
[^652]: Reference 291
[^653]: Reference 291
[^654]: Reference 291
[^655]: Reference 291
[^656]: Reference 291
[^657]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^657]: Reference 291
[^659]: Reference 291
[^657]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^651]: Reference 291
[^652]: Reference 291
[^653]: Reference 291
[^656]: Reference 291
[^657]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^659]: Reference 291
[^651]: Reference 291
[^652]: Reference 291
[^653]: Reference 291
[^657]: Reference 291
[^659]: Reference 291
[^651]: Reference 291
[^652]: Reference 291
[^653]: Reference 291
[^657]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^657]: Reference 291
[^659]: Reference 291
[^657]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^651]: Reference 291
[^659]: Reference 291
[^651]: Reference 291
[^652]: Reference 291
[^659]: Reference 291
[^651]: Reference 291
[^659]: Reference 291
[^651]: Reference 291
[^657]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^659]: Reference 291
[^651]: Reference 291
[^657]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^659]: Reference 291
[^651]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^657]: Reference 291
[^659]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^659]: Reference 291
[^651]: Reference 291
[^659]: Reference 291
[^651]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^659]: Reference 291
[^659]: Reference 291
[^651]: Reference 291
[^659]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^658]: Reference 291
[^651]: Reference 291
[^659]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^659]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^659]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^659]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^659]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^659]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^658]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^658]: Reference 291
[^658]: Reference 291
[^658]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^658]: Reference 291
[^658]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^658]: Reference 291
[^658]: Reference 291
[^658]: Reference 291
[^658]: Reference 291
[^658]: Reference 291
[^658]: Reference 291
[^658]: Reference 291
[^658]: Reference 291
[^658]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^658]: Reference 291
[^658]: Reference 291
[^658]: Reference 291
[^658]: Reference 291
[^659]: Reference 291
[^658]: Reference 291
[^658]: Reference 291
[^658]: Reference 291
[^658]: Reference 291
[^658]: Reference 291
[^658]: Reference 291
[^658]: Reference 291
[^658]: Reference 291
[^658]: Reference 291
[^658]: Reference 291
[^658]: Reference 291
[^658]: Reference 291
[^658]: Reference 291
[^658]: Reference 291
[^658]: Reference 291
[^658]: Reference 291
[^658]: Reference 291
[^658]: Reference 291
[^658]: Reference 291
[^658]: Reference 291
[^658]: Reference 291
[^658]: Reference 291
[^658]: Reference 291
[^658]: Reference 291
[^658]: Reference 291
[^658]: Reference 291
[^658]: Reference 291
[^658]: Reference 291
[^658]: Reference 291
[^658]: Reference 291
[^658]: Reference 291


debate ${ }^{30}$. Our rationale for defining a damaging variant was based on a recent study benchmarking the AI tool against clinically solved cases ${ }^{24}$. Stricter criteria for a damaging classification will allow for fewer false positives, but at the expense of false negatives and vice versa. However, the expectation is that false positives will dilute genetic signals, but truly benign variants are a priori not positively correlated with negative outcomes. Thus, the magnitudes and statistical significance of the associations between damaging genotypes and clinical variables reported here should be thought of as lower bounds. Finally, the goal of this study was to highlight the advantages of an AI-based Bayesian Networks approach as a proof-of-principle analysis, leveraging existing ISV and SVR clinical and genetic data. In this context, the risk predictions are directly relevant to the study cohort, but cannot be more widely applied without a validation cohort.

Collectively, our findings highlight how genetics, demography, and clinical variables interact synergistically to impact neurodevelopmental outcomes and underscore the importance of capturing and quantifying these synergies. We have also demonstrated the utility of Bayesian networks for conditional risk analyses. Moving forward, large-scale collaborations between genetic and clinical consortia will provide more extensive datasets to better understand the synergistic impacts of genetic and clinical variables on clinical outcomes in children with CHD.

Reporting summary. Further information on research design is available in the Nature Portfolio Reporting Summary linked to this article.

## Data availability

The sequencing data used in this analysis may be downloaded, with committee-approved access, from the database of Genotypes and Phenotypes (dbGaP) [www.ncbi.nlm.nih. gov/] (accession numbers phs000571.v5.p2). Clinical data for this cohort is available as a public use dataset (https://www.pediatricheartnetwork.org/login/). Source data for the main figures are available as Supplementary Data.

Received: 22 October 2022; Accepted: 15 September 2023;
Published online: 27 September 2023

## Acknowledgements

The clinical data for this project was supported by National Heart, Lung, and Blood Institute (NHLBI) Pediatric Heart Network grants HL068269, HL068270, HL068279, HL068281, HL068285, HL068288, HL068290, HL068292, and HL085057. The genomic data for this project was supported by the NHLBI Pediatric Cardiac Genomics Consortium (UM1-HL098147, UM1-HL128761, UM1-HL098123, UM1-HL128711, UM1HL098162, U01-HL131003, U01-HL098153, U01-HL098163), the National Center for Research Resources (U01-HL098153), and the National Institutes for Health (R01GM104390, 1S10OD021644-01A1). The content of this article is the responsibility of the authors and do not represent the official views of the National Heart, Lung, and Blood Institute or the NIH.

## Author contributions

T.A.M., E.J.H., J.W.G., M.W.R., M.Y., and M.T.F. conceived and designed the study. T.A.M., E.J.H., M.Y., and M.T.F. performed the bulk of the analysis and drafted the initial manuscript. J.W.G., M.W.R., J.W.N., W.C., E.G., J.F.C., S.C.Z., W.T.M., V.Z., C.R., J.R.K., B.W.M., S.C., J.K.V-S., E.M.G., M.S., N.R., D.B., and T.M.L. provided ongoing review of and feedback on analyses over the course of multiple meetings, and reviewed and revised the manuscript.

## Competing interests

M.Y. is a consultant to Fabric Genomics Inc. and has received consulting fees and stock grants from Fabric Genomics Inc. The remaining authors declare that they have no competing interests relevant to this project.

# Additional information 

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s43856-023-00361-2.

Correspondence and requests for materials should be addressed to Thomas A. Miller, Mark Yandell or Martin Tristani-Firouzi.

Peer review information Communications Medicine thanks Beatrice Latal and the other, anonymous, reviewer(s) for their contribution to the peer review of this work. A peer review file is available.

Reprints and permission information is available at http://www.nature.com/reprints
Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/ licenses/by/4.0/.

- The Author(s) 2023

[^0]
[^0]:    ${ }^{1}$ Department of Pediatrics, Maine Medical Center, Portland, ME, USA. ${ }^{2}$ Department of Human Genetics and Utah Center for Genetic Discovery, University of Utah, Salt Lake City, UT, USA. ${ }^{3}$ Department of Surgery, Children's Hospital of Philadelphia, and the Perelman School of Medicine, University of Pennsylvania, Philadelphia, PA, USA. ${ }^{4}$ Department of Pediatrics, University of Michigan, Ann Arbor, MI, USA. ${ }^{5}$ Department of Cardiology, Boston Children's Hospital, Department of Pediatrics, Harvard Medical School, Boston, MA, USA. ${ }^{6}$ Departments of Pediatrics and Medicine, Columbia University, New York, NY, USA. ${ }^{7}$ Division of Cardiology, Children's Hospital of Philadelphia, Department of Pediatrics, Perelman School of Medicine, University of Pennsylvania, Philadelphia, PA, USA. ${ }^{8}$ Heart Institute, Cincinnati Children's Hospital, Cincinnati, OH, USA. ${ }^{9}$ Department of Pediatrics, Medical University of South Carolina, Charleston, SC, USA. ${ }^{10}$ Children's Healthcare of Atlanta, Atlanta, GA, USA. ${ }^{11}$ Healthcore, Watertown, MA, USA. ${ }^{12}$ Division of Cardiology, Children's National Hospital, Washington, DC, USA. ${ }^{13}$ Labatt Family Heart Centre, The Hospital for Sick Children, Department of Pediatrics, University of Toronto, Toronto, ON, Canada. ${ }^{14}$ Department of Pediatrics Emory University School of Medicine, Atlanta, GA, USA. ${ }^{15}$ Department of Pediatrics, Children's Hospital Los Angeles, Los Angeles, CA, USA. ${ }^{16}$ Department of Pediatrics, Medical College of Wisconsin, Milwaukee, WI, USA. ${ }^{17}$ Stanford University School of Medicine, Stanford, CA, USA. ${ }^{18}$ Department of Pediatrics, University of Utah, Salt Lake City, UT, USA. ${ }^{19}$ These authors contributed equally: Thomas A. Miller, Edgar J. Hernandez. ${ }^{64}$ email: Thomas.A.Miller@mainehealth.org; myandell@genetics.utah.edu; Martin.Tristani@utah.edu