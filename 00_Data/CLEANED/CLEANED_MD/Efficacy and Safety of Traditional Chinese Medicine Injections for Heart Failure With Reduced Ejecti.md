# Efficacy and Safety of Traditional Chinese Medicine Injections for Heart Failure With Reduced Ejection Fraction: A Bayesian Network Meta-Analysis of Randomized Controlled Trials 

OPEN ACCESS

Edited by:
Konrad Urbanek, Magna Graecia University of Catanzaro, Italy

## Reviewed by:

Yi Wang,
Zhejiang University, China
Marcellino Monda,
Università della Campania Luigi
Vanvitelli, Italy
*Correspondence:
Xianliang Wang
xIwang1981@126.com
Jingyuan Mao
jymao@126.com

Specialty section:
This article was submitted to Cardiovascular and Smooth Muscle Pharmacology, a section of the journal Frontiers in Pharmacology

Received: 28 January 2021
Accepted: 29 October 2021
Published: 30 November 2021

Citation:
Lin S, Shi Q, Ge Z, Liu Y, Cao Y, Yang Y, Zhao Z, Bi Y, Hou Y, Wang S, Wang $X$ and Mao J (2021) Efficacy and Safety of Traditional Chinese Medicine Injections for Heart Failure With Reduced Ejection Fraction: A Bayesian Network Meta-Analysis of Randomized Controlled Trials.

Front. Pharmacol. 12:659707. doi: 10.3389/fphar.2021.659707

Shanshan Lin ${ }^{1,2}$, Qingyang Shi ${ }^{2}$, Zhao Ge ${ }^{1,2}$, Yangxi Liu ${ }^{1,2}$, Yawen Cao ${ }^{1,2}$, Ying Yang ${ }^{1}$, Zhiqiang Zhao ${ }^{1}$, Yingfei Bi ${ }^{1}$, Yazhu Hou ${ }^{1}$, Shuai Wang ${ }^{1}$, Xianliang Wang ${ }^{1 *}$ and Jingyuan Mao ${ }^{1 *}$<br>${ }^{1}$ National Clinical Research Center for Chinese Medicine Acupuncture and Moxibustion, First Teaching Hospital of Tianjin University of Traditional Chinese Medicine, Tianjin, China, ${ }^{2}$ Tianjin University of Traditional Chinese Medicine, Tianjin, China

Background: Heart failure as an important issue in global public health, has brought a heavy economic burden. Traditional Chinese medicine injections (TCMIs) have significant effects on heart failure with reduced ejection fraction (HFrEF). However, it is difficult for clinicians to identify the differences in clinical efficacy and safety of various TCMIs. The purpose of this study is to compare the efficacy and safety of various TCMIs for treating HFrEF by conducting a Bayesian network meta-analysis (NMA) and to further provide references for clinical decision-making.

Methods: The clinical randomized controlled trials of TCMIs for treating HFrEF were searched in seven database from inception to August 3rd, 2021. The Cochrane collaboration's tool was used to assess the risk of bias. NMA was performed in a Bayesian hierarchical framework. The surface under the cumulative ranking curve (SUCRA), the multi-dimensional efficacy analysis, the comparison-adjusted funnel plot, and the node-splitting analysis were conducted using R software.

Results: A total of 107 eligible RCTs involving 9,073 HFrEF patients and 6 TCMIs were included. TCMIs include Huangqi injection (HQ) also called Astragalus injection, Shenfu injection (SF), Shengmai injection (SGM), Shenmai injection (SM), Xinmailong injection (XML), and Yiqifumai lyophilized injection (YQFM). The results of NMA and SUCRA showed that with conventional treatment (CT) as a common control, in terms of clinical efficacy, CT + XML was most effective in New York Heart Association cardiac functional classification efficiency, brain natriuretic peptide, and N -terminal pro-brain natriuretic peptide; the CT + SM was most effective in 6-min walking test, left ventricular end-diastolic diameter, left ventricular end-systolic diameter and cardiac output; the CT + YQFM was most effective in left ventricular ejection fraction; the CT + HQ was most effective in stroke volume; the CT + SF

was most effective in Minnesota Living with Heart Failure Questionnaire. In terms of safety, there was no significant difference between CT + TCMIs and CT.

Conclusion: This Bayesian network meta-analysis results show that the combination of qualified TCMIs and CT is more effective for HFrEF patients than CT alone, and CT + XML and CT + SM may be one of the potential optimal treatments. Also, the safety of these TCMIs needs to be further observed. However, due to some limitations, the conclusions need to be verified by more large-sample, double-blind, multi-center RCTs.

## Keywords

traditional chinese medicine, traditional chinese medicine injection, heart failure, randomized controlled trial, network meta-analysis, bayesian model

## INTRODUCTION

Heart failure (HF) is defined as a clinical syndrome, characterized by dyspnea, fatigue, fluid retention, etc. caused by a reduced cardiac output and/or elevated intracardiac pressures due to a structural and/or functional cardiac abnormality (Ponikowski et al. 2016). It generally occurs in the terminal stage of various cardiovascular diseases, with high morbidity and mortality (Virani et al. 2020). A China Heart Failure Registry Study (China-HF) conducted between 2012 and 2014 indicated that the in-hospital mortality of HF patients was 5.3% (Zhang and Zhang, 2015). As standard treatment strategies for HF are constantly being updated and improved, the morbidity and mortality of HF have decreased slightly (Merlo et al. 2014). However, with the intensified aging of the social demographic structure, the total proportion of HF is expected to rise from 2.42% in 2012 to 2.97% in 2030. The overall cost of HF is continuing to rise, which will increase the global medical and health burden (Heidenreich et al. 2013; Cook et al. 2014; Dokainish et al. 2015; Virani et al. 2020). Therefore, how to further improve the quality of life and long-term prognosis of HF patients based on modern medicine has attracted increasing attention.

Traditional Chinese medicine (TCM) is an empirical medicine with a history of more than 2,000 years and has considerable research value. Especially in the prevention and treatment of coronavirus disease in 2019 (COVID-19), TCM has played an irreplaceable role. Therefore, the clinical value of TCM is worthy of continuous exploration, and it needs more attention from all over the world. Compared with TCM decoctions, which are generally recognized as the most traditional medicine dosage form, the effective ingredients of traditional Chinese medicine injections (TCMIs) can be directly injected into the blood through intravenous injection. On the one hand, it takes effect faster, and on the other hand, it reduces the possibility of the drug being metabolized by the digestive system, thereby ensuring sufficient active ingredients to work. Besides, as modern preparations of TCM extracts, TCMIs have a more standard quality evaluation system than TCM decoctions, so it is easier to obtain high-quality clinical evidence. At present, it has been proved that a large number of TCMIs can significantly improve the clinical efficacy of heart failure with reduced ejection fraction (HFrEF) based on conventional treatment (CT) (Xu T. et al. 2018; Zhu et al. 2018; Lin W. J. et al. 2019; Xie and Dai, 2019; Lin et al. 2021). However, due to the lack of direct comparative evidence, it is difficult for clinicians to identify the differences in clinical efficacy and safety of various TCMIs and prescribe optimal drugs.

Network meta-analysis (NMA) can compare multiple interventions simultaneously in a single analysis by synthesizing direct and indirect evidence, and ranking them according to efficacy or safety (Rouse et al. 2017). Therefore, this NMA compared the efficacy and safety of various TCMIs in the treatment of HFrEF performed in a Bayesian hierarchical framework (Jansen et al. 2008; Jonas et al. 2013), and explored the advantages of various TCMIs to provide references for clinical decision-making.

## INFORMATION AND METHODS

The protocol of this study has been registered in PROSPERO (registration number: CRD42020166900) and has been published in an open-access journal (Lin et al. 2020). The NMA was performed in accordance with the Preferred Reporting Items for Systematic Review and Meta-Analysis (PRISMA) extension statement for reporting of systematic reviews incorporating network meta-analyses of healthcare interventions (Hutton et al. 2015). See Supplementary File S1 for a completed PRISMA checklist.

## Inclusion and Exclusion Criteria

### Participants

The population was HF patients in the stable phase or acute exacerbation phase. The patient met the recognized diagnostic criteria, such as the “CCS/CHFS Heart Failure Guidelines Update: Defining a New Pharmacologic Standard of Care for Heart Failure With Reduced Ejection Fraction” (McDonald et al. 2021), the “Guidelines for diagnosis and treatment of heart failure in China 2018” (Heart Failure Group of Chinses Society of Cardiology of Chinses Medical Association et al. 2018), the “2016 ESC Guidelines for the diagnosis and treatment of acute and chronic heart failure” (Ponikowski et al. 2016) and so on, while meeting the condition of LVEF <50%. Primary diseases included coronary heart disease, hypertension, dilated cardiomyopathy, and rheumatic heart disease. Sex, age, race, and source of the case were not limited.

Interventions and Comparisons

① Conventional treatment for HF (CT_{HF}) + TCMI vs. CT_{HF} (with or without placebo); ② CT_{HF} + TCMI_{a} vs. CT_{HF} + TCMI_{b}. In the control group and the test group, the CT_{HF} is the same, and both follow national or international guidelines. TCMIs have been approved by the China Food and Drug Administration, and the drug instructions specifically defined its indications including HF or other acute and chronic diseases caused by cardiac insufficiency.

### Outcomes

- Primary outcomes: ① New York Heart Association (NYHA) cardiac functional classification efficiency: according to the NYHA cardiac function classification standard, the degree of improvement of cardiac function was rated as “markedly effective” (NYHA grade increased by ≥2), “effective” (NYHA grade increased by 1), or “ineffective” (NYHA grade remained unchanged or even deteriorated). Total effective rate = (“markedly effective” patients + “effective” patients)/all patients × 100%. ② 6-min walking test (6MWT).
- Secondary outcomes: ① left ventricular ejection fraction (LVEF); ② left ventricular end-diastolic diameter (LVEDD); ③ left ventricular end-systolic diameter (LVESD); ④ cardiac output (CO); ⑤ stroke volume (SV); ⑥ brain natriuretic peptide (BNP); ⑦ N-terminal pro-brain natriuretic peptide (NT-proBNP); ⑧ Minnesota Living with Heart Failure Questionnaire (MLHFQ); ⑨ adverse drug event: any untoward medical occurrence during treatment.

### Type of Study

Clinical randomized controlled trials (RCTs).

### Exclusion Criteria

- Participants were any of the following: HF with malignant arrhythmias, malignant tumors, hypothyroidism, severe liver and kidney dysfunction, or severe infections.
- Study with imbalanced or incomparable baseline data between the two groups.
- The study cannot be integrated because of incorrect data or incomplete information.
- For republished studies, choose the one with the most complete data.
- The full text cannot be obtained after seeking help online or contacting the corresponding author via email.
- Unfinished protocol.

### Search Strategy

The clinical RCTs of TCMIs for treating HFrEF were searched in the relevant database, including PubMed, Embase, Cochrane Library, Chinese BioMedical Literature Database (CBM), China National Knowledge Infrastructure (CNKI), Wanfang Database, and VIP Chinese Science and Technology Journal Database (VIP). The retrieval time was from inception to August 3rd, 2021. According to the instructions, TCMIs that meet the inclusion criteria included Huangqi injection (HQ) also called Astragalus injection, Shenfu injection (SF), Shengmai injection (SGM), Shenmai injection (SM), Xinmailong injection (XML), and Yiqifumai lyophilized injection (YQFM). The search strategy was developed according to the Cochrane Handbook for Systematic Reviews (Higgins and Thomas, 2020) by two researchers (SSL with clinical work experience and QYS with evidence-based work experience). Search terms included heart failure, names of TCMIs that have been included, randomized controlled trial, and their synonyms. Besides, the reference lists of related documents were tracked to avoid omission. Take PubMed as an example. The detailed search strategy is shown in Supplementary File S2.

### Literature Screening, Data Extraction, and Risk of Bias Assessment

Records from databases were managed and screened using NoteExpress software (V3.2.0). The data extraction items included publication information (title, first author, journal name, publication year), participants' characteristics (diagnostic criteria, sample size, sex, age, ethnicity, case source, and baseline status), interventions (drug name, medication route, drug dose, course of treatment, and patient compliance), outcomes, risk of bias information, and others. The Cochrane Collaboration's tool (Higgins et al. 2011) was used to assess the risk of bias of included RCTs from the following seven items: ① random sequence generation; ② allocation concealment; ③ blinding participants and personnel; ④ blinding outcome assessment; ⑤ incomplete outcome data; ⑥ selective reporting; and ⑦ other bias. The results of the risk of bias assessment included the low risk of bias, the high risk of bias, and the unclear risk of bias. Data extraction and risk of bias assessment were independently completed and cross-checked by multiple researchers. Disagreements were resolved with the assistance of other researchers. The risk of bias graph was generated by Microsoft Excel.

### Statistical Analysis

A Bayesian model was used to conduct NMAs according to the Markov chain Monte Carlo method (Jansen et al. 2008). Dichotomous variables were presented as the relative risk (RR) or odds ratio (OR) with a 95% credible interval (CrI). Continuous variables were presented as the weight mean difference (WMD) with a 95% CrI. The χ^{2} test and I^{2} test were conducted to assess the potential heterogeneity. p < 0.05 was considered statistically significant. The random-effects model was selected to synthesize the data. The network diagram of each outcome was performed to visualize the connections between different interventions. The surface under the cumulative ranking curve (SUCRA) was performed to rank different interventions (Rücker and Schwarzer, 2015). The multi-dimensional efficacy analysis was performed to integrate the results of multiple outcomes to obtain the optimal intervention. The comparison-adjusted funnel plot was plotted to detect small sample size study effects and publication bias. The node-splitting analysis was used to split mixed evidence into direct evidence and indirect evidence to evaluate the consistency of the model. All analyses were conducted using R software (V3.6.1).

![img-0.jpeg](img-0.jpeg)

FIGURE 1 | Flowchart of the literature screening process. CBM, Chinese BioMedical Literature Database; CNKI, China National Knowledge Infrastructure; VIP, VIP Chinese Science and Technology Journal Database; LVEF, left ventricular ejection fraction; RCT, randomized controlled trial; n, the number of articles.

## RESULTS

### Literature Screening Result

A total of 9,360 records were initially obtained, and 2,344 possible related records were identified by reading the title and abstract. After reading the full text, 107 eligible studies were included in this NMA. The details of the literature screening process are shown in Figure 1.

### Basic Characteristics of Included Studies

One hundred and seven RCTs involving 9,073 HFrEF patients were included, conducted in China from 2003 to 2021. Most RCTs focused on SF (40 RCTs, 37.38%) (Que and Guo, 2003; Song et al., 2006; Chen et al., 2009; Hu et al., 2009; Huang, 2009; Wu and Duan, 2009; Yang and Wu, 2009; Zhu, 2009; Lv, 2010; Wu and Wang, 2010; Yao and Lu, 2010; Bao and Yu, 2011; Wang et al., 2011; Wu et al., 2011; Dong, 2012; Ding, 2013; Wang et al., 2014; Xu et al., 2014; Yu et al., 2014; Zhang et al., 2014; Pan, 2015; Qi, 2015; Qi and Qi, 2015; Xu et al., 2015; Mao, 2016; Wang et al., 2016; Wang and Pan, 2016; Wu, 2016; Yao et al., 2016; Zhang and Wen, 2016; Deng and Bai, 2017; He, 2017; Su, 2017; Yan et al., 2017; Zhang, 2017; Han, 2018; Li L. J., 2018; Liu et al., 2018; Zhang et al., 2018; Li J. P et al., 2020), followed by XML (23 RCTs, 21.50%) (Wu et al., 2012; Tang et al., 2013; Peng et al., 2014; Su et al., 2014; Yao et al., 2014; Zhao et al., 2014; Feng et al., 2015; Liu, 2015; Liu et al., 2015; Zhong, 2016; Wang, 2017; Li X. L., 2018; Su et al., 2018; Xu S.L. et al., 2018; Zhang, 2018; Hao, 2019; Hao et al., 2019; Mao, 2019; Wang, 2019; Xue et al., 2019; Li, 2020; Xi, 2020; Wang et al., 2021), SM (22 RCTs, 20.56%) (Chen and Zhou, 2010; Huang et al., 2011; Lan and Wei, 2011; Wang and Wu, 2012; Li, 2013; Lin and Bao, 2013; Zhai, 2013; Wang, 2014; Yu et al., 2015; Li et al., 2016; Yang, 2016; Yang et al., 2016; He et al., 2018; Li L, 2018; Xu E. W. et al., 2018; An and Xiao, 2019; Cui et al., 2019; Wang, 2019; He et al., 2020; Chen 2021; Jiang 2021; Zhang et al., 2021), SGM (10 RCTs, 9.35%) (Chen et al., 2008; Liu, 2008; Lu et al., 2008; Zhang, 2008; Kong, 2010; Xu et al., 2011; Ding et al., 2012; Pan, 2013; Qi, 2015; Li J. F., 2018), HQ (8 RCTs, 7.48%) (Liu and Fu, 2003; Wang, 2003; Wu and Chen, 2005; Guo and Chen, 2006; Xing and Nie, 2006; Su et al., 2014; Sun, 2016; Gan, 2019), and YQFM (7 RCTs, 6.54%) (Yu and Wang, 2012; Yuan and Du, 2012; Li, 2014; Guo, 2015; Zhao, 2015; Tao et al., 2020; Kou 2021). As recommended by the international HF guidelines (Ponikowski et al., 2016; Heart Failure Group of Chinses Society of Cardiology of Chinses Medical Association et al., 2018; McDonald et al., 2021), CT<sub>HF</sub> included angiotensin-converting enzyme inhibitor (ACEI), angiotensin receptor blocker (ARB),

TABLE 1 | Characteristics of the studies included in this network meta-analysis.


(Continued on following page)

TABLE 1 | (Continued) Characteristics of the studies included in this network meta-analysis.


(Continued on following page)

TABLE 1 | (Continued) Characteristics of the studies included in this network meta-analysis.


(Continued on following page)

TABLE 1 | (Continued) Characteristics of the studies included in this network meta-analysis.


TABLE 1 | (Continued) Characteristics of the studies included in this network meta-analysis.


${ }^{a}$ Age is described in the form of mean $\pm$ standard deviation or mean (minimum - maximum). ${ }^{a}$ "CT $*{\mathrm{HF}}$ " refers to the conventional treatment for heart failure in the international heart failure guidelines, including angiotensin-converting enzyme inhibitor (such as captopril, enalapril), angiotensin receptor blocker (such as valsartan, irbesartan), $\beta$-blocker (such as metoprolol), mineralocorticoid receptor antagonists (spironolactone), cardiotonic drugs (such as digoxin), anticoagulant and antiplatelet drugs(such as aspirin), and so on. These drugs were the conventional doses recommended in the guidelines and needed to be adjusted according to the patient's condition, especially $\beta$-blockers and diuretics. However, the treatment plan and principles of the "CT $*{\mathrm{HF}}$ " of the test group and the control group were the same. LVEF, left ventricular ejection fraction; F, female; M, male; T, test group; C, control group; HQ, Huangqi injection; SF, Shenfu injection; SGM, Shengmai injection; SM, Shenmai injection; XML, Xinmailong injection; YQFM, Yojifumai (yophilized injection; d, day(s); w, week(s). (2) New York Heart Association cardiac functional classification efficiency; (2) 6-min walking test; (2) left ventricular ejection fraction; (2) left ventricular end-diastolic diameter; (2) left ventricular end-systolic diameter; (2) cardiac output; (2) stroke volume; (2) brain natriuretic peptide; (2) N-terminal pro-brain natriuretic peptide; (2) Minnesota Living with Heart Failure Questionnaire; (2) adverse drug event.

![img-1.jpeg](img-1.jpeg)

FIGURE 2 | Network diagrams for different outcomes. (A) New York Heart Association cardiac functional classification efficiency; (B) 6-min walking test; (C) left ventricular ejection fraction; (D) left ventricular end-diastolic diameter; (E) left ventricular end-systolic diameter; (F) cardiac output; (G) stroke volume; (H) brain natriuretic peptide; (I) N-terminal pro-brain natriuretic peptide; (J) Minnesota Living with Heart Failure Questionnaire. CT, conventional treatment; HQ, Huangqi injection; SF, Shenfu injection; SGM, Shengmai injection; SM, Shenmai injection; XML, Xinmailong injection; YQFM, Yiqifumai lyophilized injection.

![img-2.jpeg](img-2.jpeg)

FIGURE 3 | Risk of bias graph of the included RCTs. The vertical axis represents the risk of bias items, and the horizontal axis represents the percentage of the number of RCTs. For the outcome whose evaluation process is objective, the "unclear risk of bias" should be regarded as "low risk of bias".

β-blocker, mineralocorticoid receptor antagonists, diuretics, vasodilators, cardiotonic drugs, antiplatelet drugs, anticoagulant drugs, and so on. There was slight variability in the medication depending on the patient's condition. However, the medication principles of all RCTs followed the recommendations of the guidelines. The course of treatment ranged from 5 days to 12 weeks. Details are shown in Table 1. The network diagrams of the above 6 TCMIs with different outcomes are shown in Figure 2.

## Risk of Bias Assessment

The results of the risk of bias assessment are as follows. ① Random sequence generation: 34 studies (Wang, 2003; Hu, et al., 2009; Zhang et al., 2014; Wu, 2016; Yao et al., 2016; Zhang et al., 2018; Qi and Qi, 2015; Wang et al., 2014; Song et al., 2006; Xu et al., 2014; Su, 2017; Wang et al., 2011; Pan, 2015; Yan et al., 2017; Li X. L., 2018; Pan, 2013; Kong, 2010; Zhai, 2013; Li et al., 2016; An and Xiao, 2019; He et al., 2020; He et al., 2018; Xu S. L. et al., 2018; Wang, 2017; Xue et al., 2019; Xu E. W. et al., 2018; Li J. F., 2018; Zhang, 2018; Li, 2020; Tao et al., 2020; Wang et al., 2021; Chen 2021; Jiang 2021; Kou 2021) were evaluated as low risk due to the use of a random number table, one study that was randomly grouped according to the order of visits (Ding et al., 2012) was assessed as high risk, and other studies did not describe specific randomization methods. ② Allocation concealment: one study (Xue et al., 2019) was evaluated as low risk due to the use of center allocation, and one study (Ding et al., 2012) was evaluated as high risk due to the failure of allocation concealment. ③ Blinding participants and personnel: two double-blind studies (Qi, 2015; Xue et al., 2019) were evaluated as low risk, two single-blind study (Wu and Duan, 2009; Mao, 2019) was high-risk, and other studies did not mention blinding. ④ Blinding outcome assessment: one study using center allocation (Xue et al., 2019) was evaluated as low-risk, and other studies did not mention whether the evaluators were blinded. ⑤ Incomplete outcome data: there was no missing data in all studies. ⑥ Selective report: all studies did not provide a protocol, so the risk of selective reporting was unclear. ⑦ Other bias: there was not enough information to assess whether there were other biases. The summary of the risk of bias of the included RCTs is shown in Figure 3.

## Results of the Network Meta-Analysis

### NYHA Cardiac Functional Classification Efficiency

A total of 48 RCTs reported the NYHA cardiac functional classification efficiency, including six types of TCMIs and seven types of interventions (CT vs. CT + HQ (n = 4), CT vs. CT + SF (n = 28), CT vs. CT + SGM (n = 3), CT vs. CT + SM (n = 4), CT vs. CT + XML (n = 6), CT vs. CT + YQFM (n = 2), and CT + SM vs. CT + XML (n = 1)) (Table 1). The network diagram is shown in Figure 2. All TCMIs combined with CT were superior to CT alone, and the difference was statistically significant. The details are shown in Table 2: CT vs. CT + HQ (OR = 0.18, 95% CrI: 0.07–0.38), CT + SF vs. CT (OR = 0.25, 95% CrI: 0.19–0.33), CT vs. CT + SGM (OR = 0.36, 95% CrI: 0.16–0.72), CT vs. CT + SM (OR = 0.24, 95% CrI: 0.13–0.43), CT vs. CT + XML (OR = 0.18, 95% CrI: 0.11–0.31), and CT vs. CT + YQFM (OR = 0.38, 95% CrI: 0.19–0.71).

According to SUCRA probability results (Figure 4; Table 3), CT + XML was the most likely to be the best intervention for improving the NYHA cardiac functional classification efficiency. The ranking of seven interventions is as follows: CT + XML (81.36%) > CT + HQ (80.87%) > CT + SM (62.19%) > CT + SF (58.46%) > CT + SGM (34.68%) > CT + YQFM (32.39%) > CT (0.05%).

### 6MWT

A total of 31 RCTs reported 6MWT, including five types of TCMIs and six types of interventions (CT vs. CT + SF (n = 7), CT vs. CT + SM (n = 7), CT vs. CT + XML (n = 13), CT vs. CT + YQFM (n = 3), and CT + SM vs. CT + XML (n = 1)) (Table 1). The network diagram is shown in Figure 2. Apart from HQ, other TCMIs combined with CT were superior to CT alone, and the difference was statistically significant. The details are shown in Table 2: CT vs. CT + SF (WMD = -42.29 m, 95% CrI: -62.99~-22.02 m), CT vs. CT + SM (WMD = -54.92 m, 95%

TABLE 2 | Odds ratio/weight mean difference (95% credible interval) results of the network meta-analysis.


TABLE 2 | (Continued) Odds ratio/weight mean difference (95% credible interval) results of the network meta-analysis.


The bolded values indicate statistical significance. NYHA, New York Heart Association cardiac functional classification efficiency; 6WMT, 6-min walking test; LVEF, left ventricular ejection fraction; LVEDD, left ventricular end-diastolic diameter; LVESD, left ventricular end-systolic diameter; CO, cardiac output; SV, stroke volume; BNP, brain natriuretic peptide; NT-proBNP, N-terminal pro-brain natriuretic peptide; MLHFQ, Minnesota Living with Heart Failure Questionnaire; CT, conventional treatment; HQ, Huangqi injection; SF, Shenfu injection; SGM, Shengmai injection; SM, Shenmai injection; XML, Xinmailong injection; YQFM, Yiqifumai lyophilized injection. ${ }^{a}$ Indicates that the value is odds ratio.

CrI: $-76.68 \sim-32.32 \mathrm{~m})$, CT vs. CT + XML (WMD $=-51.9 \mathrm{~m} 0$, $95 \%$ CrI: $-68.50 \sim-35.82 \mathrm{~m})$, and CT vs. CT + YQFM (WMD $=$ $-43.56 \mathrm{~m}, 95 \%$ CrI: $-74.43 \sim-13.17 \mathrm{~m})$. In addition, there were statistically significant differences between CT + HQ and CT combined with other injections. As shown in Table 2: CT + HQ vs. CT + SF (WMD $=-68.87 \mathrm{~m}, 95 \%$ CrI: $-128.52 \sim-8.05 \mathrm{~m}), \mathrm{CT}+$ HQ vs. CT + SM (WMD $=-81.61 \mathrm{~m}, 95 \%$ CrI: $-141.43 \sim-19.86 \mathrm{~m}), \mathrm{CT}+$ HQ vs. CT + XML (WMD $=-78.73 \mathrm{~m}, 95 \%$ CrI: $-133.10 \sim-23.97 \mathrm{~m})$, and CT + HQ vs. CT + YQFM (WMD $=-70.41 \mathrm{~m}, 95 \%$ CrI: $-134.81 \sim-5.47 \mathrm{~m})$ had more advantages in improving 6MWT.

According to SUCRA probability results (Figure 4; Table 3), CT + SM was the most likely to become the best intervention for improving 6MWT. The ranking of six interventions is as follows:

CT + SM $(82.25 \%)>$ CT + XML $(77.40 \%)>$ CT + YQFM $(61.84 \%)>\mathrm{CT}+\mathrm{SF}(57.62 \%)>\mathrm{CT}(16.60 \%)>\mathrm{CT}+\mathrm{HQ}(4.30 \%)$.

## LVEF

A total of 91 RCTs reported LVEF, including six types of TCMIs and seven types of interventions (CT vs. CT + HQ $(n=7)$, CT vs. CT $+\mathrm{SF}(n=28)$, CT vs. CT + SGM $(n=7)$, CT vs. CT + SM $(n=19)$, CT vs. CT + XML $(n=20)$, CT vs. CT + YQFM $(n=7)$, CT + HQ vs. CT + XML $(n=1)$, CT + SM vs. CT + XML $(n=1)$, and CT + SGM vs. CT + SF $(n=1))$ (Table 1). The network diagram is shown in Figure 2. All TCMIs combined with CT were superior to CT alone, and the difference was statistically significant. The details are shown in Table 2.

![img-3.jpeg](img-3.jpeg)

**FIGURE 4** Surface under the cumulative ranking curve (SUCRA) plots for different outcomes. The vertical axis represents cumulative probabilities and the horizontal axis represents rank. NYHA, New York Heart Association cardiac functional classification efficiency; 6WMT, 6-min walking test; LVEF, left ventricular ejection fraction; LVEDD, left ventricular end-diastolic diameter; LVESD, left ventricular end-systolic diameter; CO, cardiac output; SV, stroke volume; BNP, brain natriuretic peptide; NT-proBNP, N-terminal pro-brain natriuretic peptide; MLHFQ, Minnesota Living with Heart Failure Questionnaire; CT, conventional treatment; HQ, Huangqi injection; SF, Shenfu injection; SGM, Shengmai injection; SM, Shenmai injection; XML, Xinmailong injection; YQFM, Yiqifumai lyophilized injection.

According to SUCRA probability results (**Figure 4**; **Table 3**), CT + YQFM was the most likely to become the best intervention for improving LVEDD. The ranking of seven interventions is as follows: CT + YQFM (85.88%) > CT + SM (74.75%) > CT + SF (52.46%) > CT + HQ (51.52%) > CT + XML (48.54%) > CT + SGM (36.85%) > CT (0.01%).

### LVEDD

A total of 38 RCTs reported LVEDD, including six types of TCMIs and seven types of interventions (CT vs. CT + HQ (*n* = 2), CT vs. CT + SF (*n* = 15), CT vs. CT + SGM (*n* = 2), CT vs. CT + SM (*n* = 8), CT vs. CT + XML (*n* = 8), and CT vs. CT + YQFM (*n* = 3)) (**Table 1**). The network diagram is shown in **Figure 2**. Apart from HQ and YQFM, other TCMIs combined with CT were superior to CT alone, and the difference was statistically significant. In addition, there were also statistically significant differences between different injections, such as CT + SF vs. CT + SGM, CT + SF vs. CT + SM, CT + SF vs. CT + XML, CT + SF vs. CT + YQFM, and CT + XML vs. CT + YQFM. The details are shown in **Table 2**.

According to SUCRA probability results (**Figure 4**; **Table 3**), CT + SM was the most likely to become the best intervention for improving LVEDD. The ranking of seven interventions is as follows: CT + SM (82.06%) > CT + XML (75.00%) > CT + SGM (74.36%) > CT + SF (47.04%) > CT + HQ (34.69%) > CT + YQFM (31.51%) > CT (5.34%).

### LVESD

A total of 15 RCTs reported LVESD, including six types of TCMIs and seven types of interventions (CT vs. CT + HQ (*n* = 2), CT vs. CT + SF (*n* = 3), CT vs. CT + SGM (*n* = 2), CT vs. CT + SM (*n* = 4), CT vs. CT + XML (*n* = 3), and CT vs. CT + YQFM (*n* = 1)) (**Table 1**). The network diagram is shown in **Figure 2**. **Table 2** shows that only XML combined with CT were superior to CT alone, and the difference was statistically significant.

According to SUCRA probability results (**Figure 4**; **Table 3**), CT + SM was the most likely to become the best intervention for improving LVESD. The ranking of six interventions is as follows: CT + SM (84.72%) > CT + YQFM (72.23%) > CT + SGM (49.29%) > CT + HQ (47.73%) > CT + SF (46.65%) > CT + XML (44.75%) > CT (4.63%).

### CO

A total of 19 RCTs reported CO, including five types of TCMIs and six types of interventions (CT vs. CT + HQ (*n* = 2), CT vs. CT + SF (*n* = 7), CT vs. CT + SGM (*n* = 5), CT vs. CT + SM (*n* = 3), CT vs. CT + XML (*n* = 1), and CT + SF vs. CT + SGM (*n* = 1)) (**Table 1**). The network diagram is shown in **Figure 2**. Apart from XML, other TCMIs combined with CT were superior to CT alone, and the difference was statistically significant. The details are shown in **Table 2**.

According to SUCRA probability results (**Figure 4**; **Table 3**), CT + SM was the most likely to become the best intervention for improving CO. The ranking of six interventions is as follows: CT + SM (75.03%) > CT + HQ (73.69%) > CT + SGM (66.25%) > CT + SF (51.43%) > CT + XML (28.52%) > CT (5.08%).

### SV

A total of 24 RCTs reported SV, including five types of TCMIs and six types of interventions (CT vs. CT + HQ (*n* = 3), CT vs. CT + SF (*n* = 7), CT vs. CT + SGM (*n* = 4), CT vs. CT + SM (*n* = 6), CT

TABLE 3 | Results of the surface under the cumulative ranking curve (SUCRA) (\%).


The redder the color, the greater the SUCRA, and the greater the probability of becoming the best intervention. The greener the color, the smaller the SUCRA, and the smaller the probability of becoming the best intervention. NYHA, New York Heart Association cardiac functional classification efficiency; 6WMT, 6-min walking test; LVEF, left ventricular ejection fraction; LVEDD, left ventricular end-diastolic diameter; LVESD, left ventricular end-systolic diameter; CO, cardiac output; SV, stroke volume; BNP, brain natriuretic peptide; NT-proBNP, N-terminal pro-brain natriuretic peptide; MLHFQ, Minnesota Living with Heart failure questionnaire; CT, conventional treatment; HQ, Huangqi injection; SF, Shenfu injection; SGM, Shengmai injection; SM, Shenmai injection; XML, Xinmailong injection; YQFM, Yiqifumai lyophilized injection. vs. CT + XML $(n=3)$, and CT + SF vs. CT + SGM $(n=1))$ (Table 1). The network diagram is shown in Figure 2. Table 2 shows that only HQ, SF, and YQFM combined with CT were superior to CT alone, and the difference was statistically significant.

According to SUCRA probability results (Figure 4; Table 3), CT + HQ was the most likely to become the best intervention for improving SV. The ranking of six interventions is as follows: CT + HQ $(82.24 \%)>$ CT + SF $(72.55 \%)>$ CT + XML $(64.18 \%)>$ CT + $\mathrm{SM}(44.51 \%)>\mathrm{CT}+\mathrm{SGM}(33.85 \%)>\mathrm{CT}(2.68 \%)$.

## BNP

A total of 32 RCTs reported BNP, including five types of TCMIs and six types of interventions ( CT vs. CT + HQ $(n=2), \mathrm{CT}$ vs. CT + SF $(n=$ 14), CT vs. CT + SGM $(n=1)$, CT vs. CT + SM $(n=4)$, CT vs. CT + XML $(n=9), \mathrm{CT}+\mathrm{HQ}$ vs. CT + XML $(n=1)$, and CT + SM vs. CT + XML $(n=1))$ (Table 1). The network diagram is shown in Figure 2. Table 2 shows that only SF and XML combined with CT were superior to CT alone, and the difference was statistically significant.

According to SUCRA probability results (Figure 4; Table 3), CT + XML $(87.11 \%)$ was the most likely to become the best intervention for improving BNP. The ranking of six interventions is as follows: CT + XML $(87.16 \%)>$ CT + SF $(69.84 \%)>$ CT + SM $(61.54 \%)>$ CT $+\mathrm{HQ}(34.67 \%)>\mathrm{CT}+\mathrm{SGM}(31.67 \%)>\mathrm{CT}(15.12 \%)$.

## NT-proBNP

A total of 31 RCTs reported NT-proBNP, including five types of TCMIs and six types of interventions (CT vs. CT + SF $(n=11)$, CT vs. CT + SGM $(n=1)$, CT vs. CT + SM $(n=7)$, CT vs. CT + XML $(n=8)$, and CT vs. CT + YQFM $(n=4))$ (Table 1). The network diagram is shown in Figure 2. Table 2 shows that only SF, SM, and XML combined with CT were superior to CT alone, and the difference was statistically significant.

According to SUCRA probability results (Figure 4; Table 3), $\mathrm{CT}+$ XML was the most likely to become the best intervention for improving NT-proBNP. The ranking of six interventions is as follows: CT + XML $(86.74 \%)>\mathrm{CT}+\mathrm{SM}(68.73 \%)>\mathrm{CT}+\mathrm{SGM}$ $(51.07 \%)>\mathrm{CT}+\mathrm{SF}(45.71 \%)>\mathrm{CT}+\mathrm{YQFM}(39.25 \%)>$ CT $(8.51 \%)$.

## MLHFQ

A total of 11 RCTs reported MLHFQ, including five types of TCMIs and six types of interventions (CT vs. CT + HQ $(n=1)$, CT vs. CT + SF $(n=3)$, CT vs. CT + SM $(n=2)$, CT vs. CT + XML $(n=4)$, and CT vs. CT + YQFM $(n=1))$ (Table 1). The network diagram is shown in Figure 2. Table 2 shows that only SF and XML combined with CT were superior to CT alone, and the difference was statistically significant.

According to SUCRA probability results (Figure 4; Table 3), CT + SF was the most likely to become the best intervention for improving MLHFQ. The ranking of six interventions is as follows: CT + SF $(72.90 \%)>\mathrm{CT}+$ XML $(70.03 \%)>\mathrm{CT}+$ HQ $(62.91 \%)>\mathrm{CT}+\mathrm{SM}(48.88 \%)>\mathrm{CT}+\mathrm{YQFM}(35.95 \%)>$ CT $(9.73 \%)$.

## Safety

Forty RCTs focused on adverse drug reactions (ADRs), mainly including dizziness and headache, gastrointestinal discomfort, skin allergic reactions, lowered blood pressure, and abnormal heart rhythm. Considering that the criteria for ADR in each RCT were not completely consistent, a descriptive analysis was carried out. Given the small sample size, it is not yet possible to prove that the difference between the two groups is statistically significant. Details are shown in Tables 1, 4.

## Multi-Dimensional Efficacy Analysis

This multi-dimensional efficacy analysis method integrated the results of multiple outcomes to obtain the optimal intervention. The results based on currently available clinical data indicate that, in terms of the primary outcomes (NYHA cardiac functional classification efficiency and 6WMT), CT + XML and CT + SM may be the best two treatments, followed by CT + SF, CT + YQFM, CT + HQ, and CT + SGM (Figure 5A). In terms of NYHA cardiac functional classification efficiency and the most

TABLE 4: Summary of adverse drug events.


RCTs, randomized controlled trials; CT, conventional treatment; HQ, Huangqi injection; SF, Shenfu injection; SGM, Shengmai injection; SM, Shenmai injection; XML, Xinmailong injection; YQFM, Yiqifumai lyophilized injection.

![img-4.jpeg](img-4.jpeg)

FIGURE 5 | Multi-dimensional efficacy analysis results. (A) NYHA and 6WMT; (B) NYHA and LVEF; (C) NYHA and BNP. Interventions located in the upper right corner indicate optimal therapy for two different outcomes. NYHA, New York Heart Association cardiac functional classification efficiency; 6WMT, 6-min walking test; LVEF, left ventricular ejection fraction; BNP, brain natriuretic peptide; CT, conventional treatment; HQ, Huangqi injection; SF, Shenfu injection; SGM, Shengmai injection; SM, Shenmai injection; XML, Xinmailong injection; YQFM, Yiqifumai lyophilized injection.

common cardiac ultrasound index LVEF, CT + SM, CT + HQ, CT + XML, and CT + YQFM may all be potentially optimal choices (Figure 5B). Also, in terms of NYHA cardiac functional classification efficiency and the most common laboratory test index BNP, CT + XML may be the optimal choice (Figure 5C).

### Publication Bias

The comparison-adjusted funnel plots for each outcome were plotted, the result of LVEF with the biggest sample size is shown in Figure 6. The points in the funnel chart were asymmetric based on the position of the centerline, and the scatter was found to be symmetrical along the null line to the left and right, indicating that there was no small sample effect and publication bias. Funnel plots of all outcomes were shown in Supplementary File S3.

### Consistency Tests

As shown in Figure 2, there are some closed loops in the NYHA cardiac function classification efficiency, 6WMT, LVEF, CO, SV, and BNP network diagram. Therefore, the node-splitting analysis was used to evaluate the inconsistency of the model. Figure 7 shows that there

![img-5.jpeg](img-5.jpeg)

FIGURE 6 | Funnel plot of left ventricular ejection fraction. CT, conventional treatment; HQ, Huangqi injection; SF, Shenfu injection; SGM, Shengmai injection; SM, Shenmai injection; XML, Xinmailong injection; YQFM, Yiqifumai lyophilized injection.

![img-6.jpeg](img-6.jpeg)

FIGURE 7 | Consistency test for the New York Heart Association cardiac functional classification efficiency. CT, conventional treatment; SM, Shenmai injection; XML, Xinmailong injection.

was no statistically significant inconsistency in the closed-loop of NYHA cardiac functional classification efficiency (p > 0.05), indicating that the results on NYHA cardiac functional classification efficiency were reliable. The detailed results of the consistency test for all outcomes are shown in Supplementary File S4.

# DISCUSSION

## Scientific Significance

At present, the highly contagious novel coronavirus (severe acute respiratory syndrome coronavirus 2, SARS-CoV2) has ravaged more than 200 countries around the world, triggering a global pandemic of coronavirus disease 2019 (COVID-19). Due to the unclear pathogenesis of COVID-19, there is no specific medicine in western medicine, which has caused a large number of deaths worldwide. Globally, as of 10:37am CEST, August 9, 2021, there have been 202,296,216 confirmed cases of COVID-19, including 4,288,134 deaths, reported to World Health Organization (https://covid19.who.int/). During the pandemic, the Chinese government proposes that TCM combined with western medicine can be used in treating COVID-19. TCM has been playing an irreplaceable role, significantly improving the quality of life of the affected population and reducing the mortality rate (Zhao et al., 2021). It is worth mentioning that TCM is not only widely used in China, but also transported to and served in many epidemic areas around the world. The unique advantages and clinical value of TCM have received increasing attention from all over the world.

TCM has accumulated thousands of years of clinical experience in the treatment of many diseases. Among them, HF is one of the dominant diseases of TCM. In 2018, the "Guidelines for diagnosis and treatment of heart failure in China 2018" (Heart Failure Group of Chinese Society of Cardiology of Chinese Medical Association et al., 2018) officially listed TCM as a recommendation for the treatment of HF. At present, the combination of traditional Chinese and Western medicine has become the basic model for the treatment of HF in China. Epidemiological investigations show that the common pathogenesis includes hypertension, cardiomyopathy, rheumatic heart disease, etc., of which ischemic heart disease is a major contributor to HF in Asia (Sakata and Shimokawa, 2013). According to the theory of TCM, the main pathogenesis of HF is "Qi deficiency (the lack of energy in the body in modern medicine, usually manifested as fatigue, spontaneous sweating, etc.) and blood stasis (an abnormal hemodynamic state in which blood tends to clot in modern medicine)". The raw materials for the preparation of TCMIs are derived from total extracts, active

parts or monomeric active ingredients extracted from traditional herbal medicines or traditional animal medicines. Through modern technology, further liquid preparation, purification, distillation, sterilization, etc. are accurately implemented to complete the entire preparation process.

The TCMIs included in this study all have the effect of nourishing Qi and blood. And a large number of articles and reviews have explored the protective effects of the active ingredients of these TCMIs on cardiovascular diseases in terms of molecular mechanisms, such as Huang-Qi (Radix Astragali) (Su et al., 2021) in HQ, the combination of Ren-Shen (Radix Ginseng) and Fu-Zi (processed) (Radix Aconiti Lateralis Preparata) (Tan et al., 2018; Li L. et al., 2020) in SF, the combination of Hong-Shen (Radix Ginseng Rubra) and Mai-Dong (Radix Ophiopogonis) (Wang et al., 2019) in SM and YQFM, Wu-Wei-Zi (Fructus Schisandrae) (Nasser et al., 2020) in SGM, and American cockroach (Periplaneta Americana Linnaeus) (Qi et al., 2017; Lin S. S. et al., 2019) in XML. Due to the available active ingredients, rich and diverse targets, and complex regulatory mechanisms, TCMIs have considerable development potential. This study clarified the clinical advantages of different TCMIs by performing an NMA. On the one hand, it will provide a reference for the rational use of TCMIs. On the other hand, molecular studies based on the clinical characteristics of TCMIs can provide ideas and clues for the development of new drugs.

## Summary of Main Findings

This NMA incorporated 107 RCTs on the efficacy and safety of TCM combined with CT in the treatment of HFrEF, including 9,073 patients and 6 TCMs. Among them, TCMIs include HQ, SF, SGM, SM, XML, and YQFM. In terms of clinical efficacy, the combination of CT + XML may be the most effective in improving NYHA cardiac functional classification efficiency, BNP, and NT-proBNP; the combination of CT + SM may be the most effective in improving 6MWT, LVEDD, LVESD, and CO; the combination of CT + YQFM may be the most effective in improving LVEF; the combination of CT + HQ may be the most effective in improving SV; the combination of CT + SF may be the most effective in improving MLHFQ. The results based on currently available clinical data show that the ranking results of TCMIs in various outcomes are inconsistent. Each species has its own advantages. Among them, the overall evaluation of CT + XML and CT + SM is relatively good. In terms of safety, CT + TCMIs may cause additional ADR events. However, there was no significant difference compared with the CT. The recommendation of clinical drugs requires a multi-dimensional evaluation system. In this study, NYHA and 6WMT were used as the primary outcome indicators for the comprehensive evaluation, and the results showed that CT + XML and CT + SM may be the best two treatments, followed by CT + SF, CT + YQFM, CT + HQ, and CT + SGM. Depending on the research focus and the primary outcome indicators, the conclusions may change accordingly.

In this study, there is no proof of publication bias. In addition, there are both direct comparison and indirect comparison evidence in the evaluation of six outcome indicators, including NYHA cardiac function classification efficiency, 6WMT, LVEF, CO, SV, and BNP. The consistency test results showed that, except for BNP, the consistency between the direct and indirect research evidence of other outcome indicators was good, and the evidence-based conclusions were stable and reliable. The increase in BNP is related to many diseases. In addition to HF, senile diseases such as atrial fibrillation (Silvet et al., 2003), chronic obstructive pulmonary disease (Inoue et al., 2009), and renal insufficiency (McCullough et al., 2003) can also cause non-specific increases in BNP. Although this study excluded patients with severe comorbidities as much as possible, the included population was mostly elderly patients, and individual differences had a greater impact on BNP levels, which may be the reason for the unstable evidence of BNP.

## Innovations and Limitations of This Study

At present, some researchers have performed NMAs on TCMIs for the treatment of HF (Wang et al., 2018; Yang et al., 2018). However, these studies did not consider the clinical heterogeneity between HF patients with different types of ejection fraction. A study showed that compared with heart failure with preserved ejection fraction (HFpEF), HFrEF is more related to high levels of BNP, troponin T, creatinine, uric acid, glycosylated hemoglobin levels, and the proportion of coronary heart disease (Liu et al., 2016). Considering that there may be significant differences in the pathophysiological process between HFrEF and HFpEF (Putko et al., 2021), we believe that research on different types of HF is more realistic for exploring personalized treatment plans. Therefore, we selected HFrEF with more severe clinical symptoms and more sufficient clinical data as the research object to reduce clinical heterogeneity and obtain more reliable evidence.

In addition, this study has some limitations: 1) The overall quality of the included RCTs is low. Most RCTs did not report in detail on random methods, blinding, allocation concealment, and program registration. These limitations may lead to serious risks of bias. Therefore, it is recommended that clinical research should be implemented strictly in accordance with the CONSORT checklist (Moher et al., 2012). 2) Due to the lack of clinical data, this study failed to report outcomes that directly reflect the clinical benefit and prognosis of patients, such as mortality and rehospitalization rates. 3) Since all the studies were conducted in China, the external adaptability of the conclusions will be limited to a certain extent.

## CONCLUSION

In summary, the NMA results show that compared with CT alone, the combination of qualified TCMIs and CT is more effective for HFrEF patients. Among them, CT + XML and CT + SM may be the potential optimal treatment. Besides, the safety of these TCMIs needs to be further observed through more studies using unified observation indicators that reflect safety. However, due to some limitations, the conclusions need to be verified by more large-sample, double-blind, multi-center RCTs in the future.

## AUTHOR CONTRIBUTIONS

SL is responsible for the entire research design process, especially conceptualization and methodology. JM and XW were responsible for the conceptualization, funding acquisition, and project administration. All the authors took part in the data curation, formal analysis, and visualization. SL finished the writing-original draft and all the authors participated in the writing-review and editing.

## FUNDING

This work was supported by the "Innovation Team Development Plan" of the Ministry of Education-Research on the prevention and treatment of cardiovascular diseases in traditional Chinese medicine (No. IRT_16R54), the

## SUPPLEMENTARY MATERIAL

The Supplementary Material for this article can be found online at: https://www.frontiersin.org/articles/10.3389/fphar.2021.659707/ full\#supplementary-material

Dong, Y. J. (2012). Effect of Shenfu Injection Combined with Western Medicine in the Treatment of Coronary Heart Disease with Heart Failure and its Effect on BNP. China Pract. Med. 7 (17), 138-139. doi:10.14163/j.cnki.11-5547/r.2012.17.098
Feng, Y. P., Zheng, Z. L., Zhong, L. H., Zhao, L. P., Jia, W. C., Li, J. F., et al. (2015). Effect of Xinmailong Injection on Serum hsCRP, BNP and LDL-C in Patients with Heart Failure of Coronary Heart Disease. Chin. J. Integr. Med. Cardio-Cerebrovasc. Dis. 13 (09), 1089-1090. doi:10.3969/j.issn.16721349.2015.09.011
Gan, P. Z. (2019). Efficacy of Astragalus Injection in the Treatment of Chronic Heart Failure and its Effect on BNP and CA125. China Med. Pharm. 9 (09), 48-51. doi:10.3969/j.issn.2095-0616.2019.09.014
Guo, H., and Chen, H. W. (2006). Treatment of 42 Cases of Chronic Congestive Heart Failure with Huangqi Injection. Cent. Plains Med. J. 33 (02), 85-86. doi:10.3760/cma.j.issn.1674-4756.2006.02.070
Guo, S. L. (2015). Clinical Observation of Yuji Fumai Injection in the Treatment of Chronic Heart Failure. J. Pract. Med. Tech. 22 (02), 188-189.
Han, Y. X. (2018). Analysis of the Effect of Shenfu Injection in the Treatment of Heart Failure of Coronary Heart Disease. China Pract. Med. 13 (29), 116-118. doi:10.14163/j.cnki.11-5547/r.2018.29.064
Hao, J., Zhang, Z., Qi, C. M., Cai, W. B., Zhang, Q. D., Zhou, Q., et al. (2019). The Effect of Xinmailong Injection in Patients with Chronic Heart Failure. China Health Stand. Manage. 10 (20), 96-98. doi:10.3969/j.issn.16749316.2019.20.041
Hao, Q. Y. (2019). Clinical Study of Xinmailong Injection in the Treatment of Patients with Heart Failure Reduced Ejection Fraction. Master's thesis. Changsha, Hunan, China: Hunan Normal University.
He, J. Z., Hu, Q. Y., Jiang, J., Wu, Z. J., Huang, X. X., Xu, F. J., et al. (2018). Clinical Observation of Shenmai Injection Combined with Levosimendan in the Treatment of Severe Heart Failure. Chin. J. Rural Med. Pharm. 25 (08), 37-38. doi:10.19542/j.cnki.1006-5180.001511
He, J. Z., Lu, F., Qin, G., Wu, Z. J., and Hu, Q. Y. (2020). Therapeutic Effect of Shenmai Injection Combined with Mifrinone in Treatment of Refractory Heart Failure. Chin. Arch. Tradit. Chin. Med. 38 (01), 203-206. doi:10.13193/ j.issn.1673-7717.2020.01.049

He, M. M. (2017). Effect of Shenfu Injection on Cardiac Function and Ventricular Remodeling in Patients with Dilated Cardiomyopathy with Heart Failure. Health Guide (9), 310. doi:10.3969/j.issn.1006-6845.2017.09.292
Heart Failure Group of Chinses Society of Cardiology of Chinses Medical Association; Chinses Heart Failure Association of Chinses Medical Doctor Association; Editorial Board of Chinses Journar of Cardioloy (2018). Guidelines for Diagnosis and Treatment of Heart Failure in China 2018. Chin. J. Cardiol. 46 (10), 760-789. doi:10.3760/cma.j.issn.0253-3758.2018.10.004

Heidenreich, P. A., Albert, N. M., Allen, L. A., Bluemke, D. A., Butler, J., Fonarow, G. C., et al. (2013). Forecasting the Impact of Heart Failure in the United States: a Policy Statement from the American Heart Association. Circ. Heart Fail. 6 (3), 606-619. doi:10.1161/HHF.0b013e318291329a

Higgins, J. P., Altman, D. G., Gøtzsche, P. C., Jüni, P., Moher, D., Oxman, A. D., et al. (2011). The Cochrane Collaboration's Tool for Assessing Risk of Bias in Randomised Trials. BMJ 343, d5928. doi:10.1136/bmj.d5928
Hu, Y. H., Wu, H. Q., Qi, X., Wu, Hao., Zhou, Y. P., Shi, J., et al. (2009). Influence of Shenfu Injection on Heart Function and Bone Marrow Stem Cell Mobilization in Patients with Chronic Heart Failure of Coronary Heart Disease. Zhongguo Zhong Xi Yi Jie He Za Zhi 29 (04), 309-312. doi:10.3321/j.issn:10035370.2009.04.005
Huang, S. E., Huang, Q., Yao, Q., and Pei, D. A. (2011). Influence of Shenmai Injection on Chronic Contractive Heart Failure Patients' Heart Function and BNP. J. Zhejiang Chin. Med. Univ. 35 (05), 718-719. doi:10.3969/j.issn.10055509.2011.05.037
Huang, T. (2009). Clinical Study of Shenfu Injection in the Treatment of Senile Chronic Heart Failure. J. Emerg. Tradit. Chin. Med. 18 (08), 1265-1266. doi:10.3969/j.issn.1004-745X.2009.08.034
Hutton, B., Salanti, G., Caldwell, D. M., Chaimani, A., Schmid, C. H., Cameron, C., et al. (2015). The PRISMA Extension Statement for Reporting of Systematic Reviews Incorporating Network Meta-Analyses of Health Care Interventions: Checklist and Explanations. Ann. Intern. Med. 162 (11), 777-784. doi:10.7326/ M14-2385
Inoue, Y., Kawayama, T., Iwanaga, T., and Aizawa, H. (2009). High Plasma Brain Natriuretic Peptide Levels in Stable COPD without Pulmonary Hypertension or Cor Pulmonale. Intern. Med. 48 (7), 503-512. doi:10.2169/ internalmedicine. 48.1701
J. Higgins and J. Thomas (Editors) (2020). (Version 6.1) Cochrane Handbook for Systematic Reviews of Interventions. Available at: https://training.cochrane.org/ handbook/current (Accessed January 24th, 2020).
Jansen, J. P., Crawford, B., Bergman, G., and Stam, W. (2008). Bayesian MetaAnalysis of Multiple Treatment Comparisons: an Introduction to Mixed Treatment Comparisons. Value Health 11 (5), 956-964. doi:10.1111/j.15244733.2008.00347.x

Jiang, C. A. (2021). Analysis of the Effect of Shenmai Injection Combined with Furosemide on Patients with Heart Failure. DOCTOR 6 (5), 49-51.
Jonas, D. E., Wilkins, T. M., Bangdiwala, S., Bann, C. M., Morgan, L. C., Thaler, K. J., et al. (2013). Findings of Bayesian Mixed Treatment Comparison MetaAnalyses: Comparison and Exploration Using Real-World Trial Data and Simulation. [Internet]. Rockville (MD): Agency for Healthcare Research and Quality US. Report No.: 13-EHC039-EF. PMID: 23469378.
Kong, W. W. (2010). Study on Shengmai Injection in Patients with Chronic Heart Failure of Type Qi and Yin Deficiency. Master's thesis. Guangzhou, Guangdong, China: Guangzhou University of Chinese Medicine.
Kou, P. J. (2021). Clinical Effect Analysis of Digoxin Tablets Combined with Yiuji Fumai in the Treatment of Chronic Heart Failure. J. Med. Theor. Pract. 34 (4), 582-583. doi:10.19381/j.issn.1001-7585.2021.04.016
Lan, Z. D., and Wei, H. Q. (2011). Clinical Observation of Shenmai Injection in the Treatment of Chronic Congestive Heart Failure. Chin. Community Doctors 13 (21), 177-178. doi:10.3969/j.issn.1007-614x.2011.21.165

Li, J., Wang, L., and Tan, S. (2016). Effect of Shen Mai Injection on Left Ventricular Pump Function in 60 Patients with Coronary Heart Disease and Heart Failure. Chin. Community Doctors 32 (28), 95-96. doi:10.3969/j.issn.1007614 x .2016 .28 .57
Li, J. F. (2018). Effect of Xinmailong Injection on Serum Cystatin C and Cardiac Function in Elderly Patients with Chronic Heart Failure. Chin. J. Integr. Med. Cardio-Cerebrovasc. Dis. 16 (24), 3651-3653. doi:10.12102/j.issn.16721349.2018.24.021

Li, J. P., Liu, J. L., and He, Y. (2020). Effects of Shenfu Injection Combined with Creatine Phosphate Sodium on Cardiac Function, Heart Rate Variability, and Serum BNP in Patients with Dilated Cardiomyopathy and Heart Failure. Drug Eval. Res. 43 (04), 716-719. doi:10.7501/j.issn.1674-6376.2020.04.023
Li, L. (2018). Clinical Effect of Shenmai Injection Combined with Trimetazidine in the Treatment of Dilated Cardiomyopathy Complicated with Heart Failure. Chin. J. Clin. Rational Drug Use 11 (36), 7-8+10. doi:10.15887/j.cnki.13-1389/ r.2018.36.004

Li, L., Li, J., Wang, Q., Zhao, X., Yang, D., Niu, L., et al. (2020). Shenmai Injection Protects against Doxorubicin-Induced Cardiotoxicity via Maintaining Mitochondrial Homeostasis. Front. Pharmacol. 11, 815. doi:10.3389/ fphar.2020.00815

Li, L. J. (2018). Clinical Observation of Trimetazidine Combined with Shenfu Injection in the Treatment of Chronic Heart Failure. Pract. Clin. J. Integr. Tradit. Chin. West. Med. 18 (01), 71-72. doi:10.13638/j.issn.16714040.2018.01.042

Li, X. L. (2018). Clinical Observation on Treating Chronic Heart Failure and Hypotension with the Shengmai Injection Plus Conventional Western Medicine. Clin. J. Chin. Med. 10 (7), 51-52. doi:10.3969/j.issn.1674-7860.2018.07.024
Li, Q. Z. (2013). Effect of Shenmai Injection on Therapeutic Effect and N-Terminal Brain Natriuretic Peptide in Patients with Heart Failure. Acta Acad. Med. Xuzhou 33 (12), 836-837.
Li, G. K. (2014). Clinical Observation of Yiuji Fumai Injection (Freeze-dried) in the Treatment of Dilated Cardiomyopathy. Pract. Clin. J. Integr. Tradit. Chin. West. Med. 14 (03), 76-77. doi:10.13638/j.issn.1671-4040.2014.03.051
Li, X. (2020). Clinical Observation on Xinmailong Injection Combined with Nicorandil in Treatment of Elderly Chronic Heart Failure with Reduced Ejection Fraction. Drugs Clinic 35 (05), 938-941. doi:10.7501/j.issn.16745515.2020.05.024
Lin, L., and Bao, J. L. (2013). Clinical Efficacy of Shenmai Injection in the Treatment of Senile Heart Failure and its Effect on Plasma BNP. Med. Innovation China 10 (20), 43-44. doi:10.3969/j.issn.1674-4985.2013.20.022
Lin, S., Shi, Q., Yang, F., Wang, X., and Mao, J. (2020). Traditional Chinese Medicine Injections for Heart Failure: a Protocol for Systematic Review and Network Meta-Analysis of Randomised Controlled Trials. BMJ Open 10 (9), e037331. doi:10.1136/bmjopen-2020-037331
Lin, S. S., Wang, X. L., Yang, Y., Liu, C. X., Ge, Z., Zhang, J. H., et al. (2021). Xinmailong Injection in the Treatment of Heart Failure with Different Types of Ejection Fraction: a Systematic Review. Chin. J. Evid. Based Med. 21 (04), 423-430. doi:10.7507/1672-2531.202008145
Lin, S. S., Liu, C. X., Wang, X. L., and Mao, J. Y. (2019). Intervention Mechanisms of Xinmailong Injection, a periplaneta Americana Extract, on Cardiovascular Disease: a Systematic Review of Basic Researches. Evid. Based. Complement. Alternat. Med. 2019, 8512405. doi:10.1155/2019/8512405
Lin, W. J., Li, S. S., Han, J. D., Qin, Y. B., Wang, L. J., and Xian, S. X. (2019). The Hemodynamic Effects of Huangqi Injection in the Treatment of Chronic Heart Failure: a Meta-Analysis of Clinical Controlled Trials. Res. Pract. Chin. Med. 33 (01), 63-68. doi:10.13728/j.1673-6427.2019.01.015

Liu, F., and Fu, L. H. (2003). Treatment of Congestive Heart Failure with Huangqi Injection. Clin. Focus 18 (11), 639. doi:10.3969/j.issn.1004-583X.2003.11.024
Liu, W. Q., Au, Q., Wang, X. W., and Yin, X. H. (2015). Effect of Xinmailong Injection on Brain Natriuretic Peptide Precursor and High Sensitivity C-Reactive Protein in Patients with Dilated Cardiomyopathy. Contemp. Med. 21 (18), 134-135. doi:10.3969/j.issn.1009-4393.2015.18.090
Liu, S. L., Zhao, L., and Miao, L. H. (2016). Study in Clinical Data from Heart Failure Patients with Preserved and Reduced Ejection Fraction. Chin. J. Emerg. Med. 25 (10), 1296-1300. doi:10.3760/cma.j.issn.1671-0282.2016.10.016
Liu, Q., Wang, Z. W., and Song, S. W. (2018). Effect of Shenfu Injection on CD4+ CD25+ CD127low/- Regulatory T Cells in Peripheral Blood of Patients with Chronic Heart Failure. Chin. J. Med. Drug Appl. 12 (06), 126-127. doi:10.14164/ j.cnki.cn11-5581/r.2018.06.074
Liu, S. H. (2008). "Clinical Observation of Shengmai Injection in the Treatment of 120 Cases of Chronic Heart Failure," in Proceedings of the Fourth National Symposium on Wang Qingren's Academic Thoughts, Tangshan, Hebei, China, October 17, 2008, 157-159.
Liu, R. (2015). Clinical Research on the Treatment of Heart Failure Caused by the Dilated Cardiomyopathy with Xinmailong Injection. Master's thesis. Taiai, Shandong: Taishan Medical College.
Lu, J., Chen, X. Q., and Xu, Q. Y. (2008). Clinical Observation of Shengmai Injection in the Treatment of Chronic Heart Failure. Chin. J. Integr. Med. Cardio-Cerebrovasc. Dis. 6 (10), 1142-1143. doi:10.3736/jcim20081001
Lv, G. (2010). Analysis of Therapeutic Effect of Shenfu Injection on 31 Cases of Dilated Cardiomyopathy. China Pract. Med. 5 (20), 175-176. doi:10.14163/ j.cnki.11-5547/r.2010.20.024
Mao, X. Z. (2016). Clinical Effect of Shenfu Injection on Patients with Chronic Heart Failure of Coronary Heart Disease. J. Baotou Med. Coll. 32 (12), 92-93. doi:10.16833/j.cnki.fbmc.2016.12.056
Mao, H. Y. (2019). Clinical Observation of Xinmailong Injection in the Treatment of Dilated Cardiomyopathy with Heart Failure. Chin. J. Integr. Med. Cardio-

Cerebrovasc. Dis. 17 (19), 2996-2997. doi:10.12102/j.issn.16721349.2019.19.031
McCullough, P. A., Duc, P., Omland, T., McCord, J., Nowak, R. M., Hollander, J. E., et al. (2003). B-Type Natriuretic Peptide and Renal Function in the Diagnosis of Heart Failure: an Analysis from the Breathing Not Properly Multinational Study. Am. J. Kidney Dis. 41 (3), 571-579. doi:10.1053/ajkd.2003.50118
McDonald, M., Virani, S., Chan, M., Ducharme, A., Ezekowitz, J. A., Giannetti, N., et al. (2021). CCS/CHFS Heart Failure Guidelines Update: Defining a New Pharmacologic Standard of Care for Heart Failure with Reduced Ejection Fraction. Can. J. Cardiol. 37 (4), 531-546. doi:10.1016/j.cjca.2021.01.017
Merlo, M., Pivetta, A., Pinamonti, B., Stolfo, D., Zecchin, M., Barbati, G., et al. (2014). Long-term Prognostic Impact of Therapeutic Strategies in Patients with Idiopathic Dilated Cardiomyopathy: Changing Mortality over the Last 30 Years. Eur. J. Heart Fail. 16 (3), 317-324. doi:10.1002/ejhf. 16
Moher, D., Hopewell, S., Schulz, K. F., Montori, V., Gotzsche, P. C., Devereaux, P. J., et al. (2012). CONSORT 2010 Explanation and Elaboration: Updated Guidelines for Reporting Parallel Group Randomised Trials. Int. J. Surg. 10 (1), 28-55. doi:10.1016/j.ijsu.2011.10.001

Nasser, M. I., Zhu, S., Chen, C., Zhao, M., Huang, H., and Zhu, P. (2020). A Comprehensive Review on Schisandrin B and its Biological Properties. Oxid. Med. Cel. Longev. 2020, 2172740. doi:10.1155/2020/2172740
Pan, A. Q. (2013). Clinical Study of Pulse-Activating Injection Combined with Phentolamine on Treating Chronic Heart Failure. Pract. Pharm. Clin. Remedies 16 (05), 444-445. doi:10.3969/j.issn.1673-0070.2013.05.036
Pan, L. H. (2015). Clinical Observation of Shenfu Injection in the Treatment of Senile Chronic Heart Failure. Chin. J. Trauma Disabil. Med. 23 (2), 150-151. doi:10.13214/j.cnki.cjotadm.2015.02.111
Peng, X. J., Li, M. H., and Zhang, Y. E. (2014). Effect of Xinmailong Injection on Elderly Patients with Chronic Heart Failure. Chin. J. Integr. Med. CardioCerebrovasc. Dis. 12 (11), 1401-1402. doi:10.3969/j.issn.16721349.2014.11.046
Ponikowski, P., Voors, A. A., Anker, S. D., Bueno, H., Cleland, J. G., Coats, A. J., et al. (2016). 2016 ESC Guidelines for the Diagnosis and Treatment of Acute and Chronic Heart Failure: The Task Force for the Diagnosis and Treatment of Acute and Chronic Heart Failure of the European Society of Cardiology (ESC). Developed with the Special Contribution of the Heart Failure Association (HFA) of the ESC. Eur. J. Heart Fail. 18 (12), 891-975. doi:10.1016/ j.rec.2016.11.00510.1002/ejhf. 592

Putko, B. N., Savu, A., Kaul, P., Ezekowitz, J., Dyck, J. R., Anderson, T. J., et al. (2021). Left Atrial Remodelling, Mid-regional Pro-atrial Natriuretic Peptide, and Prognosis across a Range of Ejection Fractions in Heart Failure. Eur. Heart J. Cardiovasc. Imaging 22 (2), 220-228. PMID: 32356860. doi:10.1093/ehjci/jeaa041
Qi, C. H., and Qi, L. (2015). Clinical Observation of Shenfu Injection in the Treatment of Dilated Cardiomyopathy with Intractable Heart Failure. J. Emerg. Tradit. Chin. Med. 24 (06), 1096-1098. doi:10.3969/j.issn.1004-745X.2015.06.056
Qi, J., Yu, J., Tan, Y., Chen, R., Xu, W., Chen, Y., et al. (2017). Mechanisms of Chinese Medicine Xinmailong's protection against Heart Failure in PressureOverloaded Mice and Cultured Cardiomyocytes. Sci. Rep. 7, 42843. doi:10.1038/ srep42843
Qi, H. (2015). Comparison of the Therapeutic Effect of Shenfu Injection and Shengmai Injection in the Treatment of Chronic Heart Failure. World Latest Med. Inf. 15 (07), 20-21. doi:10.3969/j.issn.1671-3141.2015.07.015
Que, H. X., and Guo, J. H. (2003). SHENFU Injection on Treatment of 32 Cases of Ectatic Cardiomyopathy. Fujian J. Tradit. Chin. Med. 34 (02), 17. doi:10.3969/ j.issn.1000-338X.2003.02.008

Rouse, B., Chaimani, A., and Li, T. (2017). Network Meta-Analysis: an Introduction for Clinicians. Intern. Emerg. Med. 12 (1), 103-111. doi:10.1007/s11739-016-1583-7
Rücker, G., and Schwarzer, G. (2015). Ranking Treatments in Frequentist Network Meta-Analysis Works without Resampling Methods. BMC Med. Res. Methodol. 15, 58. doi:10.1186/s12874-015-0060-8
Sakata, Y., and Shimokawa, H. (2013). Epidemiology of Heart Failure in Asia. Circ. J. 77 (9), 2209-2217. doi:10.1253/circj.cj-13-0971

Silvet, H., Young-Xu, Y., Walleigh, D., and Ravid, S. (2003). Brain Natriuretic Peptide Is Elevated in Outpatients with Atrial Fibrillation. Am. J. Cardiol. 92 (9), 1124-1127. doi:10.1016/j.amjcard.2003.07.010
Song, S. Q., Cheng, H. H., Huang, P. D., Huang, J. H., Ling, Q. L., and Li, R. F. (2006). Clinical Observation of Shenfu Injection in the Treatment of Chronic

Systolic Heart Failure. J. Sichuan Tradit. Chin. Med. 24 (08), 42-43. doi:10.3969/j.issn.1000-3649.2006.08.020
Su, L. J., Wang, J. Z., and Fang, Z. H. (2014). Clinical Observation of Xinmailong Injection in the Treatment of Chronic Heart Failure. Chin. J. Integr. Med. Cardio-Cerebrovasc. Dis. 12 (07), 884-885. doi:10.3969/ j.issn.16721349.2014.07.053

Su, W. H., Liang, L. W., Zhou, X. L., Huo, Q., Wang, Q., Zhang, H., et al. (2018). Effect of Xinmailong Injection on Treating of Refractory Heart Failure. Chin. J. Heart Fail. Cardiomyopathy 2 (01), 22-25. doi:10.3760/cma.j.issn.20963076.2018.03.006

Su, H. F., Shaker, S., Kuang, Y., Zhang, M., Ye, M., and Qiao, X. (2021). Phytochemistry and Cardiovascular Protective Effects of Huang-Qi (Astragali Radix). Med. Res. Rev. 41, 1999-2038. (Epub ahead of print). doi:10.1002/med. 21785
Su, Z. Q. (2017). Clinical Analysis of Creatine Phosphate Sodium Combined with Shenfu Injection in the Treatment of Dilated Cardiomyopathy with Cardiac Insufficiency. J. North Pharm. 14 (07), 70-71. doi:10.3969/j.issn.16728351.2017.07.059
Sun, H. J. (2016). Clinical Study of Huangqi Injection in the Treatment of Chronic Heart Failure. J. New Chin. Med. 48 (02), 28-30. doi:10.13457/ j.cnki.jncm.2016.02.012

Tan, G., Zhou, Q., Liu, K., Dong, X., Li, L., Liao, W., et al. (2018). Cross-platform Metabolic Profiling Deciphering the Potential Targets of Shenfu Injection against Acute Viral Myocarditis in Mice. J. Pharm. Biomed. Anal. 160, 1-11. doi:10.1016/j.jpba.2018.07.042
Tang, H., Li, J., Huang, Z. H., Ren, Z. Q., and Ning, J. P. (2013). Effect of Xinmailong on QT Dispersion and Clinical Efficacy in Patients with Ischemic Heart Failure. China Med. 8 (9), 1211-1213. doi:10.3760/cma.j.issn.16734777.2013.09.00510.1007/s11464-013-0303-0
Tao, J. Y., Li, K., Liu, Y. X., Peng, L. H., Shi, B. X., and Guan, Y. (2020). Clinical Study on Yiqi Fumai Lyophilized Injection in Treatment of Chronic Heart Failure with Hypotension. Drug Eval. Res. 43 (08), 1602-1605+1642. doi:10.7501/j.issn.1674-6376.2020.08.023
Virani, S. S., Alonso, A., Benjamin, E. J., Bittencourt, M. S., Callaway, C. W., Carson, A. P., et al. (2020). Heart Disease and Stroke Statistics-2020 Update: a Report from the American Heart Association. Circulation 141 (9), e139-e596. doi:10.1161/CIR. 0000000000000757
Wang, Y. P., and Pan, Y. B. (2016). Effect of Shenfu Injection on Serum CA125 and Troponin I in Patients with Chronic Congestive Heart Failure. Chin. J. Biochem. Pharm. 36 (02), 130-132.
Wang, X. L., and Wu, L. (2012). Effect of Shenmai Injection for Treatment of Dilated Cardiomyopathy Congestive Heart Failure. Chin. J. Integr. Med. Cardio-Cerebrovasc. Dis. 10 (09), 1041-1042. doi:10.3969/j.issn.16721349.2012.09.009
Wang, C. K., Wang, Y. H., Zhao, B., and Xie, Z. S. (2011). Effect of Shenfu Injection in the Treatment of Dilated Cardiomyopathy with Heart Failure. Chin. Heart J. 23 (05), 703-704. doi:10.13191/j.chj.2011.05. 149.wangchk. 003

Wang, L., Huang, Z. H., Guo, L. T., and Zhang, Y. B. (2014). Clinical Effects of Shenfu Injection in the Treatment of Patients with Dilated Cardiomyopathy Combined with Chronic Systolic Heart Failure. China J. Tradit. Chin. Med. Pharm. 29 (10), 3348-3350.
Wang, H., Hu, Y. H., Song, Q. Q., Qiu, Z. L., and Bo, R. Q. (2016). The Impact of Shenfu Injection on the Immune Function in Patients with Chronic Heart Failure and Heart-Kidney Yang Deficiency Syndrome. Chin. J. Integr. Med. Cardio-Cerebrovasc. Dis. 14 (13), 1441-1445. doi:10.3969/j.issn.16721349.2016.13.001
Wang, K. H., Wu, J. R., Zhang, D., Duan, X. J., and Ni, M. W. (2018). Comparative Efficacy of Chinese Herbal Injections for Treating Chronic Heart Failure: a Network Meta-Analysis. BMC Complement. Altern. Med. 18 (1), 41. doi:10.1186/s12906-018-2090-3
Wang, S., Ye, L., and Wang, L. (2019). Protective Mechanism of Shenmai on Myocardial Ischemia-Reperfusion through the Energy Metabolism Pathway. Am. J. Transl. Res. 11 (7), 4046-4062.
Wang, L. F., Chang, C., and Zhao, Y. L. (2021). Analysis of Efficacy of Metoprolol Combined with Xinmailong Injection in the Treatment of Patients with Chronic Heart Failure. Harbin Med. J. 41 (3), 3-5.

Wang, X. N. (2003). Combined Metoprolol and Huangqi Injection to Treating 35 Cases of Heart Failure from Ischemic Heart Disease. Hunan Guiding J. TCM 9 (05), 15-17. doi:10.3969/j.issn.1672-951X.2003.05.011

Wang, A. C. (2014). Ginseng Injection in the Treatment of Dilated Cardiomyopathy Heart Failure Qi and Yin Deficiency Syndrome in Clinical Research. Master's thesis. Jinan, Shandong, China: Shandong University of Traditional Chinese Medicine.
Wang, Y. X. (2017). Clinical Research of Curative Effect and Short-Term Prognosis of Xinmailong Injection in the Treatment of Patients with Chronic Heart Failure. Master's thesis. Kunming, Yunnan, China: Kunming Medical University.
Wang, J. H. (2019). Analysis of Efficacy and Safety of Xinmailong Injection in the Treatment of Chronic Heart Failure. World Latest Med. Inf. 19 (23), 145-147. doi:10.19613/j.cnki.1671-3141.2019.23.091
Wu, H. X., and Chen, K. W. (2005). Clinical Observation of Huangqi Injection in the Treatment of 26 Cases of Dilated Cardiomyopathy with Heart Failure. Yunnan J. Tradit. Chin. Med. Mater. Med. 26 (01), 13. doi:10.3969/j.issn.10072349.2005.01.013
Wu, H. J., and Duan, S. W. (2009). Clinical Study of Shenfu Injection for Heart Failure of Coronary Heart Disease. Chin. J. Integr. Med. Cardio-Cerebrovasc. Dis. 7 (05), 505-507. doi:10.3969/j.issn.1672-1349.2009.05.001
Wu, Y. B., and Wang, C. J. (2010). Clinical Observation of Shenfu Injection in Treating Congestive Heart Failure in Elderly Patients. Chin. J. Convalescent Med. 19 (12), 1128-1130. doi:10.13517/j.cnki.ccm.2010.12.015
Wu, H. Q., Hu, Y. H., Zhou, Y. P., An, C., Chu, Y. G., and Feng, L. (2011). Influence of Shenfu Injection on Cardiac Function and Content of NT-proBNP in Patients with Chronic Heart Failure. J. Emerg. Tradit. Chin. Med. 20 (08), 1207-1208. doi:10.3969/j.issn.1004-745X.2011.08.002
Wu, J. M., Yin, Z., and Du, L. J. (2012). Observation of Curative Effect of Xinmailong Combined with Dobutamine on Chronic Cardiac Dysfunction. Mod. J. Integr. Tradit. Chin. West. Med. 21 (28), 3091-3092+3094. doi:10.3969/ j.issn.1008-8849.2012.28.006

Wu, S. X. (2016). Effects of the Shenfu Injection on Heart Function and Brain Natriuretic Peptide Level in CHF Patients. Clin. J. Chin. Med. 8 (17), 23-24. doi:10.3969/j.issn.1674-7860.2016.17.007
Xi, Y. J. (2020). Effect of Xinmailong Injection on Symptoms of Heart Failure, Dosage and Prognosis of Dopamine in the Middle and Advanced Stage of Middle-Aged and Elderly Patients with Dilated Cardiomyopathy. Chin. J. Gerontol. 40 (09), 1802-1805. doi:10.3969/j.issn.1005-9202.2020.09.004

Xie, N., and Dai, X. H. (2019). Meta Analysis on Curative Effects of Yiqi Fumai Injection (Lyophilization) for Heart Failure. Chin. J. Integr. Med. Cardio-Cerebrovasc. Dis. 17 (10), 1499-1503. doi:10.12102/j.issn.16721349.2019.10.016

Xing, G. P., and Nie, X. M. (2006). Effect of Huangqi Injection on Hemodynamics in Patients with Congestive Heart Failure. Med. Industry Inf. 3 (11), 67-68. doi:10.3969/j.issn.1673-7210.2006.11.052
Xu, E. W., Fang, Y., Zhang, Q. B., Fan, X. J., and Sun, L. N. (2018). Clinical Study on Xinmailong Injection Combined with Milrinone in Treatment of Chronic Congestive Heart Failure. Drugs Clinic 33 (09), 2276-2280. doi:10.7501/ j.issn.1674-5515.2018.09.026

Xu, L., Yin, W. L., Chen, S. W., and Zhu, F. H. (2011). The Clinical Therapeutic Effect of Shengmai Injection Combining with Levocarnitine Injection on Congestive Heart Failure. Chin. J. Hosp. Pharm. 31 (19), 1620-1622.
Xu, W. J., Zhu, L. P., Su, Y. M., and Zhou, C. Y. (2014). Clinical Observation of Shenfu Injection in the Treatment of Ischemic Heart Disease with Heart Failure. J. Emerg. Tradit. Chin. Med. 23 (12), 2256-2257. doi:10.3969/ j.issn.1004-745X.2014.12.041

Xu, L. L., Guan, C. Y., Wang, Z. Y., Chen, J., and Zhang, L. L. (2015). Effect of Shenfu Injection on NT-proBNP and Quality of Life in Patients with Chronic Heart Failure. J. Emerg. Tradit. Chin. Med. 24 (05), 918-920. doi:10.3969/ j.issn.1004-745X.2015.05.066

Xu, S. L., Yang, J. Y., and Guo, H. L. (2018). Clinical Study on the Method of Tonifying Qi and Yin in the Treatment of Chronic Heart Failure with Deficiency of Both Qi and Yin. Chin. J. Coal Industry Med. 21 (04), 425-428. doi:10.11723/nngyyx1007-9564201804020
Xu, T., Shi, X. Q., Wang, F., and Liu, R. X. (2018). Effectiveness and Safety of Shenmai Injection in the Treatment of Heart Failure. J. Community Med. 16 (07), 53-56.

Xue, J., Xu, Y., Deng, Y., Li, F., Liu, F., Liu, L., et al. (2019). The Efficacy and Safety of Xinmailong Injection in Patients with Chronic Heart Failure: a Multicenter Randomized Double-Blind Placebo-Controlled Trial. J. Altern. Complement. Med. 25 (8), 856-860. doi:10.1089/acm.2019.0030
Yan, C. P., Gao, Y. S., and Li, Y. (2017). Effect of Shenfu Injection in the Treatment of Dilated Cardiomyopathy with Heart Failure and its Effect on Cardiac Function. World Chin. Med. 12 (A02), 28-29.
Yang, Y., and Wu, X. H. (2009). Clinical Observation of Shenfu Injection in the Treatment of 30 Cases of Dilated Cardiomyopathy with Heart Failure. Yunnan J. Tradit. Chin. Med. Mater. Med. 30 (09), 26-27. doi:10.16254/j.cnki.53-1120/ r.2009.09.017

Yang, M. G., Zhang, S. J., and Chen, M. Y. (2016). Effect of Shenmai Injection on LVEF and NT-proBNP of Heart Failure Patients. Guangming J. Chin. Med. 31 (13), 1885-1887. doi:10.3969/j.issn.1003-8914.2016.13.023

Yang, F. W., Zou, J. H., Wang, Y., Sun, C. X., Ge, L., Tian, J. H., et al. (2018). Network Meta-Analysis of Chinese Medical Injections for Heart Failure. Zhongguo Zhong Yao Za Zhi 43 (6), 1247-1253. doi:10.19540/ j.cnki.cjcmm.2018.0049

Yang, S. Z. (2016). Clinical Analysis of Shenmai Injection in the Treatment of Chronic Heart Failure. Chin. Prim. Health Care 30 (11), 65-66. doi:10.3969/ j.issn.1001-568X.2016.11.0026

Yao, J., and Lu, X. R. (2010). Clinical Observation of Shenfu Injection in the Treatment of Chronic Congestive Heart Failure. J. Med. Theor. Pract. 23 (03), 287-288. doi:10.19381/j.issn.1001-7585.2010.03.021
Yao, E. H., Li, S. C., and Wang, H. J. (2014). Effects of Xinmailong Injection on Vascular Endothelial Function in Elderly Patients with Chronic Heart Failure. Chin. J. Hosp. Pharm. 34 (23), 2037-2040. doi:10.13286/ j.cnki.chinhosppharmacyj.2014.23.17

Yao, K. W., Chen, M. Q., Liu, T. T., Liu, Z. J., Wang, X., Guo, Y., et al. (2016). Impact of Shenfu Injection Adjunctive Therapy on Quality of Life and Survival Condition of Patients with Coronary Heart Disease with Chronic Heart Failure. J. Tradit. Chin. Med. 57 (24), 2117-2120. doi:10.13288/j.11-2166/r.2016.24.012

Yu, D. L., and Wang, T. (2012). Treatment of 30 Cases of Chronic Heart Failure with Yiqi Fumai Injection. Shaanxi J. Tradit. Chin. Med. 33 (06), 655-656. doi:10.3969/j.issn.1000-7369.2012.06.009
Yu, H. B., Li, J., Yu, H. T., Gao, S., Qin, X. Y., and Chen, F. J. (2014). Changes of Nitric Oxide Synthase, Adrenomedullin and Interleukin-10 in Patients with Heart Failure and Intervention Effect of Shenfu Injection. Chin. J. Gerontol. 34 (24), 7065-7066. doi:10.3969/j.issn.1005-9202.2014.24.103

Yu, F. D., Zhang, X. Y., and Niu, L. (2015). Effect of Shenmai Injection Adjunctive Therapy on Echocardiographic Parameters and NT-proBNP in Patients with Chronic Heart Failure. Mod. J. Integr. Tradit. Chin. West. Med. 24 (22), 2470-2472. doi:10.3969/j.issn.1008-8849.2015.22.027
Yuan, C. L., and Du, S. L. (2012). Efficacy of Yi Qi Fu Mai Injection on Heart Failure Complicated with Angina Pectoris in Patients with Coronary Heart Disease. Chin. J. New Drugs 21 (15), 1774-1777.
Zhai, Y. X. (2013). Effect of Shenmai Injection on NT-Pro-BNP and Cardiac Function in Patients with Congestive Heart Failure. Guide China Med. 11 (22), 272-274. doi:10.15912/j.cnki.gocm.2013.22.061
Zhang, Z. L., and Wen, Y. M. (2016). Shenfu injection on inflammatory cytokines and cardiac function in patients with chronic heart failure. Jilin J. Chin. Med. 36 (03), 252-255. doi:10.13463/j.cnki.jlzyy.2016.03.010

Zhang, J., and Zhang, Y. H. (2015). China Heart Failure Registry Study-a Multicenter, Prospective Investigation for Preliminary Analysis on Etiology, Clinical Features and Treatment in Heart Failure Patients. Chin. Circ. J. 30 (05), 413-416. doi:10.3969/j.issn.1000-3614.2015.05.002
Zhang, F., Ren, K. H., and Chen, Y. L. (2014). Effect of Shenfu Injection on Cardiac Function and Ventricular Remodeling in Patients with Dilated Cardiomyopathy Associated with Heart Failure. Chin. J. Clin. Pharmacol. 30 (06), 478-480. doi:10.13699/j.cnki.1001-6821.2014.06.002

Zhang, Y., Wang, W. S., Lian, J., and Li, Y. (2018). Clinical effect of Shenfu injection combined with creatine phosphate sodium in treatment of dilated cardiomyopathy-congestive heart failure. J. Precision Med. 33 (03), 256-258+262. doi:10.13362/j.jpmed.201803018
Zhang, J., Gu, C. B., and Zhou, W. S. (2021). The Effect of Shenmai Injection Combined with Sacubitril Valsartan on Heart Function and Hemorheology in Patients with Heart Failure. J. Hubei Univ. Chin. Med. 23 (3), 34-37. doi:10.3969/j.issn.1008-987x.2021.03.08

Zhang, Y. B. (2008). Effect of Shengmai injection on cardiac function and coagulation function in patients with chronic heart failure. J. Changzhi Med. Coll. 22 (06), 420-422. doi:10.3969/j.issn.1006-0588.2008.06.007
Zhang, Q. S. (2017). Observation on therapeutic effect of Shenfu injection on chronic heart failure. World Latest Med. Inf. 17 (24), 16-18. doi:10.3969/ j.issn.1671-3141.2017.24.008

Zhang, Y. Q. (2018). Effect of Xinmailong injection in the treatment of chronic heart failure and its effect on cardiac function and brain natriuretic peptide. Chronic Pathematology J. 19 (05), 667-669. doi:10.16440/j.cnki.1674-8166.2018.05.045
Zhao, C. M., Song, X. F., Wang, X. Z., Zhang, X. M., Song, Y. X., Xu, T., et al. (2014). Effect of Xinmailong injection on the level of serum matrix metalloproteinase-1 in patients with congestive heart failure. Chin. J. Gerontol. 34 (12), 3455-3456. doi:10.3969/j.issn.1005-9202.2014.12.116
Zhao, Z., Li, Y., Zhou, L., Zhou, X., Xie, B., Zhang, W., et al. (2021). Prevention and treatment of COVID-19 using traditional Chinese medicine: a review. Phytomedicine 85, 153308. doi:10.1016/j.phymed.2020.153308
Zhao, Y. B. (2015). Clinical observation of Yugi Fumai injection in the treatment of chronic heart failure. Mod. Med. J. China 17 (01), 72-73. doi:10.3969/ j.issn.1672-9463.2015.01.036

Zhong, L. H. (2016). Clinical observation of Xinmailong injection in the treatment of heart failure in elderly patients with coronary heart disease. Diet. Health 3 (11), 94-95.
Zhu, Y. H., Shen, X. X., Han, Q. Q., and Zhao, J. (2018). A meta-analysis of Shenfu injection in myocardial infarction with heart failure. Chin. J. Evid.Based Cardiovasc. Med. 10 (4), 402-406. doi:10.3969/j.issn.16744055.2018.04.04

Zhu, X. C. (2009). Clinical observation of Shenfu injection on brain natriuretic peptide and exercise cardiac output in patients with chronic heart failure. J. Emerg. Tradit. Chin. Med. 18 (10), 1619-1620. doi:10.3969/j.issn.1004745X.2009.10.031

Conflict of Interest: The authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest.

The reviewer LH declared a shared affiliation with some of the authors, SL,QS, ZG, YL, YC, YY, to the handling editor at time of review.

Publisher's Note: All claims expressed in this article are solely those of the authors and do not necessarily represent those of their affiliated organizations, or those of the publisher, the editors and the reviewers. Any product that may be evaluated in this article, or claim that may be made by its manufacturer, is not guaranteed or endorsed by the publisher.

Copyright © 2021 Lin, Shi, Ge, Liu, Cao, Yang, Zhao, Bi, Hou, Wang, Wang and Mao. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.