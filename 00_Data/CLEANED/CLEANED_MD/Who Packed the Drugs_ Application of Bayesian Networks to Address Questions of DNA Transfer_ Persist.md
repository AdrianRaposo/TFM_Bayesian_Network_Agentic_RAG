# Article 

## Who Packed the Drugs? Application of Bayesian Networks to Address Questions of DNA Transfer, Persistence, and Recovery from Plastic Bags and Tape

Ane Elida Fonnelop ${ }^{1, * *}$, Sara Faria ${ }^{2, \dagger}$, Gnanagowry Shanthan ${ }^{1}$ and Peter Gill ${ }^{1,3}$<br>check for updates<br>Citation: Fonnelop, A.E.; Faria, S.; Shanthan, G.; Gill, P. Who Packed the Drugs? Application of Bayesian Networks to Address Questions of DNA Transfer, Persistence, and Recovery from Plastic Bags and Tape. Genes 2022, 13, 18. https:// doi.org/10.3390/genes13010018<br>Academic Editor: Emiliano Giardina

Received: 8 December 2021
Accepted: 17 December 2021
Published: 22 December 2021
Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## 0

Copyright: (c) 2021 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 Department of Forensic Sciences, Oslo University Hospital, 0372 Oslo, Norway; rmgnsa@ous-hf.no (G.S.); peterd.gill@gmail.com (P.G.)
2 Faculty of Sciences, University of Lisbon, 1749-016 Lisbon, Portugal; sarafaria1998@outlook.pt
3 Department of Forensic Medicine, University of Oslo, 0315 Oslo, Norway

* Correspondence: rmanfo@ous-hf.no
$\dagger$ Contributed equally to this work.


#### Abstract

When DNA from a suspect is detected in a sample collected at a crime scene, there can be alternative explanations about the activity that may have led to the transfer, persistence and recovery of his/her DNA. Previous studies have shown that DNA can be indirectly transferred via intermediate surfaces and that DNA on a previously used object can persist after subsequent use of another individual. In addition, it has been shown that a person's shedder status may influence transfer, persistence, prevalence, and recovery of DNA. In this study we have investigated transfer persistence and recovery on zip-lock bags and tape, which are commonly encountered in drug cases and how the shedder status of the participants influenced the results. A probabilistic framework was developed which was based on a previously described Bayesian network with case-specific modifications. Continuous modelling of data was used to inform the Bayesian networks and two case scenarios were investigated. In the specific scenarios only moderate to low support for $H_{p}$ was obtained. Applying a continuous model based on the profile quality can change the LRs.


Keywords: transfer; persistence; activity; Bayesian networks

## 1. Introduction

In criminal cases, when DNA from a suspect is detected in samples collected from drug wrappings, there can be alternative explanations about the activity that may have led to the transfer, persistence, and recovery of his/her DNA. Often these explanations involve indirect transfer from an object they have used (e.g., bag or clothing), or perhaps the suspect has been in contact with the object in a situation not related to the crime. The hierarchy of propositions describes the different levels of evaluation of the evidence given propositions at sub-source, source, activity, and offence level [1-3]. The guidelines from the International Society for Forensic Genetics (ISFG) DNA commission provide advice on evaluation and the formulation of propositions and recommend the evaluation of results at activity level in the light of the alternative propositions of the case and calculating a likelihood ratio (LR) [2]. A recommended tool to aid in the evaluation of evidence is Bayesian networks (BNs) [4] and examples of how they can be constructed and used are widely available [5,6]. To construct a BN, the relevant variables and their respective probabilities are required. Extensive research on transfer persistence, prevalence, and recovery (TPPR) of DNA has been conducted over the past 10 years [7], although knowledge bases that can be utilised for routine casework are currently lacking.

The indirect transfer of DNA is dependent upon several variables including: the amount of DNA present, time since initial contact, number of contacts and the type of surface of the objects involved [8-10]. DNA from a person who previously handled an object can be detected for some time after the object has been handed to a new user [10].

However, it is more likely that DNA from the most recent user of the object will become the major contributor over time [11,12]. Van Oorschot et al. [12] observed an average $50 \%$ drop in the DNA from the previous user immediately after handling by a new user when the surface was hard and non-porous. Mayuoni-Kirshenbaum et al. [13] studied the persistence of DNA from a person cutting aluminium foil when the foil was subsequently used for lock picking by another individual and only detected DNA from the cutter in $1 / 25$ cases while the lock-picker was detected in $9 / 25$ samples.

It has previously been demonstrated that individuals have a different propensity to transfer DNA to handled items (shedder status); shedder status is consistent over years, and it can influence transfer probabilities [14-16]. However, the classification method has been debated and a need to introduce an intermediate shedder category (between high and low) has been demonstrated [15-17].

The aim of this paper is to provide a dataset along with a probabilistic framework to interpret DNA evidence at activity level. We present two specific scenarios related to DNA evidence in drug related cases. The first considers direct and indirect transfer to a zip-lock drugs bag that has been stored in a personal bag, whilst the second considers the persistence of DNA from a previous user of tape which was used to pack drugs by a second individual (the cardboard drug wrap experiment). The results from both experiments were examined in the light of the participant's shedder status. A probabilistic framework was developed which was based on a previously described Bayesian network [5] with case-specific modifications. Previous work has usually applied discrete models to measure simple presence/absence of DNA that may be attributed to a person of interest (POI). A continuous model was demonstrated by Gill et al. [6], based upon sub-source likelihood ratios, and this was recently complemented with a method using mean $\overline{R F U}$ (peak height) instead of sub-source likelihood ratio [18]. Here we provide a demonstration of continuous modelling of indirect and direct transfer with two case examples. Continuous models are the preferred method with mixture analysis [19] because they take more information into account. It is natural that activity level assignments should take the same route.

The paper is structured as follows: in Sections 3.1-3.4 there is an empirical description of the data analysis, followed by probabilistic analysis using Bayesian networks of the zip-lock drugs bag experiment (Section 3.5.1), and the tape/cardboard drug wrap experiment (Section 3.5.2).

# 2. Materials and Methods 

This project was approved by the data protection officer at Oslo University Hospital, all participants have given informed consent prior to participating in the experiments. Twenty participants were recruited and participated in all experiments.

### 2.1. Direct and Indirect Transfer to Zip-Lock Drugs Bags

Each participant was provided with a kit for the experiments containing two DNA-free (exposed to UV light for 10 min on each side) zip-lock bags ( $16.7 \times 10 \mathrm{~cm}$ ). One of the zip-lock bags contained a 15 mL centrifuge tube (VWR) filled with water to function as a weight.

### 2.1.1. Direct Transfer

Participants were instructed to wait at least one hour after washing hands/using antibacterial hand wash, after which they touched the upper surface of the zip-lock bag for about 30 s by opening and closing it. They were then asked to repeat this process with the same bag two more times (total of three handlings). When the procedure was completed, participants were instructed to place the zip-lock bag into a new labelled envelope. The dataset generated is labelled E1 and is available in the Supplementary Material S2.

# 2.1.2. Indirect Transfer 

Participants were instructed to use their own personal bag/purse/backpack for this experiment. They were instructed to put on a pair of new disposable gloves before placing the zip-lock drugs bag containing the weight into their personal bag (which did not contain anything else during the experiment) and leave it there for 24 h ; they were also instructed to move the personal bag during this period, e.g., carry it with them to work and home. After the 24 h had passed, the zip-lock drugs bag was removed, whilst wearing clean gloves, and placed into a new labelled envelope. The dataset generated is labelled E2 and is available in Supplementary Material S2.

### 2.2. Persistence and Detection of DNA from a Previous User of a Tape Roll

In this experiment participants were divided into pairs. Participant B was given a DNA-free (treated with UV light for 20 min on each side) roll of tape. The participants were instructed to wait at least 1 h after washing hands/using antibacterial liquid; then the tape was handled for 1 min by passing it from one hand to another, stroking the sides of the tape roll towards the palm of the hands; use of the tape was mimicked by tearing off a small piece. The roll of tape was placed in a labelled envelope and passed to participant A after a minimum 10 days in storage. Participant A was provided with a piece of clean cardboard (approx. $6 \times 10 \mathrm{~cm}$ ) (UV treated on each side for 20 min ), to mimic a pack of drugs. He/she was instructed to wrap the piece of cardboard with the tape (previously handled by B). The "drug wrap" was placed in a new labelled envelope. Each of the 20 participants contributed twice to the experiments swapping the roles of A and B, giving a total of 20 wrapped cardboards. The data generated is available in Supplementary Material S2.

### 2.3. Shedder Status

Participants were asked to hold a plastic tube ( 15 mL centrifuge tube high performance tube, VWR) for 10 s in their dominant hand, at least one hour after washing hands/using antibacterial liquid. The experiments were repeated 3 times, with a new clean tube; there was a gap of at least three hours between each experiment. The data generated is available in Supplementary Material S2.

### 2.4. Sample Processing

Samples were collected with a moistened (one drop of water) swab (Tubed Sterile Dryswab, Medical Wire). The sampling was performed on: (a) zip-lock bags: the top 3 cm of the outside and inside (including lock) of the zip-lock bags; (b) wrapped cardboard: the full outside and edges of the tape around the cardboard; (c): tubes: the full body of the 15 mL centrifuge tubes (not lids). One negative control sample was collected from all items (tape, cardboard, zip-lock bag and tube). For the samples collected from zip-lock bags and wrapped cardboard, the tips of the swabs were cut, placed in 1.5 mL Eppendorf tube and stored at $-20^{\circ} \mathrm{C}$ until further processing to avoid degradation. Samples collected from tubes were stored in ventilated evidence bags to dry before the tips of the swabs were cut directly into single PCR-tubes for a direct PCR analysis.

Samples collected from zip-lock bags and wrapped cardboard were extracted by the $5 \%$ Chelex procedure [20] (no prior incubation with water) where $200 \mu \mathrm{~L}$ Chelex (Bio-Rad, Hercules, CA, USA) was added to swabs. All samples were quantified with PowerQuant (Promega, Madison, WI, USA) on the 7500 Real-Time PCR system (ThermoFisher, Waltham, MA, USA) using the manufacturers' recommendations. PCR amplification was carried out using the PowerPlex Fusion 6C System kit (Promega, Madison, WI, USA) as recommended by the manufacturer ( 1 ng template, $25 \mu \mathrm{~L}$ reaction volume and 29 amplification cycles). Samples that had lower concentrations than the recommended template amount were amplified with the maximum template volume of $15 \mu \mathrm{~L}$. For the shedder experiment, the PCR reaction mix was added directly to the tube containing the swab tips. Amplification was carried out using a Veriti 96-Well Thermal Cycler (ThermoFisher, Waltham, MA, USA). Samples were injected on the Applied Biosystems 3500 xL Genetic Analyzer at 1.2 kV

for 24 s . The results were analysed using the GeneMapper ID-X Software version 1.6 (ThermoFisher, Waltham, MA, USA). The analytical threshold (AT) for alleles was set to 100 RFU.

# 2.5. Data Analysis 

Results were analysed using R version 4.0.3 with the package tidyverse version 1.3.0. Likelihood ratios and mixture proportions were calculated using EuroForMix version 3.2.0 using propositions shown in in Equation (1), where $U$ corresponds to unknown contributors, necessary to explain all alleles present. The average $\operatorname{RFU}(\overline{R F U})$ for a contributor was calculated by dividing the total $\operatorname{RFU}\left(R F U_{\text {tot }}\right)$ by the number $(n)$ loci (23, except amelogenin), Equation (2). If the sample was a mixture, the contribution from the POI was found by multiplying $\overline{R F U}$ for the sample by the mixture proportion $\left(M_{x}\right)$. If a sample was diluted then the result was multiplied by a dilution factor $\left(d_{l}\right)$.

$$
\begin{gathered}
L R=\frac{\operatorname{Pr}\left(E \mid H_{p}: P O I+U_{1}\right)}{\operatorname{Pr}\left(E \mid H_{d}: U_{1}+U_{2}\right)} \\
\overline{R F U}_{P O I}=M_{x} \times \frac{R F U_{t o t}}{n} \times d_{l}
\end{gathered}
$$

### 2.5.1. List of Variables

We follow the notation used by Gill et al. [6] (Section 4), summarised here:
$t$ is the probability of direct transfer, persistence and recovery of DNA from the POI (under $H_{p}$ only).
$t^{\prime}$ is the probability of direct transfer, persistence and recovery of DNA from an unknown contributor (under $H_{d}$ only).
b is the probability of background DNA, based on observations, and is applied under both $H_{p}$ and $H_{d}$. Background DNA is present from unknown sources and unknown activities. It can be described as "foreign" (non-self). For further details we refer to Section 3.2 in [6]. s is the probability of transfer, persistence and recovery; in experiment 1, this is indirect transfer under $H_{p}$ and $H_{d}$, and in experiment 2, it is direct transfer under $H_{d}$ only.
Suffixes are applied to described probabilities of an event given a particular contributor, e.g., $t_{A}$ refers to the probability of direct transfer, persistence and recovery of DNA from contributor A.

### 2.5.2. Notation Relating to the Experiments

Experiment 1: zip-lock drugs bag
$E 1_{\text {dbag }}$ : Dataset from the zip-lock drugs bag; direct transfer
$E 2_{\text {pbag }}:$ Dataset from the personal bag experiment; indirect transfer
$\overline{R F U}_{E 1 \text { dbag }}:$ Lognormal distribution of mean RFU from $E 1_{\text {dbag }}$ data; direct transfer
$\overline{R F U}_{E 2 \text { pbag }}:$ Lognormal distribution of mean RFU from $E 2_{\text {pbag }}$ data; indirect transfer Experiment 2: Tape/cardboard drug wraps
$C 1_{\text {pack }}:$ Dataset from drugs wrapper; direct transfer
$C 2_{\text {tape }}:$ Dataser from the tape handler; direct transfer
$\overline{R F U}_{C 1 \text { pack }}:$ Lognormal distribution of mean RFU from $C 1_{\text {pack }}$ data; direct transfer
$\overline{R F U}_{C 2 \text { tape }}:$ Lognormal distribution of mean RFU from $C 2_{\text {tape; }}$ data; direct transfer General
$\overline{R F U}_{A}$ : the observed $\overline{R F U}$ value from contributor A
$\overline{R F U}_{B}$ : the observed $\overline{R F U}$ value from contributor B
$\overline{R F U}_{\text {unknown }}:$ the observed $\overline{R F U}$ value from an unknown contributor

### 2.5.3. Distribution Fitting

Log-normal distributions were fitted to the data using the R package fitdistrplus using function lnorm. The method is described in detail in Supplementary Material S1. The

probability of background for experiment 1 was modelled using the same lognormal parameters calculated for indirect transfer data $\overline{R F U}_{E 2 p b a g}$, as described in the Supplementary Material S1 (Section S4.4.1). To carry out sensitivity analysis, $1000 \times$ bootstraps (with replacement) were taken of datasets (Supplementary Material S2). For each bootstrap, a new set of log-normal parameters (mean log and SD log) were calculated using the fitdistrplus R package using the lnorm function. The probability distributions were used to substantiate the Bayesian networks described in Sections 3.5.1 and 3.5.2. The programming of these networks was carried with R-code using the formulae described in Sections 3.5.1 and 3.5.2.

# 3. Results 

### 3.1. Direct and Secondary Transfer to Zip-Lock Drugs Bags

The DNA from the POI could be detected in the samples collected after direct handling of a zip-lock drugs bag and after indirect transfer to the drugs bag from storage in a previously used personal bag. More alleles matching the POI along with higher DNA quantities were generally observed in the direct transfer experiment $\left(E 1_{d b a g}\right)$ compared with indirect transfer from inside a personal bag $\left(E 2_{p b a g}\right)$. Generally, the $\overline{R F U}_{P O I}$ was higher in $E 1_{\text {dbag }}$, but a few occurrences of higher $\overline{R F U}_{P O I}$ were observed in $E 2_{p b a g}$ (Figure 1).
![img-0.jpeg](img-0.jpeg)

Figure 1. Boxplots displaying (a) the measured DNA concentrations ( $\mathrm{ng} / \mu \mathrm{L}$ in $200 \mu \mathrm{~L}$ ), (b) the number of detected allele's matching the POI and (c) the $\overline{R F U}_{P O I}$ for the samples in the $E 1_{\text {dbag }}$ (direct) and $E 2_{\text {pbag }}$ (indirect) data.

In the direct transfer experiment four full and seven partial profiles were detected, while six samples only displayed six or less alleles and four samples had no results. Only one sample contained (two) unknown alleles. From the indirect transfer experiment three full and two partial profiles corresponding to the POI were detected. Four samples only displayed five or less alleles and ten samples had no profiling results. One sample was a mixture with 21 unknown alleles, and one sample was a partial profile with alleles corresponding to a child of the participant. The most frequently used type of personal bag used was a backpack but a large proportion of these samples ( $7 / 11$ ) had no results. The full dataset can be found in the Supplementary Material S2. The highest $\overline{R F U}$ values on the zip-lock drugs bags were observed after storage in a personal purse/handbag, (Figure 2).

A few participants (1 and 2, respectively) used a personal PC and shopping bag to store the zip-lock drugs bags. Most participants reported using the personal bag frequently or every day, while two participants reported rarely using their personal bags. No alleles were detected on zip lock bags after storage in rarely used personal bags.
![img-1.jpeg](img-1.jpeg)

Figure 2. Dot plot displaying the $\log _{10} \overline{R F U}$ values detected in the samples collected from zip-lock drugs bags after storage in a previously used personal bag (backpack, PC bag, purse/handbag or shopping bag).

# 3.2. Persistence and Detection of DNA from a Previous User of a Tape Roll Used to Wrap Drugs 

In samples collected from wrapped cardboard, DNA from both the person who previously handled the tape $\left(\mathrm{C} 2_{\text {tape }}\right)$ and the person who packed the tape around the cardboard $\left(\mathrm{C} 1_{\text {pack }}\right)$ could be detected. However, the quality of the profile, peak heights of detected alleles and mixture proportions varied between the cardboard wrapper and the tape handler (Figure 3).
![img-2.jpeg](img-2.jpeg)

Figure 3. Boxplot displaying (a) proportion of unique alleles, (b) the mixture proportion and (c) $\overline{R F U}$ values corresponding to the wrapper $\left(\mathrm{C} 1_{\text {pack }}\right)$ and the handler $\left(\mathrm{C} 2_{\text {tape }}\right)$ of the tape.

Three samples had no profiling results and for an additional three samples only four alleles were detected. Seven samples were full or partial profiles corresponding to the drugs wrapper (C1), five samples were mixtures of C1 and C2. For three of these mixtures, C1 was the major contributor, whilst in the last two, the contributions were of equal proportions. Two samples were partial profiles with alleles corresponding to C2. The full dataset can be found in the Supplementary Material S2.

### 3.3. Shedder Status

The total RFU values (RFU_{tot}) from the direct PCR analysis varied from 0 to 458,705, variation was greater between individuals than within the samples from one individual (ANOVA, p = 0.04), Figure 4. However, some individuals, especially those that deposited low amounts of DNA, displayed lower variation. Individuals were classified as low, medium or high shedders based on the criteria defined by Johannessen et al. [15] with the following adjustments according to the observed values of the current dataset: high shedder class was assigned to participants that had two out of three samples above the average RFU_{tot} (62,520) and two out of three samples with 20 out of 24 full loci. Low shedder class was assigned to participants where all samples were below 8000 RFU_{tot} and two out of three with negative or partial profiles. The rest were classified as medium shedders. This resulted in 4 high, 11 medium and 5 low shedders (Figure 3). The full dataset can be found in the Supplementary Material S2.

![img-3.jpeg](img-3.jpeg)

**Figure 4.** Scatter plot showing the total RFU_{tot} values (multiplied by M_{s} if sample was a mixture) for each sample collected from each participant and according to their shedder status, high (red circle), medium (blue square) low (green triangle). The average RFU_{tot} (6.25E+04) and low shedder limit of 8.00E+03 RFU_{tot} are represented with the dotted and straight lines, respectively.

DNA from unknown contributors was detected in 30/90 samples, the average $M_{x}$ proportion from unknown contributors was highest for low shedders, Table 1.

Table 1. Detection of unknown alleles in the shedder samples and the proportion of unknown DNA detected for the three different shedder classes.


# 3.4. Transfer in Relation to Shedder Status 

Data from experiment 1 (direct transfer to zip-lock drugs bag) showed highest transfer rates with high shedders (Figure 5). More variation was observed in the medium shedder group, than for the low and high shedders. The trend is not as obvious for experiment 2 (indirect transfer from personal bag to zip-lock drugs bag). In fact, the best quality profile was detected in a sample from a low shedder participant. Based on the number of samples in each group, there were insufficient data to evaluate the effect using Bayesian networks described in Section 3.5.1.
![img-4.jpeg](img-4.jpeg)

Figure 5. Boxplot displaying the $\log 10 \overline{R F U}$ detected in the direct transfer experiment $\left(E 1_{d b a g}\right)$ and indirect transfer from personal bag $\left(E 2_{p b a g}\right)$ according to the participants' shedder classification.

Data from persistence and detection of DNA from a previous user of a tape roll experiment showed that low shedders only provided low quality profiles and that higher quality profiles were provided by high shedders. Medium shedders provided both high and low quality results. (Figure 6).

![img-5.jpeg](img-5.jpeg)

Figure 6. Boxplot displaying the $\log 10 \overline{R F U}$ for the drugs wrapper $\left(\mathrm{C} 1_{\text {pack }}\right)$ and the previous handler $\left(\mathrm{C} 2_{\text {tape }}\right)$ of the tape according to the shedder classification of the participants.

# 3.5. Case Examples 

To demonstrate the potential use of the datasets obtained, we will use two fictive case examples that are based on actual experiences from case work, using a Bayesian network to evaluate the evidence.

### 3.5.1. Potential DNA Transfer from Storage in a Personal Bag

## Case Circumstances

1. A large depot of drugs was found at a hideout;
2. The drugs were packed in zip-lock bags and placed in a black gym bag;
3. Upon questioning, person A claims to have no knowledge of the drugs. However, he recognizes a gym bag that the drugs had been stored in and claims that it used to belong to him but it was lost or stolen two weeks previously.

## DNA Analysis

DNA samples were collected from the outside and opening of the zip-lock bag
4. Example 1: Result is a full DNA profile of a single individual. There is a candidate in the national DNA database who is identified as person A;
5. Example 2: Result is a mixture of two individuals. There is a candidate in the national DNA database who is identified as person A but there is no candidate for the second individual.

## Propositions

Sub-source likelihood ratios were calculated for both contributors using EuroForMix [21], although this information was not used in any further analysis. To proceed with activity level analysis, it is assumed that the sub-source LR is sufficient for a court to agree the identity of a POI [2].

The alternative activity level propositions (for both examples) are as follows:
$H_{p}$ : The suspect packed the drugs;
$H_{d}$ : The suspect has no relation to the drugs but was the owner of the gym bag which was stolen two weeks previously. An unknown individual packed the drugs.

The BN used to instantiate probabilities is identical to that described by [6] (Supplement S1), except that the title of the nodes are changed to represent the case circumstances (Figure 7). Log-normal distributions were used to calculate drug bag (direct) and personal bag (indirect) TPR probabilities, conditioned upon values of $\overline{R F U}_{A}$ modelled with $\overline{R F U}_{E 1 d b a g}$ and $\overline{R F U}_{E 2 p b a g}$ distributions respectively. $\overline{R F U}_{\text {unknown }}$ was modelled with $\overline{R F U}_{E 2 p b a g}$ distribution (Table 2), the assigned probabilities (Figure 8) were subsequently used in the BN (Figure 7) to calculate the results. To carry out sensitivity analysis, $1000 \times$ bootstraps (with replacement) were taken of the $\overline{R F U}_{E 1 \_d b a g}$ and $\overline{R F U}_{E 2 \_p b a g}$ data (Supplementary Material S2) to provide 1000 new sets of data. For each bootstrap, a new set of log-normal parameters (mean log and SD log) were calculated using the fitdistrplus R package and the variation was represented by percentiles in Table 3.
![img-6.jpeg](img-6.jpeg)

Figure 7. Bayesian network for the "drugs stored in gym bag" example showing data sets and models used to instantiate the nodes.

Table 2. Relationship of probabilities of DNA transfer from individuals A (POI) and U (unknown), showing the datasets that were used to calculate probability distributions, along with the BN nodes instantiated. See nomenclature Section 2.5.1 for definitions of probabilities.


![img-7.jpeg](img-7.jpeg)

Figure 8. Comparison of probabilities of direct, indirect and background TPPR for the zip-lock drugs bag example. Direct transfer was modelled from $\overline{R F U}_{E 1 d b a g}$; personal bag (indirect transfer) was modelled from $\overline{R F U}_{E 2 p b a g}$ data and background was also modelled from $\overline{R F U}_{E 2 p b a g}$ data, with adjusted $k=0.95$ (the proportion of observations with no background) in order to scale results as described in Supplementary Material S1.

Table 3. Activity level likelihood ratios where only contributor A is recovered, with sensitivity analysis, showing 2.5-97.5 percentiles. The median ( 50 percentile) values are those that are reported. Results for the discrete model are shown in the top row; continuous models conditioned upon $\overline{R F U}_{A}>x$ are shown in remaining rows.


Derivation of the formulae used in the calculations are the same as those described in Supplementary Material S1 of Gill et al. [6]. Likelihood ratios were calculated as shown in Formulae 3-5 (nomenclature in Table 2): (a) Only the POI (A) is observed

$$ L R=\frac{\left(s\left(1-t_{A}\right)+t_{A}\right) \times(1-b)}{s \times\left(1-\operatorname{Pr}\left(U_{d}\right)\right)} $$

(b) POI (A) and unknown is observed

$$
L R_{a}=\frac{\left(s\left(1-t_{A}\right)+t_{A}\right) \times b}{s \times \operatorname{Pr}\left(U_{d}\right)}
$$

(c) Probability of recovery of DNA from an unknown contributor

$$
\operatorname{Pr}\left(U_{d}\right)=t^{\prime} b+t^{\prime}(1-b)+b\left(1-t^{\prime}\right)=t^{\prime}+b\left(1-t^{\prime}\right)
$$

There were only three observations of background (datasets $E 1_{\text {dbag }}$ and $E 2_{\text {pbag }}$ ). Background is from indeterminate (unknown) sources and can comprise both direct and indirect transfer. Here, it was modelled using $\overline{R F U}_{E 1 p b a g}>x$ data (where $x$ is a threshold value; first column in Table 3), except that the model was scaled relative to $k=1-\operatorname{Pr}(b)$ as described in the Supplementary Material S1; where $k$ is the proportion of observations where no background was observed. From experimental observation $\operatorname{Pr}(b)=0.05$ and $k=0.95$.

Two possible outcomes of the DNA results were analysed in detail. Either a profile from the POI individual A is recovered, or A is recovered in combination with an unknown contributor which forms the basis of the proposition under $H_{d}$, else the unknown contributor is background under $H_{p}$.

# Contributor A Recovered Alone 

When contributor A is recovered alone, Table 3 shows that the median (50 percentile) LRs always favour the proposition that he/she packed the drugs; the evidence provides moderate support. If a discrete model is used where allele peak height is not considered, then $\mathrm{LR}=11$ (top row of Table 3). Taking peak height into account has little effect in this example. The sensitivity analysis shows the evidence always favours $H_{p}$ at the 2.5 percentile.

## Unknown and Contributor A Recovered

A different result is obtained when a mixture of unknown and contributor A is recovered. For the discrete model (top row of Table 4) the LR $\approx 0.1$, favouring the proposition that an unknown contributor wrapped the drugs. When allele peak height is considered, similar results are obtained (Table 4).

Table 4. Activity level likelihood ratios where contributor A and an unknown are recovered, with sensitivity analysis, showing 2.5-97.5 percentiles. The median ( 50 percentile) values are those that are reported. Results for the discrete model are shown in the top row; continuous models conditioned upon $\overline{R F U}_{A}>x$ and $\overline{R F U}_{\text {unknown }}>x$ are shown in remaining rows.


### 3.5.2. Cardboard Drug Wrap Experiment

Case Circumstances
A large depot of drugs was detected by the police during a house search of A's house. The drugs were wrapped in cardboard and covered by packing tape;
Person A admits that he packed the drugs and does not implicate anyone else;

Person B claims to have no knowledge of the drugs. However, he worked for a moving agency and often handles packing tape. Remains of packing tapes are often left behind and could be picked up and used by others.

# DNA Analysis 

DNA samples were collected from the wrappings. The results of the DNA analysis were a mixture of person A and an unknown contributor. A candidate was identified as person B from a national DNA database search.

## Propositions

Sub-source likelihood ratios were calculated for both contributors using EuroForMix [20], although this information was not used in any further analysis. To proceed with activity level analysis, it is assumed that the sub-source LR is sufficient for a court to agree the identity of a POI [2].

The prosecution and defence activity level propositions are as follows:
$H_{p}$ : A and B packed the drugs together and B did not previously handle the tape;
$H_{d}$ : A packed the drugs alone; $B$ had previously handled the tape
From the case information, a Bayesian network incorporating the relevant nodes was prepared (Figure 9). See Supplementary Materials S1 for details. Since both $H_{p}$ and $H_{d}$ agree that contributor A packed the drugs, his/her presence or absence of DNA has no effect upon the likelihood ratio. Only contributor B has an effect.
![img-8.jpeg](img-8.jpeg)

Figure 9. Bayesian network for the evaluation of evidence in the case where DNA evidence was collected from cardboard drug wrap.

## Statistical Analysis

The data are provided in Supplementary Materials S2. In the experiment, contributor B previously handled the tape as described in Section 3.5.1, and contributor A packed the drugs. The mean $\overline{R F U}$ of the observed DNA profile was split per contributor ( $\overline{R F U}_{A}$ and $\overline{R F U}_{B}$ ), based upon their respective mixture proportions $\left(M_{x}\right)$ : i.e., $\overline{R F U}_{A}=\overline{R F U}_{t o t} \times M_{x A}$ and $\overline{R F U}_{B}=\overline{R F U}_{t o t} \times M_{x B}$, where $M_{x}$ was calculated using EuroForMix [20]. Log-normal distributions were fitted to each set of data using the fitdistrplus R package (Figure 10). Distributions for the BN node "B DNA transferred when handling tape" (Figure 9) were modelled from $\overline{R F U}_{C 2 t a p e}$; distributions for BN nodes" (solo) A DNA transferred during packing" and "(joint) B DNA transferred during the packing" were both modelled from $\overline{R F U}_{C 1 p a c k}$ (Table 5).

![img-9.jpeg](img-9.jpeg)

Figure 10. Lognormal distributions of $\overline{R F U}_{C 1 p a c k}$ and $\overline{R F U}_{C 2 t a p e}$.

Table 5. Relationship of probabilities of DNA transfer from individuals A and B, showing the datasets that were used to calculate probability distributions, along with the BN nodes instantiated. Nomenclature is described in Section 2.5.1.

Probability Distribution | BN Nodes  |

Likelihood ratios were calculated as follows (see Table 5 for context): (a) A DNA is recovered: $L R=\frac{\left(1-t_{B}\right)}{(1-s)}$ (b) B DNA is recovered: $L R=t_{B} / s$ (c) A and B DNA are recovered: $L R=t_{B} / s$ (d) no DNA is recovered: $L R=\frac{\left(1-t_{B}\right)}{(1-s)}$

The formulae are derived in Supplementary Material S1. Note that likelihood ratios of (a) and (d) are the same, as are (b) and (c). This is because both $H_{p}$ and $H_{d}$ condition upon contributor A, hence his/her presence is cancelled out. To carry out sensitivity analysis, $1000 \times$ bootstraps (with replacement) were taken of the $\overline{R F U}_{A}$ and $\overline{R F U}_{B}$ data (Supplementary Material S1). For each bootstrap, a new set of log-normal parameters (mean $\log$ and SD log) were calculated using the fitdistrplus R package.

# Results of Analysis

Log-normal distributions were used to calculate the tape handling and drug packing TPR probabilities, conditioned upon values of $\overline{R F U}_{B}>x$ from simulated profiles and subsequently used in the BN (Figure 8) to calculate the results (Table 6).

Table 6. Activity level likelihood ratios, with sensitivity analysis, showing 1-99 percentiles. The median ( 50 percentile) values are those that are reported. Results for the discrete model are shown in the top row; continuous model conditioned upon $\overline{R F U}_{B}>x$ shown in remaining rows.


Likelihood ratios, along with sensitivity analyses are calculated against a range of $R F U_{B}>x$ values (Table 6). If a profile is obtained where only contributor A is present and there is no DNA present that can be attributed to contributor B, then the LR $=0.6$, i.e., supports the proposition that suspect B did not package the drugs. If DNA is present that can be attributed to B, then the LR $>1$, favouring the proposition that suspect B did package the drugs. The presence/absence of individual B as a contributor to the evidence can be described either as discrete: $\operatorname{Pr}\left(\overline{R F U}_{B}>0\right)$ vs. absence, or as a continuous distribution where $\operatorname{Pr}\left(\overline{R F U}_{B}>x\right)$, where x is a threshold value. With a discrete model, LR=1.4 (first row of Table 6). Taking the value of $\overline{R F U}_{B}>x$, with the continuous model in subsequent rows of Table 6, a higher LR is achieved, reaching a maximum median LR=6.9 if $\mathrm{RFU}_{\mathrm{B}}>1000$ (the limit of observations in Supplementary Materials S2), although the evidence can only be described as "weak" following the ENFSI verbal scale [22]. The sensitivity analysis shows the observed range between 1-99 percentiles from $1000 \times$ bootstraps of the data. The variation increases greatly as $\overline{R F U}_{B}$ increases-a reflection of the small size of the datasets. In conclusion, the discrete model understates the value of the evidence, compared with the continuous model.

# 4. Discussion 

### 4.1. Zip-Lock Drugs Bag Experiment

The DNA from the POI was detected more frequently on a zip-lock drugs bag if the bag was directly handled. However, the best quality profile observed in the study was collected from a zip-lock drugs bag stored in a personal bag (purse). From the literature, indirect transfer to a sleek surface such as the zip-lock drugs bag is expected to be low [8]. Most of the personal bags used in the experiments had previously been frequently used by the participants, although there are few observations in each class of bags, there is an indication that larger quantities of DNA can be detected on a zip-lock drugs bag after storage in purses. More DNA could be accumulated from the user on the inside of a purse as several personal items (e.g., phone, hairbrush, wallet) containing owner DNA are frequently stored there. In addition, the surface of the inside of the bag will influence accumulation and further transfer [8,23]. In the case example, it is shown that personal bags that are used to store everyday items, such as clothing or personal effects that are frequently handled, accumulate amounts of DNA that may be indirectly transferred to other objects. This resulted in low likelihood ratios (moderate evidence to support $H_{p}$ ) when DNA from only the POI was recovered. There was little difference between the discrete model and the continuous model, the latter takes the allele peak height into account. With mixtures, both discrete and continuous models favour $H_{d}$ (LR $\approx 0.1$; Table 4). In the experiment, only low amounts of background (DNA from unknown contributors) were detected. Combined with the relatively low difference between indirect and direct transfer

probabilities (Figure 8), especially when $\overline{R F U}>1000$, this has an impact of reducing the LR if the sample is in admixture with an unknown contributor, so that it always favours the defence proposition $\left(H_{d}\right)$.

# 4.2. Cardboard Drug Wrap Experiment 

In this study, the persistence of DNA from previous handlers of a roll of tape was investigated. As the top surface of the tape is hard and non-porous, the expectation is that low amounts of DNA would be transferred and detected after direct contact, in addition to a rapid removal of DNA from the previous user [8,12,13]. The findings of this study generally correlate with these expectations: a large proportion of samples produced no results or only a few alleles. The packer (last handler) was the only contributor or the one contributing a larger amount of DNA in most of the samples that gave results. Some exceptions were observed with two profiles showing results that only corresponded to the tape handler (person B). The sides of the tape have a rougher surface where more DNA is expected to be transferred upon initial contact [9,23]. In addition to DNA from the previous user persisting on the surface of the tape, it is possible that some of the DNA deposited on the side of tape could be transferred to the new user's hands and to the cardboard during the wrapping of the drugs. As no other items were touched in between handling the tape and performing the wrapping, there was no opportunity for the loss of person B's DNA to other surfaces. We did not monitor the wrapping procedure and recognise that the manner of contact during the procedure could influence the result. However, information regarding this will rarely be known in casework.

In the Bayesian network case example, we considered that an individual B claims that he/she handled tape which was later used to prepare drug wraps. Individual A has admitted the offence, hence, his/her presence of DNA on the drug wrap has no bearing on the value of the evidence. If contributor B's DNA is recovered, without taking account of $\overline{R F U}$ in the discrete model, the evidence is close to neutral $\mathrm{LR}=1.4$, whereas if $\overline{R F U}$ is taken into account, the value of the evidence increases with RFU, although it does not exceed $\mathrm{LR}=7$ where $\overline{R F U}>1000$ (the upper limit of experimental observations), i.e., the evidence would be described as weak using the ENFSI scale [22]. However, if B's DNA is absent, then this favours the defence proposition $\mathrm{LR}=0.6$.

The experimental set up is similar to that used in [13] where the question was if the POI previously cut an aluminium foil or used this foil in lock picking. The activity LR in the lock-picking study, calculated with a discrete model (7.4) was greater than that observed in the current study (1.4). However, the LR was in the same range as the maximum (median) level of the continuous model employed ( $\mathrm{LR}=6.9$ ). Some of the differences could be explained by the difference in transfer to and persistence on aluminium foil vs. tape.

### 4.3. Shedder Status and Transfer Probabilities

A person's shedder status has previously been shown to influence the probability of transfer, persistence, and detection of DNA [14,24]. Fonneløp et al. [14] demonstrated that DNA was more frequently detected in samples collected from the T-shirts of a victim if the attacker was a high shedder and that the probability of detection increased further if the victim was a low shedder. While Otten et al. [24] observed a correspondence between shedder stratus and DNA transfer to gloves. The correspondence between shedder status and the amount of DNA transferred is further demonstrated by our findings when it comes to direct transfer to zip-lock drugs bags (Figure 11), direct transfer during wrapping with a tape and transfer and persistence after touching a role of tape. On the other hand, when indirect transfer from the inside of a personal bag was considered, no clear association with shedder status was observed, and the best quality profile was detected after storage in a low shedder's personal bag. We hypothesised the amount of previous use and the surface of the inside of the bag could be of higher importance for this type of transfer. The low number of samples collected in each category is also a limitation and a clearer correspondence may be seen with a larger collection of data. Shedder status was not incorporated into the Bayesian

networks because dividing the results into three categories would lead to too few data in each group to analyse. Secondly, it would also be important to properly characterise the effect of shedder status on indirect transfer before applying this variable to the model.
![img-10.jpeg](img-10.jpeg)

Figure 11. Effect of high/medium/low shedder status on direct transfer (E1) data.
The LRs calculated in this study are comparable to other studies where DNA transferred by hands is considered [6,13,25]. It is likely that including more informationespecially shedder status, would, to some degree, change the LR calculations [14].

# 4.4. Detection of Unknown DNA 

This experiment was performed during the COVID-19 pandemic where a general recommendation to keep a social distance of at least two meters and to wash hands frequently or use antibacterial liquid was given. It is likely that these measures could have had an impact on the detection of unknown DNA in the samples, which was low compared to previous studies $[9,16,26]$.

## 5. Conclusions

We have created datasets on direct and indirect transfer to zip-lock bags and transfer and persistence to tape and further shown how the data can be used to inform Bayesian Networks. As the indirect and persistence scenarios tested are realistic under the circumstances utilised in this study, only moderate to low support for $H_{p}$ was obtained. We have shown that applying a continuous model based on the profile quality can alter LRs compared to a discrete model and is preferable. There are challenges with limited datasets, and we were not able to implement shedder status into our models. More data on the influence of shedder status are required when indirect transfer is considered.

Supplementary Materials: The following are available online at https://www.mdpi.com/article/ 10.3390/genes13010018/s1, Supplementary Material S1: Derivation of formulae from experiment 2: Cardboard drug wraps, Supplementary Material S2: Supplementary table 2.1 Results from the direct and indirect transfer to zip-lock bags experiment; Supplementary table 2.2 Results from the persistence and detection of DNA from a previous user of a tape roll experiment; Supplementary table 2.3 The results of the shedder status experiment.

Author Contributions: Conceptualization, A.E.F. methodology, A.E.F. and P.G..; software, P.G.; formal analysis, A.E.F., S.F. and P.G.; investigation, S.F and G.S.; data curation, A.E.F. and S.F.; writingoriginal draft preparation, A.E.F., S.F. and P.G.; writing-review and editing, G.S.; supervision, A.E.F. and G.S.; project administration, A.E.F. All authors have read and agreed to the published version of the manuscript.

Funding: This research received no external funding.
Institutional Review Board Statement: This project was approved by the data protection officer at Oslo University Hospital (Approval Code: 20/22532, Approval Date: 21 October 2020).

Informed Consent Statement: Informed consent was obtained from all participants involved in the study.

Data Availability Statement: The data supporting the findings reported in this manuscript can be found in the supplementary material S2, Tables S1-S3.

Acknowledgments: We would like to thank Arne Roseth for his help with the direct PCR analysis and all the participants that contributed to the study.

Conflicts of Interest: The authors declare no conflict of interest.
