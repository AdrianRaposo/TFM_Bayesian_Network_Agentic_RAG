# A Multidimensional Bayesian Network Meta-Analysis of Chinese Herbal Injections for Treating Non-small Cell Lung Cancer With Gemcitabine and Cisplatin 

OPEN ACCESS

Edited by:<br>Ruiwen Zhang,<br>University of Houston, United States<br>Reviewed by:<br>Murali M Yallapu,<br>The University of Texas Rio Grande<br>Valley, United States<br>Wei Wang,<br>Shanxi Zhendong Pharmaceutical,<br>China<br>Quan Wang,<br>Peking University, China<br>Chen He Qun,<br>Central South University, China<br>*Correspondence:<br>Jiarui Wu<br>exogamy@163.com<br>†These authors have contributed equally to this work and share first authorship<br>Specialty section:<br>This article was submitted to<br>Ethnopharmacology, a section of the journal<br>Frontiers in Pharmacology<br>Received: 11 July 2021<br>Accepted: 19 August 2021<br>Published: 06 September 2021<br>Citation:<br>Ni M, Wu Z, Wang H, Zhou W, Wu C, Stalin A, Fu C, Ye P, Lu S, Tan Y, Huang Z, Fan X, Zhang J, Zhang X, Wang M and Wu J (2021) A Multidimensional Bayesian Network Meta-Analysis of Chinese Herbal Injections for Treating Non-small Cell Lung Cancer With Gemcitabine and Cisplatin.<br>Front. Pharmacol. 12:739673.<br>doi: 10.3389/fphar.2021.739673

Mengwei $\mathrm{Ni}^{1 \dagger}$, Zhishan $\mathrm{Wu}^{1 \dagger}$, Haojia Wang ${ }^{1}$, Wei Zhou ${ }^{1}$, Chao Wu ${ }^{1}$, Antony Stalin ${ }^{2}$, Changgeng Fu ${ }^{3}$, Peizhi Ye ${ }^{4}$, Shan Lu ${ }^{1}$, Yingying Tan ${ }^{1}$, Zhihong Huang ${ }^{1}$, Xiaotian Fan ${ }^{1}$, Jingyuan Zhang ${ }^{1}$, Xiaomeng Zhang ${ }^{1}$, Miaomiao Wang ${ }^{1}$ and Jiarui Wu ${ }^{1 *}$


#### Abstract

${ }^{1}$ Department of Clinical Chinese Pharmacy, School of Chinese Materia Medica, Beijing University of Chinese Medicine, Beijing, China, ${ }^{2}$ State Key Laboratory of Subtropical Silviculture, Department of Traditional Chinese Medicine, Zhejiang A\&F University, Hangzhou, China, ${ }^{3}$ Xiyuan Hospital of China Academy of Chinese Medical Sciences, Beijing, China, ${ }^{4}$ National Cancer Center/ National Clinical Research Center for Cancer/Chinese Medicine Department of the Cancer Hospital of the Chinese Academy of Medical Sciences and Peking Union Medical College, Beijing, China


Introduction: As non-small cell lung cancer (NSCLC) seriously threatens human health, several clinical studies have reported that Chinese herbal injections (CHIs) in combination with and gemcitabine plus cisplatin (GP) are beneficial. This multidimensional network meta-analysis aimed to compare the clinical efficacy and safety of different CHIs in combination with GP against NSCLC.

Methods: Randomized controlled trials (RCTs) for the treatment of NSCLC were retrieved from seven electronic databases from inception to April 30, 2020. Study selection and data extraction were based on a priori criteria. Data analysis was performed using Stata 13.0, WinBUGS 14.0 software. Multidimensional cluster analysis was performed using the "scatterplot3d" package in R 3.6.1 software.

Results: This network meta-analysis included 71 eligible RCTs and 10 Chinese herbal injections. Delisheng injection and Kangai injection had the highest probability in terms of clinical effectiveness rate ( $94.60 \%$ ) and gastrointestinal reactions ( $82.62 \%$ ) when combined with GP compared with the other interventions. Compound Kushen injection combined with GP ranked ahead of the other interventions in terms of performance status (73.36\%) and abnormal liver function (87.17\%). Shenmai injection combined with GP had the highest probability in terms of leukopenia ( $94.59 \%$ ) and thrombocytopenia ( $99.18 \%$ ).

Conclusion: The current evidence revealed that CHIs combined with GP have a better impact on patients with NSCLC than GP alone. Aidi injection, Compound kushen injection,

[^0]
[^0]:    Abbreviations: 95\% CI, 95\% Credible intervals; ADRs, Adverse drug reactions; CHIs, Chinese herbal injections; CR, complete response; IF, Inconsistency factors; KPS, Karnofsky performance status; MeSH, Medical subject heading; NMA, Network metaanalysis; NSCLC, Non-small-cell lung cancer; OR, Odds ratio; PD, Progressive disease; PR, Partial response; PRISMA, the preferred reporting items for systematic reviews and meta-analyses; RCTs, Randomized controlled trials; REML, Restricted maximum likelihood; SD, Stable disease; SUCRA, the surface under the cumulative ranking; TNM, Tumor node metastasis.

and Kanglaite injection deserve more attention of clinicians when combined with GP in patients with NSCLC. Additionally, due to the limitations of this network meta-analysis, further well-designed, large-sample, multicenter RCTs are required to support our findings adequately.

Keywords: non-small cell lung cancer, network meta-analysis, chinese herbal injections, gemcitabine plus cisplatin, multidimensional cluster

## INTRODUCTION

According to the International Agency for Research on Cancer (Sung et al., 2021), lung cancer is the second most commonly diagnosed cancer. It is the leading cause of cancer death, accounting for 11.4 and 18.0% of new cases and deaths of all cancers worldwide. With a 5-year survival rate of only 10–20% in most countries (Allemani et al., 2018), lung cancer has a poor prognosis. Based on histological type, lung cancer is internationally divided into small-cell lung cancer and non-small-cell lung cancer (NSCLC), with NSCLC accounting for approximately 80% of all lung cancer cases (Siegel et al., 2021). The primary treatment for early-stage lung cancer is surgery. However, due to the insidious nature of lung cancer and the delay in seeking medical treatment, 50% of patients missed the best time for surgery at diagnosis (La Fleur et al., 2019). Primary treatments for patients who cannot undergo surgery include targeted therapies, immunotherapies, and the combination of two drugs based on platinum (Maione et al., 2011; Ettinger et al., 2021), such as gemcitabine plus cisplatin (GP), paclitaxel plus cisplatin and vinorelbine plus cisplatin. GP regimen is commonly used for NSCLC patients, and its antineoplastic efficacy has been endorsed. However, this treatment is associated with a highly toxic physiological environment and adverse events that may even lead to treatment discontinuation (Lischalk et al., 2016; Osarogiagbon et al., 2016).

As a complementary and alternative medicine, traditional Chinese medicine (TCM) has gradually gained acceptance as an adjuvant treatment for cancer (Bao et al., 2014; Xiang et al., 2019). Studies have shown that TCM has a positive impact in retarding cancer progression and ameliorating chemotherapy-induced complications and adverse events (Hofseth and Wargovich, 2007; Konkimalla and Efferth, 2008). TCM in lung cancer, especially in advanced lung cancer, has accumulated rich

![img-0.jpeg](img-0.jpeg)

FIGURE 1  Graphical abstract of the network meta-analysis. Note: GP, gemcitabine plus cisplatin; SUCRA, surface under the cumulative ranking curve; OR, odds ratio.

clinical experience that can improve patients' quality of life and long-term survival (Chen et al., 1999). Chinese Herbal Injections (CHIs) are an indispensable part of TCM. Chinese patent medicines have been used most frequently in lung cancer patients, and CHIs account for the most significant proportion of Chinese patent medicines (Wu et al., 2015). There have been various CHIs used in the treatment of NSCLC, and the optimal strategy for combining CHIs with GP to treat NSCLC remains unclear. Therefore, this study systematically evaluates the efficacy of 10 CHIs in combination with GP for the treatment of NSCLC through a network meta-analysis (NMA) to provide evidence-based medicine for clinicians to choose an optimal strategy. The graphical abstract of this NMA is shown in Figure 1.

## METHODS

This study was conducted in accordance with the Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) Extension Statement for Reporting of Systematic Reviews Incorporating Network Meta-analyses of Health Care Interventions (Hutton et al., 2015). A completed PRISMA checklist is included in Supplementary File S1.

### Eligibility Criteria and Exclusion Criteria

Randomized controlled trials (RCTs) of CHIs in combination with GP for the treatment of NACLC. The article describes that “random” can be included, and the blind was unrestricted. The study included patients with TNM stage Ⅲ or Ⅳ NSCLC diagnosed by cytology or pathology, with no restrictions on gender, age, race, region or nationality. Interventions with any Chinese herbal injection combined with GP to treat NSCLC. The control group included GP alone OR any other Chinese herbal injection. There were no limitations on the dosages or treatment courses. If patients had complications during the therapeutic process, the corresponding therapy had to be adopted.

The exclusion criteria were as follows: 1) patients had any other primary tumor; 2) interventions included surgery or other Chinese medicine treatments, such as other Chinese patent medicine, Chinese herbal decoction, acupuncture, and massage; 3) duplicate literature, we included the first, larger sample size, and more information publication; 4) did not report relevant outcomes or corresponding criteria for evaluating the efficacy; 5) non-intravenous administration of CHIs; 6) self-controlled studies or randomized methods are high-risk such as alternation, assignment based on date of birth, case record number and date of presentation and 7) unclear drug name, dosages, or treatment courses.

The primary efficacy outcome was the clinical effective rate. The secondary outcome was performance status, and the adverse drug reactions (ADRs) outcomes were leukopenia, gastrointestinal reactions, thrombocytopenia, and abnormal liver function. 1) Clinical effectiveness rate. According to the response evaluation criteria in solid tumors by the WHO, the clinical effectiveness rate can be divided into four levels: complete response (CR), in which visible lesions disappear completely after >4 weeks; partial response (PR), in which the tumor area of a single lesion has been reduced by ≥50% or the sum of the products of the two largest vertical diameters of multiple lesions has been reduced by >50%; stable disease (SD), in which no significant change occurred within at least 4 weeks and estimated tumor size increased by <25% or decreased by <50%; and progressive disease (PD), in which new lesions or original lesions increased by ≥25%. The following formula calculated the clinical effectiveness rate: clinical effectiveness rate = (number of CR patients + number of PR patients)/total number of patients × 100%. 2) Performance status. The performance status was evaluated by the Karnofsky performance status (KPS) score. An increase or decrease in KPS score by <10 points was considered stable after treatment; increase in KPS score by ≥10 points was considered to improvement performance status after treatment; while decrease in KPS score by ≥10 points was considered to reduce in the performance status. Performance improvement rate = the number of patients with improved performance/total number of patients × 100%. 3) leukopenia, gastrointestinal reactions, thrombocytopenia, and abnormal liver function. They were evaluated according to the WHO criteria for acute and subacute toxic reaction of anticancer drugs formulated in 1981. The ADRs were divided into 5 grades. The incidence of ADRs = number of patients with ADRs/total number of patients × 100%.

### Search Strategy

Seven electronic databases, including PubMed, Cochrane Library, Embase, Chinese National Knowledge Infrastructure, Chinese Biomedical Literature Database, Chinese Scientific Journals Fulltext Database, and Wanfang Database, were searched from inception to April 30, 2020. To obtain the relevant literature, articles were retrieved by the combination of medical subject heading (MeSH) and free-text keywords, and the search strategies were constructed for three domains: 1) NSCLC, 2) CHIs, and 3) study type (RCTs). Using PubMed as an example, the following terms were used for NSCLC: “Non-Small-Cell Lung Carcinomas [MeSH Terms],” “Non-Small-Cell Lung Carcinoma,” “Nonsmall Cell Lung Cancer,” “Non Small Cell Lung Carcinoma,” “Non-Small Cell Lung Carcinoma,” and “Non-Small Cell Lung Cancer.” In addition, there were no restrictions on the publication year or language. Details on the retrieval strategies are provided in Supplementary File S2.

### Data Extraction

After deleting duplicate records by NoteExpress software (Wuhan University Library, Wuhan, China), two investigators independently screened the titles to remove the obviously irrelevant studies such as reviews and experimental animal reports. They also read the abstracts and full texts of the remaining studies to screen for potential studies according to the inclusion criteria and extracted data from eligible RCTs. Any divergences were resolved through discussion or by the third reviewer in the implementation process.

The following data were collected according to the predesigned form. 1) Publication information: Title, first author's name, and publication year. 2) Characteristics of the

enrolled patients with NSCLC: sample size, age, gender, pathological type, stage of cancer, and KPS score. 3) Information on the intervention: dosage, duration, and treatment cycle. 4) Outcomes: clinical effectiveness rate, performance status, ADRs such as gastrointestinal reactions and abnormal liver function and immune function related ADRs (leukopenia, thrombocytopenia). 5) Description of study design: blinding, randomized allocation methods, and other quality assessment items.

### Risk of Bias Assessment

Two researchers independently assessed the risk of bias within each study using the Cochrane Risk of Bias Tool recommended by the Cochrane Handbook 5.1 (Higgins et al. 2011). The following domains were assessed: selection bias (random sequence generation and allocation concealment), performance bias (blinding of the participants and personnel), detection bias (blinding of the outcome assessment), attrition bias (incomplete outcome data), reporting bias (selective reporting) and other bias. Each bias has three levels: “low risk”, “unclear risk” and “high risk”. Any discrepancies during this process were resolved either by consensus or by consultation with a third investigator.

### Statistical Analysis

STATA 13.1 software (Stata Corp, College Station, TX, United States) and WinBUGS 1.4.3 software (Medical Research Council Biostatistics Unit, Cambridge, United Kingdom) was used for statistical analysis. All graphs of the NMA were presented using Stata 13.1 software and the thickness of the lines in the network graph was proportional to the number of trials used for the comparisons, and the node sizes corresponded to the total sample sizes for the treatments (Chaimani et al. 2013; Shim et al. 2017). The odds ratio (OR) and its 95% confidence intervals (95% CI) were used to describe the effect for dichotomous outcomes. If the 95% CI did not contain 1, differences between compared groups were statistically significant. The NMA was performed using the WinBUGS software, whereas the Markov chain Monte Carlo method with a random-effects model was used for Bayesian inference. In the WinBUGS software, the number of simulation iterations was 200,000, and the first 10,000 iterations were used for burn-in to eliminate the impact of the initial value (Crainiceanu and Goldsmith, 2010). Moreover, the results of the WinBUGS software calculations were used by the Stata software to calculate the surface under the cumulative ranking curve (SUCRA), which ranged from 0 to 100%. An intervention with a larger SUCRA value was considered the more effective treatment (Rücker and Schwarzer, 2015; Trinquart et al. 2016). The results of the WinBUGS software calculations were employed by the Stata software to obtain SUCRA. Cluster analysis was also performed to comprehensively compare the effect of CHIs on two different outcomes, with the interventions that were located in the upper-right corner being superior to the others. Publication bias was described via a comparison-adjusted funnel plot using Stata software (Trinquart et al. 2012). Symmetric points on the graph indicate that there is no obvious publication bias. Cluster analysis was also performed to compare the effect of CHIs on two different outcomes comprehensively, with the interventions that were in the upper-right corner were superior to the others (Veroniki et al. 2015).

The amount and source of heterogeneity among included RCTs were conducted by Stata 13.0 software that conduct a meta-analysis of direct comparison between CHI+GP and GP analysis for each outcome. The heterogeneity within each injection subgroup was analyzed by Q test, and the p-value was used to evaluate the degree of heterogeneity. When p > 0.05, the difference within a group is considered small and the heterogeneity is not obvious. For outcomes with obvious heterogeneity, covariates that may have an impact on heterogeneity were analyzed in meta-regression by the restricted maximum likelihood (REML) method to estimate the variance component τ^{2} between studies. Sensitivity analysis investigates the influence of each individual study on the overall meta-analysis summary estimate, and assessed robustness of results. The presence and degree of inconsistency in each loop were infer by using the magnitude of the inconsistency factors (IF), and it was regarded as a better consistency when the lower bound of 95% CIs was equal to zero (Chaimani et al. 2013).

### Multidimensional Cluster Analysis

For a comprehensive assessment of efficacy, multidimensional cluster analysis based on the SUCRA values of any three outcomes of different CHIs was performed using the “scatterplot3d” package in R 3.6.1 software (Mathsoft, Cambridge, United States). The K-means method was used to cluster these interventions, and the number of clusters was modified according to the actual situation. The steps of clustering were as follows: 1) All interventions were randomly divided into k initial classes, and the average of the outcome indicators of these k classes was used as initial aggregation points. 2) An intervention was classified into the closest aggregation point category, and then the category aggregation points were updated to the average of the current outcome indicators. All interventions were recategorized and classified, and step 2) was repeated until all interventions were assigned. Finally, the ranking of interventions with three outcome indicators was visually represented by a three-dimensional stereogram. Different colors were applied to indicate interventions belonging to different categories.

### RESULTS

### Search Results

The search strategy initially yielded 6832 prospective articles from the electronic databases. After excluding 3611 duplicates and screening titles and abstracts, 1131 articles remained for further evaluation. After a detailed review, a total of 71 RCTs with 10 CHIs met our selection criteria. The number of included studies for the different CHIs was as follows: Aidi injection (23 RCTs), Chansu injection (1 RCT), Compound kushen injection (5 RCTs), Delisheng injection (2 RCTs), Javanica oil emulsion injection (6 RCTs), Kangai injection (5 RCTs), Kanglaite injection (14 RCTs), Shenmai injection (6 RCTs),

![img-1.jpeg](img-1.jpeg)

**FIGURE 2 ** Flow chart of the search for eligible studies. Note: n, number of articles. CNKI, China National Knowledge Infrastructure; WanFang, the WanFang Database; VIP, the Chinese Scientific Journals Full-Text Database; and SinoMed, the Chinese Biomedical Literature Database.

Shenqifuzheng injection (7 RCTs), and Xiaoaiping injection (2 RCTs). Information about the included injections is shown in **Supplementary File S3**. The PRISMA flow diagram of study selection is shown in **Figure 2**.

# Inclusion Studies and Characteristics

In total, the 71 RCTs enrolled 5728 patients with NSCLC involving 10 CHIs; 2903 of them received a combination of CHIs and GP in the experimental group, and 2825 patients received the only GP in the control group. All RCTs reported the sample size, patients' age, sex, tumor node metastasis (TNM) stage, and Karnofsky performance status score before treatment. Sixty-nine (97.18%) studies reported the clinical effectiveness rate, and 40 (56.34%), 50 (70.42%), 43 (60.56%), 33 (46.48%), and 20 (28.17%) RCTs reported the performance status, leukopenia, gastrointestinal reactions, thrombocytopenia, and abnormal liver function, respectively. Baseline characteristics of all included RCTs are summarized in **Table 1**. The network graphs of the 10 CHIs with different outcomes are depicted in **Figure 3**.

# Risk of Bias Assessment

In terms of random sequence generation, 21 of 71 studies used reasonable methods to generate the random sequence, 16 RCTs (22.54%) used a random number table, and 5 RCTs (7.04%) used a lottery; thus, the selection bias of these studies was rated as "low risk". Other studies were rated as "unclear risk". None of the included studies provided information on the allocation concealment and blinding methods, so performance bias and detection bias were assessed as "unclear". In addition, as all RCTs had no incomplete data and selective reporting, their attrition bias and reporting bias were evaluated as "low risk". For the assessment of the quality of the RCTs with regard to other bias, the original studies did not report inconsistent baselines, or other problems associated with high risk of bias; therefore, the other bias was noted as "low risk". The details of the risk of bias assessment for all included studies are shown in **Figure 4**.

# Network Meta-analysis

This study conducted subgroup analysis with direct comparison and sensitivity on the involved six outcomes. The two outcomes, leukopenia, and thrombocytopenia, with significant heterogeneity in the subgroup analysis, were further analyzed by meta regression. Then two factors of DDP dose and cancer grade were explored: relationship with heterogeneity. The tumor stages included in this study were all stage III-IV, which were consistent and had no obvious clinical heterogeneity. Therefore, this study only performed regression analysis on DDP dose. The regression results showed that dosage was not a statistically significant source of heterogeneity (p > 0.05). Sensitivity investigates the results of two outcomes in the two models, were similar, and the data was steady. The details were shown in **Supplementary File S4**.

TABLE 1  Characteristics of the included randomized controlled trials.


(Continued on following page)

TABLE 1  (Continued) Characteristics of the included randomized controlled trials.

The consistency test was performed for the outcome of clinical effectiveness rate. This NMA involved one triangular loop. The result ( $\mathrm{IF}=0.175,95 \% \mathrm{CI}=0.00-1.53$ ) indicated that there is no evidence of significant inconsistency.

## Clinical Effectiveness Rate

A total of 69 studies with 10 CHIs and 11 interventions reported clinical effectiveness rates in the NMA. The results suggested 7 types of CHIs: Aidi injection, Compound kushen injection, Delisheng injection, Javanica oil emulsion injection, Kangai injection, Kanglaite injection, and Shenqifuzheng injection, combined with GP were significantly more effective than GP alone. Combined with GP, Delisheng injection might have a greater potential to increase the clinical effectiveness rate than Shenmai injection. The network graph is depicted in Figure 3A, and the ORs with $95 \%$ CI are presented in Table 2.

Based on the ranking result of the clinical effectiveness rate, the relative ranking of interventions for improving the clinical effectiveness rate was as follows: Delisheng injection + GP (94.6\%) > Kanglaite injection + GP (67.43\%) > Compound kushen injection + GP (63.92\%) > Kangai injection + GP (63.31\%) > Aidi injection + GP (50.99\%) > Shenqifuzheng injection + GP (46.34\%) > Javanica oil emulsion injection + GP (43.67\%) > Chansu injection + GP (43.22\%) > Xiaoaiping injection + GP (39.36\%) > Shenmai injection + GP (32.59\%) > GP only (4.564\%). The results of ranking probabilities based on SUCRA are shown in Figure 5A and Table 3.

## Performance Status

A total of 40 studies with 10 CHIs and 11 interventions reported performance status in the NMA. The results suggested that 8 types of CHIs: Aidi injection, Compound kushen injection, Delisheng injection, Javanica oil emulsion injection, Kangai injection, Kanglaite injection, Shenmai injection, and Shenqifuzheng injection, combined with GP were significantly more effective than GP alone. There were no statistically significant differences between the other interventions. The network graph is depicted in Figure 3B, and the ORs with $95 \%$ CI are presented in Table 2.

Based on the ranking result of performance status, the relative ranking of the interventions to improve performance status was as follows: Compound kushen injection + GP (73.36\%) > Kangai injection + GP (61.13\%) > Shenqifuzheng injection + GP (57.89\%) > Xiaoaiping injection + GP (57.29\%) > Aidi injection + GP (54.47\%) > Shenmai injection + GP (55.71\%) $>$ Kanglaite injection + GP (53.65\%) > Javanica oil emulsion injection + GP (52.34\%) > Delisheng injection + GP (45.86\%) > Chansu injection + GP (35.31\%) > GP only (0.9969\%). The results of the ranking probabilities based on SUCRA are shown in Figure 5B and Table 3.

## Leukopenia

A total of 50 studies with 10 CHIs and 11 interventions reported leukopenia in the NMA. The results suggested that 6 types of CHIs: Aidi injection, Compound kushen injection, Javanica oil

![img-2.jpeg](img-2.jpeg)

FIGURE 3 Network graph for different outcomes. (A) Clinical effectiveness rate; (B) Performance status; (C) Leukopenia; (D) Gastrointestinal reactions; (E) Thrombocytopenia; and (F) Abnormal liver function. Note: ADI, Aidi injection; CKSI, Compound Kushen injection; DLSI, Delisheng injection; GP, Gemcitabine plus Cisplatin; JOEI, Javanica oil emulsion injection; KAI, Kangai injection; KLTI, Kanglaite injection; SMI, Shenmai injection; SQFZI, Shenqifuzheng injection; and XAPI, Xiaoaiping injection.

![img-3.jpeg](img-3.jpeg)

FIGURE 4 Assessment of risk bias.

emulsion injection, Kanglaite injection, Shenmai injection, and Shenqifuzheng injection, combined with GP were significantly more effective than GP alone. Combined with GP, Aidi injection might have a more significant potential to reduce leukopenia than Delisheng injection and Kanglaite injection. In addition, Compound kushen injection combined with GP could have greater potential to reduce the leukopenia than Delisheng injection; Shenmai injection was better than Compound kushen

TABLE 2 Odds ratio/mean difference (95%CI) of all therapeutic interventions.


TABLE 2 (Continued) Odds ratio/mean difference (95%CI) of all therapeutic interventions.


Note: The differences between the compared groups were deemed as significant when the 95% CI of the OR did not contain 1.00, which is underlined and bold. ADI, Aldi injection; CKSI, Compound Kushen injection; DLSI, Delisheng injection; GP, Gemcitabine plus Cisplatin; JOEI, Javanica oil emulsion injection; KAI, Kangai injection; KLTI, Kanglaite injection; SMI, Shenmai injection; SQFZI, Shenqifuzheng injection; XAPI, Xiaoaiping injection.

![img-4.jpeg](img-4.jpeg)

FIGURE 5  Surface under the cumulative ranking curves for outcomes. (A) Clinical effectiveness rate; (B) Performance status; (C) Leukopenia; (D) Gastrointestinal reactions; (E) Thrombocytopenia; and (F) Abnormal liver function. Note: ADI, Aldi injection; CKSI, Compound Kushen injection; DLSI, Delisheng injection; GP, Gemcitabine plus Cisplatin; JOEI, Javanica oil emulsion injection; KAI, Kangai injection; KLTI, Kanglaite injection; SMI, Shenmai injection; SQFZI, Shenqifuzheng injection; and XAPI, Xiaoaiping injection.

injection, Delisheng injection, Kangai injection, Kanglaite injection and Xiaoaiping injection; Javanica oil emulsion injection was better than Shenqifuzheng injection and Delisheng injection. There were no statistically significant differences between the other interventions. The network graph is depicted in Figure 3C, and the ORs with 95% CI are presented in Table 2.

Based on the ranking result of leukopenia, the relative ranking of the interventions to reduce leukopenia was as follows: Shenmai injection + GP (94.59%) > Shenqifuzheng injection + GP


Note: ADI, Aldi injection; CKSI, Compound Kushen injection; DLSI, Delisheng injection; GP, Gemcitabine plus Cisplatin; JOEI, Javanica oil emulsion injection; KAI, Kangai injection; KLTI, Kanglaite injection; SMI, Shenmai injection; SGFZI, Shenqifuzheng injection; XAPI, Xiaoaiping injection. (81.25%) > Aidi injection + GP (74.97%) > Javanica oil emulsion injection + GP (63.47%) > Compound kushen injection + GP (49.47%) > Kangai injection + GP (46.85%) > Kanglaite injection + GP (38.99%) > Xiaoaiping injection + GP (34.25%) > GP only (12.24%) > Delisheng injection + GP only (3.91%). The results of the ranking probabilities based on SUCRA are shown in Figure 5C and Table 3.

### Gastrointestinal Reactions

A total of 43 studies with 9 CHIs and 10 interventions reported gastrointestinal reactions in the NMA. The results suggested that 3 types of CHIs: Aidi injection, Compound kushen injection, Kangai injection, Kanglaite injection and Shenmai injection, combined with GP were significantly more effective than GP alone. In combination with GP, Aidi injection, Compound kushen injection, Kangai injection, Kanglaite injection, and Shenmai injection could have greater potential to reduce the gastrointestinal reactions than Delisheng injection. The network graph is depicted in Figure 3D, and the ORs with 95% CI are presented in Table 2.

Based on the ranking result of gastrointestinal reactions, the relative ranking of interventions to reduce the gastrointestinal reactions was as follows: Kangai injection + GP (82.62%) > Shenmai injection + GP (80.69%) > Aidi injection + GP (71.12%) > Kanglaite injection + GP (63.89%) > Compound kushen injection + GP (61.12%) > Xiaoaiping injection + GP (55.13%) > Javanica oil emulsion injection + GP (35.85%) > Shenqifuzheng injection + GP (28.65%) > GP only (18.48%) > Delisheng injection + GP (2.456%). The results of the ranking probabilities based on SUCRA are shown in Figure 5D and Table 3.

### Thrombocytopenia

A total of 33 studies with 9 CHIs and 10 interventions reported thrombocytopenia in the NMA. The results suggested that 3 types of CHIs: Aidi injection, Kanglaite injection, and Shenqifuzheng injection, combined with GP, were significantly more effective than GP alone. Combined with GP, Shenmai injection might have a greater potential to reduce the thrombocytopenia than Aidi injection, Compound kushen injection, Delisheng injection, Javanica oil emulsion injection, Kangai injection, Shenqifuzheng injection and Xiaoaiping injection. The network graph is depicted in Figure 3E, and the ORs with 95% CI are presented in Table 2.

Based on the ranking result of thrombocytopenia, the relative ranking of interventions to reduce thrombocytopenia was as follows: Shenmai injection + GP (99.18%) > Kanglaite injection + GP (81.92%) > Aidi injection + GP (64.98%) > Shenqifuzheng injection + GP (60.08%) > Compound kushen injection + GP (38.82%) > Kangai injection + GP (36.46%) > Javanica oil emulsion injection + GP (34.96%) > Delisheng injection + GP (32.84%) > Xiaoaiping injection + GP (32.71%) > GP only (18.06%). The results of the ranking probabilities based on SUCRA are shown in Figure 5E and Table 3.

### Abnormal Liver Function

A total of 20 studies with 7 CHIs and 8 interventions reported abnormal liver function in the NMA. The results suggested that 4

![img-5.jpeg](img-5.jpeg)

FIGURE 6 Cluster analysis plots for six outcomes. (A) Clinical effectiveness rate (x-axis) and performance status (y-axis); (B) Leukopenia (x-axis) and gastrointestinal reactions (y-axis); (C) Clinical effectiveness rate (x-axis), performance status (y-axis), and leukopenia (z-axis); (D) Clinical effectiveness rate (x-axis), performance status (y-axis), and gastrointestinal reactions (z-axis); (E) Performance status (x-axis), clinical effectiveness rate (y-axis), and thrombocytopenia (z-axis); (F) Performance status (x-axis), clinical effectiveness rate (y-axis), and abnormal liver function (z-axis). Note: Interventions with the same color belong to the same cluster, and interventions located in the upper-right corner indicate optimal therapy for two different outcomes. ADI, Aldi injection; CKSI, Compound Kushen injection; DLSI, Delisheng injection; GP, Gemcitabine plus Cisplatin; JOEI, Javanica oil emulsion injection; KAI, Kangai injection; KLTI, Kanglaite injection; SMI, Shenmai injection; SQFZI, Shenqifuzheng injection; and XAPI, Xiaoaiping injection.

![img-6.jpeg](img-6.jpeg)

FIGURE 7 Comparison-adjusted funnel plot for outcomes. (A) clinical effectiveness rate; (B) performance status. Note: ADI, Aidi injection; CKSI, Compound Kushen injection; DLSI, Delisheng injection; GP, Gemcitabine plus Cisplatin; JOEI, Javanica oil emulsion injection; KAI, Kangai injection; KLTI, Kanglaite injection; SMI, Shenmai injection; SQFZI, Shenqifuzheng injection; and XAPI, Xiaoaiqing injection.

types of CHIs: Aidi injection, Compound kushen injection, Javanica oil emulsion injection, and Kanglaite injection, combined with GP, were significantly more effective than GP alone. There were no statistically significant differences between the other interventions. The network graph is depicted in Figure 3F and the ORs with 95% CI are presented in Table 2.

Based on the ranking result of abnormal liver function, the relative ranking of interventions to reduce abnormal liver function was as follows: Compound kushen injection + GP (87.17%) > Kanglaite injection + GP (75.31%) > Shenqifuzheng injection + GP (48.45%) > Aidi injection + GP (48.22%) > Shenmai injection + GP (46.97%) > Javanica oil emulsion injection + GP (43.39%) > Delisheng injection + GP (35.93%) > GP only (14.55%). The results of the ranking probabilities based on SUCRA are shown in Figure 5F and Table 3.

### Cluster Analysis

Cluster analysis was used to comprehensively compare the effects of the interventions on two different outcomes. Eight interventions reported both clinical effectiveness rate and performance status. Compared with other interventions, Compound kushen injection + GP, Kangai injection + GP, and Kanglaite injection + GP were similarly superior, and GP alone produced the worst result. Moreover, in terms of reducing leukopenia and gastrointestinal reactions in 10 interventions, Shenmai injection + GP and Aidi injection + GP showed the most favorable benefit. At the same time, GP alone yielded the worst result. Different colored dots indicate different types of interventions in Figure 6.

When cluster analysis was conducted on 10 interventions reporting clinical effectiveness rate, performance status, and leukopenia, Shenmai injection + GP had the highest probability. In contrast, GP only had the worst ranking result. Similarly, for clinical effectiveness rate, performance status and thrombocytopenia, Shenmai injection + GP had the highest probability among the 8 interventions. Moreover, in the comprehensive ranking of clinical effectiveness rate, performance status, and gastrointestinal reactions among 10 interventions, Compound kushen injection + GP, Kangai injection + GP and Kanglaite injection + GP had advantages in the ranking, while GP only yielded the worst result. In addition, Compound kushen injection + GP and Kanglaite injection + GP had advantages in ranking, while GP only yielded the worst result in terms of clinical effectiveness rate, performance status, and abnormal liver function. Different colored dots indicate different types of interventions in Figure 6.

### Publication Bias

Comparison-adjusted funnel plots for the clinical effectiveness rate and performance status were used to test for publication bias. As shown in Figure 7 of the clinical effectiveness rate and performance status, the determined angles between the correction auxiliary line and the centerline indicated that this study had potential publication bias.

### DISCUSSION

To compare the efficacy outcomes of different CHIs in combination with GP for NSCLC, this study used the NMA method to analyze evidence-based data from RCTs. Based on the results of NMA, Delisheng injection in combination with GP was the best choice for improving short-term clinical efficacy in patients. In terms of improvement in performance status and reduction in abnormal liver function, Compound kushen injection in combination with GP performed significantly better than the other injections. In terms of leukopenia and thrombocytopenia, Shenmai injection was the best. In addition, Kangai injection in combination with GP had the best effect on reducing gastrointestinal reactions. However, clinicians should choose different treatments based on patients' specific conditions.

With a poor prognosis, NSCLC is the leading cause of cancer death and seriously threatens human health. GP regimen is commonly used in the treatment of NSCLC patients, and highly toxic drug reactions can even lead to treatment discontinuation and failure. As a complementary and alternative medicine, TCM for lung cancer, especially advanced lung cancer, has accumulated rich clinical experience, which can improve patients' quality of life and long-term survival. Shenmai injection is mainly prepared from the extract of Panax ginseng C.A.Mey. [Araliaceae; Ginseng radix et rhizome], Ophiopogon japonicus (Thunb.) Ker Gawl. [Liliaceae; Ophiopogonis radix]. A study (Sun et al., 2020) have shown that Shenmai injection can reprogram glucose metabolism and enhance the sensitivity of lung cancer cells to chemotherapy drugs through the AKT/mTOR/c-Myc pathway. Ginsenoside Rg3, the main component of Shenmai injection, could decrease chemoresistance-induced expression of the programmed death ligand 1, increase immunomodulatory actions and response to DNA damage, and thereby inhibit tumorigenesis and viability of lung cancer cells (Park et al., 2011; Jiang et al., 2017; Liu et al., 2019). Compound Kushen injection is mainly prepared by extracting Sophora flavescens Aiton [Fabaceae; Sophorae flavescentis radix] and Heterosmilax yunnanensis Gagnep. [Liliaceae]. Moreover, the main components of Compound Kushen injection are matrine and oxymatrine, which can inhibit the growth of tumor cells (Pu et al., 2018).

There has been only one previous NMA of different CHIs combined with GP for NSCLC, which was published in 2014 and included 12 CHIs (Tian et al., 2014). In contrast, this NMA has the following merits. First, the NMA used multidimensional cluster analysis for the first time to visualize the result of three outcomes comprehensively. Second, ADRs such as thrombocytopenia and abnormal liver function were added as outcome indicators for patients. The cluster analysis was performed based on the SUCRA values to select the superior CHIs in terms of efficacy. Finally, the eligibility criteria in this NMA were strictly formulated and defined. In particular, the patients of the included RCTs were restricted to stage III or IV NSCLC to reduce clinical heterogeneity. In that study, Aidi injection, Kangai injection, and Compound Kushen injection ranked ahead in terms of leukopenia and gastrointestinal reactions. Excluding the different CHIs of the two network researches, the CHIs had a similar ranking for these two outcomes.

However, the limitations of the current NMA cannot be avoided. First, 21 (29.58%) studies adequately reported the random sequence generation methods, while none of the included studies mentioned detailed information about allocation concealment and blinding methods, which may lead to selection bias, performance bias and detection bias. Second, most interventions of the included studies were CHIs in combination with GP versus GP, and only 1 study directly compared the efficacy of two Chinese herbal injections, which is a small proportion. Finally, limited by the application scope of CHIs, all studies were conducted in China, and all patients were Chinese. Therefore, the results may not be generalizable.

## CONCLUSION

Current evidence revealed that CHIs combined with GP have a better impact on patients with NSCLC than GP alone. Aidi injection, Compound kushen injection, and Kanglaite injection deserve more attention of clinicians when combined with GP in patients with NSCLC. Additionally, due to the limitations of this NMA, more head-to-head RCTs are needed to properly support our findings.

## AUTHOR CONTRIBUTIONS

MN: conceptualization, methodology, formal analysis; ZW: methodology, formal analysis, writing the original draft, and visualization. HW: methodology, formal analysis, review editing. WZ and CW, AS, CF and PY: supervision and language editing. SL, YT, XF and ZH: software and review editing. JZ, XZ and MW: formal analysis and review editing. JW: conceptualization, funding acquisition and project administration.

## FUNDING

The authors acknowledge receipt of the following financial support for the research, authorship, and/or publication of this article: the National Natural Science Foundation of China (grant numbers 81673829) and Young Scientists Training Program of Beijing University of Chinese Medicine (grant number BUCM-QNLJ 2019001).

## SUPPLEMENTARY MATERIAL

The Supplementary Material for this article can be found online at: https://www.frontiersin.org/articles/10.3389/fphar.2021.739673/ full\#supplementary-material

[^0]
[^0]:    Allemani, C., Matsuda, T., Di Carlo, V., Harewood, R., Matz, M., Nikšić, M., et al. (2018). Global Surveillance of Trends in Cancer Survival 2000-14 (CONCORD-3): Analysis of Individual Records for 37513025 Patients Diagnosed with One of 18 Cancers from 322 Population-Based Registries in 71 Countries. Lancet 391 (10125), 1023-1075. doi:10.1016/s0140-6736(17)33326-3

Chaimani, A., Higgins, J. P., Mavridis, D., Spyridonos, P., and Salanti, G. (2013). Graphical Tools for Network Meta-Analysis in STATA. PLoS One 8 (10), e76654. doi:10.1371/journal.pone. 0076654
Chen, H. L., Wang, W. P., Lan, Y. P., and Hong, L. H. (2010). Clinical Observation on the Effect of Bruceae Javanica Oil-Emulsion Injection on the Chemotherapy of GP in Patients with Stasis Lung Collateral Syndrome in Advanced NACLC. J. Pract.Oncolic. 25 (05), 584-586.

Chen, J., Tao, Q. S., Pang, L. R., Li, H., Huang, J., and Xu, C. H. (2012). Analysis on the Curative Effect of Addie Injection or Brucea Javanica Oil Injection Combined with Gp Chemotherapy on Non Small Cell Lung Cancer. Chin. Arch. Tradit. Chin. Med. 30 (11), 2455-2457.
Chen, Q. (2009). Efficacy of Chansu Injection in Combination with Gemcitabine and Cisplatin Chemotherapy in the Treatment of Patients with Advanced Non-small-cell Lung Cancer. China Foreign Med. Treat. 28 (36), 97+99.
Chen, Q. X., and Chen, Q. L. (2013). Observation on Efficacy Aidi Injection Combined with Chemotherapy in Treating Non-small Cell Lung Cancer. Healthmost-Readmagazine 12 (5), 258.
Chen, Y. (2018). The Efficacy of GP Combined with Kanglaite in the Treatment of Advanced Non-small Cell Lung Cancer. Med. J. Chin. People's Health 30 (8), 73-75. doi:10.3969/j.issn.1672-0369.2018.08.036
Chen, Y. Y. (2016). Efficacy of Aidi Injection Combined with Chemotherapy on Expression of VEGF-C and CYFR21-1 in Peripheral Blood in Patients with Advanced Non- Small Cell Lung Cancer. Chin. J. Clin. Ration. Drug Use 9 (17), 5-6.
Chen, Z. F., Li, C. Z., Liu, S. X., Hou, J., and Wang, J. M. (1999). Meta-analysis of the Efficacy and Safety of Traditional Chinese Medicine in the Treatment of Primary Non-small Cell Lung Cancer. J. Tradit. Chin. Med. (05), 287-289+285.
Crainiceanu, C. M., and Goldsmith, A. J. (2010). Bayesian Functional Data Analysis Using WinBUGS. J. Stat. Softw. 32 (11), i11. doi:10.18637/jss.v032.i11
Cui, L. Z., Zhang, L. J., Wang, X. Y., and Liu, Q. J. (2012). Clinical Observation of Kangai Injection Combined with Cisplatin Chemotherapy in Non Small Cell Lung Cancer. Cancer Res. Clin. (09), 632-634.
Ettinger, D. S., Wood, D. E., Aisner, D. L., Akerley, W., Bauman, J. R., Bharat, A., et al. (2021). NCCN Guidelines Insights: Non-small Cell Lung Cancer, Version 2.2021. J. Natl. Compr. Canc. Netw. 19 (3), 254-266. doi:10.6004/jnccn.2021.0013
Fang, H., Wang, J., Pan, C. F., Guo, S. G., Chu, D. J., and Zhang, J. (2013). Xiaoaiping Injection Combined with Cisplatin and Gemcitabine for Non-small Cell Lung Cancer: a Clinical Observation. Eval. Anal. Drug-use Hosp. China 13 (2), 165-168.
Feng, X. R., Li, X. Y., and Cui, E. H. (2008). Clinical Observation on Aidi Injection Combined with GP Chemotherapy in Treating 68 Patients with Advanced Non-small Cell Lung Cancer. J. Chin. Oncol. 14 (11), 892-893.
Feng, X. R., Zhang, W., and Cui, E. H. (2009). Efficacy of Shenmai Injection in Combination with Chemotherapy on Treating Advanced Non-small-cell Lung Cancer. J. Zhejiang Chin. Med. Univ. 33 (3), 350-351. doi:10.3969/j.issn.1005-5509.2009.03.030
Fu, Q., Du, Y. B., and Cao, G. Z. (2012). Efficacy of Shenmai Injection in Combination with GP Chemotherapy on Treating Advanced Non-small-cell Lung Cancer. J. Chin. Pract. Diagn. Ther. 26 (6), 585-587.
Guan, X. Q., Liu, J. W., and Li, L. (2009). Clinical Observation on the Effect of Seed Oil Injection Combined with Chemotherapy of GP for Advanced NSCLC. Chin. J. Postgrad. Med. 32 (16), 60-62. doi:10.3760/cma.j.issn.1673-4904.2009.16.025
Guan, Y., Guo, Q. S., and Song, J. (2010). Clinical Observation on the Effect of Kanglaite Injection on the Chemotherapy of GP in Elderly Patients with Advanced NSCLC. Chin. J. Geriatr. Care 8 (1), 5-7. doi:10.3969/j.issn.1672-4860-B.2010.01.001
Gui, Y. X., and Tian, G. F. (2016). Effect of Shenqifuzheng Injection Combined with Cisplatin and Gemcitabine in the Treatment of Non-small Cell Lung Cancer: a Prospective Randomized Control Trial. J. China Prescr. Drug 14 (7), 53-54. doi:10.3969/j.issn.1671-945X.2016.07.035
He, W., Wu, L., Yu, C. G., and Song, Y. (2011). Observation on the Clinical Effect of Combined Therapy of GP Regimen Plus Aidi Injection on Advanced Stage Non-small-cell Lung Cancer. J. Logist. Univ. PAP. (Med. Sci. 20 (04), 296-297+326.
He, Z. F. (2009). Clinical Observation on DeLiSheng Injection Combined with GP Chemotherapy in Stage III-IV Non-small Cell Lung Cancer. Capit. Food Med. 16 (04), 49.

Higgins, J. P., Altman, D. G., Gøtzsche, P. C., Jüni, P., Moher, D., Oxman, A. D., et al. (2011). The Cochrane Collaboration's Tool for Assessing Risk of Bias in Randomised Trials. BMJ 343, d5928. doi:10.1136/bmj.d5928
Hofseth, L. J., and Wargovich, M. J. (2007). Inflammation, Cancer, and Targets of Ginseng. J. Nutr. 137 (1 Suppl. l), 183s-185s. doi:10.1093/jn/137.1.183S

Hong, Y. G., Wang, J. S., and Jiao, Z. M. (2010). Clinical Observation on Aidi Injection Combined with GP Chemotherapy in Treating Advanced Non-small Cell Lung Cancer. Chin. J. Clin. Oncol. Rehabil. 17 (03), 247-249.
Huang, A. X., Yao, G. X., Chen, Y., Qian, W., Pu, L. M., and Lu, L. W. (2014). Efficacy of Shenqifuzheng Injection Combined with PG Therapy in the Treatment of Advanced Non-small Cell Lung Cancer. Chin. J. Biochem. Pharm. (1), 88-89.
Huang, W. J., Zheng, J. Q., and Guo, B. L. (2017). Clinical Observation of Aidi Injection Combined with GP Chemotherapy in the Treatment of Advanced Non-small Cell Lung Cancer and Effect on the Immune Function. J. Med. Theor. Pract. 30 (07), 995-997.
Hutton, B., Salanti, G., Caldwell, D. M., Chaimani, A., Schmid, C. H., Cameron, C., et al. (2015). The PRISMA Extension Statement for Reporting of Systematic Reviews Incorporating Network Meta-Analyses of Health Care Interventions: Checklist and Explanations. Ann. Intern. Med. 162 (11), 777-784. doi:10.7326/m14-2385
Jiang, Z., Yang, Y., Yang, Y., Zhang, Y., Yue, Z., Pan, Z., et al. (2017). Ginsenoside Rg3 Attenuates Cisplatin Resistance in Lung Cancer by Downregulating PD-L1 and Resuming Immune. Biomed. Pharmacother. 96, 378-383. doi:10.1016/ j.biopha.2017.09.129

Jin, C., Zhang, Y. H., Peng, M. F., Li, W. D., Ma, L., and Chen, W. S. (2004). Observation on Efficacy Aidi Injection Combined with Chemotherapy in Treating Non-small Cell Lung Cancer. Chin. J. Cancer Prev. Treat. (10), 1086-1088.
Ju, S., Li, C. C., and Li, Y. H. (2013). Aidi Injection Combined with GP Chemotherapy in the Treatment of Elderly Patients with Advanced Non-small-cell Lung Cancer. Strait. Pharm. J. 25 (03), 206-207.
Koskimalis, V. B., and Efferth, T. (2008). Evidence-based Chinese Medicine for Cancer Therapy. J. Ethnopharmacol. 116 (2), 207-210. doi:10.1016/j.iep.2007.12.009
La Fleur, L., Falk-Sörqvist, E., Smeds, P., Berglund, A., Sundström, M., Mattsson, J. S., et al. (2019). Mutation Patterns in a Population-Based Non-small Cell Lung Cancer Cohort and Prognostic Impact of Concomitant Mutations in KRAS and TP53 or STK11. Lung Cancer 130, 50-58. doi:10.1016/j.lungcan.2019.01.003
Li, B. H., and Li, H. (2010). Fufang Kushen Injection Combined with GP Regimen in the Treatment of Elderly Patients with Non-small-cell Lung Cancer. Shanxi J. Tradit. Chin. Med. 26 (09), 27+40.

Li, H. J., Shang, G. M., Dong, L., Chen, Y. N., Li, Y., Wang, W. Y., et al. (2012). Shenmai Injection Combined with Systemic Chemotherapy Treatment of Advanced Non-small Cell Lung Cancer and Effect on TNF- $\alpha$ in Serum. Chin. Arch. Tradit. Chin. Med. 30 (11), 2442-2445.
Li, J., Yang, Z. W., Song, X., Jian, Q., Sun, X. J., Zhang, H., et al. (2016). Study on Short-Term Efficacy and Safety of Aidi Injection Adjuvant GP Regimen in Advanced Non-small Cell Lung Cancer. Hebei Med. J. 38 (09), 1345-1347.
Li, Y., Li, H. J., Shang, G. M., Dong, L., Chen, Y. N., Wang, W. Y., et al. (2013). Efficacy of Shenmai Injection in Combination with Chemotherapy on Treating Advanced Non-small-cell Lung Cancer. Zhejiang J. Tradit. Chin. Med. 48 (1), 14-15. doi:10.3969/j.issn.0411-8421.2013.01.010
Li, Z. X., Liu, X. P., and Yuan, L. L. (2010). Efficacy of Aidi Injection in Combination with Gemcitabine and Cisplatin Chemotherapy in the Treatment of Patients with Advanced Non-small-cell Lung Cancer. J. Commu. Med. 8 (11), 23-24.
Liang, B., Yang, J. M., and Ju, X. W. (2009). Clinical Observation of Kangai Injection Combined with GP Chemotherapy for Non Small Cell Lung Cancer. J. Med. Forum 30 (08), 68-69.

Liang, S. M., Dong, Y. H., Wang, J., Song, J., Gong, X., and Hu, J. C. (2014). Kanglaite Combined with GP in the Treatment of 25 Cases of Senile Non-smallcell Lung Carcinoma. Acta Chin. Med. 29 (1), 11-12.
Lischalk, J. W., Woo, S. M., Kataria, S., Aghdam, N., Paydar, I., Repka, M. C., et al. (2016). Long-term Outcomes of Stereotactic Body Radiation Therapy (SBRT) with Fiducial Tracking for Inoperable Stage I Non-small Cell Lung Cancer (NSCLC). J. Radiat. Oncol. 5 (4), 379-387. doi:10.1007/s13566-016-0273-4
Liu, D. M., Zhang, J., Zhang, W., He, W. J., and Hao, G. J. (2017). Clinical Observation of Kanglaite Injection Combined with GP Chemotherapy in Advanced Non Small Cell Lung Cancer. J. Mod. Oncol. 25 (22), 3626-3628.
Liu, S. (2016). Effects of Kanglaite Injection Combined with Chemotherapy in Elderly Patients with Lung Cancer. Contemp. Med. 22 (28), 157-158.
Liu, T., Zuo, L., Guo, D., Chai, X., Xu, J., Cui, Z., et al. (2019). Ginsenoside Rg3 Regulates DNA Damage in Non-small Cell Lung Cancer Cells by Activating VRK1/P53BP1 Pathway. Biomed. Pharmacother. 120, 109483. doi:10.1016/j.biopha.2019.109483
Liu, Y. H., Liu, Y. H., and Zhang, T. Y. (2010). Clinical Short-Term Observation on Aidi Injection Combined with Chemotherapy in Treating Advanced Non-small Cell Lung Cancer. Natl. Med. Front. Chin. 5 (19), 46.

Liu, Y. H., and Zhao, Y. Y. (2014). Clinical Analysis on Aidi Injection Combined with GP Chemotherapy in Treating Advanced Non-small Cell Lung Cancer. Chin. J. Pract. Med. 41 (24), 67-69.
Lu, W. L. (2017). Efficacy of Compound Matrine Injection in Combination with Gemcitabine and Cisplatin Chemotherapy in the Treatment of Patients with Advanced Non-small-cell Lung Cancer. Liaoning J. Tradit. Chin. Med. 44 (06), $1214-1215$.
Lu, Y. (2016). Clinical Assessment on Kanglaite Injection Combined with GP Chemotherapy in Treating 62 Patients with Advanced Non-small Cell Lung Cancer. J. Aerospace Med. 27 (04), 460-461.
Ma, M. (2017). Efficacy of Aidi Injection Combined with GP Chemotherapy in the Treatment of Advanced NSCLC Patients with Qi and Yin Deficiency and Effect on Immune Function. Asia-pac. Tradit. Med. 13 (21), 108-110. doi:10.1111/ajco.12731
Maione, P., Rossi, A., Bareschino, M. A., Sacco, P. C., Schettino, C., Falanga, M., et al. (2011). Factors Driving the Choice of the Best Second-Line Treatment of Advanced NSCLC. Rev. Recent Clin. Trials 6 (1), 44-51. doi:10.2174/ 157488711793980192
Osarogiagbon, R. U., Lin, C. C., Smeltzer, M. P., and Jemal, A. (2016). Prevalence, Prognostic Implications, and Survival Modulators of Incompletely Resected Non-small Cell Lung Cancer in the U.S. National Cancer Data Base. J. Thorac. Oncol. 11 (1), e5-16. doi:10.1016/j.jtho.2015.08.002
Pan, S., Peng, L. H., and Qi, X. Z. (2011). Efficacy of Aidi Injection Combined with Chemotherapy in Treating Advanced Non-small-cell Lung Cancer. Zhejiang J. Integr. Tradit. Chin. West. Med. 21 (04), 232-233.

Park, D., Bae, D. K., Jeon, J. H., Lee, J., Oh, N., Yang, G., et al. (2011). Immunopotentiation and Antitumor Effects of a Ginsenoside Rg $_{3}$-Fortified Red Ginseng Preparation in Mice Bearing H460 Lung Cancer Cells. Environ. Toxicol. Pharmacol. 31 (3), 397-405. doi:10.1016/j.etap.2011.01.008
Pu, J., Tang, X., Zhuang, X., Hu, Z., He, K., Wu, Y., et al. (2018). Matrine Induces Apoptosis via Targeting CCR7 and Enhances the Effect of Anticancer Drugs in Non-small Cell Lung Cancer In Vitro. Innate Immun. 24 (7), 394-399. doi:10.1177/1753425918800555
Qiu, K. (2013). Clinical Observation of Traditional Chinese Medicine Combined with Chemotherapy for Advanced Non-small Cell Lung Cancer. China Pract. Med. 8 (34), 167-168.
Rücker, G., and Schwarzer, G. (2015). Ranking Treatments in Frequentist Network Meta-Analysis Works without Resampling Methods. BMC Med. Res. Methodol. 15, 58. doi:10.1186/s12874-015-0060-8
Shan, H. L. (2015). Fufang Kushen Injection Combined with GP Regimen in the Treatment of Elderly Patients with Advanced Non-small-cell Lung Cancer. J. Basic Clin. Oncol. 28 (05), 419-421.

Shang, G. M., Chen, Y. N., Li, H. J., Dong, L., Li, Y., Wang, W. Y., et al. (2012). Efficacy of Shenmai Injection Combined with Chemotherapy on Expression of VEGF and BFGF in Peripheral Blood in Patients with Advanced Non-small Cell Lung Cancer. Zhejiang J. Tradit. Chin. Med. 47 (8), 620-621. doi:10.3969/ j.issn.0411-8421.2012.08.054

Shim, S., Yoon, B. H., Shin, I. S., and Bae, J. M. (2017). Network Meta-Analysis: Application and Practice Using Stata. Epidemiol. Health 39, e2017047. doi:10.4178/epih.e2017047
Siegel, R. L., Miller, K. D., Fuchs, H. E., and Jemal, A. (2021). Cancer Statistics, 2021. CA A. Cancer J. Clin. 71 (1), 7-33. doi:10.3322/caac. 21654
Song, Y. (2014). Clinical Observation on Treating Advanced Non-small Cell Lung Cancer with the Compound Kushen Injection Plus Chemotherapy. Clin. J. Chin. Med. 6 (34), 4-6.

Su, B. K. (2017). Brucea Javanica Oil Emulsion Injection Combined with GP Regimen in Treatment of Advanced Non-small Cell Lung Cancer. Master, Fujian University of Traditional Chinese Medicine.
Su, W. Z. (2010). Clinical Observation of Kangai Injection Combined with Chemotherapy in Non Small Cell Lung Cancer. Shanxi J. Tradit. Chin. Med. 26 (12), 31-32.
Sun, G. S., Liu, J. R., Wang, T. T., and Zhu, J. D. (2008). Clinical Observation on Aidi Injection Combined with GP Chemotherapy in Treating 33 Patients with Advanced Non-small Cell Lung Cancer. Fujian Med. J. 30 (06), 134.
Sun, Y., Chen, Y., Xu, M., Liu, C., Shang, H., and Wang, C. (2020). Shenmai Injection Supresses Glycolysis and Enhances Cisplatin Cytotoxicity in Cisplatin-Resistant A549/DDP Cells via the AKT-mTOR-C-Myc Signaling Pathway. Biomed. Res. Int. 2020, 9243681. doi:10.1155/2020/9243681
Sung, H., Ferlay, J., Siegel, R. L., Laversanne, M., Soerjomataram, I., Jemal, A., et al. (2021). Global Cancer Statistics 2020: GLOBOCAN Estimates of Incidence and

Mortality Worldwide for 36 Cancers in 185 Countries. CA Cancer J. Clin. 71 (3), 209-249. doi:10.3322/caac. 21660
Tian, H. Q., Yu, S. Y., Wang, B., Liang, G. W., and Huang, X. Q. (2007). Effect of Fructus Bruceae Oil Emulsion on Cellular Immune Function and Quality of Life in Patients with Non-small Cell Lung Cancer. Zhongguo Zhong Xi Yi Jie He Za Zhi 27 (02), 157-159.
Tian, J. H., Zhao, Y., Li, J. L., Ge, L., and Yang, K. H. (2014). Network MetaAnalysis of 12 Chinese Herb Injections Combined with Gemcitabine and Cisplatin for Non-small Cell Lung Cancer. Chin. J. Drug Eval. 31 (06), 350-355.
Tian, L., and Wang, C. Y. (2017). Brucea Javanica Oil Emulsion Injection Combined with GP Regimen in Treatment of Advanced Non-small Cell Lung Cancer. Acta Chin. Med. 32 (03), 339-341.
Tong, Q. (2007). Study of Kanglaite Combined with Chemotherapy on Life Quality Improved in Non-small Cell Lung Cancer Patients. Mod. J. Integr. Tradit. Chin. West. Med. (11), 1456-1457.
Tong, W. N., Zhuo, A. S., and Zhao, H. X. (2011). Brucea Javanica Oil Emulsion Injection Combined with GP Regimen in Treatment of Advanced Non-small Cell Lung Cancer. People's Milit. Surg. 54 (10), 885-887.
Trinquart, L., Attiche, N., Bafeta, A., Porcher, R., and Ravaud, P. (2016). Uncertainty in Treatment Rankings: Reanalysis of Network Meta-Analyses of Randomized Trials. Ann. Intern. Med. 164 (10), 666-673. doi:10.7326/m152521
Trinquart, L., Chatellier, G., and Ravaud, P. (2012). Adjustment for Reporting Bias in Network Meta-Analysis of Antidepressant Trials. BMC Med. Res. Methodol. 12, 150. doi:10.1186/1471-2288-12-150
Veroniki, A. A., Soobiah, C., Tricco, A. C., Elliott, M. J., and Straus, S. E. (2015). Methods and Characteristics of Published Network Meta-Analyses Using Individual Patient Data: Protocol for a Scoping Review. BMJ Open 5 (4), e007103. doi:10.1136/bmjopen-2014-007103
Wang, L., Wang, W., and Kawuli, A. T. K. (2015). Observation of Kanglaite Injection Combined with Cisplatin on Lung Cancer. Pract. Clin. J. Integr. Tradit.I Chin. West. Med. 15 (06), 10-12.
Wang, Y., Hui, S., Li, M., and Zhang, C. H. (2017). Clinical Trial of Kanglaite Injection in Gemcitabine Combined Cisplatin Regimen Chemotherapy for Advanced Non-small Cell Lung Cancer. Chin. J. Clin. Pharm. 33 (23), 2354-2356. doi:10.13699/j.cnki.1001-6821.2017.23.008
Wang, Y. L. (2009). Aidi Injection Combined with GP Regimen in the Treatment of Elderly Patients with Advanced Non-small-cell Lung Cancer. Chin. Prim. Health Care 23 (11), 101-102.
Wen, K., Li, J., and Peng, D. Y. (2009). Observation on Efficacy Aidi Injection Combined with GP Chemotherapy in Treating Advanced Non-small Cell Lung Cancer. J. Basic Chin. Med. 15 (09), 716-717.
Wu, M., Lu, P., Shi, L., and Li, S. (2015). Traditional Chinese Patent Medicines for Cancer Treatment in China: a Nationwide Medical Insurance Data Analysis. Oncotarget 6 (35), 38283-38295. doi:10.18632/oncotarget. 5711
Wu, T., and Chen, S. C. (2017). Research on Feasibility of Aidi Injection and Chemotherapy in the Non-small Cell Lung Cancer. China Foreign Med. Treat. 36 (15), 126-127+136.
Xiang, Y., Guo, Z., Zhu, P., Chen, J., and Huang, Y. (2019). Traditional Chinese Medicine as a Cancer Treatment: Modern Perspectives of Ancient but Advanced Science. Cancer Med. 8 (5), 1958-1975. doi:10.1002/cam4.2108
Xu, H., Yang, T., and Zhou, M. (2013). Clinical Assessment on Aidi Injection Combined with GP Chemotherapy in Treating Advanced Non-small Cell Lung Cancer. Int. J. Resp. (10), 765-767.
Xu, R. H. (2012). Effect of Aidi Injection Combined with GP Chemotherapy on Serum VEGF of Patients with Advanced Non-small Cell Lung Cancer. Healthmust-Readmagazine (5), 23-24.
Yao, D. J., Cai, Y., and Chen, Y. (2013). Clinical Observation on Shenqifuzheng Injection Combined with GC Chemotherapy in Treating Advanced Non-small Cell Lung Cancer. Chin. J. Clin. Res. 26 (12), 1378-1379.
Yao, J., and Song, X. (2017). Efficacy and Safety Analysis of GP Scheme Combined with Kanglaite Injection for Advanced Non-small Cell Lung Cancer. J. Clin. Exp. Med. 16 (12), 1195-1198. doi:10.3969/j.issn.16714695.2017.12.018
Yi, C. Z., Xu, T. H., Zhang, D. F., and Hu, C. X. Z. (2011). Clinical Observation on the Effect of Kangai Injection on the Chemotherapy of GP in Elderly Patients with Advanced NSCLC. Guiding J. Tradit. Chin. Med. Pharm. 17 (09), 24-26.

You, J. S., and Jia, X. H. (2011). Clinical Observation of Kanglaite Injection Combined with Chemotherapy for Advanced Non-small Cell Lung Cancer. J. Med. Inf. 24 (12), 799. doi:10.3969/j.issn.1006-1959.2011.12.B12
Zhang, B., Chen, M. X., Chen, H. Y., and Shen, Z. J. (2017a). Effect of Fructus Bruceae Oil Emulsion on Peripheral Blood T Lymphocyte Subsets and the Quality of Life in Elderly Patients with NSCLC. Shanxi Med. J. 46 (12), 1402-1404.
Zhang, F. Y., Li, Q. W., Guan, J. Z., and Cui, L. P. (2011). Curative Observation of Xiaoaiping Injection Combined with GP Regimen in the Treatment of Patients with Advanced Non-small Cell Lung Cancer. J. Basic Clin. Oncol. 24 (5), 415-417. doi:10.3969/j.issn.1673-5412.2011.05.018
Zhang, L. (2009). Clinical Observation on Aidi Injection Combined with GP Chemotherapy in Treating Advanced Non-small Cell Lung Cancer. J. Pract. Med. 25 (17), 2929-2930.
Zhang, L. M., Chen, J. H., Wang, W., Wen, X. P., Zhou, W. W., and Yi, H. H. (2017b). Efficacy of Shenqifuzheng Injection in the Treatment of Advanced Non-small Cell Lung Cancer. World Clin. Med. 11 (16), 113-114.
Zhang, Y. H. (2012). Clinical Observation on Aidi Injection Combined with GP Chemotherapy in Treating Non-small Cell Lung Cancer. Mod. J. Integr. Tradit. Chin. West. Med. 21 (19), 2095-2096.
Zhao, K., Yang, J. Q., Wang, J. H., Li, Y. H., Wang, H. J., and Zhang, A. J. (2012). Influence of Compound Matrine Injection Combined with GP Regimen on Therapeutic Efficacy and the Quality of Life in Patients with Advanced Nonsmall Cell Lung Cancer. Pract. Prev. Med. 19 (12), 1853-1854.
Zhao, X. Q. (2014). Clinical Research of Combined Therapy of Chinese and Western Medicine on Advanced Non- Small Cell Lung Cancer. Hebei J. Tradit. Chin. Med. (7), 1029-1031.
Zhou, J., and Ni, S. S. (2009). The Therapy of DLS Combined with Chemotherapy in Stage III-IV Non-small Cell Lung Cancer. J. Clin. Pulm. Med. 14 (05), 642-644.
Zhou, T., Liu, S. Q., Gao, P., Zhang, J., and Wang, L. (2009). Shenqifuzheng Injection Combined with GC Chemotherapy in the Treatment of 35 Patients of

Advanced Non-small Cell Lung Cancer. Cancer Res. Clin. 21 (10), 706-707. doi:10.3760/crna.j.issn.1006-9801.2009.10.022
Zhou, Z. Y. (2014). Clinical Observation of Kangai Injection Combined with Cisplatin Chemotherapy in Non Small Cell Lung Cancer. Chin. Community Doctors 30 (13), 82-83.
Zhu, J. J., and You, Y. J. (2016). Improvement Effect of Kanglaite Injection Combined with GP Program on the Immunity of Patients with Non-smallcell Lung Cancer at Advanced Stage. Henan Tradit. Chin. Med. 36 (11), 1943-1945.
Zou, C. Y., Lv, P. Z., Wang, X. L., and Zong, F. (2011). Effects of Kanglaite Injection on Expression of CD28 of T-Lymphocytes in Peripheral Blood in Elderly Patients with Lung Cancer. Jiangsu Med. J. 37 (13), 1768-1770.

Conflict of Interest: The authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest.

Publisher's Note: All claims expressed in this article are solely those of the authors and do not necessarily represent those of their affiliated organizations, or those of the publisher, the editors and the reviewers. Any product that may be evaluated in this article, or claim that may be made by its manufacturer, is not guaranteed or endorsed by the publisher.

Copyright © 2021 Ni, Wu, Wang, Zhou, Wu, Stalin, Fu, Ye, Lu, Tan, Huang, Fan, Zhang, Zhang, Wang and Wu. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.