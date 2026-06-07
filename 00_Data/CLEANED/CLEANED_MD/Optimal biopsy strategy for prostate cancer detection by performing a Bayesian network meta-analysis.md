# Optimal biopsy strategy for prostate cancer detection by performing a Bayesian network meta-analysis of randomized controlled trials 

Yi Wang ${ }^{1 *}$, Jundong Zhu ${ }^{1,2^{*}}$, Zhiqiang Qin ${ }^{1 *}$, Yamin Wang ${ }^{1}$, Chen Chen ${ }^{1}$, Yichun Wang ${ }^{1}$, Xiang Zhou ${ }^{1}$, Qijie Zhang ${ }^{1}$, Xianghu Meng ${ }^{1 \boxtimes}$, Ninghong Song ${ }^{1 \boxtimes}$<br>1. Department of Urology, The First Affiliated Hospital of Nanjing Medical University, Nanjing, 210029, China<br>2. Current affiliation: Department of Urology, The Third Affiliated Hospital of Soochow University, Changzhou, 213000, China<br>* Yi Wang, Jundong Zhu and Zhiqiang Qin contributed equally to this work.<br>$\boxtimes$ Corresponding authors: Ninghong Song, Department of Urology, The First Affiliated Hospital of Nanjing Medical University, No. 300 Guangzhou Road, Nanjing, 210029, China. E-mail: songninghong_uro1@163.com; TEL: +08613851490672 and Xianghu Meng, Department of Urology, The First Affiliated Hospital of Nanjing Medical University, No. 300 Guangzhou Road, Nanjing, 210029, China. E-mail: xhmeng888@163.com; TEL: +08615951945520<br>(c) Ivyspring International Publisher. This is an open access article distributed under the terms of the Creative Commons Attribution (CC BY-NC) license (https:// creativecommons.org/licenses/by-nc/4.0/). See http://ivyspring.com/terms for full terms and conditions.

Received: 2018.01.02; Accepted: 2018.03.16; Published: 2018.06.05


#### Abstract

Objective: With the increasing recognition of the over-diagnosis and over-treatment of prostate cancer (PCa), the choice of a better prostate biopsy strategy had confused both the patients and clinical surgeons. Hence, this network meta-analysis was conducted to clarify this question. Methods: In the current network meta-analysis, twenty eligible randomized controlled trials (RCTs) with 4,571 participants were comprehensively identified through Pubmed, Embase and Web of Science databases up to July 2017. The pooled odds ratio (OR) with $95 \%$ credible interval (CrI) was calculated by Markov chain Monte Carlo methods. A Bayesian network meta-analysis was conducted by using R-3.4.0 software with the help of package "gemtc" version 0.8.2. Results: Six different PCa biopsy strategies and four clinical outcomes were ultimately analyzed in this study. Although, the efficacy of different PCa biopsy strategies by ORs with corresponding $95 \%$ CrIs had not yet reached statistical differences, the cumulative rank probability indicated that overall PCa detection rate from best to worst was FUS-GB plus TRUS-GB, FUS-GB, CEUS, MRI-GB, TRUS-GB and TPUS-GB. In terms of clinically significant PCa detection, CEUS, FUS-GB or FUS-GB plus TRUS-GB had a higher, whereas TRUS-GB or TPUS-GB had a relatively lower significant detection rate. Meanwhile, TPUS-GB or TRUS-GB had a higher insignificant PCa detection rate. As for TRUS-guided biopsy, the general trend was that the more biopsy cores, the higher overall PCa detection rate. As for targeted biopsy, it could yield a comparable or even a better effect with fewer cores, compared with traditional random biopsy. Conclusion: Taken together, in a comprehensive consideration of four clinical outcomes, our outcomes shed light on that FUS-GB or FUS-GB plus TRUS-GB showed their superiority, compared with other puncture methods in the detection of PCa. Moreover, TPUS or TRUS-GB was more easily associated with the over-diagnosis and over-treatment of PCa. In addition, targeted biopsy was obviously more effective than traditional random biopsy. The subsequent RCTs with larger sample sizes were required to validate our findings.


Key words: prostate cancer, prostate cancer detection, network meta-analysis, randomized controlled trials

## Introduction

Prostate cancer (PCa) is the most common solid tumor diagnosed in the male population, which is also a major public health issue that presented many
challenges in the developed world [1]. Although most PCa followed an indolent course with an estimated 5 -year survival rate of $98.9 \%$, it still ranked second

leading cause of mortality in the western countries [2]. With the widespread usage of the diagnostic methods of PCa, including serum prostate-specific antigen (PSA) measurement, abnormal digital rectal examination (DRE) finding and transrectal ultrasound-guided biopsies (TRUS-GB), it had improved the detection rate of early PCa [3]. As recommended by the European Association of Urology Guidelines, TRUS-GB sampling 6-12 cores, 1-2 for each sextant, was the current standard diagnostic approach in suspicion of PCa [4]. Meanwhile, it was a low-cost, practical tool for visualizing the boundaries of the prostate and its adjacent structures [5]. However, this protocol still had low sensitivity with a detection rate of 27% -$40.3 \%$, which could easily cause a high rate of missed cancer, especially in the anterior areas of the prostate gland [6]. Moreover, it was more easily associated with over-diagnosis of clinically insignificant cancers and failure of detecting clinically significant cancers, which was defined as cancer volume $\geq 0.5 \mathrm{ml}$ for Gleason=6 or any cancer volume for Gleason $\geq 7$ on step-sectional analysis of radical prostatectomy(RP) [7, 8]. Thus, the ideal biopsy strategy for PCa detection remained to be completely defined.

Currently, biopsy strategy of PCa detection included TRUS-GB, transperineal ultrasound-guided biopsies (TPUS-GB), sonographic contrast (CEUS), magnetic resonance imaging-guided biopsy (MRI-GB), MRI-ultrasound fusion-guided biopsy (FUS-GB) and so on [9-12]. All these available biopsy strategy in the detection of PCa had their individual advantages and disadvantages. As for TPUS-GB, it was another primary way to obtain prostate tissue specimen randomly and its pathway was targeted to the lateral, apico-dorsal peripheral and transition zones of PCa, which was expected to increase PCa detection rates [13]. Nevertheless, the results of several clinical randomized controlled trials (RCTs) on the comparison of TRUS-GB and TPUS-GB had remained inconsistent. As for CEUS, it helped to define and characterize neoplastic areas within the periphery of the prostate by amplifying the hypervascular signal provided by Power Doppler [14]. Furthermore, several RCTs had demonstrated its advantage of detecting more cancers than systematic biopsy (SB) with a reduced number of biopsy cores [15]. As for multi-parametric MRI (mp-MRI), it had been demonstrated to be very sensitive and specific for detecting anterior and posterior cancers. Besides, it had been shown that for a volume greater than 0.5 $\mathrm{cm}^{3}$, sensitivity, specificity and the negative predictive value were $86 \%, 94 \%$ and $95 \%$, respectively [16]. Nowadays, two different MRI-guided biopsy techniques had been established: direct MRI-guided
biopsy and MRI-ultrasound fusion-guided biopsy (FUS-GB) [17]. The current drawbacks of MRI were its inability to differentiate between prostate cancer and prostatitis or inflammation and meanwhile it was costly, time-consuming, operator-dependent [16, 18]. Last but not least, FUS-GB plus TRUS-GB, which combined MRI-guided targeted biopsy and systematic TRUS-GB within one biopsy session, had been reported a $60 \%$ detection rate of PCa in 106 patients undergoing FUS-GB with additional systematic biopsy by Hadaschik et al [19].

Along with the increasing recognition of PCa's over-diagnosis and over-treatment, various imaging-guided biopsy methods had been utilized in an attempt to increase the cancer detection rate and meanwhile surgeons and patients were eager to understand which strategy was relatively the best choice to diagnose PCa accurately and reasonably [20]. Due to the absence of direct statistical analysis and limited evidence, it was harder for physicians to provide the optimal biopsy strategy. Hence, we took advantage of network meta-analysis and anticipated it to provide a hierarchy of different puncture methods in a broad spectrum of the population [21, 22]. Six different PCa biopsy strategies consisted of TRUS-GB, TPUS-GB, CEUS, MRI-GB, FUS-GB as well as FUS-GB plus TRUS-GB, and four clinical outcomes composed of overall PCa detection, significant PCa detection, insignificant PCa detection as well as comparison of different TRUS-guided biopsy cores, were ultimately analyzed in this study. As a result, our analysis was anticipated to provide some references for clinical practice.

## Material and methods

## Search strategy

Relevant articles were comprehensively retrieved from Pubmed, Embase, Web of Science, up to July 2017. The search strategy consisted of three parts (biopsy strategy, prostate cancer detection, and a specific filter for randomized controlled trials), using the following keywords in combination with Medical Subject Headings(MeSH) terms and text words: transrectal ultrasound-guided biopsy (TRUS-GB), transperineal ultrasound-guided biopsies (TPUS-GB), sonographic contrast (CEUS), magnetic resonance imaging-guided biopsy (MRI-GB), MRI-ultrasound fusion-guided biopsy (FUS-GB), prostate cancer detection, and randomized controlled trials (RCTs). Two reviewers independently screened titles and abstracts of retrieved articles in an initial search. Amongst them, irrelevant studies would be ruled out, and the remaining full text articles were evaluated, according to inclusion criteria.

## Inclusion and exclusion criteria

Studies enrolled in this meta-analysis had to meet the following criteria: (1) The language of the article was limited to English; (2) Sufficient data could be extracted from each included original study; (3) The study was designed as randomized controlled trials; (4) At least two of different biopsy methods were mentioned and compared; (5) Clinical outcomes including overall PCa detection, significant PCa detection, insignificant PCa detection and comparison of different TRUS-guided biopsy cores should be extracted in these involved articles.

Studies would be excluded if they met the following criteria: (1) The language of the article was non-English; (2) The publication types of studies were reviews or letters or case reports or comments or editorials; (3) No sufficient and qualified data could extracted from these studies.

## Data extraction and quality assessment

All eligible studies were independently reviewed by two blind reviewers (Y.W, JD.Z), according to the inclusion and exclusion criterion. Besides, the discrepancies were handled by a discussion with a third reviewer (ZQ.Q). All data were centrally extracted from the included publications, including first author's name, publication year, treatment, puncture method, overall PCa detection, clinically significant PCa detection, insignificant PCa detection and endpoints. All of the aforementioned data were comprehensively presented in Table 1. According to the Cochrane Handbook [23], the quality of eligible studies was evaluated the potential source of bias as follows: (1) Random sequence generation; (2) Allocation concealment; (3) Blinding of participants and personnel; (4) Blinding of outcome assessment; (5) Incomplete outcome data; (6) Selective reporting; (7) Other bias. The judgments were graded as a low, high or unclear risk of bias (http://www.cochranehandbook.org; Figure 1, 2). The flow diagram of the literature selection process was detailed in Figure 3.

## Statistical analysis

A pair-wise meta-analysis was performed to make direct comparison between two biopsy strategies, and the results were evaluated by the pooled odds ratio (OR) with $95 \%$ confidence interval (CI). The Chi-square test and I-square test were used to assess the heterogeneity; If $I^{2}>50 \%$ or Chi-square test $P>0.10$, it was considered as existence of significant heterogeneity. With the presence of the heterogeneity, the random-effects model was applied and ORs was calculated by the DerSimonian-Laird method; whereas in the non-existence of heterogene-
ity, the fixed-effects model (the Mantel-Haenszel method) was conducted. Publication bias was examined by Begg's and Egger's test [24]. $P$ values were adopted by a two-sided test and $P<0.05$ was regarded as statistically significant. In addition, calculations of traditional meta-analysis were conducted by Stata software (version 12.0; StataCorp LP, College Station, TX).

In addition to traditional meta-analysis, a network meta-analysis concerning multiple treatments was performed by a random-effect model within a Bayesian framework, using package "gemtc" version 0.8.2 of R software (version 3.4.0; R Foundation, Vienna, Austria) [25, 26]. Odds ratio (OR) with $95 \%$ credible interval (CrI) was calculated by Markov chain Monte Carlo methods. The function mtc.run would be used to generate samples by means of the Markov chain Monte Carlo sampler. We set 10,000 simulations for each chain as the "burn-in" period, yielding 40,000 iterations to obtain the OR of model parameters, when three Markov chains run simultaneously. The model convergence was accessed by Brooks-Gelman-Rubin plots method, trace plot and density plot (Supplement Figure 1, 2) [27]. In addition, the rank probabilities would be calculated to obtain the hierarchy of each treatment. Based on the results of rank probabilities, clinical surgeons could make the choice which puncture method could be best, second and so on [28]. The matrix of rank probabilities and the plot of rank probabilities were provided by the "gemtc" package simultaneously. From direct plot of rank probabilities, we could easily find the ranking of each biopsy strategy [29]. From cumulative rank plot, we could easily find the proportion of each ranking [30].

The pooled ORs from network meta-analysis and traditional meta-analysis were compared to estimate the consistency between direct and indirect comparisons. To access the inconsistency, the node-splitting method was implemented by reporting its Bayesian $P$ value, by means of separating the evidence concerning certain comparison into direct and indirect evidence, when a loop connecting three arms existed [31]. Last but not least, the mtc.anohe command of the "gemtc" package would be utilized to evaluate the global heterogeneity, based on the bias of the magnitude of heterogeneity variance parameter $I^{2}$.

## Results

## Search results and study characteristics

The literature search yielded 235 citations, through online databases using previous search strategy. Amongst them, 197 records were excluded

because of reviews, letters, case-reports, duplicates and so on, after screening the tittles and abstracts. The full texts of the remaining 38 articles were evaluated by the reviewers, and finally 20 RCTs were eligible for this meta-analysis (Figure 3) [2, 10, 11, 32-48]. Meanwhile, the detailed characteristics of the enrolled 20 studies with 4,571 participants were summarized in Table 1. All of these enrolled studies were RCTs and the quality of evidence was evaluated by the Cochrane Handbook and graded each potential source of bias as low, high or unclear. The details were displayed in Figure 1, 2. Clinical outcomes of involved articles included overall PCa detection, clinically significant PCa detection, insignificant PCa detection and comparison of different TRUS-guided biopsy cores.

## Network structure diagrams

These enrolled studies covered six different PCa biopsy strategies: TRUS-GB, TPUS-GB, CEUS, MRI-GB, FUS-GB and FUS-GB plus TRUS-GB. The network structure diagrams, which presented the direct association between different puncture methods, were displayed in Figure 4. Besides, the thicknesses of the lines were proportional to the number of comparisons, and the diameters of the circles were proportional to the number of treatments included in the network meta-analysis.

Table I. Main characteristics of individual studies included in the network meta-analysis.


TRUS-GB: transrectal ultrasound-guided biopsy; TPUS-GB: transperineal ultrasound-guided biopsy; CEUS: sonographic contrast; MRI-GB: magnetic resonance imaging-guided biopsy; FUS-GB: MRI-ultrasound fusion-guided biopsy; RB: random biopsy; TB: targeted biopsy; NA: not available. (1)Overall PCa detection; (2)Significant PCa detection; (3)Insignificant PCa detection; (4)Comparison of different TRUS-guided biopsy cores.

![img-0.jpeg](img-0.jpeg)

Figure 1. Risk of bias graph. Review author's judgement for each risk of bias item presented as percentages of all included studies.
![img-1.jpeg](img-1.jpeg)

Figure 2. Risk of bias summary. Review author's judgement for each risk of bias item for individual studies.

## Overall PCa detection

A total of 14 studies including six different PCa biopsy strategies contributed to the analysis of overall PCa detection. The efficacy of different PCa biopsy strategies by ORs and corresponding $95 \%$ CrIs was displayed in Figure 5. The detailed rankings of different biopsy strategies were presented in Table 2A. Based on it, Figure 6A and Figure 7A were established. Figure 6A was a direct plot of rank probabilities, from which we could easily find the ranking of each biopsy strategy. Figure 7A was a cumulative rank plot, from which we could easily find the proportion of each ranking. As a result, the cumulative rank probability of overall PCa detection from best to worst was FUS-GB plus TRUS-GB, FUS-GB, CEUS, MRI-GB, TRUS-GB and TPUS-GB. Bayesian $P$ values of node-splitting method were all $>0.05$, which indicated that the direct and indirect evidence was consistent (Figure 8A).

## Significant PCa detection

Seven studies including six different PCa biopsy strategies were involved in the analysis of clinically significant PCa detection. The efficacy of all PCa biopsy strategies by ORs and corresponding $95 \%$ CrIs was showed in Figure 5B. The detailed rankings of different biopsy strategies were presented in Table 2B. Besides, Figure 6B was a direct plot of rank probabilities and Figure 7B was a cumulative rank plot. As a result, the cumulative rank probability results indicated that CEUS, FUS-GB or FUS-GB plus TRUS-GB had a higher, whereas TRUS or TPUS-guided biopsy had a relatively lower significant PCa detection rate. The results of node-splitting method were all above 0.05 , indicating the consistency of the direct and indirect evidence (Figure 8B).

## Insignificant PCa detection

The results of insignificant PCa detection were calculated by seven studies including six different PCa biopsy strategies. The ORs and corresponding

![img-2.jpeg](img-2.jpeg)

Figure 3. The flow diagram of the literature selection process.

95\% CrIs were displayed in Figure 5C. The detailed rankings of different biopsy strategies were presented in Table 2C. Besides, Figure 6C was a direct plot of rank probabilities and Figure 7C was a cumulative rank plot. As a result, rank probability results indicated that MRI-GB, TPUS-GB or TRUS-GB had a higher, whereas FUS-GB or CEUS had a lower relatively insignificant PCa detection rate. Node-splitting method indicated the consistency of the direct and indirect evidence (Figure 8C).

## Comparison of different TRUS-guided biopsy cores

A total of seven studies including six different TRUS-guided biopsy strategies (6-core, 8-core, 10-core, 12-core, 15-core, 18-core) contributed to the analysis of the overall PCa detection of different TRUS-guided biopsy cores. The efficacy of different TRUS-guided biopsy strategies by ORs and corresponding $95 \%$ CrIs was displayed in Figure 5D. The detailed rankings of different biopsy strategies were presented in Table 2D. Besides, Figure 6D was a direct plot of rank probabilities and Figure 7D was a cumulative rank plot. As a result, rank probability results showed the general trend was that the more the biopsy cores, the higher the overall PCa detection rate, in addition to 15 -core biopsy strategy which
might be the shortage of sufficient data. The Bayesian $P$ value of node-splitting method was $>0.05$, indicating that the direct and indirect evidence was consistent (Figure 8D).

## Node-splitting method

When a loop connecting three arms existed, the node-splitting method was implemented by reporting its Bayesian $P$ value, by means of separating the evidence concerning certain comparison into direct and indirect evidence, to access the inconsistency. We could easily find that all the $P$ values of node-splitting method were above 0.05 , which indicated the consistency of the direct and indirect evidence (Figure 8).

## Discussion

Currently, TRUS-guided systematic biopsy was the gold standard biopsy strategy in the detection of PCa, recommended by the European Association of Urology guidelines 4]. Although it was a low-cost, practical tool, a large proportion of PCa patients were still missed by conventional TRUS-GB, especially in the anterior areas of the prostate gland. In addition, the harm of unnecessary biopsies and over-diagnosis of PCa had generally outweighed the benefit of reducing mortality of PCa in elderly men by

traditional method [33]. Along with the development of technology, various different biopsy techniques had come out in an attempt to increase the cancer detection. However, due to the lack of direct comparisons of different biopsy strategies, both the
clinical surgeons and their patients were still confused in the choice of a better puncture method. Hence, this network meta-analysis was performed to solve the dilemma.
![img-3.jpeg](img-3.jpeg)

Figure 4. Network structure diagrams. (A) Overall PCa detection; (B) Significant PCa detection; (C) Insignificant PCa detection; (D) Comparison of different TRUS-guided biopsy cores. The thicknesses of the lines were proportional to the number of comparisons; the diameters of the circles were proportional to the number of treatments.
![img-4.jpeg](img-4.jpeg)

Figure 5. The efficacy of different PCa biopsy strategies by ORs and corresponding $95 \%$ Crls. (A) Overall PCa detection; (B) Significant PCa detection; (C) Insignificant PCa detection; (D) Comparison of different TRUS-guided biopsy cores.

Table 2: Detailed rank probability. (A) Rank probability of Overall PCa detection; (B) Rank probability of Significant PCa detection; (C) Rank probability of Insignificant PCa detection; (D) Rank probability of Different TRUS-guided biopsy cores.


TRUS: transrectal ultrasound-guided biopsy; TPUS: transperineal ultrasound-guided biopsy; CEUS: sonographic contrast; MRI: magnetic resonance imaging-guided biopsy; FUS: MRI-ultrasound fusion-guided biopsy;

![img-5.jpeg](img-5.jpeg)

Figure 6. Rank of probability for effective outcomes. (A) Overall PCa detection; (B) Significant PCa detection; (C) Insignificant PCa detection; (D) Comparison of different TRUS-guided biopsy cores.

![img-6.jpeg](img-6.jpeg)

Figure 7. Cumulative rank plot for effective outcomes. (A) Overall PCa detection; (B) Significant PCa detection; (C) Insignificant PCa detection; (D) Comparison of different TRUS-guided biopsy cores.
![img-7.jpeg](img-7.jpeg)

Figure 8. Node-splitting method in comparison between direct and indirect evidence. (A) Overall PCa detection; (B) Significant PCa detection; (C) Insignificant PCa detection; (D) Comparison of different TRUS-guided biopsy cores.

To the best of our knowledge, this was the first network meta-analysis comparing the efficacy and accuracy of different biopsy strategies in the detection of PCa. A total of 20 RCTs including 4,571 patients were ultimately enrolled. Besides, six different PCa biopsy strategies (TRUS-GB, TPUS-GB, CEUS, MRI-GB, FUS-GB as well as FUS-GB plus TRUS-GB) and four clinical outcomes (overall PCa detection, significant PCa detection, insignificant PCa detection as well as comparison of different TRUS-guided biopsy cores), were simultaneously analyzed in this study. In terms of overall PCa detection and significant PCa detection rate, our results indicated that FUS-GB or FUS-GB plus TRUS-GB showed their superiority. As for TRUS-GB or TPUS-GB, compared with others, they had the lowest overall detection rate, not to mention its inferiority in significant PCa detection.

In the detection of insignificant PCa, the rate of MRI-GB, TPUS-GB or TRUS-GB was relatively higher. Coupled with previous results, we found that TPUS-GB or TRUS-GB had a relatively lower overall or significant PCa detection rate and a relatively higher insignificant PCa detection rate. Associated with the increasing recognition of over-diagnosis and over-treatment of PCa, these two conventional random biopsy strategies might easily contribute to the formation of this situation. Strangely, our results also presented the negative role of MRI-GB in the detection of insignificant PCa. Usually, MRI-GB had a higher degree of accuracy in the detection of clinically significant PCa and several researches had demonstrated it [16]. After re-checking our original data, this could contribute its insufficient data. More relevant data of MRI-GB were required in subsequent researches to rectify our results.

Last but not least, as for TRUS-guided biopsy, the general trend was that the more cores, the higher the detection rate. Nevertheless the 15-core TRUS-guided biopsy showed a relatively lower detection rate which could attribute to two reasons. On the one hand, the more the cores, the higher rate of occurring adverse reactions. On the other hand, RCTs regarding the different cores of TRUS-guided biopsy was quite sparse. Therefore, upcoming prospective RCTs were required to provide more available data. As showed in the results, we could easily find that a combination of different biopsy strategies could easily enhance the PCa detection rate, which brought us a novel idea with respect to increasing its effectiveness. Furthermore, complications and adverse reactions should be carefully evaluated before applying this kind of method into clinical use.

The advent of new biopsy technology such as FUS-GB or MRI-GB and so on, had changed strategies
of prostate biopsy, which allowed clinical surgeons to operate biopsy directly to the suspected areas rather than randomly [49, 50]. Usually, it seemed reasonable that the more cores, the higher the PCa detection rate in terms of conventional random biopsy. However, when compared with random biopsy, it was interesting that targeted biopsy could yield a significantly higher positivity rate for detecting PCa and thus require fewer cores [11]. Moreover, compared with traditional random biopsy, targeted biopsy had greater potential to improve benefit-to-harm ratio, in the era of PCa's over-diagnosis and over-treatment [32]. Obviously, this observation was in line with our results. We could easily conclude that targeted biopsy was more effective than traditional random biopsy, which shed light on the potential of FUS-GB or TRUS-GB plus FUS-GB as the first-line technique for detecting PCa in the following years.

In addition to different biopsy methods, there were also several other factors influencing the efficacy of detection of PCa. Accumulating data indicated that risk-stratification before biopsy was crucial for detection rate and unnecessary biopsies, such as prostate imaging and reporting data system (PI-RADS) score, different PSA or Gleason score levels and so on[33, 35]. According to the study by Alberts et.al [33], the detection rate of overall PCa or significant PCa in lesions with PI-RADS scores of 4-5 was markedly higher than in those with a PI-RADS score of 3. On the other hand, a meta-analysis by Hu et.al demonstrated that a high body mass index correlated positively with prostate cancer detection, especially high-grade prostate cancer detection [51].

As far as we were concerned, all of the results above-mentioned were made without the consideration of the complications of different biopsy strategies, nor the cost-effective way. Just from a technical perspective, FUS-GB or TRUS-guided biopsy plus FUS-GB biopsy showed their advantages. However, complications of different biopsy strategies and the cost-benefit analysis were another two major concerns, which a considerable number of patients would pay attention to. However, all of the available literature was rarely involved in it. Hopefully, subsequent analysis should take into account of these two aforementioned aspects.

The strength of our study was its strict inclusion criteria for RCTs, which could have a clear impact on the group baseline features and provide enough statistical power. In addition, it was the first time for us to put forward the hierarchy of the efficacy of different PCa biopsy strategies, which was anticipated to guide the clinical work. Nonetheless, several potential limitations should be paid attention to

before fully understanding this aim of study. Firstly, although a total of 20 RCTs were finally included, the number of RCTs enrolled in significant PCa detection, insignificant PCa detection and comparison of different TRUS-guided biopsy cores were relatively small, which could result in some bias. Secondly, the research of the complications of different biopsy strategy or the cost-benefit analysis was not involved in this article, due to the scarcity of relevant data. Thus, further stratified analyses based on a larger set of samples were recommended, which could be an important issue for future research.

Taken together, the present network meta-analysis combining both direct and indirect evidences from currently available studies was performed to compare the merits of different biopsy strategies. Our results were inclusive and consistent with previous studies. The results shed light on that FUS-GB or FUS-GB plus TRUS-GB showed their superiority, compared with other puncture methods, in the detection of PCa. Moreover, TPUS or TRUS-guided biopsy was more easily associated with the harms of unnecessary biopsies and overdiagnosis, which should balance against the benefit of mortality reduction achieved by screening. As for targeted biopsy, it could yield a comparable or even a better effect with fewer cores, compared with traditional random biopsy.

## Conclusion

In summary, the outcomes of the present network meta-analysis shed light on that FUS-GB or FUS-GB plus TRUS-GB showed their superiority, compared with other puncture methods, in the detection of PCa. Besides, TPUS or TRUS-GB was more easily associated with the harms of unnecessary biopsies and over-diagnosis. In terms of TRUS-GB, the general trend was that the more biopsy cores, the higher the overall PCa detection rate. As for targeted biopsy, it was obviously more effective than traditional random biopsy. The subsequent prospective RCTs were required to provide more available data to elaborate the efficacy of different biopsy strategies.

## Supplementary Material

Supplementary figures.
http://www.jcancer.org/v09p2237s1.pdf

## Acknowledgements

This article was funded by Medical key talent of Jiangsu Province: ZDRCA2016009 which had no role in study design, data collection, data analysis, data interpretation or writing of the report. The corresponding author had full access to all the data in
the study and had final responsibility for the decision to submit for publication.

## Authors' Contributions

XH.M, NH.S: Protocol/project development;
YM.W, C.C, YC.W: Data collection or management;
X.Z, QJ.Z: Data analysis;
Y.W, ZQ.Q, JD.Z: Manuscript writing/editing.

## Competing Interests

The authors have declared that no competing interest exists.
