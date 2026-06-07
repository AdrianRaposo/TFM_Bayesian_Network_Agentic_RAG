# Comparative Efficacy of Tonic Chinese Herbal Injections for Treating Sepsis or Septic Shock: A Systematic Review and Bayesian Network Meta-Analysis of Randomized Controlled Trials 

OPEN ACCESS

Edited by:<br>Runyue Huang, Guangdong Provincial Hospital of Chinese Medicine, China

Reviewed by: Xianfei Ding, First Affiliated Hospital of Zhengzhou University, China Chunxiang Liu, Tianjin University of Traditional Chinese Medicine, China
*Correspondence: Xinqiao Liu 13821150112@163.com Guiwei Li li-guiwei@163.com
${ }^{1}$ These authors have contributed equally to this work and share first authorship

Specialty section:
This article was submitted to Ethnopharmacology, a section of the journal
Frontiers in Pharmacology
Received: 06 December 2021
Accepted: 28 January 2022
Published: 15 March 2022
Citation:
Xiao L, Niu L, Xu X, Zhao Y, Yue L, Liu X and Li G (2022) Comparative Efficacy of Tonic Chinese Herbal Injections for Treating Sepsis or Septic Shock: A Systematic Review and Bayesian Network Meta-Analysis of Randomized Controlled Trials. Front. Pharmacol. 13:830030. doi: 10.3389/fphar.2022.830030

Lu Xiao ${ }^{1,2,3 \dagger}$, Liqing Niu ${ }^{1,2 \dagger}$, Xinyi Xu ${ }^{1,2}$, Yuetong Zhao ${ }^{1,2}$, Linkai Yue ${ }^{1,2}$, Xinqiao Liu ${ }^{1,2 *}$ and Guiwei $\mathrm{Li}^{1,2 *}$

${ }^{\dagger}$ Department of Emergency, First Teaching Hospital of Tianjin University of Traditional Chinese Medicine, Tianjin, China, ${ }^{2}$ National Clinical Research Center for Chinese Medicine Acupuncture and Moxibustion, Tianjin, China, ${ }^{3}$ State Key Laboratory of MultiFractions Traditional Chinese Medicine, Tianjin University of Traditional Chinese Medicine, Tianjin, China

Background: Sepsis has high mortality and is responsible for significant healthcare costs. Chinese herbal injections (CHIs) have been widely used in China as a novel and promising treatment option for sepsis. Therefore, this study assessed and ranked the effectiveness of CHIs to provide more sights for the selection of sepsis treatment.

Method: Eight databases were searched from their inception up to September 1, 2021. The methodological quality of included study was evaluated by the Revised Cochrane risk-of-bias tool for randomized trials. Then Bayesian network meta-analysis was performed by OpenBUGS 3.2.3 and STATA 14.0 software. The surface under the cumulative ranking curve (SUCRA) probability values were applied to rank the examined treatments. Publication bias was reflected by a funnel plot.

Results: A total of 50 eligible randomized controlled trials involving 3,394 participants were identified for this analysis. Five CHIs including Shenfu injection, Shenmai injection, Shengmai injection, Shenqifuzheng injection, and Huangqi injection were included. The results of the NMA and sensitivity analysis showed that Shenqifuzheng (MD = -4.48, 95\% $\mathrm{Cl}=-5.59$ to -3.24 ), Shenmai ( $\mathrm{MD}=-3.38,95 \% \mathrm{Cl}=-4.38$ to -2.39 ), Shenfu ( $\mathrm{MD}=$ $-2.38,95 \% \mathrm{Cl}=-3.03$ to -1.70 ) and Shengmai ( $\mathrm{MD}=-1.90,95 \% \mathrm{Cl}=-3.47$ to -0.31 ) combined with Western medicine (WM) had a superior effect in improving the APACHE II score. Based on SUCRA values, Shenqifuzheng injection (95.65\%) ranked highest in the APACHE II score, followed by Shenmai (74\%), Shenfu (47.1\%), Shengmai (35.3\%) and Huangqi injection (33.2\%). Among the secondary outcomes, Shenmai injection was the

[^0]
[^0]:    Abbreviations: CHI, Chinese herbal injection; NMA, network meta-analysis; SUCRA: surface under the cumulative ranking curve; RCT: randomized controlled trial; AMR: antimicrobial resistance; AKI: acute kidney injury; ICU: intensive care unit; WM: Western medicine; OR: odds ratio; MD: mean difference; SMD: standardized mean difference; ADRs/ADEs: adverse drug reactions or adverse drug events; CNKI: China National Knowledge Infrastructure; VIP: Chinese Scientific Journal Database; SF: Shenfu injection; SM: Shenmai injection; SGM: Shengmai injection; SQFZ: Shenqifuzheng injection; HQ: Huangqi injection.

most favorable intervention in reducing PCT and CRP levels, and Shenqifuzheng injection was the second favorable intervention in reducing CRP level. Shenfu injection combined with WM was more effective than the other treatments in decreasing the serum IL-6 and TNF- $\alpha$ levels and lowering the 28-days mortality. Regarding the improvement of immune function, Shenqifuzheng injections had obvious advantages.

Conclusion: In conclusion, Shenqifuzheng injection was the optimum treatment regimen to improve APACHE II score, reduce CRP level, and regulate immune function. Shenfu injection was superior in reducing the expression of inflammatory factors and decreasing 28-days mortality. Nevertheless, more multicenter, diverse, and direct comparisons randomized controlled trials are needed to further confirm the results.

Systematic Review Registration: https://www.crd.york.ac.uk/PROSPERO/display_ record.php?RecordID=254531, identifier CRD42021254531.

Keywords: network meta-analysis, sepsis, septic shock, Chinese herbal injections, combination therapy

## INTRODUCTION

Sepsis is life-threatening organ dysfunction caused by dysregulated host response to infection (Singer et al., 2016). Sepsis and septic shock are major healthcare problem that contributes to the most causes of death in the intensive care unit (ICU) (Annane et al., 2003). Contemporary estimates indicate that more than 19 million people develop sepsis every year and that half of these will never recover; 6 million patients will die and approximately 3 million will survive with cognitive and functional impairments (Reinhart et al., 2017; Perner et al., 2018; Prescott and Angus, 2018). What's more, the ongoing COVID-19 pandemic has infected over two million people around the world, claiming the lives of nearly 5 million people worldwide. Among the patients hospitalized with COVID-19, $26 \%$ have been treated as critical cases, which involving sepsis or even septic shock (Fan et al., 2020).

Currently, therapies for sepsis and septic shock mainly depend on fluid resuscitation, antibiotics, vasoactive agents, corticosteroid, and mechanical ventilation (Evans et al., 2021). The mainstays of treatments are early antibiotics and restoration of perfusion (IV fluids and vasopressor therapy), which are crucial for the prognosis of patients with sepsis or septic shock (Seymour et al., 2017; Kuttab et al., 2019). Timely initiation of broad-spectrum antibiotic therapy is strongly recommended in patients with sepsis and septic shock as it is associated with improved outcomes (Zhang D. et al., 2015; Seymour et al., 2017). However, the problem of antimicrobial resistance (AMR) has increased significantly worldwide (Marston et al., 2016), and decreasing the use of broad-spectrum antibiotics is a priority as this is obviously connected with the problem of AMR. This appears to be closely relevant in the ICU(De Waele et al., 2018). Additionally, optimal dosing of antibiotics in sepsis or septic shock is often not achieved with current recommended doses. The challenge is preventing underdosing while avoiding adverse effects associated with overdosing especially in those patients with acute kidney injury (AKI) due to sepsis. Moreover, fluid resuscitation is a cornerstone in the management of hemodynamic stabilization (Cheng et al., 2019;

Kuttab et al., 2019). Despite being a very common therapy in the ICU, optimizing fluid administration is still challenging. Excessive fluid loading is associated with organ dysfunction and death in patients with sepsis (Sakr et al., 2017). Selection of the right kind of fluid is also a problem. Multi-center randomized controlled trials (RCTs) have shown harmful effects of synthetic colloids, notably AKI. Corticosteroids could inhibit the expression and action of many cytokines involved in the inflammatory response associated with sepsis. International guidelines recommend that IV corticosteroids are used for adults with septic shock and an ongoing requirement for vasopressor therapy (Evans et al., 2021). Although some large trials have established that corticosteroids may be effective in shock reversal and reducing ICU length of stay, it is still unclear if corticosteroids could reduce mortality of sepsis. What's more, corticosteroids usually have some side effects, such as hyperglycemia, hypernatremia, and so on (Keh et al., 2016; Annane et al., 2018; Rochwerg et al., 2018; Venkatesh et al., 2018; Fang et al., 2019). Despite having applied all the above therapies, the mortality of sepsis remains high. Current therapies mainly rely on the timely and appropriate administration of antimicrobials and supportive therapies, but the search for pharmacotherapies modulating the host response has been unsuccessful.

In recent years, Chinese herbal injections (CHIs) especially some tonic CHIs as adjuvant treatments for sepsis or septic shock have been widely used in China. Chinese herbal medicines, i.e., Chinese herbal injections, play an essential role in the treatment of sepsis or septic shock through multicomponent, multipathway, and multitargeting abilities and have been officially recommended for the management of COVID-19 (Guo et al., 2020; Shi et al., 2021). Several Chinese treatment guidelines for sepsis management and expert consensus have been successively released for the management of sepsis (Wang and Chai, 2017; Cao et al., 2018; Zhao et al., 2019). In these guidelines and consensus, CHIs are recommended as complementary therapies based on the conventional treatment for sepsis. Shenfu and Shengmai injections are typical herbal injections officially recommended for the management of COVID-19 when patients develop into systemic inflammatory

response syndrome (SIRS) and/or multiple organ dysfunction syndrome (MODS) (National Health Commission of the People's Republic of China, 2021). Research had found that combination of Shenfu injection with standard sepsis bundle therapy significantly improved patients' circulation, tissue perfusion, coagulation function, as well as inflammation reactions (Meiling Li et al. 2019). A metaanalysis including 17 RCTs and 860 patients with septic shock suggested that adding Shengmai injection to conventional Western medicine (WM) treatment further increased the effective rate (p < 0.0001) and reduced the blood lactate concentration at 12 h (p < 0.001), 24 h (p < 0.0001), and 72 h (p = 0.002) (Ha et al. 2019). Some studies have proved that tonic CHIs could effectively reduce the level of TNF-α, IL-6, PCT, and CRP in serum and improve the APACHE II score of patients (Pan, 2011; Qiu et al. 2012; Liu and Zhang, 2013; Cheng et al. 2018; Feng, 2019). At the same time, tonic CHIs are an effective immune-adjuvant measure for restoring monocyte immunosuppression by increasing CD4^{+} and CD4^{+}/CD8^{+} levels and decreasing 28-days mortality (Zhang Z. Y. et al. 2015; Zhang et al. 2017). However, the head-to-head clinical trials comparing the efficacy of the recommended tonic CHIs are lacking up to now. Without direct evidence, it is difficult to identify the most effective one for patients with sepsis or septic shock. As a new method of evidence-based medical statistical methods, network meta-analysis (NMA) extends principles of conventional meta-analysis to the evaluation of multiple treatments in a single analysis by combining the direct and indirect evidence (Higgins and Welton, 2015; Shim et al. 2017). Another major value of NMA is that it can rank each CHI according to its effectiveness, which is important for clinicians to make the best treatment choices. Therefore, this study aimed to assess the clinical efficacy and safety of different CHIs combined with WM and provide more evidence for rational selection of CHIs for sepsis or septic shock using NMA.

## MATERIALS AND METHODS

### Study Registration

This study had been prepared under the guidance of the Preferred Reporting Items for Systematic Review and Meta-Analysis (PRISMA) guidelines (in Attachment 1) (Page et al. 2021). And the study was prospectively registered on the PROSPERO platform (https://www.crd.york.ac.uk/PROSPERO/display_record.php?RecordID=254531) with an assigned registration number CRD42021254531.

### Ethics and Dissemination

All eligible studies were approved by local institutional review boards and ethical committees, and participants included were required to complete written informed consents, this study required no further ethical approval.

### Eligibility Criteria

The PICOS (participant, intervention, comparison, outcome, and study design) principle was applied in the study design.

### Type of Included Studies

RCTs regarding CHIs for the treatment of sepsis or septic shock were included for analysis. There were no limitations on language.

### Participants

Adults (aged 18 years or older) with sepsis or septic shock, which should be confirmed according to the diagnostic criteria (American College of Chest Physicians, 1992; Levy et al. 2003; Singer et al. 2016), patients with other critical diseases (tumor, pulmonary fibrosis, tuberculosis, and secondary respiratory failure of other systems) were excluded. No limitations existed in gender, race, or nationality.

### Intervention

The control groups were treated with one of CHIs combined with WM, or only conventional Western medicine (WM). The experimental groups were treated with different types of CHIs combined with WM.

### Outcomes

The primary outcome included Acute Physiology and Chronic Health Evaluation (APACHE II score). The secondary outcomes included 28-days mortality, procalcitonin (PCT), C-reactive protein (CRP), interleukin- 6 (IL-6), tumor necrosis factor-α (TNF-α), CD4^{+}, CD8^{+}, CD4^{+}/CD8^{+}, and adverse drug reactions or adverse drug events (ADRs/ADEs).

### Data Sources and Search Strategy

A comprehensive literature search was performed using the electronic databases of PubMed, the Cochrane Library, Embase, Web of Science, China National Knowledge Infrastructure (CNKI), SinoMed, Wanfang database, and the Chinese Scientific Journal database (VIP) from their inception up to September 1, 2021. The medical subject headings (MeSH) and free text words were used. Language restriction did not exist in this study. Furthermore, we manually searched the reference lists of all retrieved studies. Five different kinds of CHIs were included in this NMA: Shenfu injection, Shenmai injection, Shengmai injection, Shenqifuzheng injection, and Huangqi injection. Full details of the search strategy were shown in Attachment 2.

### Study Selection and Data Extraction

Two researchers (LXiao and LQ Niu) independently screened the studies according to the inclusion criteria. After checking for duplicate studies, the researchers eliminated reviews and irrelevant studies by reading the titles and abstracts. Then, full texts were read to select studies that met the prespecified inclusion criteria. Inconsistencies were resolved by extensive discussion or the third researcher (GW Li). A data spreadsheet was developed with Microsoft Excel 2019 to collect relevant information. The information including eligible studies characteristics (e.g. first author, year of publication), participants characteristics (e.g. gender, age, sample), details of interventions (e.g. duration, frequency of drugs), outcomes data and factors to evaluate risk of bias were extracted and entered into the spreadsheet.

### Quality Assessment

The methodological quality of each included study was evaluated with Revised Cochrane risk-of-bias tool for randomized trials (RoB 2) (Sterne et al. 2019). The domains include the following:

1) randomisation process; 2) deviations from intended interventions; 3) missing outcome data; 4) measurement of the outcome; 5) selection of the reported result. There are some signalling questions required to answer “Yes (Y)”, “Probably Yes (PY)”, “Probably No (PN)”, “No (N)”, or “No Information (NI)” for each domain. After that, the risk of bias is categorized into three levels: high risk, some concerns, and low risk. These domain-level judgements will inform an overall risk of bias judgment for the outcome. The quality assessments were performed by two independent reviewers (LXiao and LQ Niu), and disagreements were resolved by consensus or a third opinion.

### Statistical Analysis

OpenBUGS 3.2.3 and STATA 14.0 software (Stata Corporation, College Station, TX, United States) were employed to compute calculations and prepare graphs. For binary outcomes, the combined results were calculated as odds ratios (ORs) with 95% credible intervals (CIs). For continuous outcomes, if the scales of outcomes were uniform, mean differences (MD) with 95% CIs were used, otherwise, standardized mean differences (SMD) with 95% CIs were used. When the 95% CIs of ORs did not include one and the 95% CIs of the MDs or SMDs did not contain zero, the differences between the groups were considered statistically significant. The Chi-squared test was employed to assess heterogeneity between different studies (Zheng et al. 2019). If with homogeneity (p ≥ 0.1, I^{2} ≤ 50%), a fixed-effect model was adopted; If with obvious heterogeneity (p < 0.1, I^{2} > 50%), a random-effect model was applied and the sources of heterogeneity were explored by sensitivity analysis. If existed closed loops, the node-splitting approach was utilized to examine the consistency between direct and indirect evidence. If the p > 0.05 in the node-splitting approach, it indicated that the two sources were in agreement (Dias et al. 2010).

The Markov chain Monte Carlo method was performed by using the OpenBUGS software to carry out the NMA. In OpenBUGS software, the number of iterations was set to 300,000, and the first 100,000 iterations were used for the annealing algorithm to eliminate the impact of the initial value. The network graph was constructed using STATA software to show a comparative relationship between different interventions. Surface under the cumulative ranking curve (SUCRA) probability values were applied to rank the examined treatments, and the SUCRA values of 100 and 0% were assigned to the best and worst treatments, respectively (Salanti et al. 2011; Riley et al. 2017). After that, for each treatment comparison, the comparison-adjusted funnel plot were used to assess the presence of small-study effects and publication bias if more than 10 studies were included (Salanti et al. 2014).

### RESULTS

### Literature Selection

A total of 12,121 studies were identified from the search at first. After removing duplicates, there were 7,405 remained. By screening titles and abstracts, 7,008 studies were excluded because of reviews, irrelevant studies, and animal experiments. Afterward, 397 relevant studies were reviewed for eligibility by full-text evaluations. Finally, 50 studies that met the inclusion criteria were included in our Bayesian NMA. 347 records were excluded for the following reasons: 1) incorrect randomized method or observational studies (n = 62); 2) the use of irrelevant drugs (n = 13); 3) incorrect data or repeated data (n = 16); 4) no interested outcomes (n = 89); 5) duration of therapy or the time of outcomes measurements were not satisfied (n = 98); 6) no original papers (n = 15); (7) others (n = 54). The literature selection process was illustrated in Figure 1.

### Study Characteristics

The Bayesian NMA was performed using 50 RCTs with a total of 3,394 adult patients and their sample sizes varying from 40 to 157 participants. Only one study was three-arm trial and the remaining were double-arm trials. All studies were conducted in China and published between 2008 and 2021. Five tonic CHIs were investigated including Shenfu injection (SF, n = 24), Shenmai injection (SM, n = 12), Shengmai injection (SGM, n = 5), Shenqifuzheng injection (SQFZ, n = 6), and Huangqi injection (HQ, n = 4). The control groups had been treated with conventional Western medicine of sepsis or septic shock. On the basis of the control group, the intervention of the experimental group was one of the included CHIs. The duration of treatment ranged from 7 to 14 days and the time of outcome measurements was the seventh day or eighth day after treating. The details of the study characteristics were depicted in Table 1. And the compared connections among each intervention for each outcome were displayed in Figure 2.

### Quality Assessment

We used the Revised Cochrane risk-of-bias tool for randomized studies (RoB 2) to conduct a quality evaluation. Three studies were considered as low risk for the randomization process and four studies were assessed as high risk because of their incorrect method of random sequence generation. Although the remaining 43 studies utilized correct methods of random sequence generation, their allocation concealments were not obtainable. Hence, they were considered as some concerns in randomization process. All studies were rated to have low risk of bias for deviations from intended interventions, missing outcome data, and selection of the reported result. In addition, outcomes in this study were mostly objective indicators and the methods of outcomes measurements were reasonable, so the measurements of the outcomes were assessed as low risk in all studies. In summary, four studies (8%) were considered as high risk, and 43 studies (86%) were considered as some concerns, while only three studies (6%) were considered as low risk. Further details of the risk of bias assessment were shown in Figure 3.

### Primary Outcome

### APACHE II Score

A total of 29 studies (Chen, 2008; Huang et al. 2010; Ning, 2011; Pan, 2011; Qiu et al. 2012; Ai et al. 2013; Ren et al. 2014; Shen et al. 2014; Zheng and Pan, 2014; Zhou, 2014; Chen et al. 2015; Zhang Z. Y. et al. 2015; Huang, 2015; Yao, 2015; Cui and Dai,

![img-0.jpeg](img-0.jpeg)

FIGURE 1 | Flow diagram of study inclusion.

2016; Wang and Wu, 2016; Zhang, 2016; Jin et al., 2017; Lu et al., 2017; Zhang, 2017; Zhang et al., 2017; Zhu, 2017; Cheng et al., 2018; Ma et al., 2018; Feng, 2019; Li. X et al., 2019; Meiling Li et al., 2019; Zhang, 2019; Zhang and Zhang, 2019) that were compared to six treatments were included in this analysis. Shenfu injection combined with WM was used frequently to assess APACHE II score. There was significant heterogeneity among studies as shown in Table 2, so a random-effect model was employed to conduct network meta-analysis. As seen in Table 2, four CHIs investigated combined with WM were effective in improving APACHE II score except Shengmai injection when compared to WM alone: Huangqi vs. WM (MD = -5.80, 95% CI = -9.13 to -2.38); Shenqifuzheng vs. WM (MD = -4.72, 95% CI = -6.50 to -2.97); Shenmai vs. WM (MD = -3.10, 95% CI = -4.63 to -1.55); Shenfu vs. WM (MD = -2.49, 95% CI = -3.60 to -1.35). In addition, Shenqifuzheng combined with WM was more effective than Shenfu combined with WM (MD = -2.24, 95% CI = -4.35 to -0.16). Treatments ranking based on SUCRA values, which were shown in Figure 4 and Table 11, from largest to smallest, were as follows: Hangqi (91%), Shenqifuzheng (82.3%), Shenmai (52.8%), Shenfu (38.8%), Shengmai (32.8%) and WM (2.4%). Node splitting method results showed no inconsistency existing between direct and indirect evidence according to Supplementary Table S1. The funnel plot for APACHE II score was displayed in Figure 5 and showed significant asymmetry, which indicated possible publication bias.

### Secondary Outcomes

#### 28-days Mortality

13 studies (Zhang et al., 2011; Ren et al., 2014; Zheng and Pan, 2014; Zhou, 2014; Huang, 2015; Zhou et al., 2015; Cui and Dai, 2016; Huang, 2016; Lei and Li, 2016; Zhang et al., 2017; Zhu, 2017; Meiling Li et al., 2019; Zhang, 2019) with four treatments including Shenfu, Shengmai, Huangqi and WM alone reported the 28-days mortality. There was no heterogeneity among studies as shown in Table 3. Shenfu combined WM was more effective than WM alone (OR = 0.55, 95% CI = 0.37 to 0.78), while the results showed no significant difference in the remaining cases according to Table 3. Treatments ranking based on SUCRA values, which were shown in Figure 4 and Table 11, from largest to smallest, were as follows: Shenfu (74.8%), Shengmai (63.3%), Huangqi (43.5%) and WM (18.4%). Node splitting method results and funnel plot were shown in Supplementary Table S2 and Figure 5.

#### PCT

19 studies (Ai et al., 2013; Liu and Zhang, 2013; Ren et al., 2013; Qin, 2014; Chen et al., 2015; Huang, 2015; Xu et al., 2015; Wang

TABLE 1 | Characteristics of the studies included in this meta-analysis.

F) | Age(years) | APACHE II score | Therapy of experiment group | Therapy of control group | Course(day) | Outcomes  |

(Continued on following page)

TABLE 1 | (Continued) Characteristics of the studies included in this meta-analysis.


Note: (1)APACHE II score; (2)28-day mortality; (3)The level of PCT; (4)The level of CRP; (5)IL-6; (6)TNF- $\alpha$; (7)CD4 ${ }^{+}$; (8)CD8 ${ }^{+}$; (9)CD4 ${ }^{+}$/CD8 ${ }^{+}$; (10)ADRs/ADEs. and Wu, 2016; Zhou et al., 2016; Lu et al., 2017; Zhang and Wang, 2017; Zhu, 2017; Cheng et al., 2018; Liu et al., 2018; Liu and Yang, 2018; Yan, 2018; Zhang, 2019; Chen. T. F. et al., 2020; Pan and Chen, 2020) with six treatments reported the PCT. There was significant heterogeneity among studies as shown in Table 4. Three CHIs investigated combined with WM were effective in reducing the level of PCT when compared to WM alone: Shenmai vs. WM (SMD $=-2.44,95 \% \mathrm{CI}=-3.23$ to -1.65 ); Shengmai vs. WM (SMD $=-1.80,95 \% \mathrm{CI}=-2.87$ to -0.72 ); Shenfu vs. WM (SMD $=-1.62,95 \% \mathrm{CI}=-2.27$ to -0.98 ) according to Table 4. Treatments ranking based on SUCRA values, which were shown in Figure 4 and Table 11, from largest to smallest, were as follows: Shenmai (94.4\%), Shengmai (71.9\%), Shenfu (64.6\%), Shenqifuzheng (38\%), WM (17.4\%) and Huangqi (13.8\%). Node splitting method results and funnel plot were shown in Supplementary Table S3 and Figure 5.

## CRP

Seventeen studies (Qiu et al., 2012; Ai et al., 2013; Liu and Zhang, 2013; Ren et al., 2013; Qin, 2014; Chen et al., 2015; Xu et al., 2015; Wang and Wu, 2016; Lu et al., 2017; Zhu, 2017; Li, 2018; Liu and Yang, 2018; Feng, 2019; Zhang, 2019; Chen. T. F. et al., 2020; Pan and Chen, 2020; Li et al., 2021) with six treatments reported the CRP. There was significant heterogeneity among studies as shown in Table 5. Three CHIs investigated combined with WM were superior in reducing the level of CRP when compared to WM alone: Shenmai vs. WM (SMD $=-3.22,95 \% \mathrm{CI}=-4.02$ to -2.41 ); Shenqifuzheng vs. WM (SMD $=-2.66,95 \% \mathrm{CI}=-4.06$ to -1.26 ); Shengmai vs. WM (SMD $=-1.15,95 \% \mathrm{CI}=-2.25$ to -0.04 ) according to Table 5. What's more, based on WM, Shenmai and Shenqifuzheng had more excellent performance in decreasing CRP than Shenfu. Treatments ranking based on SUCRA values, which were shown in Figure 4 and Table 11, from largest to smallest, were as follows: Shenmai (94.8\%), Shenqifuzheng

![img-1.jpeg](img-1.jpeg)
(83.1\%), Shengmai (51.4\%), Huangqi (31.2\%), Shenfu (30.9\%) and WM (8.5\%). Node splitting method results and funnel plot were shown in Supplementary Table S4 and Figure 5.

## IL-6

IL-6 was estimated in 14 studies (Chen, 2008; Huang et al., 2010; Qiu et al., 2012; Ren et al., 2013; Zhang Z. Y. et al., 2015; Xu et al., 2015; Zhou et al., 2015; Wang et al., 2016; Jin et al., 2017; Cheng et al., 2018; Yan, 2018; Feng, 2019; Meiling Li et al., 2019; Li et al., 2021) with six treatments. There was significant heterogeneity among studies as shown in Table 6. Four CHIs investigated combined with WM were outstanding in decreasing the level of PCT when compared to WM alone: Shenfu vs. WM (SMD = -4.41, $95 \% \mathrm{CI}=-5.23$ to -3.59 ); Shengmai vs. WM (SMD = $-2.26,95 \%$ $\mathrm{CI}=-4.27$ to -0.24 ); Shenmai vs. WM (SMD = $-2.05,95 \% \mathrm{CI}=$
-3.21 to -0.89 ); Shenqifuzheng vs. WM (SMD = $-1.46,95 \% \mathrm{CI}=$ -2.89 to -0.02 ) according to Table 6. Treatments ranking based on SUCRA values, which were shown in Figure 4 and Table 11, from largest to smallest, were as follows: Shenfu (99.5\%), Shengmai (64.2\%), Shenmai (61.8\%), Shenqifuzheng (45.5\%), Huangqi (24.8\%) and WM (4.1\%). Funnel plot were shown in Figure 5.

## TNF- $\alpha$

Twenty studies (Chen, 2008; Huang et al., 2010; Liu and Zhang, 2013; Qin, 2014; Chen et al., 2015; Zhang Z. Y. et al., 2015; Xu et al., 2015; Zhou et al., 2015; Hu et al., 2016; Wang et al., 2016; Wang and Wu, 2016; Zhao et al., 2016; Jin et al., 2017; Cheng et al., 2018; Liu and Yang, 2018; Yan, 2018; Feng, 2019; Li et al., 2019; Li et al., 2021; Ning et al., 2012) with six treatments reported the TNF- $\alpha$. There was significant heterogeneity among studies as shown in Table 7. Four

![img-2.jpeg](img-2.jpeg)

CHIs investigated combined with WM were excellent in reducing the level of TNF-α when compared to WM alone: Shenfu vs. WM (SMD = -4.02, 95% CI = -4.85 to -3.20); Shengmai vs WM (SMD = -2.65, 95% CI = -3.66 to -1.65); Shenmai vs WM (SMD = -2.45, 95% CI = -3.26 to -1.63); Shenqifuzheng vs WM (SMD = -1.93, 95% CI = -3.36 to -0.50) according to

TABLE 2 | MDs with 95% CIs of APACHE II score. Significant effects are printed in bold.


Table 7. Treatments ranking based on SUCRA values, which were shown in Figure 4 and Table 11, from largest to smallest, were as follows: Shenfu ( $99.1 \%$ ), Shengmai ( $68.7 \%$ ), Shenmai ( $62.2 \%$ ), Shenqifuzheng ( $49.5 \%$ ), WM ( $16.8 \%$ ) and Huangqi ( $3.4 \%$ ). Funnel plot were shown in Figure 5.

## CD4 $^{+}$

Eleveen studies (Chen, 2008; Qiu et al., 2012; Ai et al., 2013; Shen et al., 2014; Chen et al., 2015; Zhang Z. Y. et al., 2015; Zhang and

Wang, 2017; Zhu, 2017; Li, 2018; Liu and Yang, 2018; Ma et al., 2018) with five treatments reported the CD4 ${ }^{+}$. There was significant heterogeneity among studies as shown in Table 8. Three CHIs investigated combined with WM were effective in increasing the level of $\mathrm{CD} 4^{+}$when compared to WM alone: Huangqi vs. WM (SMD $=1.92,95 \% \mathrm{CI}=0.21$ to 3.63 ); Shenqifuzheng vs. WM (SMD $=1.28,95 \% \mathrm{CI}=0.42$ to 2.14 ); Shenmai vs. WM (SMD $=1.26,95 \%$ $\mathrm{CI}=0.27$ to 2.25 ) according to Table 8. Treatments ranking based on SUCRA values, which were shown in Figure 4 and Table 11, ![img-3.jpeg](img-3.jpeg)

FIGURE 4 | Plot of SUCRA for all different outcomes. Note: (A): APACHE II score; (B): 28-days mortality; (C): PCT; (D): CRP; (E): IL-6; (F): TNF- $\alpha$; (G): CD4 ${ }^{+}$; (H): CD8 $^{+}$; (I): CD4 $^{+}$/CD8 ${ }^{+}$.

![img-4.jpeg](img-4.jpeg)

FIGURE 4 | (Continued)

from largest to smallest, were as follows: Huangqi (83.3%), Shenqifuzheng (62.1%), Shenmai (60.6%), Shenfu (42.5%), and WM (1.5%). Funnel plot were shown in Figure 5.

### CD8<sup>+</sup>

Ten studies (Chen, 2008; Qiu et al., 2012; Ai et al., 2013; Shen et al., 2014; Chen et al., 2015; Zhang Z. Y. et al., 2015; Zhu, 2017; Li, 2018; Liu and Yang, 2018; Ma et al., 2018) with five treatments reported the CD8<sup>+</sup>. There was significant heterogeneity among studies as shown in Table 9. Two CHIs investigated combined with WM were effective in improving the level of CD8<sup>+</sup> when compared to WM alone: Huangqi vs. WM (SMD = -2.77, 95% CI = -5.01 to -0.53); Shenqifuzheng vs. WM (SMD = -2.02, 95% CI = -3.60 to -0.43) according to Table 9. In addition, based on

![img-5.jpeg](img-5.jpeg)

**FIGURE 5 |** Funnel Plot. Note: **(A)** APACHE II score; **(B)** 28-days mortality; **(C)** PCT; **(D)** CRP; **(E)** IL-6; **(F)** TNF-α; **(G)** CD4^{+}; **(H)** CD8^{+}; **(I)** CD4^{+}/CD8^{+}.

WM, Huangqi and Shenqifuzheng had more excellent performance in decreasing CD8+ than Shenfu. Treatments ranking based on SUCRA values, which were shown in four and **Table 11**, from largest to smallest, were as follows: Huangqi (92.2%), Shenqifuzheng (78.7%), WM (49.3%), Shenfu (23%), and Shenmai (6.9%). Funnel plot were shown in **Figure 5**.

### **CD4+/CD8+**

Ten studies (Chen, 2008; Qiu et al., 2012; Ai et al., 2013; Shen et al., 2014; Chen et al., 2015; Zhang Z. Y. et al., 2015; Zhang and Wang, 2017; Zhu, 2017; Li, 2018; Ma et al., 2018) with five treatments reported the CD4+/CD8+. There was significant heterogeneity among studies as shown in **Table 10**. Two CHIs

![img-6.jpeg](img-6.jpeg)

FIGURE 5 | (Continued)

TABLE 3 | ORs with 95% CIs of 28-days mortality. Significant effects are printed in bold.


investigated combined with WM were effective in improving the CD4+/CD8+ when compared to WM alone: Huangqi vs. WM (MD = 0.86, 95% CI = 0.17 to 1.55); Shenqifuzheng vs. WM (MD = 0.38, 95% CI = 0.04 to 0.71) according to Table 10. Treatments ranking based on SUCRA values, which were shown in Figure 4 and Table 11, from largest to smallest, were as follows: Huangqi (93.6%), Shenmai (59.1%), Shenqifuzheng (55.9%), Shenfu (35.9%), and WM (5.4%). Funnel plot were shown in Figure 5.

### ADRs/ADEs

Among the included 50 RCTs, a total of six RCTs reported the ADRs/ADEs of CHIs. There were two studies (Zhang, 2019; Li et al., 2021) involved six participants in Shenfu group associated with ADRs/ADEs, including headache and dizziness (three cases in two studies), nausea and vomiting (two cases in one study), diarrhea (one case in one study). Two studies (Ren et al., 2013; Ren et al., 2014) reported ADRs/ADEs of Huangqi injection, both of them occurred one case of rash and one case of diarrhea. Another two studies (Qin, 2014; Zhang, 2019) with Shengmai injection reported two cases of ADRs/ADEs, one case of flatulence and one case of diarrhea. The rest of included studies did not provide information on any ADRs/ADEs. All of the symptoms were alleviated by rest or symptomatic treatment without affecting the RCTs' results.

### Sensitivity Analysis

There was significant heterogeneity between studies for the primary outcome. Hence, a sensitivity analysis was conducted for the outcome of APACHE II score. After omitting six studies (Chen, 2008; Pan, 2011; Ai et al., 2013; Shen et al., 2014; Wang and Wu, 2016; Zhang and Zhang, 2019), the I^{2} values for standard pairwise meta-analysis were reduced obviously and all less than 50% according to Table 12. The remaining 23 studies were conducted a network meta-analysis again. The pooled MD and SUCRA value of Huangqi injection were changed significantly,

TABLE 4 | SMDs with 95\% CIs of PCT. Significant effects are printed in bold.


TABLE 5 | SMDs with 95\% CIs of CRP. Significant effects are printed in bold.


TABLE 6 | SMDs with 95\% CIs of IL-6. Significant effects are printed in bold.


TABLE 7 | SMDs with 95\% CIs of TNF- $\alpha$. Significant effects are printed in bold.


TABLE 8 | SMDs with 95\% CIs of CD4 ${ }^{+}$. Significant effects are printed in bold.


TABLE 9 | SMDs with 95\% CIs of CD8 ${ }^{+}$. Significant effects are printed in bold.


TABLE 10 | SMDs with 95\% CIs of CD4 ${ }^{+}$/CD8 ${ }^{+}$. Significant effects are printed in bold.


TABLE 11 | SUCRA results of the outcomes.


TABLE 12 | MDs with 95\% CIs of APACHE II score. Significant effects are printed in bold.


while the rest CHIs were slightly modified when the individual study data were removed, one at a time, from any pairwise comparison analysis. The Bayesian ranking results of sensitivity analysis from largest to smallest were Shenqifuzheng (95.65\%), Shenmai (74\%), Shenfu (47.1\%), Shengmai (35.3\%), Huangqi (33.2\%) and WM (3.4\%), respectively.

## DISCUSSION

A total of 50 studies involving 3,394 participants were included. Five tonic CHIs were identified in the treatment of sepsis or septic shock, including Shenfu injection, Shenmai injection, Shengmai injection, Shenqifuzheng injection, and Huangqi injection. According to the results of this NMA and sensitivity analysis, four CHIs including Shenqifuzheng injection, Shenmai injection, Shenfu injectuion and Shengmai injection combined with WM had a superior effect in improving the APACHE II score than WM alone and the differences were statistically significant. Based on sensitivity analysis and SUCRA values, Shenqifuzheng injection (95.65\%) combined with WM ranked highest, followed by Shenmai injection (74\%), Shenfu injection (47.1\%), Shengmai injection (35.3\%) and Huangqi injection (33.2\%). Among the secondary outcomes, Shenmai injection

was the most favorable intervention in reducing PCT and CRP levels, and Shenqifuzheng injection was the second favorable intervention in reducing CRP level. Shenfu injection combined with WM was more effective than the other treatments in decreasing the serum IL-6 and TNF-α levels and lowering the 28-days mortality. Regarding the improvement of immune function, Shenqifuzheng injections had obvious advantages.

As for safety, a total of six RCTs reported the ADRs/ADEs of CHIs, including two studies of Shenfu injection, two studies of Huangqi injection, and two studies of Shengmai injection. The ADRs/ADEs mainly involved headache, dizziness, nausea, vomiting, diarrhea, rash, and flatulence. Though all the ADRs/ADEs were mild and can be relieved by themselves, no studies reported the rate of ADRs/ADEs comparing CHIs combined with WM and WM alone. Hence, we could not draw a certain conclusion that combing CHIs with WM will not increase the ADRs/ADEs of the patients. Hopefully, further studies especially clinical trials should pay more attention to these ADRs/ADEs of CHIs and more studies are needed to determine the safety of CHIs combined with WM for sepsis.

The pathophysiology of sepsis is extremely complex. The causative pathogen produces an excessive inflammatory response with high levels of anti-inflammatory cytokines. These high levels of anti-inflammatory cytokines are associated with ICU admission and mortality. Finally, the early proinflammatory state in sepsis often develops into a later and prolonged state of immune system dysfunction over time (Gotts and Matthay, 2016).

Our study has found that Shenqifuzheng injection combined with WM had obvious advantages in improving APACHE II score, reducing CRP level, and especially enhancing immune function. Shenqifuzheng injection is a well-known Chinese traditional medicine to invigorate “Qi” and strengthen health, which is made of Codonopsis pilosula and Astragali Radix. The main active component of Codonopsis pilosula is Codonopsis pilosula polysaccharide. The related studies have demonstrated that polysaccharide isolated from Codonopsis pilosula have obvious immune-modulation effects (Zheng et al., 2014; Fu et al. 2018; Zou et al. 2019). Moreover, the polysaccharide could exhibit anti-inflammatory effect against lipopolysaccharide (LPS) induced RAW264.7 cells in vitro and in vivo and reduce the expression of inflammatory factors (Meng et al. 2020). Astragali Radix contains numerous natural products with different structural patterns and the main active constituents are astragalus polysaccharides, astragalus saponins and astragalus flavonoids. These main active constituents have shown considerable immunomodulatory properties both in vitro and in vivo (Gong et al. 2018; Chen Z. et al. 2020).

Another result of this study suggested that Shenfu injection combined with WM exhibited a better performance in reducing 28-days mortality and inhibiting inflammatory indicators, which were consistent with previous meta-analysis (Huang et al. 2019; Yu et al. 2019; Zhao et al. 2020). Shenfu injection is composed with Radix Ginseng Rubra and Radix Aconiti Lateralis Praeparata, which has great effect of restoring “Yang” from collapse and tonifying “Qi” for relieving desertion. Ginsenoside and aconitine are the main active ingredients in Shenfu injection. Modern pharmacological research shows that ginsenoside can suppress production of multiple inflammatory mediators such as TNF-α, interleukin (IL)-1β, IL-6, cyclooxygenase-2 (COX-2) and inducible nitric oxide synthase (iNOS) in Lipopolysaccharide (LPS)-stimulated cells, inhibit LPS-induced in body temperature, serum TNF-α, IL-1β, IL-6, COX-2, iNOS in rats, attenuate lethal sepsis, and protect mice from death in a mouse model of endotoxin shock (Su et al. 2012; Su et al. 2015). In addition, ginsenoside has dual roles in regulation of the immune responses: up-regulation of the immune responses and down-regulation of the proinflammatory response (Sun et al. 2008). Evidence has also revealed that aconitine has the effects of anti-inflammation and regulating the immune function. Researches have found that aconitine could partly inhibit the proliferation and NO production in LPS-induced RAW264.7 cells and showed anti-inflammatory effect by inhibiting macroscopic pathology and histological inflammation (Mi et al. 2021).

There are three advantages that could enhance the prestige of this study. First, to the best of our knowledge, this is the first NMA to compare the effects of different CHIs and rank them for the treatment of sepsis or septic shock. Secondly, these results may be helpful to clinicians to make a better choice for the treatment of sepsis or septic shock. Additionally, the inclusion and exclusion criteria were strictly established.

### Limitations

This study also has some limitations. First, all studies except one were published in China, and the data of clinical studies in other languages was lacking. Second, the qualities of included studies in this study were not high. Only three studies mentioned the method of allocation concealment. Third, there was a lack of large-sample direct comparisons between the two injections. The difference among the sample sizes of different injections would also reduce the strength of evidence for the results.

### CONCLUSION

In conclusion, Shenqifuzheng injection was the optimum treatment regimen to improve APACHE II score, reduce CRP level, and regulate immune function. Shenfu injection was superior in reducing the expression of inflammatory factors and decreasing 28-days mortality. Nevertheless, more multicenter, diverse, and direct comparisons RCTs are needed to further confirm the results.

### DATA AVAILABILITY STATEMENT

The original contributions presented in the study are included in the article/Supplementary Material, further inquiries can be directed to the corresponding authors.

### AUTHOR CONTRIBUTIONS

LX: Conceptualization, Methodology, Software, Formal analysis and Quality assessment, Investigation, Resources, Data Curation,

Writing-Original draft preparation, review and editing, Visualization. LN: Conceptualization, Methodology, Validation, Formal analysis and Quality assessment, Investigation, Data Curation, Writing-Original review and editing, Visualization. XX: Writing, revising and editing the review. YZ: Investigation, Resources, Data Curation, Software. GL: Methodology, Validation, Data Curation, Quality assessment, Writing-Original review and editing, Supervision. XL: WritingOriginal review and editing, Supervision, Project administration. LY: Software, Resources, Writing-Original draft preparation, review, and editing. All data were generated in-house, and no paper mill was used. All authors listed have made a substantial, direct and intellectual contribution to the work, and approved it for publication.

## FUNDING

This work is supported by the Key Projects in the National Science and Technology Pillar Program during the Twelfth

## ACKNOWLEDGMENTS

We thank the support of the Key Projects in the National Science and Technology Pillar Program during the Twelfth Five-year Plan Period and the Development Fund for Emergency Discipline in First Teaching Hospital of Tianjin University of Traditional Chinese Medicine.

## SUPPLEMENTARY MATERIAL

The Supplementary Material for this article can be found online at: https://www.frontiersin.org/articles/10.3389/fphar.2022.830030/ full\#supplementary-material

De Waele, JJ., Akova, M., Antonelli, M., Canton, R., Carlet, J., De Backer, D., et al. (2018). Antimicrobial Resistance and Antibiotic Stewardship Programs in the ICU: Insistence and Persistence in the Fight against Resistance. A Position Statement from ESICM/ESCMID/WAAAR Round Table on Multi-Drug Resistance. Intensive Care Med. 44 (2), 189-196. doi:10.1007/s00134-017-5036-1
Dias, S., Welton, N. J., Caldwell, D. M., and Ades, A. E. (2010). Checking Consistency in Mixed Treatment Comparison Meta-Analysis. Stat. Med. 29 (7-8), 932-944. doi:10.1002/sim. 3767
Evans, L., Rhodes, A., Alhazzani, W., Antonelli, M., Coopersmith, C. M., French, C., et al. (2021). Surviving Sepsis Campaign: International Guidelines for Management of Sepsis and Septic Shock 2021. Crit. Care Med. 49 (11), e1063-e1143. doi:10.1097/ccm. 0000000000005337
Fan, T. T., Cheng, B. L., Fang, X. M., Chen, Y. C., and Su, F. (2020). Application of Chinese Medicine in the Management of Critical Conditions: A Review on Sepsis. Am. J. Chin. Med. 48 (6), 1315-1330. doi:10.1142/s0192415x20500640
Fang, F., Zhang, Y., Tang, J., Lunsford, L. D., Li, T., Tang, R., et al. (2019). Association of Corticosteroid Treatment with Outcomes in Adult Patients with Sepsis: A Systematic Review and Meta-Analysis. JAMA Intern. Med. 179 (2), 213-223. doi:10.1001/jamainternmed.2018.5849
Feng, G. (2019). Clinical Effect and Influence on Lac, Nse and Protein S100 $\beta$ of Shenmai Injection in the Treatment of Sepsis. J. Med. Theor. Prac 32 (08), 1178-1180. doi:10.19381/j.issn.1001-7585.2019.08.034
Fu, Y. P., Feng, B., Zhu, Z. K., Feng, X., Chen, S. F., Li, L. X., et al. (2018). The Polysaccharides from Codonopsis Pilosula Modulates the Immunity and Intestinal Microbiota of Cyclophosphamide-Treated Immunosuppressed Mice. Molecules 23 (7), 1801. doi:10.3390/molecules23071801
Gong, A. G. W., Duan, R., Wang, H. Y., Kong, X. P., Dong, T. T. X., Tsim, K. W. K., et al. (2018). Evaluation of the Pharmaceutical Properties and Value of Astragali Radix. Medicines (Basel) 5 (2), 46. doi:10.3390/medicines5020046
Gotts, J. E., and Matthay, M. A. (2016). Sepsis: Pathophysiology and Clinical Management. Bmj 353, i1585. doi:10.1136/bmj.i1585
Guo, H., Zheng, J., Huang, G., Xiang, Y., Lang, C., Li, B., et al. (2020). Xuebijing Injection in the Treatment of COVID-19: a Retrospective Case-Control Study. Ann. Palliat. Med. 9 (5), 3235-3248. doi:10.21037/apm-20-1478
Ha, Y. X., Wang, X. P., Huang, P., Zhang, R., Xu, X. L., Li, B., et al. (2019). Effect of Shengmai Injection on Septic Shock, a Systematic Review and Meta-Analyse. J. Emerg. Tradit Chin. Med. 28 (11), 1893-1898+1915. doi:10.3969/j.issn.1004745X.2019.11.004
Higgins, J. P., and Welton, N. J. (2015). Network Meta-Analysis: a Norm for Comparative Effectiveness? Lancet 386 (9994), 628-630. doi:10.1016/s0140-6736(15)61478-7

Hu, D. C., Liu, Y., and Xu, H. F. (2016). Clinical Effect of Shengmai Injection Combined with Conventional Western Medicine in the Treatment of Septic Shock. J. New Chin. Med. 48 (11), 14-15. doi:10.13457/j.cnki.jncm.2016.11.007 Huang, M. H. (2015). Clinical Observation of Senile Severe Sepsis Intervened by Shenfu Injection in the Acute Deficiency.
Huang, P., Guo, Y., Feng, S., Zhao, G., Li, B., and Liu, Q. (2019). Efficacy and Safety of Shenfu Injection for Septic Shock: A Systematic Review and Meta-Analysis of Randomized Controlled Trials. Am. J. Emerg. Med. 37 (12), 2197-2204. doi:10. 1016/j.ajem.2019.03.032
Huang, X. X. (2016). Applications PiCCO Assessment of Hemodynamic Effects and Prognosis in Patients with Septic Shock Using the Shenfu Injection.
Huang, Z. F., Fang, C., Huang, X. Z., and Mei, H. Q. (2010). Effect of Shenmai (SM) Injection on the Release of Serum Inflammatory Mediators in Patients with Sepsis. Chin. Arch. Tradit Chin Med 28 (12), 2601-2603. doi:10.13193/j. archtcm.2010.12.139.huangzf. 054
Jin, L. N., Xu, H. H., and Cao, Z. Q. (2017). Clinical Effect of Shenqifuzheng Injection in the Treatment of Septic Shock. Chin. Community Doctors 24 (9), 34-35. doi:10.3969/j. issn.1006-5180.2017.09.020
Keh, D., Trips, E., Marx, G., Wirtz, S. P., Abduljawwad, E., Bercker, S., et al. (2016). Effect of Hydrocortisone on Development of Shock Among Patients with Severe Sepsis: The HYPRESS Randomized Clinical Trial. Jama 316 (17), 1775-1785. doi:10.1001/jama.2016.14799
Kuttab, H. I., Lykins, J. D., Hughes, M. D., Wroblewski, K., Keast, E. P., Kukoyi, O., et al. (2019). Evaluation and Predictors of Fluid Resuscitation in Patients with Severe Sepsis and Septic Shock. Crit. Care Med. 47 (11), 1582-1590. doi:10. 1097/ccm.0000000000003960
Lei, X. Y., and Li, Y. X. (2016). Effects of Shenfu Injection on Liver Function in Patients with Septic Shock in ICU. Asia-pac Trad Med. 12 (05), 135-136. doi:10. 11954/ytctyy.201605059
Levy, M. M., Fink, M. P., Marshall, J. C., Abraham, E., Angus, D., Cook, D., et al. (2003). 2001 SCCM/ESICM/ACCP/ATS/SIS International Sepsis Definitions Conference. Intensive Care Med. 29 (4), 530-538. doi:10.1007/s00134-003-1662-x
Li, M., Pan, T., Lyu, L., Zhang, W., Tan, R., Liu, Z., et al. (2019). Effect of Traditional Chinese Medicine Syndrome Differentiation and Standard Bundle Therapy in Patients with Septic Shock. Zhonghua Wei Zhong Bing Ji Jiu Yi Xue 31 (7), 852-856. doi:10.3760/cma.j.issn.2095-4352.2019.07.011
Li, P. (2018). Clinical Effect of Shenqifuzheng Injection in the Treatment of Severe Sepsis. Chin. Community Doctors 25 (10), 41-42. doi:10.3969/j.issn.1006-5180.2018.10.023
Li, X. X., Chen, L., Wang, D. M., and Chen, Y. (2019). Effectiveness of Shenfu Injection in the Treatment of Sepsis in Intensive Care Unit. Chin. Foreign Med. Res. 17, 36-37. doi:10.14033/j.cnki.cfmr.2019.14.015
Li, X. X., Shan, Y. H., Luo, S. Y., and Wang, L. Y. (2021). The Influences on Inflammatory Mediators and Hemodynamics of Shenfu Injection Combined with Tigecycline in the Treatment of Septic Shock. Clin. Med 41, 118-120. doi:10.19528/j.issn.1003-3548.2021.02.048
Liu, L. Q., and Zhang, W. W. (2013). Study of Shengmai Injection Intervention of Serum CRP, PCT and TNF- $\alpha$ in Patients with Septic Shock. Chin. Mod. Doctor 51 (17), 88-90.
Liu, P. F., and Yang, T. (2018). Effect of Shenfu Injection as an Adjuvant Therapy in the Treatment of Patients with Septic Shock and the Influence on Immune Modulation. Tianjin Pharm. 30, 33-35. doi:10.3969/j.issn.1006-5687.2018.04.012
Liu, Y., Liu, C., Li, H. Y., and Wang, H. Y. (2018). Effects of Shenfu Injection Combined with Low-Dose Hydrocortisone on Plasma Levels of HLA-DR and PCT in Patients with Septic Multiple Organ Dysfunction Syndrome. Chin. J. Gerontol. 38 (06), 1407-1410. doi:10.3969/j.issn.1005-9202.2018.06.054

Lu, D., Yu, G. F., Lv, T., and Ying, L. J. (2017). Effect of Shenmai Injection with Hemoperfusion on Hemodynamics and Tissue Perfusion in Septic Shock. Chin Gen. Prac 20 (34), 4322-4325+4330. doi:10.3969/j.issn.1007-9572.2017.34.021
Ma, J. Q., Zheng, Z., Jiang, L., and Wang, Y. H. (2018). The Influence of Shenqi Fuzheng Injection on Peripheral Blood Lymphocyte Subsets and Prognosis of Patients with Sepsis. Shaanxi J. Tradit Chin. Med. 39 (03), 365-367. doi:10. 3969/j.issn.1000-7369.2018.03.029
Marston, H. D., Dixon, D. M., Knisely, J. M., Palmore, T. N., and Fauci, A. S. (2016). Antimicrobial Resistance. Jama 316 (11), 1193-1204. doi:10.1001/jama.2016.11764
Meng, Y., Xu, Y., Chang, C., Qiu, Z., Hu, J., Wu, Y., et al. (2020). Extraction, Characterization and Anti-inflammatory Activities of an Inulin-type Fructan from Codonopsis Pilosula. Int. J. Biol. Macromol 163, 1677-1686. doi:10.1016/j. ijbiomac.2020.09.117

Mi, L., Li, Y.-C., Sun, M.-R., Zhang, P.-L., Li, Y., and Yang, H. (2021). A Systematic Review of Pharmacological Activities, Toxicological Mechanisms and Pharmacokinetic Studies on Aconitum Alkaloids. Chin. J. Nat. Medicines 19 (7), 505-520. doi:10.1016/s1875-5364(21)60050-x

National Health Commission of the People's Republic of China (2021). Diagnosis and Treatment Plan for COVID-19 (Trial Version 8 Revision). Chin. J. Clin. Infect. Dis. 14 (02), 81-88. doi:10.3760/cma.j.issn.1674-2397.2021.02.001
Ning, X. P. (2011). The Protection Effects of Shenmai Injection on Sepsis Patient. Hebei Med. 17 (06), 789-791. doi:10.3969/j.issn.1006-6233.2011.06.030
Ning, X. P., Wang, J. L., He, D. Y., Jiang, L., and Wang, T. (2012). The Influence of Shenmai Injection to Serum Cell Factor and Allergic C-reactive Protein of Sepsis Patients. Chin Mod Med 19 (18), 78-79. doi:10.3969/j.issn.1674-4721.2012.18.039
Page, M. J., McKenzie, J. E., Bossuyt, P. M., Boutron, I., Hoffmann, T. C., Mulrow, C. D., et al. (2021). The PRISMA 2020 Statement: an Updated Guideline for Reporting Systematic Reviews. Bmj 372, n71. doi:10.1136/bmj.n71
Pan, X. N. (2011). Clinical Efficacy Observation with Fu-Zheng-Gu-Ben on Septic Acute Deficiency Syndrome Patients. Master's thesis. Dalian(China): Dalian Medical University.
Pan, Y., and Chen, X. Q. (2020). Application Value of Shenfu Injection in the Treatment of Septic Shock. Chin. Foreign Med. Res. 18 (27), 47-48.
Perner, A., Cecconi, M., Cronhjort, M., Darmon, M., Jakob, S. M., Pettilä, V., et al. (2018). Expert Statement for the Management of Hypovolemia in Sepsis. Intensive Care Med. 44 (6), 791-798. doi:10.1007/s00134-018-5177-x
Prescott, H. C., and Angus, D. C. (2018). Postsepsis Morbidity. Jama 319 (1), 91. doi:10.1001/jama.2017.19809
Qin, H. F. (2014). Curative Effect of Shengmai Injection in the Treatment of Septic Shock. Chin. Med. Herald, 86-89.
Qiu, Z. L., Ye, Y. P., Zhang, N., Zhang, J., Xu, J. L., and Lou, T. Z. (2012). Effects of Shenfu Injection on the Modulation of Immunity in Patients with Severe Sepsis: A Prospective Clinical Trial. Chin. Arch. Tradit Chin Med 30 (02), 363-366. doi:10.13193/j.archtcm.2012.02.141.ajuzl.024
Reinhart, K., Daniels, R., Kissoon, N., Machado, F. R., Schachter, R. D., and Finfer, S. (2017). Recognizing Sepsis as a Global Health Priority - A WHO Resolution. N. Engl. J. Med. 377 (5), 414-417. doi:10.1056/NEJMp1707170

Ren, Y., Dai, Y. F., Yin, X., Wu, S. X., Guo, L. H., and Zhang, M. Z. (2013). Clinical Efficacy of Benefiting Qi for Strengthening Resistance on Sepsis and Inflammatory Reaction: A Clinical Observation of 30 Cases. Guid J. Tradit Chin. Med. Pharm. 19 (08), 26-28+31. doi:10.3969/j.issn.1672-951X.2013.08.013

Ren, Y., Wu, S. X., Yin, X., Guo, L. H., and Zhang, M. Z. (2014). A Clinical Study of Improvement of Immunologic Function in Patients with Old Age Sepsis Treated by astragalus Injection. Chin. J. TCM WM Crit. Care 5, 323-327. doi:10.3969/j.issn.1008-9691.2014.05.002
Riley, B. D., Jackson, D., Salanti, G., Burke, D. L., Price, M., Kirkham, J., et al. (2017). Multivariate and Network Meta-Analysis of Multiple Outcomes and Multiple Treatments: Rationale, Concepts, and Examples. Bmj 358, j3932. doi:10.1136/bmj.j3932
Rochwerg, B., Oczkowski, S. J., Siemieniuk, R. A. C., Agoritsas, T., Belley-Cote, E., D'Aragon, F., et al. (2018). Corticosteroids in Sepsis: An Updated Systematic Review and Meta-Analysis. Crit. Care Med. 46 (9), 1411-1420. doi:10.1097/ ccm.0000000000003262
Sale, Y., Rubatto Bieri, P. N., Kotlis, K., Nanchal, R., Shah, B., Kluge, S., et al. (2017). Higher Fluid Balance Increases the Risk of Death from Sepsis: Results from a Large International Audit. Crit. Care Med. 45 (5), 386-394. doi:10.1097/ccm.0000000000002189
Salanti, G., Ades, A. E., and Ioannidis, J. P. (2011). Graphical Methods and Numerical Summaries for Presenting Results from Multiple-Treatment Meta-Analysis: an Overview and Tutorial. J. Clin. Epidemiol. 64 (2), 163-171. doi:10.1016/j.jclinepi.2010.03.016
Salanti, G., Del Giovane, C., Chaimani, A., Caldwell, D. M., and Higgins, J. P. (2014). Evaluating the Quality of Evidence from a Network Meta-Analysis. PLoS One 9 (7), e99682. doi:10.1371/journal.pone. 0099682
Seymour, C. W., Gesten, F., Prescott, H. C., Friedrich, M. E., Iwashyna, T. J., Phillips, G. S., et al. (2017). Time to Treatment and Mortality during Mandated Emergency Care for Sepsis. N. Engl. J. Med. 376 (23), 2235-2244. doi:10.1056/ NEJMoa1703058
Shen, L. M., Du, Q. S., and Zhao, H. L. (2014). The Effects on Immune Function of Shenmai Injection in the Treatment of Sepsis. Chin. J. Clinical Rational Drug Use 7 (01), 67-68. doi:10.15887/j.cnki.13-1389/r.2014.01.141
Shi, N., Guo, L., Liu, B., Bian, Y., Chen, R., Chen, S., et al. (2021). Efficacy and Safety of Chinese Herbal Medicine versus Lopinavir-Ritonavir in Adult Patients with

Coronavirus Disease 2019: A Non-randomized Controlled Trial. Phytomedicine 81, 153367. doi:10.1016/j.phymed.2020.153367
Shim, S., Yoon, B. H., Shin, I. S., and Bae, J. M. (2017). Network Meta-Analysis: Application and Practice Using Stata. Epidemiol. Health 39, e2017047. doi:10. 4178/epih.e2017047
Singer, M., Deutschman, C. S., Seymour, C. W., Shankar-Hari, M., Annane, D., Bauer, M., et al. (2016). The Third International Consensus Definitions for Sepsis and Septic Shock (Sepsis-3). Jama 315 (8), 801-810. doi:10.1001/jama. 2016.0287

Sterne, J. A. C., Savović, J., Page, M. J., Elbers, R. G., Blencowe, N. S., Boutron, I., et al. (2019). RoB 2: a Revised Tool for Assessing Risk of Bias in Randomised Trials. Bmj 366, 14898. doi:10.1136/bmj. 14898
Su, F., Xue, Y., Wang, Y., Zhang, L., Chen, W., and Hu, S. (2015). Protective Effect of Ginsenosides Rg1 and Re on Lipopolysaccharide-Induced Sepsis by Competitive Binding to Toll-like Receptor 4. Antimicrob. Agents Chemother. 59 (9), 5654-5663. doi:10.1128/aac.01381-15
Su, F., Yuan, L., Zhang, L., and Hu, S. (2012). Ginsenosides Rg1 and Re Act as Adjuvant via TLR4 Signaling Pathway. Vaccine 30 (27), 4106-4112. doi:10. 1016/j.vaccine.2012.03.052
Sun, J., Song, X., and Hu, S. (2008). Ginsenoside Rg1 and Aluminum Hydroxide Synergistically Promote Immune Responses to Ovalbumin in BALB/c Mice. Clin. Vaccin. Immunol 15 (2), 303-307. doi:10.1128/cvi.00448-07
Venkatesh, B., Finfer, S., Cohen, J., Rajbhandari, D., Arabi, Y., Bellomo, R., et al. (2018). Adjunctive Glucocorticoid Therapy in Patients with Septic Shock. N. Engl. J. Med. 378 (9), 797-808. doi:10.1056/NEJMoa1705835
Wang, L., Chai, Y., Wang, L., and Chai, Y. (2017). Chinese Emergency Medicine Expert Consensus on Diagnosis and Treatment of Sepsis Complicated with Disseminated Intravascular Coagulation. Zhonghua Wei Zhong Bing Ji Jiu Yi Xue 29 (7), 577-580. doi:10.3760/cma.j.issn.2095-4352.2017.07.001
Wang, S., and Wu, J. Y. (2016). Effects of Shenfu Injection on Serum Levels of CRP, PCT and TNF- $\alpha$ in Patients with Elderly Acute Sepsis. Chin. J. Gerontol. 36 (17), 4307-4308. doi:10.3969/j.issn.1005-9202.2016.17.086
Wang, Y. F., Zeng, J., Fu, J., Xu, H. D., and Luo, J. R. (2016). Influence of Shengmai Injection for the Oxygen Metabolism and Serum Cytokines of Patients with Infectious Shock. Chin. J. Nosocomial 26, 5421-5423. doi:10.11816/cn.nj.2016161995
Xu, X. Y., Zhang, C. H., and Qu, X. G. (2015). 40 Cases of Sepsis Treated with Shenmai Injection by Continuous Intravenous Pumping. Shandong Med. J 55 (35), 43-45. doi:10.3969/j.issn.1002-266X.2015.35.015

Yan, Z. J. (2018). Clinical Effects and Incluence on Hemodynamics Indexes and the Levels of Inflammatory Factors of Shenfu Injection Combined with Antibiotics in the Treatment of Patients with Septic Shock in Intensive Care Units. Anti Infect. Pharm. 15 (5), 832-834+920. doi:10.13495/j.issn.1672-7878.2018.05-036
Yao, S. (2015). The Effects of Shenfu Injection on Systemic Circulation, Oxygen Metabolism and Prognosis for Patients with Septic Shock. Shenzhen J. Integr. Tradit Chin. West. Med. 25 (24), 23-25. doi:10.16458/j.cnki.1007-0893.2015.24.011
Yu, H., Wang, Y. B., Zhen, J. H., Cao, B. B., and Zhang, J. M. (2019). Meta-analysis of Clinical Effects of Shenfu Injection on Septic Patients. J. Emerg. Tradit Chin. Med. 28 (01), 29-33. doi:10.3969/j.issn.1004-745X.2019.01.008
Zhang, D., Micek, S. T., and Kollef, M. H. (2015). Time to Appropriate Antibiotic Therapy Is an Independent Determinant of Postinfection ICU and Hospital Lengths of Stay in Patients with Sepsis. Crit. Care Med. 43 (10), 2133-2140. doi:10.1097/ccm. 0000000000001140
Zhang, J. L., and Zhang, Y. F. (2019). Effects on Organs Function of Patients with Severe Sepsis Early Treated by Shenfu Injection. Mod. J. Integr. Tradit Chin. West. Med. 28 (09), 994-996+1013. doi:10.3969/j.issn.1008-8849.2019.09.023
Zhang, L. (2016). The Application Value of Shenmai Injection in the Treatment of Patients with Septic Shock. Zhejiang J. Tradit Chin. Med. 51 (12), 922-923. doi:10.3969/j.issn.0411-8421.2016.12.048
Zhang, N., Liu, J., Qiu, Z., Ye, Y., Zhang, J., and Lou, T. (2017). Shenfu Injection for Improving Cellular Immunity and Clinical Outcome in Patients with Sepsis or Septic Shock. Am. J. Emerg. Med. 35 (1), 1-6. doi:10.1016/j.ajem.2016.09.008
Zhang, N., Qiu, Z. L., Ye, Y. P., Xu, J. L., Lou, T. Z., and Lei, H. X. (2011). Influence of Shenfu Injection on Inflammatory Cytokines and Prognosis in Patients with Severe Sepsis. Chin. Arch. Tradit Chin Med 29 (03), 525-527. doi:10.13193/j. archtcm.2011.03.79.zhangn. 082
Zhang, S. Y. (2017). Clinical Observation of Shenfu Injection to Improve Septic Shock. Drugs and Clinic 32, 1034-1038. doi:10.7501/j.issn.1674-5515.2017.06.017

Zhang, W. M., and Wang, Y. X. (2017). The Curative Efect Analysis of Shenmai Injection in the Treatment of Patients with Septic Shock and its Effect on Cellular Immune Function. IMHGN 23 (20), 3228-3231.
Zhang, X. S. (2019). Clinical Observation on the Therapeutic Effect of Fu-Zheng-Gu-Ben Method in Treating Sepsis. MS thesis. Guangzhou: Guangzhou University of Chinese Medicine.
Zhang, Z. Y., You, S. Y., Yu, L. C., Ma, T., and Yang, B. J. (2015). Effects of Shenqi Fuzheng Injection on Immune Function in Patients with Sepsis. Chin. J. TCM WM Crit. Care 22, 276-280. doi:10.3969/j.issn.1008-9691.2015.03.012
Zhao, G. Z., Chen, R. B., Li, B., Guo, Y. H., Xie, Y. M., Liao, X., et al. (2019). Clinical Practice Guideline on Traditional Chinese Medicine Therapy Alone or Combined with Antibiotics for Sepsis. Ann. Transl Med. 7 (6), 122. doi:10. 21037/atm.2018.12.23
Zhao, L. Y., Liu, Q. J., and Zhao, F. L. (2020). Meta-analysis of the Influence of Shenfu Injection on Inflammatory Markers in the Treatment of Septic Shock. J. Emerg. Tradit Chin. Med. 29 (11), 1916-1920. doi:10.3969/j.issn.1004-745X.2020.11.010
Zhao, X. F., Li, Q. B., Ge, X. L., and Zhang, P. P. (2016). The Influence of astragalus on Injection Inflammatory Mediators and Clinical Effect in Elderly Patients with Septic Shock. Chin. J. Crit. Care Med. 36, 1137-1140. doi:10.3969/j.issn. 1002-1949.2016.12.019
Zheng, H., Chen, Q., Chen, M., Wu, X., She, T. W., Li, J., et al. (2019). Nonpharmacological Conservative Treatments for Chronic Functional Constipation: A Systematic Review and Network Meta-Analysis. Neurogastroenterol Motil. 31 (1), e13441. doi:10.1111/nmo. 13441
Zheng, Y., and Pan, C. W. (2014). Effect of Shenfu Injection on Oxygen Metabolism in Patients with Infection Shock. Chin. Arch. Tradit Chin Med 32, 2770-2772. doi:10. 13193/j.issn.1673-7717.2014.11.06310.1002/cjoc. 201490024
Zheng, Y. S., Wu, Z. S., Ni, H. B., Ke, L., Tong, Z. H., Li, W. Q., et al. (2014). Codonopsis Pilosula Polysaccharide Attenuates Cecal Ligation and Puncture Sepsis via Circuiting Regulatory T Cells in Mice. Shock 41 (3), 250-255. doi:10. 1097/shk. 0000000000000091
Zhou, C. L. (2014). Clinical Research of Effects on Shenfu Injection on Tissue Perfusionin of Patients with Septic Shock in the Early Recovery Capacity. MS thesis. Shandong: Shandong University of Traditional Chinese Medicine.
Zhou, H. F., Ge, Y. L., Li, H. Y., and Wang, H. Y. (2016). Effect of Shenfu Injection Combined with Low Dose Hydrocortisone on HLA-DR and PCT in Patients with Severe Sepsis. Med. Recapitulate 22, 1382-1385. doi:10.3969/j.issn.10062084.2016.07.039

Zhou, X. L., Lin, M. X., and Yu, Y. (2015). The Effect on Hemodynamics and Prognosis of Shenfu Injection for Patients with Severe Sepsis. Chongqing Med. 44 (36), 5157-5159. doi:10.3969/j.issn.1671-8348.2015.36.038
Zhu, M. G. (2017). Clinical Study on the Effect of Tonifying Qi and Warming Yang Method on Immune Function in Patients with Sepsis. MS thesis. Guangzhou: Guangzhou University of Chinese Medicine.
Zou, Y. F., Zhang, Y. Y., Fu, Y. P., Inngjerdingen, K. T., Paulsen, B. S., Feng, B., et al. (2019). A Polysaccharide Isolated from Codonopsis Pilosula with Immunomodulation Effects Both In Vitro and In Vivo. Molecules 24 (20), 3632. doi:10.3390/molecules24203632

Conflict of Interest: The authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest.

The reviewer CL declared a shared parent affiliation, with no collaboration, with the authors, to the handling editor at the time of the review.

Publisher's Note: All claims expressed in this article are solely those of the authors and do not necessarily represent those of their affiliated organizations, or those of the publisher, the editors and the reviewers. Any product that may be evaluated in this article, or claim that may be made by its manufacturer, is not guaranteed or endorsed by the publisher.

Copyright © 2022 Xiao, Niu, Xu, Zhao, Yue, Liu and Li. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.