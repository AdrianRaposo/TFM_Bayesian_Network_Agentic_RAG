# Article 

## Human Error Probability Assessment for LNG Bunkering Based on Fuzzy Bayesian Network-CREAM Model

Hongjun Fan * (D), Hossein Enshaei (D) and Shantha Gamini Jayasinghe

## check for updates

Citation: Fan, H.; Enshaei, H.; Jayasinghe, S.G. Human Error Probability Assessment for LNG Bunkering Based on Fuzzy Bayesian Network-CREAM Model. J. Mar. Sci. Eng. 2022, 10, 333. https://doi.org/ 10.3390/jmse10030333

Academic Editor: Salman Nazir
Received: 25 January 2022
Accepted: 24 February 2022
Published: 27 February 2022
Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## (D)

Copyright: (c) 2022 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

Australian Maritime College (AMC), College of Sciences and Engineering, University of Tasmania, Launceston, TAS 7248, Australia; Hossein.enshaei@utas.edu.au (H.E.); Shantha.jayasinghe@utas.edu.au (S.G.J.) * Correspondence: Hongjun.fan@utas.edu.au


#### Abstract

Liquified natural gas (LNG) as a marine fuel has gained momentum as the maritime industry moves towards a sustainable future. Since unwanted LNG release may lead to severe consequences, performing quantitative risk assessment (QRA) for LNG bunkering operations has become mandatory according to some regulations. Human error is a main contributor to the risks, and the human error probabilities (HEPs) are essential for inclusion in a QRA. However, HEPs data are unavailable in the LNG bunkering industry so far. Therefore, this study attempts to infer HEPs through on-site safety philosophical factors (SPFs). The cognitive reliability and error analysis method (CREAM) was adopted as a basic model and modified to make it suitable for HEP assessment in LNG bunkering. Nine common performance condition (CPC) indicators were identified based on the fuzzy ranking of 23 SPF indicators (SPFIs). A Bayesian network (BN) was built to simulate the occurrence probabilities of different contextual control modes (COCOMs), and a conditional probability table (CPT) for the COCOM node with 19,683 possible combinations in the BN was developed according to the CREAM's COCOM matrix. The prior probabilities of CPCs were evaluated using the fuzzy set theory (FST) based on data acquired from an online questionnaire survey. The results showed that the prior HEP for LNG bunkering is 0.009841 . This value can be updated based on the re-evaluation of on-site SPFIs for a specific LNG bunkering project to capture the dynamics of HEP. The main innovation of this work is realizing the efficient quantification of HEP for LNG bunkering operations by using the proposed fuzzy BN-CREAM model.


Keywords: maritime; LNG bunkering; quantitative risk assessment; human error; Bayesian network; CREAM; fuzzy set

## 1. Introduction

The number of liquified natural gas (LNG) fueled ships is rapidly growing due to LNG being considered as a viable transitional fuel in the maritime industry's journey towards decarbonization [1-3]. LNG is flammable and cryogenic, and unwanted release may lead to severe consequences. Particularly, the safety of LNG bunkering is a key issue of concern to the industry, because bunkering operations have a high likelihood of leakage [4]. Therefore, performing quantitative risk assessment (QRA) for LNG bunkering operations is either mandated or highly recommended for understanding and mitigating the potential risks according to the existing regulations and standards [5]. Human error has become the main contributor to the risks in the maritime industry [6,7], where the combination of human and organizational errors during operations leads to about $65 \%$ of all catastrophic accidents [8]. As a result, when performing a QRA for LNG bunkering, the human error probabilities (HEPs) are essential inclusion. The definition of HEP is the opposite of that of the human reliability probability which refers to the probability that a person: (1) correctly performs a system-required activity and (2) performs no extraneous activity that can degrade the system [9].

The LNG bunkering consists of the following main steps: preparation, connection (between bunkering side and receiving side), purging, inerting, pre-cooling, LNG transfer, purging, and disconnection. These steps are all involved with human behavior. The complex mechanism that lies behind human behavior leads to human errors. From a Bowtie model-based risk assessment perspective [9], human errors may: (1) contribute to causes of a hazardous event; (2) be the direct triggering events or even sole triggering event for the hazardous event; (3) be related to the safety barriers of potential consequences. For example, Figure 1 shows a truck-to-ship LNG bunkering scenario; as a safety barrier, an operator should press a manual emergency shutdown (ESD) switch button immediately when leakage is observed. Possible human error modes for this operation could comprise: the operator not pressing the switch button, or the operator pressing the button too late. These human error modes lead to different occurrence probabilities of consequences.
![img-0.jpeg](img-0.jpeg)

Figure 1. A truck-to-ship LNG bunkering scenario.
Some research studies have been conducted regarding the risks of LNG bunkering. These have mainly focused on the following three aspects: (1) safety zone evaluation [10,11,12,13,14,15,16,17,18,19,20,21,22], (2) risk assessment methodology and practice [23,24,25,26,27], and (3) emergency evacuation assessment [27,28]. Even though these studies have improved our understanding of LNG bunkering safety, none has quantified human errors in LNG bunkering. Stokes et al. have studied the human factor for LNG bunkering [29], and demonstrated qualitatively the importance of human error rather than quantitatively analyzing the HEP. As the LNG bunkering industry is premature, the HEPs are unavailable in existing databases [30,31,32,33]. The International Association of Oil \& Gas Producers has suggested the HEPs for rule-based actions by control room personnel after diagnosis of an abnormal event [34]; however, the available data are directly quoted from a report from the nuclear industry [35], and their applicability in the field of LNG bunkering is arguable. As an alternative solution, the HEP can be inferred through human reliability assessment (HRA) methods. Previous studies have reported many HRA approaches which are classified into three generations as summarized in Table 1, and some researchers have comprehensively reviewed these methods [36,37,38]. In recent years, second-generation methods are widely used; third-generation methods are still in the early stages of development since the artificial intelligence and computer-aided simulation techniques are still under development.

Table 1. Three generations of human reliability assessment (HRA) approach [39-47].


The significant human errors occur as a result of a combination of on-site conditions and certain personal psychological factors that trigger error mechanisms in personnel [9]. The psychological factors of operators are complex and difficult to quantify in an LNG bunkering operation. In fact, the negative impact of psychological factors on human performance can be reflected in on-site conditions which can be defined as safety philosophical factors (SPFs). For example, a superior safety culture can ensure that workers have a good mental state during work. Consequently, it is assumed that human errors during LNG bunkering are determined by on-site SPFs.

Further to this background, this research attempts to explore inferring HEP from on-site SFPs of LNG bunkering. Among the second-generation HRA approaches as shown in Table 1, the CREAM (cognitive reliability and error analysis method), which is widely utilized in many industries, is able to infer HEPs through safety factors. Therefore, in this research, the CREAM is employed as a basic method while modified to make it suitable for HEPs inference during LNG bunkering operations.

The CREAM was originally developed for the nuclear industry but becomes popular in other industries [41,48-50]. A human error has multiple causes, and the original CREAM model uses nine common performance condition (CPC) indicators to determine a specific contextual control mode (COCOM) out of four COCOMs, namely, "Strategic", "Tactical"," Opportunistic", and "Scrambled". Each CPC is given a score ( 1,0 or -1 ) by the analysts, and each COCOM is connected to a HEP interval as described in Table 2. A matrix is used to convert the performance of nine CPCs into a COCOM. The combined CPC score can be derived by counting the number of times where a CPC is expected to have negative effect ( -1 ), no significant effect ( 0 ), or positive effect (1). Furthermore, in order to generate a specific crisp HEP, an extended CREAM method should be used [41].

Table 2. The COCOMs and their human error probability (HEP) intervals.


The applications of CREAM have solved HEPs in many studies. However, there is still a major limitation of utilizing CREAM. Experts' judgments on CPCs are subjective which makes uncertainties in the results of CPCs' performance higher. Nevertheless, CREAM assigns a human error to a certain COCOM without considering the probabilities of it falling into different COCOMs which increases the uncertainty of the results to a certain extent.

In order to deal with the uncertainty and to capture the conditional independence relationships between the interacting variables, the probabilistic graphical models could be employed. Generally, there are two main probabilistic graphical models, namely, the Bayesian networks (BNs) and the Markov Random Fields. The BNs are directed acyclic graphs with variables representing observable or latent variables of the model. However, the Markov Random Fields are undirected acyclic graphs that might contain cycles, they thus can describe a different set of dependency relationships than their BN counterparts. In this research, a directed acyclic graph is able to establish the causal relationships between the CPCs and the COCOMs; therefore, the BN is employed to calculate the probabilities of COCOMs.

The BN is a powerful method. In addition, the utilization of the fuzzy set theory (FST) can cope with the data shortage in a BN model. In the existing literature, studies have demonstrated that combining BN or fuzzy-BN (FBN) with CREAM can consider the uncertainty of the model and the given information. For example, Yang, Z. et al. established a BN-based CREAM which can provide the instant estimation of HEP given the updated data [51]. Yang, Z.L. et al. proposed a modified BN based CREAM to quantify HEPs in marine engineering by incorporating fuzzy evidential reasoning [52]. Zhou, Q. et al. applied the FBN CREAM model in HRA for a case of tanker shipping [53]. Similarly, Ung. S used a fault tree analysis structure combined with a modified FBN CREAM to analyse the HEPs that trigger oil tanker collisions [54]. Chen, D. et al. conducted an HRA for a submersible diving process based on the CREAM model and BN [55]. Abbasinia, M. et al. used FBN to improve the capabilities of CREAM for determining the COCOMs [56]. Ghasemi, F. et al. used the FBN CREAM model to predict HEP for a road tanker loading operation [57]. Wu, Y. et al. adopted the FBN CREAM to determine the COCOMs and calculate the HEPs in a metallurgical enterprise [49]. These efforts have developed and enhanced the CREAM with computer-aided simulation techniques. However, the proposed methods in the literature cannot be applied directly in the LNG bunkering industry because the CPCs are required to be purpose-defined for LNG bunkering operations. Besides, it is noteworthy that the conditional probability table (CPT) for the COCOM node in the BN has yet to be addressed, because in the existing literature, the dimension of the CPT was reduced to achieve the purpose of simplifying the calculation. For example, the intermediate nodes or assumed rules were used, which violated the principle of the original CREAM model and decreased the accuracy of the results.

With this context, this study attempts to address the following main research questions (RQs) about inferring HEP:

RQ1: How to define CPCs for LNG bunkering?
RQ2: How to build a BN model that fully complies with the original CREAM principle?
RQ3: How to obtain the prior probabilities of CPCs?
As the premise of this research, there are the following basic assumptions:
(1) All HEPs in a specific LNG bunkering operation are the same. There are two reasons for this. Firstly, the individual differences of operators are ignored due to few onsite operators needed according to practice. Usually, there are less than five on-site operators during LNG bunkering. Secondly, all human operations are stipulated in the LNG bunkering operation manual, and any possible human error is a violation of the procedures in the operation manual. In other words, human error modes are essentially the same.
(2) The HEP is independent of time. This means that HEP remains the same irrespective of how long the bunking operations last. This is different from the probabilities of failure

of technical equipment, which increase with time or deterioration of the equipment. This is equivalent to treating a person as "a new equipment" at all times [9].
The main novelty of this work is an attempt to realize the efficient quantification of HEP for LNG bunkering operations using the fuzzy BN-CREAM model.

The remainder of this article is structured as follows. Section 2 presents the methodology. Section 3 introduces the data collection and analysis. Section 4 presents the results and discussion. Finally, Section 5 outlines the conclusions.

# 2. Methodology 

This section provides a framework of the proposed method for HEP assessment shown in Figure 2. It can be implemented to the project in three phases demonstrated below.
![img-1.jpeg](img-1.jpeg)

Figure 2. The framework of human error probability (HEP) assessment.

### 2.1. Identification of the Common Performance Condition Indicators (CPCs)

The original CREAM was developed for the nuclear industry, CPCs are therefore particularly designed for nuclear plants related operations. This paper attempts to use the basic principle of CREAM in the LNG bunkering industry; thus, purpose-defined CPCs should be identified according to the characteristics of LNG bunkering operations. CPCs are environmental factors, personal, or directed to activities that have the potential to affect human performance positively, neutrally or negatively; therefore, identifying CPCs is a key step in this study.

### 2.1.1. Identifications of the Safety Philosophical Factors (SPFs) and the Safety Philosophical Factors' Indicators (SPFIs)

Safety philosophical factors (SPFs) influence not only how humans perceive their actions, but also humans' response to the events. In this study, the safety documents from three LNG bunkering service companies were reviewed. Five safety philosophical factors (SPFs), namely, safety culture (SC), safety management (SM), safety process (SP), safety training (ST), and safety awareness (SA) were identified to encapsulate the human safety performance. Totally, 23 measurable safety philosophical factors' indicators (SPFIs) are identified. Some environmental factors that might impact safety performance are implicit in some SPFIs, for example, SM5, SP2, and SP4. Table 3 presents five SPFs and the identified


23 SPFIs. The collection of SPFIs is used as a pool for CPCs screening. According to the CREAM model, nine SPFIs are selected to represent nine CPCs. To this end, 23 SPFIs are ranked, and the top nine SPFIs are designated as CPCs. The ranking is based on an online questionnaire survey data and the FST.

Table 3. The safety philosophical factors (SPFs) and the safety philosophical factors' indicators (SPFIs).

23 SPFIs. The collection of SPFIs is used as a pool for CPCs screening. According to the CREAM model, nine SPFIs are selected to represent nine CPCs. To this end, 23 SPFIs are ranked, and the top nine SPFIs are designated as CPCs. The ranking is based on an online questionnaire survey data and the FST.

Table 3. The safety philosophical factors (SPFs) and the safety philosophical factors' indicators (SPFIs).

2.1.2. Online Questionnaire on Importance and Performance of the Safety Philosophical Factors' Indicators (SPFIs)

A qualitative online questionnaire survey method is conducted to obtain information for measuring the SPFIs. A survey questionnaire form is developed and made available to potential experts online with the Microsoft Forms tool. The specially designed closed-ended structured questionnaire includes the following sections:

Section A: Demographics information about the experts.
Section B: Likert scale multiple-choice questions.

The gathered demographic information about the experts includes four variables, namely, job affiliation, job professional position, service time, and education level. The information is used to calculate the weights of experts in evaluating the fuzzy numbers (FNs) of SPFIs. In Section B, a seven-point Likert type scale is employed anchored with "Negligible (Very low)" and "Extremely important (Very high)" for the importance of an SPFI to human safety performance. A three-point Likert type scale is also employed with "Adequate", "Acceptable", and "Inadequate" options for the current performance of an SPFI which is applied in phase 3, shown in Figure 2, to evaluate the prior probabilities of CPCs. Figure 3 shows an example of questions for the SPFI of "SC1".

![img-2.jpeg](img-2.jpeg)

Figure 3. An example of questions for the safety philosophical factors' indicator (SPFI) of "SC1".
2.1.3. Converting the Experts' Qualitative Linguistic Expression into Fuzzy Numbers (FNs)

In this step, the qualitative linguistic expressions from experts on the importance of SPFIs are converted into FNs based on the FST [58]. A fuzzy number is a convex fuzzy set, characterized by a given interval of real numbers, each with a grade of membership between 0 and 1. Its membership function is piecewise continuous and satisfies the following conditions:

Let a fuzzy set $\tilde{A}=[a, b, c, d]$, then the membership function of the fuzzy set, $f_{\tilde{A}}(x)$, can be expressed as:
(1) $f_{\tilde{A}}(x)=0$ outside some interval $[a, b]$;
(2) $f_{\tilde{A}}(x)$ is non-decreasing (monotonic increasing) on $[a, b]$; and non-increasing (monotonic decreasing) on $[c, d]$;
(3) $f_{\tilde{A}}(x)=1$ for each $x \in[b, c]$.

In this study, the trapezoidal fuzzy numbers whose membership functions are defined as Equation (1) are used.

$$
(x)=\left\{\begin{aligned}
f_{\tilde{A}}^{L}(x) & =\frac{x-a}{b-a}, a \leq x \leq b \\
1, b \leq x \leq c \\
f_{\tilde{A}}^{R}(x) & =\frac{d-x}{d-c}, c \leq x \leq d \\
0, \text { otherwise }
\end{aligned}\right.
$$

where $f_{\tilde{A}}(x)$ is the membership function of the fuzzy set $\tilde{A}=[a, b, c, d]$. The $f_{\tilde{A}}^{L}(x)$ represents the left side of the membership function, and $f_{\tilde{A}}^{R}(x)$ represents the right side of the membership function.

The conversion scale, which includes seven qualitative linguistic terms, is adopted for estimating the FNs of SPFIs as shown in Figure 4 [59]. This maps an expert's judgment to a

fuzzy set. For example, if an expert's linguistic expression on the importance of an SPFI is "Medium", then the fuzzy set is $[0.4,0.5,0.5,0.6]$.
![img-3.jpeg](img-3.jpeg)

Figure 4. The conversion scale including seven qualitative terms.
The next step is to aggregate multiple judgements on an SPFI from multiple experts into a single judgement.

# 2.1.4. Aggregating the Fuzzy Sets into an Integrated Fuzzy Set 

Various methods are available in the literature to aggregate experts' opinions including linear opinion pool [60], max-min Delphi [61], sum-product [62], max-product [63], etc. Among the aforementioned methods, the linear opinion pool is adopted in this study since it is an effective and easy approach [64]. Based on the linear opinion pool method, the aggregated integrated fuzzy set (IFS) can be expressed by Equation (2).

$$
I F S_{j}=\sum_{i=1}^{n}\left(W_{i} \times E_{i j}\right), j=1,2,3 \ldots, m
$$

where $I F S_{j}$ is the IFS of $j$ th SPFI. $W_{i}$ is the weight given to the $i$ th expert, and $\sum_{i=1}^{n} w_{i}=1$; $E_{i j}$ is the linguistic expression corresponding to fuzzy set obtained from $i$ th expert about $j$ th SPFI. For example, if the 1st expert's linguistic expression on the 1st SPFI is "Medium" (see Figure 4), then $E_{11}$ is $[0.4,0.5,0.5,0.6] ; n$ is the total number of experts while $m$ is the total number of SPFs.

Each expert's professional background is different, so his/her judgment contributes differently to the results. This article uses weights for considering the contribution of each expert to the results. The weighting criterion of experts is designed and presented in Table 4. The weights of experts are calculated using the Equation (3) [65].

$$
W_{i}=\frac{W S_{i}}{\sum_{i=1}^{n} W S_{i}}
$$

where $W S_{i}$ is the weight score of the $i$ th expert, $W S_{i}=P P S_{i}+S T S_{i}+E L S_{i}, P P S_{i}, S T S_{i}$, and $E L S_{i}$ represent the professional position score, the service time score, and the education level score of the $i$ th expert, respectively.

Table 4. The weighting criteria of experts.


The next step is to convert the aggregated IFS for each SPFI into a fuzzy number (FN), i.e., defuzzification.

# 2.1.5. Defuzzification 

There are many different methods of defuzzification available, including basic defuzzification distributions, bisector of area, center of area, etc. [66,67]. The center of area method which is the most widely used method is adopted in this study. Let a fuzzy set $\tilde{A}=[a, b, c, d]$, then defuzzification of the trapezoidal fuzzy number $\tilde{A}$ is given by Equation (4) [68], $\bar{x}_{0}(\tilde{A})$ is obtained as a FN. Equation (5) which is for a single trapezoidal fuzzy number can be derived by Equation (4). According to the ranking of FNs of SPFIs, the top nine SPFIs can be designated as CPCs.

$$
\begin{gathered}
\bar{x}_{0}(\tilde{A})=\frac{\int_{-\infty}^{+\infty} x f_{\tilde{A}}(x) d x}{\int_{-\infty}^{+\infty} f_{\tilde{A}}(x) d x}=\frac{\int_{a}^{b} x f_{\tilde{A}}^{L}(x) d x+\int_{b}^{c} x d x+\int_{c}^{d} x f_{\tilde{A}}^{R}(x) d x}{\int_{a}^{b} f_{\tilde{A}}^{L}(x) d x+\int_{b}^{c} d x+\int_{c}^{d} f_{\tilde{A}}^{R}(x) d x} \\
\bar{x}_{0}(\tilde{A})=\frac{1}{3} \times\left(a+b+c+d-\frac{c d-a b}{c+d-a-b}\right)
\end{gathered}
$$

### 2.2. BN Modelling

In a BN, the nodes represent variables, arcs represent causal relationships between the linked variables, and their conditional dependencies are represented through the conditional probability tables (CPTs) assigned to the nodes. The joint probability distribution $P(U)$ of variables $U=\left\{A_{1}, \ldots, A_{n}\right\}$ included in the BN is expressed by Equation (6).

$$
P(U)=\prod_{i=1}^{n} P\left(A_{i} \mid P a\left(A_{i}\right)\right)
$$

where $P a\left(A_{i}\right)$ is the parent set of $A_{i}[69]$.
In the BN, the Bayes theorem is used to update the prior probabilities for events given evidence, thus yielding the posterior probability which is expressed by Equation (7):

$$
P(U \mid E)=P(U, E) / P(E)
$$

where $P(U \mid E)$ represents the posterior probability of the $U$ given the evidence $E ; P(U, E)$ means the probability of $U$ and $E$ happening together; $P(E)$ represent the occurrence probability of evidence $E$.

The software, Netica, is used to build BN. According to the CREAM model, a BN model is built as shown in Figure 5. Each CPC is represented by a node having three states, namely, 1 (Adequate), 0 (Acceptable), and -1 (Inadequate). A causal arc is directed from each CPC node to the COCOM node which has four states, namely, "Strategic", "Tactical", "Opportunistic", and "Scrambled". It is assumed that CPCs are independent; therefore, there are no causal arcs among CPC nodes.

![img-4.jpeg](img-4.jpeg)

Figure 5. The BN model for the CREAM.
Building CPTs is core for a BN. Each CPC has three states, and there are nine CPCs; thus, there are $3^{9}=19,683$ rows in the CPT of the COCOM node. In practice, it is a challenge to input a CPT with so many rows in the software; therefore, in order to simplify BN, some researchers have attempted to group CPCs into a few intermediate nodes based on some assumptions [49,51,53,56,57], or developed some assumed rules for the CPT of COCOMs node [52,54]. It is argued that these practices increased the uncertainty of the model, because to a certain extent, the formulation of these assumptions and rules is based on the subjective judgments of the researchers, thereby weakening the outcomes of these studies. In this study, the BN model is fully complied with the CREAM matrix without using intermediate nodes or assumed rules. A program based on the Microsoft EXCEL platform is compiled to calculate the CPT of the COCOM node based on Figure 6. The obtained CPT data can then be directly imported into the Netica software. The original CREAM matrix, in which y-axis has 8 values ( $0-7$ ) is extended to 10 , as each CPC has the states of " 1 ", " 0 ", and " -1 ", as shown in Figure 6. Table 5 shows a part of the CPT, and the original code for the calculation of CPT is attached in Table S1 in the Supplemental Material available online.
![img-5.jpeg](img-5.jpeg)

Figure 6. The relations between the common performance condition indicators (CPCs) and the COCOMs.

Table 5. A part of the conditional probability table (CPT).


${ }^{1}$ Str: Strategic; Tac: Tactical; Opp: Opportunistic; Scr: Scrambled.

# 2.3. Human Error Probability (HEP) Calculation 

This section presents the calculations of prior probabilities of CPCs and HEP.

### 2.3.1. Prior Probabilities of the Common Performance Condition Indicators (CPCs)

The prior probabilities of CPCs are necessary conditions for solving the probabilities of COCOM node's states in the BN. The qualitative judgements of experts for the current performance of each CPC can be converted into the prior probability of each CPC through using the FST. As mentioned in Section 2.1.2, a three-point Likert type scale is used to express the current performance of CPCs; therefore, the conversion scale, which includes three qualitative linguistic terms, is adopted for quantifying the prior probability of each CPC as shown in Figure 7. In this model, "Inadequate" represents the negative effect $(-1)$; "Acceptable" represents the no significant effect ( 0 ); "Adequate" represents the positive effect (1). The trapezoidal fuzzy numbers' membership functions are expressed by Equations (8)-(10).

$$
\begin{aligned}
& f_{\tilde{A}}(x)_{\text {Inadequate }}=\left\{\begin{array}{c}
f_{\tilde{A}}^{L}(x)=1,0 \leq x \leq 0.1 \\
f_{\tilde{A}}^{R}(x)=\frac{0.5-x}{0.4}, 0.1 \leq x \leq 0.5 \\
0, \text { otherwise }
\end{array}\right. \\
& f_{\tilde{A}}(x)_{\text {Acceptable }}=\left\{\begin{array}{c}
f_{\tilde{A}}^{L}(x)=\frac{x-0.1}{0.4}, 0.1 \leq x \leq 0.5 \\
f_{\tilde{A}}^{R}(x)=\frac{0.9-x}{0.4}, 0.5 \leq x \leq 0.9 \\
0, \text { otherwise }
\end{array}\right. \\
& f_{\tilde{A}}(x)_{\text {Adequate }}=\left\{\begin{array}{c}
f_{\tilde{A}}^{L}(x)=\frac{x-0.5}{0.4}, 0.5 \leq x \leq 0.9 \\
f_{\tilde{A}}^{R}(x)=1,0.9 \leq x \leq 1 \\
0, \text { otherwise }
\end{array}\right.
\end{aligned}
$$

![img-6.jpeg](img-6.jpeg)

Figure 7. The fuzzy membership functions for the common performance condition indicators (CPCs).

The aggregation and defuzzification methods used in this step are the same as what was described in Sections 2.1.4 and 2.1.5. The FNs of CPCs are designated as the prior probabilities of CPCs. Once the prior probabilities of CPCs are assigned to the associated nodes, the probabilities of COCOM node's states can be obtained through running the BN model.

# 2.3.2. Defuzzification of the Fuzzy Sets for COCOMs and HEP Calculation 

The fuzzy sets for COCOM node's states according to Table 2 are shown in Figure 8. The trapezoidal fuzzy numbers' membership functions are expressed by Equations (11)-(14). Equation (4) is then used to perform the defuzzification process of the trapezoidal fuzzy set $\bar{A}$, where

$$
f_{\bar{A}}(x)=f_{\bar{A}}(x)_{\text {Strategic }}+f_{\bar{A}}(x)_{\text {Tactical }}+f_{\bar{A}}(x)_{\text {Opportunistic }}+f_{\bar{A}}(x)_{\text {Scrambled }}
$$

![img-7.jpeg](img-7.jpeg)

Figure 8. The fuzzy membership functions for the COCOMs.
Subsequently, HEP can be obtained using Equation (15).

$$
\begin{gathered}
f_{\bar{A}}(x)_{\text {Strategic }}=\left\{\begin{array}{c}
f_{\bar{A}}^{L}(x)=\frac{x+5.3}{1.65},-5.3 \leq x \leq-3.65 \\
f_{\bar{A}}^{R}(x)=\frac{-2-x}{1.65},-3.65 \leq x \leq-2 \\
0, \text { otherwise }
\end{array}\right. \\
f_{\bar{A}}(x)_{\text {Tactical }}=\left\{\begin{array}{c}
f_{\bar{A}}^{L}(x)=\frac{x+3}{1},-3 \leq x \leq-2 \\
f_{\bar{A}}^{R}(x)=\frac{-1-x}{1},-2 \leq x \leq-1 \\
0, \text { otherwise }
\end{array}\right. \\
f_{\bar{A}}(x)_{\text {Opportunistic }}=\left\{\begin{array}{c}
f_{\bar{A}}^{L}(x)=\frac{x+2}{0.85},-2 \leq x \leq-1.15 \\
f_{\bar{A}}^{R}(x)=\frac{-0.3-x}{0.85},-1.15 \leq x \leq-0.3 \\
0, \text { otherwise }
\end{array}\right. \\
f_{\bar{A}}(x)_{\text {Scrambled }}=\left\{\begin{array}{c}
f_{\bar{A}}^{L}(x)=\frac{x+1}{0.5},-1 \leq x \leq-0.5 \\
f_{\bar{A}}^{R}(x)=\frac{x+2}{0.5},-0.5 \leq x \leq 0 \\
0, \text { otherwise }
\end{array}\right. \\
H E P=10^{x_{0}(\bar{A})}
\end{gathered}
$$

## 3. Data Acquisition and Analysis

Data for ranking the SPFIs and analyzing the fuzzy probabilities of CPCs were acquired through an online questionnaire survey. The criterion for the selection of experts was set to have LNG bunkering related knowledge or experience. The ethics application was approved by the University of Tasmania's Social Sciences Human Research Ethics Committee on 9 February 2021 (Project ID:23903). The online survey was distributed


Table 6. Selective information of the experts and the associate weights.


Table 7. Selective expressions on the importance to the safety of each safety philosophical factors' indicator (SPFIs).


Table 8. Top nine ranked safety philosophical factors' indicator (SPFIs).


See Table S2 in the Supplemental Material available online.
See Table S3 in the Supplemental Material available online.

# 3.2. Prior Probabilities of Common Performance Conditions (CPCs) 

The prior probabilities of CPCs are obtained as shown in Table 9 using Equations (2), (3), (5), (8)-(10). The obtained data are then assigned to CPC nodes in the BN model.

Table 9. The prior probabilities of the common performance condition indicators (CPCs).


${ }^{1}$ Ad: Adequate; Ac: Acceptable; In: Inadequate. See Table S4 in the Supplementary Materials available online.

# 4. Results and Discussion

This section presents the results and discussion on the probabilities of COCOMs and HEP for five hypothetical cases.

### 4.1. Results

The probabilities of obtained COCOM node's states are shown in Figure 9 and Table 10. Figure 10 presents the degrees of fuzzy membership functions of COCOMs, and Table 10 presents the calculation of HEP. The FN is calculated using Equation (4), and HEP $=0.009841$ is obtained using Equation (15). This HEP value represents the prior HEP during LNG bunkering operations in the current LNG bunkering industry. These data can also be used in a QRA model. For a specific project, if on-site CPCs are re-evaluated and the posterior probabilities are obtained, then the risk analyst can still use the proposed BN model to update the data in obtaining the posterior HEP. ![img-8.jpeg](img-8.jpeg)

Figure 9. The probabilities of the COCOM node's states.

Table 10. The probabilities of the COCOMs and the human error probability (HEP).


![img-9.jpeg](img-9.jpeg)

Figure 10. The degrees of the fuzzy membership functions of COCOMs ( $\mathrm{x} 1=-5.29788$; $\mathrm{x} 2=-2.0021186 ; \mathrm{x} 3=-2.0013 ; \mathrm{x} 4=-1.9987$ ).

# 4.2. Discussion

This sub-section uses five hypothetical cases to discuss the dynamic characteristics of the proposed model. In each case, a specific homogenized probability of CPCs, $P_{h}$, is assumed. The assumed conditions are Case $1\left(P_{h}=0\right)$, Case $2\left(P_{h}=0.2\right)$, Case $3\left(P_{h}=0.5\right)$, Case $4\left(P_{h}=0.8\right)$, and Case $5\left(P_{h}=1\right)$. These cases reflect the changes of on-site CPCs from low levels to high levels.

Table 11 presents obtained probabilities of CPCs using Equations (8)-(10) for Case 1-5. Gradually increasing the $P_{h}$ value from 0 to 1 means that the safety performance of each CPC is improved gradually. For example, the Case 2 represents the probabilities of "adequate", "acceptable", and "inadequate" to be 0,0.25 , and 0.75 , respectively, for each CPC. However, the Case 4 represents the probabilities of "adequate", "acceptable", and "inadequate" to be $0.75,0.25$, and 0 , respectively, for each CPC. From Case 2 to Case 4, the probability of the safety performance of each CPC being "adequate" increases from 0 to 0.75 , while the probability of the safety performance being "inadequate" decreases from 0.75 to 0 . Table 12 presents the probabilities of COCOMs and HEPs for five cases. Figure 11 shows the relationship between HEP and homogenized probability of CPCs.

It is apparent that as the $P_{h}$ value increases, the value of HEP decreases. When the $P_{h}$ is less than 0.5 , the HEP value decreases relatively quickly, and when the $P_{h}$ is greater than 0.5 , the HEP value decreases relatively slowly. This trend is related to the intervals of the four states of COCOM, from "Scrambled" to "Strategic", and the logarithmic interval that each state falls into is gradually widen as shown in Figure 8.

The prior probabilities of CPCs can be updated to obtain the posterior probabilities in the BN model according to the actual safety situation of the LNG bunkering site based on periodic evaluation of SPFIs, such as quarterly or annually. Therefore, the proposed model can be used to conduct a dynamic evaluation of HEP. In fact, most of the current techniques are unable to capture the dynamics of HEP. Dynamic HEP can be used as the input data in the dynamic QRA model so that more accurate dynamic risk profiles of LNG bunkering can be achieved.

Table 11. The probabilities of the common performance condition indicators (CPCs) for five cases.


${ }^{1}$ Ad: Adequate; ${ }^{2}$ Ac: Acceptable; ${ }^{3}$ In: Inadequate Table 12. The probabilities of the COCOMs and the human error probabilities (HEPs) for five cases.


${ }^{1} \mathrm{P}:$ Probability. $\square$ CPC 11. The relationship between the human error probability (HEP) and the homogenized probability of the common performance condition indicators (CPCs).

# 5. Conclusions

In this research, the original CREAM model was modified to be adapted to HEP assessment in LNG bunkering operations. Nine CPCs were identified from 23 SPFIs for LNG bunkering operations based on the ranking of FNs as a way of capturing the essential aspects of the situation and the conditions for human behaviors. The BN was employed in the modified CREAM model to consider the uncertainty of a specific task falling into different COCOMs. The CPT for the COCOM node in the BN was coded based on extended COCOMs matrix rather than using intermediate nodes or other assumed rules to reduce the dimension of CPT which decreases the accuracy of the results. Furthermore, sufficient data reflecting the current safety status of the LNG bunkering industry in terms of human factors ensures that the prior probabilities of CPCs are calculated accurately.

This study has the following main findings:

- The prior HEP of 0.009841 was obtained which represents the current human safety level in the LNG bunkering industry. The analysis process showed the fuzzy BNCREAM model is efficient in performing the HEP assessment.
- Five hypothetical case studies demonstrated that an increase in the homogenized probability of CPCs leads to an increase in the human safety level. It can be seen that the CPCs provide insights that may improve the human safety level in an LNG bunkering project.
- The proposed model can be used to dynamically grasp the changes of HEP. If the reassessments identify the changes in the on-site CPCs, then these changes can be converted into quantitative data, where the input into the model obtains the latest HEP. Furthermore, this dynamic HEP assessment can be an input to a dynamic QRA model to obtain more accurate risk profiles.
To some extent, this study improved the original CREAM from a second-generation HRA to a third generation HRA method which can use computer-aided simulation techniques to evaluate HEPs.

The findings of this research fill a gap in the literature regarding the lack of quantitative HEP data for LNG bunkering operations. However, the generalizability of these results is subject to a limitation. The obtained HEP was based on the current human safety level in the LNG bunkering industry, and real-time variations in human safety levels during LNG bunkering operations may change the result of this study. For example, a largescale LNG bunkering might take more than 20 h , some CPCs' safety performances might change during such a time-consuming bunkering operation which generates real-time HEPs. Therefore, further research could be undertaken to explore the methodology for realtime prediction of HEP changes during LNG bunkering based on real-time data variations on site.

Supplementary Materials: The following are available online at https://www.mdpi.com/article/ 10.3390/jmse10030333/s1, Table S1: The conditional probability table of the BN model, Table S2: The weights of the experts, Table S3: The experts' expression on importance of SPFIs, Table S4: The experts' expression on performance of SPFIs.

Author Contributions: Conceptualization, H.F. and H.E.; methodology, H.F.; validation, H.F., H.E., and S.G.J.; formal analysis, H.F.; resources, H.F. and H.E.; data curation, H.F. and H.E.; writing-original draft preparation, H.F.; writing-review and editing, H.E. and S.G.J.; supervision, H.E. and S.G.J.; project administration, H.F. and H.E. All authors have read and agreed to the published version of the manuscript.
Funding: This research received no external funding.
Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: Not applicable.
Acknowledgments: The authors would like to express their gratitude to the experts who participated in the online questionnaire survey.

Conflicts of Interest: The authors declare no conflict of interest.

# Abbreviations 

