# Comparative Efficacy of East Asian Herbal Formulae Containing Astragali Radix-Cinnamomi Ramulus Herb-Pair against Diabetic Peripheral Neuropathy and Mechanism Prediction: A Bayesian Network Meta-Analysis Integrated with Network Pharmacology 

Hee-Geun Jo ${ }^{1,2, \star}$ (D), Eunhye Baek ${ }^{3}$ and Donghun Lee ${ }^{1, \star}$ (D)

## check for updates

Citation: Jo, H.-G.; Baek, E.; Lee, D. Comparative Efficacy of East Asian Herbal Formulae Containing Astragali Radix-Cinnamomi Ramulus Herb-Pair against Diabetic Peripheral Neuropathy and Mechanism Prediction: A Bayesian Network Meta-Analysis Integrated with Network Pharmacology. Pharmaceutics 2023, 15, 1361. https://doi.org/10.3390/ pharmaceutics15051361

Academic Editor: Donald E. Mager
Received: 14 March 2023
Revised: 19 April 2023
Accepted: 24 April 2023
Published: 28 April 2023

## (0)

Copyright: (c) 2023 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 Department of Herbal Pharmacology, College of Korean Medicine, Gachon University, 1342 Seongnamdae-ro, Sujeong-gu, Seongnam 13120, Republic of Korea
2 Naturalis Inc., 6 Daewangpangyo-ro, Bundang-gu, Seongnam 13549, Republic of Korea
3 RexSoft Inc., 1 Gwanak-ro, Gwanak-gu, Seoul 08826, Republic of Korea

* Correspondence: jho3366@hanmail.net (H.-G.J.); dlee@gachon.ac.kr (D.L.)

Abstract: The Astragali Radix-Cinnamomi Ramulus herb-pair (ACP) has been widely used in the treatment of diabetic peripheral neuropathy (DPN) as part of East Asian herbal medicine (EAHM). Eligible randomized controlled trials (RCTs) were identified by searching 10 databases. The outcomes investigated were response rate, sensory nerve conduction velocity (SNCV), and motor nerve conduction velocity (MNCV) in four regions of the body. The compounds in the ACP and their targets of action, disease targets, common targets, and other relevant information were filtered using network pharmacology. Forty-eight RCTs, with 4308 participants, and 16 different interventions were identified. Significant differences were observed in the response rate, MNCV, and SNCV, as all EAHM interventions were superior to conventional medicine or lifestyle modification. The EAHM formula containing the ACP ranked highest in more than half of the assessed outcomes. Furthermore, major compounds, such as quercetin, kaempferol, isorhamnetin, formononetin, and beta-sitosterol, were found to suppress the symptoms of DPN. The results of this study suggest that EAHM may increase therapeutic efficacy in DPN management, and EAHM formulations containing the ACP may be more suitable for improving treatment response rates to NCV and DPN therapy.

Keywords: herbal medicine; diabetic peripheral neuropathy; network meta-analysis; network pharmacology; herb-pair

## 1. Introduction

Diabetic peripheral neuropathy (DPN) is a common complication, affecting around half of diabetic patients [1,2]. Both diabetes and prediabetes can cause DPN, leading to various types of nerve damage and accompanying clinical findings [3-5]. Accordingly, approximately $40 \%$ of patients with DPN develop neuropathic pain that does not respond to treatment, and various motor dysfunctions and sensory losses [4,6]. Owing to these pathophysiological characteristics, DPN not only reduces the quality of life of patients but also imposes an immense social burden. A recent study reinforced this problem by reporting that the medical expenses of patients with painful DPN are $20 \%$ higher than those of diabetic patients without corresponding complications, and the cost increases over time [7]. Various interventions for the treatment and management of DPN have been discussed; however, no disease-modifying treatment is available [1,8]. Currently, the main therapies focus on symptomatic pain relief using conventional medicines (CM), such as anticonvulsants, antidepressants, methylcobalamin, and alpha-lipoic acid [9,10]. Therefore,

further investigation is needed to develop candidate drugs that can alleviate DPN-related systemic pathophysiology while exhibiting fewer adverse events.

Natural products are considered a promising alternative treatment because they can be applied to the multifaceted lesions of DPN owing to their safety and higher patient compliance [11,12,13,14,15]. Recent studies have reported that widely used plant compounds can improve DPN because of their neuroprotective, antioxidative, and anti-neuroinflammatory effects [16]. Flavonoids, alkaloids, phenolic compounds, terpenoids, saponins, and phytosteroltype constituents of herbal medicines used worldwide are being actively studied as new drug candidates for the treatment of various diabetic complications [17]. Among these, East Asian herbal medicine (EAHM) is an area of natural medicine in which therapeutic candidates for DPN have been the most actively investigated [10,12,18,19,20,21]. EAHM is a generic term for natural materials used as medicines for the treatment of diseases in many countries in East Asia, including Korea, China, Taiwan, and Japan, and the study thereof [22,23,24,25,26]. EAHM is operated under a unique prescription principle that seeks to maximize the synergistic effect of polyherbal formulae and is distinct from herbal medicine in other regions of the world in that treatments using the same materials are practiced in several countries [27,28,29,30]. EAHM is still being actively used for treatment in the aforementioned regions, and substantial clinical and preclinical evidence establish its efficacy [19,31,32,33]. Therefore, considering the efficacy of EAHM in DPN treatment, the EAHM constituents conducive to DPN mitigation must be investigated.

As described above, in EAHM, the synergistic effect of drug combinations is as important as that of a single material. A combination of two or three materials capable of obtaining such a synergistic effect is called an "herb-pair", which is the smallest unit of an EAHM polyherbal formula and an appropriate unit of analysis for investigating candidate therapeutics [34,35,36,37]. One useful herb-pair for DPN, as suggested in several previous studies and by traditional experience, is the Astragali Radix-Cinnamomi Ramulus herbpair (ACP). Previous reviews have reported the effectiveness of prescriptions, including ACP, for cervical radiculopathy, neuropathy with DPN, and other mechanisms [38,39]. Furthermore, previous studies assessing the effect of EAHM on peripheral neuropathy and association rule mining on individual materials have revealed a pattern of relationships between the two herbs constituting the ACP [40]. In addition, preclinical evidence related to Hwanggi Gyeji Omul-tang (Huangqi Guizhi Wuwu decoction in Chinese), a representative EAHM formula containing the ACP, shows that this combination may exert neuroprotective effects against various causes of neuropathy and nerve damage [41,42,43,44]. Several approaches are being used to explore effective EAHM formulae or herb-pairs that are believed to have synergistic effects. However, a research method for comparing the benefits of the anticipated synergistic effects of individual herb-pairs, rather than multiherbal formula units, has not yet been fully established.

Accordingly, we hypothesized that the ACP might be a combination that can show high efficacy in the treatment of DPN. To verify this hypothesis, this study was conducted as follows: (1) After a systematic search for randomized controlled trials in patients with DPN, a Bayesian network meta-analysis was performed to determine whether the EAHM formula containing the ACP was superior to that without the ACP. (2) Further network pharmacology analyses of the ACP were performed to predict the compounds and gene targets involved in the putative synergistic mechanisms. Therefore, we aimed to explore the efficacy of ACP in the treatment of DPN and its potential as a candidate drug.

# 2. Materials and Methods 

This study was conducted in accordance with the Preferred Reporting Items for Systematic Reviews and Meta-Analyses extension statement for network meta-analysis [45]. The protocol for this systematic review was registered in PROSPERO (registration number: CRD42021290004). This study was conducted as a process of building multidisciplinary-integrative-decision making-actual achievement-scientific creativity (M.I.D.A.S) research platform.

# 2.1. Search Strategy 

A comprehensive electronic search of four databases in English (PubMed, Cochrane Library, Cumulative Index to Nursing and Allied Health Literature (CINAHL), and EMBASE, four Korean databases (Korean Studies Information Service System (KISS), Research Information Service System (RISS), Oriental Medicine Advanced Searching Integrated System (OASIS), and Korea Citation Index (KCI)), one Chinese database (Chinese National Knowledge Infrastructure Database (CNKI)), and one Japanese database (CiNii) was conducted by two investigators from inception to 20 July 2021. The following Boolean format was used for the search: (mononeuropathy (MeSH) OR nerve compression syndromes (MeSH) OR neuralgia (MeSH) OR polyneuropathies (MeSH)) AND ("neuropathy"(Title/Abstract) OR "peripheral neuropathy"(Title/Abstract) OR "neuropathic pain"(Title/Abstract) OR "neuralgia"(Title/Abstract)) AND ("Medicine, Chinese Traditional"(MeSH) OR "Medicine, Kampo"(MeSH) OR "Medicine, Korean Traditional"(MeSH) OR "Herbal Medicine"(MeSH)). These search terms were appropriately modified to perform a search in the Korean, Chinese, and Japanese databases. The detailed search strategy is shown in Supplementary Table S1.

### 2.2. Study Selection

### 2.2.1. Type of Studies

Only randomized controlled trials (RCTs) evaluating the efficacy and safety of oral administration of EAHM for DPN were included. There were no restrictions on language, publication date, or type of diabetes. Studies were excluded if they met any of the following criteria: (a) not an RCT or quasi-RCT; (b) a control group was not used or was inappropriate; (c) unrelated to manifestations due to DPN; (d) animal experiments; (e) case reports or reviews; or (f) not published in peer-reviewed scientific journals, including postgraduate theses or dissertations.

### 2.2.2. Type of Participants

Trials were considered eligible for inclusion if they were conducted on adults (age $>18$ years) diagnosed with DPN with no restrictions on age, sex, or race.

### 2.2.3. Type of Interventions

RCTs trials comparing EAHM as an active intervention in the treatment group with CM in the control group were included. However, RCTs that used a combination of EAHM and CM as an intervention were beyond the scope of this review and were omitted. All dosage forms of EAHM intervention for symptom management in DPN, such as decoctions, granules, and capsules, were included. Studies in which East Asian medical interventions such as acupuncture, massage, or other nondrug therapies were only combined in the treatment group were excluded. Studies in which the control group included other EAHM were excluded. Even if all other inclusion criteria were satisfied, RCTs in which the exact constituent herbs of the EAHM formulation used as an intervention were not identified were excluded.

### 2.2.4. Type of Outcome Measures

The remission rate of DPN-related global symptoms observed according to the explicit criteria was selected as the outcome measure. However, most of the included studies reported the remission rates of complete remission (CR), partial remission (PR), mild remission (MR), and no remission (NR) as CR + PR/all patients. Considering that the remission rates reported by individual studies would have led to inconsistencies in the outcomes because different studies used different categorization criteria, the proportion of patients who achieved symptom alleviation in each group was used as the response rate in this review, and various study results were converted into this system.

The first set of secondary outcomes was indices evaluating motor nerve conduction velocities associated with neurological abnormalities in patients with DPN. Therefore,

to evaluate the neurological improvement of the motor nerves, the median motor nerve conduction velocity (MMNCV), ulnar motor nerve conduction velocity (UMNCV), peroneal motor nerve conduction velocity (PMNCV), and tibial motor nerve conduction velocity (TMNCV) were selected as indices for each upper and lower extremity. The second set of secondary outcomes was indices evaluating sensory nerve conduction velocities associated with neurological abnormalities in patients with DPN. Accordingly, the median sensory nerve conduction velocity (MSNCV), ulnar sensory nerve conduction velocity (USNCV), peroneal sensory nerve conduction velocity (PSNCV), and tibial sensory nerve conduction velocity (TSNCV) were selected as indices for the upper and lower limbs. Finally, the adverse events occurring in each intervention and control group were used as safety evaluation indicators.

# 2.3. Data Extraction 

According to the aforementioned search strategy, titles and abstracts of potentially eligible studies were independently screened by two investigators (H.-G.J. and D.L.). Subsequently, a full-text review was conducted based on the inclusion and exclusion criteria. Information from the included studies was independently extracted by two reviewers (H.-G.J. and D.L.). The following information was collected: title, author name, the country where the clinical trial was conducted, diagnostic criteria, trial design, publication year, sample size, participant age, sex distribution, interventions in the treatment group and comparators, treatment duration, outcome index, reported adverse events, EAHM composition, and dosage. Discrepancies were resolved through discussions between the two investigators.

### 2.4. Methodological Quality Assessment

Two investigators (H.-G.J. and D.L.) independently evaluated the methodological quality of each included study using the revised tool for the risk of bias in randomized trials, RoB 2 [46]. RoB 2 is characterized by the following five bias domains: bias arising from the randomization process, bias due to deviations from intended interventions, bias due to missing outcome data, bias in selecting the reported results, and bias in the measurement of the outcome. Methodological quality was assessed at three levels: "high risk of bias", "low risk of bias", and "some concerns". Disagreements between the two investigators were resolved through discussions.

### 2.5. Data Analysis

### 2.5.1. Pairwise Meta-Analysis

A pairwise meta-analysis (PMA) was performed to directly compare the EAHM with the comparator. Evidence synthesis of the included studies using the available data was performed by calculating the effect size and $95 \%$ confidence interval (CI) using a randomeffects model. Heterogeneity was considered statistically significant when the $p$-value based on the $\chi^{2}$ test was $<0.10$ or $\mathrm{I}^{2}$ was $\geq 50 \%$. Two-sided $p<0.05$ was considered statistically significant. Statistical synthesis of individual research results was performed using the software R (version 4.1.2; R Foundation for Statistical Computing, Vienna, Austria) and RStudio version 2022.02.3 build 492 (Integrated Development for R. RStudio, PBC, Boston, MA, USA) using the default settings of the "meta" and "metafor" package [47]. The RR and $95 \%$ confidence interval (CI) were calculated for the response rate. The mean difference (MD) and $95 \%$ confidence interval (CI) were calculated for the motor and sensory nerve conduction velocities. If heterogeneity was observed in the synthesized meta-analysis results for outcome measures involving $>10$ trials, the cause of heterogeneity was traced using sensitivity analysis. To distinguish publication bias, a contour-enhanced funnel plot that included most of the studies was used [48]. To address the asymmetry of the visually confirmed funnel plot, Egger's test [49] and Begg's test [50] were performed to confirm publication bias. The overall quality of evidence for each outcome was evaluated using the Grading of Recommendations Assessment, Development, and Evaluation (GRADE)

Pro [51]. The GRADE assessment evaluated the overall quality of evidence on four levels: very low, low, moderate, and high. The level of evidence is lowered by factors such as the risk of bias, inconsistency, indirectness, imprecision, and publication bias.

# 2.5.2. Network Meta-Analysis 

A network meta-analysis (NMA) was performed to evaluate the relative efficacy of EAHM formulae containing AC herb-pairs and other interventions. In this review, Bayesian NMAs were performed using R v. 4.1.2, and RStudio V. 2022.02.3 build 492 to evaluate the comparative effectiveness of treatments, using the most commonly used control intervention as a common comparator. The default settings of the R packages "BUGSnet" and "GeMTC" were used for the implementation of NMA [52,53]. For the response rate results, the effect was measured as an odds ratio (OR) with a $95 \%$ credible interval (Crl) using the binomial distribution assumption and logit link function. For the results of the eight nerve conduction velocity indices, the effects were analyzed as MD with $95 \%$ Crl using the normal likelihood model and identity link function. Markov chain Monte Carlo (MCMC) simulations were set up with a burn-in of 20,000 iterations and a total of 50,000 iterations, and every 10th value was extracted. Convergence was graphically assessed using trace and density plots. Node splitting was performed to assess the consistency of the response rate and a leverage plot was used to compare the DIC of the model based on the consistency assumption and the inconsistent model for the secondary outcome. A heat map with all feasible comparisons was constructed using the relative effect estimates from the NMA. We used a surface under the curve cumulative ranking probabilities (SUCRA) plot to demonstrate the ranking of treatments.

### 2.5.3. Network Pharmacology Analysis of the Synergistic Mechanism of the ACP against DPN

All bioactive ingredients in the ACP were screened and retrieved from the Traditional Chinese Medicine Systems Pharmacology (TCMSP; https://tcmsp-e.com/) analysis platform [54]. In this study, components with oral bioavailability (OB) $\geq 30 \%$ and drug-likeness (DL) index $\geq 0.18$ were selected as candidate ingredients. The target information of active ingredients was standardized using the Uniprot database (http:// www.uniprot.org/) with the species filter "Homo sapiens". Using "diabetic peripheral neuropathy" as the keyword, data on DPN-related target genes were obtained from the GeneCards database (http://www.genecards.org). For targets in GeneCards, only those with a score $\geq 10$ were screened [55]. Venn diagrams of consensus targets between the ACP and DPN were constructed using the Bioinformatics and Evolutionary Genomics website (https://bioinformatics.psb.ugent.be/webtools/Venn/). Using Cytoscape (v. 3.9.1; https://cytoscape.org/), a network of the components of the ACP and DPN targets was created to graphically depict the complex interactions between compounds and targets. The degree of each node is measured using a layout tool: the larger the node in the network, the higher the degree. The STRING protein analysis platform (v. 11.5; https://string-db.org/), together with the protein categorization "Homo sapiens", was used to import the interacting gene targets of the ACP and DPN [56]. Protein interaction network analysis was performed and Cytoscape software version 3.9.1 [57] was used to construct protein-protein interaction (PPI) network maps. Gene targets with a degree of centrality above the average value were selected as hub targets. Gene ontology (GO) functional analysis was used as the primary method to describe the functions of gene targets, including biological processes, cellular components, and molecular functions. Kyoto Encyclopedia of Genes and Genomes (KEGG) enrichment analysis was used to identify common targets of the ACP and DPN in the signaling pathways. Metascape (https://metascape.org/), an online tool for gene enrichment analysis, incorporates more than 40 functional annotation datasets [58]. Hub targets were uploaded to the Metascape platform for GO and KEGG analyses. The data selection criterion was set at $p<0.05$.

## 3. Results

### 3.1. Study Identification

Based on the search strategy, 903 potentially relevant articles were identified through electronic searches of 10 databases. After excluding 37 duplicates, 866 articles were retrieved. After screening titles and abstracts, 743 articles that met at least one of the exclusion criteria were excluded. The full texts of the remaining 123 studies were assessed, and 75 articles were excluded for the reasons listed in Figure 1. Finally, 48 eligible studies were included in our meta-analysis [59–106]. The screening process is summarized in the PRISMA 2020 flow diagram (Figure 1).

![img-0.jpeg](img-0.jpeg)

**Figure 1.** PRISMA 2020 flow diagram.

### 3.2. Study Characteristics

The basic characteristics of the included studies are summarized in Table 1. The 48 trials included in this review were published between 2004 and 2021. A total of 4308 participants in the included studies were divided into experimental (n = 2175) and control groups (n = 2133), with sample sizes ranging from 29 to 202 participants. The average age of participants ranged from 38.7 to 69.8 years. The duration of neuropathy manifestations ranged from one month to >15 years. In 21 trials, the effects of EAHM monotherapy were compared with those of the comparator [59,61,64,65,70,75,76,79,81–83,86–88,90,93,95,99–102]. All studies that used EAHM monotherapy compared its effects with those of CM, except for one trial that adopted lifestyle modification as a control [83]. In contrast, 27 trials adopted EAHM and CM combination therapy as an intervention [60,62,63,66–69,71–74,77,78,80,84,85,89,91,92,94,96–98,103–106]. In all studies that adopted EAHM and CM combination therapy as an intervention, CM was used as a control group. Twenty-one trials included the

ACP in herbal formulae [63,68,71,72,73,76,79,80,83,84,85,86,90,92,94,96,98,101,102,103,106]. Detailed information on the EAHM formulae, including ingredients, dosage, preparation type, and administration route, is provided in Supplementary Table S2. The interventions adopted as controls in the various trials were as follows: methylcobalamin (MCB, $\mathrm{n}=27$ ) [59,60,61,66,68,72,76,78,80,81,82,85,88,89,91,92,93,95,97,102,103,104], epalrestat (ERT, $\mathrm{n}=7$ ) [77,79,86,90,96,99,105], $\alpha$-lipoic acid (ALA, $\mathrm{n}=4$ ) [69,74,100,106], methylcobalamin plus epalrestat (MpE, $\mathrm{n}=2$ ) [87,98], gabapentin (GBP, $\mathrm{n}=1$ ), nimodipine (NMD, $\mathrm{n}=1$ ) [101], methylcobalamin plus $\alpha$-lipoic acid injection (MpA, $\mathrm{n}=1$ ) [73], methylcobalamin plus gabapentin ( $\mathrm{MpG}, \mathrm{n}=1$ ) [101], vitamin B1 plus vitamin B6 (V1pV6, $\mathrm{n}=1$ ) [65], methylcobalamin plus vitamin B1 plus vitamin B6 (MpV1pV6, $\mathrm{n}=1$ ) [70], adenosylcobalamin plus oryzanol plus vitamin B1 (ApOpV1, $\mathrm{n}=1$ ). [75] All included studies reported treatment duration, which ranged from 4 to 24 weeks, with 13 studies adopting a treatment period of $\geq 12$ weeks [63,64,70,77,79,81,84, $86,87,96,100,102,105]$.

# 3.3. Risk of Bias 

The methodological quality of the 48 included studies is summarized in Table 2. The risk of bias in studies was assessed using the RoB 2 tool [46]. All the included studies had a high risk of bias in one or more domains. According to the RoB 2 evaluation criteria, the "overall risk of bias" is also regarded as high if the risk of bias is assessed to be high even for one domain. The overall risk of bias for all studies included in this review was also considered high. Studies that were rated as having a "high" overall risk of bias frequently lacked information on the randomization method, and the absence of a preregistered protocol made it difficult to address concerns about selective outcome reporting. Additionally, as most studies lacked a blinded design, every variation in the intended intervention had a substantial risk of bias.

### 3.4. Pairwise Meta-Analysis

A pairwise meta-analysis was conducted for each intervention (EACP, ECCP, EAWP, and ECWP) to evaluate the effects on the response rate, motor nerve conduction velocity (MNCV), and sensory nerve conduction velocity (SNCV) compared to the control group.

### 3.4.1. Response Rate

In seven studies comparing the effect of EACP with the CM control, EACP significantly improved the response rate compared with the CM control ( 7 trials, $\mathrm{n}=516$; RR:1.3629; $95 \%$ CI:1.2259 to $1.5151 ; p<0.0001 ; \mathrm{I}^{2}=0 \%, p=0.9420$; Figure 2). In 12 trials, ECCP was significantly more effective than the CM control in terms of response rate ( 11 trials, $\mathrm{n}=1006$; RR:1.1978; 95\% CI:1.1129 to 1.2892; $p<0.0001 ; \mathrm{I}^{2}=22 \%, p=0.2341$; Figure 2). ECWP was superior to CM control in response rate ( 12 trials, $\mathrm{n}=908$; RR: 1.2863; 95\% CI: 1.1959 to 1.3835; $p<0.0001 ; \mathrm{I}^{2}=0 \%, p=0.9957$; Figure 2). Compared with the CM control, EAWP demonstrated a superior response rate ( 11 trials, $\mathrm{n}=931$; RR:1.2830; 95\% CI:1.1472 to 1.4349; $p<0.0001 ; \mathrm{I}^{2}=65.6 \%, p<0.0012$; Figure 2). One study evaluating the effect of EACP versus lifestyle modification control was excluded from the pairwise meta-analysis. In this study, EACP showed a stronger effect on the response rate than the CM control ( 1 trial, $\mathrm{n}=227$; RR:1.174; 95\% CI:1.0221 to 1.3484; $p<0.01$ ).

Table 1. Basic demographic data and intervention of studies includes in the review.

2. MSNCV $(p<0.01)$
3. PMNCV $(p<0.05)$
4. PSNCV $(p<0.01)$ | 8 w | Trial: 1
AE/diarrhea
Control: 3
AEs/abdominal pain with diarrhea |   |
2. MMNCV $(p<0.05)$
3. MSNCV $(p<0.05)$
4. UMNCV $(p<0.01)$
5. USNCV $(p<0.01)$
6. PMNCV $(p<0.05)$
7. PSNCV $(p>0.05)$
8. TMNCV $(p>0.05)$
9. TSNCV $(p<0.01)$ | 8 w | Trial: No AE Control: No AE  |
2. PMNCV $(p<0.01)$
3. PSNCV $(p<0.01)$
4. TMNCV $(p<0.01)$
5. TSNCV $(p<0.01)$ | 4 w | NR  |

Table 1. Cont.

2. Mecobalamin injection ( 0.5 mg , q.d., i.m.) | Mecobalamin injection ( 0.5 mg , q.d., i.m.) | $7.12 \pm 4.25 \mathrm{y}$ | $6.98 \pm 4.62 \mathrm{y}$ | 1. Response rate $(p<0.01)$
2. MMNCV $(p<0.01)$
3. MNSCV $(p<0.01)$
4. PMNCV $(p<0.01)$
5. PSNCV $(p<0.01)$ | 12 w | NR  |
2. PMNCV $(p<0.01)$
3. PSNCV $(p<0.01)$ | 6 w | NR  |
2. Methylcobalamine ( 0.5 mg , t.i.d.) | Methylcobalamine ( 0.5 mg , t.i.d.) | NR | NR | 1. Response rate $(p<0.05)$
2. MMNCV $(p<0.01)$
3. MSNCV $(p<0.01)$
4. PMNCV $(p<0.01)$
5. PSNCV $(p<0.01)$ | 8 w | Trial: 2 AEs/ nausea, upper abdominal discomfort Control: No AE  |
2. PMNCV $(p<0.01)$
3. PSNCV $(p>0.05)$ | 30 d | Trial: No AE Control: No AE  |

Table 1. Cont.

2. PMNCV $(p<0.01)$
3. PSNCV $(p<0.01)$
4. MMNCV $(p<0.01)$
5. MSNCV $(p<0.01)$ | 8 w | NR  |
2. MMNCV $(p<0.05)$
3. MSNCV $(p<0.05)$
4. PMNCV $(p<0.05)$
5. PSNCV $(p<0.05)$ | 3 w | NR  |
2. MMNCV $(p<0.01)$
3. MSNCV $(p<0.01)$
4. UMNCV $(p<0.01)$
5. USNCV $(p<0.01)$
6. PMNCV $(p<0.01)$
7. PSNCV $(p<0.01)$ | 24 w | Trial: No AE Control: 1 AE/skin rash  |

Table 1. Cont.

2. $\alpha$-Lipoic acid injection ( 0.3 g , q.d., i.v. drip)
3. Mecobalamin injection ( 0.5 mg , q.d., i.v. drip) | 1.
$\alpha$-Lipoic acid injection ( 0.3 g , q.d., i.v. drip)
2. Mecobalamin injection ( 0.5 mg , q.d., i.v. drip) | $3.65 \pm 1.12$ y | $3.36 \pm 1.18$ y | 1. Response rate $(p<0.05)$ | 4 w | NR  |
Modified huangqiguizhiwuwu decoction (200 mL, q.d.)
2. Methylcobalamine injection (500 mg, q.d., i.m.) | 1. Methylcobalamine injection (500 mg, q.d., i.m.) | $4.1 \pm 1.3 \mathrm{~m}$ | $3.9 \pm 1.4 \mathrm{~m}$ | 1. Response rate $(p<0.05)$ | 4 w | NR  |
2. 0.9\% Sodium chloride 200 mL + $\alpha$-Lipoic acid injection ( 450 mg , q.d., i.v. drip) | 1. 0.9\% Sodium chloride 200 mL + $\alpha$-Lipoic acid injection ( 450 mg , q.d., i.v. drip) | $2.3 \pm 2.1$ y | $2.6 \pm 1.9$ y | 1. Response rate $(p<0.05)$
2. PMNCV $(p<0.01)$
3. PSNCV $(p<0.01)$ | 4 w | Trial: No AE Control: No AE  |
2. Maixuekang capsule (3c, t.i.d.) | 1. Oryzanol (20 mg, t.i.d.)
2. Vitamin B1 (10 mg, t.i.d.)
3. Adenosylcobalamin (1 mg, t.i.d.) | $10-12$ y | $10-12$ y | 1. Response rate $(p<0.05)$ | 4 w | Trial: No AE Control: No AE  |
Modified
liutengshuilinshexian decoction (150 mL, q.d.) | 1.
Methylcobalamine tablet ( 0.5 mg , t.i.d.) | $28-73$ d | $30-73$ d | 1. Response rate $(p<0.01)$
2. MSNCV $(p<0.01)$
3. TSNCV $(p<0.01)$
4. PSNCV $(p<0.01)$ | 3 w | Trial: No AE Control: No AE  |

Table 1. Cont.

Qitengtongluo decoction (b.i.d.)
2. Epalrestat ( $50 \mathrm{mg}, 1 \mathrm{t}, \mathrm{t} . \mathrm{i} . \mathrm{d}$.) | 1. Epalrestat ( $50 \mathrm{mg}, 1 \mathrm{t}, \mathrm{t} . \mathrm{i} . \mathrm{d}$.) | $1.91 \pm 2.09 \mathrm{y}$ | $6.59 \pm 1.91 \mathrm{y}$ | 1. Response rate $(p<0.05)$
2. NCSS $(p<0.05)$
3. MSNCV $(p<0.05)$
4. TSNCV $(p<0.05)$
5. PMNCV $(p<0.05)$
6. PSNCV $(p<0.05)$ | 12 w | NR  |
2. Mecobalamin tablets ( $500 \mathrm{mg}, \mathrm{t} . \mathrm{i} . \mathrm{d}$.) | 1. Mecobalamin tablets ( $500 \mathrm{mg}, \mathrm{t} . \mathrm{i} . \mathrm{d}$.) | $2.4 \pm 1.2 \mathrm{y}$ | $2.6 \pm 1.3 \mathrm{y}$ | 1. Response rate $(p<0.05)$ | 4 w | NR  |
2. PMNCV $(p<0.05)$ | 12 w | Trial: No AE Control: No AE  |

Table 1. Cont.

m | $\begin{aligned} & 17.97 \pm 12.54 \ & \mathrm{~m} \end{aligned}$ | 1. Response rate $(p<0.01)$
2. TSNCV $(p<0.01)$
3. PSNCV $(p<0.05)$ | 8 w | Trial: No AE Control: No AE  |
2. MSNCV $(p<0.01)$
3. USNCV $(p<0.01)$
4. PMNCV $(p<0.01)$
5. TMNCV $(p<0.01)$ | 4 w | NR  |
2. MSNCV $(p<0.05)$
3. TMNCV $(p<0.05)$ | 12 w | NR  |
2. MMNCV $(p<0.01)$
3. MSNCV $(p<0.01)$
4. UMNCV $(p<0.05)$
5. USNCV $(p<0.01)$
6. TMNCV $(p<0.05)$
7. TSNCV $(p<0.01)$ | 12 w | Trial: No AE Control: 1 AE/mild dizziness  |

Table 1. Cont.

2. Epalrestat ( 50 mg , t.i.d.) | $3.87 \pm 1.5 \mathrm{y}$ | $3.69 \pm 1.3 \mathrm{y}$ | 1. TSNCV $(p<0.01)$ | 15 w | NR  |
2. MMNCV $(p>0.05)$
3. MSNCV $(p>0.05)$
4. PMNCV $(p<0.05)$
5. PSNCV $(p<0.05)$
6. TMNCV $(p<0.05)$
7. TSNCV $(p<0.05)$ | 8 w | NR  |
2. Mecobalamin tablets ( 500 mg , t.i.d.) | Mecobalamin tablets ( 500 mg , t.i.d.) | $3.6 \pm 1.8 \mathrm{y}$ | $2.4 \pm 2.1 \mathrm{y}$ | 1. Response rate $(p<0.05)$ | 4 w | Trial: 2
AEs/skin rash, gastrointestinal discomfort Control: 3 AEs/diarrhea (2), skin rash  |
2. UMNCV $(p<0.05)$
3. USNCV $(p<0.05)$
4. PMNCV $(p<0.05)$
5. PSNCV $(p<0.05)$ | 3 w | NR  |

Table 1. Cont.

2. PMNCV $(p<0.05)$ | 8 w | NR  |
2. PMNCV $(p<0.05)$
3. TSNCV $(p<0.05)$ | 8 w | Trial: 3 AEs/ Abdominal bloating with anorexia (3) Control: 2 AEs/Abdominal bloating with anorexia (2)  |

Table 1. Cont.

2. MMNCV $(p>0.05)$
3. MSNCV $(p>0.05)$
4. PMNCV $(p<0.05)$
5. PSNCV $(p<0.05)$
6. TMNCV $(p<0.05)$
7. TSNCV $(p<0.05)$ | 8 w | Trial: No AE Control: No AE  |
2. MSNCV $(p<0.05)$
3. PSNCV $(p<0.05)$ | 4 w | Trial: No AE Control: No AE  |
2. MSNCV $(p<0.05)$
3. PMNCV $(p<0.05)$
4. PSNCV $(p<0.05)$ | 24 w | Trial: 5 AEs/ nausea (2), anorexia (3) Control: 6 AEs/ nausea (2), gastric pain (2)  |
Yangyinzhuyu decoction (150 mL, b.i.d.) 2. Epalrestat tablet (50 mg, t.i.d.) | Epalrestat tablet (50 mg, t.i.d.) | $10.24 \pm 3.08 \mathrm{y}$ | $10.53 \pm 2.66 \mathrm{y}$ | 1. Response rate $(p<0.05)$ | 90 d | Trial: No AE Control: No AE  |
2. MSNCV $(p<0.05)$
3. TMNCV $(p<0.05)$
4. TSNCV $(p<0.05)$ | 4 w | NR  |

Table 1. Cont.

2. PSNCV $(p<0.05)$
3. MSNCV $(p<0.05)$
4. USNCV $(p<0.05)$ | 12 w | NR  |
2. MMNCV $(p<0.05)$
3. MSNCV $(p<0.05)$
4. PMNCV $(p<0.05)$
5. PSNCV $(p<0.05)$ | 8 w | Trial: 5
AEs/diarrhea
(1), nausea (1), constipation (2), dizziness (1)
Control: 1
AE/ nausea (1)  |

Table 1. Cont.

2. Epalrestat tablets ( 50 mg , t.i.d.) | 1. Epalrestat tablets ( 50 mg , t.i.d.) | $6.14 \pm 1.24 \mathrm{y}$ | $6.12 \pm 1.22 \mathrm{y}$ | 1. Response rate $(p<0.05)$ | 12 w | NR  |
2. Mecobalmin capsule ( 0.5 mg , t.i.d.) | 1. Mecobalamin capsule ( 0.5 mg , t.i.d.) | $1.57 \pm 0.51 \mathrm{y}$ | $1.42 \pm 0.83 \mathrm{y}$ | 1. MMNCV $(p<0.05)$
2. MSNCV $(p<0.05)$
3. PMNCV $(p<0.05)$
4. PSNCV $(p<0.05)$
5. TMNCV $(p<0.05)$
6. TSNCV $(p<0.05)$ | 4 w | NR  |
2. $\alpha$-Lipoic acid injection ( 0.6 g , q.d.) combined $0.9 \%$ Sodium chloride injection (250 mL, q.d.) | 1. $\alpha$-Lipoic acid injection ( 0.6 g , q.d.) combined $0.9 \%$ Sodium chloride injection (250 mL, q.d.) | Total
$9.33 \pm 1.25 \mathrm{y}$ | Total
$9.33 \pm 1.25 \mathrm{y}$ | 1. TSNCV $(p<0.05)$
2. PSNCV $(p<0.05)$ | 8 w | NR  |

AEs: adverse events; b.i.d.: bis in die; c: capsules; d: days; EAHM: East Asian herbal medicine; g: grams; i.v.: intravenous; m: months; mg: milligrams; MMNCV: median motor nerve conduction velocity; MSNCV: median sensory nerve conduction velocity; NR: not reported; $p$ : packs; p.o.: per os; PMNCV: peroneal motor nerve conduction velocity; PSNCV: peroneal sensory nerve conduction velocity; q.d: quaque die; SD: standard deviation; t: tablets; t.i.d.: ter in die; T1DM: type one diabetes mellitus; T2DM: type two diabetes mellitus; TMNCV: tibial motor nerve conduction velocity; TSNCV: tibial sensory nerve conduction velocity; UMNCV: ulnar motor nerve conduction velocity; USNCV: ulnar sensory nerve conduction velocity; w: weeks; WHO: World Health Organization; y: years; $\mu \mathrm{g}$ : microg.

Table 2. Methodological quality of the included studies according to the Risk of Bias 2.0 tool.


Table 2. Cont.


D1-D5: five domain criteria; D1: bias arising from the randomization process; D2: bias due to deviations from intended interventions; D3: bias due to missing outcome data; D4: bias in the measurement of the outcome; D5: bias in the selection of the reported results; H : high risk of bias; L : low risk of bias; Sc : some concerns.


Figure 2. Forest plot of the trials that compared EAHM with CM for response rate. CI: confidence interval; CM: conventional medicine; EAHM: East Asian herbal medicine.

# 3.4.2. Motor Nerve Outcomes: MMNCV, PMNCV, UMNCV, TMNCV 

The meta-analysis results indicated that ECCP significantly increased MMNCV compared to the CM control (4 trials, $\mathrm{n}=423$; MD: 5.0142; 95\% CI, 3.4682 to 6.5602; $p<0.0001$; $\mathrm{I}^{2}=74.6 \%, p=0.0081$; Supplementary Figure S1). ECWP remarkably increased MMNCV compared to the CM control ( 6 trials, $\mathrm{n}=520$; MD: 2.6593; 95\% CI: 1.3840 to 3.9345; $p<0.0001 ; \mathrm{I}^{2}=70.6 \%, p=0.0044$; Supplementary Figure S1). EAWP also increased MMNCV compared with the CM control ( 4 trials, $\mathrm{n}=422$; MD: 1.6437; 95\% CI: 0.7178 to 2.5696; $p=0.0005 ; \mathrm{I}^{2}=0 \%, p=0.8350$; Supplementary Figure S1).

Compared to CM control, EACP (2 trials, $\mathrm{n}=188$; MD: 3.2718; 95\% CI: 2.0037 to 4.5364; $p<0.0001 ; \mathrm{I}^{2}=0 \%, p=0.7087$; Supplementary Figure S2) and ECCP (4 trials, $\mathrm{n}=379$; MD: 3.3977; 95\% CI: 2.0446 to 4.7508; $p<0.0001 ; \mathrm{I}^{2}=61.2 \%, p=0.0521$; Supplementary Figure S2) increased PMNCV, and EAWP ( 6 trials, $\mathrm{n}=782$; MD: 2.2025; 95\% CI: 1.1826 to 3.2225; $p<0.0001 ; \mathrm{I}^{2}=65.4 \%, p=0.0130$; Supplementary Figure S2) and ECWP significantly increased PMNCV ( 9 trials, $\mathrm{n}=743$; MD: 3.2034; 95\% CI: 2.2196 to 4.1871; $p<0.0001$; $\mathrm{I}^{2}=81.9 \%, p<0.0001$; Supplementary Figure S2).

Compared to the CM control, EACP (1 trial, $\mathrm{n}=80$; MD: 4.5500; 95\% CI: 2.8743 to 6.2257; $p<0.0001 ; \mathrm{I}^{2}=$ not applicable; Supplementary Figure S3) and ECCP (1 trial, $\mathrm{n}=120$; MD: 3.3000; 95\% CI: 2.2787 to 4.3213; $p<0.0001 ; \mathrm{I}^{2}=$ not applicable; Supplementary Figure S3) significantly increased UMNCV. In the two studies comparing the effect of EAWP with that of the CM control, EAWP significantly increased UMNCV compared to the CM control (2 trials, $\mathrm{n}=160$; MD:2.5186; 95\% CI: 0.6061 to 4.4312; $p<0.0001 ; \mathrm{I}^{2}=61.6 \%, p=0.1064$; Supplementary Figure S3).

Compared to the CM control, both ECCP (2 trials, $\mathrm{n}=216$; MD: 2.9846; 95\% CI:1.9157 to 4.0535; $p<0.0001, \mathrm{I}^{2}=0 \% ; p=0.6993$; Supplementary Figure S4) and ECWP (4 trials, $\mathrm{n}=370$; MD: 3.7942; 95\% CI:1.8227 to 5.7658; $p=0.0002 ; \mathrm{I}^{2}=88.9 \%, p<0.0001$; Supplementary Figure S4) significantly increased TMNCV. In contrast, there was no significant difference between the effects of EAWP and the CM control on TMNCV (3 trials, $\mathrm{n}=280$; MD: 3.9412; 95\% CI: -0.0158 to 7.8982; $p=0.0509 ; \mathrm{I}^{2}=94.2 \%, p<0.0001$; Supplementary Figure S4).

### 3.4.3. Sensory Nerve Outcomes: MSNCV, PSNCV, USNCV, TSNCV

Compared to the CM control, both EACP (2 trials, $\mathrm{n}=151$; MD: 4.1171; 95\% CI: 3.1335 to 5.1007; $p<0.0001 ; \mathrm{I}^{2}=0 \%, p=0.3491$; Supplementary Figure S5) and ECCP (4 trials, $\mathrm{n}=437$; MD: 4.9293; 95\% CI: 4.1356 to 5.7229; $p<0.0001 ; \mathrm{I}^{2}=20.1 \%, p=0.2893$; Supplementary Figure S5) increased MSNCV. Compared to the CM control, EAWP ( 7 trials, $\mathrm{n}=722$; MD:2.4150; 95\% CI: 1.1971 to 3.6329; $p<0.0001 ; \mathrm{I}^{2}=86.5 \%, p<0.0001$; Supplementary Figure S5) and ECWP ( 7 trials, $\mathrm{n}=584$; MD:2.2200; 95\% CI:1.1962 to 3.2439; $p<0.0001$; $\mathrm{I}^{2}=76.5 \%, p=0.0003$; Supplementary Figure S5) significantly increased MSNCV.

Compared to the CM control, both EACP (3 trials, $\mathrm{n}=231$; MD: 2.8905; 95\% CI: 1.7993 to 3.9818; $p<0.0001 ; \mathrm{I}^{2}=5.5 \%, p=0.3471$; Supplementary Figure S6) and ECCP ( 5 trials, $\mathrm{n}=511$; MD:3.5114; 95\% CI: 2.0661 to 4.9567; $p<0.0001 ; \mathrm{I}^{2}=83 \%, p=0.0001$; Supplementary Figure S6) significantly increased PSNCV. EAWP was superior to the CM control in increasing PSNCV ( 7 trials, $\mathrm{n}=659$; MD: 3.3038; 95\% CI:2.0664 to 4.5413; $p<0.0001 ; \mathrm{I}^{2}=86 \%, p<0.0001$; Supplementary Figure S6). Compared with the CM control, ECWP was superior in increasing PNSCV ( 8 trials, $\mathrm{n}=656$; MD: 2.0450; 95\% CI: 1.0524 to 3.0375; $p<0.0001 ; \mathrm{I}^{2}=80.7 \%, p<0.0001$; Supplementary Figure S6).

Compared to the CM control, EACP (2 trials, $\mathrm{n}=147$; MD: 3.4537; 95\% CI: 1.5180 to 5.3895; $p<0.0001 ; \mathrm{I}^{2}=0 \%, p=0.3843$; Supplementary Figure S7) and ECCP (2 trials, $\mathrm{n}=216$; MD: 5.0567; 95\% CI: 4.2339 to 5.8795; $p<0.0001 ; \mathrm{I}^{2}=0 \%, p=0.9061$; Supplementary Figure S7) significantly increased USNCV. EAWP was superior in increasing USNCV compared to the CM control ( 2 trials, $\mathrm{n}=160$; MD: 1.9357; 95\% CI: 0.0310 to 3.8404; $p<0.0001 ; \mathrm{I}^{2}=68.8 \%$, $p=0.0733$; Supplementary Figure S7).

EACP (1 trial, $\mathrm{n}=84$; MD: 2.1000; 95\% CI: 0.9369 to 3.2631; $p=0.0004 ; \mathrm{I}^{2}=$ not applicable; Supplementary Figure S8), ECCP (3 trials, $\mathrm{n}=328$; MD: 4.5060; 95\% CI: 3.3591 to 5.6592; $p<0.0001 ; \mathrm{I}^{2}=61.9 \%, p=0.0724$; Supplementary Figure S8), EAWP (4 trials; MD:

3.1575; 95\% CI: 2.5478 to 3.7672; $p<0.0001 ; \mathrm{I}^{2}=0 \%, p=0.7979$; Supplementary Figure S8), and ECWP were significantly more effective than the CM control in increasing TSNCV (5 trials, $\mathrm{n}=472$; MD: $3.1596 ; 95 \%$ CI: 2.0694 to $4.2497 ; p<0.0001 ; \mathrm{I}^{2}=79.2 \%, p=0.0007$; Supplementary Figure S8).

# 3.4.4. Safety Assessment 

Of the studies included in this review, 20 reported adverse events [59,61,66,67,70,74$76,79,80,83,84,86,89,91,93,96,99,100,103]$. Of these, 12 studies reported no adverse events in either the treatment or control group [61,67,74-76,79,80,83,86,91,96,99]. The adverse events reported in eight trials were mostly digestive disorders such as anorexia, nausea, abdominal blotting, and diarrhea. Additionally, skin rash was observed in two trials and mild dizziness was reported in one trial [70,84,89]. No serious adverse events were reported in any of the included trials, and no significant differences were observed in the frequency or characteristics of adverse events between the EAHM intervention and CM control groups. The details of all adverse events reported in each trial are summarized in Table 1.

### 3.4.5. Sensitivity Analysis

More than 10 trials were included in the meta-analysis of the EAWP and CM on the response rate. Because severe heterogeneity was observed in this analysis, a sensitivity analysis of the leave-one-out method was performed, and one trial that significantly affected heterogeneity was identified [61]. However, this study did not show evident differences from other studies, and no separate effect on the overall effect size (Figure 3A,B). No additional sensitivity analysis was performed for the other pairwise meta-analysis items because there were no reports of more than 10 trials per outcome.
![img-1.jpeg](img-1.jpeg)

Figure 3. Cont.

![img-2.jpeg](img-2.jpeg)

Figure 3. (A) Forest plot of the sensitivity analysis ordered by heterogeneity for response rate. (B) Forest plot of the sensitivity analysis ordered by effect size for the response rate.

# 3.4.6. Publication Bias 

A contour-enhanced funnel plot analysis was performed to explore publication bias through the response rate, which was the outcome of most of the included studies. Since the pattern in the funnel plot displayed asymmetry, publication bias was deemed possible (Figure 4). This finding was further confirmed using Egger's test ( $\mathrm{t}=10.10, \mathrm{df}=39$, $p<0.0001$ ) and Begg's test ( $z=4.23, p<0.0001$ ).
![img-3.jpeg](img-3.jpeg)

Figure 4. Contour-enhanced funnel plot of the response rate of the trials.

3.4.7. Quality of Evidence According to Outcome Measures

In the comparison between the EAHM interventions and CM controls, the overall quality of evidence according to all outcome measures ranged from very low to moderate. The results of the GRADE assessment are presented in Table 3 and Table S3.

Table 3. Quality of evidence ratings for the response rate in pairwise meta-analysis.


CM: conventional medicine; EACP: East Asian herbal medicine monotherapy containing the Astragali RadixCinnamomi Ramulus herb-pair; EAWP: East Asian herbal medicine monotherapy without the Astragali RadixCinnamomi Ramulus herb-pair; ECCP: East Asian herbal medicine and conventional medicine combined therapy containing the Astragali Radix-Cinnamomi Ramulus herb-pair; ECWP: East Asian herbal medicine and conventional medicine combined therapy without the Astragali Radix-Cinnamomi Ramulus herb-pair. GRADE working group grades of evidence. High quality( $\oplus \oplus \oplus \oplus$ ): further research is unlikely to change our confidence in estimating this effect. Moderate quality( $\oplus \oplus \oplus \bigcirc$ ): further research is likely to have an important impact on our confidence in estimating the effect, and may change the estimate. Low quality( $\oplus \oplus \bigcirc \bigcirc$ ): further research is likely to impact our confidence in the estimate of the effect and is likely to change the estimate. Very low quality( $\oplus \bigcirc \bigcirc \bigcirc$ ): very uncertain about the estimate. a: study design with some bias in randomized or distributed blind. b: $95 \%$ confidence interval passes 0 (MD and SMD) or 1 (RR and OR), and other interventions are not satisfied. c: confidence intervals are less overlapping, or the heterogeneity is high.

# 3.5. Network Meta-Analysis 

NMA was performed for all 16 treatments, and the network relationships between the treatments for each outcome are shown in Figure 5. Detailed information is summarized in Table 4, including the number of interventions and networks for each outcome, the number of patients, whether the network is closed, and the number of direct comparisons.

Table 4. Network characteristics of each outcome included in the NMA.


Table 4. Cont.


![img-4.jpeg](img-4.jpeg)

Figure 5. Geometry of the network: (A) response rate; (B) MMNCV; (C) PMNCV; (D) TMNCV; (E) UMNCV; (F) MSNCV; (G) PSNCV; (H) TSNCV; (I) USNCV.

# 3.5.1. Response Rate 

The SUCRA plot for the response rate with MCB as a comparator is shown in Figure 6A. The highest-ranked treatments were EACP (SUCRA $=0.945$ ), EAWP (SUCRA $=0.831$ ),

ECWP (SUCRA $=0.875$ ), ECCP (SUCRA $=0.800$ ), and GBP (SUCRA $=0.72$ ). The heat map in Figure 6B shows similar trends for all comparisons. EACP showed significantly better results than lifestyle modification (OR 2.32; 95\% CrI 1.09 to 4.94), ALA (OR 3.69; 95\% CrI 1.21 to 12.09), ERT (OR 4.08; 95\% CrI 2.38 to 7.15), MpV1pV6 (OR 4.21; 95\% CrI 1.12 to 17.99), MCB (OR 4.34; 95\% CrI 2.52 to 7.83), V1pV6 (OR 5.23; 95\% CrI 1.22 to 22.02), MpA (OR 5.20; 95\% CrI 1.17 to 32.78), MpG (OR 5.39; 95\% CrI 1.17 to 31.05), NMD (OR 6.30; 95\% CrI 2.12 to 20.10), MpE (OR 17.34; 95\% CrI 2.10 to 356.64), and ApOpV1 (OR 4.28; 95\% CrI 1.09 to 71.43). These results show that the EACP is superior to all other interventions and has significantly different effects from those of most treatments.
![img-5.jpeg](img-5.jpeg)

Figure 6. (A) SUCRA plot for response rate; SUCRA: surface under the curve cumulative ranking probabilities, shows probability of ranking for each treatment illustrated by graphs. (B) League heat plot for response rate; OR is statistically significant when the $95 \%$ credible interval does not include 1 and are indicated by a double asterisk in league heat plot.

3.5.2. Motor Nerve Outcomes: MMNCV, PMNCV, UMNCV, TMNCV

The SUCRA plot for the MMNCV with MCB as a comparator is shown in Figure 7A. The highest-ranked treatments were ECCP (SUCRA = 0.872), ECWP (SUCRA = 0.783), and EAWP (SUCRA = 0.656). The heat map in Figure 7B shows similar trends for all comparisons. ECCP showed significantly better results than MCB (MD 3.67; 95% CrI 1.17 to 6.14) and NMD (MD 5.48; 95% CrI 0.70 to 10.28). ECCP was the best-ranked intervention in the network.
![img-6.jpeg](img-6.jpeg)

Figure 7. (A) SUCRA plot for MMNCV. (B) League heat plot for MMNCV. (C) SUCRA plot for PMNCV. (D) League heat plot for PMNCV. MD is statistically significant when the $95 \%$ credible interval does not include 0 and are indicated by a double asterisk in league heat plot.

The SUCRA plot for the PMNCV with MCB as a comparator is shown in Figure 7C. The highest-ranked treatments were EACP (SUCRA = 0.915), ECCP (SUCRA = 0.834), ECWP (SUCRA = 0.803), and EAWP (SUCRA = 0.675). The heat map in Figure 7D shows similar trends for all comparisons EACP showed significantly better results than ERT (MD 3.31; 95\% CrI, 1.00 to 5.59), MCB (MD 4.16; 95\% CrI 0.36 to 8.14), MCV (MD 5.27; 95\% CrI 0.07 to 10.59), ALA (MD 5.29; 95\% CrI 1.11 to 9.44), and V1pV6 (MD 7.53; 95\% CrI 2.32 to 12.84). EACP was the most effective intervention in the network.

The SUCRA plot for TMNCV with MCB as the comparator is shown in Supplementary Figure S9. The highest-ranked treatments were ECWP (SUCRA = 0.728), EAWP (SUCRA = 0.727), and ECCP (SUCRA = 0.585). The heat map in Supplementary Figure S10 shows similar trends for all comparisons. ECWP showed remarkably better results than MCB (MD 3.89; 95\% CrI 0.02 to 7.80). The ECWP was the best-ranked intervention in the network.

The SUCRA plot for UMNCV with MCB as the comparator is shown in Supplementary Figure S11. The highest-ranked treatments were EAWP (SUCRA $=0.610$ ), EACP (SUCRA $=0.601$ ), ECCP (SUCRA $=0.572$ ), and ALA (SUCRA $=0.503$ ). The heat map in Supplementary Figure S12 shows similar trends for all comparisons. The EAWP was the best-ranked intervention in the network, but the difference was not statistically significant.

# 3.5.3. Sensory Nerve Outcomes: MSNCV, PSNCV, USNCV, TSNCV 

The SUCRA plot for MSNCV with MCB as the comparator is shown in Figure 8A. The highest-ranked treatments were ECCP (SUCRA $=0.903$ ), EACP (SUCRA $=0.794$ ), EAWP (SUCRA $=0.697$ ), and ECWP (SUCRA $=0.618$ ). The heat map in Figure 8B shows similar trends for all comparisons. ECCP showed significantly better results than NMD (MD 4.79; $95 \%$ CrI 1.41 to 8.17), and NMD (MD 4.36; 95\% CrI 2.60 to 6.15). ECCP was the best-ranked intervention in the network.
![img-7.jpeg](img-7.jpeg)

Figure 8. (A) SUCRA plot for MSNCV. (B) League heat plot for MSNCV. (C) SUCRA plot for USNCV. (D) League heatplot for USNCV. MD is statistically significant when the $95 \%$ credible interval does not include 0 and are indicated by a double asterisk in league heat plot.

The SUCRA plot for PSNCV, with MCB as the comparator, is shown in Supplementary Figure S13. The highest-ranked treatments were EAWP (SUCRA $=0.915$ ), ECCP (SUCRA $=0.740$ ), EACP (SUCRA $=0.675$ ), and V1pV6 (SUCRA $=0.672$ ). The heat map in Supplementary Figure S14 shows similar trends for all comparisons. EAWP showed significantly better results than ECWP (MD 2.10; 95\% CrI 0.19 to 4.05), MCB (MD 4.05; 95\% CrI 2.46 to 5.73), ERT (MD 4.25; 95\% CrI, 2.04 to 6.43), and ALA (MD 4.38; 95\% CrI 2.20 to 6.51). The EAWP was the best-ranked intervention in the network.

The SUCRA plot for TSNCV, with MCB as the comparator, is shown in Supplementary Figure S15. The highest-ranked treatments were EAWP (SUCRA $=0.855$ ), ECCP

(SUCRA $=0.740$ ), EACP (SUCRA $=0.675$ ), MpV1pV6 (SUCRA $=0.676$ ), and V1pV6 (SUCRA $=0.671$ ). The heat map in Supplementary Figure S16 shows similar trends for all comparisons. ECWP showed significantly better results than MCB (MD 3.55; 95\% CrI 2.26 to 5.09), ALA (MD 5.16; 95\% CrI 1.25 to 9.21), and NMD (MD 5.84; 95\% CrI 1.93 to 10.00). The ECWP was the best-ranked intervention in the network.

The SUCRA plot for USNCV with MCB as the comparator is shown in Figure 8C. The highest-ranked treatments were ECCP (SUCRA $=0.785$ ), EACP (SUCRA $=0.771$ ), and EAWP (SUCRA $=0.552$ ). The heat map in Figure 8D shows similar trends for all comparisons. ECCP was the best-ranked intervention in the network but was not statistically significant.

# 3.5.4. Inconsistency Test 

Regarding the response rate, as a result of node-splitting analysis of six interventions including multiple studies, no significant heterogeneity was observed in any comparison (EACP vs. ERT, $p=0.9615$; EACP vs. MCB, $p=0.9997$; EAWP vs. ERT, $p=0.7399$; EAWP vs. MCV, $p=0.6651$; ECCP vs. ERT, $p=0.9645$; ECCP vs. MCV, $p=0.9968$; ECWP vs. ERT, $p=0.6720$; ECWP vs. MCV, $p=0.7770$ ). Additionally, for all studies related to response rate, no finding supporting heterogeneity was confirmed in the comparison of the posterior mean deviance between the consistency and inconsistency models (Figure S17). In the case of secondary outcomes, DIC was compared using a leverage plot, and no significant inconsistency model DIC values were observed for any outcome that violated the consistency assumption (Figure S18A-H).

### 3.6. Analysis of the Mechanism of the ACP on DPN through Network Pharmacology

### 3.6.1. Active Ingredients and Anti-DPN Gene Targets of the ACP

The TCMSP platform was screened using the absorption, distribution, metabolism, and excretion (ADME) criterion index of $\mathrm{OB} \geq 30 \%$ and $\mathrm{DL} \geq 0.18$ to identify the active components in the ACP. A total of 27 active ingredients derived from the ACP were identified. Of these, 20 compounds occurred in Astragali Radix, and seven occurred in Cinnamomi Ramulus (Table 5). The DrugBank database contains information on 364 component-target relationships (Supplementary Table S4), and the GeneCards database contains information on 1157 human target genes associated with DPN (Supplementary Table S5). After intersection mapping, 57 consensus genes were identified as potential therapeutic targets of the ACP against DPN (Figure 9).
![img-8.jpeg](img-8.jpeg)

Figure 9. Venn diagram of targets of the ACP against DPN.

Table 5. Detailed information on the active compounds in the ACP.


Table 5. Cont.


Table 5. Cont.


Mol ID: molecule ID; Mol name: molecule name; OB: oral bioavailability; DL: drug-likeness.

# 3.6.2. Network Analysis of the ACP and DPN Targets 

The ACP component-DPN target network was mapped using Cytoscape software version 3.9.1. As shown in Figure 10, the network contained 78 nodes and 148 edges. The degree of a single target in the ACP-DPN network indicates the number of linked nodes. Network tools were analyzed to examine the network, and the degree of the active component was rated. Table 6 lists the top ten active ingredients according to degree, betweenness, and closeness centralities.

Table 6. The top ten active compounds of the ACP.


AR: Astragali Radix; CR: Cinnamomi Ramulus.

![img-9.jpeg](img-9.jpeg)

Figure 10. ACP-DPN network graph. Red nodes are active components of Astragali Radix; orange nodes are active components of Cinnamomi Ramulus; Blue nodes are potential multiple targets of ACP for the treatment of DPN.

# 3.6.3. PPI Network Construction 

Using the STRING 11.5 platform, we imported the common targets and constructed a PPI network, as shown in Figure 11A. One target (MT-ND6) was excluded from the PPI network as it did not interact with any other target. The PPI network of intersecting targets contained 56 nodes and 612 edges. Nodes that satisfied the average value of degree centrality (21.47) were retrieved through an additional examination of topological attributes, and 30 targets were eliminated during screening. Figure 11B shows the PPI network of the hub targets. Table 7 lists the top 27 hub targets based on their degree of centrality. On the other hand, every PPI pair analyzed on the STRING platform is assigned a score. This score does not indicate the strength or specificity of the PPI, but rather its reliability based on the available evidence. Calculated on a scale of 0 to 1 , the closer the score is to 1 , the more likely it is that the PPI is true. The interaction scores for all PPI pairs utilized in the study are presented in Table S6.

Table 7. The top 27 hub targets.


Table 7. Cont.

Centrality | Closeness
Centrality  |

![img-10.jpeg](img-10.jpeg)

Figure 11. (A) ACP-DPN PPI network. (B) Top 27 hub targets ranked by degree centrality.

# 3.6.4. Gene Ontology and KEGG Pathway Enrichment Analysis 

The results of the GO and KEGG analyses of the top 27 hub targets are shown in Figure 12. A total of 510 biological processes (BP) were identified, including the cellular response to chemical stress, positive regulation of cell migration, response to lipopolysaccharide, positive regulation of protein phosphorylation, regulation of inflammatory response,

regulation of smooth muscle cell proliferation, the mitogen-activated protein kinase signaling (MAPK) cascade, and regulation of epithelial cell migration (Figure 12A). A total of 93 molecular functions were identified including cytokine activity, heme binding, MAP kinase activity, chromatin binding, metalloendopeptidase activity, fibronectin binding, integrin binding, carboxylic acid binding, kinase activator activity, and protease binding (Figure 12B). A total of 33 cellular components were identified, including the membrane raft, vesicle lumen, endocytic vesicle, early endosome, external side of the plasma membrane, transcription regulator complex, extracellular matrix, and endoplasmic reticulum lumen (Figure 12C). A total of 135 pathways were identified using KEGG pathway analysis (Figure 12D). The results suggested that the mechanisms of the ACP were mainly linked to fluid shear stress, atherosclerosis, and the interleukin-17 (IL-17), MAPK, and vascular endothelial growth factor (VEGF) signaling pathways (Table S7).
![img-11.jpeg](img-11.jpeg)

Figure 12. (A-C) GO enrichment analyses of DPN hub targets. (D) KEGG analysis of the DPN hub targets.

# 4. Discussion 

### 4.1. Summary of the Findings

In our study, EAHM interventions were classified into four categories depending on the inclusion of the ACP and combination therapy with CM, and the comprehensive efficacy of EAHM interventions against DPN was compared with that of the CM control. EAHM showed considerably higher efficacy against DPN than the CM control, as determined by the response rate, SNCV, and MNCV indices, regardless of the mode of usage. The EAHM formula containing ACP was ranked highest in NMA for each treatment in terms of response rate, MMNCV, PMNCV, MSNCV, and USNCV. As a result, the ACP appears to be a candidate combination that can significantly influence the therapeutic response and nerve damage recovery in DPN. Based on network pharmacology analysis, the aforementioned study predicted that 10 compounds, including quercetin, kaempferol, isorhamnetin, formononetin, and beta-sitosterol, would act on 27 targets.

### 4.2. Strengths and Limitations

This study has the following strengths: First, there are countless meta-analyses related to EAHM; however, to the best of our knowledge, this is the first network meta-analysis to investigate the synergistic effect of an herb-pair. The analysis performed in this study is expected to be useful in identifying the synergistic effects of EAHM through continuous improvements and developments in the future. Second, the mechanism of EAHM was reviewed at a deeper level using network pharmacology analysis in conjunction with NMA in clinical studies. Because the mechanism of action of EAHM is complex, detailed pharmacological information is often not discussed in clinical studies. Therefore, this study is valuable because it supports the efficacy hypothesis for DPN to be tested in EAHM clinical research. Third, the overall direction of this study was consistent with the proposal for determining candidate combinations for drug discovery. Meta-analysis is one of the most important clinical research methodologies; however, in the case of EAHM, personalized prescription is advantageous, and it is difficult to draw a firm conclusion about which material is valid owing to the heterogeneity between different EAHM formulae. The authors suggest that meta-analysis may be a useful tool for developing new drug candidates by scientifically validating the tacit knowledge associated with complex EAHM combinations.

Due to the following limitations, caution should be exercised when interpreting the results of this study: First, although the EAHM formula containing the ACP at various NMA endpoints occupied the highest rank, the results were not consistent in terms of all indicators. This is mainly because the interactions with herbs other than the ACP also affect the efficacy, and few studies have performed a stable-effect comparison between multiple treatments. However, the design of this study was based on the premise that the ACP is a combination with appropriate compatibility, and its synergistic effect is stronger than that for other herbal combinations. To overcome these limitations, additional clinical trials are required to conduct updated NMA. Second, the quality of the studies included in the NMA was generally low, and no RCTs employed a double-blind design. This is another limitation that can affect the results. As a follow-up to this review, the validation of the effect of the ACP may be firmly established with new clinical trials with an improved design in the future. Third, in this study, the mechanism was analyzed using network pharmacology. However, as the compounds and targets of ACP have not yet been fully identified, databasebased mechanism analysis based on data from previous studies revealed only predictive and not definitive mechanisms. Therefore, conclusions regarding the synergistic effects of the ACP and DPN can only be drawn through experimental studies. Prior to experimental testing, this study should be accepted to provide guidance.

### 4.3. Implications for Clinical Decision-Making

The significant difference between the effects of EAHM and the CM control, which was supported by the PMA data, is important because CM was used as a comparative treatment in most studies. Moreover, these results are encouraging because they are

consistent with previous studies of similar design that investigated the effect of EAHM on DPN [31,32,33,38,107]. However, such a meta-analysis, which includes several types of EAHM formulae, has many limitations in its direct application to clinical decisionmaking, owing to strong heterogeneity due to differences in intervention composition and dose. Nevertheless, the consistent efficacy demonstrated by the findings of PMA in several previous studies and this review reinforces the idea that EAHM is a highly valuable candidate for drug discovery, at least for DPN treatment.

The EAHM formula containing the ACP occupied the highest rank among the multiple indicators included in the NMA target. Clinical evidence has established that EAHM formulae containing the ACP are useful for DPN, and the related mechanisms have been extensively explored [38,41,42,108]. Considering this and the fact that the ACP has long been used in combination with several EAHM prescriptions, the compatibility between the two components of the ACP is supported academically and historically. Moreover, both Astragali Radix and Cinnamomi Ramulus that make up the ACP have been shown to separately exert a wide range of pharmacological effects on systemic diseases, including the nervous, immune, endocrine, and cardiovascular systems, and are widely used medicinal plants [109,110,111,112]. Overall, EAHM formulae containing the ACP are considered superior for the treatment of DPN, and the development of a new drug for DPN using ACP or an EAHM combination containing the ACP as a candidate component seems valuable.

# 4.4. Implications for Drug Discovery 

It is important to understand the herb-pair theory of EAHM outlined in the introduction to accurately predict the synergistic effects of herbal medicine combinations and apply it for drug discovery [22,24,25,26,113,114,115]. EAHM is often used as a polyherbal mixture following established academic principles. The synergistic effects of these mixtures are expected to improve their efficacy while lowering the potential toxicity of the individual herbs. This is made feasible by the basic prescription premise of EAHM, which is "Gun-Shin-Jwa-Sa" (King-Retainer-Officer-Messenger in English) [27]. The places of "Gun" and "Shin" are given to herbs that have the strongest influence and in greater doses. In contrast, relatively smaller doses of herbs are considered at "Jwa" and "Sa" to reduce adverse effects or boost synergistic effects. Thus, a suitable herbal combination can exhibit amplified efficacy compared to a single herb [30,116,117,118,119,120]. To establish these synergistic effects, an appropriate combination of EAHMs must be selected for drug development. Herb-pair theory is the most fundamental theory for compatibility [28,121,122]. This is extremely helpful as a research hypothesis for evaluating synergistic effects because it facilitates the development of an EAHM formula through the combination of two or three herbs.

Therefore, in recent years, an increasing number of studies have used various methods to identify the synergistic mechanisms of potentially useful herb-pairs [123,124,125]. A previous study using a combination of network pharmacology and bioinformatics reported that Astragali Radix, which was also used in this study, could form a promising herbal pair for the treatment of DPN with Notoginseng Radix [126,127]. We combined network meta-analysis and network pharmacology analyses with reference to the latest studies to investigate the clinical effects and synergistic mechanisms of the ACP simultaneously. We found that DPN treatment using an EAHM involving the ACP is closely related to the IL-17 signaling pathway. The IL-17 cytokine family is primarily associated with acute and chronic inflammation. Accordingly, this pathway is considered a therapeutic target for chronic inflammatory diseases in humans, and blocking this pathway prevents the onset of type 1 diabetes in rodent models [128,129]. In addition, a recent cross-sectional study confirmed that the development of peripheral neuropathy in patients with type 2 diabetes was independently and positively associated with elevated IL-17 levels. This study suggests that IL-17 may have greater diagnostic value for DPN than other inflammatory cytokines [130]. The ACP is also involved in the regulation of the MAPK pathway. This is important because the MAPK cascade is a major factor in DPN pathogenesis. Recent studies have shown that nerve growth factors induced by high blood glucose levels promote an

increase in MAPK levels, which contributes to an increase in the levels of inflammatory mediators that cause DPN, such as tumor necrosis factor (TNF) and IL-1. Increased levels of MAPKs are also involved in the pathogenesis of DPN via inflammatory cytokines via the activation of c-Jun/JNK. Therefore, the inhibitory effect of the ACP on this mechanism is significant because activation of MAPKs contributes to the overall progression of DPN [131]. Additionally, neuroinflammation and neurodegeneration are important pathologies in diabetic complications including DPN. Hyperglycemia-induced reactive metabolites damage the blood vessels and promote capillary thickening and endothelial proliferation. The resulting decreased oxygen supply and increased reactive oxygen species (ROS) synthesis further damage the neurons and induce vascular endothelial growth factor (VEGF) expression. Therefore, VEGF has been extensively studied as a primary singlemolecule target for the treatment of DPN, and our study predicted that the ACP could exert its therapeutic effect on DPN based on its action on this target [132]. Collectively, these potential predictive mechanisms and the fact that neuroinflammation is one of the major pathologies of DPN suggest that the ACP's mechanism of action is likely related to the inhibition of inflammation-induced neuronal degeneration. [10]. In this regard, the ACP may have neuroprotective effects similar to those of berberine, which served as a target in a rat model of diabetic neuropathy, resulting in better neuritin expression and micropathology [133,134].

The results of our study showed that ten active components, according to degree centrality, ensured the main effects of the ACP. Among these compounds, quercetin, kaempferol, isorhamnetin, formononetin, and beta-sitosterol are thought to exert synergistic effects [135,136]. Quercetin is a promising candidate compound for a multitargeted approach to the complications of type 2 diabetes and has been reported to reduce oxidative stress, protect beta cells, and stimulate glucose uptake in muscle cells via the AMPK pathway [137]. In addition, it prevented diabetic complications by alleviating oxidative stress-induced apoptosis in a rat model of type 1 diabetes [138]. Kaempferol inhibits hyperglycemia-induced RhoA activation and diabetic kidney disease by reducing oxidative stress and proinflammatory cytokine levels [139]. Isorhamnetin is known for its various physiological activities, including neuroprotective, anti-inflammatory, antioxidative, and immunomodulatory effects [140,141]. DPN-related mechanisms have also been reported to prevent hyperglycemia by promoting glucose uptake by skeletal muscle cells and inhibiting insulin resistance [142,143]. Formononetin suppresses neuronal damage by controlling hyperglycemia in a rat model of diabetic neuropathy, improves nerve conduction velocity, and elicits synergistic effects by reducing thermal hyperalgesia and mechanical allodynia [144]. Finally, beta-sitosterol has been reported to have neuroprotective and antinociceptive effects in an animal model of diabetic neuropathic pain, based on insulin secretion promotion, alpha-glucosidase inhibition, blood sugar suppression, and antioxidant action [145]. In summary, several physiologically active ingredients present in the ACP may have synergistic effects on the prevention of nerve damage, repair of damaged nerves, and inhibition of DPN progression through an antidiabetic action via multiple pathways. This finding is consistent with the results of NMA in clinical trials. Therefore, the ACP is a promising candidate combination and its synergistic effects must be verified through subsequent experimental studies.

# 5. Conclusions 

EAHM may promote therapeutic efficacy in the management of DPN; when combined with CM, it can treat DPN significantly more effectively than CM alone. EAHM formulae containing the ACP may be more suitable than other EAHM formulae for improving NCV and the treatment response rate to DPN therapy, as determined by a network meta-analysis. The ACP has also been shown to cure DPN synergistically via multiple pathways and may work primarily through the IL-17 and MAPK signaling pathways to alter the pathophysiology of chronic diabetes mellitus in peripheral nerves. These observations suggest that

ACP could be used to treat pain, paresthesia, neuroinflammation, and neurodegeneration in patients with DPN.

The key ingredients in the ACP, including quercetin, kaempferol, isorhamnetin, formononetin, and beta-sitosterol, might have synergistic effects in neuroprotection, antiinflammation, antioxidation, immunomodulation, and antinociception. These results suggest that ACP is a useful candidate for the treatment of DPN and should be studied further. However, the findings of this study should be verified through clinical trials and experimental studies. Despite these limitations, this study is valuable for proposing research hypotheses for candidate natural therapeutics based on herbal pairs and their synergistic effects.

Finally, the above study exploring the synergistic effects of herbal medicine combinations is expected to verify the efficacy of licensed herbal medicines and classical EAHM prescriptions consisting of multiple herbs based on a traditional holistic perspective. Currently, the standardization of herbal formulations mainly depends on the content of a single indicator component; however, this information is insufficient to support efficacy. Therefore, an advanced test method to clarify the multilayered indications of herbal medicines is essential. To clarify the indications for complex herbal medicine prescriptions beyond the mechanisms and effects of individual herbal medicines, it is necessary to continuously and multidimensionally verify the synergistic effects explored in this study.

Supplementary Materials: The following supporting information can be downloaded at: https: //www.mdpi.com/article/10.3390/pharmaceutics15051361/s1, Supplementary Table S1. Search strategies; Supplementary Table S2. EAHM ingredients used in clinical trials included in this review; Supplementary Table S3. Quality of evidence ratings for secondary outcomes in pairwise metaanalysis; Supplementary Table S4. The protein targets from the candidate bioactive components in ACP; Supplementary Table S5. The detailed information of potential DPN targets from GeneCard database; Supplementary Table S6. Protein-protein interaction score; Supplementary Table S7. KEGG enrichment analysis; Supplementary Figure S1. Forest plot of the trials that compared EAHM with CM for MMNCV; Supplementary Figure S2. Forest plot of the trials that compared EAHM with CM for PMNCV; Supplementary Figure S3. Forest plot of the trials that compared EAHM with CM for UMNCV; Supplementary Figure S4. Forest plot of the trials that compared EAHM with CM for TMNCV; Supplementary Figure S5. Forest plot of the trials that compared EAHM with CM for MSNCV; Supplementary Figure S6. Forest plot of the trials that compared EAHM with CM for PSNCV; Supplementary Figure S7. Forest plot of the trials that compared EAHM with CM for USNCV; Supplementary Figure S8. Forest plot of the trials that compared EAHM with CM for TSNCV; Supplementary Figure S9. SUCRA plot for TMNCV; Supplementary Figure S10. League heat plot for TMNCV; Supplementary Figure S11. SUCRA plot for UMNCV; Supplementary Figure S12. League heat plot for UMNCV; Supplementary Figure S13. SUCRA plot for PSNCV; Supplementary Figure S14. League heat plot for PSNCV; Supplementary Figure S15. SUCRA plot for TSNCV; Supplementary Figure S16. League heat plot for TSNCV; Supplementary Figure S17. Posterior mean deviance compare plot for response rate; Supplementary Figure S18A. Leverage plots and fit statistics for MMNCV; (B) Leverage plots and fit statistics for PMNCV; (C) Leverage plots and fit statistics for TMNCV; (D) Leverage plots and fit statistics for UMNCV; (E) Leverage plots and fit statistics for MSNCV; (F) Leverage plots and fit statistics for PSNCV; (G) Leverage plots and fit statistics for TSNCV; (H) Leverage plots and fit statistics for USNCV.

Author Contributions: H.-G.J.: conceptualization, methodology, software, validation, formal analysis, investigation, resources, data curation, writing-original draft preparation, writing-review and editing, visualization, and project administration; E.B.: conceptualization, methodology, validation, writing-original draft preparation, and writing-review and editing; D.L.: conceptualization, methodology, validation, formal analysis, investigation, writing-review and editing, supervision, project administration, and funding acquisition. All authors have read and agreed to the published version of the manuscript.

Funding: This research was supported by a grant (21173MFDS561) from the Ministry of Food and Drug Safety (2022).
Institutional Review Board Statement: Not applicable.

Informed Consent Statement: Not applicable.
Data Availability Statement: The data in this study were all utilized from public databases and published studies and had unrestricted access.

Acknowledgments: The methodology used in this study was created to carry out research tasks that the Ministry of Food and Drug Safety had requested. The methodological progress and practical application discussed in this research will be made in order to complete the aforementioned duties successfully.

Conflicts of Interest: The authors declare no conflict of interest. The funders had no role in the design of the study; in the collection, analyses, or interpretation of data; in the writing of the manuscript; or in the decision to publish the results.
