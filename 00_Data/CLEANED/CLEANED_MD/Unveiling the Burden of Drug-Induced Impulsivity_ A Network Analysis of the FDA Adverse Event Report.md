# Unveiling the Burden of Drug-Induced Impulsivity: A Network Analysis of the FDA Adverse Event Reporting System 

Michele Fusaroli ${ }^{1}$ (D) $\cdot$ Stefano Polizzi ${ }^{2} \cdot$ Luca Menestrina ${ }^{3} \cdot$ Valentina Giunchi ${ }^{1} \cdot$ Luca Pellegrini ${ }^{4,5} \cdot$ Emanuel Raschi ${ }^{1} \cdot$ Daniel Weintraub ${ }^{6,7} \cdot$ Maurizio Recanatini ${ }^{3} \cdot$ Gastone Castellani ${ }^{2} \cdot$ Fabrizio De Ponti ${ }^{1} \cdot$ Elisabetta Poluzzi ${ }^{1}$<br>Accepted: 22 July 2024 / Published online: 15 August 2024<br>(c) The Author(s) 2024


#### Abstract

Introduction Impulsivity induced by dopaminergic agents, like pramipexole and aripiprazole, can lead to behavioral addictions that impact on social functioning and quality of life of patients and families (e.g., resulting in unemployment, marital problems, anxiety). These secondary effects, interconnected in networks of signs and symptoms, are usually overlooked by clinical trials, not reported in package inserts, and neglected in clinical practice. Objective This study explores the syndromic burden of impulsivity induced by pramipexole and aripiprazole, pinpointing key symptoms for targeted mitigation. Methods An event-event Information Component (IC) on the FDA Adverse Event Reporting System (FAERS) (January 2004 to March 2022) identified the syndrome of events disproportionally co-reported with impulsivity, separately for pramipexole and aripiprazole. A greedy-modularity clustering on composite network analyses (positive pointwise mutual information [PPMI], Ising, $\Phi$ ) identified sub-syndromes. Bayesian network modeling highlighted possible precipitating events. Results Suspected drug-induced impulsivity was documented in $7.49 \%$ pramipexole and $4.50 \%$ aripiprazole recipients. The highest IC concerned obsessive-compulsive disorder (reporting rate $=26.77 \%$; IC median $=3.47,95 \%$ confidence interval $[\mathrm{CI}]=3.33-3.57$ ) and emotional distress $(21.35 \% ; 3.42,3.26-3.54)$ for pramipexole, bankruptcy $(10.58 \% ; 4.43,4.26-4.55)$ and divorce $(7.59 \% ; 4.38,4.19-4.53)$ for aripiprazole. The network analysis identified delusional jealousy and dopamine dysregulation sub-syndromes for pramipexole, obesity-hypoventilation and social issues for aripiprazole. The Bayesian network highlighted anxiety and economic problems as potentially precipitating events. Conclusion The under-explored consequences of drug-induced impulsivity significantly burden patients and families. Network analyses, exploring syndromic reactions and potential precipitating events, complement traditional techniques and clinical judgment. Characterizing the secondary impact of reactions will support informed patient-centered decision making.


## Key Points

Network analyses characterize drug-induced impulsivity as a syndrome with several possible manifestations.

Manifestations were shaped by interactions between impulsivity and the underlying disease.

Michele Fusaroli, Stefano Polizzi, and Luca Menestrina equally contributed.

[^0]
## 1 Introduction

Adverse drug reactions (ADRs) significantly impact patients' well-being [1], extending from biological to psychological and social issues [2, 3]. For instance, immunodeficiency perturbs social activities. Dysphonia hinders the ability to function in positions requiring extensive vocal communication such as teaching or other public-facing roles. Sexual dysfunction can affect relationships and even personal identity, with further cascading effects on psychological and physical well-being. Despite their profound effects and complex networks of interactions, ADRs are often inadequately recognized, resulting in compromised patient-doctor relationships [4], prolonged hospitalization [5], and a pervasive decline in quality of life (QoL) [6]. Evidence obtained from patient-reported outcomes, is crucial for QoL assessment and patient-centered care [7], but is equally disregarded and


[^0]:    Extended author information available on the last page of the article

often relegated to the margins in prescribing information or package inserts [8].

Drug-induced impulsivity, classified as "impulse control disorders induced by other specified psychoactive substance (6C4E.73)" in the International Classification of Diseases (ICD-11) category of disorders due to substance use, represents a distressing group of conditions marked by a loss of behavioral control. This pathological disinhibition can yield behaviors as pervasive as pathologic gambling, hypersexuality, compulsive shopping, and hyperphagia-the so-called "four knights of Impulse Control Disorder", all with important further repercussions on social relationships, physical and psychological well-being [9]. Other behaviors such as stealing, hair pulling, and compulsive hoarding, while less acknowledged, can also occur, and further diversify potential manifestations of drug-induced impulsivity $[10,11]$.

The first reports of drug-induced impulsivity were linked to dopamine receptor agonists like pramipexole, ropinirole, and rotigotine, licensed for treating Parkinson's disease (PD) [12] and restless legs syndrome (RLS) [13, 14]. Dopamine agonists administered for PD show a 5-year cumulative incidence of impulsivity of $50 \%$ [15]. More recently, partial dopamine agonists like aripiprazole, brexpiprazole, and cariprazine, licensed for treating psychosis and mood disorders, have also emerged as potential causes of druginduced impulsivity [16], but with a still under-characterized epidemiology [17]. Impulsivity as induced by PD treatment has a complex trajectory and may have a different impact on QoL depending on underlying susceptibilities and on the occurrence of exacerbating events. The treatment might initially induce a "honeymoon period", in which patients experience heightened motivational drive and often engage in new satisfying hobbies [18]. However, impulsivity can eventually lead to pervasive behaviors and become pathologic. Even when concealed in subclinical forms [19], drug-induced impulsivity holds the potential to significantly erode patients' QoL [20]. This erosion, appraised through metrics like the PDQ-39 scale [21], encompasses diverse neuropsychiatric and somatic domains including mobility, daily activities, stigma, social support, communication [22], urinary and sexual function, sleep, attention, and cardiovascular symptoms [23]. The impact extends beyond patients as it affects caregivers, who grapple with their own set of health issues, depression, and social impediments due to their duties of care [24].

Nevertheless, conventional evaluations focus on simple drug-physical adverse reaction associations, and often ignore neuropsychiatric symptoms, altered behavior patterns, financial hardships, and legal entanglements as emerging from drug-induced impulsivity [25], thus failing to capture the complex network of consequences of its manifestation [26]. This underscores the crucial need for an integrative
approach that consider the perspectives of both patients and caregivers and acknowledges the complex interconnections between symptoms [27], including identifying subsyndromes and exacerbating events.

In order to better characterize such networks, we can rely on databases collecting individual case safety reports of suspected ADRs from patients and healthcare professionals. In this manuscript we will rely on the US FDA Adverse Event Reporting System (FAERS), as it is global and public [28]. Crucially, the patient-produced reports offer impactful insights into the experiences and impacts of ADRs on QoL, beyond those provided by healthcare professionals [29-33].

Network analyses provide the means to explore ADRs as complex systems consisting of multiple interacting entities. Specifically, they enable the analysis and visualization of ADRs as interwoven symptoms and signs [34]: a composite syndrome encompassing psychosocial implications, clustered into sub-syndromes. This approach overcomes the drawbacks of viewing drug-induced impulsivity as an isolated incident. Beyond more descriptive approaches such as those built on measures of association (Ising [35], $\Phi$ [36], and PPMI [37]), network approaches can also explore possible causal connections between symptoms, allowing to identify potential exacerbating events [38, 39].

In the current manuscript we pursue three goals. First, we want to fully acknowledge the complexity of drug-induced impulsivity as reported not only by clinical researchers, but also by clinicians and patients. We go beyond a pairwise drug to adverse reaction approach and more fully embrace the idea of a syndrome of causally interconnected events, from behavioral addictions to their organic and psychosocial sequelae. By examining the network in which symptoms interact and affect each other, we aim to gain a deeper understanding of the impact of drug-induced impulsivity on patients' lives.

Second, we want to assess the possibility of distinct subsyndromes within the broader spectrum of drug-induced impulsivity. For example, when impulsivity manifests as hyperphagia it may have more organic sequelae related to increased weight compared to when it manifests as pathological gambling.

Third, we assess the presence of central symptoms, potentially crucially exacerbating the syndrome of drug-induced impulsivity. By pin-pointing these key symptoms, we aim to pave the way for targeted interventions that alleviate the adverse effects on patients' lives.

In pursuing these goals, our study focused on two widely used drugs representative of the two drug classes with an established role in causing impulsivity: pramipexole and aripiprazole. Pramipexole, a dopamine agonist used in neurological conditions, is typically prescribed to older individuals with stronger social support and a lower baseline motivational drive.

Fig. 1 Pipeline of the study, showing step-by-step study design. FAERS FDA Adverse Event Reporting System, $P P M I$ positive pointwise mutual information
![img-0.jpeg](img-0.jpeg)

Aripiprazole, a dopamine partial agonist employed in psychiatric disorders, is usually prescribed to younger and more stigmatized individuals, with a higher baseline motivational drive. Using these two examples allowed us to capture commonalities in drug-induced impulsivity as well as potentially different mechanisms/syndromes that manifest only in a specific indication/patient type or with a specific drug class. A better understanding of the impact of these ADRs on QoL could contribute to informed decision making for patients and caregivers, laying the foundation
for interventions that are capable of alleviating the burden exacted by impulsivity.

## 2 Methods

### 2.1 Study Design

The study design is presented in Fig. 1. We first downloaded and pre-processed FAERS reports from January

1st, 2004, to March 31st, 2022 (Step 1) and selected cases recording impulsivity among the two separate populations of aripiprazole and pramipexole recipients (Step 2). In order to characterize the impulsivity syndrome, we identified the set of events disproportionally co-reported with drug-induced impulsivity, rather than with other suspected reactions to the same drug, using an event-event disproportionality analysis (Step 3). To explore potential sub-syndromes, we relied on three parallel commonly used descriptive network analyses and a greedy-modularity algorithm, able to identify more cohesive clusters of coreported events (Step 4). Finally, to explore possible causal relations within these networks and the secondary impact of drug-induced impulsivity, we relied on a Bayesian network approach, able to estimate conditional probabilities of chained events (Step 5). These operations were performed in a standardized and reproducible fashion, made possible by the DiAna R package: an open-access toolkit for disproportionality analyses and other pharmacovigilance investigations in the FAERS [40].

### 2.2 Step 1: Data Preprocessing

We downloaded FAERS quarterly data in ASCII format (January 1st, 2004, to March 31st, 2022) [28]. Adverse events were coded according to the Medical Dictionary for Regulatory Activities (MedDRA ${ }^{\circledR}$, version 25.0) ${ }^{1}$ preferred terms (PTs) [41], while drugs were standardized according to their active ingredients [42]. The latest report version was retained, and rule-based deduplication was applied to reduce redundancy (cfr. https://github.com/fusarolimichele/DiAna).

### 2.3 Step 2: Case Retrieval

We retrieved aripiprazole and pramipexole recipients separately and identified cases as reports recording impulsivity among the suspected reactions. To identify impulsivity we used a MedDRA ${ }^{\circledR}$ PT list specifically curated for investigating druginduced impulsivity within the FAERS database [10], encompassing heterogenous manifestations including gambling, hypersexuality, compulsive shopping, hyperphagia, computer gaming, setting fires, stealing, hoarding, excessive exercise, overwork, compulsive wandering, body-focused repetitive behaviors, stereotypy, and impulsivity (see Table S1). MedDRA ${ }^{\circledR}$ PTs used for reporting suspected ADRs do not align directly with terms in other frameworks like the Diagnostic and Statistical Manual

[^0]Table 1 Two-way contingency table


The table shows the different instances that can be observed when considering pathologic impulsivity and a specific event $\mathrm{E}=$ event, $\mathrm{I}=$ impulsivity, $1=$ presence, $0=$ lack, $N=$ total $\mathrm{IC}(x, y)=\operatorname{PMI}(x, y)=\log _{2} \frac{p(y, x)}{p(y) p(y)}=\log _{2} \frac{n_{I_{1} E_{1}}+N}{n_{I_{1}}+n_{E_{1}}} \approx \log _{2} \frac{n_{I_{0} E_{1}}+0.5}{n_{I_{0}}+0.5} \times 0.5$ $\mathrm{IC}(x, y)_{025}=\mathrm{IC}-3.3 *\left(n_{I_{1} E_{1}}+0.5\right)^{-\frac{1}{2}}-2 *\left(n_{I_{1} E_{1}}+0.5\right)^{-\frac{1}{2}}$ $\mathrm{IC}(x, y)_{075}=\mathrm{IC}+2.4 *\left(n_{I_{1} E_{1}}+0.5\right)^{-\frac{1}{2}}-0.5 *\left(n_{I_{1} E_{1}}+0.5\right)^{-\frac{1}{2}}$
of mental disorders (DSM-5-TR) and ICD-11 (e.g., referring to "kleptomania" as an idiopathic condition).

To explore potential risk factors for impulsivity, demographic characteristics, outcomes, and reporter contributions (e.g., healthcare practitioners, patients, lawyers) were compared between cases and non-cases within each population, using the Chi-square test for categorical and Mann-Whitney test for continuous variables. To address multiple testing, we applied the Holm-Bonferroni correction with a significance level of 0.05 .

### 2.4 Step 3: Disproportionality Analysis: The Drug-Induced Impulsivity Syndrome

We conducted an event-event disproportionality analysis to identify events frequently co-reported with drug-induced impulsivity, separately for aripiprazole and pramipexole recipients (see Table 1). Following Good Signal Detection Practices by IMI PROTECT [43], we chose as measure of disproportionate reporting the Information Component (IC) [44], also known as pointwise mutual information (PMI) in information theory [45, 46]. The IC compares the actual co-reporting of two events $x$ (i.e., drug-induced impulsivity) and $y$ (i.e., any specific event) with their expected co-reporting if their probability were independent $(p(y, x)>p(x) * p(y))$ [45]. Information Component was particularly appropriate for our study, compared to frequentist disproportionality measures, as it mitigates the risk of false positives for infrequent events and small datasets [47] through a shrinkage/smoothing approach applied by adding $k=0.5$ to both the numerator and denominator. Significance was determined using $\mathrm{IC}_{025}>0$.

### 2.5 Step 4: Network Analysis: Sub-syndromes

Building on insights from prior studies on drugs [48] and event $[34,49,50]$ co-occurrence, our network analysis aimed to unveil, within the drug-induced impulsivity syndrome, sub-syndromes of cohesively clustered events. Together with the Ising estimation [35, 51], already implemented in


[^0]:    ${ }^{1}$ MedDRA $^{\circledR}$ the Medical Dictionary for Regulatory Activities terminology is the international medical terminology developed under the auspices of the International Conference on Harmonization of Technical Requirements for Registration of Pharmaceuticals for Human Use (ICH). MedDRA ${ }^{\circledR}$ trademark is owned by the International Federation of Pharmaceutical Manufacturers and Associations (IFPMA) on behalf of ICH.

Table 2 Network estimations

A LASSO method pruned out weak links, eliminating spurious associations but potentially sacrificing weaker genuine relationships, especially triangular type interactions. | Focuses on cases where events were reported together $\left(n_{11}\right)$, applying additive smoothing $(k=1, d=$ no. events) Bootstrap and Bonferroni adjustments assessed statistical significance, with a 0.01 threshold for higher specificity. Gives more weight to associations with infrequent events. | The $\phi$ coefficient, akin to the traditional correlation coefficient, approaches one when two events are frequently reported together and converges to zero if they are either independent or mutually exclusive. The Bonferroni adjustment was applied with a significance threshold of 0.01 . The $p$ value was computed using a $\chi^{2}$ probability distribution with one degree of freedom.  |

The table shows the features of the network estimations implemented PPMI positive pointwise mutual information pharmacovigilance because of its ability to obtain a sparser and easily interpretable network (because of fewer links and more definite clusters) [34], we implemented two other more connected network estimations in order to identify broader co-reporting patterns (positive pointwise mutual information [PPMI] [37], Ising, $\phi$ [36]). See Table 2 for the features of the three networks. We did not consider negative links (i.e., potential mutually exclusive events).

Separately for the two populations of aripiprazole and pramipexole recipients, the three networks shared identical nodes by definition but different links were inferred due to the different properties of the algorithms. We used modularity maximization [52] and the greedy modularity algorithm [53] to detect clusters of co-reported signs and symptoms. Between networks we compared degree of link overlap (Jaccard similarity index [54]), goodness of partitioning (clustering modularity), cluster agreement (Purity index [55-57]), link density (ratio of actual links to possible links), and interconnectedness among neighbors (small worldness [58]).

### 2.6 Step 5: Bayesian Network: The Secondary Impact of Drug-Induced Impulsivity

While other methods look only at symmetrical associations, we expect that some events may cause other events. To exploratively identify these potential causal dependencies following drug-induced impulsivity, we estimated the conditional probabilities of chained events [38, 39]. The resulting Bayesian network is both directed (offering insights into plausible causal relationships), and acyclic (no chain of arrows loops back to itself). The network was derived through 1000 bootstraps, optimizing the BIC score with the Hill-Climbing algorithm. We computed the average network retaining links exceeding a threshold computed via $L_{1}$ minimization. Evaluation focused on nodes with the highest out-degree centrality and the main manifestations of drug-induced impulsivity.

## 3 Results

### 3.1 Case Retrieval

We retrieved 12,030,756 distinct reports: 27,601 pramipexole recipients and 80,238 aripiprazole recipients. Suspected drug-induced impulsivity was documented in $7.49 \%$ of pramipexole recipients $(n=2066$ : mainly gambling disorder, $n=1345,4.87 \%$; hypersexuality, 612, $2.22 \%$; impulsivity, $453,1.64 \%$; compulsive shopping, 384 , $1.39 \%$; hyperphagia, $334,1.21 \%$ ) and in $4.50 \%$ aripiprazole recipients $(n=3609$ : mainly gambling disorder, $n=2067$, $2.58 \%$; hypersexuality, $1077,1.34 \%$; compulsive shopping, $1029,1.28 \%$; hyperphagia, $868,1.08 \%$; impulsivity, 730 , $0.91 \%$ ) (see Table S2).

Among pramipexole recipients, drug-induced impulsivity was more frequently reported in males ( $57.42 \%$ vs $36.99 \%$, $p<0.001$ ) and younger patients ( 56 vs $67, p<0.001$ ), often recording non-serious outcomes (i.e., no death, disability, or hospitalization; $44.87 \%$ vs $33.58 \%, p<0.001$ ) and Parkinson's Disease (PD) as indication (see Fig. 2 and Table S3). Similarly, among aripiprazole recipients, drug-induced impulsivity was more common in males ( $48.59 \%$ vs $40.72 \%$, $p<0.001$ ); peculiarly, hospitalization was more common ( $33.39 \%$ vs $23.39 \%, p<0.001$ ), and an important portion of reports was submitted by lawyers ( $34.08 \%$ vs $1.10 \%, p<$ 0.001 ) (see Table S4).

![img-1.jpeg](img-1.jpeg)

Fig. 2 Characteristics of the investigated populations. The figure presents information about two populations extracted from the deduplicated FDA Adverse Event Reporting System (FAERS) database-one consisting of reports related to pramipexole and the other consisting of reports related to aripiprazole. Within these populations, cases of pathologic impulsivity were identified. The figure compares druginduced impulsivity cases and the reference group (other reports recording the drug), considering the indication for use. Only the two most prevalent indications were considered. For each drug and indication, the caption describes the percentage of reports with the specified indication, the percent of reports involving males, and the median and interquartile range of ages. In the drug-induced impulsivity cases sections, green plus signs and red minus signs indicate variables that are respectively higher or lower than expected based on the reference group

### 3.2 Disproportionality Analysis: The Drug-Induced Impulsivity Syndrome

A total of 56 events were disproportionally reported with pramipexole-related impulsivity. The highest IC was found for obsessive-compulsive disorder (OCD, reporting rate $=$ $26.77 \%$; IC median $=3.47,95 \% \mathrm{CI}=3.33-3.57$ ), emotional distress ( $21.35 \% ; 3.42,3.26-3.54$ ), marital problem ( $1.11 \%$; $3.30,2.61-3.79$ ), dependence ( $2.37 \% ; 3.26,2.79-3.6$ ), economic problems ( $6.05 \% ; 3.15,2.85-3.36$ ), compulsions $(1.74 \% ; 3.05,2.49-3.44)$, fear $(4.65 \% ; 2.95,2.61-3.19)$, eating disorder $(2.47 \% ; 2.95,2.49-3.28)$, personality change $(2.66 \% ; 2.93,2.49-3.26)$, and suicide attempt $(5.28 \% ; 2.74$, $2.43-2.97$ ).

A total of 107 events was disproportionally reported with aripiprazole-related impulsivity. The highest IC was found for bankruptcy ( $10.58 \% ; 4.43,4.26-4.55$ ), divorce ( $7.59 \%$; $4.38,4.19-4.53$ ), homelessness ( $6.93 \% ; 4.37,4.16-4.52$ ), shoplifting ( $5.02 \% ; 4.37,4.12-4.54$ ), neuropsychiatric symptoms $(4.74 \% ; 4.35,4.1-4.53)$, loss of employment $(12.64 \% ; 4.33,4.18-4.44)$, theft $(5.79 \% ; 4.32,4.09-4.48)$, economic problems $(37.85 \% ; 4.28,4.19-4.34)$, sexually transmitted disease $(3.05 \% ; 4.24,3.93-4.47)$, and OCD $(33.19 \% ; 4.16,4.07-4.23)$ (see Fig. 3 and Tables S5 and S6).

### 3.3 Network Analysis and Sub-syndromes

In the second step we estimated the networks using three different approaches and identifying clusters of events. We included a total of 120 nodes ( 107 events disproportionally reported with impulsivity +13 impulsivity PTs) and 70 nodes $(56+14)$ for the aripiprazole and pramipexole network, respectively. Although the nodes remained constant, edges, clusters, and network properties were different in the three mathematical representations (Table 3, S7, S10-S11, Figs. S1-S8, S11-S16). As expected, the degree centrality was highest for the most common events in Ising and for the rarest in PPMI. The Jaccard similarity was highest between the networks estimated by Ising and $\phi$ and lowest for the networks estimated by $\phi$ and PPMI (half of the links being different). The clustering was most overlapping between $\phi$ -PPMI, followed by $\phi$-Ising and PPMI-Ising, as captured by the purity index. $\phi$ and PPMI tended to present clusters including multiple clusters from the Ising estimated network (Figs. S11-S16).

The three representations were considered as three different perspectives on the same phenomenon and composed into a single visualization for each population (Figs. 4, 5). For a detailed description of the identified clusters, contextualized within the existing literature, see the discussion (Sect. 4.4).

### 3.4 Bayesian Network: The Secondary Impact of Drug-Induced Impulsivity

The Bayesian Network yielded insights into the directional associations between co-reported events (see Fig. 6 and open

![img-2.jpeg](img-2.jpeg)

Fig. 3 Secondary impact of drug-induced impulsivity. The dendrogram shows the events disproportionally reported with aripiprazole- and pramipexole-related impulsivity. Events are gathered by clinical similarity in alternately colored slices, labeled on the outer border with a name and
an icon. Disproportionalities are shown as dots organized in two colored rings, each representing a drug/case population. The dot size is proportional to the percent of reports showing the event, the color is darker for stronger disproportionality (higher median Information Component)
science framework [OSF] repository [59]). High out-degree centrality identified pivotal events that likely heightened the likelihood of reporting other events (Figs. S9-S10). Since this directed network only generates hypotheses, we preferred temporal terminology (i.e., preceding and following) to causal terminology even if no data on actual temporal sequences were included in the analyses.

In pramipexole recipients, anxiety (3.55), emotional distress (2.92), and gambling (2.30) attained the highest outdegree centrality. Anxiety preceded insomnia (with irritability, somnolence, and attention disturbances), stress and depression (with suicide), fear, OCD, and emotional distress. Emotional distress preceded pain and injury (with major depression and economic problems), abnormal thinking and behavior, weight gain, and pathologic gambling. Furthermore, hypersexuality preceded delusional jealousy and
marital difficulties, compulsive shopping preceded stealing behaviors, and hyperphagia preceded weight increase.

In aripiprazole recipients, economic problems (5.97), gambling (4.15), and hyperphagia (2.33) attained the highest out-degree centrality. Economic problems preceded theft, hoarding, divorce, loss of employment, homelessness, suicide, sexual dysfunction, sexually transmitted diseases, and eating disorder. Gambling preceded aggressivity, suicide, cognitive disorders, hyperphagia, and paraphilia. Hyperphagia preceded somnolence and fatigue (with stress, attention disturbances, myalgia, cough), hunger, weight increase (with constipation), obesity (with hypertension), compulsive wandering, and paraphilic disorders. Anxiety preceded depression (with sleep disorders and suicide), fear and panic attacks (with relationship issues), pain and injury (with emotional distress, disability, anhedonia, and

Table 3 Network properties
Aripiprazole (120 nodes)
gambling disorder $(N=2057)$, economic problems (1366), obsessive-compulsive disorders (1198)


Pramipexole (70 nodes)
gambling disorder $(N=1340)$, obsessive-compulsive disorders (553), and hypersexuality (543)


The table shows the network properties for the three networks estimated for aripiprazole and pramipexole, respectively, and for their comparison $(-)$ means that there is also a strong link between the first and last element
PPMI positive pointwise mutual information
${ }^{\mathrm{a}}\left(J(A, B)=\frac{(A \cap B)}{(A \cup B)}\right)$
${ }^{\mathrm{b}}$ Purity $=\frac{1}{N} \sum_{k=1}^{K_{\min }} \max _{k} n_{L, \pi}$, with $K_{\min }$ the minimum clusters and $\max _{k} n_{L, \pi}$ the maximum elements
${ }^{\mathrm{c}}$ A small world has $\omega=\frac{L_{i}}{L}-\frac{C}{C_{i}} \approx 0$ : the shortest path length $L$ is similar to that of an equivalent random network $r$ and the clustering coefficient $C$ is similar to that of an equivalent lattice network $l$
economic problems). Hypersexuality preceded sexual dysfunction, sexually transmitted diseases, unintended pregnancy, and loss of employment. Compulsive shopping preceded eating disorders and economic problems.

## 4 Discussion

### 4.1 Summary and Key Results

We investigated aripiprazole and pramipexole reports to capture the syndromes and sub-syndromes related to
drug-induced impulsivity with dopamine partial agonists and dopamine agonists, respectively.

The event-event disproportionality analysis revealed signs and symptoms commonly reported alongside impulsivity, thus delineating an impulsivity syndrome separately for aripiprazole and pramipexole recipients. The impulsivity syndrome encompassed mainly psychosocial events but also organic conditions.

The network analysis identified meaningful clusters, such as delusional jealousy (also known as Othello syndrome [60]) and dopamine dysregulation syndrome (i.e., the excessive use of levodopa) in pramipexole recipients, and obesity-hypoventilation syndrome (historically Pickwickian

![img-3.jpeg](img-3.jpeg)

Fig. 4 The secondary impact of aripiprazole-induced impulsivity. The network shows the events disproportionally reported with ari-piprazole-related impulsivity and their pattern of co-reporting. Drug-induced impulsivity manifestations are shown as squares and other events as circles. Node colors identify clusters from the Ising estimation, dashed contours for the $\phi$ estimation, and colored contours for the positive pointwise mutual information (PPMI) estimation. The
syndrome) and social issues in aripiprazole recipients. In particular, employing more sensitive network analyses like Phi and PPMI generated more interconnected networks, which identified potential macro-clusters combining several smaller clusters identified by the Ising model.

Crucially, potential causal mechanisms and secondary consequences of drug-induced impulsivity can be highlighted by Bayesian Network methods, providing targets for potential interventions, for example targeting anxiety and economic problems.
link width represents the weight of the links of the Ising, here chosen over the others because links are fewer and more conservative. The layout has been manually adjusted to reduce the overlapping. The layout calculated using a spring model with, as weight, the weights from the individual networks and the average of the weights of the three networks, after rescaling them from 0 to 1 , is shown in the supplementary material

In order to better contextualize and qualify these findings, we now discuss in detail the results of case retrieval, disproportionality analysis, network analysis, Bayesian network, and the limits and conclusions of the study.

### 4.2 Case Retrieval

Our findings align with established risk factors for impulsivity, including male gender and younger age [61, 62], Parkinson's Disease (PD) [63, 64] and depression [65]. Commonly reported impulsivity manifestations included

![img-4.jpeg](img-4.jpeg)

**Fig. 5** The secondary impact of pramipexole-induced impulsivity. The network shows the events disproportionally reported with pramipexole-related impulsivity and their pattern of co-reporting. Drug-induced impulsivity manifestations are shown as squares and other events as circles. Node colors identify clusters from the Ising estimation, dashed contours for the φ estimation, and colored contours for the positive pointwise mutual information (PPMI) estimation. The link width represents the weight of the links of the Ising, here chosen over the others because links are fewer and more conservative. The layout has been manually adjusted to reduce the overlapping. The layout calculated using a spring model with, as weight, the weights from the individual networks and the average of the weights of the three networks, after rescaling them from 0 to 1, is shown in the supplementary material.

### 4.3 Disproportionality Analysis: The Drug-Induced Impulsivity Syndrome

By performing the event–event disproportionality analysis within each drug population separately, comparing reports involving impulsivity with those encompassing various reactions—other than impulsivity—to the same drug, we addressed indication bias and other confounding factors. This comparative analysis served as a rigorous filter,

Fig. 6 The secondary impact of the main manifestations of drug-induced impulsivity, aripiprazole and pramipexole. The subgraphs extracted from the Bayesian Network show the potential direction of the co-reporting relationships between the events, thus providing insight into the direct and indirect impact of drug-induced impulsivity. Nodes linked to hyperphagia, hypersexuality, pathological gambling, and compulsive shopping are represented. Only out-neighbors of order equal or less than 1 are shown here, together with outneighbors of order 2 considered relevant for clinical interpretation
![img-5.jpeg](img-5.jpeg)
allowing us to sift through the complex data and unveil the genuine characteristics associated with impulsivity, as well as those arising from the dynamic interaction between impulsivity and the underlying drug or disease, excluding traits tied solely to the underlying drug or disease.

This approach revealed a complex syndrome, characterized by psychosocial, cognitive, psychosomatic, and metabolic events. The syndromes identified for impulsivity within pramipexole and aripiprazole recipients differ significantly. Multiple factors may contribute to the seemingly higher burden on QoL observed with aripiprazole-induced impulsivity, with functional (or psychosomatic) manifestations and social issues impacting work, relationships, and economics. Pramipexole is primarily administered to older patients with hypodopaminergic conditions, characterized
by motor impairment and reduced motivational drive. These patients, well managed and supported by caregivers because of the later onset and clear neurologic origin of the disease, may experience a mitigated drug-induced impulsivity burden. Conversely, aripiprazole is prescribed to younger patients with mood and psychotic disorders, often linked to hyperdopaminergic states and a pre-existing diathesis for impulsivity. Challenges for caregivers and social support are heightened in these cases due to earlier onset, psychiatric origins, and stigma, potentially leading to a greater burden. Further, over one-third of aripiprazole cases were submitted by lawyers. This may be explained either by a potentially malicious overreporting for legal compensation (cfr., Abilify lawsuit) [66] or by a reaction to underdiagnosis by physicians, who may be hesitant to attribute behavioral changes to

![img-6.jpeg](img-6.jpeg)

Fig. 7 Drug-induced impulsivity syndrome, aripiprazole and pramipexole. The main syndrome, representing one or more strongly interconnected central clusters of symptoms and signs identified through
the medication when underlying psychiatric conditions are present. In reports filed by lawyers, the desire to win legal compensation may have prompted more detailed descriptions of the impact of impulsivity on QoL, or possibly even exaggerated the impact, thus contributing to the observed differences between the two drugs. Intriguingly, there could also be an ascertainment bias, as neurologists prescribing pramipexole may be less aware of psychiatric issues compared to psychiatrists prescribing aripiprazole.

### 4.4 Network Analysis: Sub-syndromes

Network analysis in pharmacovigilance, complementary to other unsupervised approaches such as vigiGroup [67], is a promising tool to detect potential syndromes and subsyndromes, to help the characterization of signals. Employing three estimation methods, the network analysis revealed potential sub-syndromes associated with specific impulsivity expressions in the two populations (Fig. 7). The Ising delineated well-defined clusters, while PPMI and $\phi$
network analysis, is depicted as the central figure. Other potential sub-syndromes are shown on the sides highlighted with a colored square
emphasized inter-clusters relationships. By incorporating various expressions of impulsivity, we anticipated that the central cluster would encompass the key features of impulsivity regardless of its form, whether they act as risk factors or consequences of impulsivity. In both populations, cognitive and mood disorders (e.g., cognitive and memory impairment, bipolar disorder, depression) were included in the central cluster. Notably, they have been recorded as frequently associated with drug-induced impulsivity and contributing to disability development [68]. Obesityhypoventilation syndrome [69], which involves weight gain, cognitive and sleep disorders, and sedation, was consistent in both populations but seemingly heavier in aripiprazole recipients, which also reported obesity, sleep apnea syndrome, hypertension, and metabolic blood alterations (increased lipids, transaminases, and glucose in the blood), supporting the observed link between hyperphagia and diabetes onset [70].

For aripiprazole recipients (Fig. 4), the central cluster also included panic attack and auditory hallucinations, sleep

disorders, decreased appetite, and stress. Stress was further connected to a psychosomatic sub-syndrome involving irritability, migraine, back and abdominal pain, reflux, diarrhea, constipation, and hyperidrosis. Gambling and shopping were linked to pervasive social issues (hoarding, unemployment, homeless, bankruptcy, divorce), theft, and suicidal ideation and attempts (already observed during hyperdopaminergic impulsive states [71]). Hypersexuality was linked to unintended pregnancy, sexually transmitted diseases, and sexual dysfunction.

Among pramipexole recipients (Fig. 5), the central cluster also included apathy, delusion, and economic problems. The dopamine dysregulation sub-syndrome (a manifestation of pathological impulsivity marked by excessive levodopa use [72-74], co-administered with dopamine agonists to better control motor symptoms), involved on and off phenomenon (oscillations in effectiveness and motor and motivational symptoms), excessive levodopa use to avoid off phases, and dopamine agonist withdrawal syndromes (DAWS) upon discontinuation [75]. A cluster aligned with paranoid delusional jealousy (false and unwavering belief in the partner's unfaithfulness), often seen in PD with drug-induced hypersexuality [76] and here characterized by delusional jealousy, hallucinations, irritability, crying, and marital problems. We also found a cluster with fear, pain, stress, anxiety, depression, and suicidal ideation, indicative of the transformation of reward-driven impulsivity into stressful risk-averting compulsivity over time [77]. Finally, the co-reporting of two archetypal compulsive symptoms-body-focused repetitive behaviors and stealing behaviors-was evident.

### 4.5 Bayesian Network: The Secondary Impact of Drug-Induced Impulsivity

This interplay of events within the context of drug-induced impulsivity is intricate and multifaceted. Events reported alongside drug-induced impulsivity may result from impulsivity itself (like financial problems from gambling) or may predispose individuals to impulsivity (e.g., bipolar disorder). Sometimes, events can both trigger and be exacerbated by drug-induced impulsivity (e.g., anxiety [78, 79]). Sometimes events are concomitantly mentioned for precision, such as in cases of semantic overlap (e.g., theft and shoplifting, or injury and brain injury). Events associated with drug-induced impulsivity may even be synonyms for well-known impulsivity expressions (e.g., restlessness, referring to excessive wandering and poriomania), or could be the very reason for prescribing the drug, as seen in the off-label use of aripiprazole and dopamine partial agonists to prevent behavioral and cognitive decline in brain injury [80] or to address dependence [81-85]. We implemented a Bayesian Network to obtain insights into potential directional associations to attempt the formulation on clinically plausible causal sequences. Anxiety
emerged as a central factor, preceding insomnia, irritability, cognitive impairment, stress, injury, pain (linked to disability and economic problems), depression, and even suicidal ideation. Drug-induced impulsivity manifestations appeared to exacerbate each other. Economic problems had the highest out-degree centrality among aripiprazole recipients, preceding theft, relationship difficulties, and suicidal ideation.

The Bayesian Network provides researchers with valuable insights on the pivotal nodes that could be targeted by interventions to disrupt the cascade of events and ameliorate the secondary impact of drug-induced impulsivity. It also highlighted secondary ramifications of main impulsivity manifestations: hypersexuality precedes marital problems through delusional jealousy in pramipexole recipients, while it precedes unintended pregnancy and sexually transmitted diseases in aripiprazole recipients; hyperphagia precedes weight increase in pramipexole recipients and obesity, somnolence, and cognitive impairment in aripiprazole. Finally, the Bayesian Network seems to support the higher secondary impact of drug-induced impulsivity in aripiprazole recipients.

### 4.6 Clinical Considerations

This study underscores the significant burden of druginduced impulsivity, which encompasses biological, psychological, and social consequences. Clinical outcomes related to such impulsivity are broad and multifaceted, often manifesting as complex syndromes rather than isolated events. These syndromes can have prognostic and therapeutic implications. For instance, impulsivity in the form of hyperphagia can lead to metabolic syndrome and sleep disorders, in the form of hypersexuality to sexually transmitted diseases and unintended pregnancies, and in the form of pathological gambling and compulsive shopping to severe social issues such as job loss, bankruptcy, and divorce. Furthermore, the impact of aripiprazole-induced impulsivity appears more severe compared to pramipexole, potentially due to differences in the patient populations using these medications.

Given the substantial burden associated with druginduced impulsivity, it is crucial to meticulously review patients' medical histories. Factors such as young age, male gender, pre-existing mood disorders, and family history of dependencies should be considered red flags, necessitating heightened vigilance. When impulsivity is detected, the recommended course of action is to taper the offending medication and switch to an alternative. However, this pharmacological switch is not always feasible or sufficient, and in this case there is no consensus among experts on the optimal strategy [86]. In such cases, the Bayesian Network can be an invaluable causal discovery tool for identifying critical events that might be targeted by interventions to

prevent the chronicization and exacerbation of drug-induced impulsivity. For example, effective management strategies might include monitoring and addressing anxiety, providing financial guidance, or appointing legal guardianship to prevent wasteful spending, thus targeting critical events in the evolution of the syndrome. Additionally, addressing marital issues is crucial, as they are linked to early placement in nursing homes and poorer prognoses [24, 87]. Specifically, tackling delusional jealousy and economic problems, which often precede marital issues, may be vital for preserving the well-being of pramipexole recipients.

In conclusion, this study highlights the necessity for comprehensive clinical evaluations and individualized management plans for patients at risk of or exhibiting drug-induced impulsivity. Proactive measures and targeted interventions, driven by the conceptualization of ADRs as networks of causally interacting events, can mitigate the adverse outcomes associated with these medications, improving overall patient prognosis and QoL.

### 4.7 Limitations and Further Developments

While this study provides valuable insights into the intricate interplay of events related to drug-induced impulsivity and its subsequent implications, it is crucial to acknowledge its limitations.

Individual case safety reports, while uniquely granting access to a patient's perspective, are susceptible to biases such as under-reporting, missing data, and unverified reliability, preventing reliable incidence or prevalence estimates. The high contribution of reports from lawyers may have influenced the higher psychosocial impact attributed to aripiprazole-induced impulsivity. Nonetheless, this study sets the foundation for further studies and a potential score to assess the impact of ADRs on QoL.

Limitations in network analysis methodologies adopted include the Ising estimation's assumptions (pairwise interaction, linear effects, and binary variables), and the inability to account for time and severity in symptom manifestation. The incorporation of negative links could facilitate a more nuanced separation of symptoms that infrequently co-occur. The Bayesian Network lacks bidirectional relationships and cyclic feedback loops and would require the inclusion of all shared causes between any two events (causal Markov condition) to achieve its full capacity to illuminate causality. These limitations could be rectified by integrating clinical longitudinal data and embedding temporal aspects into the network analysis (see Fusaroli et al for similar, more detailed, considerations [88]). Moreover, the used models assume that an event can only be part of a sub-syndrome, while we know that in fact the same event can be a manifestation of multiple subsyndromes. In the future, it could be an opportunity for the integration of network analysis with vigiGroup [67], a latent class expectation maximization model developed by Uppsala Monitoring Centre, which instead allows for one event to be part of multiple sub-syndromes (but not for one report to describe multiple sub-syndromes).

Looking ahead, a broader definition of drug-induced impulsivity could improve sensitivity in case retrieval. Conditions such as suicide attempts, hypersomnia, obsessive-compulsive symptoms, explosive anger, personality changes, disturbance in attention, and drug dependence might represent different expressions of this underdefined condition, warranting further exploration [10, 74]. Additionally, aripiprazole and pramipexole may not fully represent their entire drug classes. This could be due to their use in different populations or their distinct pharmacological activities. In the future, it would be valuable to conduct network analyses on newer drugs (e.g., brexpiprazole and cariprazine) as more reports become available.

## 5 Conclusion

The profound impact of drug-induced impulsivity reverberates across patients and their families, encompassing psychosocial challenges and organic complications such as metabolic syndrome (in the case of hyperphagia), and sexual health issues (in the case of hypersexuality). Recognizing these potential consequences is crucial for informed pharmacological management and diligent patient monitoring. Network analysis reveals intriguing co-reporting patterns among adverse events, identifying potential subsyndromes such as obesity-hypoventilation syndrome with hyperphagia and the association of hypersexuality with delusional jealousy in pramipexole recipients and unintended pregnancy and sexually transmitted diseases in aripiprazole recipients. Our parallel approach effectively avoids the risk of disease-related diathesis compromising analytical integrity, enhancing the robustness of our findings.

Central to our findings is the pivotal realization that drug reactions rarely occur in isolation; instead, they manifest as syndromes with diverse signs and symptoms. These can be direct reactions to the drug itself, secondary consequences, risk factors for the reaction, or comorbidities. Causal chains and loops can contribute to symptom aggravation and chronicity. Identifying syndromes and sub-syndromes, combining network strategies with traditional techniques and clinical judgment, proves a potent strategy for delving into the secondary impact of ADRs and fostering heightened awareness within clinical practice.

In summary, the intricate relationships between signs and symptoms, coupled with the insights from the Bayesian Network, underscore the multifaceted nature of druginduced impulsivity. More significantly, it equips research, and secondarily clinicians, with indispensable tools to

identify potential intervention points, decipher causal sequences, and mitigate the cascading secondary effects associated with drug-induced impulsivity. In doing so, this study contributes to advancing our comprehension and management of drug-induced impulsivity, ultimately enhancing the well-being and care of affected patients.

Supplementary Information The online version contains supplementary material available at https://doi.org/10.1007/s40264-024-01471-z.

Acknowledgements MedDRA ${ }^{\circledR}$, version 25.0 was developed under the auspices of the International Council for Harmonization of Technical Requirements for Pharmaceuticals for Human Use. Part of the work was presented orally at the SIF congress, 2023, in Rome. Erika Polizzi made the vignettes in Fig. 7.

## Declarations

Funding Open access funding provided by Alma Mater Studiorum Università di Bologna within the CRUI-CARE Agreement.

Conflict of interest The authors declare no conflict of interest specific for this research. Fabrizio De Ponti is an Editorial Board member of Drug Safety. Fabrizio De Ponti was not involved in the selection of peer reviewers for the manuscript nor any of the subsequent editorial decisions.

Ethics approval Not applicable because spontaneous reports of the FAERS are anonymous and publicly available.

Consent to participate Not applicable because spontaneous reports of the FAERS are anonymous and publicly available.

Consent for publication Not applicable because spontaneous reports of the FAERS are anonymous and publicly available.

Availability of data and material The data we used come from the FDA Adverse Event Reporting System (FAERS) and is made publicly available by the FDA as quarterly data downloadable at https://fis.fda.gov/ extensions/FPD-QDE-FAERS/FPD-QDE-FAERS.html. The algorithm for cleaning FAERS data is open-source at https://github.com/fusar olimichele/DiAna, and the cleaned database is available on an OSF repository [89] and through the R package DiAna [40].

Code availability The code for the project is available on an OSF repository [59], the function for the Ising network is also available in the DiAna package (cfr. "network_analysis()") [40]. Analyses were performed using R (version 4.2.1) [90] and Python (version 3.8.16) [91]. We relied on several essential packages for network analysis: IsingFit [51], igraph [92], psych [93], and bnlearn [38].

Author contributions MF, SP, LM, conceptualized and designed the study. MF, SP, LM developed the methodology. The formal analysis was performed by MF, SP, LM, VG. MF, SP, VG performed the visualization. MF, SP, LM, VG wrote the original draft. All the authors strongly contributed to the interpretation of results, and to the review and editing of the draft. All the authors read and approved the final version.

Open Access This article is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License, which permits any non-commercial use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the
original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by-nc/4.0/.

# Authors and Affiliations 

Michele Fusaroli ${ }^{1}$ (D) $\cdot$ Stefano Polizzi ${ }^{2} \cdot$ Luca Menestrina ${ }^{3} \cdot$ Valentina Giunchi ${ }^{1} \cdot$ Luca Pellegrini ${ }^{4,5} \cdot$ Emanuel Raschi ${ }^{1} \cdot$ Daniel Weintraub ${ }^{6,7} \cdot$ Maurizio Recanatini ${ }^{3} \cdot$ Gastone Castellani ${ }^{2} \cdot$ Fabrizio De Ponti ${ }^{1} \cdot$ Elisabetta Poluzzi ${ }^{1}$

Michele Fusaroli
michele.fusaroli2@unibo.it
1 Pharmacology Unit, Department of Medical and Surgical Sciences, University of Bologna, Bologna, Italy
2 Unit of Medical Physics, Department of Medical and Surgical Sciences, University of Bologna, 40138 Bologna, Italy
3 Department of Pharmacy and Biotechnology, Alma Mater Studiorum-University of Bologna, Via Belmeloro 6, 40126 Bologna, Italy

4 Hertfordshire Partnership NHS University Foundation Trust, Highly Specialised OCD and BDD Service, Rosanne House, Parkway, Welwyn Garden City, Hertfordshire, UK
5 School of Life and Medical Sciences, University of Hertfordshire, Hatfield, Hertfordshire, UK
6 Perelman School of Medicine, University of Pennsylvania, Philadelphia, PA, USA
7 Parkinson's Disease Research, Education and Clinical Center (PADRECC), Philadelphia Veterans Affairs Medical Center, Philadelphia, PA, USA