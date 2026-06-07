# Comparative Effectiveness of Neoadjuvant Treatments for Resectable Gastroesophageal Cancer: A Network Meta-Analysis 

Zhaolun Cai ${ }^{1 \dagger}$, Yiqiong Yin ${ }^{1 \dagger}$, Zhou Zhao ${ }^{1}$, Chunyu Xin², Zhaohui Cai ${ }^{3,4}$, Yuan Yin ${ }^{1}$, Chaoyong Shen ${ }^{1}$, Xiaonan Yin ${ }^{1}$, Jian Wang ${ }^{1}$, Zhixin Chen ${ }^{1}$, Ye Zhou ${ }^{5}$ and Bo Zhang ${ }^{1 *}$<br>${ }^{1}$ Department of Gastrointestinal Surgery, West China Hospital, Sichuan University, Chengdu, China, ${ }^{2}$ West China College of Public Health, Sichuan University, Chengdu, China, ${ }^{3}$ Department of Infectious Disease, Jiangsu Province Hospital of Traditional Chinese Medicine, Affiliated Hospital of Nanjing University of Chinese Medicine, Nanjing, China, ${ }^{4}$ The First College of Clinical Medicine, Nanjing University of Chinese Medicine, Nanjing, China, ${ }^{5}$ Department of Gastric Surgery, Fudan University Shanghai Cancer Center, Shanghai, China

OPEN ACCESS
Edited by:
Sandor Kerpel-Fronius, Semmelweis University, Hungary

Reviewed by:
Domenico Criscuolo, Genovax S.r.l., Italy Robert L. Lins, Retired, Antwerpen, Belgium
*Correspondence: Bo Zhang hxwowk@126.com
${ }^{\dagger}$ These authors have contributed equally to this work.

Specialty section:
This article was submitted to Pharmaceutical Medicine and Outcomes Research, a section of the journal Frontiers in Pharmacology
Received: 09 June 2018
Accepted: 19 July 2018
Published: 06 August 2018
Citation:
Cai Z, Yin Y, Zhao Z, Xin C, Cai Z, Yin Y, Shen C, Yin X, Wang J, Chen Z, Zhou Y and Zhang B (2018) Comparative Effectiveness of Neoadjuvant Treatments for Resectable Gastroesophageal Cancer: A Network Meta-Analysis. Front. Pharmacol. 9:872. doi: 10.3389/fphar. 2018.00872

Background: Several neoadjuvant treatments are available for patients with resectable gastroesophageal cancer. We did a Bayesian network meta-analysis (NMA) to compare available treatments, summarizing the direct and indirect evidence.

Method: We searched relevant databases for randomized controlled trials of neoadjuvant treatments for resectable gastroesophageal cancer which compared two or more of the following treatments: surgery alone, perioperative docetaxel, oxaliplatin, leucovorin, and fluorouracil (FLOT), and neoadjuvant treatments listed in National Comprehensive Cancer Network guideline. Then we performed a NMA to summarize the direct and indirect evidence to estimate the relative efficacy for outcomes including overall survival (OS), progression-free survival and R0 resection rate. We calculated odds ratio (OR) and hazard ratio (HR) with $95 \%$ credible intervals (CrI) for dichotomous data and time-to-event data, respectively. We also calculated the surface under the cumulative ranking curve (SUCRA) value of each intervention to obtain a hierarchy of treatments.

Result: Eight eligible trials (2434 patients) were included in our NMA. The treatment with the highest probability of benefit on OS as compared with surgery alone was perioperative FLOT [HR $=0.58$ with $95 \%$ CrI: $(0.43,0.78)$, SUCRA $=93 \%$ ], followed by preoperative radiotherapy, paclitaxel, and carboplatin (RT/PC) [HR $=0.68$ with $95 \% \mathrm{CrI}$ : $(0.53,0.87)$, SUCRA $=72 \%$ ], perioperative cisplatin with fluorouracil (CF) [HR $=0.70$ with $95 \%$ CrI: $(0.51,0.95)$, SUCRA $=68 \%$ ], and perioperative epirubicin, cisplatin, and fluorouracil or capecitabine (ECF/ECX) [HR $=0.75$ with $95 \%$ CrI: $(0.60,0.94)$, SUCRA $=56 \%$ ].

Conclusion: Compared with surgery alone, perioperative CF, perioperative ECF/ECX, perioperative FLOT, and preoperative RT/PC significantly improved survival. Perioperative FLOT is likely to be the most effective neoadjuvant treatment for the disease. Further clinical studies are needed and justified.

Keywords: gastric cancer, neoadjuvant, chemotherapy, chemoradiotherapy, network meta-analysis

## INTRODUCTION

Gastric cancer (GC) is the third leading cause of cancer death worldwide in 2012 (Job Action Sheets, 2014). Complete surgical resection currently is the only curative treatment for localized GC (Van de Velde and Peeters, 2003; van Cutsem et al. 2011). However, GC is often diagnosed at an advanced stage which is unsuitable for radical surgery (Van de Velde and Peeters, 2003). Even despite potentially curative surgical resections, the prognosis of patients with more advanced GC (T2-4) remains poor due to metastatic disease or local recurrence after radical gastrectomy (Briasoulis et al. 2006; Reim et al. 2013). The high risk of disease relapse prompted the investigation of multidisciplinary strategies. Neoadjuvant chemotherapy or chemoradiotherapy with the advantages of downsizing the tumor before surgery and improving R0 resection rate (Xiong et al. 2014; Xu et al. 2014; Fu et al. 2015; Jiang et al. 2015; Miao et al. 2018) provides a therapeutic alternative for patients with resectable GC. Previous randomized controlled trials (RCTs) have assessed the outcomes of preoperative and perioperative treatments, producing conflicting results (Hartgrink et al. 2004; Burmeister et al. 2005; Cunningham et al. 2006; Shapiro et al. 2015). Efficacy of several neoadjuvant treatments has been established, and the National Comprehensive Cancer Network (NCCN) guideline for GC described numerous recommended neoadjuvant treatments (Ajani et al. 2016). Perioperative docetaxel, oxaliplatin, leucovorin, and fluorouracil (FLOT) have also demonstrated high efficacy against resectable gastroesophageal cancer (Al-Batran et al. 2017). However, the lack of head-to-head clinical trials made the role of optimal neoadjuvant treatments unknown.

To solve above problems, we conducted a Bayesian network meta-analysis (NMA). In the Bayesian hierarchical model, we can combine direct and indirect comparisons to compare two or more inventions at the same time when head-to-head studies are not available (Lumley, 2002; Song et al. 2003; Rucker, 2012; Dias et al. 2013). Our NMA aimed to summarize the direct and indirect evidence to obtain the estimates of relative effectiveness

![img-0.jpeg](img-0.jpeg)

for perioperative FLOT and available neoadjuvant treatments listed in the NCCN guidelines for resectable GC.

## MATERIALS AND METHODS

## Search Strategy

PubMed, Embase (Ovid), Cochrane Library (Ovid) were searched systematically for RCTs until the end of September 2017 without language restriction. We used combinations of the following terms: "gastric cancer," "stomach neoplasms," "stomach cancer," "esophagogastric junction," "gastroesophageal junction," "neoadjuvant," "adjuvant," "perioperative," "preoperative," "chemotherapy," "chemoradiotherapy," "Randomized Controlled Trial," "Controlled Clinical Trial" in accordance with the Cochrane Handbook (Higgins and Green, 2014).

The bibliographies of included studies were also checked for additional trials.

## Study Selection

We only included the RCTs that compared at least two arms of following treatments: surgery alone, perioperative FLOT, surgery combined with neoadjuvant treatments involving chemotherapy or chemoradiotherapy listed in the NCCN guidelines. Patients had been histologically proven gastric or lower third of the esophagus cancer with no evidence of distant metastasis.

We excluded studies if they were non-RCTs. Trials without enough data for us to estimate hazard ratios (HR) for survival were also excluded. Studies enrolling patients with esophageal cancer were excluded when data for gastric and lower third of the esophagus cancer were not separately extractable and/or the study included a limited number of patients with gastroesophageal cancer $(<80 \%)$.

## Assessment of Risk of Bias and Data Collection

Qualitative assessment and data extraction were finished by two investigators independently; disagreements were resolved in discussion with a third author. The two authors independently extracted data from each enrolled study according to the same standardized collection form.

We collected the data regarding study quality, the year of publication, country, the sample size, treatment strategies, tumor site, median follow-up time, and outcomes.

The primary outcome was overall survival (OS). Secondary outcomes were progression-free survival (PFS) and R0 resection rate. We used HR and 95\% Confidence Interval (CI) to assess OS and PFS.

The quality and the risk of bias of RCTs were assessed by Cochrane Collaboration's tool in terms of sequence generation, allocation concealment, blinding of participants and researchers, incomplete outcome data, selective reporting, and other bias (Higgins et al., 2011; Higgins and Green, 2014). Blinding was not performed in all the enrolled trials, but assessment of survival was not likely to be influenced by lack of blinding of participants and researchers.

## Statistical Analysis

The primary outcome of our NMA was OS, and the secondary outcomes were PFS and R0 resection rate. Time-to-event

TABLE 1 | Study and patient population characteristics of included studies.

Paclitaxel
Radiotherapy | - | - | - | GOJ (24\%) Lower esophagus (58\%) Others (18\%) | 84.1  |

NA, not available; NR, not reported; 5-FU, fluorouracil; CAP, capecitabine; GOJ, gastroesophageal junction.

outcomes such as OS and PFS were assessed by HRs which take the number and timing of events into consideration with its 95% CI (Higgins and Green, 2014). For dichotomous data, treatment effects were expressed as odds ratio (OR). 95% credible intervals (CrIs) which could be interpreted as 95% CI were used for the estimating treatment effects of NMA.

The NMA was performed in R, version 3.3.3 and Stata, version 12 (StataCorp., College Station, TX, United States) with the Bayesian methods (Lumley, 2002) and fixed-effect model. We used the node-split method to assess inconsistency between indirect and direct comparisons in closed loops, and a P-value lower than 0.05 indicates a statistically significant inconsistency (Dias et al., 2010). The consistency model was used when there was no significant inconsistency; otherwise, the inconsistency model was conducted.

We calculated values of the surface under the cumulative ranking curve (SUCRA) of each intervention to obtain a hierarchy of treatments. A higher SUCRA value indicated a better efficacy (Salanti et al., 2011).

## RESULTS

### Study Selection and Characteristics

The systematic search identified 3794 potentially relevant studies. Eight studies which met the inclusion criteria were included for the study (Burmeister et al., 2005; Cunningham et al., 2006; Stahl et al., 2009; Schuhmacher et al., 2010; Ychou et al., 2011; Shapiro et al., 2015; Klevebro et al., 2016; Al-Batran et al., 2017). Trials reported by Burmeister et al. (2005) and Klevebro et al. (2016) included several subgroups, and the subset with gastric or lower third of the esophagus cancer was used for the NMA. Literatures screening process was shown in Figure 1 in accordance with PRISMA flowchart (Moher et al., 2009).

The characteristics of included studies are shown in Table 1. A total of 2434 patient treated in seven different treatments were included: 701 treated with surgery alone; 113, perioperative cisplatin with fluorouracil (CF); 207, preoperative CF; 610, perioperative epirubicin, cisplatin, and fluorouracil or capecitabine (ECF/ECX); 356, perioperative FLOT; 234, preoperative radiotherapy combined with CF (RT/CF); 213, preoperative radiotherapy, paclitaxel, and carboplatin (RT/PC). The network plots of OS, PFS, and R0 resection were shown in Figure 2, each node represents a treatment and the thickness of lines represents the number of trials.

### Network Meta-Analysis

#### Overall Survival

A total of eight trials contributed to our analysis, comparing the seven treatments. HRs were explicitly reported in all the eight trials. We summarize the comparisons analyzed by the Bayesian NMA in Figure 3 and present the forest plots of meta-analysis comparing neoadjuvant treatments with surgery alone in Figure 4. Four treatments which significantly improved prognosis as compared with surgery alone were perioperative CF [HR = 0.70 with 95% CrI: (0.51, 0.95)], perioperative ECF/ECX [HR = 0.75 with 95% CrI: (0.60, 0.94)], perioperative FLOT [HR = 0.58 with 95% CrI: (0.43, 0.78)], and preoperative RT/PC [HR = 0.68 with 95% CrI: (0.53, 0.87)]. The rest of enrolled neoadjuvant treatments were not associated with an improved OS when compared with surgery alone. Adding radiation to

![img-1.jpeg](img-1.jpeg)

FIGURE 2 | Network of the comparisons for the Bayesian network meta-analysis. (A) Overall survival; (B) progression-free survival; (C) R0 resection rate. The size of the nodes and the thickness of the edges are weighted according to the number of studies evaluating each treatment and direct comparison, respectively.

preoperative CF also provided little further survival benefit as compared with preoperative CF [HR = 0.88 with 95% CrI: (0.67, 1.2)].

Perioperative FLOT had a statistical advantage over perioperative ECF/ECX, preoperative CT, and preoperative RT/CF in OS and showed a statistically non-significant trend to better survival as compared with the rest of treatments. No significant difference reached between the rest of four treatments which significantly improved OS as compared with surgery alone. The SUCRA values indicated that perioperative FLOT had the highest probability of being the best treatment for OS (SUCRA = 93%), followed by preoperative RT/PC (SUCRA = 72%), perioperative CF (SUCRA = 68%), and perioperative ECF/ECX (SUCRA = 56%). Surgery alone had the least chance of improving OS (SUCRA = 12%) (**Table 2**).

### Progression-Free Survival

In terms of PFS, seven treatments were compared, and six trials contributed to the analysis (Cunningham et al., 2006; Schuhmacher et al., 2010; Ychou et al., 2011; Shapiro et al., 2015; Al-Batran et al., 2017; Stahl et al., 2017). HRs were explicitly reported in all the six trials. In **Figure 3** we summarize the comparisons analyzed by the Bayesian methods. The forest plots of results with surgery alone as the common reference are illustrated in **Figure 4**. Five treatments which reached statistical significance in terms of PFS as compared with surgery alone were perioperative FLOT [HR = 0.50 with 95% CrI: (0.37, 0.66)], preoperative RT/CF [HR = 0.49 with 95% CrI: (0.25, 0.94)], preoperative RT/PC [HR = 0.64 with 95% CrI: (0.49, 0.84)], perioperative ECF/ECX [HR = 0.66 with 95% CrI: (0.53, 0.82)], and perioperative CF [HR = 0.69 with 95% CrI: (0.50, 0.95)]. Preoperative CF alone showed no statistically significant survival benefit when compared with surgery alone [HR = 0.76 with 95% CrI: (0.49, 1.2)].

Perioperative FLOT also had a statistical advantage over perioperative ECF/ECX in PFS and showed a statistically non-significant trend to better survival as compared with the rest of treatments. No significant difference reached between the rest of four treatments which significantly improved PFS as compared with surgery alone. SUCRA values indicated that perioperative FLOT had the highest probability of being the best treatment for PFS (SUCRA = 87%), followed by preoperative RT/CF (SUCRA = 81%), preoperative RT/PC (SUCRA = 54%), perioperative ECF/ECX (SUCRA = 48%), and perioperative CF (SUCRA = 44%). Surgery alone had the least chance of improving PFS (**Table 2**).

### R0 Resection Rate

Four trials (Cunningham et al., 2006; Stahl et al., 2009; Schuhmacher et al., 2010; Ychou et al., 2011) contributed to our analysis of R0 resection rate, comparing the three preoperative treatments. Perioperative/Preoperative CF was shown to have a significantly increased curative resection rate compared with surgery alone group [OR = 2 with 95% CrI: (1.2, 3.4)]. Preoperative RT/CF showed a trend to better resection rate as compared surgery alone [OR = 2.3 with 95% CrI: (0.88, 5.9)]. Perioperative ECF/ECX did not significantly improve R0 resection rate as compared with surgery alone [OR = 1.1 with 95% CrI: (0.78, 1.7)]. Perioperative/Preoperative CF also showed a statistically non-significant trend to better R0 resection rate as


**Overall Survival**

**FIGURE 3** Comparative effectiveness of neoadjuvant treatments in network meta-analysis. Hazard ratio (95% credible interval) for comparisons are in cells in common between column-defining and row-defining treatment. Bold cells are significant. For overall survival, hazard ratio <1 favors row-defining treatment. For progression-free survival, hazard ratio <1 favors column-defining treatment.

![img-2.jpeg](img-2.jpeg)

FIGURE 4 Forest plots of results with surgery alone as the common reference.

TABLE 2 The SUCRA value of different treatments on each outcome.

CF | Perioperative
ECF/ECX | Perioperative
FLOT | Preoperative
CF | Preoperative
RT/CF | Preoperative
RT/PC | Surgery alone  |

*A higher SUCRA value indicates a better efficacy.*

compared with perioperative ECF/ECX [OR = 1.8 with 95% CrI: (0.95, 3.4)].

### Quality of Evidence

The assessment of the risk of bias for selected studies in the NMA was shown in Figure 5 according to the Cochrane risk-of-bias tool, indicating low risk of bias.

The node-splitting method suggested that there was no statistically significant inconsistency in any closed loop (P > 0.05) (Supplementary Figure S1).

### DISCUSSION

In the absence of head-to-head comparative data, a definitive statement on the optimum neoadjuvant treatment for resectable gastroesophageal cancer is still absent. NMA synthesizing both direct and indirect evidence provides more powerful estimates and allows comparisons of relative effectiveness between interventions that have never been compared head to head. In this NMA, we combined direct and indirect evidence from seven RCTs involving 2434 patients with resectable gastroesophageal cancer to estimate the relative efficacy of included neoadjuvant treatments for outcomes including OS, PFS, and R0 resection rate.

We made several key observations regarding OS: (1) perioperative CF, perioperative ECF/ECX, perioperative FLOT, and preoperative RT/PC were superior to surgery alone for improving OS; (2) SUCRA value for indirect comparison indicated that perioperative FLOT is more likely to be the most effective treatment. Perioperative FLOT also showed a trend to better survival as compared with the rest of treatments,

![img-3.jpeg](img-3.jpeg)

FIGURE 5 | Risk of bias graph for all studies included.

and the statistically significant difference was reached for the comparisons of perioperative FLOT versus perioperative ECF/ECX, preoperative CF, and preoperative RT/CF. (3) Preoperative CF and preoperative RT/CF failed to detect survival benefits as compared with surgical resection alone, which might result from inadequate statistical power due to the low number of events in relevant groups or the real possibility that preoperative CF or preoperative RT/CF does not have a beneficial impact on patients with the disease (Schuhmacher et al., 2010). Besides, no statistical difference was reached between preoperative CF and preoperative RT/CF. The previous study indicated a survival advantage for preoperative chemoradiotherapy compared with preoperative chemotherapy in adenocarcinomas of the esophagogastric junction, however, failed to achieve statistical significance. On the other hand, a meta-analysis reported the survival advantage from preoperative chemoradiotherapy over preoperative chemotherapy (Fu et al., 2015). Thus, the effect of adding radiotherapy to preoperative chemotherapy separately is still uncertain, and more high-quality RCTs are needed; (4) preoperative CF failed to demonstrate a survival benefit. Perioperative CF, however, improved survival significantly. Among preoperative, postoperative, and perioperative treatments, which is the key to improve survival is still controversial. Recently a trial has been conducted to investigate effects of postoperative oxaliplatin combined with S-1 and oxaliplatin with capecitabine, and perioperative oxaliplatin and S-1 on locally advanced GC. The patient recruitment had finished, and disease-free survival would be achieved in 2 years (Ji et al., 2017). The results would provide the clues to the question mentioned above.

The JCOG0501 trial explored neoadjuvant S-1 and cisplatin versus surgical resection followed by S-1 for type 4 and large type 3 GC, and the results suggested that neoadjuvant chemotherapy was safely performed without increasing morbidity and mortality (Japan Clinical Oncology Group, 2005). The results of survival will be demonstrated soon and promising.

When we were focusing on the results of PFS, five treatments which were shown to have a significantly improved prognosis as compared with surgery alone were perioperative CF, perioperative ECF/ECX, perioperative FLOT, preoperative RT/CF, and preoperative RT/PC. The results demonstrated perioperative FLOT might be the best treatment. No statistically significant difference reached between the rest treatments which improved the PFS.

Our analysis of R0 resection rate showed best results with perioperative/preoperative CF. Perioperative ECF/ECX failed to improve R0 resection rate. It is worth mentioning that preoperative CF was associated with a higher complete resection rate, however, failed to demonstrate a statistically significant survival benefit. Perioperative ECF/ECX which did not improve R0 resection rate, however, significantly improved OS and PFS. Whether improved R0 resection rate is associated with a better survival merits further discussion.

Our NMA has several limitations. First, based on meta-analyses of summary data, it was difficult for us to explore the impact of tumor location which might be the potential source of heterogeneity. Second, survival benefits must be balanced against risk of adverse effects. However, we could not conduct a quantitative synthesis on adverse effects associated with the relevant treatments because the data on adverse events were rarely available. Al-Batran et al. (2016) suggested that nonsurgical adverse events in both perioperative ECF/ECX and perioperative FLOT were well tolerated and the incidences of adverse events were similar, and further clinical studies are needed. Third, some additional neoadjuvant treatments including S-1 combined with cisplatin and paclitaxel plus cisplatin are under study for the treatment of resectable GC (Yoshikawa et al., 2016). The study suggested that two courses of S-1 and cisplatin should be recommended as a reference arm in future to evaluate neoadjuvant chemotherapy for GC (Yoshikawa et al., 2016). However, the treatments mentioned above were excluded for the shortage of treatments which could connect the network nodes. Fourth, only a limited number of studies (n = 8) were included in the analysis. Furthermore, the best performing treatment (perioperative FLOT) has been investigated in only one study. Although no obvious inconsistency and severe risk of bias were detected, the limited number of trials and patients weakens the external validity of our study.

## CONCLUSION

The NMA provides the first comparison between neoadjuvant treatments for resectable gastroesophageal cancer. In the absence of head to head clinical trials to guide the choice of treatment, it has been unclear which treatment is optimal. The results show that OS is improved with perioperative CF, perioperative ECF/ECX, perioperative FLOT, and preoperative RT/PC. Perioperative FLOT is likely to be the most effective neoadjuvant treatment for the disease. Still, large prospective studies are required to investigate the optimal neoadjuvant treatment for the disease.

## AUTHOR CONTRIBUTIONS

BZ, ZlC, and YiY designed the study. JW and XY screened studies and extracted data. Disagreements were resolved by discussion

## FUNDING

This work was supported by National Natural Science Foundation of China (No. 81572931).

## SUPPLEMENTARY MATERIAL

The Supplementary Material for this article can be found online at: https://www.frontiersin.org/articles/10.3389/fphar. 2018.00872/full\#supplementary-material
gastric cancer: long term results of the Dutch randomised FAMTX trial. Eur. J. Surg. Oncol. 30, 643-649. doi: 10.1016/j.ejso.2004.04.013

Higgins, J. P. T., Altman, D. G., Gøtzsche, P. C., Jüni, P., Moher, D., Oxman, A. D., et al. (2011). The Cochrane Collaboration's tool for assessing risk of bias in randomised trials. BMJ 343:d5928. doi: 10.1136/bmj.d5928
Higgins, J. P. T., and Green, S. (2014). Cochrane handbook for systematic reviews of interventions version 5.1.0 (updated March 2011). Naunyn Schmiedebergs Arch. Exp. Pathol. Pharmakol. 5:S38. doi: 10.1002/14651858.CD008754.pub2
Japan Clinical Oncology Group. (2005). Randomized Phase III Trial of Surgery Plus Neoadjuvant TS-1 and Cisplatin Compared with Surgery Alone for Type 4 and Large Type 3 Gastric Cancer: Japan Clinical Oncology Group Study (JCOG 0501). Clinical Trials. Gov NCT00252161. Available at: http://clinicaltrials.gov/show/ NCT00252161
Ji, J., Liang, H., Xue, Y., Shen, L., Wang, Y., Zhou, Z., et al. (2017). Peri/postoperative chemotherapy of oxaliplatin combined with S-1 (SOX) versus postoperative oxaliplatin with capecitabine (XELOX) in locally advanced gastric cancer: resolve trial. J. Clin. Oncol. 35:e15519. doi: 10.1200/JCO.2017.35.15suppLe15519
Jiang, L., Yang, K. H., Guan, Q. L., Chen, Y., Zhao, P., and Tian, J. H. (2015). Survival benefit of neoadjuvant chemotherapy for resectable cancer of the gastric and gastroesophageal junction. J. Clin. Gastroenterol. 49, 387-394. doi: 10.1097/MCG. 0000000000000212
Job Action Sheets. (2014). All Cancers (Excluding Non-Melanoma Skin Cancer) Estimated Incidence, Mortality and Prevalence Worldwide in 2012. Toledo: The University of Toledo.
Klevebro, F., von Dobeln, G. A., Wang, N., Johnsen, G., Jacobsen, A. B., Friesland, S., et al. (2016). A randomized clinical trial of neoadjuvant chemotherapy versus neoadjuvant chemoradiotherapy for cancer of the oesophagus or gastro-oesophageal junction. Ann. Oncol. 27, 660-667. doi: 10.1093/annonc/mdw010
Lumley, T. (2002). Network meta-analysis for indirect treatment comparisons. Stat. Med. 21, 2313-2324. doi: 10.1002/sim. 1201
Miao, Z. F., Liu, X. Y., Wang, Z. N., Zhao, T. T., Xu, Y. Y., Song, Y. X., et al. (2018). Effect of neoadjuvant chemotherapy in patients with gastric cancer: a PRISMA-compliant systematic review and meta-analysis. BMC Cancer 18:118. doi: 10.1186/s12885-018-4027-0
Moher, D., Liberati, A., Tetzlaff, J., and Altman, D. G. (2009). Preferred reporting items for systematic reviews and meta-analyses: the PRISMA statement. Ann. Intern. Med. 151, 264-269. doi: 10.7326/0003-4819-151-4-200908180-00135
Reim, D., Loos, M., Vogl, F., Novotny, A., Schuster, T., Langer, R., et al. (2013). Prognostic implications of the seventh edition of the international union against cancer classification for patients with gastric cancer: the western experience of patients treated in a Single-Center European Institution. J. Clin. Oncol. 31, 263-271. doi: 10.1200/jco.2012.44.4315

Rucker, G. (2012). Network meta-analysis, electrical networks and graph theory. Res. Synth. Methods 3, 312-324. doi: 10.1002/jrsm. 1058
Salanti, G., Ades, A. E., and Ioannidis, J. P. (2011). Graphical methods and numerical summaries for presenting results from multiple-treatment metaanalysis: an overview and tutorial. J. Clin. Epidemiol. 64, 163-171. doi: 10.1016/ j.jclinepi.2010.03.016

Schuhmacher, C., Gretschel, S., Lordick, F., Reichardt, P., Hohenberger, W., Eisenberger, C. F., et al. (2010). Neoadjuvant chemotherapy compared with surgery alone for locally advanced cancer of the stomach and cardia: European Organisation for Research and Treatment of Cancer randomized trial 40954. J. Clin. Oncol. 28, 5210-5218. doi: 10.1200/jco.2009.26.6114
Shapiro, J., van Lanschot, J. J., Hulshof, M. C., van Hagen, P., van Berge Henegouwen, M. I., Wijnhoven, B. P., et al. (2015). Neoadjuvant chemoradiotherapy plus surgery versus surgery alone for oesophageal or junctional cancer (CROSS): long-term results of a randomised controlled trial. Lancet Oncol. 16, 1090-1098. doi: 10.1016/s1470-2045(15)00040-6
Song, F., Altman, D. G., Glenny, A., and Deeks, J. J. (2003). Validity of indirect comparison for estimating efficacy of competing interventions: empirical evidence from published meta-analyses. BMJ 326:472. doi: 10.1136/bmj. 326. 7387.472

Stahl, M., Walz, M. K., Riera-Knorrenschild, J., Stuschke, M., Sandermann, A., Bitzer, M., et al. (2017). Preoperative chemotherapy versus chemoradiotherapy in locally advanced adenocarcinomas of the oesophagogastric junction (POET): long-term results of a controlled randomised trial. Eur. J. Cancer 81, 183-190. doi: 10.1016/j.ejca.2017.04.027
Stahl, M., Walz, M. K., Stuschke, M., Lehmann, N., Meyer, H. J., RieraKnorrenschild, J., et al. (2009). Phase III comparison of preoperative chemotherapy compared with chemoradiotherapy in patients with locally advanced adenocarcinoma of the esophagogastric junction. J. Clin. Oncol. 27, 851-856. doi: 10.1200/jco.2008.17.0506
van Cutsem, E., Dicato, M., Geva, R., Arber, N., Bang, Y., Benson, A., et al. (2011). The diagnosis and management of gastric cancer: expert discussion and recommendations from the 12th ESMO/World Congress on Gastrointestinal Cancer, Barcelona, 2010. Ann. Oncol. 22(Suppl. 5), v1-v9. doi: 10.1093/annonc/ mdr284

Van de Velde, C. J., and Peeters, K. C. (2003). The Gastric Cancer Treatment Controversy. Alexandria, VA: American Society of Clinical Oncology.
Xiong, B. H., Cheng, Y., Ma, L., and Zhang, C. Q. (2014). An updated meta-analysis of randomized controlled trial assessing the effect of neoadjuvant chemotherapy in advanced gastric cancer. Cancer Invest. 32, 272-284. doi: 10.3109/07357907. 2014.911877

Xu, A. M., Huang, L., Liu, W., Gao, S., Han, W. X., and Wei, Z. J. (2014). Neoadjuvant chemotherapy followed by surgery versus surgery alone for gastric carcinoma: systematic review and meta-analysis of randomized controlled trials. PLoS One 9:e86941. doi: 10.1371/journal.pone. 008 6941
Ychou, M., Boige, V., Pignon, J. P., Conroy, T., Bouche, O., Lebreton, G., et al. (2011). Perioperative chemotherapy compared with surgery alone for resectable gastroesophageal adenocarcinoma: an FNCLCC and FFCD multicenter phase III trial. J. Clin. Oncol. 29, 1715-1721. doi: 10.1200/jco.2010.33. 0597
Yoshikawa, T., Morita, S., Tanabe, K., Nishikawa, K., Ito, Y., Matsui, T., et al. (2016). Survival results of a randomised two-by-two factorial phase II trial comparing neoadjuvant chemotherapy with two and four courses of S-1 plus cisplatin (SC) and paclitaxel plus cisplatin (PC) followed by D2 gastrectomy for resectable advanced gastric cancer. Eur. J. Cancer 62, 103-111. doi: 10.1016/j.ejca.2016. 04.012

Conflict of Interest Statement: The authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest.

Copyright © 2018 Cai, Yin, Zhao, Xin, Cai, Yin, Shen, Yin, Wang, Chen, Zhou and Zhang. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.