# Comparative Efficacy of Acupuncture-Related Techniques for Urinary Retention After a Spinal Cord Injury: A Bayesian Network Meta-Analysis 

Kelin He ${ }^{1,2 \dagger}$, Xinyun Li ${ }^{1 \dagger}$, Bei Qiu ${ }^{\dagger}$, Linzhen Jin ${ }^{\dagger}$ and Ruijie Ma ${ }^{1,2 *}$<br>${ }^{\dagger}$ Key Laboratory of Acupuncture and Neurology of Zhejiang Province, Third School of Clinical Medicine (School of Rehabilitation Medicine), Zhejiang Chinese Medical University, Hangzhou, China, ${ }^{2}$ Department of Acupuncture and Moxibustion, The Third Affiliated Hospital of Zhejiang Chinese Medical University (Zhongshan Hospital of Zhejiang Province), Hangzhou, China

## OPEN ACCESS

Edited by:
Ahmed Negida,
Zagazig University, Egypt
Reviewed by:
Ali Hammed,
Tishreen University, Syria
Peijing Rong,
China Academy of Chinese Medical
Sciences, China
*Correspondence:
Ruijie Ma
maria7878@sina.com
${ }^{\dagger}$ These authors have contributed equally to this work and share first authorship

Specialty section:
This article was submitted to Neurotrauma, a section of the journal Frontiers in Neurology
Received: 10 June 2021
Accepted: 27 December 2021
Published: 07 February 2022
Citation:
He K, Li X, Qiu B, Jin L and Ma R (2022) Comparative Efficacy of Acupuncture-Related Techniques for Urinary Retention After a Spinal Cord Injury: A Bayesian Network Meta-Analysis. Front. Neurol. 12:723424. doi: 10.3389/fneur.2021.723424

Background: Urinary retention is one of the most frequent complications of spinal cord injuries (SCI) and negatively impacts patient satisfaction and quality of life. Acupuncture as an integral part of traditional Chinese medicine (TCM) has recently drawn widespread attention for its potential in the management of urinary retention. However, there are many different styles of acupuncture-related techniques, and the optimal choice of acupuncture for urinary retention after SCI is still unclear. Hence, this study uses a Bayesian network meta-analysis (NMA) to compare the efficacy of different types of acupuncture therapies using both direct and indirect evidence.
Methods: Randomized controlled trials of acupuncture-related techniques for treating urinary retention after SCI were retrieved from the following electronic databases: Pubmed, Cochrane Library, Web of Science, China National Knowledge Infrastructure (CNKI), the Chinese Biomedical Literature Service System (SinoMed), the Wan-Fang database, and the Chinese Scientific Journals Database (VIP). The retrieval time was from inception to November 2020. Clinical effective rate (CER) was the primary outcome indicator and residual urine volume (RUV) was the secondary outcome indicator. A Bayesian NMA was performed using the Markov chain Monte Carlo method in R software (version 3.6.1) interfacing with JAGS software (version 4.3.0). The node-splitting method was used to identify inconsistencies. In addition, a comparative adjusted funnel plot was used to assess publication bias.
Results: A total of 26 randomized controlled trials involving 1,652 patients were included. Bayesian NMA showed that electroacupuncture combined with moxibustion ranks first in both CER and RUV. In addition, in terms of cumulative probability, electro-acupuncture combined with moxibustion ranked first in CER. The results of the node splitting method revealed that direct and indirect evidence were consistent $(P>0.05)$. In addition, publication bias was detected.

Conclusion: A Bayesian NMA that combined direct and indirect comparisons showed that electro-acupuncture combined with moxibustion had a better effect on urinary retention due to SCI. However, it still needs a large sample size and high-quality randomized controlled trials to verify this finding.

Systematic Review Registration: https://inplasy.com/, identifier: INPLASY2021110005.

Keywords: acupuncture, urinary retention, network meta-analysis, spinal cord injury, clinical efficacy

## INTRODUCTION

Urinary retention is impaired voiding despite a full bladder, leading to a post-void residual (PVR) (1). It is one of the most frequent results of spinal cord injury (SCI) and negatively impacts patient satisfaction and quality of life. Urinary retention after SCI refers to dysfunction of the urinary bladder due to damaged bladder neural circuits following SCI. Studies have found that the bladder wall appears ischemic following SCI, affecting bladder metabolic function and resulting in the inability to discharge urine (2). Urinary retention has been closely associated with adverse outcomes including urinary tract infections, overdistension of the urinary bladder, and high mortality rates (3-5). Urethral catheterization and bladder function training are currently the main treatments for urinary retention among those SCI patients whose normal bladder function is altered. However, urethral catheterization is strongly associated with urinary tract infection (UTI), and the risk of a UTI increases with how long the patient catheterizes (6). Catheter-associated UTIs are the most common nosocomial infections. Catheter-associated UTIs affect men and women, and long-term urinary catheterization always and inevitably leads to bacteria in the urine of both sexes. Long-term catheterization typically results in a daily risk of $3-7 \%$ for the development of symptomatic catheter-associated UTI (7). In contrast, bladder function training leads to limited functional improvement. There is therefore a strong demand for novel and effective therapies for urinary retention after SCI.

Acupuncture as an integral part of traditional Chinese medicine (TCM) has recently drawn widespread attention for its potential in the management of urinary retention. It has consequently been the subject of research works on the topic (8-12). Advantages of acupuncture, as non-pharmacological therapy, including safety, convenience, and minimal side effect profile (13, 14). In China, many domains of acupuncture such as manual acupuncture, electro-acupuncture, moxibustion therapy, auricular acupuncture, and acupoint patching are widely used in the treatment of urinary retention after SCI. A previous traditional pairwise meta-analysis indicated that acupuncture has a positive effect on urinary retention due to SCI (15). However, there are many different styles of acupuncture, and

[^0]the optimal acupuncture intervention is still unclear. Network meta-analysis (NMA) based on the traditional pairwise metaanalysis is an increasingly popular tool that can simultaneously synthesize direct and indirect evidence by summarizing different interventions for the same disease $(16,17)$. NMA can also assess the efficacy of different treatments and estimate the relative efficacy of such interventions $(18,19)$. Therefore, this study aimed to use NMA to explore the efficacy of different acupuncture therapy types in the treatment of urinary retention after SCI. This work may help provide guidelines for acupuncture therapy in the treatment of urinary retention after SCI and serve as the basis of future work.

## MATERIALS AND METHODS

This study followed the Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) guidelines (20), and the study protocol has been registered on the website of https:// inplasy.com/ (Registration number: INPLASY2021110005).

## Eligibility and Exclusion Criteria

Literature inclusion: The PICOS framework (participants, interventions, comparisons, outcome, and study design) was used to identify literature appropriate for inclusion in this work. Eligible literature were randomized controlled trials (RCTs): (1) Study design: only articles referring to RCTs were included; (2) Participants: diagnosed with spinal cord injury, survived the shock period, not limited by age, gender, race, or nationality; (3) Intervention and control measures: using a similar study as the reference (21), acupuncture-related techniques were defined as acupoint-based therapy (e.g., manual acupuncture, electroacupuncture, auricular acupuncture, moxibustion, acupoint patching, acupoint injection, acupoint embedding, and warm needling moxibustion) in this systematic review, regardless of stimulation method. The control group received conventional therapy or conventional therapy combined with some other therapy. The current conventional-therapies strategy for urinary retention after SCI consists of intermittent catheterization and bladder function training. (4) Outcome indicators: The primary outcome was Clinical effective rate (CER). Based on the presence of clinical symptoms and objective indicators, efficacy was divided into valid and invalid categories. No improvement in clinical symptoms, including those that worsen, was considered invalid. $\mathrm{CER}=$ (total number - invalid number)/total number $\times$ $100 \%$ (22). The secondary outcome was residual urine volume


[^0]:    Abbreviations: CT, conventional therapy; EA, electro-acupuncture; MA: manual acupuncture; WNM, warm needle moxibustion; AA, auricular acupuncture; AP, acupoint patching; DSQP, dong shi qi point; WAA, wrist-ankle acupuncture; SA, sham acupuncture; SCI, spinal cord injury.

(RUV). The level of urinary retention was evaluated by the amount of RUV.

Literature exclusion: (1) Treatment measures in the experimental group included non-acupuncture-related therapies such as Chinese medicine and Western medicine; (2) The trial data was wrong; (3) The trial data was repeated; (4) The full text could not be obtained; (5) The outcome was not relevant.

## Search Strategy

RCTs of acupuncture-related techniques for the treatment of urinary retention after SCI were extracted from the following electronic databases: China National Knowledge Internet (CNKI), Wan-fang Database, Chinese Scientific Journals Database (VIP), the Chinese Biomedical Literature Service System (SinoMed), PubMed, Cochrane Library, and Web of Science. The retrieval period was from inception to November 2020. Terms such as "acupuncture," "manual acupuncture," "electro-acupuncture," "scalp needle," "elongated needle," "moxibustion," "warm needling," "acupuncture plus moxibustion," "acupoint injection," "acupoint patching," "auricular acupuncture," "ear acupuncture," "spinal cord injury," "urinary retention," and "neurogenic bladder" were used as subject words, keywords, free-text terms, or MeSH (Medical Subject Heading) terms to identify potentially eligible studies. The search strategy was adjusted for each database. There were no restrictions on blinding methods, language, and year of publication.

## Data Extraction and Quality Assessment

Relevant data from the eligible studies were extracted by two independent reviewers, and Microsoft Excel 2019 (Microsoft Corp, Redmond, WA, USA) was used to manage the data. A standard form table was constructed that included publication information (authors, publish date), demographic data (gender, age, ASIA grading, sample size, the course of SCI onset), intervention measures (experimental group: acupuncture treatments plus conventional therapy; control group: conventional therapy or conventional therapy plus other acupuncture therapy), and outcome (CER, RUV). The independent reviewers assessed the quality of the included trials using the Cochrane risk of bias tool (23). The Cochrane Risk of Bias tool includes seven items: (1) random sequence generation; (2) allocation concealment; (3) blinding of participants and personnel; (4) blinding of outcome assessment; (5) incomplete outcome data; (6) selective reporting; (7) other sources of bias. Each trail was graded as either "low," "high," or "unclear" risk. During trial selection when data extraction and quality assessment scores were inconsistent, discrepancies were resolved by a third reviewer.

## Statistical Analysis

Given the potential sources of clinical heterogeneity among the included studies, a random effect model was adopted to merge the datasets. The Bayesian meta-analysis was performed using R software (version 3.6.3; http://www.Rproject.org) and JAGS software (version 4.3.0, https://nchc.dl.sourceforge.net/project/ mcmc-jags/JAGS/4.x/Windows/JAGS-4.3.0.exe), using the

Bayesian hierarchical model and the Markov Chain Monte Carlo algorithm (24). We used 200,000 iterations, and the first 5,000 iterations were regarded as burn-in for annealing to eliminate the influence of the initial value. The combined results were presented as odds ratios (ORs) with $95 \%$ confidence intervals ( $95 \%$ CIs) for dichotomous outcomes. Due to the limitations of dichotomous outcomes, the description of "healing," "remarkable effect," and "effective" described in the study were combined into valid. The combined results were presented as mean differences (MDs) with $95 \%$ CIs for continuous outcomes. If $95 \%$ CIs of ORs did not contain 1 and $95 \%$ CIs of MDs did not contain 0 , the corresponding ORs or MDs were considered to indicate a statistically significant difference. The surface under the cumulative ranking area (SUCRA) was used to rank the probabilities for different interventions. The SUCRA values range from 0 to $100 \%$, assigned to the worst and best treatments (25), respectively. Publication bias and small-study effects among the included RCTs for the primary outcome were compared using an adjusted funnel plot (26).

## RESULTS

## Literature Selection

A total of 1,199 references were identified ( 375 references from CNKI, 405 references from Wanfang, 188 references from VIP, 190 references from SinoMed, 8 references from Pubmed, 19 references from Cochrane Library, and 14 references from Web of Science) and imported into Endnote X9 (Clarivate Analytics, Philadelphia, PA, USA). After eliminating duplicates, 419 articles remained. Following the exclusion of reviews, case reports, animal experiments, and other irrelevant content, 125 studies remained. Non-randomized methodologies, data duplication, mixed interventions, and outcome indicators that did not include CER or RUV were also excluded. A total of 26 RCTs were ultimately included after evaluating the full text. A detailed flowchart depicting the article screening process is shown in Figure 1.

## Study Characteristics

A total of 26 articles were included, of which 25 trials (27-51) were double-arm RCTs and one trial (11) was three-arm RCTs. The total sample consisted of 1,652 patients ( 805 in the control group and 847 in the treatment group). Eight studies did not mention American Spinal Injury Association (ASIA) grade. Six studies did not report the course of SCI. Three studies did not mention the gender ratio of the participants. Two studies only reported the overall gender ratio. Three studies did not report patient age. The interventions in the control group included conventional therapy (CT) combined with electro-acupuncture (EA), CT combined with drug, CT combined with warm needle moxibustion (WNM), and CT combined with manual acupuncture (MA). The interventions in the experimental group included CT combined with EA, CT combined with Moxibustion (MOX), CT combined with MA, CT combined with acupoint patching (AP), CT combined with MOX, and Dong Shi Qi Point (DSQP), CT combined with auricular acupuncture (AA), CT combined with EA and MOX, CT combined with MOX

![img-0.jpeg](img-0.jpeg)

FIGURE 1 | Flow diagram depicting the selection process of eligible studies. CNKI, China national knowledge infrastructure; VIP, Chinese Scientific Journals Database; SinoMed, Chinese Biomedical Literature Service System; n, number of publications.

and Wrist-ankle acupuncture (WAA). The shortest treatment course was 7 days and the longest was 2 months. Twenty-one trials reported CER and 20 trials reported RUV. Detailed study summaries are shown in Table 1.

### Quality Evaluation

Figure 2 depicts the risk of bias. For random sequence generation, 13 trials used random number tables, three trials used network programming software, six trials did not provide randomization details, and four trials used a wrong random method. Two trials involved allocation concealment and were assigned a low risk of bias. Only one trial mentioned single blindness and was assigned a low risk of bias. Only one trial reported two cases dropped out and the influence of incomplete outcome data was assigned a low risk of bias. All trials that did not mention study protocol and the influence of selective reporting were assigned an "uncertain" risk of bias. Only one trial reported disclosure of conflict of interest and the influence of other sources of bias was assigned a low risk of bias.

### Outcome

#### Clinical Effectiveness

Figure 3 shows 12 direct comparisons: CT vs. CT+MA (n = 2), CT vs. CT+EA (n = 2), CT vs. CT+MOX (n = 5), CT vs. CT+AA (n = 1), CT vs. CT+AP (n = 1), CT vs. CT+DSQP+MOX (n = 1), CT vs. CT+WAA (n = 1), CT+Drug vs. CT+MA (n = 1), CT+Drug vs. CT+EA (n = 1), CT+EA vs. CT+EA+MOX (n = 2).

TABLE 1 | Characteristics of the included studies.


TABLE 1 Continued

E:32 | BCD | $\begin{aligned} & \mathrm{C}: \leq 4 \mathrm{w} ; \ & \mathrm{E}: \leq 4 \mathrm{w} \end{aligned}$ | $-$ | $-$ | CT (intermittent catheterization) | CT+MA (Zhibian (BL54) toward the direction of Shuidao (ST28); treatment duration was 30 min , once every other day for 30 days) | CER, RUV  |
E:31 | ABCD | $\begin{aligned} & \text { C:(35.67 } \pm 8.29) \mathrm{d} ; \ & \text { E:(36.12 } \pm 4.83) \mathrm{d} \end{aligned}$ | $\begin{aligned} & \text { C:26/5; } \ & \text { E:24/7 } \end{aligned}$ | $\begin{aligned} & \text { C:41.87 } \pm 13.88 ; \ & \text { E:40.25 } \pm 14.06 \end{aligned}$ | CT (not very clear) +Drug (3 mg neostigmine, once a day for 6 consecutive days) | CT+EA (EA at Baliao (BL31-34); treatment duration was 30-40 min, 6 times per week for 2-3weeks) | CER, RUV  |
E:30 | AB | $\begin{aligned} & \text { C:(67.61 } \pm 17.04) \mathrm{d} ; \ & \text { E:(66.20 } \pm 13.14) \mathrm{d} \end{aligned}$ | $\begin{aligned} & \text { C:21/10; } \ & \text { E:22/8 } \end{aligned}$ | $\begin{aligned} & \text { C:34.48 } \pm 9.04 ; \ & \text { E:34.23 } \pm 9.62 \end{aligned}$ | CT (intermittent catheterization) | CT +MOX (herb-partitioned MOX at Shenque (CV8), Guanyuan (CV4), Zhongji (CV3), Zusanli (ST36), Mingmen (GV 4), Shenshu (BL23), and Pangguangshu (BL28); treatment duration was 20 min, 6 times per week for 5 weeks) | CER, RUV  |
E:30 | ABCD | $\begin{aligned} & \text { C:(3.12 } \pm 0.81) \mathrm{m} ; \ & \text { E:(3.56 } \pm 0.79) \mathrm{m} \end{aligned}$ | $\begin{aligned} & \text { C:13/17; } \ & \text { E:16/14 } \end{aligned}$ | $\begin{aligned} & \text { C:40.25 } \pm 5.12 ; \ & \text { E:39.87 } \pm 5.61 \end{aligned}$ | CT (intermittent catheterization and bladder training) | CT +MA (MA at Zhongji (CV3), Qihai (CV6), Guanyuan (CV4), Gutia (ST29), Shuidao (ST28), Yinlingquan (SP9), and Sanyinjiao (SP6); treatment duration was 30 min , once a day for 28 days) | CER, RUV  |
E:30 | $-$ | $-$ | $-$ | $-$ | CT (catheterization) | CT +multiple acupuncture (Morning: MA at Guanyuan (CV4), Afternoon: EA at Ciliao (BL32), and Zhongliao (BL33); treatment duration was 30 min , once a day for 10 days) | CER  |
E:30 | $-$ | $-$ | $\begin{aligned} & \text { C:21/9; } \ & \text { E:19/11 } \end{aligned}$ | $\begin{aligned} & \text { C:44.7 } \pm 3.9 ; \ & \text { E:45.1 } \pm 3.7 \end{aligned}$ | CT (intermittent catheterization and bladder training) | CT+MOX (box MOX at Shenque (CV8), Guanyuan (CV4), Qihai (CV6), Zhongji (CV3), Shenshu (BL23), Weizhong (BL40), Sanyinjiao (SP6), and Zusanli (ST36); treatment duration was 30 min , once a day for 30 days) | CER, RUV  |
E:26 | $-$ | $(7.42 \pm 5.13) \mathrm{m}$ | 28/23 | $36.20 \pm 8.64$ | CT (not very clear) +WNM (WNM at Qihai (CV6), Guanyuan (CV4), and Ciliao (BL32), the treatment duration was 40 min , once a day for 60 days) | CT+MOX (heat-sensitive MOX at Qihai (CV6), Guanyuan (CV4), and Ciliao (BL32); treatment duration was 40 min , once a day for 60 days) | CER  |
E:30 | $-$ | $-$ | $\begin{aligned} & \text { C:25/5; } \ & \text { E:26/4 } \end{aligned}$ | $\begin{aligned} & \text { C:34.62 } \pm 1.85 ; \ & \text { E:36.78 } \pm 2.32 \end{aligned}$ | CT (routine rehabilitation) | CT +AP (AP at Qihai (CV6), Guanyuan (CV4), Zhongji (CV3), Yinlingquan (SP9), Sanyinjiao (SP6), Shenshu (BL23), and Pangguangshu (BL28), once a day for 7 consecutive days) | CER, RUV  |
E:45 | $-$ | $(1-4) \mathrm{m}$ | $\begin{aligned} & \text { C:23/21; } \ & \text { E:25/20 } \end{aligned}$ | $\begin{aligned} & \text { C:36.1; } \ & \text { E:35.3 } \end{aligned}$ | CT (intermittent catheterization) +Drug (0.5-1 mg neostigmine, once a day for 7 consecutive days) | CT+MA (MA at Shenshu (BL23), Ciliao (BL32), Yinlingquan (SP9), Sanyinjiao (SP6), and Zhongji (CV3); treatment duration was 30 min , once a day for 7 consecutive days) | CER  |
E:32 | $-$ | $\begin{aligned} & \text { C:(8.84 } \pm 2.94) \mathrm{d} ; \ & \text { E:(8.31 } \pm 2.51) \mathrm{d} \end{aligned}$ | $\begin{aligned} & \text { C:22/10; } \ & \text { E:25/7 } \end{aligned}$ | $\begin{aligned} & \text { C:41 } \pm 9.36 ; \ & \text { E:40.53 } \pm 10.76 \end{aligned}$ | CT (intermittent catheterization) | CT +DSQP (the treatment duration was 30 min , once a day for 7 consecutive days) +MOX (herb-partitioned MOX at Shenque (CV8), once a day for 30 days) | CER, RUV  |

TABLE 1 Continued

E:30 | A | - | 46/14 | - | CT (intermittent catheterization) | CT+EA (EA at Shuidao (ST28), Yinlingquan (SP9), Ciliao (BL32), and Pangguangshu (BL28); treatment duration was 30 min, 6 times per week for 6 weeks) | CER, RUV  |
E:32 | BCD | $\begin{aligned} & \mathrm{C}:(46.03 \pm 8.33) \mathrm{d} \ & \mathrm{E}:(48.34 \pm 10.12) \mathrm{d} \end{aligned}$ | $\begin{aligned} & \mathrm{C}: 16 / 14 ; \ & \mathrm{E}: 15 / 17 \end{aligned}$ | $\begin{aligned} & \mathrm{C}: 35.20 \pm 8.12 ; \ & \mathrm{E}: 37.20 \pm 7.09 \end{aligned}$ | CT (voiding and bladder training) | CT+MA (MA at Qihai (CV6), Guanyuan (CV4), Zhongji (CV3), Yaoyangguan (GV3), and Mingmen (GV 4); treatment duration was 30 min, 6 times per week for 8 weeks) | RUV  |
E:30 | BCD | $\begin{aligned} & \mathrm{C}:(33.57 \pm 17.89) \mathrm{d} ; \ & \mathrm{E}(35.17 \pm 15.48) \mathrm{d} \end{aligned}$ | $\begin{aligned} & \mathrm{C}: 17 / 13 ; \ & \mathrm{E}: 14 / 16 \end{aligned}$ | $\begin{aligned} & \mathrm{C}: 45.2 \pm 11.43 ; \ & \mathrm{E}: 43.7 \pm 10.89 \end{aligned}$ | CT (voiding and bladder training) | CT+EA (EA at Qihai (CV6), Guanyuan (CV4), Zhongji (CV3), Yaoyangguan (GV3), and Mingmen (GV 4); treatment duration was 30 min, 6 times per week for 4 weeks) | RUV  |
E:34 | ABCD | $\begin{aligned} & \mathrm{C}:(10 \pm 4.8) \mathrm{d} ; \ & \mathrm{E}(11 \pm 3.9) \mathrm{d} \end{aligned}$ | $\begin{aligned} & \mathrm{C}: 28 / 4 ; \ & \mathrm{E}: 29 / 5 \end{aligned}$ | $\begin{aligned} & \mathrm{C}: 37.4 \pm 16.3 ; \ & \mathrm{E}: 38.2 \pm 15.1 \end{aligned}$ | CT (intermittent catheterization) | CT+AA (AA at bladder, ureter, kidney, cervical spine, thoracic spine, and lumbosacral spine point; treatment duration was 30-60 min, 20 times for 25 days) | CER, RUV  |
EA:38 | $\begin{aligned} & \mathrm{C}:(22.2 \pm 2.4) \mathrm{d} \ & \mathrm{EA}(25.8 \pm 2.4) \mathrm{d} \ & \mathrm{SA}:(25.5 \pm 2.5) \mathrm{d} \end{aligned}$ | - | $\begin{aligned} & \mathrm{C}: 40.6 \pm 9.8 ; \ & \text { EA:39.6 } \pm 7.6 \ & \text { SA:40.75 } \pm 12.5 \end{aligned}$ | CT (behavioral interventions, such as fluid schedules and regular voiding attempts, clean intermittent catheterization) | CT+EA (EA at Shangliao (BL31), Xialiao (BL34); treatment duration was 20 min ) SA (the needle was taped to the dermal surface of Baliao (BL31-34) using an adhesive tape without insertion, serving as a mock EA therapeutic instrument) | RUV  |

C, control group; E, experimental group; m, month; d, day; w, week; CT, conventional therapy; EA, electro-acupuncture; MOX, moxibustion; WNM, warm needle moxibustion; AA, auricular acupuncture; AP, acupoint patching; DSQP, Dong Shi Qi point; MA: manual acupuncture; WAA, wrist-ankle acupuncture; SA, sham acupuncture; RUV, residual urine volume; CER, clinical effective rate.

![img-1.jpeg](img-1.jpeg)

**FIGURE 2 |** Risk of bias of the included studies. The vertical axis represents the quality evaluation items and the horizontal axis represents the number of studies.

CT+MOX vs. CT+WNM (*n* = 1), CT vs. CT+multiple acupuncture (*n* = 1). **Figure 4** shows the ranked and SUCRA values. CT+EA+MOX ranked first. CT+EA+MOX (97%) had the highest SUCRA value in CER followed by CT+EA (74%), CT+MA (66%), CT+MOX (64%), CT+AP (63%), CT+multiple acupuncture (59%), CT+WAA+MOX (54%), CT+DSQP+MOX (54%), CT+Drug (24%), CT+WNM (21%), CT (21%), and CT+AA (4%). **Table 2** shows the Odds ratio (95%CIs) of all treatments. Compared with CT, CT+MA, CT+EA, CT+MOX, and CT+EA+MOX were associated with significantly higher probabilities of CER.

### Residual Urine Volume

**Figure 5** presents 11 direct comparisons: CT vs. CT+MA (*n* = 3), CT vs. CT+EA (*n* = 2), CT vs. CT+MOX (*n* = 6), CT vs. CT+SA (*n* = 1), CT vs. CT+AA (*n* = 1), CT vs. CT+AP (*n* = 1), CT vs. CT+DSQP+MOX (*n* = 1), CT vs. CT+WAA (*n* = 1), CT+Drug vs. CT+EA (*n* = 1), CT+EA vs. CT+EA+MOX (*n* = 2), CT+EA vs. CT+SA (*n* = 1). **Figure 6** presents the ranked and SUCRA value. CT+EA+MOX ranked first in terms of RUV and the SUCRA value followed by CT+MA (79%), CT+EA+MOX (78%), CT+MOX (76%), CT+EA (62%), CT+AP (52%), CT+MOX+DSQP (42%), CT+WAA+MOX (41%), CT+Drug (40%), CT+AA (37%), CT+SA (23%), and CT (17%). **Table 3** presents the mean differences (95%CIs) of all therapeutic measures. Compared with CT (control group), CT+MA, CT+EA, CT+MOX, and CT+EA+MOX were associated with significantly higher probabilities of RUV.

![img-2.jpeg](img-2.jpeg)

**FIGURE 3 |** Network of eligible comparisons for the network meta-analysis of CER. Each node represents an intervention and the size of each node represents the number of randomly assigned participants. Each line represents a direct comparison between interventions and the width of the lines represents the number of studies.

### Publication Bias

A comparative adjusted funnel plot was used to assess CER publication bias. When the distribution points in the funnel plot are symmetric, there is no publication bias (52). As shown in **Figure 7**, all points on the funnel plot were asymmetric and two points were at the

![img-3.jpeg](img-3.jpeg)

**FIGURE 4 |** Cumulative probability ranking curve of different interventions for CER. The vertical axis represents cumulative probabilities, while the horizontal axis represents ranks.

bottom of the funnel plot, which represents a potential publication bias.

### Consistency Test

The node-splitting method was used to assess the inconsistency of the model between direct and indirect evidence (53, 54). Closed loops within the network were divided into direct and indirect comparison results. As shown in **Figure 8**, the results of node splitting revealed that direct and indirect evidence were consistent (*P* > 0.05).

### DISCUSSION

To the best of our knowledge, this is the first Bayesian NMA of acupuncture-related techniques in the treatment of urinary retention in patients with SCI. This study included 26 RCTs. The results of CER in NMA demonstrated that EA combined with MOX, EA, MOX, and MA have significantly increased treatment effects compared with CT. RUV in NMA demonstrated that EA combined with MOX, EA, MOX, and MA have significantly increased positive effects compared with CT. In terms of ranking probability, EA combined with MOX ranked first in both CER and RUV. In terms of cumulative probability, EA combined with MOX ranked first in CER. CER was assessed based on the degree of improvement of TCM clinical symptoms before and after treatment. This evaluation criterion was widely used to evaluate the efficacy of TCM (55–57). Further, the node splitting method showed that the direct and indirect evidence supporting treatment efficacy was consistent. Therefore, EA combined with MOX may be the best acupuncture intervention in patients with urinary retention secondary to an SCI.

The outcomes of the works included in this meta-analysis highlight several important factors, the most important of which is that EA combined with MOX may have better therapeutic efficacy in the treatment of urinary retention due to SCI. There is a good deal of evidence to support this view. An earlier study performed by our team indicated that acupuncture contributed to the recovery of neurologic function after SCI (58), and EA was the most frequently used technique. Another systematic review also suggests that acupuncture was helpful in the treatment of urinary retention after SCI, and EA was also primarily used (15). EA has been found to promote the recovery of bladder function in the setting of multiple pathologies (59, 60). Experimental studies showed that the mechanism of action of EA on bladder function includes apoptosis inhibition, nerve cell protection, and promotion of recovery of injured nerves (61). MOX is also an important part of acupuncture therapy, and has been widely used since ancient times in China. MOX exerts a warm stimulation effect by burning the herb Artemisia vulgaris over an acupoint and is widely considered a type of acupuncture treatment (62). Previous studies have shown that MOX can be used to treat urinary dysfunction caused by a stroke, SCI, or other factor

TABLE 2 | League table of all CER comparisons.


A, CT; B, CT+Drug; C, CT+MA; D, CT+EA; E, CT+MOX; F, CT+WNM; G, CT+EA+MOX; H, CT+AA; I, CT+AP; J, CT +MOX+DSQP; K, CT+MOX+WAA; L, CT+multiple acupuncture. The bolded and underlined results indicate statistical significance.

![img-4.jpeg](img-4.jpeg)

**FIGURE 5 |** Network of eligible comparisons for the network meta-analysis of RUV. Each node represents an intervention and the size of each node represents the number of randomly assigned participants. Each line represents a direct comparison between interventions and the width of the lines represents the number of studies.

(29, 63–65). Furthermore, EA combined with MOX is commonly used in research and clinical practice (66, 67). It is therefore noteworthy that the cumulative probability of EA combined with MOX did not show a significant advantage over EA alone in terms of RUV. Due to individual variation, RUV may not be the most suitable method for evaluating the clinical efficacy of TCM.

One important factor that needs to be taken into consideration is the selection of a Bayesian method or frequency analysis. The Bayesian method integrates overall information, sample information, and prior information of unknown parameters. According to Bayes' theorem, the posterior distribution of unknown parameters is obtained and unknown parameters are statistically inferred. This flexibility permits the wide use of Bayesian methodology in scientific research. Bayesian NMA also fully considers the uncertainty of parameters and can describe them with direct probabilities (for example, the probability that one intervention is better than another). Compared with frequency methods, Bayesian methods are more valuable when dealing with complex or sparse data (20). Finally, the comparison-adjusted funnel plot was used to detect publication bias in this study. The comparison-adjusted funnel plot appeared to have a degree of asymmetry, suggesting that potential publication bias

![img-5.jpeg](img-5.jpeg)

**FIGURE 6 |** Cumulative probability ranking curve of different interventions for RUV. The vertical axis represents cumulative probabilities, while the horizontal axis represents ranks.

TABLE 3 | League table of all RUV comparisons.


A, CT; B, CT+Drug; C, CT+MA; D, CT+EA; E, CT+MOX; F, CT+SA; G, CT+EA+MOX; H, CT+AA; I, CT+AP; J, CT+MOX+DSQP; K, CT+WAA+MOX. The bolded and underlined results indicate statistical significance.

![img-6.jpeg](img-6.jpeg)

FIGURE 7 | Comparison-adjusted funnel plots for the CER network. The vertical axis represents "standard error of effect size" and the horizontal axis represents "effect size centered at the comparison-specific pooled effect (y_{Wj-uWj})." (A, CT; B, CT+Drug; C, CT+MA; D, CT+EA; E, CT+MOX; F, CT+WNM; G, CT+EA+MOX; H, CT+AA; I, CT+AP; J, CT+MOX+DSQP; K, CT+WAA+MOX; L, CT+multiple acupuncture).

![img-7.jpeg](img-7.jpeg)

FIGURE 8 | Consistency test results assessed different treatment measures of CER (A, CT; B, CT+ Drug; C, CT+MA; D, CT+EA; E, CT+MOX).

existed in which "negative" studies were less likely to be reported. Prioritizing the publication of only articles that demonstrated differences between groups might be due to the rejection by journal editors of studies in this research field that report negative findings and seriously limits the quality of the evidence that addresses the effectiveness of acupuncture treatment.

Many other factors are also evident based on the studies we analyzed. First, most studies did not mention the ASIA grade of the SCIs. According to a previous study, ASIA grade on admission affected recovery in both univariate and multivariate analyses (68). We therefore could not explore the homogeneity of the ASIA grade included in these patients. Second, an outstanding question was the course of SCI-mediated urinary retention, as only 20 of our included studies mentioned the specific course of the SCI. Therefore, we were unable to compare differences between the acute and chronic phases. Third, most studies do not report on the long-term efficacy of acupuncture treatments. We therefore could not compare the long-term efficacy of acupuncture treatments. In addition, we could not assess the effect of acupoints on urinary retention due to SCI.

### LIMITATIONS

First, the currently available evidence on acupuncture and SCI-related urinary retention is insufficient due to small available sample sizes, limited numbers of patients in each trial, and limited analysis of CER and RUV data. Second, this study did not evaluate the safety of acupuncture because there was a lack of adverse event reporting in most of the included trials. Third, although a comprehensive literature search was performed using multiple online databases, it remains possible that some eligible studies may still have been missed.

### CONCLUSION

The results of this NWM show that EA combined with MOX may be the most effective acupuncture technique for urinary retention after SCI. Our study may provide an important clinical reference value for clinical investigations of acupuncture in the treatment of neurogenic urinary retention and provide essential information to decision-makers. However, there are too many differences between the designs of the included studies to draw a definitive and clinical recommendation. High quality, large sample size, multicenter clinical trials are needed.

### DATA AVAILABILITY STATEMENT

The original contributions presented in the study are included in the article, further inquiries can be directed to the corresponding author/s.

### AUTHOR CONTRIBUTIONS

KH and XL were involved in writing and draft preparation. BQ and LJ were involved in literature inclusion and exclusion. RM was involved in writing, draft preparation, and supervision. All authors critically revised the manuscript and approved its final version.

## FUNDING

This work was supported by the Zhejiang Chinese Medical University Research Fund (Nos. 2019ZG17 and 2018ZY17 to KH); Chinese Medicine Research
