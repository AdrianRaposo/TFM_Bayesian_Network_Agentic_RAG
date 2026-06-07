# Prokinetics for the treatment of functional dyspepsia: Bayesian network meta-analysis 

Young Joo Yang, Chang Seok Bang ${ }^{\circ}$ (D) Gwang Ho Baik, Tae Young Park, Suk Pyo Shin, Ki Tae Suk and Dong Joon Kim


#### Abstract

Background: Controversies persist regarding the effect of prokinetics for the treatment of functional dyspepsia (FD). This study aimed to assess the comparative efficacy of prokinetic agents for the treatment of FD.


Methods: Randomized controlled trials (RCTs) of prokinetics for the treatment of FD were identified from core databases. Symptom response rates were extracted and analyzed using odds ratios (ORs). A Bayesian network metaanalysis was performed using the Markov chain Monte Carlo method in WinBUGS and NetMetaXL.
Results: In total, 25 RCTs, which included 4473 patients with FD who were treated with 6 different prokinetics or placebo, were identified and analyzed. Metoclopramide showed the best surface under the cumulative ranking curve (SUCRA) probability ( $92.5 \%$ ), followed by trimebutine ( $74.5 \%$ ) and mosapride ( $63.3 \%$ ). However, the therapeutic efficacy of metoclopramide was not significantly different from that of trimebutine (OR:1.32, 95\% credible interval: $0.27-6.06$ ), mosapride (OR: 1.99, 95\% credible interval: 0.87-4.72), or domperidone (OR: 2.04, 95\% credible interval: 0.92-4.60). Metoclopramide showed better efficacy than itopride (OR: 2.79, 95\% credible interval: 1. 29-6.21) and acotiamide (OR: 3.07, 95\% credible interval: 1.43-6.75). Domperidone (SUCRA probability 62.9\%) showed better efficacy than itopride (OR: 1.37, 95\% credible interval: 1.07-1.77) and acotiamide (OR: 1.51, 95\% credible interval: $1.04-2.18$ ).
Conclusions: Metoclopramide, trimebutine, mosapride, and domperidone showed better efficacy for the treatment of FD than itopride or acotiamide. Considering the adverse events related to metoclopramide or domperidone, the short-term use of these agents or the alternative use of trimebutine or mosapride could be recommended for the symptomatic relief of FD.
Keywords: Comparative effectiveness research, Functional dyspepsia, Network meta-analysis, Systematic review, Prokinetics

## Background

Functional dyspepsia (FD) is a common condition in clinical practice [1]. According to the Rome III and IV criteria, FD is defined as the presence of at least one of the following symptoms; postprandial fullness, early satiation, epigastric pain or burning, without evidence of structural disease to explain the symptoms fulfilling time criteria for the last three months with symptom onset at least six months before diagnosis and a frequency of at least three days per week [2, 3]. FD is subcategorized

[^0]into two distinct conditions, which are postprandial distress syndrome, associated with meal-induced bothersome fullness or early satiation, and epigastric pain syndrome, showing bothersome epigastric pain or burning $[2,3]$.
This condition involves complex pathophysiologic mechanisms and shares overlapping symptoms with gastroesophageal reflux disease or other functional gastrointestinal disorders. The mainstay of the treatment of FD has been to target gastric acid secretion and impaired gut motility. The role of acid inhibitory drugs in the treatment of FD is well established [4]. In a subtype of FD, the response rate of epigastric pain syndrome to

[^1]
[^0]:    * Correspondence: csbang@hallym.ac.kr

    Department of Internal Medicine, Hallym University College of Medicine, Chuncheon Sacred Heart Hospital, Sakju-ro 77, Chuncheon, Gangwon-do 24253, Republic of Korea

[^1]:    (c) The Author(s). 2017 Open Access This article is distributed under the terms of the Creative Commons Attribution 4.0 International License (http://creativecommons.org/licenses/by/4.0/), which permits unrestricted use, distribution, and reproduction in any medium, provided you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The Creative Commons Public Domain Dedication waiver (http://creativecommons.org/publicdomain/zero/1.0/) applies to the data made available in this article, unless otherwise stated.

acid inhibitory therapy is known to be better than that of post-prandial distress syndrome [5].

Excluding acid inhibitory therapy, prokinetics are the mainstay of the treatment of FD. However, the role of prokinetics has not been well established, and inconsistent results have been reported regarding the therapeutic efficacy of each drug [6--10]. Moreover, previously published pairwise meta-analyses were conducted by examining several drugs with different mechanisms of action as a single group, which cannot present the efficacy of each prokinetic agent [8, 9]. However, head-to-head efficacy comparison of prokinetic agents in the treatment of FD is not easy and pooled comparative efficacy has not been established.

Unlike traditional pair-wise meta-analysis, network meta-analysis enables comparing more than 2 treatments strengthening the precision in the estimate and presenting relative effect sizes in a rank order [11]. Therefore, this study aimed to evaluate the comparative effectiveness of each prokinetic in the treatment of FD using an indirect comparison method.

## Methods

### Literature search

A systematic review was conducted using electronic databases. MEDLINE (PubMed), EMBASE, and the Cochrane Central Register of Controlled Trials (CENTRAL) in the Cochrane Library were searched using common keywords related to FD and prokinetics (inception to July 2015). The keywords were as follows: ‘functional dyspepsia', ‘prokinetics', ‘mosapride', ‘itopride', ‘trimebutine', ‘metoclopramide', ‘domperidone', and ‘acotiamide', drawn from MeSH or Emtree terminology and using Boolean operators. Only publications involving human subjects were searched. The bibliographies of relevant articles were also reviewed to identify additional studies. The language of publication was not restricted and all publications except Korean and English were translated using commercial translation service.

### Selection criteria

We included only randomized controlled trials (RCTs) meeting all of the following criteria: 1) designed to evaluate FD in the target or control group; 2) included a group that was given prokinetics and a comparison group that was given placebo or other prokinetics; and 3) presented comparative outcomes about symptomatic relief rates of FD after treatment. Exclusion criteria were as follows: 1) incomplete data or 2) review article.

### Selection of relevant studies

Two of the authors (C.S.B. and G.H.B.) independently evaluated the eligibility of all studies retrieved from the databases based on the predetermined selection criteria. The abstracts of all identified studies were reviewed to exclude irrelevant articles. Full-text review was performed to determine whether the inclusion criteria were satisfied by the remaining studies. Disagreements between the two evaluators were resolved by discussion or by consultation with a third author (D.J.K.).

### Assessment of methodological quality

The methodological quality of the enrolled studies was assessed using the Risk of Bias table (RoB). The RoB was assessed as described in the Cochrane handbook by recording the method used to generate the randomization sequence, allocation concealment, the determination of whether blinding was implemented for participants or staff, and whether there was evidence of selective reporting of the outcomes [12]. Review Manager version 5.3.3 (Revman for Windows 7, the Nordic Cochrane Centre, Copenhagen, Denmark) was used to generate the RoB table. Two of the authors (C.S.B. and G.H.B.) independently evaluated the methodological quality of all studies, and any disagreements between the two evaluators were resolved by discussion or by consultation with a third author (D.J.K.).

### Statistical analysis

We investigated the efficacy of prokinetics for the treatment of FD using odds ratios (ORs). We calculated the ORs based on an intention-to-treat analysis, when possible, from the original articles to compare the efficacy of prokinetics for the treatment of FD. Network meta-analyses were conducted using the Bayesian Markov Chain Monte Carlo method in WinBUGS 1.4.3 (MRC Biostatistics Unit, Cambridge, and Imperial College School of Medicine, London, UK) and Microsoft-Excel-based network metaanalysis tool (NetMetaXL) [11]. Effect sizes for the Bayesian network meta-analysis were described with 95% credible interval. Statistical validity is guaranteed when the 95% credible interval does not include 1. The detailed data input form and initial data for the analysis of network meta-analysis can be found in the Additional file 1.

## Results

### Identification of relevant studies

Figure 1 shows a flow diagram of how relevant studies were identified. A total of 946 articles were identified by searching 3 core databases and by hand searching the relevant bibliographies. In all, 307 duplicate articles and an additional 550 articles were excluded during the initial screening after reviewing the titles and abstracts. The full texts of the remaining 89 articles were thoroughly reviewed. Among these studies, 63 were excluded from the final analysis. The reasons for the exclusion of studies during the final review were as follows: review article (n = 19) or incomplete data (n = 45). The remaining 25 RCTs were included in the final analysis.

![img-0.jpeg](img-0.jpeg)

## Characteristics of studies included in the final analysis

In the 25 RCTs, we identified a total of 4473 participants (1602 placebo, 955 itopride, 773 domperidone, 713 acotiamide, 335 mosapride, 68 metoclopramide, and 27 trimebutine-treated participants). The enrolled studies were published between 1978 and 2012 [13-37]. All of the articles were full-text format except 2 studies [13, 36], which was in abstract format. More than half of the enrolled studies were conducted in Asia ( $n=14$ ) [13-26], followed by 9 studies in Europe [27-34], and the remaining 3 studies in the US [35-37]. Sixteen English-, 8 Chinese-, 1 Portuguese-, and 1 Korean-language studies were enrolled. The treatment duration ranged from 2 to 12 weeks. Eighteen studies used control medication as a placebo, whereas the remaining 8 studies performed direct head-to-head comparisons of prokinetic agents. All the prokinetic agents were orally administered and the detailed dosage, duration of prokinetics, and characteristics of the enrolled studies are shown in Table 1.

Figure 2 shows the network plot of relevant studies. Circles represent each prokinetic drug as a node and lines represent the direct comparisons. The extent of the circle indicates the number of included participants for each prokinetic drug, and the line thickness indicates the number of studies included in each comparison. Placebo was the biggest node, while the node size of metoclopramide and trimebutine was relatively smaller than the other remaining prokinetics. Direct comparisons were made between B (itopride) and D (domperidone) and between B (itopride) and C (mosapride). The remaining comparisons were performed in a pairwise manner.

## Comparative efficacy of prokinetics in FD

Figure 3 shows the Forest plot of the results from a Bayesian network meta-analysis of the enrolled studies. The fixed-effect model was adopted based on the DIC statistics. The relative efficacy is plotted as OR with $95 \%$ credible interval. Based on these results, we calculated the surface under the cumulative ranking curve (SUCRA), which is the converted value reflecting the probability of a treatment being the best according to the ranking of each treatment [11]. Table 2 shows the SUCRA of each treatment regimen. A higher SUCRA value indicates better therapeutic results based on the indirect comparison method [38]. Metoclopramide showed the best SUCRA probability ( $92.5 \%$ ), followed by trimebutine ( $74.5 \%$ ), mosapride ( $63.3 \%$ ), domperidone ( $62.9 \%$ ), itopride ( $32.4 \%$ ), acotiamide ( $24.3 \%$ ), and placebo.

However, the therapeutic efficacy of metoclopramide was not significantly different from that of trimebutine (OR: $1.32,95 \%$ credible interval: $0.27-6.06$ ), mosapride (OR: $1.99,95 \%$ credible interval: $0.87-4.72$ ), and domeperidone (OR: $2.04,95 \%$ credible interval: $0.92-4.60$ ) in the league table, which shows the relative efficacy using OR and $95 \%$ credible interval (Table 3). Metoclopramide showed better efficacy than itopride (OR: $2.79,95 \%$ credible interval: $1.29-6.21$ ) and acotiamide (OR: $3.07,95 \%$ credible interval: $1.43-6.75$ ). Domperidone also showed better efficacy than itopride (OR: $1.37,95 \%$ credible interval: $1.07-1.77$ ) and acotiamide (OR: $1.51,95 \%$ credible interval: $1.04-2.18$ ).

Figure 4 shows the inconsistency plot of the enrolled studies. The plot demonstrates the posterior mean deviance of each study for the consistency model (horizontal

Table 1 Clinical data of included studies


Table 1 Clinical data of included studies (Continued)
![img-1.jpeg](img-1.jpeg)

![img-2.jpeg](img-2.jpeg)

**Fig. 2** Network plot of relevant studies. Circles represent the each prokinetic drug as a node and lines represent the direct comparisons. The extent of circle indicates the number of included participants in each prokinetic drug and the line thickness indicates the number of studies included in each comparison

axis), and the unrelated mean-effects model (vertical axis), along with the line of equality. There is some probability of inconsistency in the plot.

### Adverse events related to prokinetics

Adverse events related to prokinetics were as follows: domperidone induced diarrhea, constipation, intestinal colic, galactorrhea, bilateral breast tenderness, hyperprolactinemia, headache, dizziness, insomnia, and skin scare [19, 28, 35]; mosapride induced diarrhea, constipation, abdomen pain, dry mouth, fatigue, dizziness, headache, leg pain, and nausea [33]; itopride induced abdomen pain, diarrhea, constipation, nausea, and hyperprolactinemia [34, 38]; Acotiamide induced headache, diarrhea, increase in serum alanine aminotransferase, potassium, triglycerides, γ-glutamyltransferase, nasopharyngitis, and hyperprolactinemia [24–26]. Even control groups using placebo showed similar adverse events with treatment group taking prokinetics. Most adverse events were mild to moderate and have resolved after discontinuing prokinetics.

### Methodological quality

For the methodological quality of enrolled studies, the exact determination of random sequence generation and allocation concealment was not available, and double-blinding was not consistent in all of the enrolled studies. The summary of the risk of bias is demonstrated in Fig. 5, and the risk of bias table of all enrolled studies is shown in Fig. 6.

### Discussion

FD involves complex pathophysiologic mechanisms including visceral hypersensitivity, impaired gastric accommodation, delayed gastric emptying, *H. pylori* infection, psychosocial disorders, and even an unhealthy lifestyle [39–41]. The prevalence of gastric emptying delay was reported to be 37–39% in patients with FD. Consequently, prokinetics were developed based on the concept that promoting impaired gut motility could reduce the symptoms of FD [39, 40]. However, improved delayed gastric emptying was not associated with symptomatic relief in patients with gastroparesis [39, 40]. It is apparent that dysmotility cannot be the only target.

**Table 2** SUCRA of each treatment regimen


**SUCRA, surface under the cumulative ranking curve**

![img-3.jpeg](img-3.jpeg)

Multiple other mechanisms should be considered in the treatment of FD.

Proton-pump inhibitors (PPI) and prokinetic agents are the mainstays of the treatment of FD [39], both of which have similar relative efficacy [42]. However, adverse events related to PPI have been reported, and the comparative efficacy of prokinetics has thus far not been evaluated [43, 44]. Because the adverse events associated with PPIs are linked to long-term use of this medication and the recurrence of FD is not infrequent [45], repeated prescriptions of PPI should be re-evaluated and additional focus should be

Table 3 League table of each treatment regimen


Odds ratio with $95 \%$ credible interval is described in each column. Prokinetic agent in the top left means better efficacy and statistical validity is guaranteed when the $95 \%$ credible interval does not include 1

![img-4.jpeg](img-4.jpeg)

**Fig. 4** Inconsistency plot of enrolled studies. Plot of the posterior mean deviance of each study for the consistency model (horizontal axis), and the unrelated mean-effects model (vertical axis), along with the line of equality

directed toward the role of prokinetic agents in the treatment of FD.

In this analysis, the relative efficacy of prokinetics was based on the SUCRA value. However, there was no significant difference in efficacy between the prokinetics including metoclopramide, trimebutine, mosapride, and domperidone (Table 3). Though the mechanisms of action of these medications are slightly different, the precise reason for the superior or inferior comparative efficacy between these medications could not be evaluated in this analysis. For example, although mosapride, itopride, and acotiamide are all known to modulate gastric accommodation, the statistical effects of these drugs differed in this analysis [46–48].

The frequency of adverse event must also be considered in selecting prokinetics for the treatment of FD. In the case of metoclopramide, which is a central D1 and D2 receptor antagonist, extrapyramidal symptoms including dystonic movement or tardive dyskinesia, which are often irreversible, inhibit the administration of high doses or the long-term use of this medication [49].

In addition to the occurrence of adverse events, drug incompatibility due to drug interactions from a combination of prokinetics or other drugs should be considered in selecting prokinetics. Because domperidone, which is a peripheral D2 and D3 receptor antagonist is associated with ventricular arrhythmia, concomitant use of drugs that prolong the QTc interval, and potent CYP3A4 inhibitors should be avoided [50].

With respect to serotonergic agonists, targeting multiple receptors with non-selective inhibition can potentially lead to adverse events. Cardiac arrhythmia or QTc prolongation was most commonly associated with cisapride and tegaserod [51]. 5HT1 receptor subtypes have been suggested to account for adverse events due to interactions with HERG cardiac potassium channel and 5-hydroxytryptamine [52]. Mosapride, which is a nonselective 5-HT4 agonist with no HERG or 5HT1 affinity, could be substituted for metoclopramide or domperidone for the specific subset of patients who need long-term treatment.

Trimebutine, which is an enkephalin agonist, has a dual action on both of hyperkinetic and hypokinetic motility disorders [53]. This medication accelerates gastric emptying by inducing premature phase III activity of the migrating motor complex in gut [9]. Although most studies are focused on the treatment of irritable bowel syndrome, this medication could be substituted for other prokinetics that potentially have serious adverse effects.

In this study, we could not investigate the reason for the relatively lower efficacy of itopride, a mixed D2 receptor antagonist, and acetylcholinesterase inhibitor or acotiamide, an M1/M2 muscarinic receptor antagonist and acetylcholinesterase inhibitor. Given the probability of inconsistencies in the enrolled studies and the superior efficacy of prokinetics that have a relatively small number of enrolled population, there could be an overestimation of efficacy drawn from the pairwise indirect comparison.

This study is the first meta-analysis evaluating the comparative effectiveness of prokinetic agents. The strength of

![img-5.jpeg](img-5.jpeg)

![img-6.jpeg](img-6.jpeg)

this study is the rigorous searching of the literature without language limitations and the use of an indirect comparative method to address the challenge of performing head-tohead analyses in clinical practice. Nonetheless, there are several limitations that impact the generalizability of the main results. All of the available prokinetic drugs could not be included in this study. These omitted agents include levosulpiride, a selective $\mathrm{D}_{2}$ receptor antagonist, erythromycin, a motilin receptor agonist, tandospirone, a $5 \mathrm{HT}_{1 \mathrm{~A}}$ agonist, prucalopride, a selective $5 \mathrm{HT}_{4}$ agonist or DA9701, a $5 \mathrm{HT}_{4}$ agonist, $\mathrm{D}_{2}$ receptor and $5 \mathrm{HT}_{3}$ antagonist. These medications are not available in some countries. Furthermore, levosulpiride is associated with drug-induced parkinsonism, inhibiting its wide application in clinical practice [54]. Prucalopride was developed and licensed for the treatment of constipation. Therefore, these drugs were excluded from the beginning of this study. Another limitation was the lack of data for some prokinetic agents in this analysis. The relatively small number of studies evaluating metoclopramide and trimebutine may in part explain the inconsistencies as well as the overestimation of the comparative effectiveness of some medications. In addition, most enrolled studies did not discriminate between epigastric pain and postprandial distress syndromes, which are subtypes of FD or post-infectious FD. Moreover, H. pylori infection, which is closely associated with the pathogenesis of FD, was not considered in most of the studies [39]. Overlap syndrome (FD + gastroesophageal reflux disease or FD + irritable bowel syndrome) which is frequently encountered in clinical practice, was also not considered [39]. A further limitation was the absence of a no common validated outcome measurement scale for all the enrolled studies. As we have noted in a previous study, there is no definite and unanimous way of defining symptomatic improvement in patients with FD [6]. Further studies that include newer prokinetics and control for the abovementioned limitations are needed to confirm the results of this study.

## Conclusion

In conclusion, metoclopramide, trimebutine, mosapride, and domperidone showed better efficacy for the treatment of FD than that of itopride or acotiamide. Considering the adverse events related to metoclopramide or domperidone, the short-term use of these agents or the alternative use of trimebutine or mosapride could be recommended for the symptomatic relief of FD.

## Additional file

Additional file 1: Contains tables for data input form and initial data for the analysis of network meta-analysis. (XLSX 17.6 kb)

## Abbreviations

FD: Functional dyspepsia; OR: Odds ratio; PPI: Proton pump inhibitor; RCT: Randomized controlled trial; RoB: Risk of bias; SUCRA: Surface under the cumulative ranking curve

## Acknowledgements

none.

## Funding

This research was supported by Hallym University Research Fund (HURF-2015-18).

## Availability of data and materials

Input data for the analyses are available from the corresponding author on request.

## Authors' contributions

YJY participated data analysis and interpretation, and article drafting. CSB participated to study design, data analysis and interpretation, article drafting and gave final approval for publication. GHB participated to data analysis and interpretation. TYP participated to data analysis and interpretation. SPS participated to data analysis and interpretation. KTS participated to data analysis and interpretation. DJK participated to data analysis and interpretation. All authors have read and approved the final version of this manuscript.

## Ethics approval and consent to participate

Not applicable.

## Consent for publication

Not applicable.

## Competing interests

The authors declare that they have no competing interests.

## Publisher's Note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## Received: 8 January 2017 Accepted: 20 June 2017

Published online: 26 June 2017

## Submit your next manuscript to BioMed Central and we will help you at every step:

- We accept pre-submission inquiries
- Our selector tool helps you to find the most relevant journal
- We provide round the clock customer support
- Convenient online submission
- Thorough peer review
- Inclusion in PubMed and all major indexing services
- Maximum visibility for your research

Submit your manuscript at www.biomedcentral.com/submit
(1) BioMed Central