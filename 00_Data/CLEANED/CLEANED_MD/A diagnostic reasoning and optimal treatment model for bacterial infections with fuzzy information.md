![img-0.jpeg](img-0.jpeg)

Since January 2020 Elsevier has created a COVID-19 resource centre with free information in English and Mandarin on the novel coronavirus COVID19. The COVID-19 resource centre is hosted on Elsevier Connect, the company's public news and information website.

Elsevier hereby grants permission to make all its COVID-19-related research that is available on the COVID-19 resource centre - including this research content - immediately available in PubMed Central and other publicly funded repositories, such as the WHO COVID database with rights for unrestricted research re-use and analyses in any form or by any means with acknowledgement of the original source. These permissions are granted for free by Elsevier for as long as the COVID-19 resource centre remains active.

# A diagnostic reasoning and optimal treatment model for bacterial infections with fuzzy information 

Han-Ying Kao ${ }^{\mathrm{a}, *}$, Han-Lin $\mathrm{Li}^{\mathrm{b}}$<br>${ }^{a}$ Department of Marketing and Distribution Management, Hsuan Chuang University, 48 Hsuan Chuang Road, Hsinchu 300, Taiwan<br>${ }^{\text {b }}$ Institute of Information Management, National Chiao Tung University, 1001 Ta Hsueh Road, Hsinchu 300, Taiwan

Received in revised form 1 August 2004; accepted 1 August 2004

KEYWORDS
Influence diagrams;
Bayesian networks;
Diagnostic reasoning;
Optimal treatment;
Fuzzy parameters;
Constraints

## 1. Introduction

Two generic reasoning tasks are vital in medical reasoning: diagnostic reasoning and treatment planning. Diagnostic reasoning is the process of reconstructing the past facts from the observed

[^0]Summary This study proposes an optimization model for optimal treatment of bacterial infections. Using an influence diagram as the knowledge and decision model, we can conduct two kinds of reasoning simultaneously: diagnostic reasoning and treatment planning. The input information of the reasoning system are conditional probability distributions of the network model, the costs of the candidate antibiotic treatments, the expected effects of the treatments, and extra constraints regarding belief propagation. Since the prevalence of the pathogens and infections are determined by many site-by-site factors, which are not compliant with conventional approaches for approximate reasoning, we introduce fuzzy information. The output results of the reasoning model are the likelihood of a bacterial infection, the most likely pathogen(s), the suggestion of optimal treatment, the gain of life expectancy for the patient related to the optimal treatment, the probability of coverage associated with the antibiotic treatment, and the cost-effect analysis of the treatment prescribed.
(c) 2004 Elsevier Ireland Ltd. All rights reserved.
evidence. Treatment planning is reasoning about the effects of actions treated on patients [1]. Usually, the practice of medicine requires both kinds of reasoning to work simultaneously. However, few current reasoning methods can conduct the two reasoning tasks successfully at one time. Besides, the reasoning systems become more complex when considering the complexity of human bodies and its relationships with the environmental factors.


[^0]:    * Corresponding author. Tel.: +886 3 5302255/5227;
    fax: +886 35391236.
    E-mail address: teresak.hk@yahoo.com.tw (H.-Y. Kao).

In some clinical cases, various factors may raise the difficulty in reasoning, such as the demographic variances of nosography, the incomplete knowledge of the diseases (e.g. severe acute respiratory syndrome (SARS) in the early 2003), some specific restrictions on estimating relevant parameters of the diseases, etc. In these cases, the clinicians' experiences and judgments may be useful to diagnosis and prescription. Therefore, the site-by-site factors and clinicians' knowledge, which may be expressed as extra constraints in the reasoning systems, need to be integrated into the medical decision support systems. At the same time, owing to the difficulties to estimate the causal effects between possible pathogens and the diseases, the parameters of the knowledge base can be expressed as fuzzy numbers.

Considering the clinical issues mentioned above, the authors are motivated to develop a reasoning model with the following features.
(i) Complete diagnostic reasoning as well as treatment planning.
(ii) Combine the formal knowledge base as well as decision-makers' judgments that present as extra constraints.
(iii) Work compatibly with the circumstance where fuzzy information is involved.

In the following section, the background of this research and the proposed approach will be interpreted.

## 2. Background

In medical informatics and other domains, Bayesian networks [1-10] and influence diagrams [6,8,11-13] are widely used knowledge representation and decision models under uncertainty. However, there are two limitations of utilizing the above approaches for solving medical reasoning problems:
(i) All associated probabilities are assumed to be crisp.
(ii) Difficult to consider the constraints for the relationships among the nodes in Bayesian networks or influence diagrams.
(iii) Treatment planning and diagnostic problems are not considered in one paradigm.

The limitations mentioned above restrict the practical usefulness of medical reasoning on Bayesian networks and influence diagrams in the following facts. First, the conditional probabilities between a node and its parent or children nodes could be fuzzy instead of a crisp numbers,
due to the difficulties of learning accurately the cause-effect relationships among the nodes [14]. Second, as a common fact, the experts may have some professional speculations in the form of constraints when reasoning from a Bayesian network or an influence diagram. These constraints could be boundary, dependency, or disjunctive conditions. Third, the investigators of influence diagrams used to maximize the utility functions by node removal processes [11-13] and ignore diagnostic reasoning tasks. Oppositely, Bayesian networks have been used widely in probabilistic reasoning but lacked the capability to suggest the optimal decision $[2,3,8-10]$.

This study proposes an optimization model to make diagnostic reasoning and treatment planning for bacterial infections, where the cause-effect relationships are expressed with an influence diagram and fuzzy data. The input information of the reasoning system are conditional probability distributions of the network model, the costs of the candidate antibiotic treatments, the expected effects of the treatments, and extra constraints regarding belief propagation. Since the prevalence of the pathogens and infections are determined by many site-by-site factors, the decisions involve uncertainty not compliant with conventional approaches. So, we allow the decisions to be made under fuzzy contexts, at which some of the parameters could be fuzzy parameters [14], and some constraints regarding diagnosis are introduced. When a patient is received, this reasoning system can, based on the present symptoms or bacteriological tests, help the clinician make precise diagnosis at the first decision point, and also supply the suggestions of optimal treatment for the infection. The outputs of the reasoning model are the likelihood of a bacterial infection, the most likely pathogen(s), the suggestion for the optimal treatment, the gain of life expectancy of the patient related to the optimal treatment, the probability of coverage associated with the antibiotic treatment, and the cost-effect analysis of the treatment prescribed. The input-output diagram is depicted in Fig. 1.

In the remaining of this article, the design considerations are introduced in Section 3. An influence diagram is used to represent the relationships among the variables relevant to the infections. In Section 4, this study describes the reasoning model and system thoroughly. In Section 5, we implement the diagnostic reasoning and planning problem as an optimization model. The illustration and solutions of this numerical example is given as well. In Section 6, some comments and lessons are given. Finally, we discuss the future extensions in Section 7.

![img-1.jpeg](img-1.jpeg)

Fig. 1. The input-output diagram of the optimization model in this study.

## 3. Design considerations

In this section, the authors will introduce an example of urinary tract infection (UTI), the problem and design goal, and handling the fuzzy information sequentially.

### 3.1. An example of urinary tract infection (UTI)

Consider one example of urinary tract infections simplified from Leibovici et al. [5]. As depicted in Fig. 2, this example uses an influence diagram as
the knowledge and decision model where the conditional probability distributions for the relevant random and decision variables are calculated. For the sake of simplicity and without loss of generality, all random nodes are assumed binary. The conditional probability distributions of the variables are given in Tables 1-3. The nodes and their states in Fig. 2 are described as follows.

- Pathogen $\left(\right.$ Patho $\left._{i}\right)$ : A microorganism capable of causing urinary tract infection. For the convenience of illustration, only 3 of 12 pathogens are presented: Patho (Klebsiella pneumoniae), Patho $_{2}$ (Pseudomonas aeruginosa), Patho $_{3}$ (Es-
![img-2.jpeg](img-2.jpeg)

Tr: Antibiotic treatment
Cost: Costs of antibiotic treatments
Resist: Resistance
Patho $_{1}$ : Klebsiella pneumoniae
Patho $_{2}$ : Pseudomonas aeruginosa
Patho $_{3}$ : Escherichia Coli
Test $_{1}$ : Grow of microorganisms in the blood
Test $_{2}$ : Grow of microorganisms in the urine
Test $_{3}$ : Nitrite test

Gain: Gross gain in life expectancy
Underlying: Underlying disorder of patients
UTI: Urinary Tract Infection
Sign $_{1}$ : Suprapubic pain
Sign $_{2}$ : Frequent micturition
Sign $_{3}$ : Flank pain
Sign $_{4}$ : Urinary symptoms
Sign $_{5}$ : Serum albumin
Sign $_{6}$ : Fever

Fig. 2. A revised influence diagram for urinary tract infection [5]. In the latter part of this figure, the authors put pairs of (node.name: description) for each node in the network to explain what the nodes represent.

cherichia coli). The states of this kind of nodes are severity: severe $\left(\right.$ Patho $\left._{i}=1\right)$ and not severe (Patho ${ }_{i}=0$ ).

- Urinary tract infection (UTI): The states of this node are infected (UTI=1) and not infected (UTI = 0).
- Signs and symptoms of urinary tract infection (Sign ${ }_{i}$ ): The manifestations that might cause from UTI. There are six possible signs presented in Fig. 2: Sign ${ }_{1}$ (suprapubic pain), Sign ${ }_{2}$ (frequent micturition), Sign ${ }_{3}$ (flank pain), Sign ${ }_{4}$ (urinary symptoms), Signs (serum albumin) and Sign ${ }_{6}$ (fever). The states of these nodes are present $\left(\operatorname{Sign}_{i}=1\right)$ and absent $\left(\operatorname{Sign}_{i}=0\right)$.
- Bacteriological tests (Test ${ }_{i}$ ): Test ${ }_{1}$ (growth of microorganisms in the blood), Test ${ }_{2}$ (growth of microorganisms in the urine) and Test ${ }_{3}$ (nitrite test). The states of these nodes are positive (Test ${ }_{i}=1$ ) and negative (Test ${ }_{i}=0$ ).
- Coverage of UTI (Coverage): The percent of pathogens of UTI susceptible to an antibiotic drug. The states of this node are covered (Coverage $=1$ ) and not covered (Coverage $=0$ ).
- Resistance to antibiotic drugs (Resist): The states of this node are resistant (Resist $=1$ ) and not resistant (Resist $=0$ ).
- Antibiotic treatment (Tr): The treatment will be appropriate if it matches the in-vitro susceptibility of the pathogens. For simplicity of demonstration, we consider 5 of 26 antibiotic drugs and one additional state for no treatment. Thus, we have six alternatives, that is $\operatorname{Tr}=\left\{\operatorname{tr}_{0}, \operatorname{tr}_{1}, \operatorname{tr}_{2}, \operatorname{tr}_{3}, \operatorname{tr}_{4}\right.$, $\left.\operatorname{tr}_{5}\right\}$, where $\operatorname{tr}_{0}$ stands for no treatment and $\operatorname{tr}_{i}=0$ or 1 . When $\operatorname{tr}_{i}=1$, it means that $\operatorname{tr}_{i}$ is prescribed; oppositely, $\operatorname{tr}_{i}=0$ means that $\operatorname{tr}_{i}$ is not prescribed. For the efficiency of computation, we allow only one antibiotic drug at one time, which let it possible to formulate this decision problem as a mixed $0-1$ integer program. If more than one drug is mixed in the therapy, the mixed treatment will be regarded as another treatment. Notably, this node is a decision node that has effects on the coverage from urinary tract infection.
- Underlying (Underlying): The underlying disorder of the patient, which will be represented by an equivalent base years of the remaining life in this illustrative example.
- Cost $\left(\operatorname{Cost}\left(\operatorname{tr}_{i}\right)\right)$ : A utility node associated with antibiotic treatments.
- Gain (Gain): The gain in life expectancy obtained by prescribing an antibiotic drug, which is a function of the coverage (Coverage) and the underlying disorder of the patient (Underlying).

Each variable above is characterized by crisp or fuzzy probabilities given the state of its parents.

Table 1 The probability distributions of the pathogens and UTI

$$
\begin{aligned}
& P\left(+\text { patho }_{1}\right)=0.1 \\
& P\left(+\text { patho }_{2}\right)=0.09 \\
& P\left(+\text { patho }_{3}\right)=0.09 \\
& P\left(+\text { uti } \mid+\text { patho }_{1},+\text { patho }_{2},+\text { patho }_{3}\right)=\bar{x}_{1} \\
& P\left(+\text { uti } \mid+\text { patho }_{1},-\text { patho }_{2},+\text { patho }_{3}\right)=\bar{x}_{2} \\
& P\left(+\text { uti } \mid+\text { patho }_{1},+\text { patho }_{2},-\text { patho }_{3}\right)=\bar{x}_{3} \\
& P\left(+\text { uti } \mid+\text { patho }_{1},-\text { patho }_{2},-\text { patho }_{3}\right)=\bar{x}_{4} \\
& P\left(+\text { uti } \mid-\text { patho }_{1},+\text { patho }_{2},+\text { patho }_{3}\right)=\bar{x}_{5} \\
& P\left(+\text { uti } \mid-\text { patho }_{1},-\text { patho }_{2},+\text { patho }_{3}\right)=\bar{x}_{6} \\
& P\left(+\text { uti } \mid-\text { patho }_{1},+\text { patho }_{2},-\text { patho }_{3}\right)=\bar{x}_{7} \\
& P\left(+\text { uti } \mid-\text { patho }_{1},-\text { patho }_{2},-\text { patho }_{3}\right)=\bar{x}_{8}
\end{aligned}
$$

For instance, UTI $\in\{0,1\}$ represents the dichotomy between having urinary tract infection and not having one. Also, +uti stands for the assertion UTI $=1$ or "urinary tract infection is present", and -uti stands for the negation of +uti, i.e., UTI $=0$.

Denote $Y$ the random node set of the influence diagram depicted in Fig. 2. The probability distribution of the random nodes given treatment $\mathrm{tr}_{i}$ can be expressed as (3.1):

$$
\begin{aligned}
P(y)= & \prod_{i=1}^{3} P\left(\text { patho }_{i}\right) \times P\left(\text { uti| patho }_{1}, \text { patho }_{2}, \text { patho }_{3}\right) \\
& \times \prod_{j=1}^{6} P\left(\text { sign }_{j} \mid \text { uti }\right) \times P(\text { resist }) \\
& \times \prod_{k=1}^{3} P\left(\text { test }_{k} \mid \text { patho }_{1}, \text { patho }_{2}, \text { patho }_{3}\right) \\
& \times P\left(\text { coverage } \mid \text { patho }_{1}, \text { patho }_{2}, \text { patho }_{3}\right. \\
& \text { resist, } \left.\operatorname{tr}_{i}\right)
\end{aligned}
$$

### 3.2. Problem and design goals

Consider the conditional probabilities in Table 1 and Table 2, and the evidence that a patient has suffered from frequent micturition (Sign ${ }_{2}=1$ ), flank pain $\left(\operatorname{Sign}_{3}=1\right)$ and urinary symptoms $\left(\operatorname{Sign}_{4}=1\right)$, but has not fallen into a suprapubic pain $\left(\operatorname{Sign}_{1}=0\right)$,

Table 2 The conditional probabilities of signs $\left(\operatorname{Sign}_{i}\right)$


serum albumin $\left(\operatorname{Sign}_{5}=0\right)$ or fever $\left(\operatorname{Sign}_{6}=0\right)$. Denote the evidence set $\mathrm{E}=\{e\}=\left\{\operatorname{Sign}_{1}=0, \operatorname{Sign}_{2}=1\right.$, $\left.\operatorname{Sign}_{3}=1, \operatorname{Sign}_{4}=1, \operatorname{Sign}_{5}=0, \operatorname{Sign}_{6}=0\right\}$. We need to solve the following two problems.
(i) Compute the belief distribution of Patho ${ }_{1}$, Patho $_{2}$, Patho $_{3}$ and UTI.
(ii) Make the suggestion of the optimal treatment based on the information given in Table 3, assuming the patient with resistance to the antibiotic treatments (Resist $=1$ ).

At the first decision point, the clinician tends to make the diagnosis without biological test
![img-3.jpeg](img-3.jpeg)

Fig. 3. The membership function $\mu_{\bar{x}_{1}}\left(x_{1}\right)$.
not a crisp but a fuzzy number, say $\bar{x}_{1}$, that is $P\left(+u t i \mid+\right.$ patho $_{1}$, + patho $_{2}$, + patho $\left._{3}\right)=\bar{x}_{1}$, and is described with a membership function $\mu_{\bar{x}_{1}}\left(x_{1}\right)$ represented as follows (see Fig. 3):

$$
\mu_{\bar{x}_{1}}\left(x_{1}\right)= \begin{cases}5\left(x_{1}-0.6\right)-5\left(\left|x_{1}-0.8\right|+x_{1}-0.8\right), & 0.6 \leq x_{1} \leq 1.0 \\ 0, & \text { elsewhere. }\end{cases}
$$

results; that is, the task is reasoning on the subgraph omitting the nodes Test $_{i}$ and simplified as to compute $P(y \mid e)$, where $e$ stands for an instance of the evidence set $E$, and $Y$ shrinks as $\left\{\right.$ Patho $_{1}$, Patho $_{2}$, Patho $_{3}$, UTI, Coverage $\}$. This is reasonable because the tests will have no effect on the diagnostic results if they do not provide extra information. If the treatment prescribed at the first time does not work, then some biological tests would be further required. Besides, this model would like to provide the suggestion for the optimal treatment that maximizes the gain of life expectancy and minimizes the total costs.

### 3.3. Handling fuzzy information

Notice that some of the parameters in Table 1 are not crisp but fuzzy numbers. Freeling [14] claimed fuzzy probability as an extension of probability theory, which is more promising than possibility and probability theory as the uncertainty mearsure. For instance, $P\left(+u t i \mid+\right.$ patho $_{1}$, + patho $\left._{2},+_{p a t h o_{3}}\right)$ is
where "|*|" is the absolute value of a term *.
The above expression means that the support of $\bar{x}_{1}$ is between 0.6 and 1.0. For example, if $x_{1}=0.7$, then $\mu_{\bar{x}_{1}}\left(x_{1}\right)=0.5$. If $x_{1}=0.8$ then $\mu_{\bar{x}_{1}}\left(x_{1}\right)=1.0$, which implies that $x_{1}=0.8$ is the most confident value. If $x_{1} \leq 0.6$ or $x_{1} \geq 1.0$ then $\mu_{\bar{x}_{1}}\left(x_{1}\right)=0$, which is least possible to happen.

For the fuzzy parameters in Table 1, we will formulate the membership functions of $\bar{x}_{i}, i=1,2, \ldots$, 8.

Consider a membership function $\mu_{\bar{x}}(x)$ of a fuzzy parameter $\bar{x}$ as portrayed in Fig. 4. This piecewise membership function is usually expressed as

$$
\mu_{\bar{x}}(x)= \begin{cases}s_{1}\left(x-a_{1}\right), & a_{1}<x \leq a_{2} \\ \mu_{\bar{x}}\left(a_{2}\right)+s_{2}\left(x-a_{2}\right), & a_{2}<x \leq a_{3} \\ \mu_{\bar{x}}\left(a_{3}\right)+s_{3}\left(x-a_{3}\right), & a_{3}<x \leq a_{4} \\ \mu_{\bar{x}}\left(a_{4}\right)+s_{4}\left(x-a_{4}\right), & a_{4}<x \leq a_{5} \\ 0, & \text { elsewhere }\end{cases}
$$

where $a_{j}, j=1, \ldots, 5$ represents the break points; $s_{i}$, $i=1, \ldots, 4$ represents the slopes of the segments. The above expression is not convenient for compu-

Table 3 The conditional probabilities of coverage given Resist $=1$


[^0]
[^0]:    ${ }^{a}$ The costs of the $\operatorname{tr}_{0}, \operatorname{tr}_{1}, \operatorname{tr}_{2}, \operatorname{tr}_{3}, \operatorname{tr}_{4}, \operatorname{tr}_{5}$ are 5000 (the receiving and process costs), $\$ 20,000,25,000,30,000,32,000$ and 50,000 , respectively.
    ${ }^{\text {b }}$ No treatment.

Table 4 The membership functions of fuzzy probabilities


tation. Here, we adopt an efficient way to express a piecewise linear function. Consider the following proposition.

Proposition 1. Let $\mu_{\hat{x}}(x)$ be the membership function of a fuzzy variable $\hat{x}$, as depicted in Fig. 4, where $a_{j}, j=1,2, \ldots, m$ are the break points of $\mu_{\hat{x}}(x)$, and $s_{j}, j=1,2, \ldots, n$ are the slopes of line segments between $a_{j}$ and $a_{j+1}, \mu_{\hat{x}}(x)$ can be expressed as the sum of absolute terms $[15,16]$ :

$$
\begin{aligned}
\mu_{\hat{x}}(x)= & \mu_{\hat{x}}\left(a_{1}\right)+s_{1}\left(x-a_{1}\right) \\
& +\sum_{j=2}^{m} \frac{s_{j}-s_{j-1}}{2}\left(\left|x-a_{j}\right|+x-a_{j}\right)
\end{aligned}
$$

Now we are ready to express the membership functions of the fuzzy parameters $\mu_{\hat{x}_{i}}\left(x_{i}\right)$ in Table 4. The readers may find that all the eight fuzzy parameters are triangular fuzzy numbers. However, the membership functions in Table 4 involve absolute terms, which is not convenient for computation. Since $\mu_{\hat{x}}(x)$ in (3.4) is a function to be maximized, we used the following proposition to linearize the membership functions.

Proposition 2. To maximize a membership function $\mu_{\hat{x}}(x)$ in (3.4) is equivalent to solve the following linear program $[15,16]:(3.5)$
![img-4.jpeg](img-4.jpeg)

Fig. 4. A membership function of fuzzy probability $\hat{x}$.
$\left.\operatorname{Max} z=s_{1}\left(x-a_{1}\right)+2 \sum_{j=2}^{m} \frac{s_{j}-s_{j-1}}{2}\left(x-a_{j}+\sum_{k=1}^{j} d_{k}\right)\right]$
subject to
$x+d_{1} \geq a_{2}$,
$x+d_{1}+d_{2} \geq a_{3}$,
$\vdots$
$x+d_{1}+d_{2}+\cdots+d_{m-1} \geq a_{m}$,
$0 \leq d_{1} \leq a_{2}$,
$0 \leq d_{k-1} \leq a_{k}-a_{k-1}, \quad$ for $k=2,3, \ldots, m$,
$x \in F$ (feasible set),
where $d_{k-1}$ stands for the lower bound of distance between $a_{k-1}$ and $a_{k}$. For the detailed proof of Proposition 2, please refer to $[15,16]$.
Now we are ready to formulate the optimization model for diagnosis and treatment planning.

## 4. System description

Here we formulate the diagnostic reasoning and treatment planning problems as an optimization model. The objectives of this model are described as follows.

### 4.1. System objectives

The objectives of this model are described below.
(i) To maximize the sum of all fuzzy membership functions. That is, we will make the suggestions of optimal treatment under the maximal confidence of the fuzzy information [17].
(ii) To maximize the gain in life expectancy.
(iii) To minimize the total costs of the treatments.

In this problem, the clinician has six candidate treatments to choose, where no treatment is included. We represent each antibiotic treatment as a binary variable $\operatorname{tr}_{i}$ (including $\operatorname{tr}_{0}$ standing for no treatment) and the cost as $\operatorname{Cost}\left(\operatorname{tr}_{i}\right)$. The total cost

is $\sum_{i=0}^{5} \operatorname{Cost}\left(\operatorname{tr}_{i}\right)$. The objective functions can be expressed as follows:
$\operatorname{Max} z_{1}=\sum_{i=1}^{8} \mu_{\bar{x}_{i}}\left(x_{i}\right)$
Max $z_{2}=E($ Gain(Coverage, Underlying $))$
$\operatorname{Min} z_{3}=\sum_{i=0}^{5} \operatorname{Cost}\left(\operatorname{tr}_{i}\right)$
where " $E\left({ }^{*}\right)$ " stands for the expectation of a term *.

In (4.2), we express the expected gain in life expectancy as a function of Coverage and Underlying. We assume that the underlying disorder and health status can be converted to an equivalent base year, in this case, 35 years, and the gain is a multiple of the base year. This study assumes that, in this clinical case, the patient has the ideal 35 years gain of life expectancy if the probability to recover from UTI is 1 . Since the literature [5] shows that oneyear gained in life can be regarded equivalent to $dollars $ 55,000, we re-write (4.2) as (4.4) for unit standardization:
$z_{2}^{\prime}=55,000 \times E($ Gain(Coverage $)) \div 35$
Setting that only one treatment can be chosen at one decision point, we can formulate the total cost function as in (4.3). Notably, the probability of coverage is determined by the resistance of antibiotic treatment (given Resist $=1$ ), the pathogens (Patho ${ }_{j}$ ), and the treatment $\left(\operatorname{tr}_{i}\right)$. The reader may refer to their relationships in Table 3. Defining $\mathrm{tr}_{i}$ as a $0-1$ variable, the expectation of Coverage, $E$ (Coverage) can be computed as

$$
\begin{aligned}
& E(\text { Coverage } \mid \text { Resist }=1) \\
& =\alpha \sum_{i} \sum_{\text {patho }_{1}} \sum_{\text {patho }_{2}} \sum_{\text {patho }_{3}} \operatorname{tr}_{i} \\
& \times P\left(\text { coverage } \mid \text { patho }_{1}, \text { patho }_{2}\right. \\
& \text { patho }_{3}, \text { resist }=1, \operatorname{tr}_{i}
\end{aligned}
$$

where $\alpha$ is the normalizing constant, which will be explained in next subsection.

In this optimization program, two categories of constraints must to be satisfied: (1) the constraints for the probability theory, and (2) the extra constraints regarding belief propagation. This optimization model can be implemented with various exact propagation methods. This study does not intend to discuss the details of reasoning algorithms but focus on how to formulate this problem as an
optimization model. The interested readers may refer to the literatures $[2,3,7-10]$.

### 4.2. Basic constraints

Now we formulate the first category of constraints as

$$
\begin{aligned}
& \sum_{y} P(y) \\
& =\alpha \sum_{\text {patho }_{1}} \sum_{\text {patho }_{2}} \sum_{\text {patho }_{3}} \sum_{\text {uti }} \sum_{\text {coverage }} \\
& \times\left[\prod_{i=1}^{3} P\left(\text { patho }_{i}\right) \times P\left(\text { uti } \mid \text { patho }_{1}, \text { patho }_{2}\right.\right. \\
& \text { patho }_{3}\right) \times P\left(\text { sign }_{1}=0 \mid \text { uti } \mid \times P\left(\text { sign }_{2}=1 \mid \text { uti }\right)\right. \\
& \times P\left(\text { sign }_{3}=1 \mid \text { uti } \mid \times P\left(\text { sign }_{4}=1 \mid \text { uti }\right)\right. \\
& \times P\left(\text { sign }_{5}=0 \mid \text { uti } \mid \times P\left(\text { sign }_{6}=0 \mid \text { uti }\right)\right. \\
& \times \sum_{i=0}^{5} P\left(\text { coverage } \mid \text { patho }_{1}, \text { patho }_{2}, \text { patho }_{3}\right. \\
& \left.\text { resist }=1, \operatorname{tr}_{i}\right]=1 \\
& \sum_{i=0}^{5} \operatorname{tr}_{i}=1 . \quad \operatorname{tr}_{i}=1 \text { or } 0
\end{aligned}
$$

where $\alpha$ is the normalizing constant which ensures that the sum of the probabilities of every instance of $y$ is 1 . The constraint in (4.7) regulates the clinician to prescribe only one treatment in the first decision point.

### 4.3. Extra constraints

At the same time, in addition to a given formal knowledge base, the clinicians may have some professional speculations about the features of some nodes and the relationships among them, in some specific diagnostic context. These features and relationships can be identified as the following types of constraints.
(i) Boundary constraints

Some posterior beliefs may have upper or lower bounds. For instance, a clinician may speculate that the posterior probability of Patho ${ }_{3}$ should be higher than 0.3 but lower than 0.5 , which can be expressed as
$0.3 \leq P\left(+\right.$ patho $\left._{3} \mid e\right) \leq 0.5$

(ii) Dependency constraints

The beliefs of some nodes in the belief network may exist mutually dependent relationships. For example, a clinician may presume that the posterior probability of Patho ${ }_{1}$ should be some multiple of Patho ${ }_{3}$. Such a relationship is expressed as
$P\left(+\right.$ patho $\left._{1} \mid e\right) \leq 0.5 P\left(+\right.$ patho $\left._{3} \mid e\right)$
(iii) Disjunctive constraints

Sometimes the disjunctive condition between the nodes may exist. For example, a doctor may estimate that either $P\left(+p a t h o_{2} \mid e\right)$ or $P\left(+p a t h o_{1} \mid e\right)$ is equal to or less than 0.4 , which is expressed as
either $P\left(+\right.$ patho $\left._{2} \mid e\right)$

$$
\leq 0.4 \text { or } P\left(+\operatorname{patho}_{1} \mid e\right) \leq 0.4
$$

### 4.4. The model

Combining constraints (4.8) and (4.10) into this reasoning system, this optimization program becomes

$$
\left.\begin{array}{l}
\text { Max } z_{1} \\
\text { Max } z_{2}^{\prime} \\
\text { Min } z_{3}
\end{array}\right\}
$$

s.t. $(4.6)-(4.8),(4.10)$

Since the disjunctive constraint (4.10) is a nonlinear constraint, we will linearize it by some $0-1$ variables as the following.

$$
\left.\begin{array}{l}
M\left(\theta_{1}-1\right) \leq P\left(+p a t h o_{2} \mid e\right)-0.4 \leq M \theta_{1}+M\left(1-\theta_{2}\right) \\
M\left(\theta_{2}-1\right) \leq P\left(+p a t h o_{1} \mid e\right)-0.4 \leq M \theta_{2}+M\left(1-\theta_{1}\right) \\
\varepsilon \leq \theta_{2}+\theta_{1} \leq 1
\end{array}\right\}
$$

where $\theta_{1}$ and $\theta_{2}$ are $0-1$ variables, $M$ is a relatively large number, and $\varepsilon$ is a relatively small positive number.

We can check the four possible combinations of $\theta_{1}$ and $\theta_{2}$. (1) $\theta_{1}=1, \theta_{2}=1$ : (4.12) turns into $0 \leq P\left(+p a t h o_{2} \mid e\right)-0.4 \leq M$ and $0 \leq P\left(+p a t h o_{1} \mid e\right)-0.4 \leq M$, which are inactive constraint; (2) $\theta_{1}=0, \quad \theta_{2}=1$ : (4.12) turns into $-M \leq P\left(+p a t h o_{2} \mid e\right)-0.4 \leq 0$ and $0 \leq P\left(+p a t h o_{1} \mid e\right)-0.4 \leq 2 M$, which means that when $P\left(+p a t h o_{1} \mid e\right) \geq 0.4, \quad P\left(+p a t h o_{2} \mid e\right)$ must be less than or equal to 0.4 ; (3) $\theta_{1}=1, \theta_{2}=0$ : (4.12) works as $0 \leq P\left(+p a t h o_{2} \mid e\right)-0.4 \leq 2 M$ and $-M \leq P\left(+p a t h o_{1} \mid e\right)-0.4 \leq 0$, which implies that when $P\left(+p a t h o_{2} \mid e\right) \geq 0.4, \quad P\left(+p a t h o_{1} \mid e\right)$ must be less than or equal to 0.2 ; (4) $\theta_{1}=0, \theta_{2}=0$ : (4.12) becomes $-M \leq P\left(+p a t h o_{2} \mid e\right)-0.4 \leq M$ and
$-M \leq P\left(+p a t h o_{1} \mid e\right)-0.4 \leq M$, which are inactive constraints. The third inequalities in (4.12) exclude the combinations when $\theta_{1}=1, \theta_{2}=0$ and $\theta_{1}=0$, $\theta_{2}=0$. To summarize, (4.12) implies that either $P\left(+p a t h o_{2} \mid e\right) \leq 0.4$ or $P\left(+p a t h o_{1} \mid e\right) \leq 0.4$ must be satisfied.

## 5. Status report

The model formulated in the previous section is a multiobjective program, so we adopt the fuzzy approach $[18,19]$ to solve it. Following the steps described below, the model is solved.

Step 1: Get the ideal solutions of every objective. To obtain the ideal solutions, every objective is optimized independently regardless of other objectives. In (4.11), we maximize $z_{1}, z_{2}^{\prime}$, and minimize $z_{3}$ individually to acquire their ideal solutions $z_{1}^{*}$, $z_{2}^{*}$ and $z_{3}^{*}$, respectively. The ideal values are $z_{1}^{*}=8$, $z_{2}^{*}=1,722,198$, and $z_{3}^{*}=5000$.
Step 2: Get the anti-ideal solution of every objective.
To obtain the anti-ideal solutions, every objective is computed in the opposite way regardless of other objectives. Now, we minimize $z_{1}, z_{2}^{\prime}$, and maximize $z_{3}$ to acquire the anti-ideal solutions $z_{1}^{-}$, $z_{2}^{-}$and $z_{3}^{-}$, respectively. The anti-ideal values are $z_{1}^{-}=4, z_{2}^{-}=733764.5$, and $z_{3}^{-}=40,000$.

Step 3: Define the membership function of every objective by its ideal and anti-ideal solutions. With the ideal and anti-ideal solutions of every objective, we can define their membership functions as follows:
$\mu_{z_{k}}\left(z_{k}\right)=\frac{z_{k}-z_{k}^{-}}{z_{k}^{*}-z_{k}^{-}}$

The membership functions evaluate the degree of fulfillment for every objective.
Step 4: Maximize the minimal membership function of the three objectives.
Using Zimmermann's fuzzy approach for multiobjective programs, the model (4.11) can be con-

![img-5.jpeg](img-5.jpeg)
where $\lambda$ is defined as $\lambda=\min _{1,2,3}\left(\mu_{z_{1}}\left(z_{1}\right)\right.$. $\left.\mu_{z_{2}^{\prime}}\left(z_{2}^{\prime}\right), \mu_{z_{3}}\left(z_{3}\right)\right)$

In (5.2), this study intends to search for the maximum of the minimal satisfaction level of all the objective functions. To avoid the poor estimation of the fuzzy parameters and decision quality, we set the strict lower bound for the membership of every fuzzy parameter at 0.5 . Applying the ideal and antiideal values computed in Step 1 and Step 2, (5.2) is specified as (5.3):

Max $\lambda$
s.t.

$$
\begin{aligned}
& \lambda \leq \frac{z_{1}-4}{8-4} \\
& \lambda \leq \frac{z_{2}^{\prime}-733764.5}{1,722,198-733764.5} \\
& \lambda \leq \frac{z_{3}-40,000}{5000-40,000} \\
& \text { (4.6)-(4.8), (4.12). }
\end{aligned}
$$

This study will solve (5.3) with LINGO 8.0 developed by LINGO Systems Inc. [21]. LINGO is a software designed to build and solve linear, nonlinear and integer optimization models. LINGO provides an integrated package that includes a language for expressing optimization models, a full featured environment for building and editing problems, and a set of built-in solvers. Part of the LINGO model is listed in Appendix A.

LINGO 8.0 solves (5.3) in 1 s and obtains the optimal treatment as $\operatorname{tr}_{1}\left(\operatorname{tr}_{1}=1\right.$, $\left.\operatorname{tr}_{0}=\operatorname{tr}_{2}=\operatorname{tr}_{3}=\operatorname{tr}_{4}=\operatorname{tr}_{5}=0\right)$, the normalizing constant $\alpha=303.9275$, the optimal minimal membership of the objectives $\lambda=0.5714$, and the likelihood of every pathogens:

$$
\begin{array}{ll}
P\left(+ \text { patho }_{1} \mid e\right)=0.4000, & P\left(+ \text { patho }_{2} \mid e\right)=0.2916 \\
P\left(+ \text { patho }_{3} \mid e\right)=0.3606, & P(+\mathrm{uti} \mid e)=0.9430
\end{array}
$$

Table 5 The result table


The suggested optimal treatment results in a probability of 0.8369 to cover from the urinary tract infection, equivalent gain in life expectancy as $dollars $ $1,616,259$, and the total costs in $\$ 20,000$. Besides, the clinician can make the diagnosis and optimal prescription at the first decision point with an overall confidence of the fuzzy parameters at 0.5978 . We also find that $\bar{x}_{4}, \bar{x}_{7}, \bar{x}_{8}$ are referenced significantly apart from the most possible values. It makes sense that, under this reasoning context, the experts need to make some subjective judgment or trade-off between different, even conflicting information sources, which make the fuzzy parameters referenced apart from their most confident values. The detailed solutions and part of LINGO solution report are listed in Table 5 and Appendix B.

## 6. Lesson learned

During the implementation of the reasoning model, the authors find the strength of the optimization model. First, the reasoning system allows the clinicians to combine their special judgments or experiences as extra constraints, which supplement

the incomplete formal knowledge. This is useful for some newly discovered disease or infections, and increase the flexibility and robustness for various clinical settings. Second, the model completes two major tasks in medical informatics: diagnostic reasoning and treatment planning simultaneously, which is an important requirement for clinical decision support systems. Third, LINGO provides an efficient computation tool for solving the optimization model, especially when the authors adopt some linearizing techniques to transform the highly nonlinear program. Based on the authors' experiences, LINGO performs better in solving linear programs than in solving nonlinear programs.

However, the authors also find several potential challenges in developing the proposed reasoning system. First, as the clinical problems grow larger and more complex, it may be a burden for the clinicians to formulate the model. In some diseases, there may be tens or hundreds of nodes in the networks. The clinicians will have difficulties to estimate the parameters or specify the conditions of their diagnosis and prescription. Therefore, the system needs some experts in knowledge engineering or information management to participate in, which consequently increases the costs to implement. Second, as the scales of network grow larger, belief propagation will be more complicated and time-consuming. Some special techniques for belief propagation may be considered, such as clustering, joint tree decomposition, stochastic simulation, and so on $[2,3,7-10]$. How to integrate these propagation methods and the optimization model will be a critical issue in implementing the reasoning system. Third, as network structures become huge, implementing the optimization model with LINGO will be fairly challenging. LINGO provides several interfaces with other applications, such as Visual C++, Visual Java, Visual Basic, etc. The system developers can bundle LINGO's functionality into their applications, or call functions from within
the LINGO models that were written in an external programming language [21]. It will facilitate generating the codes for LINGO models and importing the input data from other applications.

## 7. Future plans

The authors suggest several future extensions to this research.

1. Global optimization: Most medical diagnostic problems are highly nonlinear, and the global optimization is difficult to achieve in most cases. The model solvers need some special techniques to search for the global optimum. These optimization techniques can improve the solution quality and reliability of the reasoning model [20].
2. Integration with other heuristic computation techniques: As the problem and network structure grow complex, some heuristic methods may be needed for belief propagation. The computation efficiency will be improved if the reasoning systems integrate some heuristic techniques, such as stochastic simulation, genetic algorithms, neural network computing, etc.
3. Integrate various medical knowledge bases: The developers can integrate various medical knowledge bases to acquire richer diagnostic references and treatment suggestions, such as from traditional Chinese medicine, western medicine, Indian medicine, and so on.
4. Integrate with regional clinical or medical databases: The reasoning system may raise the feasibility and reliability by integrating local or regional medical databases, which will guarantee more accurate parameter estimation and fitness to different regional diagnostic environments. It is also an important stepping stone to build a complete medical decision support system.

# Appendix A. Part of the LINGO model 

```
max = beta; ! the minimal membership of the three objectives;
beta1 = (u1+u2+u3+u4+u5+u6+u7+u8- 4)/(8 - 4); !the membership of z1;
beta2 = (cov * 35 * 55000 - 733764.5) /(1722198-733764.5) ; !the
membership of z2;
beta3 = ((5000*tr0 + 20000*tr1 + 25000*tr2 +30000*tr3 +32000*tr4
+50000*tr5)- 40000)/ (5000-40000); !the membership of z3;
beta <= beta1;
beta <= beta2;
beta <= beta3;
!constraint (4.6);
alpha*(t111_11 + t101_11 + t110_11 + t100_11 + t011_11 + t001_11 +
t010_11 + t000_11 +t111_01 + t101_01 + t110_01 + t100_01 + t011_01 +
t001_01 + t010_01 + t000_01 +t111_10 + t101_10 + t110_10 + t100_10 +
t011_10 + t001_10 + t010_10 + t000_10 +t111_00 + t101_00 + t110_00 +
t100_00 + t011_00 + t001_00 + t010_00 + t000_00) = 1;
!constraint (4.7);
tr0 + tr1 + tr2+ tr3+ tr4+ tr5 = 1;
! tr0-tr5 are the treatments, stand for tri in the paper;
@bin(tr1); !means binary variable;
@bin(tr2);
@bin(tr3);
@bin(tr4);
@bin(tr5);
@bin(tr0);
!constraint (4.8), p1= Prob(Pathol = 1), p2= Prob(Patho2 = 1);
!p3= Prob(Patho3 = 1);
0.3 <= p3; p3 <=0.5;
!constraint (4.12) disjunctive constraint;
!p1 <= 0.4 or p2 <= 0.4;
BIG_M = 1000;
@bin(g1); @bin(g2);
BIG_M *(g1 -1) <= p1 - 0.4; p1 - 0.4 <= BIG_M *g1+BIG_M *(1-g2);
BIG_M *(g2-1) <= p2 - 0.4; p2 - 0.4 <= BIG_M *g2+BIG_M *(1-g1);
ep <= g1 + g2; g1 + g2 <= 1;
ep = 0.001; ! end of (4.12);
! Linearizing the membership functions u1-u8;
!d1 - d8 are the distances, which stand for the d1-d8 in the paper;
u1 = 5*(x1-0.6) - 2*(5*(x1 - 0.8 + d1));
x1 + d1 >= 0.8;
0<= d1; d1<= 0.8;
u2 = 10*(x2-0.7) - 2*(10*(x2 - 0.8 + d2));
x2 + d2 >= 0.8;
0<= d2; d2<= 0.8;
u3 = 20*(x3-0.7) - 2*(20*(x3 - 0.75 + d3));
x3 + d3 >= 0.75;
0<= d3; d3<= 0.75;
u4 = 10*(x4-0.5) - 2*(10*(x4 - 0.6 + d4));
x4 + d4 >= 0.6;
0<= d4; d4<= 0.6;
u5 = 10*(x5-0.7) - 2*(10*(x5 - 0.8 + d5));
x5 + d5 >= 0.8;
0<= d5; d5<= 0.8;
u6 = 20*(x6-0.55) - 2*(20*(x6 - 0.6 + d6));
x6 + d6 >= 0.6;
0<= d6; d6<= 0.6;
u7 = 10*(x7-0.4) - 2*(10*(x7 - 0.5 + d7));
```

```
x7 + d7 >= 0.5;
0<= d7; d7<= 0.5;
u8 = 100*(x8-0.0) - 2*(100*(x8 - 0.01+ d8));
x8 + d8 >= 0.01;
0<= d8; d8<= 0.01;
```

lwhen uti =1, the coefficient of prob(signs|uti): sign1 to sign6;
sign1 $=(1-.6) * .9 * .6 * .8 *(1-.6) *(1-.7)$;
lwhen uti $=0$, the coefficient of signs;
sign0 $=(1-.01) * .1 * .05 * .05 *(1-.1) *(1-.01)$;
ldefining the coverage probability for the instance with 3 pathogens
and 6 treatments;
cov111= .3*tr0 + .7*tr1 + .7*tr2+ .8*tr3 + .7*tr4 + .8*tr5;
cov101= .4*tr0 + .9*tr1 + .7*tr2+ .8*tr3 + .95*tr4 + .9*tr5;
cov110= .4*tr0 + .99*tr1 + .85*tr2+ .87*tr3 + .8*tr4 + .85*tr5;
cov100= .5*tr0 + .95*tr1 + .7*tr2+ .8*tr3 + .9*tr4 + .9*tr5;
cov011= .4*tr0 + .7*tr1 + .85*tr2+ .95*tr3 + .8*tr4 + .8*tr5;
cov001= .3*tr0 + .8*tr1 + .8*tr2+ .99*tr3 + .7*tr4 + .9*tr5;
cov010= .3*tr0 + .75*tr1 + .99*tr2+ .8*tr3 + .9*tr4 + .9*tr5;
cov000= .6*tr0 + .7*tr1 + .8*tr2+ .9*tr3 + .95*tr4 + .9*tr5;
!Prob(p1,p2,p3,uti+, cov+);
t111_11 = .1* .09* .09*x1* sign1 *cov111;
t101_11 = .1*(1-.09)*.09*x2*sign1 *cov101;
t110_11 = .1* .09* (1-.09)*x3*sign1 *cov110;
t100_11 = .1*(1-.09)*(1-.09)*x4*sign1*cov100;
t011_11 = .9* .09* .09*x5* sign1 *cov011;
t001_11 = .9*(1-.09)*.09*x6*sign1 *cov001;
t010_11 = .9* .09* (1-.09)*x7*sign1 *cov010;
t000_11 = .9*(1-.09)*(1-.09)*x8*sign1*cov000;
!Prob(p1,p2,p3,uti-, cov+);
t111_01 = .1* .09* .09*(1-x1)* sign0 *cov111;
t101_01 = .1*(1-.09)*.09*(1-x2)* sign0 *cov101;
t110_01 = .1* .09* (1-.09)*(1-x3)* sign0 *cov110;
t100_01 = .1*(1-.09)*(1-.09)*(1-x4)* sign0*cov100;

```
t011_01 = .9* .09* .09*(1-x5)* sign0 *cov011;
t001_01 = .9*(1-.09)*.09*(1-x6)* sign0 *cov001;
t010_01 = .9* .09* (1-.09)*(1-x7)* sign0 *cov010;
t000_01 = .9*(1-.09)*(1-.09)*(1-x8)* sign0 *cov000;
! Prob(p1,p2,p3,uti+,cov-);
t111_10 = .1* .09* .09*x1* sign1 *(1-cov111);
t101_10 = .1*(1-.09)*.09*x2* sign1 *(1-cov101);
t110_10 = .1* .09* (1-.09)*x3* sign1 *(1-cov110);
t100_10 = .1*(1-.09)*(1-.09)*x4* sign1 *(1-cov100);
t011_10 = .9* .09* .09*x5* sign1 *(1-cov011);
t001_10 = .9*(1-.09)*.09*x6* sign1 *(1-cov001);
t010_10 = .9* .09* (1-.09)*x7* sign1 *(1-cov010);
t000_10 = .9*(1-.09)*(1-.09)*x8* sign1 *(1-cov000);
! Prob(p1,p2,p3,uti-,cov-);
t111_00 = .1* .09* .09*(1-x1)* sign0 *(1-cov111);
t101_00 = .1*(1-.09)*.09*(1-x2)* sign0 *(1-cov101);
t110_00 = .1* .09* (1-.09)*(1-x3)* sign0 *(1-cov110);
t100_00 = .1*(1-.09)*(1-.09)*(1-x4)* sign0 *(1-cov100);
t011_00 = .9* .09* .09*(1-x5)* sign0 *(1-cov011);
t001_00 = .9*(1-.09)*.09*(1-x6)* sign0 *(1-cov001);
t010_00 = .9* .09* (1-.09)*(1-x7)* sign0 *(1-cov010);
t000_00 = .9*(1-.09)*(1-.09)*(1-x8)* sign0 *(1-cov000);
! defining the marginal probabilities;
! p1= Prob(Pathol = 1), p2= Prob(Patho2 = 1),p3= Prob(Patho3 = 1);
p1 = alpha*(t111_11 + t101_11 + t110_11 + t100_11
+ t111_01 + t101_01 + t110_01 + t100_01
+ t111_10 + t101_10 + t110_10 + t100_10
+ t111_00 + t101_00 + t110_00 + t100_00);
p2 = alpha*(t111_11 + t110_11 + t011_11 + t010_11
+ t111_01 + t110_01 + t011_01 + t010_01
+ t111_10 + t110_10 + t011_10 + t010_10
+ t111_00 + t110_00 + t011_00 + t010_00);
p3 = alpha*(t111_11 + t101_11 + t011_11 + t001_11
    + t111_01 + t101_01 + t011_01 + t001_01
    + t111_10 + t101_10 + t011_10 + t001_10
    + t111_00 + t101_00 + t011_00 + t001_00);
    ! uti= Prob(uti = 1),
    uti = alpha*(t111_11 + t101_11 + t110_11 + t100_11
    + t011_11 + t001_11 + t010_11 + t000_11
    + t111_10 + t101_10 + t110_10 + t100_10
    + t011_10 + t001_10 + t010_10 + t000_10);
    ! cov= Prob(coverage = 1),
    cov = alpha*(t111_11 + t101_11 + t110_11 + t100_11
    + t011_11 + t001_11 + t010_11 + t000_11
    + t111_01 + t101_01 + t110_01 + t100_01
    + t011_01 + t001_01 + t010_01 + t000_01);
```

# Appendix B. Part of the LINGO solution report 

