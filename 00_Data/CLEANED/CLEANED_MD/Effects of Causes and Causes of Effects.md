# Effects of Causes and Causes of Effects 

A. Philip Dawid ${ }^{1}$ and Monica Musio ${ }^{2}$<br>${ }^{1}$ Statistical Laboratory, University of Cambridge, UK; email:<br>apd@statslab.cam.ac.uk<br>${ }^{2}$ Dipartimento di Matematica ed Informatica, Università degli Studi di Cagliari, Italy; email: mmusio@unica.it

Xxxx. Xxx. Xxx. Xxx. YYYY. AA:1-28
https://doi.org/10.1146/((please add article doi))

Copyright (C) YYYY by Annual Reviews. All rights reserved

## Keywords

causal Bayesian network, counterfactual, decision theoretic causality, directed acyclic graph, instrumental variable, interval of ambiguity, potential outcome, probability of causation, statistical causality, stochastic causal model, structural causal model, structural equation model, twin network


#### Abstract

We describe and contrast two distinct problem areas for statistical causality: studying the likely effects of an intervention ("effects of causes"), and studying whether there is a causal link between the observed exposure and outcome in an individual case ("causes of effects"). For each of these, we introduce and compare various formal frameworks that have been proposed for that purpose, including the decision-theoretic approach, structural equations, structural and stochastic causal models, and potential outcomes. It is argued that counterfactual concepts are unnecessary for studying effects of causes, but are needed for analysing causes of effects. They are however subject to a degree of arbitrariness, which can be reduced, though not in general eliminated, by taking account of additional structure in the problem.

# INTRODUCTION 

## 1. Overview

The enterprise of "statistical causality" has seen much activity in recent years, both in its foundational and theoretical aspects, and in applications. However it remains rare to draw the distinction (recognised by Mill (1843)) between two different problem areas within it: assessing (in individual cases, or in general) the likely effects of applied or considered interventions - the problem of "effects of causes", EoC; and assessing, in an individual case, whether or not an observed outcome was caused by an earlier intervention or exposurethe problem of "causes of effects", CoE. Where this distinction is made, it is typically assumed that both problems can be represented and addressed using a common theoretical framework, such as the structural causal model of Pearl (2009).

The purpose of the current article is to emphasise the important logical and technical differences between EoC and CoE problems, and to explore and compare the various ways in which problems of each kind can be and have been formulated. In particular it is argued that different tools are appropriate for the two different purposes.

In $\S 2$ we introduce the variety of concerns to be addressed, in the context of a specific law suit. In Part I we introduce and compare a variety of formalisms that have been proposed to address "Effects of Causes". Section 4 briefly summarises some philosophical and implementational issues. Section 5 introduces, with examples, the problem of inference in the presence of an instrumental variable, which is then used throughout Part I as a hook on which to hang the general discussion. Section 6 describes purely probabilistic aspects. Then $\S 7$ introduces the decision-theoretic approach to EoC, $\S 8$ an approach based on linear models, $\S 9$ a nonparametric generalisation of that, and $\S 10$ the approach based on potential outcomes.

We turn to address "Causes of Effects" in Part II, for problems similar to those of $\S 2$. Section 11 points to the need for counterfactual inference, which can not however totally resolve the ambiguities inherent in such problems. Two ways of conducting counterfactual modelling are described in $\S 12$, which can both be subsumed in the potential outcome approach of $\S 13$. In $\S 14$ we consider how empirical data can be used to inform CoE analysis, but can not totally resolve the inherent ambiguities. In $\S 15$ we apply this to address the legal CoE issues of $\S 2$, showing how the basic ambiguity, expressed by interval bounds on the "probability of causation", can be refined when we can observe other variables in the problem. Section 16 indicates just how limited our CoE analyses have been, and what difficulties might attend further extension.

Our concluding remarks summarise some of the lessons to learned from this review of the different approaches to EoC and CoE.

## 2. A law suit

In 2014 a class action ("multidistrict litigation", MDL) was brought in the United States by more than three thousand women who sued the pharmaecutical company Pfizer, claiming that they developed (type 2) diabetes as a result of taking its drug Lipitor (Atorvastatin Calcium) (Case Report 2015). The plaintiffs identified two "bellwether cases" of women making such a claim for closer attention.

In order to succeed in such a suit, the plaintiffs would have to demonstrate, in succession,

to the Law's satisfaction, two points (Dawid et al. 2014):
General causation: Can Lipitor cause diabetes?
Specific causation: In the individual cases, did Lipitor cause their diabetes?
The eventual judgment was in favour of Pfizer. It was judged that general causation had not been established for doses $10 \mathrm{mg}, 20 \mathrm{mg}$ and 40 mg of the drug, but could be considered for the 80 mg dose. And with regard to the bellwether cases, it was judged that specific causation could not be established.

The distinction the court made between the two varieties of causal question, general and specific, is fundamental, and occurs in many contexts. It has various descriptions. Philosophers talk of "type" and "token" causation. Legal scholars talk of "group" and "individual" causation, and have coined the expression G2i ("Group to individual") for the task of arguing from one to the other (Faigman et al. 2014). In statistical contexts we may talk of inference about "the effects of causes" (EoC), and "the causes of effects" (CoE), which are the designations we mostly use here.

# 3. Statistical and causal questions 

Questions about individual cases can usefully be organised in a fourfold classification. We exemplify these for the bellwether case of Juanita, who is 55 years old, has a total cholesterol of $250 \mathrm{mg} / \mathrm{dL}$, LDL of $175 \mathrm{mg} / \mathrm{dL}$, HDL of $46 \mathrm{mg} / \mathrm{dL}$, triglycerides of $142 \mathrm{mg} / \mathrm{dL}$, weighs 176 lbs , and has a body mass index (BMI) of 26.37 .

Forecasting: Juanita has started taking a 80 mg dose of Lipitor daily. Is she likely to develop diabetes?
Backcasting: Juanita has developed diabetes. Did she take Lipitor, and if so in what dose and for how long?
Decision: Juanita is considering whether to take Lipitor, but is worried about developing diabetes. What should she do?
Attribution: Juanita took Lipitor 80mg daily for 3 years, and developed diabetes. Was that because she took Lipitor?

While Forecasting and Backcasting are fundamentally purely statistical exercises, Decision and Attribution can be classified as "causal" questions-the former addressing "Effects of Causes" (EoC), and the latter, "Causes of Effects" (CoE).

Forecasting. This is an apparently straightforward statistical task, at least conceptually: we gather high quality data on individuals sufficiently like Juanita, taking the same treatment, and observe the proportion going on to develop diabetes. In practice this simple recipe will be complicated by non-random sampling of cases, differences in background characteristics, difficulties associated with long-term follow-up, censoring by death, etc., etc. Handling such complications has been a prime focus of statistical research over many decades, and though the issues raised are very far from trivial, they raise no new issues of principle. But we would also need to argue that the proportion, estimated from the data, of individuals developing diabetes can be identified with Juanita's "individual risk". While this does raise some subtle philosophical issues (Dawid 2017), they can largely be ignored for practical purposes.

Backcasting. This refers to the task of "predicting" uncertain past events on the basis of later observations. In a statistical context, this is most typically performed by application of Bayes's theorem. Suppose we do not know whether or not Juanita took the Lipitor, but, as above, have estimated the two "forward" forecast probabilities, under each scenario. We would also need to assign a prior probability to the event that she did, in fact, take the drug. Bayes's theorem supplies the machinery for combining these ingredients to produce the required "backward" probability that she indeed took Lipitor, on the basis of her having developed diabetes. Although such Bayesian inferences have, from the very beginning, often been described as estimating the "probabilities of causes", use of the term "cause" here is not really appropriate, since even if we can conclude that Juanita had taken Lipitor, that might not have been the cause of her diabetes.

Applying Bayes's theorem is not the only way to conduct backcasting. More straightforwardly, we could simply collect a sample of individuals sufficiently like Juanita, confine attention to those who develop diabetes, and use the proportion of these who had taken Lipitor to estimate the desired probability for Juanita. Indeed, there are circumstances where this simple approach may be preferable to the Bayesian route (Dawid 1976).

Decision. Forecasting is of fundamental importance in decision analysis. Suppose Juanita has not yet started taking Lipitor, and is considering whether or not to do so. One of her concerns is whether she will develop diabetes. She should thus consider, and compare, how probable this event is under two possible scenarios: that she does, or that she does not, take the drug. This would requires two separate forecasting exercises, and correspondingly data from two different sets of individuals, according as they do or do not take Lipitor.

But new difficulties now arise in gathering and using such data. In particular, the very treatment desired by such an individual might be related to her overall health status, and thus affect her risk of developing diabetes - even were she not to receive that desired treatment. In such as case it becomes problematic to disentangle the effects of desire for treatment and of application of treatment. This is an example of the problem of "confounding", which requires careful attention in such cases.

Attribution. Questions of forecasting, backcasting and decision, although beset with many practical difficulties, can all, in principle at least, be answered directly by means of probabilities attached to unknown events of interest, probabilities that can be estimated given suitable data. However, a question of attribution-such as "did taking Lipitor cause Juanita's diabetes" - is not so readily resolved. For what is it now that is unknown? We know that Juanita took Lipitor, and we know that she developed diabetes. There is no unknown event about which we require inference. Rather, it the relationship between these events that is uncertain-was it causal, or not? Even to understand what we might mean by such a question is problematic.

We shall consider how to formalise such questions, and explore just what can be concluded from data about them, in Part II below.

# Part I 

## Effects of Causes

## 4. Introduction

### 4.1. Causality and agency

Philosophers have debated causality for millennia, and have propounded a large variety of conceptions and approaches. Statisticians, on the other hand, had traditionally been reluctant to imbue their inferences with causal meaning. But in recent years much more attention has been given to what we can now term "statistical causality". Particularly influential have been the contributions of Rubin (1974), who promoted a formulation based on "potential outcomes", and of Pearl (2009), based on graphical representations.

Implicit in both these approaches is the idea of a cause as an intervention applied to a system, in line with the "agency" interpretation of causality (Reichenbach 1956, Price 1991, Hausman 1998, Woodward 2003, 2016). A main task for statistical causality is to make inference about the effects of such interventions-that is, understanding the "effects of causes"-on the basis of data. When making use of data, it is important to distinguish between data generated through experimentation and purely observational data.

### 4.2. Experiment

In an experiment, interventions are made on experimental units according to some known protocol, often involving randomisation, and their responses measured. To the extent that the experimental units and interventions can be regarded as representative of future interventions on new units, it is in principle straightforward to infer what effects those interventions will have in future. "Design and analysis of experiments" is a major enterprise within modern statistics, involving many subtle and technical considerations, but no special issues of principle arise.

### 4.3. Observation

Things are not so straightforward when the data available are purely observational, and the process whereby treatment interventions were applied to units is not known. For example, when choosing between two treatments, a doctor may have given one preferentially to those patients he considers sicker. Then a simple comparison of the outcomes in the two treatment groups will be misleading, since even if there is no difference between the treatments, a difference in outcomes may be seen because of the difference in general health of the two treatment groups. This is the problem of "confounding", which prevents us from taking the observational data at face value. In such a case it may or may not be possible to assess, by more sophisticated means, genuine causal effects, depending on what is observed and what assumptions can reasonably be made. If we know or can reasonably assume how the doctor behaved, and have data on the patient characteristics that the doctor used, then we can make meaningful comparisons and extract causal conclusions; but-in the absence of further structure or assumptions-this will not be the case if either of the conditions fails.

Much of the modern enterprise of statistical causality is focused on addressing this issue of extracting causal conclusions from observational data. In order to do so, it will invariably be necessary to make assumptions, generally untestable in practice, about the relationship

between the behaviours of the "idle" observational system, which generates the observed data, and the same system under a specified intervention-which is what it wanted, but is not directly observed. Such assumptions are sometimes made explicit, and so open to reasoned scrutiny and debate, but sometimes they remain implicit and hidden, being taken for granted without critical examination. The kind of relationships required can typically be expressed, explicitly or implicitly, as asserting the equality of certain ingredients in both idle and interventional circumstances. While such invariance properties have sometimes been taken as the very definition of causality (Bühlmann 2020), they can be applied without any such philosophical commitment. (Our own philosophical standpoint remains that based on agency.)

The "do-calculus" (Pearl (2009, §3.4); see also Dawid (2015, §9.7)) applies to problems that can be modelled by means of a directed acyclic graph, representing both assumed conditional independence properties of the observational regime, and assumed relationships between the observational and interventional regimes. For such a case it supplies a complete method for determining whether a causal estimand of interest can be identified from observational data, and if so how.

# 5. Instrumental variable 

Below we shall introduce, compare and contrast some of the different statistical formalisms that have been used to model effects of causes. To be concrete, we shall consider, for each formalism, how it might model an instrumental variable problem (Bowden \& Turkington 1984). This involves, in addition to the treatment variable $X$ and response variable $Y$, a further observed variable $Z$ (the instrument), and an unobserved variable $U$-all defined for individuals in a study or larger population. Typically $Z$ is binary, $X$ and $Y$ are binary or continuous, and $U$ is multivariate. Note that in this problem it is not possible, without imposing still further structure, to identify the causal effect of $X$ on $Y$ from observational data.

We suppose:
(a). $U$ is a set of pre-existing characteristics of the individual
(b). $Z$ is associated with $X$, but not with $U$
(c). While $X$ could in principle be assigned externally, in the study it was not
(d). "Exclusion restriction": Given $X$, and the individual characteristics $U$, the response $Y$ is unaffected by $Z$. (This vague requirement will be clarified further below).

## Example 1 Encouragement trial

In an encouragement trial (Holland 1988), students are randomly assigned to receive encouragement to study. However, a student may not or may not respond to the encouragement. Here $Z$ is a binary assignment indicator, taking value 1 for encouragement, 0 for no encouragement; $X$ is the number of hours the student actually studies; $Y$ is the student's score in the final test; and $U$ comprises individual characteristics of the student, that may affect both $X$ and $Y$; because of randomisation, $Z$ is independent of $U$. We are interested in how a student's choice of study hours affects their test score.

## Example 2 Incomplete compliance

In a medical trial, each patient is randomly assigned to take either active treatment $(Z=1)$ or placebo $(Z=0)$. However, the patient may not comply with the assignment, so that the treatment actually taken, $X=1$ or 0 , may differ from $Z$. Finally we observe whether

the patient recovers $(Y=1)$ or not. We allow for possible dependence of both $X$ and $Y$ on further unobserved patient characteristics, $U$. Again, randomisation ensures that $Z$ is independent of $U$. We are principally interested in the effect of taking the treatment on recovery.

# Example 3 Availability trial 

In a variation of Example 2, $Z=1$ means the active treatment is made available to the patient, $Z=0$ that it is not; $X=1$ if the treatment is taken, $X=0$ if not. It is supposed that if the treatment is unavailable $(Z=0)$ it can not be taken $(X=0)$ (though it need not be taken when it is available).

## Example 4 Mendelian randomisation (Katan 1986)

Low serum cholesterol level $(X=1)$ is thought to be a risk factor for cancer $(Y=1)$. Both serum cholesterol and cancer may be affected by indicators of lifestyle $(U)$. Possession of the E2 allele $(Z=1)$ of the apolipoprotein E (APOE) gene is known to be associated with low serum cholesterol level: this relationship need not be causal, but may arise because APOE is in linkage disequilibrium with the actual causative gene. Since "Nature" randomises the APOE allele at birth, and its level is not thought to affect lifestyle, $U$ should not be associated with $Z$. We are interested in whether intervening to raise serum cholesterol could lower the risk of cancer.

There are a number of questions we could ask (but not necessarily be able to answer) in such examples. In Example 2, these might include:
(i). "What is the probability of recovery for a patient who is assigned to active treatment (irrespective of the treatment actually taken)?"
(ii). "What is probability of recovery for a patient who (irrespective of assigned treatment) in fact took active treatment?"
(iii). "What is the probability that a patient who recovered complied with the assignment?"
(iv). "What is the effect on recovery of assignment to treatment?"
(v). "What is the causal effect of taking the treatment on recovery?"

Questions (i), (ii) and (iii) inhabit the lowest rung, "seeing", of Pearl's "ladder of causation" (Pearl \& Mackenzie 2018), the first two being instances of "forecasting", and the last of "backcasting". Questions (iv) and (v) are on the second rung of the ladder, "doing", being instances of "decision". In the sequel we shall mainly be interested in (v). Since $Z$ has been randomised, we could argue that the "intention to treat" question (iv) is essentially the same as (i), which can be straightforwardly addressed from the study data on $(Z, Y)$. However, (v) can not readily be answered in the same way as (ii) (an "as treated" analysis), since $X$ has not been randomised, and any observed association between $X$ and $Y$ might be due to their common dependence on $U$.

## 6. Seeing: Conditional independence

We first consider how to express, formally, purely probabilistic properties of the observational joint distribution of $(X, Y, Z, U)$. This is all that is required to address forecasting and backcasting questions such as (i)-(iii). However, it will not be possible to formulate, let alone solve, causal queries such as (v) in this setting: these live on the second rung, "doing".

Specifically, (b) implies that $Z$ is independent of $U$ : using the notation of Dawid (1979), we write this as

$$
Z \Perp U
$$

Here (d) is interpreted as asserting the probabilistic independence of $Y$ from $Z$, conditional on $X$ and $U$ :

$$
Y \Perp Z \mid(X, U)
$$

# 6.1. Graphical representation 

![img-0.jpeg](img-0.jpeg)

Figure 1
Instrumental variable: seeing

It is often convenient to display such conditional independence properties by means of a directed acyclic graph (DAG). Each node in the DAG represents a variable in the problem, and missing arrows represent assumed properties of conditional independence in their joint distribution - see Dawid (2015, Section 6) for full details. The DAG is a partial description, displaying only qualitative aspects, of the joint distribution.

The DAG representing (1) and (2) looks like Figure 1 (the dotted outline of $U$ is nonessential, merely a reminder that $U$ is unobserved). The absence of an arrow between $Z$ and $U$ represents their independence, (1), while the missing arrow from $Z$ to $Y$ represents their conditional independence, given the "parents" of $Y$, namely $X$ and $U$, (2). In general in a DAG representation, any variable is conditionally independent of its non-descendants, given its parents. Further conditional independence properties implied by these can be read off the DAG, using the $d$-separation (Verma \& Pearl 1990) or equivalent moralisation (Lauritzen et al. 1990) criteria, as described in Dawid (2015).

The qualitative DAG representation of a joint distribution can be expanded to a full quantitative description by specifying, for each variable, its conditional distribution given its parents in the DAG. (This would be required to encode the condition in (b) that $X$ is not independent of $Z$ ). Elegant algorithms exist, taking advantage of the DAG structure, for streamlining quantitative computation of joint and conditional probabilities (Cowell et al. 1999). Such probabilities are what is needed to address questions of forecasting and backcasting.

## 7. Doing: Decision-theoretic causality

The decision-theoretic (DT) approach to causality has been described in this journal (Dawid 2015); its foundational underpinnings are examined in Dawid (2021a).

We have several regimes of interest. For each possible value $x$ of $X$ we have an interventional regime, where treatment value $x$ is forced on an individual (that is, $X$ is "set" to $x$, which we notate as $X \leftarrow x$ ). We also have an "idle" regime, in which the treatment $X$ is merely observed, and any value may occur. It is helpful to introduce a non-stochastic "regime indicator" variable $F_{X}$, where $F_{X}=x$ labels the interventional regime with $X \leftarrow x$, and $F_{X}=\emptyset$ labels the idle regime. The response variable $Y$ may have different distributions in the different regimes. The object of causal inference will usually be some contrast between the response distributions in the various interventional regimes-this is what is required to address the decision problem of choosing which value to set $X$ to. For example, when $X$ is binary, interest typically centres on the difference in the expected response between the two interventional regimes, $\mathrm{E}\left(Y \mid F_{X}=1\right)-\mathrm{E}\left(Y \mid F_{X}=0\right)$, which is termed the "average causal effect", ACE.

But in the cases to be considered there will be no data available directly relevant to the interventional settings of interest, and we shall want to make use of observational data collected under the idle regime, $F_{X}=\emptyset$, to make inferences about what would happen in interventional settings. This may or may not be possible. At the least, it will be necessary to make, and justify, relationships between the idle and the interventional settings. DT studies when and how such relationships can be used to support causal inference from observational data.

For example, we might be willing to assume, in addition to (1) and (2), that, no matter whether $X$ is merely observed $\left(F_{X}=\emptyset\right)$, or is set by external intervention $\left(F_{X}=0\right.$ or 1$)$, the following ingredients will be the same:
(e). the distribution of $Z$
(f). the distribution of $U$, with $U$ independent of $Z$
(g). the conditional distribution of $Y$ given $(Z, X, U)$ (which would then in all cases depend only on $(X, U)$, since this is so under regime $F_{X}=\emptyset$, by (d).)

These properties do not follow logically from (1) and (2) (Dawid 2021b), and if they are to be applied they need additional argument, such as described in Dawid (2021a).

We can interpret assumptions (e)-(g) as conditional independence properties:

$$
\begin{aligned}
& Z \Perp F_{X} \\
& U \Perp\left(F_{X}, Z\right) \\
& Y \Perp\left(F_{X}, Z\right) \mid(X, U)
\end{aligned}
$$

Even though $F_{X}$ is a non-stochastic indicator of regime (observational/interventional), these intuitively meaningful "extended conditional independence" expressions can be manipulated essentially just as if $F_{X}$ were a random variable (Constantinou \& Dawid 2017).

In this approach, the conditions (e)-(g), or equivalently (3)-(5), which relate to behaviour under possible intervention at $X$, are the full "causal ingredients" of our model.

# 7.1. Graphical representation 

We can augment Figure 1 with an additional node for $F_{X}$ (square to indicate it is nonstochastic). We obtain Figure 2. This DAG represents (in exactly the same way as before) the assumed conditional independence assumptions (1)-(5), which fully embody our causal assumptions. (The dashed arrows from $Z$ and $U$ to $X$ are there to indicate that they are absent under an interventional regime $F_{X}=x$, since then we have $X=x$, trivially

![img-1.jpeg](img-1.jpeg)

Figure 2
Instrumental variable: doing
independent of $(Z, U)$ ). Note in particular that the arrow from $Z$ to $X$ in Figure 2 does not encode a causal effect of $Z$ on $X$, since (e)-(g) are fully consistent with cases, such as Example 4, where $Z$ and $X$ are merely associated (Dawid 2010, §10).

# 7.2. Causal Bayesian Network 

Pearl (2009) uses the same causal semantics as described above to construct what he terms a causal Bayesian network (CBN). The difference is that he would normally consider the possibility of intervention on every observable variable-which in our case would mean adding further intervention indicator nodes $F_{Z}, F_{Y}$ to Figure 2, parents, respectively, of $Z$ and $Y$. In such a case the presence of all the intervention nodes is usually taken for granted, and omitted from the augmented DAG-so rendering it visually indistinguishable from an unaugmented DAG, here Figure 1. However there are clear advantages to retaining explicit intervention nodes in the figure:
(i). This eliminates the possibility of confusion between rung 1 (seeing) and rung 2 (doing) interpretations of apparently identical DAGs.
(ii). The "causal" links assumed between regimes are fully represented by $d$-separation properties of the augmented DAG.
(iii). It will (as above) often be appropriate to consider interventions on only some of the variables. In particular, there will then be no need to impose the additional crossregime causal constraints associated with further, inessential, intervention indicators.

### 7.3. Estimation

Even after assuming links, as above, between the observational and interventional regimes, it does not follow that we have enough structure to enable us to use the observational data to estimate, say, the causal effect, ACE, of $X$ on $Y$. And indeed, in this example, further structure must be imposed to support such causal inference. For instance, in Example 1 we might require that $Y$ has a linear regression on $(X, U)$ (this being the same in all regimes, by $(5))$ :

$$
\mathrm{E}\left(Y \mid X, U, F_{X}\right)=W+\beta X
$$

where $W$ is a function of $U$. Since then $\mathrm{E}\left(Y \mid F_{X}=x\right)=w_{0}+\beta x$, where $w_{0}=\mathrm{E}(W)$, $\beta$ has a clear causal interpretation. Also, restricting attention to the observational regime $F_{X}=\emptyset$, we obtain $\mathrm{E}(Y \mid Z)=\mathrm{E}\{\mathrm{E}(Y \mid X, U, Z) \mid Z\}=\mathrm{E}\{\mathrm{E}(Y \mid X, U) \mid Z\}$, by (5),

$=w_{0}+\beta \mathrm{E}(X \mid Z)$, by (4). This implies that we can estimate $\beta$, from the observational data, as the ratio of the coefficients of $Z$ in the sample linear regressions of $Y$ on $Z$ and of $X$ on $Z$.

In cases such as Example 2 with binary $X,(6)$ is equivalent to

$$
\operatorname{SCE}(u)=\beta
$$

a constant for all $u$, where $\operatorname{SCE}(u)=\mathrm{E}\left(Y \mid U=u, F_{X}=1\right)-\mathrm{E}\left(Y \mid U=u, F_{X}=0\right)$ is the specific causal effect of $X$ on $Y$, relevant to the subpopulation having $U=u$. That is to say, the specific causal effect is required to be non-random, the same in all subpopulations. Then $\mathrm{ACE}=\mathrm{E}\{\operatorname{SCE}(U)\}=\beta$ also, and so is estimable as above. Alternatively, when all variables are binary, without making any modelling assumptions we can determine bounds on ACE from the data (Balke \& Pearl 1997, Dawid 2003).

# 8. Linear structural equation model (SEM) 

Linear structural equation modelling, closely related to path analysis (Wright 1921), is perhaps the earliest approach to instrumental variable problems-and much else besides. It can be considered as an extension of linear regression modelling. In the context of the encouragement trial of Example 1, we might express the relationship between $Z, X, Y$ by the pair of regression-like equations:

$$
\begin{aligned}
X & =\alpha_{0}+\alpha_{1} Z+U_{X} \\
Y & =\beta_{0}+\beta_{1} X+U_{Y}
\end{aligned}
$$

(Such a system would often be completed with a further equation for $Z$, which here would simply be $Z=U_{Z}$. However we omit this on account of its triviality). Here $U_{X}, U_{Y}$ are zero-mean "residual error" terms. In this problem it would be assumed that $U_{X}$ and $U_{Y}$ are uncorrelated with $Z$, but not necessarily with each other. The absence of $Z$ in (9) embodies the "exclusion restriction".

This model can be rendered graphically as in Figure 3. This may be compared with
![img-2.jpeg](img-2.jpeg)

Figure 3
Structural equation graph
Figure 1, identifying $U=\left(U_{X}, U_{Y}\right)$.
As discussed by Pearl (2009, §5.1.2), the intended interpretation-in particular, the causal interpretation-of SEM has often been unclear. Pearl's suggestion is as follows.
(i). In the system (8)-(9), $X$ is functionally determined by $\left(Z, U_{X}\right)$, and $Y$ is functionally determined by $\left(X, U_{Y}\right)$. So we can solve for $(X, Y)$ in terms of $\left(Z, U_{X}, U_{Y}\right)$. If we have a joint distribution for $\left(Z, U_{X}, U_{Y}\right)$, this determines a joint distribution for $(Z, X, Y)$-which can be regarded as representing the undisturbed system.

(ii). If, alternatively, we intervene to set $X$ to $x$, it is assumed that we can replace (8) by $X=x$, but retain (9) essentially as is, so that $Y=\beta_{0}+\beta_{1} x+U_{Y}$, with the distribution of $U_{Y}$ unchanged.

This approach gives a causal semantics to a SEM, relating the observational regime with possible interventional regimes. As with any such assumed relationship, it is not to be taken for granted, but argued for in the context of each particular problem. When we can assume (ii), $\beta_{1}$ has a clear causal interpretation, being the rate of change of $\mathrm{E}(Y \mid X \leftarrow x)$ with respect to the value set, $x$. However, since $U_{Y}$ is correlated with $U_{X}$, and hence in general with $X, \beta$ will not be the coefficient of $X$ in the observational regression of $Y$ on $X$ in (i), so can not be identified from that. Instead we can argue that, since $U_{X}$ is uncorrelated with $Z, \mathrm{E}(X \mid Z)=\alpha_{0}+\alpha_{1} Z$; and, since $U_{Y}$ is uncorrelated with $Z$, $\mathrm{E}(Y \mid Z)=\beta_{0}+\beta_{1} \mathrm{E}(X \mid Z)=\beta_{0}+\alpha_{0} \beta_{1}+\alpha_{1} \beta_{1} Z$. It again follows, as in $\S 7.3$, that $\beta_{1}$ can be identified as the ratio of the coefficients of $Z$ in the observational regressions of $Y$ on $Z$ and $X$ on $Z$.

# 9. Structural Causal Model (SCM) 

We can generalise the system (8)-(9) by dropping the linearity requirement, yielding

$$
\begin{aligned}
& X=f_{X}\left(Z, U_{X}\right) \\
& Y=f_{Y}\left(X, U_{Y}\right)
\end{aligned}
$$

where $f_{X}, f_{Y}$ are specified general functions of their arguments, and $\left(U_{X}, U_{Y}\right)$ have a specified joint distribution, typically not being independent of each other, but being jointly independent of $Z$. The absence of $Z$ as an argument of $f_{Y}$ embodies the exclusion restriction. Pearl \& Mackenzie (2018) refer to such a nonparametric structural equation model as a Structural Causal Model (SCM), and we use this designation in the sequel.

Again, this system can be represented graphically by Figure 3. But with no loss of generality we can use $U$ instead of the pair $\left(U_{x}, U_{Y}\right)$, and write the system as

$$
\begin{aligned}
& X=f_{X}(Z, U) \\
& Y=f_{Y}(X, U)
\end{aligned}
$$

with $U$ independent of $Z$. This system again determines a joint observational distribution for $(X, Y, Z)$, which is represented by Figure 1. We might again imbue this structural equation system with causal semantics (whose relevance in a real life context will need justification): assume that, under an intervention $X \leftarrow x$, we can replace (12) by $X=x$, and (13) by $Y=f_{Y}(x, U)$, where $U$ is supposed to retain its original distribution. The extended structure is then again represented by Figure 2. In particular, $Y$ will be independent of $Z$ in an interventional regime, where the dotted arrows in Figure 2 are absent. In contrast, in the observational regime, the distribution of $Y$, given $X=x, Z=z$, is that of $Y=f_{Y}(x, U)$ given $f_{X}(z, U)=x$; because of this conditioning, the value of $Z$ will typically make a difference to the distribution of $Y$.

In using Figure 1 (and, implicitly or explicitly, Figure 2) as representations of the SCM system (12)-(13), we are supplying these figures with yet another semantic interpretation, where the dependence of $X$ and $Y$ on their parents is taken as deterministic, not stochastic. This is to be contrasted with the CBN interpretation of $\S 7.2$, in which all relationships are allowed to be stochastic.

It can be be shown that, by suitable choice for the distribution of its $U$ (which distribution is, however, not uniquely determined), the SCM model can fully reproduce the joint distribution of $(X, Y, Z)$, in all regimes, implied by a given fully stochastic DT model. This property holds in general for any problem represented by a DAG. For identifying effects of causes we gain nothing by replacing a stochastic DT model with a deterministic SCM model. ${ }^{1}$ In particular, we again can not identify the causal effect of $X$ on $Y$ without further assumptions, such as linearity in (13), as for (9) (with $U_{Y}$ some function of $U$ ).

# 9.1. A comment 

If, in a SEM or SCM, $U$ is regarded as a persistent attribute of an individual, the assumed determinism would mean that we would get the same output each time we applied the same intervention to that individual. That would be an unreasonable assumption in most contexts. Consequently we should normally consider $U$ as also incorporating information specific to the occasion of application (including, perhaps, "random error"), varying from occasion to occasion. Nevertheless, assuming the distribution of $U$ does not change, average causal effects will still be constant, and so be meaningful, across occasions.

## 10. Potential outcomes

In the potential outcomes (PO) approach to statistical causality (Rubin 1974), for each possible value $x$ of the treatment $X$, we conceive of a version $Y(x)$ of the outcome variable $Y$, all of these versions co-existing, even before application of treatment. It is supposed that $Y(x)$ (or, to be more explicit, $Y(X=x)$ ) is the outcome that would be observed in the interventional regime $F_{X}=x$. Typically it is further assumed ("consistency") that in the idle regime $F_{X}=\emptyset$ also, whenever $X=x$, the outcome will be $Y=Y(x)$ (which is why we don't distinguish between $Y(X=x)$ and $Y(X \leftarrow x))$. Consistency is required to relate the observational and interventional regimes.

In the special but common and important case of binary $X,{ }^{2}$ intervening to set $X$ to 1 would reveal the value of $Y(1)$, while $Y(0)$ would remain unobserved; and similarly on interchanging 1 and 0 . In this approach, the single response $Y$ is replaced by a bivariate quantity $\mathbf{Y}=(Y(0), Y(1))$, which must thus be endowed with a bivariate distribution. The fundamental causal contrast, comparing the effects of the two interventions, is considered to be the individual causal effect, ICE $=Y(1)-Y(0)$. However, direct inference about ICE is complicated by the fact (termed "the fundamental problem of causal inference" by Holland (1986)) that, because it is logically impossible to intervene on the same individual in two mutually exclusive ways simultaneously, we can never observe ICE, or estimate its distribution. For this reason, it is customary to divert attention to the expected individual causal effect, $\mathrm{E}(\mathrm{ICE})$. By linearity of expectation, this is $\mathrm{E}\{Y(1)\}-\mathrm{E}\{Y(0)\}$, each term of which involves only one intervention. This then is the PO version of ACE, as introduced in $\S 7$, with essentially the same interpretation. Note however that there is no analogue of ICE in the DT approach; neither is there any DT analogue of, say, var(ICE), which involves the

[^0]
[^0]:    ${ }^{1}$ See however $\S 10.1$, and especially $\S 10.1 .1$, for further discussion of this point. Also, while Balke \& Pearl (1997) make essential use of the deterministic functional relationships in the SCM to derive estimable bounds on ACE in the case of binary variables, Dawid (2003) showed how the same bounds can be obtained from the purely stochastic DT model.
    ${ }^{2}$ Of course, similar considerations apply more generally.

correlation between $Y(0)$ and $Y(1)$-a correlation that can never be estimated, on account of the fundamental problem of causal inference.

If we start with a SCM representation of a system, we can use it to construct associated potential outcomes. For example, starting from (13), just define, for each $z, X(Z=z)=$ $f_{X}(z, U)$, and for each $x, Y(X=x)=f_{Y}(x, U)$. Under the SCM causal semantics, $X(Z=$ $z)=f_{X}(z, U)$ is assumed to supply the value of $Y$, when $X=x$, whether or not there are interventions at $X$ or anywhere else in the system (except at $Y$ itselvf); this corresponds to the PO consistency property. This construction of POs makes them all functions of $U$, whose distribution thus generates a joint distribution for all POs.

Typically, however, a PO analysis would not make explicit use of an exogenous variable such as $U$, and might not want to require that there exist any real-world variable or set of variables $U$ with the properties assumed in $\S 9$ (for example, that $Y$ is fully determined by $X$ and $U)$. Instead, one starts by introducing, as primitives, jointly distributed stochastic potential outcomes, $X(Z=z), Y(X=x), Y(Z=z)$, for all possible values of $x$ and $z$, and work directly with them. The exclusion restriction now becomes $Y(Z=z)=Y\{X=$ $X(Z=z)\}$.

Introduce now a new variable $V$, which is simply the collection of all $X(Z=z)$ 's and $Y(X=x)$ 's, as $z$ and $x$ vary. Then $X$ is fully determined by $(Z, V)$ : when $Z=z$, we simply select the relevant element $X(Z=z)$ of $V$ (this being valid in all regimes, by consistency); similarly $Y$ is determined by $(X, V)$. We thus recover a formal ${ }^{3}$ identity with the SCM of (12) and (13), with $V$ substituting for $U$-so long as we have $V$ independent of $Z$. If we were starting from a SCM, as above, the independence of $U$ and $Z$, and thus of $V$ and $Z$, would be easy to justify, since $U$ represents pre-existing characteristics of the individual, and $Z$ is randomised. To make a similar argument for $V$ when taking POs as primitive is more problematic, since $V$ does not correspond to any real-world quantity (in particular, on account of "the fundamental problem of causal inference", certain elements of $V$, e.g. $X(Z=1)$ and $X(Z=2)$, are not simultaneously observable). Nevertheless, the typical assumption is that it is indeed meaningful to consider the collection $V$ of all possible potential responses as a pre-existing (albeit unobservable) characteristic of the individual, and thus argue that $V$ is independent of the randomised variable $Z$. In this case, we recover a purely formal identity with an SCM model. Now the linearity condition (6) is equivalent to $Y(X=x)-Y\left(X=x^{\prime}\right)=\beta\left(x-x^{\prime}\right)$-which is thus being required to be non-random.

# 10.1. A variation 

The above specifications can be considered simply as more detailed ways of realising the CBN structure of $\S 7$, which is more general since in a CBN we need not assume the existence of potential outcomes, which can not be derived from its stochastic form. And indeed, for estimating the average causal effect, the extra structure imposed beyond that of a CBN does not offer any improvement. But a SCM or PO approach does allow us to formulate, and purports to solve, other causal questions. We consider one such in the context of Example 2, where $Z, X, Y$, are all binary (Imbens \& Angrist 1994, Angrist et al. 1996).

Let $\mathbf{X}$ denote the pair $(X(Z=0), X(Z=1))$, and $\mathbf{Y}$ the pair $(Y(X=0),(Y(X=1))$.

[^0]
[^0]:    ${ }^{3}$ In a genuine SCM, $U$ is regarded as a set of unobserved real-world background variables, with an appropriate, in principle knowable, distribution, that, together with $X$, would determine $Y$. But is is hard to conceive of such a real-world interpretation of $V$.

We shall assume consistency, the exclusion restriction $Y(Z=z)=Y\{X=X(Z=z)\}$, and $Z \Perp(\mathbf{X}, \mathbf{Y})$. It is easy to see that

$$
Y(Z=z)=Y(X=1) X(Z=z)+Y(X=0)\{1-X(Z=z)\}
$$

We can define the following "individual causal effects":

$$
\begin{aligned}
& \operatorname{ICE}_{Z \rightarrow X}=X(Z=1)-X(Z=0) \\
& \operatorname{ICE}_{Z \rightarrow Y}=Y(Z=1)-Y(Z=0) \\
& \operatorname{ICE}_{X \rightarrow Y}=Y(X=1)-Y(X=0)
\end{aligned}
$$

and deduce from (14) that

$$
\operatorname{ICE}_{Z \rightarrow Y}=\operatorname{ICE}_{Z \rightarrow X} \times \operatorname{ICE}_{X \rightarrow Y}
$$

We note that, since $Z$ is randomised, $\operatorname{ACE}_{Z \rightarrow X}=\mathrm{E}\left(\mathrm{ICE}_{Z \rightarrow X}\right)=\mathrm{E}(X \mid Z=1)-\mathrm{E}(X \mid$ $Z=0)$ is readily estimable from the observational data, and so likewise is $\mathrm{ACE}_{Z \rightarrow Y}=$ $\mathrm{E}(Y \mid Z=1)-\mathrm{E}(Y \mid Z=0)$. However, there is no immediate parallel for $\mathrm{ACE}_{X \rightarrow Y}$, since $X$ has not been randomised.

If we could replace each ICE term in (18) by its expectation ACE, we would have

$$
\mathrm{ACE}_{X \rightarrow Y}=\mathrm{ACE}_{Z \rightarrow Y} / \mathrm{ACE}_{Z \rightarrow X}
$$

where the right hand-side of (19) is estimable from the observational data (it is assumed that $Z$ has a causal effect on $X$, so that $\mathrm{ACE}_{Z \rightarrow X} \neq 0$ ).

When we can assume (7), $\operatorname{ICE}_{X \rightarrow Y}=\beta$ is non-random, we can take expectations in (18), and (19) does indeed hold, allowing estimation of $\beta$. But more generally $\mathbf{X}$ and $\mathbf{Y}$ are not independent of each other (when constructed from a SCM, they both involve the same variable $U$ ), and so neither are $\operatorname{ICE}_{Z \rightarrow X}$ and $\operatorname{ICE}_{X \rightarrow Y}$. So we can not just take expectations of all terms in (18), and (19) is typically not valid.

To make further progress, other assumptions must be imposed, in particular, monotonicity:

$$
X(Z=1) \geq X(Z=0)
$$

That is to say, we do not have any "defiers", for which both $X(Z=0)=1$ (treatment would be taken when not assigned) and $X(Z=1)=0$ (treatment would not be taken when assigned).

Even monotonicity is not sufficient to allow estimation of $\mathrm{ACE}_{X \rightarrow Y}$. However, it does allow a new interpretation of the right-hand side of (19). For it implies that the individual causal effect $\operatorname{ICE}_{Z \rightarrow X}$ of (15) is either 1 or 0 . Thus, from (18),

$$
\begin{aligned}
\operatorname{ACE}_{Z \rightarrow Y} & =\mathrm{E}\left(\operatorname{ICE}_{X \rightarrow Y} \mid \operatorname{ICE}_{Z \rightarrow X}=1\right) \times \operatorname{Pr}\left(\operatorname{ICE}_{Z \rightarrow X}=1\right) \\
& =\mathrm{E}\left(\operatorname{ICE}_{X \rightarrow Y} \mid \operatorname{ICE}_{Z \rightarrow X}=1\right) \times \mathrm{E}\left(\operatorname{ICE}_{Z \rightarrow X}\right)
\end{aligned}
$$

It follows that

$$
\mathrm{ACE}_{Z \rightarrow Y} / \mathrm{ACE}_{Z \rightarrow X}=\mathrm{E}\left(\operatorname{ICE}_{X \rightarrow Y} \mid \operatorname{ICE}_{Z \rightarrow X}=1\right)
$$

The right-hand side of (21) is termed the "local average treatment effect", LATE. Under monotonicity, LATE is estimable from the data, since the left-hand side of (21) is.

# 10.1.1. Critical comments. 

(i). Considerations similar to $\S 9.1$ suggest that it would typically be appropriate to regard potential outcomes, and so individual causal effects, as varying from one occasion to another, only their expectations remaining constant.
(ii). In general the monotonicity assumption is untestable, since (under the assumptions of (i) above) $X(Z=1)$ and $X(Z=0)$ can not both be observed on the same occasion. However, it must hold in the case of an availability trial as in Example 3, where necessarily $X(Z=0)=0$. Another extreme case where it can be inferred is in the presence of a variable $W$, a complete mediator between $Z$ and $X$ (so that $X(Z)=$ $X\{W(Z)\})$, where we have empirical evidence that, with probability $1, W(Z=1)=1$ and $X(W=0)=0$. If $X(Z=0)=1$, then we deduce $W(Z=0)=1=W(Z=1)$, and so $X(Z=1)=X(Z=0)=1$, and we have no defiers.
(iii). LATE is an average causal effect in a subgroup of the population: those for whom both $X(Z=0)=0$ and $X(Z=1)=1$. These are termed "compliers", since they would take the treatment if assigned to do so, and not take it if not assigned (in an availability setting, they are those who would take the treatment if assigned to do so). However it is impossible to tell who belongs to this subpopulation by knowing only what treatment was assigned and what treatment was taken (in an availability trial, an individual who was assigned treatment and took it must be a complier, but we still can not tell the status of an individual who was not assigned treatment). Indeed, assuming as in (i) that $\mathbf{X}$ will vary from occasion to occasion, so too will the group of compliers. So the relevance of LATE in practice is debatable. Even its definition, relying as it does on a "cross-world" comparison of potential outcomes under both $Z=1$ and $Z=0$, can be criticised as essentially metaphysical and unscientific (Dawid \& Didelez 2012).
(iv). In cases such as Example 4 where $Z$ is not directly causal for $X$, the notation $X(Z=$ $z$ ) is meaningless, and the above analysis can not even get started.

## Part II <br> CAUSES OF EFFECTS

## 11. Introduction

Let us consider again the initial attribution example: Juanita took Lipitor 80 mg daily for 3 years and developed diabetes. Was that because she took Lipitor?

One way of formulating this CoE question is through what the courts sometimes refer to as the "but for" test: is it the case that, but for her having taking Lipitor, the diabetes would not have developed? This immediately plunges us into counterfactual considerations. We know that, in the actual world, the Lipitor was taken and diabetes developed, and are asked to contrast this with the outcome in a counterfactual world, in which (counter to the known facts) the Lipitor had not been taken. The problem of course is that the counterfactual world is, by definition, unobservable, and even its existence-certainly its uniqueness-are questionable.

Even in deciding on the exact question, choices have to be made. Juanita took Lipitor 80 mg daily for 3 years. Did she develop diabetes because she took the 80 mg dose (the

only one for which the court accepted general causation), rather than 40 mg ? Did it develop because she took it for 3 years, rather than 2 years? Each such choice conjures up a different counterfactual world for comparison with this one. We also have choice over what was the observed response: that she developed diabetes at some point?; that she developed diabetes within 1 year of stopping Lipitor? Detailed specification is obviously important in cases where the response is death: since death is certain, even in a counterfactual world, we can never say that an individual would never have died, but for some exposure. ${ }^{4}$

Under the "but for" criterion, "causation" is understood as the case that, in the appropriate counterfactual world, where Juanita did not take the Lipitor (in the same way that she in fact did), she did not develop diabetes (in the relevant time-frame). This is appropriate when the response is all or nothing. We can also consider cases with a continuous response, such as time to death, but then it is not so clear what the focus of our attention should be. We might ask, for example, does death occur later, in the relevant counterfactual world, than it actually did in this world (Greenland 1999)?

Even when our variables have been carefully specified, and the relevant counterfactual question formulated, it remains unclear just how to conceive of and structure the counterfactual world of interest. Lewis (1973) develops an approach based on the "closest possible world" to this one, save only for the change to the exposure; but this only shifts, not solves, the problem. There appears to be an unresolvable ambiguity about our counterfactual contrast.

Clearly there are deep philosophical problems, as well as technical specification issues, besetting any approach to formulating a CoE problem. In the sequel we deal only with the case of binary exposure and outcome variables, denoted by $X$ and $Y$ respectively, assuming the above specification problems have been addressed. But there will still remain some ambiguity about the relevant counterfactual world, which will be reflected in ambiguity about the answer to the CoE question.

In $\S 12$ we introduce two approaches to relating the actual and counterfactual worlds: SCM and CIM. The former is essentially deterministic, while the latter allows some stochastic elements. However both make assumptions that might be regarded as over-strong, leading to misleadingly precise answers to the CoE question. In $\S 13$ we show how each of these models can be reformulated in terms of "potential outcomes". In $\S 14$ we explain how, taking full account of real-world data on exposure and outcome, this approach can handle and quantify the remaining ambiguities, by supplying an appropriate "interval of ambiguity" for the probability of causation, PC.

We can narrow the interval of ambiguity for an individual case by deeper understanding of the mechanisms and processes involved (Beyea \& Greenland 1999)—even when we can't access the specific details of these for the individual case at hand. We develop this theme in the remaining sections, showing how information about additional variables can tighten the bounds on PC.

[^0]
[^0]:    ${ }^{4}$ Even in EoC cases, specification of the outcome matters. In March 2021, a few cases of blood clots among individuals who had received the Astra-Zeneca vaccine against Covid-19 were observed, and concerns were raised about a possible causal connexion, leading to a pause in the vaccine's rollout in some countries. When it was pointed out that the rate of such clots was in fact lower than in the general population, attention turned to the few cases of a specific rare presentation of the blood clot, cerebral venous sinus thrombosis, and whether the vaccine could cause that. (For this outcome too, there was no evidence for causation).

# 12. Counterfactual constructions 

### 12.1. SCM

The approach of Pearl (2009) (see also Pearl (2015), Dawid et al. (2015)) to CoE is based on SCMs. In the case of Juanita, this would involve the introduction of an unobserved exogenous "background" variable $U$, and the assumption that Juanita's diabetes status $Y$ is fully determined by her Lipitor status $X$ and $U: Y=f_{Y}(X, U)$ (this requires a conception of $U$ as comprising all other pre-existing quantities that, together with $X$, would totally determine $Y$-a collection that may not be easy to comprehend, let alone specify). In some contexts it might be appropriate ("ignorability") to regard $X$ as independent of $U$ in the observational regime, as would happen, if, for example, $X$ is generated by a randomising device. We do not impose this throughout, and will specify where we do assume it.

The same functional relationship $Y=f_{Y}(X, U)$ is assumed to hold ("consistency") whether or not $X$ is imposed by external intervention. To this invariance requirement, familiar from "effects of causes" analysis, we add another, specific to "causes of effects": that the value of the background variable $U$ be the same in both the factual world, and in the counterfactual world that we wish to contrast with this one.

To start with, we assume that the function $f_{Y}$ and the joint distribution of $(X, U)$ are known. These unrealistic requirements are removed in $\S 14$ below.

In the factual world we have observed $X=1$ and $Y=1$, i.e. $f_{Y}(1, U)=1$. We can express the resulting uncertainty about the value of $U$ by means of its conditional distribution, given $X=1, f_{Y}(1, U)=1$ (or, under ignorability, given only $f_{Y}(1, U)=1$ ). We now turn to consider the counterfactual world. Although $U$ is supposed to be the same in both worlds (and thus endowed with the above conditional distribution), $X$ and $Y$ need not be. We introduce "mirror variables", $X^{\prime}$ and $Y^{\prime}$, as their counterfactual counterparts. We retain the general structure across worlds, so that $Y^{\prime}=f_{Y}\left(X^{\prime}, U\right)$, both in observational and in interventional counterfactual regimes.

In the counterfactual world, we now consider the effect of an intervention $X^{\prime} \leftarrow 0$. The value of $Y^{\prime}$ will be $f_{Y}(0, U)$. Using the previous conditional distribution of $U$, we obtain the counterfactual distribution for $Y^{\prime}$, given the hypothetical intervention $X^{\prime} \leftarrow 0$ and the factual knowledge $X=Y=1$. We can thus evaluate the "probability of causation" as the probability that, in this distribution, $Y^{\prime}=0$. That is,

$$
\mathrm{PC}=\operatorname{Pr}\left(Y^{\prime}=0 \mid X=1, Y=1, X^{\prime} \leftarrow 0\right)
$$

### 12.2. Stochastic Causal Model (StCM)

A generalisation of the above model, which does not require deterministic functional relationships, was suggested by Dawid (2000, §12), although it has not been developed in detail. We again assume that the variable $U$ retains its identity across the parallel worlds, and introduce the mirror variables $X^{\prime}, Y^{\prime}$. But we now allow the dependence of $Y$ on $(X, U)$ to be given by a known conditional probability distribution: this allows a more liberal attitude to the nature of $U$, which can be a perfectly normal, in principle observable (though typically not observed), variable.

We assume that the same stochastic relationship also governs the dependence of $Y^{\prime}$ on $\left(X^{\prime}, U\right)$. We again require consistency to relate observational and interventional regimes: the value of $Y$ (resp., $Y^{\prime}$ ) would be the same, whether $X$ (resp., $X^{\prime}$ ) arose by intervention or not. In order to complete the specification, we regard $Y^{\prime}$ and $Y$ as conditionally indepen-

dent, given $\left(X, X^{\prime}, U\right)$ (for example, we might consider them as involving "random noise", operating independently across worlds).

Having now a joint distribution for all variables in all worlds, we can again compute $\mathrm{PC}=\operatorname{Pr}\left(Y^{\prime}=0 \mid X=1, Y=1, X^{\prime} \leftarrow 0\right)$. Specifically, by conditional independence,

$$
\begin{aligned}
\operatorname{Pr}\left(Y^{\prime}=0 \mid X=1, Y=1, X^{\prime} \leftarrow 0, U\right) & =\operatorname{Pr}\left(Y^{\prime}=0 \mid X^{\prime} \leftarrow 0, U\right) \\
& =\operatorname{Pr}\left(Y^{\prime}=0 \mid X^{\prime}=0, U\right) \\
& =\operatorname{Pr}(Y=0 \mid X=0, U)
\end{aligned}
$$

Then PC is the expectation of this, in the conditional distribution of $U$ given $X=1, Y=$ $1, X^{\prime} \leftarrow 0$. But setting $X^{\prime}$ does not affect the joint distribution of $(X, Y, U)$, so we just compute, from Bayes's theorem, the posterior density

$$
p(u \mid X=1, Y=1) \propto \operatorname{Pr}(X=1 \mid u) \operatorname{Pr}(Y=1 \mid X=1, u) p(u)
$$

where $p(u)$ is the prior density of $U$ (and the first term on the right-hand side can be omitted under ignorability). Finally,

$$
\mathrm{PC}=\frac{\int \operatorname{Pr}(Y=0 \mid X=0, u) \operatorname{Pr}(X=1 \mid u) \operatorname{Pr}(Y=1 \mid X=1, u) p(u) d u}{\int \operatorname{Pr}(X=1 \mid u) \operatorname{Pr}(Y=1 \mid X=1, u) p(u) d u}
$$

# 12.3. Twin network 

In both the SCM and StCM approaches, the required computation can be automated by building a "twin network" representation of the problem (Pearl 2009, §7.1.4), as in Figure 4, and making use of probability propogation algorithms (Cowell et al. 1999) as implemented in software systems such as Hugin. ${ }^{5}$ This is useful in more complex problems with more variables.
![img-3.jpeg](img-3.jpeg)

Figure 4
Twin network. Under ignorability, the arrow from $U$ to $X$ can be removed. That from $U$ to $X^{\prime}$ is absent because we are considering $X^{\prime}$ as set by external intervention, taking no account of $U$.

The factual information $X=1, Y=1$ and the counterfactual intervention $F_{X^{\prime}}=0$ (implying $X^{\prime}=0$ ) are entered at the relevant nodes, and propagated through the network to obtain the appropriate conditional distribution for $Y^{\prime}$.

[^0]
[^0]:    ${ }^{5}$ https://www.hugin.com

# 12.4. More general StCMs 

The StCM approach involves nominating some of the variables in a problem as shared across worlds, while the others are allowed to differ. The associated twin network will have a single copy of the shared variables and mirror copies of the others, with the original DAG replicated and stitched together through the shared variables. As discussed in Dawid (2000), the choice of which variables are to be regarded as shared ${ }^{6}$ is a matter of imagination rather than science, and should relate to the specific problem of interest-there can be no context-free right answer. For example, there have been law suits by various states against tobacco companies, claiming that if they had publicised their knowledge of the dangers of smoking when they first knew of them, many lives could have been saved. Damages are sought for the additional costs placed on health services-meaning the excess cost in the actual world, over that of an imagined world in which they had made their knowledge public. But how should we imagine that world? One could reasonably argue that, in such a world, by giving up smoking, people would have lived longer than they actually did. Then the actual (non-)actions of the tobacco companies might well have increased the cost to the health services. But what seems to be required for the case at hand is to imagine a world where people had the same lifetimes, but were healthier, i.e., to regard lifetimes as shared across parallel worlds-and this even though lifetimes can be considered an effect of the companies' decisions. It is not clear how such considerations could be accommodated in a SCM.

## 13. Potential outcomes

As observed in $\S 10$, the SCM approach produces implied potential outcomes, $Y(1)=$ $f_{Y}(1, U), Y(0)=f_{Y}(0, U)$. The pair $\mathbf{Y}=(Y(1), Y(0))$ is a function of $U$, with a bivariate distribution induced by that of $U$. And in fact $\mathbf{Y}$ is all that needs to be retained of $U$ to fully describe the problem: we can replace $U$ by $\mathbf{Y}$, with the functional dependence of $Y$ on $(X, \mathbf{Y})$ given simply by $Y=Y(X)$. The problem can thus be more concisely expressed in terms of $(X, \mathbf{Y})$, these having a joint distribution. Then (22) becomes

$$
\mathrm{PC}=\operatorname{Pr}(Y(0)=0 \mid X=1, Y(1)=1)
$$

Note that under ignorability $X$ is independent of $\mathbf{Y}$ (this is indeed the very definition of ignorability in the PO framework), and then the conditioning on $X=1$ in (24) can be removed.

For the StCM approach we proceed as follows. The stochastic dependence of $Y$ on $(X, U)$ can be modelled by introducing a further unobserved "noise" variable $V$, independent of $(X, U)$, and representing $Y=f_{Y}(X, U, V)$ for a suitable function $f_{Y}$. This can be done in many ways. One possible way uses the probability integral transformation: if $Y$ is a univariate variable whose conditional distribution function $F_{x, u}(y)$, given $X=x, U=u$, is strictly increasing, take $V$ to be uniform on $[0,1]$, and $f_{Y}(x, u, v)=F_{x, u}^{-1}(v)$.

There will be a counterfactual mirror $V^{\prime}$ of $V$, with $Y^{\prime}=f_{Y}\left(X, U, V^{\prime}\right)$. We now define potential outcomes $Y(1)=f_{Y}(1, U, V), Y(0)=f_{Y}\left(0, U, V^{\prime}\right)$, having a joint distribution induced by that of $\left(U, V, V^{\prime}\right)$. Although the variables so constructed will depend on the

[^0]
[^0]:    ${ }^{6}$ Mackie (1980) refers to these as the "causal field", and notes the rôle of our own choice in its specification.

specific choices made for the noise variable $V$ and the function $f_{Y}$, it is easy to see that their joint distribution will in all cases be that of $\left(Y, Y^{\prime}\right)$, given interventions $X \leftarrow 1$, $X^{\prime} \leftarrow 0$. And since $X=1 \Rightarrow Y=Y(1)$, etc., (24) again holds.

We thus see that, in all cases, we can ignore the finer details, and represent the problem by means of a joint distribution for $(X, \mathbf{Y})$, with PC given by (24).

# 14. Empirical information 

We have so far supposed that the full probabilistic structure of the model, with its variables $U, X, Y$, is known. In a StCM, we can take $U$ to be a specified potentially observable variable, and then this assumption is not unreasonable. However it is typically implausible for a SCM, where, in order to achieve the required deterministic dependence of $Y$ on $(X, U)$, we would have to conceive of a fantastically rich $U$. Alternatively, we can re-express the problem in terms of the pair $\mathbf{Y}$ of potential responses, with a joint distribution for $(X, \mathbf{Y})$. Without making further assumptions on the originating SCM or StCM, there are no constraints on this joint distribution (other than independence of $X$ and $\mathbf{Y}$ under ignorability). We can however gather empirical data to constrain it, and thus hope to estimate PC by (24).

In the sequel we proceed on this basis, and consider what can indeed be estimated. We initially assume that we can only observe $X$ and $Y$, in interventional and/or observational circumstances. We can estimate $\operatorname{Pr}\{Y(x)=1\}=\operatorname{Pr}(Y=1 \mid X \leftarrow x)$ from interventional studies. When we can not assume ignorability, we can also estimate, from observational data, $\operatorname{Pr}\{Y(1)=1 \mid X=1\}=\operatorname{Pr}(Y=1 \mid X=1)$ (by consistency), and $\operatorname{Pr}\{Y(0)=1 \mid$ $X=0\}=\operatorname{Pr}(Y=1 \mid X=0)$, as well as the marginal distribution of $X$. For this general case it might initially seem problematic to estimate, say, $\operatorname{Pr}\{Y(1)=1 \mid X=0\}$, since this involves non-coexisting worlds, one with $X=1$ and the other with $X=0$; but we can in fact solve for it, using $\operatorname{Pr}\{Y(1)=1\}=\operatorname{Pr}\{Y(1)=1 \mid X=1\} \operatorname{Pr}(X=1)+\operatorname{Pr}\{Y(1)=1 \mid$ $X=0\} \operatorname{Pr}(X=0)$, where all other terms are estimable.

We can thus estimate the bivariate distribution of $(X, Y(1))$, and likewise that of $(X, Y(0))$. However, the full trivariate distribution of $(X, Y(1), Y(0))$ is not estimable: since we can never observe both $Y(0)$ and $Y(1)$ simultaneously, no data can tell us directly about the dependence between $Y(0)$ and $Y(1)$, either marginally or conditionally on $X$. And since (24) requires such information, typically PC is not identifiable from empirical data.

Nevertheless, the estimable bivariate distributions do impose constraints on the possible values of PC. Moreover, these constraints can often be tightened still further when we can observe other, related, variables in the problem. We now turn to investigate such constraints, in a number of contexts.

## 15. Analysis of the probability of causation

Let us consider the initial attribution example: Juanita took Lipitor 80mg daily for 3 years $(X=1)$ and developed diabetes $(Y=1)$. Was that because she took Lipitor? We wish to address this question and assess the probability of causation, PC, for Juanita's case, using data collected on other individuals. To this end we assume

Exchangeability Juanita is similar to the population from which probabilities have been computed, so that those probabilities apply to her.


Table 1 Joint distribution of $Y(0)$ and $Y(1)$

Exchangeability may require restriction of the data considered to individuals deemed sufficiently like Juanita.

Except where relaxed in $\S 15.3$ below, we shall also assume
Ignorability The fact that Juanita chose to take the drug is not informative about her response to it, either factually or counterfactually. Formally, we require independence, $X \Perp \mathbf{Y}$, between $X$ and the pair of potential responses $\mathbf{Y}=(Y(1), Y(0))$.

Ignorability is a strong assumption, and will often be inappropriate. When it can be assumed, we can use data from either experimental or observational studies; otherwise we need data from both of these.

Under ignorability, the target (24) becomes

$$
\operatorname{PC}=\operatorname{Pr}(Y(0)=0 \mid Y(1)=1)
$$

We proceed to assess this using the general potential outcome framework of $\S 13$ and $\S 14$, where no assumptions are imposed on the joint distribution of $Y(0)$ and $Y(1)$ beyond those that can be informed by the empirical data. Further details may be found in Dawid et al. (2017), Dawid \& Musio (2021).

# 15.1. Basic inequalities 

Suppose we have access to (observational or experimental) data, supplying values for

$$
\operatorname{Pr}\{Y(x)=y\}=\operatorname{Pr}(Y=y \mid X=x) \quad(x=0,1 \quad y=0,1)
$$

Define

$$
\begin{aligned}
& \tau:=\operatorname{Pr}(Y=1 \mid X=1)-\operatorname{Pr}(Y=1 \mid X=0) \\
& \rho:=\operatorname{Pr}(Y=1 \mid X=1)-\operatorname{Pr}(Y=0 \mid X=0)
\end{aligned}
$$

The joint distribution of $(Y(0), Y(1))$ must have the form of Table 1, where the marginal probabilities are given by (26), re-expressed in terms of $\tau$ and $\rho$, and where the unidentified "slack" quantity $\xi$ embodies the residual ambiguity in the distribution. For all the entries of Table 1 to be non-negative, we require

$$
$$

The probability of causation (25) is

$$
\mathrm{PC}=\frac{\xi+\tau}{1+\tau+\rho}
$$

On using (27), we obtain the following interval bounds for PC:

$$
l:=\max \left\{0, \frac{2 \tau}{1+\tau+\rho}\right\} \leq \mathrm{PC} \leq \min \left\{1, \frac{1+\tau-\rho}{1+\tau+\rho}\right\}=: u
$$

or equivalently

$$
l=\max \left\{0,1-\frac{1}{\mathrm{RR}}\right\} \leq \mathrm{PC} \leq \min \left\{1, \frac{\operatorname{Pr}(Y=0 \mid X=0)}{\operatorname{Pr}(Y=1 \mid X=1)}\right\}=u
$$

where

$$
\mathrm{RR}=\frac{\operatorname{Pr}(Y=1 \mid X=1)}{\operatorname{Pr}(Y=1 \mid X=0)}
$$

is the risk ratio (Robins \& Greenland 1989).
In the absence of additional information or assumptions, these bounds constitute the best available inference regarding PC. In particular, RR $>2$, "doubling the risk", implies that $\mathrm{PC}>0.5$. In a civil legal case, causality might then be concluded "on the balance of probabilities". However, because of the remaining ambiguity, expressed by the inequalities in (30), finding that RR falls short of 2 does not imply that $\mathrm{PC}<0.5$.

# 15.2. Refining the inequalities: Covariates 

When we have additional information we may be able to refine our inferences about PC (Kuroki \& Cai 2011).

Thus suppose that we also have information on a covariate $S$, a pretreatment individual characteristic that can vary from person to person and can have an effect on both $X$ and $Y$. The relevant potential responses are now $\mathbf{X}:=(X(s): s \in S), \mathbf{Y}:=(Y(s, x): s \in$ $S, x=0$ or 1$)$ and the relationship between potential and actual responses is $X=X(S)$, $Y=Y(S, X)$. We again assume exchangeability and ignorability, the latter now being formalised as mutual independence between $S, \mathbf{X}$ and $\mathbf{Y}$.

For simplicity we suppose that $S$ is discrete and that we can estimate from the data the full joint distribution of $(S, X, Y)$.

In the case that we are also able to measure $S$ for Juanita, say $S=s$, we can simply restrict the experimental subjects to those having the same covariate value (who are thus like Juanita in all relevant respects). The probability of causation is now

$$
\operatorname{PC}(s)=\operatorname{Pr}(Y(s, 0)=0 \mid Y(s, 1)=1)
$$

We can bound this just as in (30), but with all probabilities now conditioned on $S=s$, obtaining $l(s) \leq \operatorname{PC}(s) \leq u(s)$.

More interesting is the case in which we don't observe $S$ for Juanita. We have to consider what would have been the response if, counterfactually, Juanita's exposure had been $X=0$. We assume that this is the minimal change made between the factual and the counterfactual worlds, so that, in particular, there is no change to the value or distribution of $S$.

The probability of causation is now:

$$
\begin{aligned}
\mathrm{PC} & =\operatorname{Pr}\{Y(S, 0)=0 \mid X(S)=1, Y(S, 1)=1\} \\
& =\sum_{s} \operatorname{PC}(s) \times \operatorname{Pr}(S=s \mid X=1, Y=1)
\end{aligned}
$$

There are no logical relationships between the distributions of $(Y(s, 0), Y(s, 1))$ for different values of $S$. So by independently varying the values taken by the slack variables in the joint distribution of these potential responses, all the lower bounds $l(s)$ for $\operatorname{PC}(s)$ can

be achieved simultaneously. This leads to an achievable lower bound for PC:

$$
\mathrm{PC} \geq L=\sum_{s} l(s) \times \operatorname{Pr}(S=s \mid X=1, Y=1)
$$

We can express

$$
\begin{aligned}
L= & \frac{1}{\operatorname{Pr}(Y=1 \mid X=1)} \\
& \times \sum_{s} \max \{0, \operatorname{Pr}(Y=1 \mid X=1, S=s)-\operatorname{Pr}(Y=1 \mid X=0, S=s)\} \times \operatorname{Pr}(S=s \mid X=1)
\end{aligned}
$$

Similarly we obtain upper bound

$$
\begin{aligned}
U= & 1-\frac{1}{\operatorname{Pr}(R=1 \mid E=1)} \\
& \times \sum_{s} \max \{0, \operatorname{Pr}(Y=1 \mid X=1, S=s)-\operatorname{Pr}(Y=0 \mid X=0, S=s)\} \times \operatorname{Pr}(S=s \mid X=1)
\end{aligned}
$$

We can not compare these bounds directly with those of (30), since when we don't take account of $S$ the relation between $X$ and $Y$ is generally non-ignorable: $\operatorname{Pr}(Y=y \mid X \leftarrow$ $x) \neq \operatorname{Pr}(Y=y \mid X=x)$.

# 15.3. Non-ignorability 

Tian \& Pearl (2000) analysed this non-ignorable case where we don't observe $S$, either for Juanita or in the external data (still considered exchangeable with Juanita). We now need both observational and experimental data on $X$ and $Y$. Tian \& Pearl (2000) develop the following lower bound for $\mathrm{PC}=\operatorname{Pr}\{Y(0)=0 \mid X=1, Y(1)=1\}$ :

$$
L^{\prime}=\max \left\{0, \frac{\operatorname{Pr}(Y=1)-\operatorname{Pr}(Y=1 \mid X \leftarrow 0)}{\operatorname{Pr}(X=1, Y=1)}\right\}
$$

Dawid \& Musio (2021) show that this can also be derived as a special case of our expression (34), if we substitute for $S$ the binary variable $D=$ "desired exposure" (Corradi \& Musio 2020). $D$ will be identical with $X$ in an observational context, but need not be so in an experimental setting, where $D$ may not be observable.

In our case, with access to information on $S$, we could compute $\operatorname{Pr}(Y=1 \mid X \leftarrow 0)$ by the "back-door formula":

$$
\operatorname{Pr}(Y=1 \mid X \leftarrow 0)=\sum_{s} \operatorname{Pr}(Y=1 \mid X=0, S=s) \times \operatorname{Pr}(S=s)
$$

and thus compute $L^{\prime}$ of (36). It can be shown (Dawid \& Musio 2021) that $L^{\prime} \leq L$ of (34), with equality if and only if all the conditional risk ratios

$$
\frac{\operatorname{Pr}(Y=1 \mid X=1, S=s)}{\operatorname{Pr}(Y=1 \mid X=0, S=s)} \quad(s \in S)
$$

lie on the same side of 1: knowing, and using, the information about $S$ is at least as good as ignoring it. Similarly we can show that the upper bound $U$ of (35) does not exceed the upper bound $U^{\prime}$ derived by Tian \& Pearl (2000),

$$
U^{\prime}=\min \left\{1, \frac{\operatorname{Pr}(Y=0 \mid X \leftarrow 0)-\operatorname{Pr}(X=0, Y=0)}{\operatorname{Pr}(X=1, Y=1)}\right\}
$$

with equality if and only if all the ratios

$$
\frac{\operatorname{Pr}(Y=1 \mid X=1, S=s)}{\operatorname{Pr}(Y=0 \mid X=0, S=s)} \quad(s \in S)
$$

lie on the same side of 1 .

# 15.4. Mediators 

We now consider the case that a third variable $M$ acts a complete mediator in the causal pathway $X \rightarrow M \rightarrow Y$ between the exposure $X$ and the response $Y$. Again we restrict to the case that all variables are binary. We introduce the potential value $M(x)$ of $M$ for $X=x$, and $Y(m)$, the potential value of $Y$ for $M=m$, and define $\mathbf{M}=(M(0), M(1)), \mathbf{Y}=$ $(Y(0), Y(1))$. We observe $X, M=M(X)$ and $Y=Y(M)$. We assume the exchangeability and the ignorability conditions, the latter expressed as mutual independence between $X$, $\mathbf{M}$ and $\mathbf{Y}$. This implies the observational conditional independence

$$
Y \Perp X \mid M
$$

which is a testable implication of our assumptions. We assume we have data supplying values for $\operatorname{Pr}(M=m \mid X=x)$ and $\operatorname{Pr}(Y=y \mid M=m)$, and compute, by (38),

$$
\operatorname{Pr}(Y=y \mid X=x)=\sum_{m} \operatorname{Pr}(Y=y \mid M=m) \operatorname{Pr}(M=m \mid X=x)
$$

For the case that $M$ is observed in the experimental data, but not for Juanita, Dawid et al. (2016) showed that this additional information does not change the lower bound $l$ on PC in (30), but does lower the upper bound, $u$. Dawid \& Musio (2021) extend this analysis to cases with additional covariates, while Dawid et al. (2019) deal with the case that we have a complete mediation sequence $X=M_{0} \rightarrow M_{1} \rightarrow \cdots \rightarrow M_{n-1} \rightarrow M_{n}=Y$, and know the probabilistic structure of each link in the chain; with all, some, or none of the $M$ s being observed for Juanita.

## 16. Further CoE problems

We have only dealt here with the case of a single putative cause, understanding causation in terms of the "but for" criterion. There are many more complex problems that can not be handled in this way: in particular, the whole field of legal causation has to handle a wide variety of problems involving multiple competing causes and other concepts of causality (Hart \& Honore 1985, Goldberg 2011). While there have been some interesting statistical treatments of specific problems, e.g., Cox (I984), it seems fair to say that general philosophical understandings of causality in such problems have not reached maturity. To the extent that problems are modelled in formal terms, this often involves a purely deterministic understanding of causality, which is not easily translated into a stochastic framework. Halpern

(2016) makes an interesting attempt to pin down the concept of "the actual cause" using the SCM framework, but admits that he is unable to reach a fully satisfying conclusion.

There is clearly much ground remaining to be covered in understanding "causes of effects", but it is perhaps premature to attempt more detailed statistical treatment before clearer general principles have emerged.

# CONCLUSION 

We have presented a thorough account of a number of ways in which the statistical problems of effects of causes (EoC) and of causes of effects (CoE) have been formulated. Although most treatments of statistical causality use essentially identical tools to address both these problem areas, we consider that this is inappropriate. Popular formalisms, such as potential outcomes and structural causal models, involve deterministic relations, and allow formal statements concerning two or more parallel worlds simultaneously. While something of this nature appears unavoidable for CoE considerations, it is unnecessary for EoC analyses, which can proceed using stochastic models and statistical decision theory. Furthermore, the use of an inappropriate formal framework brings with it the danger that we treat any mathematically well-formed formula (such as those describing "individual causal effect" and "local average treatment effect") as meaningful, when it may not be.

## DISCLOSURE STATEMENT

The authors are not aware of any affiliations, memberships, funding, or financial holdings that might be perceived as affecting the objectivity of this review.

## ACKNOWLEDGMENTS

The second author was partially supported by the project STAGE of Fondazione di Sardegna.

## LITERATURE CITED

Angrist J, Imbens G, Rubin DB. 1996. Identification of causal effects using instrumental variables. Journal of the American Statistical Association 91:444-455
Balke AA, Pearl J. 1997. Bounds on treatment effects from studies with imperfect compliance. Journal of the American Statistical Association 92:1172-6
Beyea J, Greenland S. 1999. The importance of specifying the underlying biologic model in estimating the probability of causation. Health Physics 76:269-274
Bowden RJ, Turkington DA. 1984. Instrumental Variables. Cambridge University Press
Bühlmann P. 2020. Invariance, causality and robustness (with Discussion). Statistical Science $35: 404-436$
Case Report. 2015. Hempstead v. Pfizer, Inc. (In re Lipitor (Atorvastatin Calcium) Mktg., Sales Practices \& Prods. Liab. Litig. 150 F. Supp. 3d 644 (D.S.C. 2015)
Constantinou P, Dawid AP. 2017. Extended conditional independence and applications in causal inference. Annals of Statistics 45:2618-2653
Corradi F, Musio M. 2020. Causes of effects via a Bayesian model selection procedure. Journal of the Royal Statistical Society, Series A 183:1777-1792

Cowell RG, Dawid AP, Lauritzen SL, Spiegelhalter DJ. 1999. Probabilistic Networks and Expert Systems. New York: Springer
Cox LA. I984. Probability of causation and the attributable proportion of risk. Risk Analysis 4:221230
Dawid AP. 1976. Properties of diagnostic data distributions. Biometrics 32:647-658
Dawid AP. 1979. Conditional independence in statistical theory (with Discussion). Journal of the Royal Statistical Society, Series B 41:1-31
Dawid AP. 2000. Causal inference without counterfactuals (with Discussion). Journal of the American Statistical Association 95:407-448
Dawid AP. 2003. Causal inference using influence diagrams: The problem of partial compliance (with Discussion), In Highly Structured Stochastic Systems, eds. PJ Green, NL Hjort, S Richardson, pp. 45-81, Oxford University Press
Dawid AP. 2010. Beware of the DAG!, In Proceedings of the NIPS 2008 Workshop on Causality, eds. I Guyon, D Janzing, B Schölkopf, vol. 6 of Journal of Machine Learning Research Workshop and Conference Proceedings, pp. 59-86. http://tinyurl.com/33va7tm
Dawid AP. 2015. Statistical causality from a decision-theoretic perspective. Annual Review of Statistics and its Application 2:273-303
Dawid AP. 2017. On individual risk. Synthese 194:3445-3474
Dawid AP. 2021a. Decision-theoretic foundations for statistical causality (with Discussion). Journal of Causal Inference (in Press) arXiv:2004.12493
Dawid AP. 2021b. The tale wags the DAG. In Probabilistic and Causal Inference: The Works of Judea Pearl, eds. R Dechter, H Geffner, J Halpern. Association for Computing Machinery. (In Press).
Dawid AP, Didelez V. 2012. "Imagine a can opener" - The magic of principal stratum analysis. International Journal of Biostatistics 8. DOI: 10.1515/1557-4679.1391
Dawid AP, Faigman DL, Fienberg SE. 2014. Fitting science into legal contexts: Assessing effects of causes or causes of effects? (with Discussion and authors' rejoinder). Sociological Methods and Research 43:359-421
Dawid AP, Faigman DL, Fienberg SE. 2015. On the causes of effects: Response to Pearl. Sociological Methods and Research 44:165-174
Dawid AP, Humphreys M, Musio M. 2019. Bounding causes of effects with mediators. arXiv:1907.00399
Dawid AP, Murtas R, Musio M. 2016. Bounding the probability of causation in mediation analysis, In Topics on Methodological and Applied Statistical Inference, eds. TD Battista, E Moreno, W Racugno, pp. 75-84, Springer
Dawid AP, Musio M. 2021. What can group level data tell us about individual causality? In Statistics in the Public Interest, eds. A Carriquiry, W Eddy, J Tanur. Springer. In Press
Dawid AP, Musio M, Murtas R. 2017. The probability of causation. Law, Probability and Risk 16:163-179
Faigman DL, Monahan J, Slobogin C. 2014. Group to individual (G2i) inference in scientific expert testimony. University of Chicago Law Review 81:417-480
Goldberg R, ed. 2011. Perspectives on Causation, Oxford. Hart Publishing
Greenland S. 1999. Relation of probability of causation to relative risk and doubling dose: A methodologic error that has become a social problem. American Journal of Public Health 89:1166-1169
Halpern JY. 2016. Actual Causality. Cambridge, Massachusetts: MIT Press
Hart HLA, Honore AM. 1985. Causation in the Law. Oxford: Clarendon Press
Hausman D. 1998. Causal Asymmetries. Cambridge: Cambridge University Press
Holland PW. 1986. Statistics and causal inference (with Discussion). Journal of the American Statistical Association 81:945-970.
Holland PW. 1988. Causal inference, path analysis, and recursive structural equations models. Sociological Methodology 18:449-484

Imbens GW, Angrist J. 1994. Identification and estimation of local average treatment effects. Econometrica $62: 467-476$
Katan MB. 1986. Apolipoprotein E isoforms, serum cholesterol, and cancer. The Lancet 327:507-508
Kuroki M, Cai Z. 2011. Statistical analysis of 'probabilities of causation' using co-variate information. Scandinavian Journal of Statistics 38:564-577
Lauritzen SL, Dawid AP, Larsen BN, Leimer HG. 1990. Independence properties of directed Markov fields. Networks 20:491-505
Lewis DK. 1973. Counterfactuals. Oxford: Blackwell
Mackie JL. 1980. The Cement of the Universe: A Study of Causation. Oxford University Press
Mill JS. 1843. A system of logic, ratiocinative and inductive: Being a connected view of the principles of evidence, and methods of scientific investigation. London: John W. Harper
Pearl J. 2009. Causality: Models, Reasoning and Inference. Cambridge: Cambridge University Press, Second ed.
Pearl J. 2015. Causes of effects and effects of causes. Sociological Methods and Research 44:149-164
Pearl J, Mackenzie D. 2018. The Book of Why. New York: Basic Books
Price H. 1991. Agency and probabilistic causality. British Journal for the Philosophy of Science $42: 157-176$
Reichenbach H. 1956. The Direction of Time. Berkeley: University of Los Angeles Press
Robins JM, Greenland S. 1989. The probability of causation under a stochastic model for individual risk. Biometrics 45:1125-1138
Rubin DB. 1974. Estimating causal effects of treatments in randomized and nonrandomized studies. Journal of Educational Psychology 66:688-701
Tian J, Pearl J. 2000. Probabilities of causation: Bounds and identification. Annals of Mathematics and Artificial Intelligence 28:287-313
Verma T, Pearl J. 1990. Causal networks: Semantics and expressiveness, In Uncertainty in Artificial Intelligence 4, eds. RD Shachter, TS Levitt, LN Kanal, JF Lemmer, pp. 69-76, Amsterdam: North-Holland
Woodward J. 2003. Making Things Happen: A Theory of Causal Explanation. Oxford: Oxford University Press
Woodward J. 2016. Causation and manipulability. The Stanford Encyclopedia of Philosophy, Edward N. Zalta (ed.).
https://plato.stanford.edu/entries/causation-mani/
Wright SS. 1921. Correlation and causation. Journal of Agricultural Research 20:557---585