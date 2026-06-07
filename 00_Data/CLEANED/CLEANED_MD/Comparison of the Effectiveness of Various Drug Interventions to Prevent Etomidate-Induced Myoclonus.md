# Comparison of the Effectiveness of Various Drug Interventions to Prevent Etomidate-Induced Myoclonus: A Bayesian Network Meta-Analysis 

Kang-Da Zhang ${ }^{1}$, Lin-Yu Wang ${ }^{1}$, Dan-Xu Zhang ${ }^{1}$, Zhi-Hua Zhang ${ }^{1}$ and Huan-Liang Wang ${ }^{1,2 *}$<br>OPEN ACCESS

Edited by:
Ata Murat Kaynar, University of Pittsburgh, United States

Reviewed by:
Ali Solhpour, University of Florida, United States Cheng-Mao Zhou, First Affiliated Hospital of Zhengzhou University, China Behzad Nazemroaya, Isfahan University of Medical Sciences, Iran
*Correspondence: Huan-Liang Wang wanghuanliang@email.sdu.edu.cn

Specialty section:
This article was submitted to Intensive Care Medicine and Anesthesiology, a section of the journal Frontiers in Medicine

Received: 21 October 2021
Accepted: 30 March 2022
Published: 26 April 2022
Citation:
Zhang K-D, Wang L-Y, Zhang D-X, Zhang Z-H and Wang H-L (2022) Comparison of the Effectiveness of Various Drug Interventions to Prevent Etomidate-Induced Myoclonus: A Bayesian Network Meta-Analysis. Front. Med. 9:799156. doi: 10.3389/fmed.2022.799156

Background: Myoclonic movement is a very common but undesirable phenomenon during the induction of general anesthesia using etomidate. Such movement may cause unnecessary problems. Currently, there is an increasing number of drugs for preventing etomidate-induced myoclonus (EM). However, direct comparisons of various drugs are lacking, and this interferes with clinical decision-making. Our network metaanalysis (NMA) aimed to compare the efficacy of different drugs for the prevention of moderate-to-severe general myoclonus.

Methods: Using several biomedical databases, randomized controlled trials (RCTs) published in English from inception to August 22, 2021 were searched. Among the various interventions, we selected nine types of intervention drugs (dexmedetomidine, etomidate, lidocaine, NMDA receptor antagonist, $\kappa$ opioid receptor agonist, $\mu$ opioid receptor agonist, muscle relaxant, gabapentin, and midazolam) for comparison, according to the number of studies. Bayesian NMA was performed using STATA16 and R softwares. The relative risk of EM was assessed using risk ratios (RRs) and the corresponding $95 \%$ confidence intervals (CI).

Results: A total of 31 RCTs (3209 patients) were included. NMA results showed that, compared with a placebo, etomidate (RR 4.0, 95\%CI 2.1-7.8), $\kappa$ opioid receptor agonist (RR 2.9, 95\%Cl 1.9-4.6), $\mu$ opioid receptor agonist (RR 3.1, 95\%Cl 2.3-4.3), NMDA receptor antagonist (RR 1.7, 95\%Cl 1.0-2.8), dexmedetomidine (RR 2.4, 95\%Cl 1.5-3.9), lidocaine (RR 2.1, 95\%Cl 1.2-3.9), and midazolam (RR 2.2, $95 \%$ Cl 1.5-3.2) can significantly reduce the risk of EM. In contrast, the effects of muscle relaxants (RR 2.1, 95\%Cl 0.81-5.3) and gabapentin (RR 2.8, 95\%Cl 0.92-9.3) were inconclusive. Further subgroup analyses showed that preoperative low-dose etomidate, $\mu$-opioid receptor agonist, and $\kappa$-opioid receptor agonist were significantly better than other interventions in the prevention of moderate to severe EM.

Conclusion: Preoperative use of small doses of etomidate or opioids may be the most effective way to avoid EM, especially moderate and severe EM, which makes anesthesia induction safer, more stable, and aligns better with the requirements of comfortable medicine.

Systematic Review Registration: [https://www.crd.york.ac.uk/prospero/], identifier [CRD4202127706].

Keywords: etomidate, myoclonus, anesthesia induction, network meta-analysis, Bayesian framework

## INTRODUCTION

Etomidate, a compound containing an imidazole carboxyl group, was introduced to clinical practice in the 1970s. In addition to its strong anesthetic efficacy, rapid onset, and rapid recovery, etomidate has the advantages of stable cardiovascular profiles and minimal respiratory depression, making it an ideal substitute for propofol and the first-line anesthetic for many elderly people and patients with impaired hemodynamics and cardiac reserve (1, 2).

However, etomidate often induces spontaneous movements, especially myoclonic activities. Generalized convulsive seizures may occur in severe cases, with an incidence of $50 \%-$ $80 \%$ (3). Myoclonus is also related to epileptiform activities. Therefore, epileptic activities may be enhanced in the EEG of some patients after etomidate injection (4). According to the classical definition, myoclonus is a sudden, brief, lightninglike muscle jerk arising from an abnormality of the nervous system, excluding short or prolonged movements caused by the muscle itself such as fasciculation, spasms, or cramps (5). Myoclonus can damage muscle fibers and cause serum potassium to rise. Transient mild myoclonus may not be pathologically significant in most patients, but severe myoclonus can have unintended consequences, especially in patients with a full stomach, malignant hypertension, open eye injury, aneurysms, and hyperkalemia $(6,7)$.

In the past few decades, many drugs have been used in clinical practice for the prevention and treatment of EM, including opioids, benzodiazepines, dexmedetomidine, ketamine, lidocaine, magnesium sulfate, muscle relaxants, antiepileptics, and preoperative low-dose etomidate. The variety of drugs available is appreciated by many anesthesiologists. Some traditional pairwise meta-analyses have evaluated the efficacy of two drugs or a drug versus a placebo to guide agent selection (8-15). However, when faced with a wide range of interventions, most anesthesiologists still struggle to choose the best option, and instead, use the drug empirically. Furthermore, traditional metaanalyses cannot clearly rank different classes of interventions based on their efficacy outcomes.

Owing to the limitations of standard pairwise meta-analyses, we adopted a network meta-analysis (NMA) to determine the most effective approach for preventing myoclonus. NMA integrates direct and indirect evidence and enables the evaluation of multiple treatments in a single analysis (16). In this study, we determined the effectiveness of all interventions, as well as their ranking probabilities in overall and subgroup networks by summarizing the available evidence. The results of this study will provide evidence for the best preventive measure of moderate to severe myoclonus, when using etomidate.

## METHODS

## Protocol and Registration

This systematic review followed the recommendations of the Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) guidelines (17), and was registered under the PROSPERO International prospective register of systematic reviews on October 6, 2021 (registration number CRD42021277063).

## Search Strategy

The search strategy was first designed jointly by the two authors, and then, the search was conducted independently. PubMed, Embase, the Cochrane Central Register of Controlled Trials (CENTRAL), and NIH ClinicalTrials.gov were searched to find relevant articles from inception to August 2021 within the restriction limit of "randomized controlled trial" and "Englishlanguage." Some of the English literature from the CNKI database was supplemented. Using the combination of MeSH medical subject words and item words, the search terms were combined for literature retrieval through the logical characters "OR" and "AND." Relevant search strategies are provided in the Supplementary Material.

All citations were downloaded and imported into EndNote for management (18). First, duplicates were excluded from the analysis. The titles and abstracts were then reviewed, and studies that did not meet the inclusion criteria were excluded. Finally, the full text of any potential study was analyzed and further screened according to the exclusion criteria. The above tasks were also performed by two authors independently. The reasons for article exclusion were recorded for the preparation of the literature screening flowchart.

## Inclusion and Exclusion Criteria

Inclusion criteria were formulated according to the PICOS framework (19), as follows: (1) adult patients who are purposed to surgical or invasive intervention under etomidate; (2) interventions including opioids, lidocaine, ketamine, dexmedetomidine, etomidate, muscle relaxant, magnesium sulfate, gabapentin, and midazolam; and (3) the control group could be a placebo or a comparison between the above drugs;

(4) the outcome was the incidence of myoclonus induced by etomidate, and the degree of myoclonus was divided into none, mild (mild myoclonus in the face and/or upper limbs and/or distal lower limbs), moderate (some movement in the face and/or limbs), and severe (movement in limbs and trunk); and (5) the study must be a randomized controlled trial and published in English.

Studies were excluded if they included the following characteristics: (1) patients who had neuropsychological disease; adrenal cortex dysfunction; heart failure; renal, pulmonary, hepatic, or endocrine diseases; history of allergic reaction to etomidate and other study drugs; (2) patients who had taken sedative and analgesic drugs on the day of operation; and (3) lack of necessary outcomes to be extracted, for example, incomplete data.

### Data Extraction and Methodological Quality Assessment

We created a unified information extraction table in advance. Two authors independently screened the information, and any discrepancies were resolved through discussion. The following information was extracted: author's name, publication year, age distribution, type of surgery, American Society of Anesthesiologists (ASA) physical status, induction dose of etomidate, treatment, sample size, and outcome. The primary outcomes were the incidence of EM and moderate-to-severe EM.

For randomized controlled trials, two reviewers independently applied the Cochrane Review Manager (Version 5.4) to assess the risk of bias (ROB) in randomized trials (20). The Cochrane Collaboration's bias risk assessment tools are well-structured and mainly included random sequence generation, allocation concealment, blinding of participants and personnel, blinding of outcome assessment, incomplete outcome data, selective reporting, and other biases. Each trial was independently performed by two reviewers and classified as low-, unclear-, or high-risk. The Grades of Recommendation, Assessment, Development, and Evaluation (GRADE) Working Group recommended a four-step evidence quality grading for network meta-analyses (21). The certainty of the evidence was appraised as high, moderate, low, or very low.

### Statistical Analysis

We first constructed a network evidence plot using Stata16.0, and conducted a traditional pairwise direct comparison meta-analysis. The network plot clearly showed whether there was a direct comparison, and whether the effect between interventions was the result of direct comparison, indirect comparison, or a combination of the two. Heterogeneity was assessed between studies using the Q test and I² statistic (22). If the P value of Cochran's Q test statistic was less than 0.05, or the I² statistic was greater than 50%, large heterogeneity between studies was determined, and the random-effects model was preferred. A pairwise meta-analysis was performed using the random-effects model. For binary outcomes, we reported the risk ratios (RR) and corresponding 95% confidence intervals (CI). If the 95%CI did not include 1, the difference between the two comparisons was considered statistically significant. A comparison-adjusted funnel plot was used to determine the possibility of a publication bias.

Owing to the existence of closed rings in the network evidence graph, we used a Bayesian network meta-analysis to compare the differences between different interventions (23). The “gemtc” package and the “rjags” package of R software that invoke the JAGS software for NMA based on a Bayesian generalized linear model were used (24, 25). For each outcome, the fixed-effects model and random-effects model were used for evaluation. The fitting degree of the model was determined by the deviance information criterion (DIC), and a model with less DIC was generally selected (26). Four Markov chains were used to set the initial values. The iterations were set to 70000, and the initial 30000 iterations, with a thinning factor of 10. Furthermore, the convergence of the model was diagnosed using a trace plot, density plot, and Brooks-Gelman-Rubin diagnosis plot (25). Finally, we calculated the RR and corresponding 95%CI, and the surface under the cumulative ranking (SUCRA) probabilities were used to rank the efficacy of various interventions (27). The value of the SUCRA is between 0 and 1 (0 ≤ SUCRA ≤ 1). When the SUCRA was 1, the intervention was effective, whereas when the SUCRA was 0, the intervention was ineffective. Subgroup analysis was performed according to EM severity (mild, moderate, and severe). Only 29 of the 31 RCTs included had myoclonus classification; therefore, a subgroup analysis was performed.

Song et al. pointed out that indirect comparison and NMA often involved three basic assumptions: homogeneity, similarity, and consistency hypothesis (28). In this study, we used the “node-splitting technique” to evaluate network consistency (29). A P value > 0.05 indicated consistency, and as such, we combined the direct and indirect estimates in the comparison of mixed treatment.

### RESULTS

### Search Results

The literature retrieval results and screening process are shown in Figure 1. A total of 251 studies were initially retrieved. Of these, 89 duplicate studies were removed using the EndNote software. A total of 108 studies were excluded after reading the titles and abstracts. Based on the full-text reviews, 24 studies were further excluded for various reasons: 15 did not meet the inclusion criteria or had incomplete information, and the full text of 6 records was not available. Finally, 31 RCTs (3209 patients) were included in this study.

### Characteristics of Included Studies

An overview of the selected studies is shown in Table 1. Most patients were scheduled for elective surgery under general anesthesia, with ASA physical status ranging from I to IV. During the induction of general anesthesia, the injection dosage of etomidate was 0.2--0.3 mg/kg, which is a commonly used

http://mcmc-jags.sourceforge.net/

![img-0.jpeg](img-0.jpeg)

induction dose in clinical practice. While there was a wide variety of drugs studied, for drugs with similar pharmacological effects, we categorized them as a group for analysis. Oxycodone, fentanyl, sufentanil, and remifentanil are all μ opioid agonists (μ-R agonists). Butorphanol, dezocine, and nalbuphine are κ opioid agonists predominate (κ-R agonists), and magnesium sulfate and ketamine are N-methyl-D-aspartic acid receptor antagonists (NMDA-R antagonists). The sample size of the 31 studies ranged from 45 to 284.

### Pairwise Meta—Analysis and Network Meta-Analysis Results

The network relationship between different treatment regimens and placebo is shown in **Figure 2**. In our NMA, there were 26 two-arm studies, 4 three-arm studies, and 1 four-arm study, and a comparison between 10 interventions, including placebo, was performed. μ-R agonists were most frequently included for comparisons, followed by midazolam, and NMDAR antagonists. Regarding heterogeneity, we compared the fixed-effects model with the random-effects model, and the results showed that the latter had smaller DIC and I² values. Therefore, based on the heterogeneity analysis and DIC comparison, all data were analyzed using a consistent random-effects model. After 70000 iterations, the fluctuation of the four Markov chains was small, the trace plot and density plot tended to be stable, and the PSRF was close to 1, indicating satisfactory convergence of the model and relatively stable results (**Supplementary Figure 1**).

The results of the pairwise meta-analysis are shown in **Figure 3**. The results produced by NMA are illustrated in **Figure 4A**. In comparison with placebo, overall myoclonus incidence was significantly reduced after low-dose dexmedetomidine (RR 2.4, 95%CI 1.5–3.9), etomidate (RR 4.0, 95%CI 2.1–7.8), NMDA-R antagonist (RR 1.7, 95%CI 1.0–2.8), lidocaine (RR 2.1, 95%CI 1.2–3.9), midazolam (RR 2.2, 95%CI 1.5–3.2), μ-R agonist (RR 3.1, 95%CI 2.3–4.3), and κ-R agonist (RR 2.9, 95%CI 1.9–4.6) before induction of anesthesia. Gabapentin (RR 2.8, 95%CI 0.92–9.3) and muscle relaxants (RR 2.1, 95%CI 0.81–5.3) did not significantly reduce the overall incidence of EM. Additionally, etomidate (RR 2.35, 95%CI 1.11–5.06) was significantly better than the NMDAR antagonist, NMDAR antagonist (RR 0.56, 95%CI 0.31–0.96) was significantly worse than the μ-R agonist, and the differences among other drugs were not statistically significant. To further understand the results, the nine interventions were ranked by the SUCRA value. The higher the SUCRA value, the lower the incidence of myoclonus after etomidate induction. The corresponding SUCRA values are shown in **Figure 4B**. The results suggest that preoperative administration of low doses of opioids and etomidate is preferable to other regimens.

### Study Quality

Node-splitting technology was used to test the consistency of indirect and direct evidence, and the results are shown in **Supplementary Figure 2**. In the vast majority of comparisons, there was no statistically significant inconsistency between the direct and indirect estimates (P > 0.05). Publication bias was visually inspected using comparison-adjusted funnel plots (**Supplementary Figure 3**). Most studies were distributed on

TABLE 1 | Characteristics of included studies.


TABLE 1 [ (Continued)


ASA status = American Society of Anesthesiologists physical status; EM = Etomidate- induced myoclonus; TNM = Total number of myoclonus cases. *The presence of myoclonus was only reported as "present/absent", and no gradation was performed. both sides of the midline, and the left and right distributions were roughly symmetrical, suggesting that there was little possibility of publication bias and a small sample effect.

The risk of bias for the 31 RCTs is presented in Supplementary Figure 4. A total of 21 studies described the generation of random sequences, 23 trials described concealment details, 29 studies blinded subjects, 28 trials blinded evaluators of outcomes, and all the included studies showed complete data. One study was judged to be high-risk because of the different baseline data (the induction dose of etomidate was statistically different between different groups). The GRADE assessment showed that the quality of evidence for etomidate compared to other interventions was "high," indicating that the effect of using small doses of etomidate pre-induction to prevent EM is likely supported. The quality of evidence for the other comparisons is detailed in Supplementary Table 1.

## Subgroup Analysis of Myoclonus of Different Degrees

Mild myoclonus is a brief movement of a part of the body, such as the fingers and wrist. Moderate myoclonus is usually

![img-1.jpeg](img-1.jpeg)

FIGURE 2 | Network plot of treatment comparisons. The width of the line represents the number of RCTs per pairwise comparison, and the size of each node is proportional to the number of sample size.

![img-2.jpeg](img-2.jpeg)

FIGURE 3 | Forest plot for direct comparison of each pair of interventions. Meta-analysis use RR and 95%CI for the incidence of etomidate-induced myoclonus. RR, risk ratio; CI, confidence interval.

a movement of two different muscles, such as the face, leg, shoulder or elbow, with pronounced tremors. Severe myoclonus is the intense movement or rigidity of two muscles; for example, the body undergoes fast abduction (30). Subgroup analysis was conducted based on the severity of myoclonus. Here, we mainly divided the patients into two groups: mild

![img-3.jpeg](img-3.jpeg)

FIGURE 4 | Network meta-analysis comparison. (A) The incidence of etomidate-induced myoclonus was analyzed by using RR and 95%CI. Data in each cell are RR (95%CI) for the comparison of column-defining treatment versus row-defining treatment. Significant results are highlighted in red. RR, risk ratio; CI, confidence interval. (B) Graphical ranking based on SUCRA values (Incidence of total EM). The numbers on the X-axis represent the rankings. As the numbers increases, the effectiveness of the interventions decreases. B muscle relaxant, D dexmedetomidine, E etomidate, G gabapentin, P placebo, K κ opioid receptor agonist, L lidocaine, M midazolam, U μ opioid receptor agonist, N NMDA receptor antagonist.

![img-4.jpeg](img-4.jpeg)

FIGURE 5 | Subgroup analysis of myoclonus of different degrees. (A) The incidence of myoclonus of different severity after etomidate induction was analyzed by using RR and 95%CI. Data in each cell are RR (95%CI) for the comparison of column-defining treatment versus row-defining treatment. Significant results are highlighted in red. RR, risk ratio; CI, confidence interval. (B) Graphical ranking based on SUCRA values (Incidence of moderate to severe EM). The numbers on the X-axis represent the rankings. As the numbers increases, the effectiveness of the interventions decreases. B muscle relaxant, D dexmedetomidine (RR 1.14, 95%CI 1–1.31), midazolam (RR 1.14, 95%CI 1.06–1.24), κ-R agonist (RR 1.08, 95%CI 1–1.18), and μ-R agonist (RR 1.09, 95%CI 1.02–1.17) reduced the incidence of mild myoclonus. The results of the subgroup analysis are shown in Figure 5A. Since moderate-to-severe myoclonus is the most common clinical problem, we focused on the prevention and treatment effects of various interventions on moderate-to-severe myoclonus. For effectiveness in preventing moderate to severe EM, Figure 5B shows the corresponding ranking based on SUCRA values: etomidate > μ-R agonist > κ-R agonist > lidocaine > gabapentin > midazolam > dexmedetomidine > muscle relaxant > NMDA-R antagonist.

# DISCUSSION

Our NMA attempted to summarize the available data using direct and indirect evidence to conclude that pre-induction of anesthesia with low-dose opioids and etomidate is the best intervention to reduce the incidence and severity of etomidate-induced myoclonus. However, further research is warranted.

As a fast-acting intravenous anesthetic, etomidate has a low risk of hemodynamic damage. Compared with propofol, etomidate is especially suitable for anesthesia, procedural sedation and analgesia (PSA) in the emergency department for patients with trauma, shock, and acute abdomen, with hemodynamic instability. However, in some areas, etomidate use is partially limited by its ability to cause adrenocortical depression, myoclonus, and injection pain (31). Etomidate can induce myoclonus which may increase the risk of aspiration in satiated patients and patients with a decreased cardiac reserve and increased cardiac oxygen consumption (32). During severe myoclonus, electrocardiogram electrode shifts and pulse oxygen saturation measurements often show desaturation (33).

Myoclonus has been reported to be associated with hypoxemia during spontaneous ventilation when etomidate was used in the emergency department for PSA (34). In summary, myoclonic events may be large enough to delay patient monitoring and evaluation of intervention success.

The anesthetic effects of etomidate and its derivatives are generally thought to occur via GABA $_{A}$ receptors (35). Our current understanding of the mechanisms of etomidate-induced myoclonus is fragmented, contradictory, and confusing. Modica and Gancher et al. noted that etomidate is an electroencephalogram drug that has been shown to cause epileptic activities in non-epileptic patients (36-38). Therefore, etomidate-induced myoclonus may occur as epileptic activities, similar to the mechanisms underlying epilepsy. In contrast, Doenicke et al., in their study, reported that after giving etomidate, part of myoclonus patients only can be observed in EEG amplitude smaller, isolated, rapid, sharp transient wave, different from the typical epileptic EEG activity (30). Epilepsy is a clinical event with a definitive EEG diagnosis accompanied by a widespread, diffuse wave of EEG activities (39). It is prudent to say that anesthetics usually induce epileptiform activity, but rarely seizures. Epileptiform activity differs from epilepsy in that it primarily refers to the hypersynchrony of neurons in a small area $\left(<1 \mathrm{~cm}^{2}\right)$, and is considered an indicator of an incipiently unstable neocortex, with a weak association with clinically meaningful seizures (40). Another theory is that etomidate-induced myoclonus is a disinhibitory phenomenon (41). It may be that there are differences in local cerebral blood flow or in the affinity of receptors in the central nervous system that cause the action of etomidate to become unsynchronized. For example, large quantities of etomidate tend to inhibit cortical activity before they inhibit subcortical activity (30). Subsequently, subcortical disinhibition makes the pathways associated with controlling skeletal muscles more sensitive to spontaneous neurotransmitters, causing spontaneous myoclonus. GABAergic synaptic excitation and subgroup specificity between interneurons, which control the output of pyramidal cells, also partly explain this remarkable neurophysiological phenomenon (40). Although myoclonic excitation is not thought to be caused by epileptic foci, drugs such as dexmedetomidine ( $\alpha-2$ agonistmediated reduction of convulsion severity) and gabapentin (antiepileptic agents that increase the inhibitory effect of GABA) effectively reduce EM (33).

Although knowledge gaps still remain, it seems that implementing effective prevention is crucial and of the most practical value. As a single large dose of etomidate inhibits cortical activity earlier than subcortical activity, myoclonus can be prevented by prior suppression of subcortical neuronal activity with known drugs. Among the results of our analysis, seven interventions ( $\mu-\mathrm{R}$ agonist, $\kappa-\mathrm{R}$ agonist, etomidate, dexmedetomidine, midazolam, NMDA-R antagonist, and lidocaine) showed statistically significant improvements in preventing the incidence of EM compared with placebo, and six interventions ( $\mu-\mathrm{R}$ agonist, $\kappa-\mathrm{R}$ agonist, etomidate, dexmedetomidine, midazolam, and lidocaine) showed statistically significant improvements in preventing the incidence of moderate to severe EM.

The distinct distribution of $\mathrm{GABA}_{A}$ receptor subunits (mainly $\beta$ subunits) explains the dose-dependent effects of etomidate on the central nervous system. Etomidate can inhibit subcortical inhibitory circuits earlier and at lower doses, and when large doses are administered simultaneously, this mismatch is exaggerated, producing clinically visible myoclonus (32, 42, 43). Therefore, small doses of etomidate pre-induction can reduce the incidence of myoclonus.

The role of the $\kappa$-opioid receptor as a neuronal excitatory modulator is well known. Activation of the $\kappa$ receptor reduces glutamate release, produces postsynaptic hyperpolarization, and inhibits seizure activity (44). $\kappa$-opioid receptor agonists also interact with a variety of neurotransmitter systems ( $\mu$ opioid receptor, $\delta$ opioid receptor, $\gamma$-aminobutyric acid-benzodiazepinechloride ion channel, GABA receptors, and NMDA receptor). Dezocine, butorphanol, and nalbuphine mainly bind to and regulate $\kappa$-opioid receptors; therefore, the mechanism by which these drugs reduce etomidate-induced myoclonus may lie in their activation through $\kappa$ receptor regulation as agonists (45-49).

Benzodiazepines and opioids, such as fentanyl, are known to inhibit subcortical neuronal activity (38). Many randomized controlled trials have shown that multiple opioids, including fentanyl, sufentanil, remifentanil, and oxycodone, are effective in reducing the incidence and severity of EM. However, apnea, nausea, vomiting, and bradycardia are possible (46, 50, 51). In the study by Su et al., intramuscular injection of midazolam $(0.05 \mathrm{mg} / \mathrm{kg}) 30 \mathrm{~min}$ before etomidate injection did not reduce the incidence of myoclonus, which was not significantly different from the previously reported incidence of myoclonus (50). Since opioid receptors are widely distributed in the brain, the mechanism by which opioid agonists inhibit myoclonus remains unknown. It may be that $\mu$-opioid receptors are stimulated in the basal ganglia, which changes the function of GABA receptors and reduces the release of GABA, thus inhibiting subcortical neuronal activity. In Parkinson's-related studies, opioid neuropeptides have been reported to strongly regulate synaptic transmission and striatal projection neuron (SPNs) activity (52). High opioid levels occur in parallel with abnormal dopaminergic transmission, producing symptoms similar to increased dopamine levels, thus attenuating the onset of muscle fibrillation.

Although other studies were included in a supplementary analysis, the reduction in myoclonic symptoms was not as significant as opioid and etomidate preconditioning, as indicated by our results. Non-depolarizing muscle relaxants are associated with blocking nerve conduction at neuromuscular junctions (53). Lidocaine reduces the activity of the nerve centers that cause myoclonus (54). Magnesium sulfate and ketamine are noncompetitive N-methyl-D-aspartate receptor antagonists, and their myoclonic inhibition is thought to be related to the inhibition of NMDA receptor activity in the central nervous system $(42,55)$. However, the efficacy varies from study to study. In the study by Un et al., the incidence of EM after magnesium sulfate pretreatment was $26 \%$, whereas in the study by Sedighinejad et al., the incidence was as high as $86 \%(42,56)$.

Regarding the response rates before and after the entire NMA, the hierarchical order of total myoclonus incidence differed

slightly from the results of the subgroup analysis, but opioid or etomidate preconditioning still showed a significant advantage. The latter seems to be the more important result.

There were some limitations to our study. First, fewer than $60 \%$ of the studies included more than 100 participants, which could have contributed to the risk of bias. Second, SUCRA was used to estimate the rank probability of comparative efficacy between different interventions. However, it has limitations, all of which are subject to uncertainties, and thus, the results need to be interpreted with caution. Third, in the past, most studies had different drug dosages according to the different curative effects. However, in this study, we only limited the category of drugs. We did not limit the dosage. This may have caused a bias. Fourth, this study did not consider the safety of using these drugs because only a few studies reported adverse reactions and there was not a large amount of data available. Fifth, although transcutaneous acupoint electrical stimulation has been previously reported to reduce the incidence and severity of etomidate myoclonus (57), non-pharmacological or other interventions were not considered in our study. Sixth, 31 RCTs were included, including nine interventions. However, only seven were studied in two or more trials. Only two studies reported on both muscle relaxants and gabapentin, respectively, which explains the wide $95 \%$ confidence interval for the ultimate RR for both drugs.

## CONCLUSION

Based on the currently available evidence, we used the NMA approach to compare the impact of different interventions on EM for the first time. Taken together, preoperative low-dose etomidate is the best intervention for preventing severe general myoclonus. Although opioids also have a prophylactic effect on general myoclonus, side effects should not be ignored. Our study provides strong evidence that implicates clinical practice.

## DATA AVAILABILITY STATEMENT

The original contributions presented in the study are included in the article/Supplementary Material, further inquiries can be directed to the corresponding author/s.

## AUTHOR CONTRIBUTIONS

K-DZ proposed the research idea, developed a retrieval strategy, and drafted the manuscript. L-YW and K-DZ conducted a literature search, literature selection, and bias risk assessment. D-XZ and Z-HZ performed data extraction. H-LW reviewed and revised the manuscript. All authors contributed to the analysis and interpretation of the data, revised the manuscript, and approved the final version prior to submission.

## FUNDING

This study was funded by the National Natural Science Foundation of China (NSFC 81570044), Shandong Provincial Natural Science Foundation (ZR2021MH099 and ZR2015HM038), and Shenzhen Fundamental Research Program (JCYJ20190807093801661).

## SUPPLEMENTARY MATERIAL

The Supplementary Material for this article can be found online at: https://www.frontiersin.org/articles/10.3389/fmed. 2022.799156/full\#supplementary-material
7. Hueter L, Schwarzkopf K, Simon M, Bredle D, Fritz H. Pretreatment with sufentanil reduces myoclonus after etomidate. Acta Anaesthesiol Scand. (2003) 47:482-4. doi: 10.1034/j.1399-6576.2003.00081.x
8. Du X, Zhou C, Pan L, Li C. Effect of dexmedetomidine in preventing etomidate-induced myoclonus: a meta-analysis. Drug Des Devel Ther. (2017) 11:365-70. doi: 10.2147/dddt.S121979
9. Hua J, Miao S, Shi M, Tu Q, Wang X, Liu S, et al. Effect of butorphanol on etomidate-induced myoclonus: a systematic review and meta-analysis. Drug Des Devel Ther. (2019) 13:1213-20. doi: 10.2147/dddt.S191982
10. Lang B, Zhang L, Li F, Lin Y, Zhang W, Yang C. Comparison of the efficacy and safety of remifentanil versus different pharmacological approaches on prevention of etomidate-induced myoclonus: a meta-analysis of randomized controlled trials. Drug Des Devel Ther. (2019) 13:1593-607. doi: 10.2147/dddt. S200200
11. Lang B, Zhang L, Yang C, Lin Y, Zhang W, Li F. Pretreatment with lidocaine reduces both incidence and severity of etomidate-induced myoclonus: a meta-analysis of randomized controlled trials. Drug Des Devel Ther. (2018) 12:3311-9. doi: 10.2147/dddt.S174057
12. Wang J, Li QB, Wu YY, Wang BN, Kang JL, Xu XW. Efficacy and safety of opioids for the prevention of etomidate-induced myoclonus: a meta-analysis. Am J Ther. (2018) 25:e517-23. doi: 10.1097/mjt. 0000000000000404

13. Zhou C, Zhu Y, Liu Z, Ruan L. Effect of pretreatment with midazolam on etomidate-induced myoclonus: a meta-analysis. J Int Med Res. (2017) 45:399-406. doi: 10.1177/0300060516682882
14. Zhu Y, Yang Y, Zhou C, Bao Z. Using dezocine to prevent etomidate-induced myoclonus: a meta-analysis of randomized trials. Drug Des Devel Ther. (2017) 11:2163-70. doi: 10.2147/dddt.S137464
15. Zhu Y, Zhou C, He Q. Butorphanol effectively prevents etomidate-induced myoclonus: a pooled analysis of 788 patients. J Int Med Res. (2019) 47:353-60. doi: 10.1177/0300060518801457
16. Rouse B, Chaimani A, Li T. Network meta-analysis: an introduction for clinicians. Intern Emerg Med. (2017) 12:103-11. doi: 10.1007/s11739-016-1583-7
17. Hutton B, Salanti G, Caldwell DM, Chaimani A, Schmid CH, Cameron C, et al. The PRISMA extension statement for reporting of systematic reviews incorporating network meta-analyses of health care interventions: checklist and explanations. Ann Intern Med. (2015) 162:777-84. doi: 10.7326/m142385
18. Bramer WM, Milic J, Mast F. Reviewing retrieved references for inclusion in systematic reviews using EndNote. J Med Lib Assoc JMLA. (2017) 105:84-7. doi: $10.5195 / \mathrm{jmla} .2017 .111$
19. Schardt C, Adams MB, Owens T, Keitz S, Fontelo P. Utilization of the PICO framework to improve searching PubMed for clinical questions. BMC Med Inform Decis Mak. (2007) 7:16. doi: 10.1186/1472-6947-7-16
20. Higgins JP, Altman DG, Gøtzsche PC, Jüni P, Moher D, Oxman AD, et al. The cochrane collaboration's tool for assessing risk of bias in randomised trials. BMJ (Clin Res ed). (2011) 343:d5928. doi: 10.1136/bmj.d5928
21. Puhan MA, Schünemann HJ, Murad MH, Li T, Brignardello-Petersen R, Singh JA, et al. A GRADE working group approach for rating the quality of treatment effect estimates from network meta-analysis. BMJ (Clin Res ed). (2014) 349:g5630. doi: 10.1136/bmj.g5630
22. Higgins JP, Thompson SG, Deeks JJ, Altman DG. Measuring inconsistency in meta-analyses. BMJ (Clin Res ed). (2003) 327:557-60. doi: 10.1136/bmj.327. 7414.557
23. Sobieraj DM, Cappelleri JC, Baker WL, Phung OJ, White CM, Coleman CI. Methods used to conduct and report Bayesian mixed treatment comparisons published in the medical literature: a systematic review. BMJ Open. (2013) 3:e003111. doi: 10.1136/bmjopen-2013-003111
24. Xu Q, Zhang X, Huang M, Dai X, Gao J, Li S, et al. Comparison of efficacy and safety of single and double immune checkpoint inhibitor-based first-line treatments for advanced driver-gene wild-type non-small cell lung cancer: a systematic review and network meta-analysis. Front Immunol. (2021) 12:731546. doi: 10.3389/fimmu.2021.731546
25. Shim SR, Kim SJ, Lee J, Rücker G. Network meta-analysis: application and practice using R software. Epidemiol Health. (2019) 41:e2019013. doi: 10.4178/ epih.e2019013
26. Spiegelhalter DJ, Best NG, Carlin BR, van der Linde A. Bayesian measures of model complexity and fit. J Royal Stat Soc Ser B Stat Methodol. (2002) 64:583-616. doi: 10.1111/1467-9868.00353
27. Salanti G, Ades AE, Ioannidis JP. Graphical methods and numerical summaries for presenting results from multiple-treatment meta-analysis: an overview and tutorial. J Clin Epidemiol. (2011) 64:163-71. doi: 10.1016/j. jclinepi.2010.03.016
28. Song F, Loke YK, Walsh T, Glenny AM, Eastwood AJ, Altman DG. Methodological problems in the use of indirect comparisons for evaluating healthcare interventions: survey of published systematic reviews. BMJ (Clin Res ed). (2009) 338:b1147. doi: 10.1136/bmj.b1147
29. van Valkenhoef G, Dias S, Ades AE, Welton NJ. Automated generation of node-splitting models for assessment of inconsistency in network meta-analysis. Res Synth Methods. (2016) 7:80-93. doi: 10.1002/jrsm .1167
30. Doenicke AW, Roizen MF, Kugler J, Kroll H, Foss J, Ostwald P. Reducing myoclonus after etomidate. Anesthesiology. (1999) 90:113-9. doi: 10.1097/ 00000542-199901000-00017
31. Moningi S, Reddy GP, Nikhar SA, Chikkala R, Kulkarni DK, Ramachandran G. Comparison of the influence of low dose etomidate and propofol as priming dose on the incidence of etomidate induced myoclonus: a randomised, doubleblind clinical trial. Braz J Anesthesiol (Elsevier). (2021). doi: 10.1016/j.bjane. 2021.02.047 [Epub ahead of print].
32. Aissaoui Y, Belyamani L, El Wali A, Idrissi Hajjouji SM, Atmani M, Drissi Kamili N. [Prevention of myoclonus after etomidate using a priming dose]. Ann Fr Anesth Reanim. (2006) 25:1041-5. doi: 10.1016/j.annfar.2006.07.079
33. Ydmaz Çakirgöz M, Demirel Ý, Duran E, Özer AB, Hancı V, Türkmen ÜA, et al. Effect of gabapentin pretreatment on myoclonus after etomidate: a randomized, double-blind, placebo-controlled study. Braz J Anesthesiol (Elsevier). (2016) 66:356-62. doi: 10.1016/j.bjane.2014.11.014
34. Van Keulen SG, Burton JH. Myoclonus associated with etomidate for ED procedural sedation and analgesia. Am J Emerg Med. (2003) 21:556-8. doi: 10.1016/j.ajem.2003.08.004
35. Sneyd JR. Novel etomidate derivatives. Curr Pharmaceut Des. (2012) 18:62536. doi: 10.2174/138161212803832362
36. Gancher S, Lazer KD, Krieger W. Activation of epileptogenic activity by etomidate. Anesthesiology. (1984) 61:616-8. doi: 10.1097/00000542-198411000-00029
37. Modica PA, Tempelhoff R, White PF. Pro- and anticonvulsant effects of anesthetics (Part I). Anesth Analg. (1990) 70:303-15. doi: 10.1213/00000539-199003000-00015
38. Modica PA, Tempelhoff R, White PF. Pro- and anticonvulsant effects of anesthetics (Part II). Anesth Analg. (1990) 70:433-44. doi: 10.1213/00000539-199004000-00016
39. Fisher RS, van Emde Boas W, Blume W, Elger C, Genton P, Lee P, et al. Epileptic seizures and epilepsy: definitions proposed by the international league against epilepsy (ILAE) and the International Bureau for Epilepsy (IBE). Epilepsia. (2005) 46:470-2. doi: 10.1111/j.0013-9580.2005.66104.x
40. Voss LJ, Sleigh JW, Barnard JP, Kirsch HE. The howling cortex: seizures and general anesthetic drugs. Anesth Analg. (2008) 107:1689-703. doi: 10.1213/ ane.0b013e3181852595
41. Reddy RV, Moorthy SS, Dierdorf SF, Deitch RD Jr., Link L. . Excitatory effects and electroencephalographic correlation of etomidate, thiopental, methohexital, and propofol. Anesth Analg. (1993) 77:1008-11. doi: 10.1213/ 00000539-199311000-00023
42. Sedighinejad A, Naderi Nabi B, Haghighi M, Biazar G, Imantalab V, Rimaz S, et al. Comparison of the effects of low-dose midazolam, magnesium sulfate, remifentanil and low-dose etomidate on prevention of etomidate-induced myoclonus in orthopedic surgeries. Anesthesiol Pain Med. (2016) 6:e35333. doi: 10.5812/aapm. 35333
43. Mullick P, Talwar V, Aggarwal S, Prakash S, Pawar M. Comparison of priming versus slow injection for reducing etomidate-induced myoclonus: a randomized controlled study. Korean J Anesthesiol. (2018) 71:305-10. doi: 10.4097/kja.d.18.27168
44. Burtscher J, Schwarzer C. The opioid system in temporal lobe epilepsy: functional role and therapeutic potential. Front Mol Neurosci. (2017) 10:245. doi: 10.3389/fnmol.2017.00245
45. Bisht M, Pokhriyal AS, Khurana G, Sharma JP. Effect of fentanyl and nalbuphine for prevention of etomidate-induced myoclonus. Anesth Essays Res. (2019) 13:119-25. doi: 10.4103/aer.AER_188_18
46. Gupta M, Gupta P. Nalbuphine pretreatment for prevention of etomidate induced myoclonus: a prospective, randomized and double-blind study. J Anaesthesiol Clin Pharmacol. (2018) 34:200-4. doi: 10.4103/joacp.JOACP_ 210_16
47. He L, Ding Y, Chen H, Qian Y, Li Z. Butorphanol pre-treatment prevents myoclonus induced by etomidate: a randomised, double-blind, controlled clinical trial. Swiss Med Wkly. (2014) 144:w14042. doi: 10.4414/smw. 2014. 14042
48. He L, Ding Y, Chen H, Qian Y, Li Z. Dezocine pretreatment prevents myoclonus induced by etomidate: a randomized, double-blinded controlled trial. J Anesth. (2015) 29:143-5. doi: 10.1007/s00540-014-1854-2
49. Lv Z, Fang J, Zhu J, Liang B, Li F, Jiang S, et al. Intravenous dezocine pretreatment reduces the incidence and intensity of myoclonus induced by etomidate. J Anesth. (2014) 28:944-7. doi: 10.1007/s00540-014-1842-6
50. Ri HS, Shin SW, Kim TK, Baik SW, Yoon JU, Byeon GJ. The proper effect site concentration of remifentanil for prevention of myoclonus after etomidate injection. Korean J Anesthesiol. (2011) 61:127-32. doi: 10.4097/kjae.2011.61.2. 127
51. Hwang JY, Kim JH, Oh AY, Do SH, Jeon YT, Han SH. A comparison of midazolam with remifentanil for the prevention of myoclonic movements following etomidate injection. J Int Med Res. (2008) 36:17-22.

52. Sgroi S, Tonini R. Opioidergic modulation of striatal circuits, implications in parkinson's disease and levodopa induced dyskinesia. Front Neurol. (2018) 9:524. doi: 10.3389/fneur.2018.00524
53. Choi JM, Choi IC, Jeong YB, Kim TH, Hahm KD. Pretreatment of rocuronium reduces the frequency and severity of etomidate-induced myoclonus. J Clin Anesth. (2008) 20:601-4. doi: 10.1016/j.jclinane.2008.06.010
54. Nyman Y, Von Hofsten K, Palm C, Eksborg S, Lönnqvist PA. EtomidateLipun is associated with considerably less injection pain in children compared with propofol with added lidocaine. Br J Anaesth. (2006) 97:536-9. doi: 10. 1093/bja/ael187
55. Wu GN, Xu HJ, Liu FF, Wu X, Zhou H. Low-dose ketamine pretreatment reduces the incidence and severity of myoclonus induced by etomidate: a randomized, double-blinded, controlled clinical trial. Medicine. (2016) 95:e2701. doi: 10.1097/md. 0000000000002701
56. Un B, Ceyhan D, Yelken B. Prevention of etomidate-related myoclonus in anesthetic induction by pretreatment with magnesium. J Res Med Sci. (2011) $16: 1490-4$.
57. Lv Y, He H, Xie J, Jin W, Shou C, Pan Y, et al. Effects of transcutaneous acupoint electrical stimulation combined with low-dose sufentanil pretreatment on the incidence and severity of etomidate-induced myoclonus: A randomized controlled trial. Medicine. (2018) 97:e10969. doi: 10.1097/md. 0000000000010969
58. Wang W, Lv J, Wang Q, Yang L, Yu W. Oxycodone for prevention of etomidate-induced myoclonus: a randomized double-blind controlled trial. $J$ Int Med Res. (2018) 46:1839-45. doi: 10.1177/0300060518761788
59. Mizrak A, Koruk S, Bilgi M, Kocamer B, Erkutlu I, Ganidagli S, et al. Pretreatment with dexmedetomidine or thiopental decreases myoclonus after etomidate: a randomized, double-blind controlled trial. J Surg Res. (2010) 159:e11-6. doi: 10.1016/j.jss.2009.07.031
60. Miao S, Zou L, Wang G, Wang X, Liu S, Shi M. Effect of dexmedetomidine on etomidate-induced myoclonus: a randomized, double-blind controlled trial. Drug Des Devel Ther. (2019) 13:1803-8. doi: 10.2147/dddt.S19 4456
61. Alipour M, Tabari M, Azad AM. Comparative study evaluating efficacy of sufentanil versus midazolam in preventing myoclonic movements following etomidate. J Anaesthesiol Clin Pharmacol. (2016) 32:29-32. doi: 10.4103/09709185.173382
62. An X, Li C, Sahebally Z, Wen X, Zhao B, Fang X. Pretreatment with oxycodone simultaneously reduces etomidate-induced myoclonus and rocuronium-induced withdrawal movements during rapid-sequence induction. Med Sci Monit. (2017) 23:4989-94. doi: 10.12659/msm. 90 2652
63. Luan HF, Zhao ZB, Feng JY, Cui JZ, Zhang XB, Zhu P, et al. Prevention of etomidate-induced myoclonus during anesthetic induction by pretreatment with dexmedetomidine. Braz J Med Biol Res. (2015) 48:186-90. doi: 10.1590/ 1414-431x20144100
64. Guler A, Satilmis T, Akinci SB, Celebioglu B, Kanbak M. Magnesium sulfate pretreatment reduces myoclonus after etomidate. Anesth Analg. (2005) 101:705-9. doi: 10.1213/01.Ane.0000160529.95019.E6
65. Gultop F, Akkaya T, Bedirli N, Gumus H. Lidocaine pretreatment reduces the frequency and severity of myoclonus induced by etomidate. J Anesth. (2010) 24:300-2. doi: 10.1007/s00540-010-0869-6
66. Gupta P, Gupta M. Comparison of different doses of intravenous lignocaine on etomidate-induced myoclonus: a prospective randomised and placebocontrolled study. Indian J Anaesth. (2018) 62:121-6. doi: 10.4103/ija .IJA_563_17
67. Hüter L, Schreiber T, Gugel M, Schwarzkopf K. Low-dose intravenous midazolam reduces etomidate-induced myoclonus: a prospective, randomized study in patients undergoing elective cardioversion. Anesth Analg. (2007) 105:1298-302. doi: 10.1213/01.ane.0000287248.25610.c0
68. Aktolga S, Gunes Y, Gunduz M, Isik G. A comparison of midazolam and dexmedetomidine for the prevention of myoclonic movements and pain following etomidate injection. J Anaesthesiol Clin Pharmacol. (2010) 26:162-6.
69. Ko BJ, Oh JN, Lee JH, Choi SR, Lee SC, Chung CJ. Comparison of effects of fentanyl and remifentanil on hemodynamic response to endotracheal intubation and myoclonus in elderly patients with etomidate induction. Korean J Anesthesiol. (2013) 64:12-8. doi: 10.4097/kjae.2013.6 4.1.12
70. Woo LS, Jue GH, Chul PS, Young KJ, Hyung KJ, Yeon LJ, et al. The effect of remifentanil for reducing myoclonus during induction of anesthesia with etomidate. Korean J Anesthesiol. (2009) 57:438-43. doi: 10.4097/kjae.2009.57. 4.438
71. Prakash S, Mullick P, Virmani P, Talwar V, Singh R. Effect of Pre-Treatment with a Combination of Fentanyl and Midazolam for Prevention of EtomidateInduced Myoclonus. Turk J Anaesthesiol Reanim. (2019) 49:11-7.
72. Ilke I, Sinan U, Mehmet T, Ayşe V, Gökhan GY, Yilmaz IF, et al. Prevention of etomidate-induced myoclonus: which is superior: Fentanyl, midazolam, or a combination? A Retrospective comparative study. Med Sci Monit. (2014) 20:262-7. doi: 10.12659/MSM. 889833
73. Singh K, Ruchi G, Singh A, Kaur B. Efficacy of lignocaine versus midazolam in controlling etomidate-induced myoclonus: a randomized placebo-controlled study. Ain-Shams J Anaesthesiol. (2014) 7:460-4. doi: 10.4103/1687-7934. 139597
74. Boztug N, Bigat Z, Onder G, Dikici A, Karsli B, Ertok E. The comparison of different doses of remifentanil on preventing myoclonus due to etomidate: A-504. Eur J Anaesthesiol. (2005) 22 (Suppl. 34):132. doi: 10.1097/00003643-200505001-00472
75. Yukselen AM, Guler A, Celebioglu B, Kanbak M, Aypar U. Comparison of the effect of remifentanil and fentanyl on myoclonus due to etomidate: A507. Eur J Anaesthesiol. (2005) 22 (Suppl. 34):132-3. doi: 10.1097/00003643-200505001-00475
76. Mutlu NM, Ediz N, Karabulut E, Gogus N. The effects of different doses of remifentanil pretreatment on etomidate injection pain and myoclonus: 9AP3-9. Eur J Anaesthesiol. (2007) 24 (Suppl. 39):115. doi: 10.1097/00003643-200706001-00426

Conflict of Interest: The authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest.

Publisher's Note: All claims expressed in this article are solely those of the authors and do not necessarily represent those of their affiliated organizations, or those of the publisher, the editors and the reviewers. Any product that may be evaluated in this article, or claim that may be made by its manufacturer, is not guaranteed or endorsed by the publisher.

Copyright © 2022 Zhang, Wang, Zhang, Zhang and Wang. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.