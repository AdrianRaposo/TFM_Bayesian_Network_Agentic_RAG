# E-synthesis for carcinogenicity assessments: A case study of processed meat 

Francesco De Pretis PhD ${ }^{1}$ (D) | Saana Jukola PhD ${ }^{2,3}$ (D) | Jürgen Landes PhD ${ }^{4,5}$ (D)<br>${ }^{1}$ Department of Communication and Economics, University of Modena and Reggio Emilia, Reggio, Emilia, Italy<br>${ }^{2}$ Department of Philosophy I, Ruhr-University Bochum, Bochum, Germany<br>${ }^{3}$ Institute for Medical Humanities, University Clinic Bonn, University of Bonn, Bonn, Germany<br>${ }^{4}$ Munich Center for Mathematical Philosophy, Faculty of Philosophy, Philosophy of Science and Study of Religion, Ludwig-MaximiliansUniversität München, München, Germany<br>${ }^{5}$ Open Science Center, Ludwig-MaximiliansUniversität München, München, Germany

## Correspondence

Jürgen Landes, PhD, Munich Center for Mathematical Philosophy, Faculty of Philosophy, Philosophy of Science and Study of Religion, Ludwig-Maximilians-Universität München, 80539 München, Germany. Email: juergen_landes@yahoo.de

Funding information
Deutsche Forschungsgemeinschaft, Grant/Award Numbers: 282210851, 405961989337 and 432308570


#### Abstract

Rationale, Aims and Objectives: Recent controversies about dietary advice concerning meat demonstrate that aggregating the available evidence to assess a putative causal link between food and cancer is a challenging enterprise. Methods: We show how a tool developed for assessing putative causal links between drugs and adverse drug reactions, E-Synthesis, can be applied for food carcinogenicity assessments. The application is demonstrated on the putative causal relationship between processed meat consumption and cancer. Results: The output of the assessment is a Bayesian probability that processed meat consumption causes cancer. This Bayesian probability is calculated from a Bayesian network model, which incorporates a representation of Bradford Hill's Guidelines as probabilistic indicators of causality. We show how to determine probabilities of indicators of causality for food carcinogenicity assessments based on assessments of the International Agency for Research on Cancer. Conclusions: We find that E-Synthesis is a tool well-suited for food carcinogenicity assessments, as it enables a graphical representation of lines and weights of evidence, offers the possibility to make a great number of judgements explicit and transparent, outputs a probability of causality suitable for decision making and is flexible to aggregate different kinds of evidence.


KEYWORDS
Bayesian network, cancer, causality, E-synthesis, evidence aggregation, meat

## 1 | INTRODUCTION

The number of studies investigating relationships between particular foods and particular aspects of cancer and its onset, prediction, prevention and treatment is growing at a rapid and increasing pace. However, growing bodies of evidence do not always produce consensus. For example, the possible causal relationship between the consumption of meat products and cancer is currently fiercely debated. ${ }^{1-7}$

Underlying this dispute is a disagreement on how to assess and amalgamate the available evidence. ${ }^{6}$ One side of the dispute insists on giving priority to well-conducted randomized controlled trials (RCTs) in drawing causal inferences from data. ${ }^{5,7-9}$ This side of the dispute denies that there is decisive evidence for a causal relationship if there are no RCTs showing a causal relationship. The other side of the debate maintains the sufficiency of observational studies and/or points to methodological deficiencies of RCTs investigating causal

[^0]
[^0]:    This is an open access article under the terms of the Creative Commons Attribution License, which permits use, distribution and reproduction in any medium, provided the original work is properly cited.
    (c) 2022 The Authors. Journal of Evaluation in Clinical Practice published by John Wiley \& Sons Ltd.

relationships between nutrition and cancer.10, 11, 12, 13 For example, observational studies are often much cheaper to conduct14 and hence record many more person years,15 and it is practically impossible to blind participants in RCTs on nutrition. Summing up, there is a dispute between evidence purists relying only on evidence of the prima facie highest quality16 and evidence pragmatists taking what in philosophy of science has been referred to as total evidence approach.17

The challenge arises for those taking a total evidence approach to aggregate evidence from different study methodologies into a final useful assessment. In particular, possible confounding and biases in observational studies should be modelled and then the thusly modelled evidence needs to be amalgamated with available RCTs. Even though there are some suggestions for strength of evidence assessment tools that take into consideration contributions of diverse methods,12 the aggregation of assessments of evidence originating from different study types (RCTs, observational studies and basic science studies) is often hard to carry out quantitatively18 and the final aggregation of assessments is then based on a narrative review. These reviews necessarily rely on a number of implicit and intransparent judgements that make the final assessment somewhat opaque.19 Furthermore, the final assessment is often communicated in a form that is not ready‐touse in concrete decision problems, for example, a probability that a certain action will lead to a desired outcome.

E‐Synthesis is an emerging tool for drug safety assessments,20, 21, 22, 23, 24, 25 modelling confounding and biases of observational studies and RCTs. It offers a principled approach to produce a posterior probability of causal relationships given evidence produced by diverse observational and randomized studies. In this study, we consider its applicability as a tool for food carcinogenicity assessments exemplified by an application to the disputed causal relationship between processed meat and cancer. E‐Synthesis can address the above mentioned challenges for aggregating bodies of evidence on food carcinogenicity, as it (1) seamlessly aggregates evidence from different methodologies (randomized studies, observational studies and mechanistic evidence), (2) it outputs a Bayesian probability26 that a food causes an adverse health effect in a population of food consumers that is ready‐to‐use for decision making and (3) it makes a number of judgements explicit and open to inspection and criticism that may remain opaque otherwise.

## MATERIALS AND METHODS

We now show how E‐Synthesis20, 21, 22, 23, 24, 25 can be employed as a tool for food carcinogenicity assessment, see also the Appendix (A Primer on Bayesian Reasoning).

### Theoretical constructs

A causal hypothesis linking a particular food or substance to (a particular) cancer in a population consuming this food or substance is the starting point. As such causal relationships cannot be observed directly, the framework incorporates indicators of causality, which are observable consequences of the causal hypothesis of interest. Learning that a nonempty subset of indicators of causality likely hold increases the probability that the causal hypothesis is true. Learning that a nonempty subset of indicators of causality likely fails to hold decreases the probability that the causal hypothesis is true. Absence of evidence does not lead to a change of probabilities. We here consider the causal hypothesis that processed meat consumption causes cancer.

The indicators of causality are based on best practice medical inference modelling Bradford Hill Guidelines, cf. Table 1.27 The International Agency for Research on Cancer (IARC) also employs these guidelines.28 The indicators are as follows: (1) probabilistic dependence, (2) dose--response relationship, (3) rate of growth, (4) mechanism, (5) temporality and (6) difference making. The indicators are true, respectively, if (1) there exists a positive correlation between processed meat consumption and cancer, (2) there is a clear DR between processed meat consumption and cancer, (3) the DR is strongly increasing, (4) there is a 'linkage between a direct molecular initiating event [...] and an adverse outcome at a biological level of organization relevant to risk assessment',29 (5) processed meat consumption precedes cancer on the relevant time scale and (6) there exists a counterfactual difference between processed meat consumption and cancer. In principle, E‐Synthesis is flexible to incorporate a set of different indicators of causality.

Evidence is then informative about subsets of indicators. For example, randomized studies in human populations are informative about difference making, observational studies of human populations can be informative about probabilistic dependence, dose--response relationship, rate of growth and temporality. Basic science studies inform us about the causality indicator called mechanism.

Evidential modulators apply to the studies to track the methodology and qualities of studies. Concerning internal validity, observational studies of human populations are modulated by their power (sample size), the time studied (duration), their covariate

TABLE 1 Mapping of Bradford Hill Guidelines into the E‐Synthesis framework according to Figure 221


Note: Italics here represent 'dimensions of scientific research'.


Note: We employed the mentioned simplification to binary variables with values 0 and 1. Here, 1 stands for a positive value, for example, the presence of sponsorship bias, and 0 stands for absence of sponsorship bias. The values specified in the table represent our assessments.
Abbreviations: A, adjustment and stratification; ES, effect size; Ind, indicator of causality; P, probability function; PD, probabilistic dependence; RoG, rate of growth; SS, sample size.

TABLE 2 Assessed studies, the indicators they pertain to, assessed modulators and conditional probabilities

TABLE 3 Posterior probability of $\odot$ (hypothesis of causality) with accumulating evidence for different initial priors (from $1 \%$ to $10 \%$ )


Note: Every row indicates the probability of $\odot$ given the body of evidence up to and including this row. Calculations are based on the Bayesian network formalism presented in Section 3; the conditional probabilities of the evidence are given in Table 2, and the graph of the Bayesian network (without modulator variables) is shown in Figure 2.
Abbreviation: $\odot$, causal hypothesis of interest.
analysis (adjustment and stratification) and the assessed conflicts of interest (sponsorship bias). Randomized studies of human populations are also modulated by what sets them apart from observational studies (blinding, randomization and placebo control). External validity is modulated by the degree to which the studied population is relevant (in terms of relevant similarities) to the target population.

These modulators influence how much the available evidence changes the plausibility of indicators of causality. For example, a poorly designed observational study reporting a rather weak dose-response relationship may only marginally increase our belief in the existence of an actual DR between processed meat and cancer. Since the existence of a dose-response relationship can also be due to confounding, our belief in the truth of the causal hypothesis increases even less.

### 2.2 | Bayesian network approach

This three-layered structure consisting of the causal hypothesis (Layer 1), testable consequences (Layer 2) and the evidence and its modulators (Layer 3) is an instance of a "Hierarchy-ofHypotheses" approach. ${ }^{30}$ A blueprint for creating Bayesian networks to compute a probability of the causal hypothesis in Layer 1 given modulated evidence (Layer 3) has been provided. ${ }^{31}$ E-Synthesis implements and modifies this blueprint providing a Bayesian network that allows one to calculate the probability of the causal hypothesis of interest given an available modulated body of evidence. An overview of the most important notation and abbreviations can be found in Table 4.

Bayesian networks are a popular tool for reasoning with and representing probabilities defined over a finite set of variables. ${ }^{32}$ The variables together with a set of directed arrows between pairs of variables form a directed acyclic graph. The graph is called directed due to the arrows having a direction. Acyclicity means that directed cycles are not permitted; it is hence impossible to walk along the arrows and return to the starting point. The set of directed arrows encodes probabilistic independence relations. To specify a probability function consistent with these independence relations, one first determines for every variable $X$ the set of its parent variables $\vec{Y}$. A variable $Y$ is called a parent of $X$, if and only if there exists a directed edge originating at the parent variable $Y$ pointing to said variable $X$. Secondly, for all truth values of all variables $X$ and all truths values of the respective set of parents, one chooses a probability between 0 and 1 . These choices have to sum to 1 in an appropriate sense, for every fixed variable $X$ and fixed truth values of all its parent variables $\vec{Y}=\vec{Y}$ the sum over the possible values of $X$ has to equal 1:

$$
\sum_{x} P\left(X=x \mid \vec{Y}=\vec{Y}\right)=1
$$

### 2.3 | The generic model

Applying E-Synthesis, we then create one variable for the causal hypothesis of interest (©), one variable for every indicator of causality ( $P D, D R, R o G, M, T, \Delta$ ), one variable for every

TABLE 4 Notation and abbreviations


study in the to be aggregated body of evidence and for every evidential variable a set of pertinent modulator variables is created.

Directed arrows are inserted as follows: there are six arrows originating from $\mathbb{\odot}$ pointing towards the six indicators of causality. If a study is informative about an indicator variable other than $P D$ or $D R$, then there is an arrow originating from the indicator variable and pointing to the evidential variable. Furthermore, RoG is a parent of $D R$ and $D R$ a parent of $P D$. If the indicator variable is $P D$ or $D R$, then the arrow is only inserted, if the study is not also informative about $D R$ or RoG, respectively. Finally, the modulator variables are the parents of their respective evidential variables, see Figure 1 for a graphical representation.

Probabilities of the variables conditional on the set of parent variables are set as described above. The probabilities reflect one's knowledge and judgements based on the available background knowledge.

## 3 | RESULTS

We now exemplify how E-Synthesis can be a tool for food carcinogenicity assessments by considering a possible causal relationship between processed meat and cancer. Our focus is on showing how an application of this tool works in principle. We hence only consider a few select studies rather than a substantial body of evidence. Furthermore, we focus on how to set (conditional) probabilities in principle and are less interested in the concrete values.
![img-0.jpeg](img-0.jpeg)

FIGURE 1 Graph of the Bayesian network with one report for every causal indicator variable given in Landes et al. ${ }^{21}$ The dots indicate that there might be further indicators of causality. The nodes reliability (REL) and relevance (RLV) are evidential modulators variables of studies, REP nodes.

### 3.1 Conditional probabilities of causality and its indicators

The prior probability of processed meat consumption causing cancer is based only on the available background knowledge and not on the specific evidence on meat consumption and cancer to be aggregated. This prior probability, $P(\mathbb{\sim})$, is eventually updated by the available and modulated evidence to a posterior probability, $P(\mathbb{\bigodot} \mathbb{\bigodot})$ (read as: probability of causality given the evidence $\mathcal{E}$ ). For ease of presentation all variables used are binary (with the exception of sample size (SS). As the value of $S S$ is known with certainty, $S S$ is not much of a variable, cf. Section 3.4). A generalization to variables of greater arity is straightforward but cumbersome.

Some conditional probabilities of the indicators of causality follow from their relationships (with $\mathbb{\sim}$ ). A strong dose-response relationship entails the existence of a dose-response relationship, which in turn entails a positive correlation. Furthermore, causality entails $T$ and $M$. Following De Pretis et al., ${ }^{20}$ we equate $\Delta$ with $\mathbb{\sim}$, as we are not interested in philosophical disputes on the nature of causality. We hence obtain the following conditional probabilities

$$
\begin{array}{cc}
P(D R \mid R o G)=1 & P(P D \mid D R)=1 \\
P(T \mid \mathbb{\bigodot})=1 & P(\Delta \mid \mathbb{\bigodot})=1 \\
P(\Delta \mid \overline{\mathbb{\bigodot}})=0
\end{array}
$$

Ontologically, the conditional probabilities of indicators of causality are best interpreted by natural frequencies, for example, the proportion of agents that cause cancer also do so in a strong dose-response relationship equals $P(R o G \mid \mathbb{\bigodot})$.

We extracted such frequencies from the IARC monographs for the remaining conditional probabilities of indicators of causality not covered by the above considerations, if $\mathbb{\sim}$ is true. The conditional probabilities we thus determine are $P(R o G \mid \mathbb{\bigodot}), P(D R \mid \overline{R o G} \& \mathbb{\bigodot})$ and $P(P D \mid \overline{D R} \& \overline{R o G} \& \mathbb{\bigodot})$.

How strongly Class 1 agents satisfied all nine of Hill's guidelines has been assessed (see Tables A1 and A2). ${ }^{33}$ To select a pertinent reference class for food carcinogenicity assessment, we firstly excluded all general occupational exposures (i.e., furniture and cabinet making), while including those with a selective definition (i.e., wood dust). Secondly, evidence of absence and absence of evidence for dose response were represented by the same number (Table A2). ${ }^{33}$ For thusly assessed agents, we studied the respective most recent IARC monograph and assessed whether IARC reported that RoG \& $\mathbb{\mathbb{\bigodot}}, D R \& \overline{R o G} \& \mathbb{\mathbb{\bigodot}}$ or $P D \& \overline{D R} \& \overline{R o G} \& \mathbb{\mathbb{\bigodot}}$ holds (Table A3) or whether there still is absence of evidence (Table A4). Our more fine-grained assessments of these agents supersede the previous assessments.

The nonsuperseded assessments by Swaen and van Amelsvoort, ${ }^{33}$ as well as our assessments of DR were translated into the conditional probabilities as follows. If this degree for an agent had been assessed to be $90 \%$ or greater, indicating a strong dose-response relationship, then we represented this as case of RoG \& $\mathbb{\mathbb{\bigodot}}$ being true. A degree between $50 \%$ and $90 \%$ is represented by $D R \& \overline{R o G} \& \mathbb{\mathbb{\bigodot}}$ and degree $<50 \%$ is represented by $P D \& \overline{D R} \& \overline{R o G} \& \mathbb{\mathbb{\bigodot}}$. For all agents where the dose-
response relationship was assessed to be below $50 \%$, a positive correlation between agent and cancer was assessed.

There are 68 agents relevant to our study, see Table A3. Thirtytwo agents were assessed to be in the range 90-100 indicating RoG and 29 agents were in the range 50-90 indicating a modest (not strong) dose-response relationship $D R \& \overline{R o G}$ and 7 agents were in the range $0-50$ indicating a lack of a dose-response relationship. We assessed that all agents in the range $0-50$ were positively correlated to cancer $P D \& \overline{D R} \& \overline{R o G} \& \mathbb{\mathbb{\bigodot}} .{ }^{1}$ So,

$$
\begin{aligned}
& P(R o G \mid \mathbb{\mathbb{\bigodot}})=\frac{32}{68}=\frac{8}{17}=47 \% \\
& P(D R \mid \overline{R o G} \& \mathbb{\mathbb{\bigodot}})=\frac{29}{68-32}=80 . \overline{5} \% \quad P(P D \mid \overline{D R} \& \overline{R o G} \& \mathbb{\mathbb{\bigodot}})=1
\end{aligned}
$$

Unfortunately, there is no suitable knowledge base from which we could extract the conditional probabilities for noncarcinogenic agents, that is, when $\overline{\mathbb{\mathbb{\bigodot}}}$ holds. We thus follow ${ }^{20}$ and let

$$
\begin{aligned}
& P(R o G \mid \overline{\mathbb{\bigodot}})=\frac{3}{700} \quad P(D R \mid \overline{R o G} \& \overline{\mathbb{\bigodot}})=\frac{18}{697} \\
& P(P D \mid \overline{D R} \& \overline{\mathbb{\bigodot}})=\frac{4}{97}
\end{aligned}
$$

In case there is no causal relationship between an agent and cancer in reality, we are indifferent on the truth value of temporality. Furthermore, due to the great number possible ways that agent could potentially cause cancer, we follow ${ }^{33}$ and adopt an indifference prior for $P(M \mid \overline{\mathbb{\bigodot}})=0.5$.

## 3.2 | Temporality

The indicator of causality called temporality concerns information about relevant temporal aspects of cancer and processed meat consumption, for example, is processed meat consumed within the right time frame to cause cancer or is cancer the reason for a change in diet? ${ }^{34,35}$

## 3.3 | Choice of body of evidence

At the end of 2015, IARC classified processed meat as a Class 1 carcinogenic agent. ${ }^{36}$ We wanted to assess primary evidence that has since then been produced. As we here restrict ourselves to exemplifying the application of E-Synthesis, we restricted our search to publications appearing in Nutrition and Cancer from January 2016 to December 2020.

On April 27, 2021, we searched that journal (search string: *processed meat*) and found 62 studies published between 2016 and 2020 (including studies published ahead of print). E-Synthesis is

[^0]
[^0]:    ${ }^{1}$ In principle, causality does not necessarily entail a positive correlation, as the following somewhat contrived example shows. Smoking causes cancer and reduces the distance one can run. Running along dirty roads also causes cancer. Thus, smoking has some preventative effect (in this hypothetical[!] example). If the numbers are set in just the right way, then smoking causes cancer but also prevents cancer at the same rate. On the population level, there may hence be no positive correlation between smoking and cancer.

a methodology for evidence aggregation, we hence excluded all studies that are aggregations of previously published studies and all studies that did not report specifically on processed meat. Furthermore, we excluded all studies that did not report processed meat as a separate category and all studies with surrogate measures severing the direct link between processed meat and cancer (e.g., studies only investigating the relationship between processed meat and inflammatory indexes and/or inflammatory indexes and cancer). We also excluded all basic science and animal studies; how ESynthesis can be employed to include such studies has been demonstrated. ${ }^{20,22}$

## 3.4 | Methodology of assessments

Nine studies satisfied all these constraints. We excluded one study reporting unclear results, ${ }^{37}$ which could not sensibly be modelled by our binary outcome variable, $E S \in\{0,1\}$ and $E S=1$ meaning that a significant effect was found. The remaining eight studies are enumerated in Table 2, where we also report the indicators they pertain to, their assessed evidential modulators and the relevant conditional probabilities, see Equation (1).
auTo simplify matters, we did not distinguish between different types of processed meat (which are rarely reported in the primary studies) and the different types and locations of cancer (there were only few studies on the same type and location of cancer). Furthermore, we do not distinguish between different processed meat consuming populations. We hence made the simplifying assumption of a perfect external validity and omitted the relevance variables.

Sponsorship bias was always assessed as nonpresent, as no thor reported commercial sponsorship, $S B=0$. Only one study stated adjustments for potential confounders. ${ }^{38}$ More thorough assessments of these modulators are required for more realistic applications of
E-Synthesis. To represent the sample size, we used a logarithmic modelling through a geometric progression of the type $a_{n}=2 \cdot a_{n-1}+100$, with $a_{0}=0 . S S$ was set to 0 if the reported sample of patients in the study was less than $a_{1}$, whereas $S S=1$ for $S S>1,022,100$. In between, we discretized the variable $S S$ with decimal step size.

None of the eight studies was assessed to be informative about T. All studies are observational. $T$ and $\Delta$ hence do not have children in the Bayesian network (Figure 2).

E-Synthesis uses the follow-up time after drug use as a relevant modulator for assessing the (un-)safety of a drug. In that context, it is relevant for how long patients are followed up after treatment. The studies we assessed here were all of a different study design; these studies all reported dietary patterns of patients diagnosed with cancer and controls. The duration of these studies, the time period of collected data, is irrelevant in these studies, what matters is the sample size. We hence excluded the duration variable in De Pretis et al., ${ }^{20} D$, from consideration. The formulae for conditional probabilities of observing a positive effect size given that the indicator holds, respectively, fails to hold, thus are

$$
\begin{aligned}
& P(E S=1 \text { ilnd })=0.5+\frac{A+S S}{4} \\
& P(E S=1 \text { innd })=0.5-\frac{A+S S}{4}
\end{aligned}
$$

These simplistic formulae exemplify the working of E-Synthesis. More work is required to obtain formulae more suitable for realworld assessments. ${ }^{39}$

The resulting Bayesian network is shown in Figure 2. As this exemplification of E-Synthesis does not require the modelling of uncertainties of evidence modulator variables, there are no relevance and no reliability variables displayed in the graph. Furthermore, as we did not consider basic science studies and there were no randomized
![img-1.jpeg](img-1.jpeg)

FIGURE 2 Directed acyclic graph of the Bayesian network used to compute the posterior probability of $\odot$ (Hypothesis of Causality). The considered studies are reported according to their study number (see Table 2). Evidential modulator variables are not shown to simplify the exposition.

![img-2.jpeg](img-2.jpeg)

FIGURE 3 Posterior probability of the causal hypothesis $\odot$ depending on the prior probability of $\odot$. Solid curve shows the posterior given all the evidence, dotted curve shows posterior of taking only the first study into account.
studies in our body of evidence, the variables $T, M$ and $\Delta$ do not have children.

## 3.5 | Aggregated evidence

We report the posterior probability of the causal hypothesis, $P(\odot \mid \mathcal{C})$, in Table 3 and Figure 3 depending on the prior probability, $P(\odot)$. We want to stress again that these values are obtained using simplistic formulae that have not been validated; Equation (1) and some conditional probabilities of indicators of causality still need significant further improvements.

These numbers display the dynamical behaviour of the posterior probability of $\odot$. This probability increases with every study reporting some positive association between processed meat and cancer and decreases with the null result. Furthermore, Figure 3 displays the lack of randomized and basic science studies. All evidence we collected consisted of observational evidence at the population level.

## 4 | DISCUSSION

## 4.1 | Comparing food safety assessments to drug safety assessments

Food and drug safety assessments share a number of common properties, which facilitate the repurposing of methodology. Firstly, RCTs normally fail to reach required numbers of patient months to reliably secure causal inferences. ${ }^{6,11,40-43}$ They fail for drug safety assessments, because they do not last long enough (adverse drug reactions may manifest only after a long time (years of treatment with olanzapine cause tardive dyskinesia, ${ }^{44}$ treatment of pregnant women with diethylstilbestrol (DES) caused vaginal adenocarcinoma in their pubertal and adult children ${ }^{45}$ ) and they study too few patients ${ }^{15}$ (serious adverse reactions may be very rare but so severe that the risk-benefit balance becomes negative in some cases, 1 fatality in every 10,000 patients ${ }^{46}$ ).

The (un-)safety of food stuffs and drugs depends on a greater number of concomitant factors including genetics, overall health and diet. Consuming moderated amounts of salted chips is, presumably, fine with a otherwise low salt diet but not with an otherwise high-salt diet. Drugs and their metabolites are also affected by our diet, even food stuffs that are apparently innocuous can cause major disruptions to the proper functioning of drugs, for example, the consumption of grapefruit juice is now known to have enabled fatal adverse drug reactions. ${ }^{47}$

Food and drugs are big business inducing significant incentives acting on market participants and evidence producers. Evidence is subsequently regularly biased. ${ }^{48-51}$ For instance, in drug research there have been cases of industry funded RCTs in which study outcomes have been chosen in a way that makes detecting adverse effects less likely. ${ }^{52}$ Similarly, the food and beverage industry has been linked to RCTs designed not to be able to detect negative effects of dietary choices. ${ }^{53}$ Evidence assessors and policymakers need to consider potential biases, including their own biases, at all times.

The need to assess and incorporate assessed biases in evidence aggregation procedures as well as hard questions about causal inference from data have contributed to the development of lively debates on (the) appropriate standards of evidence for safety assessments. Both in the context of assessing drug safety and in research to adverse health effects of food stuffs or dietary choices, it has been argued that RCTs may not be as strong as when drug efficacy claims are evaluated. ${ }^{6,54}$ Consequently, in both fields evidence assessment and aggregation methods alternative to GRADE and other tools placing the results from RCTs above other study types have been called for. ${ }^{54-58}$

There are also some dissimilarities to note. Firstly, plants and animals normally vary by location and season entailing that the nutritional value, chemical composition and so on of our food slightly varies in time and location. Virtually, all properly factory-produced drugs do not significantly vary.

In the European Union, nonrandomized studies are given explicit weight when it comes to drug safety assessments. The European Medicines Agency emphasizes the value of nonrandomized studies ${ }^{59}$ and called for efforts to amalgamate safety signals such as spontaneous case reports, data-mining, pharmacoepidemiological studies, drug utilization studies and nonclinical studies. ${ }^{19}$ The regulation of food safety assessments in the EU has yet to explicitly value evidence from nonrandomized evidence. The current regulation is noncommittal when it comes to evidence standards stating that assessments "shall be based on the available scientific evidence and undertaken in an independent, objective and transparent manner" (Regulation (EC) No 178/2002 §6.2).

### 4.2 E‐synthesis

The similarities between food and drug safety assessments make cross fertilization between the fields a priori plausible. Given the need to aggregate all the available evidence we chose to investigate the applicability of an E‐Synthesis approach to food safety assessments. We exemplified an application of E‐Synthesis on the suspected causal relationship between processed meat consumption and cancer. We gave a graphical summary of the lines of evidence (see Figure 2), made a number of judgements explicit and finally obtained a posterior probability of causality, which is suitable for decision making.

Although, E‐Synthesis has been originally developed for drug safety assessment, it is more appropriate for food carcinogenicity assessments in two respects. Firstly, no proposal has been made to incorporate case reports in E‐Synthesis. Although assessments of long‐ and short‐term use of drugs are often based on case reports,57, 60, 61 assessments of adverse health outcomes due to long term food consumption are normally not based on case reports. So, E‐Synthesis is better suited for typical food carcinogenicity assessments than for typical drug safety assessments. Secondly, the freely available IARC monographs permit us to calculate conditional probabilities of indicators of causality. Drug‐licensing agencies carrying out drug safety assessments do not publish documents listing all the evidence they base their assessments on.62 Determining appropriate conditional probabilities is hence much harder in drug safety assessments.

Challenges and controversies can arise in applications of E‐Synthesis when it comes to determining (conditional) probabilities. These probabilities represent assessments, for example, assessments of the degrees of sponsorship bias and blinding, as well as quality of covariate analysis. Assessments carried out by different actors are, in general, resulting in different probabilities. Differences between neutral researchers and experts working on behalf of food producers are bound to increase due to significant differences in their respective incentives. In our opinion, it would be wrong to blame these differences on the methodology used for safety assessments, as the methodology can only be as good as the assessments it uses as inputs. E‐Synthesis at least makes such assessments transparent and open to scrutiny and debate. Furthermore, such assessments can be treated as parameters enabling robustness analyses studying the (in‐)dependence of the posterior probability of © with respect to these parameters.

We hence find that E‐Synthesis can serve as a well‐motivated methodology for food carcinogenicity assessments.

### The meat and cancer debate

A series of articles published in the Annals of Internal Medicine in October 2019 reviewed evidence on the association between red and processed meat consumption and all‐cause mortality, cardiometabolic outcomes and cancer.2, 3, 4, 5, 6 The authors used systematic review methodology and the GRADE tool to assess the certainty of the evidence for the outcomes. The reviews concluded that the association between red and processed meat consumption and negative health outcomes is very small and the existing evidence is of low or very low certainty. In addition, the group of researchers published guidelines recommending that given the uncertainty of the existing evidence, adults can continue their red and processed meat consumption.7 The publication of these articles raised a storm of critical responses and counter responses.6, 9, 13

Our approach fits into this debate as a contribution providing a methodology for aggregating evidence from randomized and nonrandomized studies. Both sides of this debate may, in principle, use our approach. Their respective views on the weight of observational evidence is then reflected in different weights of the indicators of causality informed by observational evidence (conditional probabilities such as P(PDI©) and P(DRI©)). The ferocity of this debate makes it rather unlikely that both sides can agree on conditional probabilities. Our approach of determining (some of) these probabilities in an objective manner from a database of known carcinogenic agents may be a methodological approach both sides might be willing to pursue.

### Related work and the wider context

To conclude the study, we briefly mention relevant related works situating our approach in a wider context.

Bayesian networks continue to be a popular tool for artificial intelligence (applications) and evidence aggregation tasks. Their versatility has facilitated academic studies on nutrition and health,63, 64 as well as food safety65, 66 and patents for predicting responses to food (US patent).

The methodology for risk and safety assessments is continuously developing. There is a fruitful back‐and‐forth between regulators56, 67 and academia,62, 68, 69 as well as a growing number of proposals.70, 71, 72, 73, 74 A particular focus lies on the role of real‐world evidence (evidence obtained without randomization).75 With the passing of the 21st Century Cures Act in the United States, real‐world evidence may now also be used to argue for the efficacy of drugs. It seems unwise to assume that these methodological debates will soon be resolved.

Foundational aspects of these topics make contact with ethics,76 the notion of healthy food,77 cancer aetiology1 and causal inference causal inference in health sciences.21, 78, 79

## AUTHOR CONTRIBUTIONS

All authors contributed to the paper's conception, drafting, and revisions. All the authors gave their approval to the final version and take accountability for the research.

Saana Jukola gratefully acknowledges funding from the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) 282210851. Jürgen Landes gratefully acknowledges funding from

the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) 405961989 and 432308570. Open Access funding enabled and organized by Projekt DEAL.

## CONFLICTS OF INTEREST

The authors declare no conflicts of interest.

## DATA AVAILABILITY STATEMENT

We use data that has been reported in Swaen \& Amelsvoort ${ }^{33}$ but never published. The original data and the analysis of Swaen \& van Amelsvoort is documented in the supplementary material. The material is reproduced with their permission.

## ORCID

Francesco De Pretis (2) http://orcid.org/0000-0001-8395-7833
Saana Jukola (3) http://orcid.org/0000-0001-9740-309X
Jürgen Landes (3) http://orcid.org/0000-0003-3105-6624

## SUPPORTING INFORMATION

Additional supporting information can be found online in the Supporting Information section at the end of this article.

How to cite this article: De Pretis F, Jukola S, Landes J. E-synthesis for carcinogenicity assessments: a case study of processed meat. J Eval Clin Pract. 2022;28:752-772. doi:10.1111/jep. 13697

## APPENDIX A:

We now provide data and methodological details in a technical appendix.

## A. 1 | Data from Swaen \& Van Amelsvoort

The original data from Swaen \& Van Amelsvoort can be found in the Supplementary material.

## A. 2 | Our dose-response assessments

We assessed how strongly the agents in Table A2 relevant to our study satisfied Hill's dose-response criterion. Agents for which there was evidence are collected in Table A3 and those with absence of evidence are in Table A4.

## A. 3 | Decoding IARC monographs and rationales

For all the agents we assessed, we here list a decoding of the variables names in Swaen \& van Amelsvoort ${ }^{33}$ (see Table A2). Additionally, for each agent we provide the relevant IARC monographs, including the corresponding URL of the latest, and in case there is some evidence we also give a verbatim quote supporting our assessment. Finally, we list either and the assessed degree of dose response or conclude that there is absence of evidence.

TABLE A1 IARC Group 1 agents with (some) evidence of a dose response according to Swaen and van Amelsvoort. ${ }^{33}$


(Continues)

TABLE A1 (Continued)


Abbreviation: IARC, International Agency for Research on Cancer.

TABLE A2 IARC Group 1 agents with evidence of absence or absence of evidence of a dose response according to Swaen and van Amelsvoort ${ }^{33}$


TABLE A2 (Continued)


Note: Both these absences are represented by the column of zeros.

TABLE A3 Sixty-eight IARC Group 1 agents relevant to our study for which IARC reported sufficientevidence to assess the strength of (a possible) dose-response relationship


TABLE A3 (Continued)


TABLE A3 (Continued)


Note: Agents are ordered by the assessed strengths. Starred estimates originate from authors, nonstarred estimates are taken from Swaen \& van Amelsvoort ${ }^{23}$ (see Table A1). Further classification is provided through CAS numbers, volumes and related years. The former are unique numerical identifiers assigned to every chemical substance by the CAS, a division of the American Chemical Society. The latter refer to the IARC monographs where the agents are studied, with years pointing to the most recent publications in print.
Abbreviations: CAS, Chemical Abstracts Service; IARC, International Agency for Research on Cancer.

TABLE A4 Twenty-five IARC Group 1 agents relevant to our study for which IARC reported absence of evidence


TABLE A4 (Continued)


Note: The information was retrieved from Table A2 and these agents were omitted from our study. Similar to Table A3, for each agent proper CAS number, volume and year are reported.
Abreviations: CAS, Chemical Abstracts Service; IARC, International Agency for Research on Cancer.

- aurim.manuf: Auramine and auramine production. Auramine production 1 Sup 7, 99, 100F 2012. No dose-response information or not sufficient dose-response information. https:// monographs.iarc.who.int/wp-content/uploads/2018/06/ mono100F-12.pdf-absence of evidence.
- Azathioprine: 446-86-6 Azathioprine 1 26, Sup 7, 100A 2012. No dose-response information or not sufficient dose-response information. https://monographs.iarc.who.int/wp-content/uploads/2018/ 06/mono100A-20.pdf-absence of evidence.
- Nbischlonaph-Chlornaphazine: 494-03-1 Chlornaphazine 1 4, Sup 7, 100A 2012. No dose-response information or not sufficient dose-response information. https://monographs.iarc.who.int/wp-content/uploads/2018/06/mono100A-21.pdf-absence of evidence.
- boot + shoe-Boot and shoe manufacture and repair: Boot and shoe manufacture and repair (see Leather dust, Benzene) 25, Sup 7 1987. 'Occupational exposure'-absence of evidence.
- Butanediol-1,3-Butadiene: 106-99-0 1,3-Butadiene 1 Sup 7, 54, 71, 97, 100F 2012. 'A statistically significant dose-response trend was noted for all leukaemia. [...] Among men there was no indication of an increased risk for lung cancer and no evidence for an internal dose-response. Among women there was evidence of an increased risk for lung cancer, although there was no evidence for an internal dose-response in the exposed group. [...] Overall, the epidemiological evidence from the styrene-butadiene and the butadienemonomer industries clearly indicates an increased risk for haematolymphatic malignancies. Studies from the styrene-butadiene industry show an excess of leukaemia, and a dose-response relationship with cumulative exposure to butadiene, while studies from the monomer industry show an excess of haematolymphatic malignancies in general, attributable both to leukaemia and malignant lymphoma'. https:// monographs.iarc.who.int/wp-content/uploads/2018/06/mono100F26.pdf at p. 312-assessed degree of dose-response relationship 50.

- Semustine-Methyl-CCNU: 13909-09-6 Semustine [1-(2-Chloroethyl)-3-(4-methylcyclohexyl)-1-nitrosourea, Methyl-CCNU] 1 Sup 7, 100A 2012. 'A subsequent report described a strong dose-response relationship, adjusted for survival time, giving a relative risk of almost 40 among patients who had received the highest dose'. https://publications.iarc.fr/118 at p. 58-assessed degree of dose-response relationship 100.
- Chimny s-Chimney sweeping, that is, soot (s found in occupational exposure of chimney sweeps): Chimney sweeping (see Soot) 92 2010. 'Occupational exposure'-absence of evidence.
- Cyclosporin-Cyclosporine. 59865-13-3, 79217-60-0 Cyclosporine 1 50, 100A 2012. No dose-reponse information or not sufficient dose-response information. https://publications.iarc. fr/_publications/media/download/5195/47e16232b61bbce71c1 49f (...)-absence of evidence.
- Coal Gassif-Coal Gasification: Coal gasification 1 Sup 7, 92, 100F 2012. No dose-reponse information or not sufficient dose-response information. https://monographs.iarc.who.int/wp-content/uploads/ 2018/06/mono100F-15.pdf-absence of evidence.
- Coal.t.dest-Occupational exposures during coal-tar distillation: 8007-45-2 Coal-tar distillation 1 92, 100F 2012. No dose-reponse information or not sufficient dose-response information. https://monographs.iarc.who.int/wp-content/uploads/ 2018/06/mono100F-16.pdf-absence of evidence.
- Coaltarp-Coal-tar pitch: 65996-93-2 Coal-tar pitch 1 35, Sup 7, 100F 2012. 'When the workers were stratified by 1hydroxypyrene excretion in the urine, the amount of DNA strand-breaks in their leukocytes increased, and the 8-oxo-dG/ dG ratio decreased in a dose-dependent manner'. https:// monographs.iarc.who.int/wp-content/uploads/2018/06/mono1 00F-17.pdf at p. 165-assessed degree of dose-response relationship 100.
- Cyclophos-Cyclophosphamide: 50-18-0, 6055-19-2 Cyclophosphamide 1 26, Sup 7, 100A 2012. '[...] and a case-control study of leukaemia following ovarian cancer in the former German Democratic Republic where a strong dose-response relationship was observed'. https://monographs.iarc.who.int/wp-content/ uploads/2018/06/mono100A-9.pdf at p. 66-assessed degree of dose-response relationship 100.
- Des-Diethylstilbestrol: 56-53-1 Diethylstilbestrol 1 21, Sup 7, 100A 2012. 'The pituitary growth response of the diethylstilbestrol-treated ( 5 mg at $63 \pm 4$ days until 12 weeks of age) in F1 (COPxACI) rats was intermediate (6.9-fold) to that exhibited by the parental ACI and COP strains'. https:// monographs.iarc.who.int/wp-content/uploads/2018/06/ mono100A-16.pdf at p. 190-assessed degree of dose-response relationship 50.
- Epstein-bar-Epstein-Barr virus: Epstein-Barr virus 1 70, 100B 2012. 'Infectious condition'-absence of evidence.
- Erionite: No dose-reponse information or not sufficient dose-response information. https://publications.iarc.fr/ publications/media/download/5227/44041c781b3b6eb52ad87 (...)—absence of evidence.
- estro.nonst-Oestrogen-progestogen menopausal therapy (combined): Oestrogen-progestogen menopausal therapy (combined) 1 72, 91, 100A 2012. No dose-reponse information or not sufficient dose-response information. https://publications.iarc.fr/ 118-absence of evidence.
- etoposide + pl-Etoposide in combination with cisplatin and bleomycin: 33419-42-0, 15663-27-1, 11056-06-7. Etoposide in combination with cisplatin and bleomycin 1 76, 100A 2012. 'The risk for leukemia increased strongly with cumulative dose of etoposide in multivariate analyses'. https://publications.iarc.fr/118 at p. 99-assessed degree of dose-response relationship 100.
- Gallium ars-Gallium Arsenide. 1303-00-0 Gallium arsenide (see Arsenic and inorganic arsenic compounds) 86, 100C 2012. 'In female rats, dose-related responses were reported for the incidence of lung alveolar/bronchiolar tumours and atypical hyperplasia of the alveolar epithelium. In male rats, though treatment-related tumours were not observed, a dose-related increase in the incidence of atypical hyperplasia of the lung alveolar epithelium occurred'. https://publications.iarc.fr/120 at pp. 76-79-assessed degree of dose-response relationship 75.
- haemat.min-Haematite mining (underground): Haematite mining (underground) 1 1, Sup 7, 100D 2012. Occupational exposureabsence of evidence.
- elicib.pyl-Helicobacter pylori (infection with): 1 61, 100B 2012. 'Infectious condition'-absence of evidence.
- Hep.b-Hepatitis B virus (chronic infection with): Hepatitis B virus (chronic infection with) 1 59, 100B 2012. 'Infectious condition'absence of evidence.
- Hep.c-Hepatitis C virus (chronic infection with): Hepatitis C virus (chronic infection with) 1 59, 100B 2012. 'Infectious condition'absence of evidence.
- Herb.rem-Aristolochia (herbal medicine), Plants containing Aristolochic acid. 313-67-7 Aristolochic acid, plants containing 1 82, 100A 2012. 'Oral administration of aristolochic acid to rats caused a doseand time-dependent tumour response'. https://publications.iarc.fr/ Book-And-Report-Series/Iarc-Monographs-On-The-Identification-Of-Carcinogenic-Hazards-To-Humans/Pharmaceuticals-2012 at p. 357assessed degree of dose-response relationship 100.
- HIV-Human immunodeficiency virus type 1 (infection with). Human immunodeficiency virus type 1 (infection with) 1 67, 100B 2012. 'Infectious condition'-absence of evidence.
- HPV-Human papillomavirus types 16, 18, 31, 33, 35, 39, 45, 51, 52, 56, 58, and 59: Human papillomavirus types 16, 18, 31, 33, 35, $39,45,51,52,56,58,59,164,90,100 B$ 2012. 'Infectious condition'-absence of evidence.
- Htcel 1-Human T-cell lymphotropic virus type I (HTLV-I). Human T-cell lymphotropic virus type I 1 67, 100B 2012. 'Infectious condition'-absence of evidence.
- isopropalc-Isopropyl alcohol manufacture by the strong-acid process. Isopropyl alcohol manufacture using strong acids 1 Sup 7, 100F 2012. No dose-response information or not sufficient dose-response information. https://monographs.iarc.who.int/wp-content/uploads/ 2018/06/mono100F-32.pdf-absence of evidence.

- magenta.man-Magenta and magenta production: Magenta production 1 Sup 7, 57, 99, 100F 2012. No dose-response information or not sufficient dose-response information. https:// monographs.iarc.who.int/wp-content/uploads/2018/06/ mono100F-13.pdf-absence of evidence.
- red8methoxy-Methoxsalen plus ultraviolet A radiation: 298-81-7 Methoxsalen (8-methoxypsoralen) plus ultraviolet A radiation 124 , Sup 7, 100A 2012. 'The studies that undertook analyses by level of exposure to PUVA found dose-related increases in the incidence of squamous cell carcinoma'. https://monographs.iarc.who.int/wp-content/uploads/2018/06/mono100A-24.pdf at p. 365-assessed degree of dose-response relationship 100.
- Mineral oils: Mineral oils, untreated or mildly treated 133 , Sup 7, 100F 2012. 'Dose-related increase with $p$-value $<0.01$. [...] No comparison with unused oil, but the strong dose-response and the large number of animals per group are noted'. https://monographs.iarc.who.int/wp-content/uploads/2018/06/mono100F-19.pdf at p. 185-assessed degree of dose-response relationship 90.
- Mustard Gas: 505-60-2 Sulfur mustard 19 , Sup 7, 100F 2012. 'There was evidence of a dose-response relationship between exposure to mustard gas and subsequent development of respiratory cancer'. https://monographs.iarc.who.int/wp-content/ uploads/2018/06/mono100F-30.pdf at p. 439-assessed degree of dose-response relationship 100.
- Neutron Radiation: Neutron radiation 175, 100D 2012. 'Neutron radiation has clear carcinogenic effects in a variety of experimental animal studies in mice, rats and monkeys. [...] There is also evidence of an increased incidence of tumours as a function of dose in several studies in mice and one new study in rats. [...] There is inadequate evidence in humans for the carcinogenicity of neutron radiation. There is sufficient evidence in experimental animals for the carcinogenicity of neutron radiation'. https://monographs.iarc.who.int/wp-content/uploads/201 8/06/mono100D-8.pdf at p. 237-assessed degree of dose-response relationship 70.
- n.nitrosonic-N'-nitrosonornicotine and 4-(methylnitrosamino)-1-(3-pyridyl)-1-butanone. 16543-55-8, 64091-91-4 N'-Nitrosonornicotine (NNN) and 4-(N-Nitrosomethylamino)-1-(3-pyridyl)-1-butanone (NNK) 1 Sup 7, 89, 100E 2012. 'Two molecular epidemiology studies investigated the relationship of NNK to lung cancer in smokers using nested case-control designs. In one, urinary levels of NNAL plus its glucuronides (total NNAL), metabolites of NNK, were significantly associated with risk for lung cancer in a dose-dependent manner'. https://publications.iarc.fr/Book-And-Report-Series/Iarc-Monograph s-On-The-Identification-Of-Carcinogenic-Hazards-To-Humans/Perso nal-Habits-And-Indoor-Combustions-2012 at pp. 321-322-assessed degree of dose-response relationship 100.
- opishor. inf- Opisthorchis viverrini (infection with): Opisthorchis viverrini (infection with) 161, 100B 2012. 'Infectious condition'absence of evidence.
- painter-Painter (occupational exposure as a): Painter (occupational exposure as a) 147, 98, 100F 2012. 'Occupational exposure'-absence of evidence.
- Paving/roofing-Paving and roofing with coal-tar pitch (see Coaltar pitch): Paving and roofing with coal-tar pitch (see Coal-tar pitch) 35, Sup 7, 92, 100F 2010. 'Occupational exposure'-absence of evidence.
- phosphorous32-Phosphorus-32: 14596-37-3 Phosphorus-32, as phosphate 178, 100D 2012. 'Furthermore, the risk of leukemia increased with increasing doses of 32-P'. https://publications.iarc.fr/ Book-And-Report-Series/Iarc-Monographs-On-The-Identification-Of-Carcinogenic-Hazards-To-Humans/Radiation-2012 at p. 287assessed degree of dose-response relationship 100.
- rubber.ind-Rubber manufacturing industry. Rubber manufacturing industry 1 28, Sup 7, 100F 2012. 'Occupational exposure'absence of evidence.
- salt.fish-Chinese-style salted fish: Salted fish, Chinese-style 156, 100E 2012. 'A dose-response relationship was found in two smaller studies, with odds ratios ranging from 3.4 to 5.7 in the most exposed individuals (salted fish at least three times/week). [...] In a Southern Chinese population an increased risk for oesophageal cancer was associated with adult salted fish consumption in women, but not in men, and there was no dose-response relationship from both sexes combined'. https:// publications.iarc.fr/Book-And-Report-Series/Iarc-Monographs-On-The-Identification-Of-Carcinogenic-Hazards-To-Humans/Personal-Habits-And-Indoor-Combustions-2012 at pp. 505-506-assessed degree of dose-response relationship 40.
- Schistosoma - Schistosoma haematobium (infection with). Schistosoma haematobium (infection with) 161, 100B 2012. 'Infectious condition'-absence of evidence.
- Shale oil-Shale oils: 68308-34-9 Shale oils 135 , Sup 7, 100F 2012. 'Crude shale oil and its aromatic fractions were enclosed in bee's wax pellets-which allow slow release of the content-and implanted in the lungs of rats. The substances induced a dosedependent increase in lung cancer (epidermoid carcinomas)'. https://monographs.iarc.who.int/wp-content/uploads/2018/06/ mono100F-20.pdf at pp. 199-202-assessed degree of dose-response relationship 100.
- Solar rad-Natural sunlight: Solar radiation 155, 100D 2012. 'The dose-response relationship with recalled average annual hours spent in outdoor activities was incosistent. [...] Risk was increased with cumulative sun exposure in outdoor work during the summer months, but without any dose-response (OR 11.7-12.7; with wide confidence intervals). [...] In the other two, which were more recent and had better measures of exposure than many previous studies, one study related only to occupational sun exposure and showed a strong association with a dose-response relationship, and the strongest association seen in the other was with occupational sun exposure and showed evidence of a dose-response relationship'. https://monographs.iarc.who.int/ wp-content/uploads/2018/06/mono100D-6.pdf at pp. 42-43, 62 -assessed degree of dose-response relationship 50.
- smokl.tob-Smokeless tobacco: Tobacco, smokeless 1 Sup 7, 89, 100E 2012. 'Dose-response relationships were observed in several studies. [...] Strong dose-response relationships have been

observed in studies in the USA with intensity and duration of use of smokeless tobacco, snuff or chewing tobacco'. https:// monographs.iarc.who.int/wp-content/uploads/2018/06/mono1 00E-8.pdf at pp. 280, 283-assessed degree of dose-response relationship 100.

- Strong mists-Mists from strong inorganic acids. Acid mists, strong inorganic 1 54, 100F 2012. 'Soskolne et al. (1992) assessed the duration and intensity of exposure to sulfuric acid among laryngeal cancer cases in a case-control study in Canada and found a dose-response progression from 10 years of probable exposure (OR, 1.97; 95\%CI: 0.6-6.1) to $>10$ years of substantial exposure (OR, 5.6; 95\%CI: 2.0-15.5)'. https://publications.iarc.fr/ publications/media/download/3076/73443059d4ec0adde7332 (...) at p. 492-assessed degree of dose-response relationship 100.
- talc.asbest-Talc containing asbestiform fibres (see Asbestos): 1332-21-4, 12172-73-5, 12001-29-5, 12001-28-4. Asbestos (all forms, including actinolite, amosite, anthophyllite, chrysotile, crocidolite, tremolite) 1 14, Sup 7, 100C 2012. 'From IARC List of Classification, additional information for Asbestos: Mineral substances (e.g., talc or vermiculite) that contain asbestos should also be regarded as carcinogenic to humans'. Repeated entry from Table A1. See Asbestos.
- Thiotepa: 52-24-4 Thiotepa 1 Sup 7, 50, 100A 2012. 'This study, which used a case-control methodology within a cohort of women treated for ovarian cancer, found a strong association between the risk for leukaemia and treatment with thiotepa with a relative risk of 8.3 in the lower dose group $(n=4)$, and 9.7 in the higher dose group $(n=5)$. [...] The increase in the incidence of forestomach papillomas was dose-dependent in rasH2 mice (Yamamoto et al., 1998a, b). [The Working Group noted the limited reporting of the study, i.e., no tumour incidences were provided.]'. https:// publications.iarc.fr/_publications/media/download/5187/1c46 1f2a92d04f2f5da5dbb (...) at pp. 164, 166-assessed degree of dose-response relationship 70.
- Treosulfan: 299-75-2 Treosulfan 1 26, Sup 7, 100A 2012. 'In an international case-control study of women treated for ovarian cancer, Kaldor et al. (1990) found that the relative risk was 3.6 in the group treated with the lowest dose of treosulfan, and 33.0 within the highest dose group. [The Working Group noted that there may have been an overlap between the two studies, as the case-control study included Denmark, and covered a similar time period as the Danish cohort study.]'. https://monographs.iarc.who. int/wp-content/uploads/2018/06/mono100A-15.pdf at p. 172assessed degree of dose-response relationship 70.
- wooddust-Wood dust. Wood dust 1 62, 100C 2012. Repeated entry from Table A1. See Furniture and cabinet making.


## A. 4 A primer on Bayesian reasoning

We now briefly introduce key elements of the Bayesian approach to uncertain inference.

1) Bayesian approaches interpret probabilities as an agent's rational degrees of belief. The probabilities represent the agent's
knowledge, beliefs and evidence. The probabilities are thus epistemic in that they represent an agent's view of the world and not necessarily the actual world. Probabilities can be elicited and interpreted via betting scenarios: the betting quotient at which a rational agent is willing to buy and sell bets on a proposition of interest is her probability of that proposition. Unlike in Bayesian statistics, propositions of interest are not limited to (parts of) statistical models. ${ }^{87,88}$
2) To adopt a probability Bayesian agents fix a finite set of elementary events $\Omega$. Propositions of interest are then identified with subsets of $\Omega$. An initial, prior, probability function is then adopted by the agent, which takes her background knowledge (e.g., theory and expert opinion) into account but not the evidence that she later learns. The prior probability function represents the agent's belief at an very early stage of her epistemic life. To set these probabilities we first learn how to set them in rather uncontroversial settings (e.g., die rolls and roulette) and later move to more realistic problems.
3) Evidence the agent acquires is then used to update her beliefs. In case the evidence is certain, the agent learns that the actual world is surely within some nonempty subset $F \subset \Omega$, probabilities are updated by conditionalization. In case the evidence is uncertain, the agent learns that the actual world is in $F$ with probability $0<p<1$, Jeffrey updating is used. The belief updates produce posterior probabilities.
4) Confirmation tracks how the posterior probability of a hypothesis of interest changes with the agent acquiring new evidence. The most popular and simple way to measure confirmation is to consider the difference between prior and posterior probability of the hypothesis, although other measures continue to attract interests. ${ }^{89}$
5) Evidence of absence means that the agent has information which decreases the probability that the hypothesis of interest is true. Conversely, absence of evidence means that the agent does not possess evidence that makes the hypothesis of interest more or less likely. Clearly, evidence of absence and absence of evidence have to be distinguished in a Bayesian setting. Although, absence of evidence leaves the relevant probabilities unchanged, there is a growing consensus that confirmation via nonempirical considerations is possible. ${ }^{90}$
6) Decisions are made by performing the act that maximizes expected utility. The agent first determines a finite set of possible acts $A$. Every ordered pair of an act $\sigma$ and a possible world $\omega$ is then assigned some utility, $u(\sigma, \omega) \in \mathbb{R}$. The expected utility of act $\sigma$ is then $\sum_{\omega \in \Omega} P(\omega) u(\sigma, \omega)$. Acting in a way that maximises expected utility is deemed rational, acting in a way that affords the agent less expected utility is considered irrational. ${ }^{91}$
7) E-Synthesis applies the Bayesian approach. The probabilities represent an agent's degrees of belief aiming to determine a probability that eating processed meat causes cancer. The set of elementary events is generated by the set of variables used to reason about this probability. Evidence comes in the form of studies. Confirmation is reported in Table 3. Evidence of absence

needs to differentiated from absence of evidence; we hence could not simply copy the assessment scheme of Swaen \& van Amelsvoort. ${ }^{33}$
8) Common objections to the Bayesian approach and counterarguments are now briefly considered.
i) Objection: The Bayesian approach falsely offers a precise real number as a probability of a hypothesis the inquiring agent remains unsure about. These probabilities appear out of thin air. Counterargument: Bayesian probabilities are a representation of an agent's state of mind given a prior belief and an updating procedure for acquired evidence. Bayesian probabilities are not necessarily objective nor do they necessarily track the truth. The fact that a single real number is assigned to a hypothesis of interest is owed to the choice of representing rational degrees of belief. The posterior probability function depends on the choice of $\Omega$ and the prior.
ii) Objection: The Bayesian approach does not make all information explicit and fails to take all information into account. Counterargument: It is true that not all information is made explicit. In general, choosing a small event space, $\Omega$, entails that a great deal of information remains implicit in the prior probability function. Furthermore, it is simply infeasible to build models that can take all information explicitly into account. This infeasibility besets all formal models of uncertain inference. The quality of the inferences does, in general, depend on the quality of the underlying event space. It is hence important to adopt an appropriate event space.
iii) Objection: A single probability function is not an appropriate model of rational degrees of belief. There are two main competitors to the Bayesian approach: i) the imprecise probabilities approaches uses sets of probability functions, rather than a single probability function, to model degrees of belief. ${ }^{92}$ ii) Ranking functions are used to avoid having to attach precise numbers to uncertain events. ${ }^{93}$
iv) Objection: The Bayesian approach is hopelessly subjective. Counter-arguments: (i) Bayesian probabilities are based-to the best of the agent's abilities-on her information. These probabilities hence represent the agent's considered judgements. ${ }^{94}$ (ii) In realistic cases, subjectivity is not going to make a large difference to the posterior and the Bayesian approach is virtuous in other important senses. ${ }^{95}$ (iii) The choice of a prior ought to be an objective one, which can be achieved by an application of a principle of entropy maximization. ${ }^{96}$ (iv) The subjectivity can be investigated and reduced by performing numerical sensitivity analyses.