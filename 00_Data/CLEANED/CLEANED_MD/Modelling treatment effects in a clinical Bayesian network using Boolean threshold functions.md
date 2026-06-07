# Modelling treatment effects in a clinical Bayesian network using Boolean threshold functions 

Stefan Visscher ${ }^{\text {a }}$, Peter J.F. Lucas ${ }^{\text {b,* }}$, Carolina A.M. Schurink ${ }^{\text {c }}$, Marc J.M. Bonten ${ }^{\text {a, }}$ d<br>${ }^{a}$ Department of Internal Medicine and Infectious Diseases, University Medical Center Utrecht, HP F.02.126, Heidelberglaan 100, 3584 CX Utrecht, The Netherlands<br>${ }^{\text {b }}$ Institute for Computing and Information Sciences, Radboud University Nijmegen, Toernooiveld 1, 6525 ED Nijmegen, The Netherlands<br>${ }^{\text {c }}$ Department of Medical Microbiology and Infectious Diseases, Erasmus University Medical Center, L327, 's Gravendijkwal 230, 3015 CE Rotterdam, The Netherlands<br>${ }^{\text {d }}$ Department of Medical Microbiology, University Medical Center Utrecht,<br>HP. G.04.614, Heidelberglaan 100, 3584 CX Utrecht, The Netherlands

Received 22 April 2008; received in revised form 11 August 2008; accepted 6 November 2008

## KEYWORDS

Computer-based medical decision making;
Decision-support systems;
Bayesian networks;
Causal independence models;
Boolean threshold functions;
Ventilator-associated pneumonia;
Treatment selection

## Summary

Objective: Appropriate antimicrobial treatment of infections in critically ill patients should be started as soon as possible, as delay in treatment may reduce a patient's prognostic outlook considerably. Ventilator-associated pneumonia (VAP) occurs in patients in intensive care units who are mechanically ventilated and is almost always preceded by colonisation of the respiratory tract by the causative microorganisms. It is very difficult to clinically diagnose VAP and, therefore, some form of computerbased decision support might be helpful for the clinician.
Materials and methods: As diagnosing and treating VAP involves reasoning with uncertainty, we have used a Bayesian network as the primary tool for building a decision-support system. The effects of usage of antibiotics on the colonisation of the respiratory tract by various pathogens and the subsequent antibiotic choices in case of VAP were modelled using the notion of causal independence. In particular, the conditional probability distribution of the random variable that represents the overall coverage of pathogens by antibiotics was modelled in terms of the conjunctive effect of the seven different pathogens, usually referred to as the noisy-AND model. In this paper, we investigate different coverage models, as well as generalisations of the

[^0]
[^0]:    * Corresponding author.

    E-mail addresses: Stefan.Visscher@gmail.com (S. Visscher), peterl@cs.ru.nl (P.J.F. Lucas),
    C.Schurink@ErasmusMC.nl (C.A.M. Schurink), mbonten@umcutrecht.nl (M.J.M. Bonten).

noisy-AND, called noisy-threshold models, and test them on clinical data of intensive care unit (ICU) patients who are mechanically ventilated.
Results: Some of the constructed noisy-threshold models offered further improvement of the performance of the Bayesian network in covering present causative pathogens by advising appropriate antimicrobial treatment.
Conclusions: By reconsidering the modelling of interactions between the random variables in a Bayesian network using the theory of causal independence, it is possible to refine its performance. This was clearly shown for our Bayesian network concerning VAP, indicating that only specific noisy-threshold models might be appropriate for the modelling of the interaction between pathogens and antimicrobial treatment with respect to susceptibility. The results obtained also provide evidence that the noisy-OR and noisy-AND might not always be the best functions to model interactions among random variables.
(C) 2008 Elsevier B.V. All rights reserved.

## 1. Introduction

Establishing an accurate diagnosis and choosing appropriate treatment for infections are desirable, especially when it concerns critically ill patients. In the intensive care unit (ICU) patients who depend on respiratory support are prone to develop ventilatorassociated pneumonia, or VAP for short. Although it is important to start antimicrobial treatment for VAP as soon as possible, when indicated, unnecessary antimicrobial treatment will enhance selection of antibiotic-resistant pathogens, which may subsequently hamper the treatment future infections. Since the accurate diagnostic tests for diagnosing VAP (i.e., bronchoscopy with quantitative microbiological cultures) are invasive, expensive and labour intensive, some form of computer-based decision support could be helpful in the process of early diagnosis and treatment of VAP.

Previously, we have developed a computer-based decision-support system (DSS) that is aimed at assisting physicians with the diagnosis and treatment of VAP. The model underlying the DSS consists of a Bayesian network with an associated decisiontheoretic part. The structure as well as the conditional probabilities and utilities were elucidated with the help of two infectious-disease specialists (IDS). The resulting decision-theoretic model, or influence diagram, was translated into a Bayesian network, and this is the model currently used (cf. Ref. [1] for details concerning the model and the construction process of the model). The probability of VAP is computed using the diagnostic part of the Bayesian network. In addition, the therapeutic part of the network can be used to determine the best possible combination of antibiotics.

When prescribing antimicrobial treatment a physician intends to cover all microorganisms causing the infection, using an antibiotic with the narrowest possible spectrum. This policy aims at preventing antibiotic resistance and at saving costs [2]. This was
already taken into account when constructing the DSS, described in more detail in Ref. [1]. To cover as many pathogens as possible by the antibiotic treatment advised by the DSS, a noisy-AND probabilistic model was used in the Bayesian network for the modelling of the probabilistic interactions of the effects of the prescribed antibiotics on the pathogens, taking into account colonisation by those pathogens. However, this approach yielded antibiotic choices that were considered much too broad.

The start of the current research reported in this paper is an analysis of the reason of this behaviour of the model, and a number of alternatives to define this particular conditional probability distribution are studied. As the noisy-AND is a special case of the more general class of probabilistic models based on the Boolean threshold functions, Boolean functions that are defined in terms of the number of truths among Boolean values, it is also studied theoretically what happens when the AND is replaced by a threshold function. The resulting probabilistic models are called noisy-threshold models [3,4]. Arguments are presented why we expect that a noisythreshold model might work better than the noisyAND. Finally, behaviour of the various noisy-threshold probabilistic models is investigated by replacing the noisy-AND used, using data of patients with VAP from the ICU of the University Medical Center, Utrecht. It is also investigated whether the therapeutic performance of the Bayesian network for VAP improves in this way.

Although we focus on an actual clinical problem the prescription of antibiotics for patients with VAP - this problem can be seen as an instance of a common and important problem in medicine: the modelling of the effectiveness of treatment. In this sense, the results achieved here have a bearing on a clinical area wider than infectious disease.

The paper is organised as follows. In the next section, our earlier work on the development of a Bayesian network that is able to assist physicians in

the diagnosis and treatment of VAP is briefly reviewed. In Section 3, the mathematical principles of causal independence models are discussed and noisy-threshold models are introduced. Furthermore, three different models of antimicrobial coverage are constructed and analysed. In Section 4, the data and methods used in evaluating the Bayesian networks incorporating the threshold functions are described. The results achieved are commented on in Section 5. The paper is rounded off by some conclusions in Section 6.

## 2. A Bayesian network for the management of VAP

Bayesian networks, or BNs for short, have been introduced in the 1980s as a formalism to compactly represent and reason efficiently with joint probability distributions. Bayesian networks are in particular well suited for the representation of causal relations within a specific domain of expertise.

Formally, a Bayesian network $\mathcal{B}=(G, \operatorname{Pr})$ is an acyclic directed graph $G=(\mathrm{V}(G), \mathrm{A}(G))$ with set of vertices $\mathrm{V}(G)=\left\{V_{1}, \ldots, V_{n}\right\}$, corresponding to random variables, here denoted by the same letters or strings of characters, and a set of arcs $\mathbf{A}(G) \subseteq \mathbf{V}(G) \times \mathbf{V}(G)$, representing statistical dependences and independences among the variables. On the set of random variables, a joint probability distribution $\operatorname{Pr}(\mathrm{V}(G))$ is defined that is factorised according to the structure of the graph:
$\operatorname{Pr}(\mathrm{V}(G))=\prod_{V \in \mathrm{~V}(G)} \operatorname{Pr}(V \mid \pi(V))$,
where $\pi(V)$ stands for the variables corresponding to the parents of vertex $V$.

In the following, we will often make use of binary random variables. If the variable $X$ assumes the value 'true' or 'yes', this will be sometimes indicates by $x$, whereas if $X$ assumes the value 'false' or 'no', this will be indicated by $\neg x$.

The formalism of BNs supports the kind of reasoning under uncertainty that is typical for medicine when dealing with diagnosis, treatment selection, planning, and prediction of prognosis. Our clinical domain is restricted to patients who are mechanically ventilated and are at risk of developing VAP. Entities that play an important role in the development of VAP and that belong to the diagnostic part of the Bayesian network for VAP include: the duration of mechanical ventilation, the amount of sputum, radiological signs, i.e., whether the chest radiogram shows signs of an infection, body temperature of the patient and the number of leukocytes (white blood cells) [5]. The structure of the Bayesian net-
![img-0.jpeg](img-0.jpeg)

Figure 1 Abstract model of the Bayesian network for the management of VAP. Colonisation and VAP play a central role in this model. The duration of hospitalisation and mechanical ventilation influence colonisation (col.) of the patient. PA: Pseudomonas aeruginosa; HI: Haemophilus influenzae; SP: Streptococcus pneumoniae; Ent[1,2]: Enterobacteriaceae[1,2]; SA: Staphylococcus aureus; AC: Acinetobacter spp. Each pathogen is susceptible (suscept.) to particular antibiotics and an optimal coverage of pathogens is what the model aims to achieve. The duration of mechanical ventilation, immunological status and colonisation influence the development of VAP. When a patient is diagnosed with VAP, the patient often has symptoms such as an increased body temperature. Boxes denote entities or processes which are observed; processes that change or can be changed are denoted by ellipses.
work for VAP is shown in Fig. 1. Mechanically ventilated ICU patients become colonised by bacteria. When colonisation of the lower respiratory tract occurs within 2-4 days after intubation, this is usually caused by antibiotic-sensitive bacteria, whereas after one week of intubation often anti-biotic-resistant bacteria are involved in colonisation and infection. Such infections are more difficult to treat and immediate start of appropriate treatment in case of infection is, therefore, important. Duration of hospital stay and severity of illness are associated with an increased risk of colonisation and infection with Gram-negative bacteria. We modelled seven groups of microorganisms, each by one vertex in the Bayesian network, and the pathogenicity, i.e., the influence of that particular microorganism on the development of VAP, was included in the model. The presence of certain bacteria is influenced by antimicrobial therapy; however, a microorganism is susceptible only for particular antibiotics. Susceptibility, in this case, is stated as the sensitivity to or degree to which a microorganism is affected by treatment with a specific antibiotic. The susceptibility of each microorganism was taken into account while constructing

the model. The infectious-disease experts assigned utilities, by definition quantitative measures of the strength of the preference for an outcome [6], to each combination of microorganism(s) and antimicrobial drug(s) using a decision-theoretic model. These variables are included in the therapeutic part of the Bayesian network for VAP.

## 3. Causal independence modelling

Causal independence is a popular means to facilitate the specification of conditional probability distributions $\operatorname{Pr}\left(V_{i} \mid \pi\left(V_{i}\right)\right)$ involving many parent variables $\pi\left(V_{i}\right)$. Its basic principles and some special forms are briefly discussed below.

### 3.1. Basic principles

Consider the conditional probability distribution $\operatorname{Pr}\left(E \mid C_{1}, \ldots, C_{n}\right)$, where the variable $E$ stands for an effect, e.g., coverage, and the variables $C_{j}, j=1, \ldots, n$, denote causes, e.g., colonisation by pathogens in combination with treatment by means of antibiotics. By taking a number of assumptions into account, which are summarised in Fig. 2, it is possible to simplify the specification of $\operatorname{Pr}\left(E \mid C_{1}, \ldots, C_{n}\right)$. These assumptions are: (1) the causes $C_{j}$ are assumed to be mutually independent, and (2) the variable $E$ is conditionally independent of any cause variable $C_{j}$ given the intermediate variables $I_{1}, \ldots, I_{n}$. In our domain the intermediate variable $I_{j}$ stands for susceptibility of pathogen ${ }_{j}$ to a specific antibiotic. Using basic probability theory, it follows that:
$\operatorname{Pr}\left(e \mid C_{1}, \ldots, C_{n}\right)=\sum_{I_{1}, \ldots, I_{n}} \operatorname{Pr}\left(e \mid I_{1}, \ldots, I_{n}\right) \prod_{j=1}^{n} \operatorname{Pr}\left(I_{j} \mid C_{j}\right)$.
Now, if we assume that the probability distribution $\operatorname{Pr}\left(E \mid I_{1}, \ldots, I_{n}\right)$ that is specified for variable $E$ expresses some deterministic function $f: I_{1} \times \cdots \times I_{n} \rightarrow E$, with $I_{j}, E \in\{\perp, \top\}$, called an interaction function, an alternative formalisation is
![img-1.jpeg](img-1.jpeg)

Figure 2 Causal independence model.
possible. Using the interaction function $f$ and the causal parameters $\operatorname{Pr}\left(I_{j} \mid C_{j}\right)$, it follows that $[7,3,8]$ :
$\operatorname{Pr}\left(e \mid C_{1}, \ldots, C_{n}\right)=\sum_{f\left(I_{1}, \ldots, I_{n}\right)=e} \prod_{j=1}^{n} \operatorname{Pr}\left(I_{j} \mid C_{j}\right)$.
The result is called a causal independence model $[7,9,3]$. In this paper we assume that the function $f$ in Eq. (2) is a Boolean function. The consequences are that instead of a specification of a conditional probability distribution that is exponential in size, one only needs to specify a conditional probability distribution in terms of a linear number of parameters $\operatorname{Pr}\left(I_{j} \mid C_{j}\right)$ and a Boolean function $f$.

Systematic analyses of the global probabilistic patterns in causal independence models based on restricted Boolean functions were presented in Refs. [3,10]. There are $2^{2^{n}}$ different $n$-ary Boolean functions [11,12]; thus, the potential number of causal interaction models is huge. If we assume that the order of the cause variables does not matter, the Boolean functions become symmetric; formally, an interaction function $f$ is called symmetric if [12]
$f\left(I_{1}, \ldots, I_{n}\right)=f\left(I_{j_{1}}, \ldots, I_{j_{n}}\right)$
for any index function $j:\{1, \ldots, n\} \rightarrow\{1, \ldots, n\}$ [12]. The number of different Boolean function reduces then to $2^{n+1}$. Examples of symmetric binary Boolean functions include the logical OR, AND, exclusive OR and bi-implication. An example of a general, possibly non-binary, symmetric Boolean function is the exact Boolean function $e_{k}$, which is defined as follows [12,3]:

Definimos la función exacta $e_k$ como:

$$
e_{k}\left(I_{1}, \ldots, I_{n}\right)=
\begin{cases}
\top & \text{si } \sum_{j=1}^{n} v\left(I_{j}\right)=k, \\[6pt]
\perp & \text{en otro caso},
\end{cases}
$$

con $k \in \mathbb{N}$, y donde

$$
v(I)=
\begin{cases}
1 & \text{si } I=\top, \\[6pt]
0 & \text{en otro caso}.
\end{cases}
$$

Aquí, $\top$ denota “verdadero” y $\perp$ denota “falso”.

---

Las funciones booleanas simétricas pueden descomponerse en términos de las funciones exactas $e_k$ de la siguiente forma:

$$
f\left(I_{1}, \ldots, I_{n}\right)= \bigvee_{k=0}^{n} \left(e_{k}\left(I_{1}, \ldots, I_{n}\right) \wedge \gamma_{k}\right),
$$

donde $\gamma_{k}$ son constantes booleanas que dependen únicamente de la función $f$.

---

Usando este resultado, la probabilidad condicional de la ocurrencia del efecto $E$, dado que se presentan las causas $C_{1}, \ldots, C_{n}$, puede expresarse en términos de las probabilidades de que exactamente $k$ de las variables intermedias $I_{1}, \ldots, I_{n}$ sean verdaderas:

$$
\Pr\left(E \mid C_{1}, \ldots, C_{n}\right)
= \sum_{k=0}^{n} \gamma_{k}\;
\Pr\!\left(e_{k}\left(I_{1}, \ldots, I_{n}\right)\,\middle|\, C_{1}, \ldots, C_{n}\right).
$$

Si además suponemos independencia condicional entre los $I_j$ dado cada $C_j$, se tiene:

$$
\Pr\!\left(e_{k}\left(I_{1}, \ldots, I_{n}\right)\,\middle|\, C_{1}, \ldots, C_{n}\right)
= \sum_{\substack{S \subseteq \{1,\dots,n\} \\ |S| = k}} \;\prod_{j \in S}\Pr(I_j \mid C_j)\;\prod_{j \notin S}\bigl(1-\Pr(I_j \mid C_j)\bigr).
$$

Thus, Eq. (5) yields a general formula to compute the probability of the effect in terms of exact functions in any causal independence model where an interaction function $f$ is a symmetric Boolean function.

The interaction among variables modelled by the susceptibility, or coverage variables, as shown in Fig. 1, was modelled by assuming $f$ to be a logical AND. The resulting probabilistic model $\operatorname{Pr}\left(E \mid C_{1}, \ldots, C_{n}\right)$ is usually called the noisy-AND model, or noisy-AND for short. The probability distribution of the variable that represents the overall susceptibility (coverage in Fig. 1), models the conjunctive effect of the seven different pathogens. This principle is modelled by a probability distribution $\operatorname{Pr}\left(E \mid C_{1}, \ldots, C_{n}\right)$ that is defined as in Eq. (1) by the noisy-AND, yielding the following equation:

$$
\begin{aligned}
& \operatorname{Pr}(\text { coverage } \mid \text { Colonisation }_{1}, \ldots, \text { Colonisation }_{n} \\
& \text { Antibiotics) } \\
& =\prod_{j=1}^{n} \operatorname{Pr}\left(\text { susceptibility-pathogen }_{j} \mid \text { Colonisation }_{j}\right. \\
& \text { Antibiotics) }
\end{aligned}
$$

By adopting this modelling approach, the network attempts to cover all pathogens in choosing appropriate antimicrobial treatment. As revealed in our dataset, patients were colonised by at most 3 pathogens. Therefore, covering all 7 possible groups of pathogens is simply too much and results, most of the time, in antimicrobial treatments that are too broad. Furthermore, in modelling the effect of antibiotics on the susceptibility, one also needs to express what effect the absence of colonisation has in the absence or presence of antimicrobial treatment. In the next section, both issues will be explored in detail. Both issues have raised doubts on the appropriateness of the noisy-AND for the modelling of interactions concerning coverage of bacteria by antibiotics.

As the methods which are developed subsequently are generic, a slightly more general terminology than the one above will be adopted. Thus, in the following, 'coverage' will be abbreviated to $O$ (outcome), 'sus-ceptibility-pathogen ${ }_{j}$ ' by $S_{j}$ (susceptibility), 'Colonisation ${ }_{j}$ ' by $C_{j}$ (causal factor) and 'Antibiotics' by $M$ (medication), i.e., the conditional probability distribution that is studied is of the form
$\operatorname{Pr}\left(O \mid C_{1}, \ldots, C_{n}, M\right)$.

### 3.2. Bayesian network coverage models

As argued in Section 1, it is generally felt that clinicians could be more careful in the prescription
of antibiotics as they tend to prescribe antibiotics that are either not needed or have a too broad spectrum [13]. A symmetric Boolean function that is useful in designing a generalised version of the noisy-AND is the threshold function $\tau_{k}$, which simply checks whether there are at least $k$ trues among its arguments; it is defined as follows:
$\tau_{k}\left(I_{1}, \ldots, I_{n}\right)= \begin{cases}\top & \text { if } \sum_{j=1}^{n} v\left(I_{j}\right) \geq k \\ \perp & \text { otherwise }\end{cases}$
where again $v\left(I_{j}\right)$ equals 1 if $I_{j}$ equals $T$ (true) and 0 otherwise [12]. Let us denote a conditional probability of the effect $E$ given causes $C_{1}, \ldots, C_{n}$ in a noisythreshold model with interaction function $\tau_{k}$ as $\operatorname{Pr}_{\tau_{k}}\left(e \mid C_{1}, \ldots, C_{n}\right)$. Then, from Eq. (5) it follows that:
$\operatorname{Pr}_{\tau_{k}}\left(e \mid C_{1}, \ldots, C_{n}\right)=\sum_{k \leq I \leq n} \sum_{e_{i}\left(I_{1}, \ldots, I_{n}\right)} \prod_{j=1}^{n} \operatorname{Pr}\left(I_{j} \mid C_{j}\right)$.
Note that the Boolean AND corresponds to the threshold function $\tau_{k}$ with $k=n$, whereas the Boolean OR is a threshold function with $k=1$. Hence, the AND and OR can be seen as the extremes of a spectrum of Boolean functions based on the threshold function.

The prototypical structure that can be used to model the outcome $O$ of medication $M$ on the causal factors $C_{j}$ is shown in Fig. 3; it offers a possible way to model the conditional probability distribution of Formula (6). The resulting decomposition then has the following form:
$\operatorname{Pr}_{\tau_{k}}\left(o \mid C_{1}, \ldots, C_{n}, M\right)=\sum_{k \leq I \leq n} \sum_{e_{i}\left(S_{1}, \ldots, S_{n}\right)} \prod_{j=1}^{n} \operatorname{Pr}\left(S_{j} \mid C_{j}, M\right)$.
There are various choices possible for the conditional probability distributions
$\operatorname{Pr}\left(S_{j} \mid C_{j}, M\right)$
![img-2.jpeg](img-2.jpeg)

Figure 3 Prototypical structure for investigating outcome of medication $M$, based on the susceptibility of the causal factors $C_{j}$ to that medication. The meaning of the used abbreviations is as follows: $C_{j}$ : causal factor $J ; S_{j}$ : susceptibility to medication; $M$ : treatment by antimicrobial medication; $O$ : overall outcome. The variable $O$ is taken as a measure of success of the treatment.

that are associated with the vertex $S_{j}$ (susceptibility) indicated in Figure 3. Let us for simplicity's sake assume that $M$ takes only two values: 'no' (sometimes indicated by $\neg m$ ), which corresponds to the situation where no treatment is given, and 'yes' (sometimes indicated by $m$ ), which corresponds to the situation that drugs are given that influence some susceptibilities $S_{j}$. For the example, we also assume this probability distribution to be deterministic, which normally will not hold in real life. One way to define the probability distribution (9) is as follows:
$\operatorname{Pr}\left(s_{j} \mid C_{j}, M\right)=\left\{\begin{array}{l}0 \text { if } C_{j}=\text { yes, } M=\text { no } \\ 1 \text { otherwise }\end{array}\right.$
![img-3.jpeg](img-3.jpeg)
(a)
![img-4.jpeg](img-4.jpeg)
(c)
![img-5.jpeg](img-5.jpeg)
(e)

We call this definition the 'susceptibility I model'. The implication of this definition is that treatment is always successful in the absence of the causal factors, such as the absence of colonisation in the case of VAP. Although this may seem natural at first sight, a disadvantage is that when optimising the medication, it is likely that causal factors that have no effect, will have a major influence on the choice of medication. In case of VAP this means that absence of colonisation is consistent with medication.

Another way to model susceptibility might be to change the probability distribution above by
![img-6.jpeg](img-6.jpeg)
(b)
![img-7.jpeg](img-7.jpeg)
(d)
![img-8.jpeg](img-8.jpeg)
(f)

Figure 4 Comparison of the three different susceptibility models, assuming that the patient is colonised by one microorganism, where each subfigure includes the results of three threshold interactions functions: $\tau_{1}$ (Coverage_AND), $\tau_{2}$ (Coverage_2) and $\tau_{1}$ (Coverage_OR). To the left are shown the marginal probability distributions when the choice is to give no medication; to the right are shown the marginal probability distributions when effective medication against the infection is given. (a) Susceptibility I model; colonisation by 1 microorganism, no medication. (b) Susceptibility I model; colonisation by 1 microorganism, effective medication. (c) Susceptibility II model; colonisation by 1 microorganism, no medication]. (d) Susceptibility II model; colonisation by 1 microorganism, effective medication. (e) Susceptibility III; colonisation by 1 microorganism, no medication. (f) Susceptibility III model; colonisation by 1 microorganism, effective medication.

stating that $\operatorname{Pr}\left(s_{i} \mid \neg c_{i}, \neg m\right)=1$, whereas $\operatorname{Pr}\left(s_{i} \mid \neg c_{i}, m\right)=0$. We call this definition the 'susceptibility II model'; it has the advantage that when optimising medication, it is unlikely that a drug will be selected in the absence of the causal factor. However, a disadvantage is that the model may select no medication when only a few causal factors are active, and covering the inactive causal factors would already be optimal. In the case of VAP this corresponds to covering absent colonisation by no medication.

A third way to model likelihood of susceptibility is to take almost the reverse of the definition above:
$\operatorname{Pr}\left(s_{j} \mid C_{j}, M\right)= \begin{cases}1 & \text { if } C_{j}=\text { yes }, M=\text { yes } \\ 0 & \text { otherwise }\end{cases}$
We call this definition the 'susceptibility III model'. This implies that as long as causal factors are active, the optimal policy is to cover those by medication. For VAP this means coverage of the microorganisms colonising a patient by means of appropriate treatment.
![img-9.jpeg](img-9.jpeg)

Figure 5 Comparison of susceptibility models II and III, assuming the patient is colonised by two microorganisms, with three threshold interactions functions: $\mathrm{r}_{3}$ (Coverage_AND), $\mathrm{r}_{2}$ (Coverage_2) and $\mathrm{r}_{1}$ (Coverage_OR), and assuming that no medication or effective medication is given, respectively. (a) Susceptibility II model; colonisation by 2 microorganisms, no medication. (b) Susceptibility II model; colonisation by 2 microorganisms, effective medication. (c) Susceptibility III model; colonisation by 2 microorganisms, no medication. (d) Susceptibility III model; colonisation by 2 microorganisms, effective medication. (e) Susceptibility III model; colonisation by 2 microorganisms, no medication. (f) Susceptibility III model; colonisation by 2 microorganisms, effective medication.

Another issue that should be considered concerns the choice of the Boolean interaction function $f$ corresponding to the deterministic probability distribution $\operatorname{Pr}\left(O \mid S_{1}, \ldots, S_{n}\right)$. In the original model, we took the logical AND as an implementation for this probability distribution. Using the threshold function $\tau_{k}$ with $k \neq 1, n$, may result in a more intuitive model. Using a particular way of exploiting the noisy-threshold functions, the network might be redesigned such that it only covers a fixed number of the causal factors. For the VAP model, it might, for example, cover $1(k=1)$, i.e., the noisy-OR, $2(k=2), 3$ $(k=3), 4(k=4), 5(k=5)$ or $6(k=6)$ of the causative pathogens compared to the noisy-AND gate, where all pathogens, i.e., $k=7$, are taken into account. However, as the behaviour of the entire Bayesian network model shown in Fig. 3 is not only determined by the probability distribution $\operatorname{Pr}\left(O \mid S_{1}, \ldots, S_{n}\right)$ but, in addition, also by $\operatorname{Pr}\left(S_{i} \mid C_{j}, M_{j}\right)$ we first need to study the various behaviours obtained by combining various definitions of these two conditional probability distributions. Next, we explore the consequences of choosing a particular combination of these two conditional probability distributions for the case of VAP.

The behaviour of the susceptibility I model, as shown in Fig. 4(a) and (b), indicates that no distinction is made between presence and absence of colonisation by a particular microorganism. As a consequence, all three threshold functions indicate coverage even when the patient is only colonised by one microorganism. Fig. 4(a) and (b) also indicate that as soon as effective treatment against the single microorganism by which the patient is colonised is selected, the noisy-AND concludes that it is able to cover all, i.e., both microorganism by which the patient is and is not colonised.

The results for the susceptibility II model with no medication, as shown in Fig. 4(c), are identical to those of Fig. 4(a). However, as medication is no longer assumed to cover microorganisms by which the patient has not been colonised, the noisy-AND and noisy- $\tau_{2}$ models indicate failure of coverage. This behaviour is identical to the probabilistic behaviour shown in Fig. 4(f).

As shown in Fig. 5(b) and (d), the susceptibility II and III models also give identical results if the patient is colonised by two microorganisms and being appropriately treated. However, as Fig. 5(a) and (c) indicate, the susceptibility II model indicates coverage of the single microorganism by which the patient has not been colonised when no medication is given, whereas the susceptibility III model indicates failure. Clearly, the susceptibility II model encodes a sort of symmetry between no treatment
in the absence of colonisation and treatment in the presence of colonisation, where the susceptibility III model is asymmetric and incorporates the implicit assumption that it is unlikely that patients are completely uncolonised and that taking this situation into account is therefore unnecessary. The susceptibility model III also clearly indicates probable coverage of microorganisms, as shown in Fig. 5(f) in the vertex concerning the noisy-AND, which appears to be another advantage.

Probability distributions $\operatorname{Pr}\left(E \mid C_{1}, \ldots, C_{n}\right)$ defined in terms of Boolean threshold functions using the same probabilistic parameters $\operatorname{Pr}\left(I_{k} \mid C_{k}\right)$ have the following important property (Monotonicity):
$\operatorname{Pr}_{\tau_{k}}\left(e \mid C_{1}, \ldots, C_{n}\right) \geq \operatorname{Pr}_{\tau_{k+1}}\left(e \mid C_{1}, \ldots, C_{n}\right)$
for each nonnegative integer $k$, where again $\operatorname{Pr}_{\tau_{k}}$ is a probability distribution defined in terms of the threshold function $\tau_{k}$. The proof follows directly from Eq. (7), as according to this equation

$$
\begin{aligned}
& \operatorname{Pr}_{\tau_{k}}\left(e \mid C_{1}, \ldots, C_{n}\right)+\sum_{e_{k+1}\left(I_{1}, \ldots, I_{n}\right)} \prod_{j=1}^{n} \operatorname{Pr}\left(I_{j} \mid C_{j}\right) \\
& \quad=\operatorname{Pr}_{\tau_{k+1}}\left(e \mid C_{1}, \ldots, C_{n}\right)
\end{aligned}
$$

and $\sum_{e_{k+1}\left(I_{1}, \ldots, I_{n}\right)} \prod_{j=1}^{n} \operatorname{Pr}\left(I_{j} \mid C_{j}\right) \geq 0$. This property is consistent with the probabilities of coverage depicted in the bar charts in Figs. 4 and 5, as the probability for the noisy-AND is never above that for $\tau_{2}$, which is never above that for the noisy-OR.

In the following we therefore investigate properties of the threshold function, and subsequently study its use in improving the Bayesian network model shown in Fig. 1.

### 3.3. Counting functions

So far we have assumed that the probability distributions
$\operatorname{Pr}\left(O \mid S_{1}, \ldots, S_{n}\right)$
are defined as single big tables. However, it is possible to decompose these probability distributions using a basic property of symmetric Boolean functions [12]. The values of a symmetric Boolean function can be represented as a vector $\left(v_{0}, \ldots, v_{n}\right)$ such that $f\left(I_{1}, \ldots, I_{n}\right)=v_{i}$ if $I_{1}+\cdots+I_{n}=I$. This means that it suffices to count the number of trues in the arguments of $f$, interpreting 'true' arithmetically as 1 and 'false' as 0 , and this can be done incrementally, as addition is commutative and associative: $I_{1}+\cdots+I_{n}=\left(\cdots\left(\left(I_{1}+I_{2}+I_{3}\right)+\cdots\right.\right.$ $\left.\left.+I_{n-1}\right), I_{n}\right)=I$. The probability distribution that corresponds to this counting is defined in terms of the following conditional probability distributions:

![img-10.jpeg](img-10.jpeg)

Figure 6 Decomposition of the conditional probability distribution $\operatorname{Pr}\left(O \mid S_{1}, \ldots, S_{n}\right)$.

$$
\begin{aligned}
& \operatorname{Pr}\left(O_{1}=v\left(I_{1}, I_{2}\right) \mid I_{1}, I_{2}\right) \quad=1 \\
& \operatorname{Pr}\left(O_{2}=v\left(O_{1}, I_{3}\right) \mid O_{1}, I_{3}\right) \quad=1 \\
& \vdots \\
& \operatorname{Pr}\left(O_{n-2}=v\left(O_{n-3}, I_{n-1}\right) \mid O_{n-3}, I_{n-1}\right)=1 \\
& \operatorname{Pr}\left(O_{n-1}=v_{i} \mid O_{n-2}, I_{n}\right) \\
& \quad=\left\{\begin{array}{ll}
1 & \text { if } v\left(O_{n-2}, I_{n}\right)=i \\
0 & \text { otherwise }
\end{array}\right.
\end{aligned}
$$

Note that the last variable, $O_{n-1} \equiv O$, is binary, whereas the other $O_{k}$ variables, $1 \leq k \leq n-2$, take values from the set $\left\{0, \ldots, v\left(o_{k-1}, I_{k+1}\right)\right\}$, where $o_{k-1}$ indicates the maximum value of the random vari-
![img-11.jpeg](img-11.jpeg)
able $O_{k-1}$. The resulting Bayesian network structure, when the susceptibility variables $S_{k}$ are taken as the intermediate variables $I_{k}$, is shown in Fig. 6.

For a threshold function $\tau_{k}$ it is only necessary that random variables take values out of the set $\{0,1, \ldots, k\}$, as when the maximum $k$ is reached, $\operatorname{Pr}\left(O \mid S_{1}, \ldots, S_{n}\right)=1$. An example is shown in Fig. 7.

## 4. Validation

The usefulness of the methods described above has been investigated for the Bayesian network concerning VAP, using data of actual ICU patients. The characteristics of the data are described in the next section, after which we return to the problem of the prescription of antibiotics to patients with VAP.

### 4.1. ICU data

We used a temporal database with 17,710 records, each record containing data of a period of 24 h of a mechanically ventilated patient admitted to the ICU of the University Medical Center Utrecht between 1999 and 2002. The database contains information of 2233 distinct patients. For 157 of these 2233 patients, a VAP was diagnosed according to the judgement of two infectious-disease specialists, which was subsequently considered as the reference standard. Four of 157 patients with VAP were
![img-12.jpeg](img-12.jpeg)

Figure 7 Example Bayesian network implementation of the decomposition of threshold function $\tau_{3}$. (a) Posterior probabilities for 2 observations. (b) Posterior probabilities for 3 observations.

excluded from analyses, as these infections were caused by a type of pathogen that was not modelled in the Bayesian network model. The distribution of all monobacterial (caused by one pathogen) and polymicrobial (caused by 2 or more pathogens) infections among patients with VAP is shown in Table 1.

### 4.2. Methods

In order to improve the therapeutic performance of the Bayesian network, the network was inspected in detail. Points for possible improvement that were identified included the way probable pathogen coverage by antibiotics was modelled for the assessment of the conditional probability distribution
$\operatorname{Pr}($ Coverage $)$ Colonisation $_{1}, \ldots$
Colonisation $_{7}$, Antibiotics),
as described in detail in Section 3.
Prescribing antibiotics that cover all likely pathogens is not an easy task for non-specialists. Normally, a fixed list of antimicrobials to which pathogens are susceptible, so-called susceptibility patterns, is available. As antibiotic resistance patterns differ between countries and even hospitals, this list may be different for each hospital. When susceptibility tests indicate resistance of the pathogen against antimicrobial $a$, another antibiotic, or combination of antibiotics, should be prescribed. In the model, susceptibility probabilities were computed using data from the Department of Medical Microbiology, indicated that in a particular percentage of cases pathogen $p$ was susceptible to antibiotic $a$.

As described earlier, there are several types of antibiotics; some antibiotics have a narrow spectrum and are effective against specific pathogens, whereas other antibiotics have a broad spectrum, that usually cover difficult-to-treat pathogens. In
addition, two groups of pathogens are clinically distinguished: early-onset and late-onset pathogens. The former are pathogens that colonise patients predominantly during the first 5 days of ICU admission, whereas the latter pathogens mainly occur after day 6 of ICU admission. Subdividing the pathogens modelled in our Bayesian network yields:

- Early:
- S. aureus
- H. influenzae
- S. pneumoniae
- Late:
- Enterobacteriaceae
- Acinetobacter spp.
- P. aeruginosa

For each pathogen, we selected the commonly used antibiotics, modelled in the Bayesian network, and that are highly effective according to laboratory data. For some pathogens, there are multiple antibiotics that are effective. Table 2 gives a summary of this information. For example, amoxicillin is a very narrow-spectrum antibiotic that is effective against-in other words, covers-both H. influenzae (HI) and S. pneumoniae (SP). Furthermore, in general, one would expect broad-spectrum antibiotics to have better coverage numbers than narrow-spectrum antibiotics.

For the assessment of the covering behaviour of the Bayesian network, the overall coverage for the pathogens of all 153 episodes of VAP was calculated, using different susceptibility models and threshold functions. In particular, we explored the question how well the model was able to cover the pathogens. To answer this question, the following assumptions were made:

1. presence of VAP was assumed, based on the reference standard and, therefore, the VAP vertex in the Bayesian-network model was always instantiated;

Table 1 Reference standard: frequency of VAP-causing pathogens.


Table 2 Antibiotics and their effectiveness (+). PA: P. aeruginosa; AC: Acinetobacter spp.; Ent[1,2]: Enterobacteriaceae; SA: S. aureus; HI: H. influenzae; SP: S. pneumoniae. Names of antibiotics are abbreviated, e.g., 'A' stands for amoxicillin; antimicrobial spectrum: vn: very narrow; n: narrow; i: intermediate; b: broad.


2. based on previous endotracheal culture data, the colonisation vertices in the model were instantiated to denote either the presence or absence of particular pathogens colonising a patient.

## 5. Results

The results of using different threshold functions and susceptibility models were subsequently computed. The probability of coverage, which was between $0 \%$ and $100 \%$, denotes how well a particular model was able to cover the present VAP-causing pathogens. However, these probabilities may not be correct. For example, it might be the case that, according to the model, there is $100 \%$ coverage of a pathogen by an antibiotic, where in reality this probability should be $0 \%$.

The tables have been split up in terms of earlyand late-onset VAP, as well as by the number of VAPcausing pathogens; Nr. 1 denotes that the patient was infected by one pathogen (monobacterial episodes), where Nr. 2 denotes that the patient has been infected by 2 pathogens (polymicrobial epi-
sodes). Table 5, for example, shows the results for the susceptibility I model for threshold functions $\tau_{1}$ (or equivalently, the noisy-OR) and $\tau_{2}$. In the 'Patho' column, the name of the pathogen is listed. The mean coverage for the in total 13 early-onset polymicrobial episodes of VAP when prescribing antibiotic B, i.e., amoxicillin-clavulanic acid, is 97 . Prescribing no antibiotics in this case would not be advisable, as column K indicates that coverage would then be zero.

The various definitions of Boolean threshold functions, from $\tau_{1}$ (noisy-OR), $\tau_{2} \ldots, \tau_{7}$ (noisy-AND) were combined with the three susceptibility models defined above. The following tables summarise the results obtained:

Susceptibility I model: Tables 3-8 show the results for susceptibility model I for threshold functions $\tau_{k}$, for $k=1, \ldots 7$.

Susceptibility II model: For $k=1, \ldots 5$ the coverage results obtained for this model are identical to those obtained for susceptibility model III, with the exception of the probabilities in column K, i.e., the case when no antibiotics are prescribed, which

Table 3 Predicting optimal treatment for 153 patients diagnosed with VAP using the (SI, $k=1,2$ ) model, distinguished by different number of colonising pathogens (Nr.). Mean coverage is specified for a selection of antibiotics.


Table 4 Predicting optimal treatment for 153 patients diagnosed with VAP using the (SI, $k=3$ ) model, distinguished by different number of colonising pathogens (Nr.). Mean coverage is specified for a selection of antibiotics.


Table 5 Predicting optimal treatment for 153 patients diagnosed with VAP using the (SI, $k=4$ ) model, distinguished by different number of colonising pathogens (Nr.). Mean coverage is specified for a selection of antibiotics.


are always $0 \%$ for model III and $100 \%$ for model II. For $k=6,7$ the pathogen coverages for susceptibility model II are equal to the coverages for susceptibility model III. To save space, the outcome tables for model II have, therefore, been omitted.

Susceptibility III model: Tables 9-14 show the results for susceptibility model III for the various threshold functions $\tau_{k}$, for $k=1, \ldots, 7$.

Note that the changes in probabilities when going from $\tau_{1}$ to $\tau_{7}$ are according to the Monotonicity Property (10), and this is thus as expected. What is important is to look for cases where the coverage, computed using the Bayesian network, becomes very low, even though the antibiotics are known to be effective according to Table 2, or very high, even though the antibiotics are known

Table 6 Predicting optimal treatment for 153 patients diagnosed with VAP using the (SI, $k=5$ ) model, distinguished by different number of colonising pathogens (Nr.). Mean coverage is specified for a selection of antibiotics.


Table 7 Predicting optimal treatment for 153 patients diagnosed with VAP using the ( $\mathrm{SI}, k=6$ ) model, distinguished by different number of colonising pathogens (Nr.). Mean coverage is specified for a selection of antibiotics.


Table 8 Predicting optimal treatment for 153 patients diagnosed with VAP using the ( $\mathrm{SI}, k=7$ ) (noisy-AND gate) model, distinguished by different number of colonising pathogens (Nr.). Mean coverage is specified for a selection of antibiotics.


Table 9 Predicting optimal treatment for 153 patients diagnosed with VAP using the (SIII, $k=1$ ) (noisy-OR gate) model, distinguished by different number of colonising pathogens (Nr.). Mean coverage is specified for a selection of antibiotics.


Table 10 Predicting optimal treatment for 153 patients diagnosed with VAP using the (SIII, $k=2$ ) model, distinguished by different number of colonising pathogens (Nr.). Mean coverage is specified for a selection of antibiotics.


Table 10 (Continued)


Table 11 Predicting optimal treatment for 153 patients diagnosed with VAP using the (SIII, $k=3$ ) model, distinguished by different number of colonising pathogens (Nr.). Mean coverage is specified for a selection of antibiotics.


Table 12 Predicting optimal treatment for 153 patients diagnosed with VAP using the (SIII, $k=4$ ) model, distinguished by different number of colonising pathogens (Nr.). Mean coverage is specified for a selection of antibiotics.


Table 13 Predicting optimal treatment for 153 patients diagnosed with VAP using the (SIII, $k=5$ ) model, distinguished by different number of colonising pathogens (Nr.). Mean coverage is specified for a selection of antibiotics.


Table 14 Predicting optimal treatment for 153 patients diagnosed with VAP using the (SIII, $k=6,7$ ) model, distinguished by different number of colonising pathogens (Nr.). Mean coverage is specified for a selection of antibiotics.


to be ineffective. In the next section, the clinical implications of these results are discussed in detail.

## 6. Conclusions and discussion

In this paper, we have shown that by reconsidering the modelling of interactions between the random variables in a Bayesian network using the theory of causal independence, it is possible to refine its performance. We used a Bayesian network for the diagnosis and treatment of ventilator-associated pneumonia as an example. The advantage of the theory of causal independence is that it not only facilitates the assessment of probability tables by allowing the specification of a table in terms of a linear number of parameters of the form $\operatorname{Pr}\left(I_{j} \mid C_{j}\right)$, but it also allows taking into account domain characteristics in choosing the right Boolean function [3]. This was clearly shown for our Bayesian network concerning VAP, where motivation was derived from the domain of infectious diseases, indicating that only specific noisy-threshold models might be appropriate for the modelling of the interaction between pathogens and antimicrobial treatment with respect to susceptibility.

As the Boolean threshold functions are examples of symmetric Boolean functions, the exploitation of this form of symmetry may suggest that the effects of presence of particular pathogens are judged equally. However, this is not the case, as the probability of being colonised by a particular pathogen together with the susceptibility of a pathogen to specific antibiotics determine to what extent a pathogen-treatment combination contributes to the overall effect. For example, the presence of $P$. aeruginosa has more effect on the type of antibiotics to be prescribed than the presence of $S$. pneumoniae, as it is in general more likely that
patients are colonised by $P$. aeruginosa than by S. pneumoniae.

When using the susceptibility I model (i.e., prescribing antimicrobial therapy results in coverage of pathogens colonising as well as pathogens not colonising a patient), the model always gives high coverage. It is counter-intuitive that even threshold functions with high $k$ give high coverage, as patients are usually colonised with at most two pathogens. In addition, this probabilistic model does not support obtaining insight into the actual effects of the antibiotics on the pathogens that cause the infection. This is the information a clinician would like to obtain from a probabilistic model.

The results for susceptibility II model (i.e., when there is no colonisation no medication should be prescribed), however, indicate that when a patient is colonised with, for example, 2 pathogens, the model advises to prescribe no antimicrobial therapy. This is due to dominance of the remaining five pathogens by which the patient has not been colonised. This is clearly undesirable for a lifethreatening disease like VAP. This model might, therefore, be used for patients with a low likelihood of having VAP.

Incorporation of susceptibility III model (i.e., when there is colonisation, cover it with antibiotics) yields a Bayesian network that performs best at prescribing antimicrobial therapy for monobacterial as well polymicrobial VAP. It appeared that a threshold function $\tau_{k}$ with $k=1$ and $k=2$ yielded the best results, according to the reference standard. Using a model that is able to combine and compare covering results of both $k=1$ and 2 would be worth considering. As can be learnt from these tables, coverage probabilities for $k=1$ are high for monobacterial as well as for polymicrobial VAP, whereas for $k=2$ coverage probabilities for monobacterial infections were relatively low, compared to those for polymi-

crobial VAP episodes. Therefore, a combination model should be used as follows:

IF results for $k=2$ indicate relatively
high coverage probabilities
for polymicrobial VAP
THEN use $k=2$ to calculate treatment for polymicrobial VAP
ELSE use $k=1$ to calculate treatment for monobacterial VAP
FI
Clearly, susceptibility model III is able to distinguish between monobacterial and polymicrobial VAP, which is important for the selection of appropriate therapy. In addition, early-onset VAP requires other, often more narrow-spectrum antibiotics compared to late-onset VAP. These two findings that are important to limit the creation of antibiotic resistance have certain implications for the construction of a clinical Bayesian network model for assisting in the prescription of antimicrobial therapy.

Naturally, susceptibility model II has other implications to the selection of antimicrobial therapy, as compared to susceptibility model I, as it accounts for the pathogens that are absent. Therefore, the specificity of the model predictions for selecting antimicrobial treatment will be high for model II, whereas for model I the sensitivity will be high.

In general, these results also provide evidence that the noisy-OR and noisy-AND, which are very popular in Bayesian network modelling, might not always be the best functions to model interactions among random variables.

Although in this paper, we have studied the use of susceptibility models in combination with the use of Boolean threshold functions for treatment selection in VAP, it is likely that the techniques introduced in this paper are also relevant to other biomedical fields. In particular in biomedical areas where it is relevant to consider the number of causes of disease in selecting treatment of the disease, the methods can be of use.

To conclude, it was shown that the noisy-threshold model is useful from a practical point of view by using it as a basis for the refinement of an existing real-world Bayesian network for the management of critically ill patients.

## Acknowledgements

This research, undertaken in the TimeBayes project, was funded by the Netherlands Organisation for Scientific Research (NWO) under the ToKeN programme (grant number 634.000.026). We would like to thank Rasa Jurgelėnaitė for her help with the theoretical work concerning noisy-threshold models.
