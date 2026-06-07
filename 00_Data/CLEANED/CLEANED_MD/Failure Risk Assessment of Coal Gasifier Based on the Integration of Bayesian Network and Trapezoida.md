# Article 

## Failure Risk Assessment of Coal Gasifier Based on the Integration of Bayesian Network and Trapezoidal Intuitionistic Fuzzy Number-Based Similarity Aggregation Method (TpIFN-SAM)

Yunpeng Liu ${ }^{1}$, Shen Wang ${ }^{1}$, Qian Liu ${ }^{2}$, Dongpeng Liu ${ }^{3}$, Yang Yang ${ }^{1}$, Yong Dan ${ }^{1}$ and Wei Wu ${ }^{1, * *}$


#### Abstract

check for updates Citation: Liu, Y.; Wang, S.; Liu, Q.; Liu, D.; Yang, Y.; Dan, Y.; Wu, W. Failure Risk Assessment of Coal Gasifier Based on the Integration of Bayesian Network and Trapezoidal Intuitionistic Fuzzy Number-Based Similarity Aggregation Method (TpIFN-SAM). Processes 2022, 10, 1863. https://doi.org/10.3390/ pr10091863


Academic Editor: Tamás Varga
Received: 18 August 2022
Accepted: 13 September 2022
Published: 15 September 2022
Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## (0)

Copyright: (c) 2022 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 School of Chemical Engineering, Northwest University, Xi'an 710069, China
2 Central Research Institute of China Chemical Science and Technology Co., Ltd., Beijing 100083, China
3 School of Chemical Engineering and Technology, Xi'an Jiaotong University, Xi'an 710049, China

* Correspondence: wuwei@nwu.edu.cn


#### Abstract

The coal gasifier is the core unit of the coal gasification system. Due to its exposure to high temperatures, high pressures, and aggressive media, it is highly susceptible to serious accidents in the event of failure. Therefore, it is important for the gasifier to perform failure-risk assessment to understand its safety status and provide safety measures. Bayesian networks (BNs) for risk analysis of process systems has received a lot of attention due to its powerful inference capability and its ability to reflect complex relationships between risk factors. However, the acquisition of basic probability data in a Bayesian network is always a great challenge. In this study, an improved Bayesian network integrated with a trapezoidal intuitionistic fuzzy number-based similarity aggregation method (TpIFN-SAM) is proposed for the failure-risk assessment of process systems. This approach used the TpIFN-SAM to collect and aggregate experts' opinions for obtaining the prior probabilities of the root events in the BN. In the TpIFN-SAM, the intuitionistic fuzzy analytic-hierarchy-process method (IF-AHP) was adopted to assign the expert weights for reducing subjectivity or the bias caused by individual differences. To clarify the suitability of the proposed method, a case study of a coal gasifier was demonstrated, and both prediction and diagnosis analyses of the BN were performed; finally, the weak links of the gasifier were identified.


Keywords: coal gasifier; trapezoidal intuitionistic fuzzy number; Bayesian network; failure probability; risk analysis

## 1. Introduction

The coal-gasification process is an essential part of the "clean coal" technology that can improve overall energy-conversion and -utilization efficiency [1]. This process is carried out in a gasifier (also known as a gasification furnace), in which the combustible parts of coal or coal coke are converted into gases like CO and $\mathrm{H}_{2}$ by chemical reactions at high temperatures and high pressures. In this condition, the gasifier needs to ensure safe operation. Fire and explosion are unimaginable consequences that may easily occur when equipment fails.

Equipment-failure-risk assessment is a necessary means to clarify the safety status of the equipment and ensure the normal operation of the chemical systems. There are numerous risk-assessment methods available in process systems, one group of which is based on a combination of logical/probabilistic diagrams and deductive reasoning, such as fault-tree analysis (FTA), event-tree analysis (ETA), the bow-tie model (BT), and Bayesian networks (BNs), and are very widely used for risk and reliability analysis due to their intuitiveness, expressiveness, ease of analysis, and reasoning [2-5]. Of these, BN is suitable for modelling and analyzing complex systems and has gained much attention

compared to others, since it can handle the occurrence of multi-state variables, express conditional dependencies among events, and allow for bidirectional reasoning to identify the most failure-prone links of the system better [6,7,8]. As with other approaches, the limitation is that a BN cannot succeed without complete and accurate data (i.e., base-event probabilities and conditional-probability tables), and unfortunately in practice the required data are difficult to obtain. For this reason, a BN is often integrated with data-extraction technologies, particularly expert elicitation.

Currently, the common approaches to data acquisition for a BN include fuzzy set theory [9], rough set theory [10], evidence theory [11], the cloud model [12], and hybrid models [13]. Among them, the combination of fuzzy sets and a BN has been most extensively studied in process-safety engineering since fuzzy set theory is well recognized as a very effective mathematical tool for dealing with uncertain and incomplete information [14]. Kabir et al. [15] developed an O \& G pipeline-failure model by assimilating a fuzzy set into a BN. In this model, the prior probability and conditional probability values in the BN can be interpreted according to the linguistic terms corresponding to the trapezoidal fuzzy numbers. Yazdi and Kabir [16] presented a comprehensive framework for risk evaluation of complex process systems through integrating fuzzy set theory with a BN. In this framework, the uncertainty problem of failure data was solved by expert knowledge with improved fuzzy AHP. Zhao et al. [17] also employed fuzzy AHP and BN to assess the domino effects in the coal-gasification process. Yan et al. [18] applied a BN with a fuzzy set to analyze biomass gasification when a gas leakage happens, and they confirmed the missing reliability failure probabilities by using expert judgments obtained based on linguistic terms corresponding to triangular and trapezoidal fuzzy numbers. Subsequently, Mostafa Pouyakian et al. [19] proposed a similar approach to analyze the possible risk factors of storage tanks with a floating roof. Akbar Rostamabadi et al. [20] integrated the fuzzy best-worst method (Fuzzy-BWM) with a BN for safety and reliability analysis of a process system that used Fuzzy-BWM for expert judgment to obtain the required fuzzy probabilities.

These research endeavors have contributed significantly to the successful utilization of BNs in the reliability and risk evaluation of process industries. However, the limitations are that the fuzzy set theory may cause deprivation and deformation of evaluation information because it uses only one membership function to represent the extent to which a particular target pertains to a set [21,22]. In reality, there are often situations where a person may suppose that a target pertains to a set to an extent, but they may not be quite sure about it, which means there may be indecision about the membership extent of the target in the set. For the purpose of resolving the challenge, Atanassov [23] proposed a intuitionistic fuzzy set (IFS) in 1986. In IFS theory there are two different functions, i.e., the membership and non-membership functions, to describe uncertain information. The difference between the two functions is called the degree of hesitation. The IFS theory extends the traditional fuzzy set theory, and it has a stronger ability to express and dispose of uncertainty than fuzzy set theory. In this light, Yu et al. [24] introduced triangular intuitionistic fuzzy numbers (a special case of IFS) to BNs for analysis of the fire damage and blast accident of a crude-oil-storage tank. This attempt showed the potential power of combining IFS with BNs. As far as intuitionistic fuzzy numbers (IFNs) are concerned, trapezoidal IFNs, as an extension of triangular IFNs, better accommodate for the description of non-deterministic information. This inspired us to try to integrate trapezoidal IFNs with BNs to analyze the failure risk of process systems so as to improve the feasibility and flexibility of BNs in engineering applications. Similarly, this is also the motivation for the new approach that is presented next.

When acquiring data using fuzzy set theory or intuitionistic fuzzy set theory, experts often need to be involved. Given the limitations of experts' own knowledge and experience, certain means are required to deal with experts' opinions to reduce subjective bias, usually through assigning different weights to the experts and then aggregating the different opinions [25]. Recently, the similarity aggregation method (SAM) [26] as an aggregation

strategy for experts' opinions has been of increasing interest in the safety analysis of process systems like storage tanks for hazardous chemicals [27-29] and oil and gas pipelines [30]; this is because it not only conforms to the custom of expert evaluation, but also enables the aggregation result to be more exact and workable [29,31].

The main contributions of this paper are as follows: (1) This study attempts to propose an improved framework integrating intuitionistic fuzzy AHP, trapezoidal intuitionistic fuzzy number-based SAM, and a Bayesian network for failure-risk assessment of a coal gasifier. (2) This framework uses intuitionistic fuzzy AHP to assign the expert weights for reducing subjectivity or the bias caused by individual differences and obtains the likelihood of occurrence of root events in the BN through trapezoidal intuitionistic fuzzy numberbased SAM with experts' judgment. (3) This strategy can more convincingly translate the judgments of all experts into a clear probability value by an intuitionistic fuzzy reasoning approach, thus overcoming the difficulty of obtaining the basic probability data in the BN.

For the remainder, the organization is arranged as follows: Section 2 introduces basic concepts of intuitionistic fuzzy sets, trapezoidal intuitionistic fuzzy numbers, and Bayesian networks. Section 3 presents the improved framework and provides the detailed implementation processes. In Section 4, an example of clarification is provided to demonstrate the specific analysis process and verify the feasibility of the method. Finally, the conclusions are described in Section 5.

# 2. Preliminaries 

### 2.1. Intuitionistic Fuzzy Set

Definition 1 [23,32]: Let $X$ be a general set, and the intuitionistic fuzzy set (IFS) $\widetilde{A}$ is a set in

$$
\widetilde{A}=\left\{x, \mu_{\widetilde{A}}(x), v_{\widetilde{A}}(x) \mid x \in X\right\}
$$

where $\mu_{\widetilde{A}}(x): X \rightarrow[0,1]$ and $v_{\widetilde{A}}(x): X \rightarrow[0,1]$ are membership and non-membership, respectively. Furthermore, the following requirements are fulfilled $0 \leq \mu_{\widetilde{A}}(x)+v_{\widetilde{A}}(x) \leq 1$ for all $x \in X$ in the $\widetilde{A}$. An ordered interval pair consisting of $\mu_{\widetilde{A}}(x)$ and $v_{\widetilde{A}}(x)$ is an intuitionistic fuzzy set, written as $\left\langle\mu_{\widetilde{A}}(x), v_{\widetilde{A}}(x)\right\rangle$.

For each intuitionistic fuzzy set in $X, \pi_{\widetilde{A}}(x)=1-\mu_{\widetilde{A}}(x)-v_{\widetilde{A}}(x)$ is the intuitionistic index of $x$ in $\widetilde{A}$. This is a measure of the hesitancy of $x$ to $\widetilde{A}$. Distinctly, for each $x \in X, 0 \leq \pi_{\widetilde{A}}(x) \leq 1$.

Definition 2 [33]: Let $\widetilde{A}$ be an intuitionistic fuzzy number on a real number set $R$, and its membership and non-membership functions fulfill the following equations:

$$
\mu_{\widetilde{A}}(x)=\left\{\begin{array}{ll}
f_{\widetilde{A}}(x), & a<x<b \\
1, & b \leq x \leq c \\
g_{\widetilde{A}}(x), & c<x<d \\
0, & \text { otherwise }
\end{array}, v_{\widetilde{A}}(x)= \begin{cases}h_{\widetilde{A}}(x), & a^{\prime}<x<b \\
0, & b \leq x \leq c \\
k_{\widetilde{A}}(x), & c<x<d^{\prime} \\
1, & \text { otherwise }\end{cases}\right.
$$

respectively, where $0 \leq \mu_{\widetilde{A}}(x) \leq 1,0 \leq v_{\widetilde{A}}(x) \leq 1$, and $0 \leq \mu_{\widetilde{A}}(x)+v_{\widetilde{A}}(x) \leq 1 . a^{\prime}, a, b, c$, $d, d^{\prime} \in R$, such that $a^{\prime} \leq a \leq b \leq c \leq d \leq d^{\prime}$ and four functions $f_{\widetilde{A}}, g_{\widetilde{A}}, h_{\widetilde{A}}, k_{\widetilde{A}}: R \rightarrow[0,1]$ are known as the sides of intuitionistic fuzzy numbers. In addition, $f_{\widetilde{A}}, k_{\widetilde{A}}$, are non-decreasing continuous functions, and $g_{\widetilde{A}}, h_{\widetilde{A}}$ are non-increasing continuous functions. A set of intuitionistic fuzzy numbers can be defined when the four functions are linear functions, as shown in Definition 3.

Definition 3 [34]: Let $\widetilde{A}_{1}$ and $\widetilde{A}_{2}$ be two intuitionistic fuzzy numbers $\widetilde{A}_{1}=\left(\mu_{\widetilde{A}_{1}}, v_{\widetilde{A}_{1}}\right)$, $\widetilde{A}_{2}=\left(\mu_{\widetilde{A}_{2}}, v_{\widetilde{A}_{2}}\right)$ on a real number set $R$, then

$$
\begin{aligned}
& \widetilde{A}_{1}+\widetilde{A}_{2}=\left(\mu_{\widetilde{A}_{1}}+\mu_{\widetilde{A}_{2}}-\mu_{\widetilde{A}_{1}} \mu_{\widetilde{A}_{2}}, v_{\widetilde{A}_{1}} v_{\widetilde{A}_{2}}\right) \\
& \widetilde{A}_{1} \times \widetilde{A}_{2}=\left(\mu_{\widetilde{A}_{1}} \mu_{\widetilde{A}_{2}}, v_{\widetilde{A}_{1}}+v_{\widetilde{A}_{2}}-v_{\widetilde{A}_{1}} v_{\widetilde{A}_{2}}\right)
\end{aligned}
$$

$$
\begin{aligned}
\lambda \widetilde{A}_{1} & =\left(1-\left(1-\mu_{\widetilde{A}_{1}}\right)^{\lambda}, v^{\lambda}{ }_{\widetilde{A}_{1}}\right), \lambda>0 \\
\widetilde{A}_{1}^{\lambda} & =\left(\mu^{\lambda}{ }_{\widetilde{A}_{1}}, 1-\left(1-v_{\widetilde{A}_{1}}\right)^{\lambda}\right), \lambda>0
\end{aligned}
$$

# 2.2. Trapezoidal Intuitionistic Fuzzy Number 

Definition 4 [33]: Let $\widetilde{A}$ be a trapezoidal intuitionistic fuzzy number (TpIFN) with parameters $a^{\prime} \leq a \leq b \leq c \leq d \leq d^{\prime}$ and indicated as $\widetilde{A}=\left(a, b, c, d ; a^{\prime}, b, c, d^{\prime}\right)$ on a real number set $R$, then its membership and non-membership functions satisfy the following equations:

$$
\mu_{\widetilde{A}}(x)= \begin{cases}\frac{x-a}{b-a}, & a<x<b \\ 1, & b \leq x \leq c \\ \frac{d-c}{d-c}, & c<x<d \\ 0, & \text { otherwise }\end{cases}, v_{\widetilde{A}}(x)= \begin{cases}\frac{b-x}{b-a^{\prime}}, & a^{\prime}<x<b \\ 0, & b \leq x \leq c \\ \frac{d-c}{d-c}, & c<x<d^{\prime} \\ 1, & \text { otherwise }\end{cases}
$$

respectively, where $0 \leq \mu_{\widetilde{A}}(x) \leq 1,0 \leq v_{\widetilde{A}}(x) \leq 1,0 \leq \mu_{\widetilde{A}}(x)+v_{\widetilde{A}}(x) \leq 1$. Figure 1 shows a general trapezoidal intuitionistic fuzzy number.
![img-0.jpeg](img-0.jpeg)

Figure 1. A general trapezoidal intuitionistic fuzzy number.
Definition 5 [34]: Let $\widetilde{A}_{1}=\left(a_{1}, b_{1}, c_{1}, d_{1} ; a_{1}^{\prime}, b_{1}, c_{1}, d_{1}^{\prime}\right)$ and $\widetilde{A}_{2}=\left(a_{2}, b_{2}, c_{2}, d_{2} ; a_{2}^{\prime}, b_{2}, c_{2}, d_{2}^{\prime}\right)$ be two trapezoidal intuitionistic fuzzy numbers, then

$$
\begin{gathered}
\widetilde{A}_{1}+\widetilde{A}_{2}=\left(a_{1}+a_{2}, b_{1}+b_{2}, c_{1}+c_{2}, d_{1}+d_{2} ; a_{1} t+a_{2}^{\prime}, b_{1}+b_{2}, c_{1}+c_{2}, d_{1}^{\prime}+d_{2}^{\prime}\right) \\
\widetilde{A}_{1} \times \widetilde{A}_{2}=\left(a_{1} a_{2}, b_{1} b_{2}, c_{1} c_{2}, d_{1} d_{2} ; a_{1}^{\prime} a_{2}^{\prime}, b_{1} b_{2}, c_{1} c_{2}, d_{1}^{\prime} d_{2}^{\prime}\right) \\
\lambda \widetilde{A}_{1}=\left(\lambda a_{1}, \lambda b_{1}, \lambda c_{1}, \lambda d_{1} ; \lambda a_{1}^{\prime}, \lambda b_{1}, \lambda c_{1}, \lambda d_{1}^{\prime}\right) \\
\widetilde{A}_{1}^{\lambda}=\left(a_{1}^{\lambda}, b_{1}^{\lambda}, c_{1}^{\lambda}, d_{1}^{\lambda} ; a_{1}^{\prime \lambda}, b_{1}^{\lambda}, c_{1}^{\lambda}, d_{1}^{\prime \lambda}\right)
\end{gathered}
$$

### 2.3. The Expectation of a TpIFN

Heilpern [35] defined the expected interval and expected value of a fuzzy number. The expected interval and expected value can be applied to fuzzy-number ranking or comparison problems. The expected value as the center of the expected interval can be regarded as the expected payoff connected to a linguistic term. This can also be generalized for TpIFNs. It is assumed that that $\widetilde{A}=\left(a, b, c, d ; a^{\prime}, b, c, d^{\prime}\right)$ is a TpIFN, and $E I^{\mu}$ and $E I^{\nu}$ denote the expected interval matching with membership and non-membership functions, respectively. The center of the expected interval of an intuitionistic fuzzy number is called the expected value of this number, denoted by $E V(\widetilde{A})$, and $E V^{\mu}$ and $E V^{\nu}$ denote the

expected value corresponding to membership and non-membership functions, respectively. Its parametric form are $\mu(\alpha)=\left(\overline{\mu(\alpha)}, \underline{\mu(\alpha)}\right)$ and $\nu(\alpha)=\left(\overline{\nu(\alpha)}, \underline{\nu(\alpha)}\right)$, where $\mu(\alpha)$ and $\nu(\alpha)$ are the parametric form of a TpIFN corresponding to membership and non-membership functions, respectively, and $\overline{\mu(\alpha)}=d-\alpha(d-c) ; \underline{\mu(\alpha)}=a+\alpha(b-a)$ and $\overline{\nu(\alpha)}=b-$ $(1-\alpha)\left(b-a^{\prime}\right) ; \underline{\nu(\alpha)}=c+(1-\alpha)\left(d^{\prime}-c\right)$ [36].

$$
\begin{gathered}
E V^{\mu}(\widetilde{A})=\frac{\int_{0}^{1} \overline{\mu(\alpha)} d \alpha+\int_{0}^{1} \underline{\mu}(\alpha) d \alpha}{2}=\frac{a+b+c+d}{4} \\
E V^{\nu}(\widetilde{A})=\frac{\int_{0}^{1} \overline{\nu(\alpha)} d \alpha+\int_{0}^{1} \underline{\nu}(\alpha) d \alpha}{2}=\frac{a^{\prime}+b+c+d^{\prime}}{4} \\
E V(\widetilde{A})=\lambda E V^{\mu}(\widetilde{A})+(1-\lambda) E V^{\nu}(\widetilde{A})
\end{gathered}
$$

Let $\lambda=0.5$, then

$$
E V(\widetilde{A})=\frac{1}{2} E V^{\mu}(\widetilde{A})+\frac{1}{2} E V^{\nu}(\widetilde{A})=\frac{a+a^{\prime}+2 b+2 c+d+d^{\prime}}{8}
$$

See Appendix A for the proof process.

# 2.4. Bayesian Network 

A Bayesian network (BN), known as a probabilistic graphical model, is a directed acyclic graph (DAG) that binds graph theory with probability theory. A BN consists of nodes representing events (i.e., random variables) and oriented lines (from parent nodes to child nodes) connecting these nodes and representing their causal relationships. Each node and its set of parent nodes corresponds to a conditional probability distribution $P\left(X_{i} \mid\right.$ Parent $\left.\left(X_{i}\right)\right)$ that indicates how much influence there is among the parent nodes and the child node. Given that a BN consists of $n$ random variables $X_{1}, X_{2}, \ldots, X_{n}$, according to the conditional independency and chain laws, the complete united probability distribution can be recorded as [37]

$$
P\left(X_{1}, X_{2}, \ldots, X_{n-1}, X_{n}\right)=\prod_{i=1}^{n} P\left(X_{i} \mid\right. \text { Parent }\left(X_{i}\right))
$$

Figure 2 shows an illustration of a BN including six nodes. Node $X_{1}$ is called the parent node of $X_{2}$ and $X_{3}$, whereas $X_{2}$ and $X_{3}$ are called the child nodes of $X_{1}$. It is worth mentioning that $X_{1}$ is also called the root node because it has no parent node. The complete united probability distribution of this can be expressed by Equation (16):

$$
P\left(X_{1}, X_{2}, X_{3}, X_{4}, X_{5}, X_{6}\right)=P\left(X_{6} \mid X_{5}\right) P\left(X_{5} \mid X_{3}, X_{2}\right) P\left(X_{4} \mid X_{2}, X_{1}\right) P\left(X_{3} \mid X_{1}\right) P\left(X_{2} \mid X_{1}\right) P\left(X_{1}\right)
$$

In the BN model, it has a forward (predictive) and backward (diagnostic) ability of inference. The forward inference is the inference from the causes (root nodes) to their effects (leaf nodes). Under the circumstances, new beliefs about this effect are obtained by using information about causes. In contrast, the backward inference is the inference on the contrary side (i.e., from the effect back to the cause). In this inference, the process of obtaining a new belief about causes based on known effects is continuously estimated and upgraded. Bayes' theorem can be used to advance the diagnosis analysis of the BN model (see Equation (18)) [37].

$$
P(A \mid B)=\frac{P(B \mid A) P(A)}{P(B)}
$$

where $A$ and $B$ are two random events; $P(A)$ and $P(B)$ are the prior probability of event $A$ and $B$, respectively; and $P(A \mid B)$ is the posterior probability of event $A$ occurring given after the occurrence of $B$.
![img-1.jpeg](img-1.jpeg)

Figure 2. Example of a Bayesian network.

# 2.5. Mapping to Bayesian Network from Fault Tree 

The determination of a BN structure is the first step in using it for prediction and diagnosis. There are several ways of constructing BNs: (1) expert knowledge-based [38], (2) data-driven [39], and (3) mapped from other models like the fault-tree, event-tree, or bow-tie models [40,41,42]. The third approach is adopted in this study, where the potential accident scenarios of a system are first determined by a fault tree, which is then mapped into a BN according to the method shown in Figure 3.
![img-2.jpeg](img-2.jpeg)

Figure 3. Mapping rules from fault tree to Bayesian network.
The conditional probability table (CPT) is another key component of BNs for implementing inference. During this process, the logical gate of the fault tree (FT) is used to confirm the CPT of each node in the BN. The logic gate rules of the FT describe the fault-logic relationship between parent and child events. Tables 1 and 2 show the rules of how to obtain a CPT according to the two most critical logic gates of FT: the "AND" gate and the "OR" gate [40].

Table 1. CPT corresponding to the AND gate in FT (Occ: occurred; Non: non-occurred).


Table 2. CPT corresponding to the OR gate in FT (Occ: occurred; Non: non-occurred).


# 3. Proposed Model for Failure-Risk Assessment Based on BN with TpIFN-SAM 

### 3.1. General Framework

The proposed framework is mainly used to analyze the failure probability of process systems, which consists of five core parts-construction of the BN through FT, expert elicitation, aggregation of experts' opinions by the TpIFN-SAM, the defuzzification process, and BN analysis-and is shown in Figure 4. The specific analysis process is described from Sections 3.2-3.7.
![img-3.jpeg](img-3.jpeg)

Figure 4. The proposed analysis framework.

### 3.2. Construction of the BN through FT

The construction of a BN describing system-failure scenarios and paths is the first step in analyzing the probability of possible failures in a process system. Here, the FT is first drawn according to the system's structural characteristics and associated risk factors,

where the top event is generally set as the most undesired event. Then, the FT is mapped into a BN with CPTs using the mapping rules mentioned in Section 2.5.

# 3.3. Expert Elicitation 

In this framework, expert elicitation is put to use for computing the probabilities of root events in the BN when the accurate probabilities of the events are lacking. In generally, the experts cannot give accurate probability values. This study therefore uses a method combining the TpIFNs and expert elicitation to elaborate the failure probabilities of each root node. Experts express their opinions on risk events in linguistic terms based on the practice or standards in the actual situation in this industry. In addition, the natural estimate of human memory capacity is $7 \pm 2$ grades [28,43]. Thus, 5-9 language terms scored by experts is most appropriate. Furthermore, heterogeneous expert judgment is adopted to reduce the prejudice of expert evaluation.

### 3.4. Aggregation of Experts' Opinions by TpIFN-SAM

### 3.4.1. Determination of Experts' Weights by Intuitionistic Fuzzy AHP (IF-AHP)

For the purpose of resolving the subjective preferences of experts and the incompleteness of individual knowledge and experience that may lead to biased results, the preference is usually to create an expert group of professionals and the relative importance of each expert's opinion is represented by assigning weights to each expert. There are several expert-weighting methods, like the method of arithmetic average [22], the Delphi method [44], and AHP [45]. However, these methods are often criticized for failing to sufficiently solve the intrinsic ambiguity and subjectivity. As an extension of AHP, intuitionistic fuzzy AHP (IF-AHP) [46] can enhance the inconsistent intuitive-preference relationship without the involvement of decision-makers, thereby fundamentally solving the above-mentioned problems. As a result, this work employs the IF-AHP method to acquire the expert-weight coefficients. The specific calculation of the expert weights are as follows.

Step 1. Establish the evaluation indices of expert weights.
There are some general deviations in the experts' judgements on the same event. This situation is affected by their professional position, educational background, and work experience. Therefore, a three-level hierarchical structure diagram of judging expert weights is established, as shown in Figure 5. Professional position, education level, and service time are accommodated as the evaluation indices of expert weights.
![img-4.jpeg](img-4.jpeg)

Figure 5. Three-level hierarchical structure of judging expert weights.
Step 2. Construct the IF-judgment matrix.
The intuitionistic fuzzy judgment matrices for the three-level indices are then established. Factors belonging to the same level of each factor of the previous level are matched and compared to build an intuitionistic fuzzy judgment matrix: $R=\left(r_{i j}\right)_{n \times n}$, with $i, j$ representing the rows and columns of the matrix, respectively, where $r_{i j} \equiv\left(\mu_{i j}, v_{i j}\right) ; \mu_{i j}$ denotes the degree to which an expert prefers $i$ when comparing the importance of factor

$i$ and factor $j ; v_{i j}$ denotes the degree to which an expert prefers $j$; and $\pi_{i j}=1-\mu_{i j}-v_{i j}$ denotes the hesitation degree. To better identify the intuitionistic preference relationship, an evaluation scale table is constructed, as shown in Table 3.

Table 3. IF-AHP preference scale.


Note: Reciprocal IFNs can be obtained by exchanging $\mu$ and $v$.
Step 3. Check consistency.
The consistency-test formula shown below is given for distance measurement based on the intuitionistic fuzzy information [46]:

$$
d(\bar{R}, R)=\frac{1}{2(n-1)(n-2)} \sum_{i=1}^{n} \sum_{j=1}^{n}\left(\left|\bar{\mu}_{i j}-\mu_{i j}\right|+\left|\bar{v}_{i j}-v_{i j}\right|+\left|\bar{\pi}_{i j}-\pi_{i j}\right|\right)
$$

where $R=\left(r_{i j}\right)_{n \times n}$ is the intuitionistic fuzzy judgment matrix obtained by pairwise comparison of indices at each layer $R=\left(r_{i j}\right)_{n \times n^{\prime}} \bar{R}=\left(\bar{r}_{i j}\right)_{n \times n}$ is the intuitionistic fuzzy consistency-judgment matrix calculated from the intuitionistic fuzzy judgment matrix, and $n$ represents the number of experts.

Let $\bar{R}=\left(\bar{\mu}_{i j}, \bar{v}_{i j}\right)$ when $j>i+1$, where

$$
\begin{gathered}
\bar{\mu}_{i j}=\frac{\sqrt[j-i-1]{\prod_{t=i+1}^{j-1} \mu_{i t} \mu_{t j}}}{\sqrt[j-i-1]{\prod_{t=t+1}^{j-1} \mu_{i t} \mu_{t j}}+\sqrt[j-i-1]{\prod_{t=i+1}^{j-1}\left(1-\mu_{i t}\right)\left(1-\mu_{t j}\right)} \\
\bar{v}_{i j}=\frac{\sqrt[j-i-1]{\prod_{t=i+1}^{j-1} v_{i t} v_{t j}}}{\sqrt[j-i-1]{\prod_{t=i+1}^{j-1} v_{i t} v_{t j}}+\sqrt[j-i-1]{\prod_{t=i+1}^{j-1}\left(1-v_{i t}\right)\left(1-v_{t j}\right)}}
\end{gathered}
$$

Let $\bar{r}_{i j}=r_{i j}$ when $j=i+1$; let $\bar{r}_{i j}=\left(\bar{v}_{i j}, \bar{\mu}_{i j}\right)$ when $j<i+1$.
Substitute $\bar{\mu}_{i j}, \bar{v}_{i j}$ into $d(\bar{R}, R)$, if $d(\bar{R}, R)<0.1$, then pass the consistency check; if $d(\bar{R}, R) \geq 0.1$, the parameters $\sigma$ will be set to iterate-that is, to transform the matrix by regulating the iterative parameters $\sigma$ until it passes. Given parameters $\sigma(\sigma \in[0,1])$, let

$$
\begin{gathered}
\widetilde{\bar{\mu}}_{i j}=\frac{\left(\mu_{i j}\right)^{1-\sigma}\left(\mu_{i j}\right)^{\sigma}}{\left(\mu_{i j}\right)^{1-\sigma}\left(\bar{\mu}_{i j}\right)^{\sigma}+\left(1-\mu_{i j}\right)^{1-\sigma}\left(1-\bar{\mu}_{i j}\right)^{\sigma}}, i, j=1,2, \ldots, n \\
\widetilde{\bar{v}}_{i j}=\frac{\left(v_{i j}\right)^{1-\sigma}\left(\bar{v}_{i j}\right)^{\sigma}}{\left(v_{i j}\right)^{1-\sigma}\left(\bar{v}_{i j}\right)^{\sigma}+\left(1-\bar{v}_{i j}\right)^{1-\sigma}\left(1-\bar{v}_{i j}\right)^{\sigma}}, i, j=1,2, \ldots, n
\end{gathered}
$$

Substitute the adjusted matrix into $d(\widetilde{R}, R)$, and then we can get

$$
d(\widetilde{R}, R)=\frac{1}{2(n-1)(n-2)} \sum_{i=1}^{n} \sum_{j=1}^{n}\left(\left|\widetilde{\mu}_{i j}-\mu_{i j}\right|+\left|\widetilde{v}_{i j}-v_{i j}\right|+\left|\widetilde{\pi}_{i j}-\pi_{i j}\right|\right)
$$

Step 4. Calculate the priority.
After obtaining the intuitionistic fuzzy consistency-judgment matrix, the priority of the indices of the previous layer is calculated by

$$
\varepsilon_{i}=\left(\frac{\sum_{j=1}^{n} \mu_{i j}}{\sum_{i=1}^{n} \sum_{j=1}^{n}\left(1-v_{i j}\right)}, 1-\frac{\sum_{j=1}^{n}\left(1-v_{i j}\right)}{\sum_{i=1}^{n} \sum_{j=1}^{n}\left(1-\mu_{i j}\right)}\right), i=1,2, \ldots, n
$$

where $i$ denotes the number of experts.
Step 5. Aggregate the IFNs.
According to the priority $\varepsilon_{i}$, the aggregated priority value of each expert $W_{i}$ can be calculated by

$$
W_{i}=\sum_{j=1}^{n}\left(\varepsilon_{j} \times \varepsilon_{i j}\right), i=1,2, \cdots, n
$$

Step 6. Sort experts' priority and calculate their weights.
The crisp value of the priority of each expert is obtained by

$$
\rho\left(W_{i}\right)=0.5\left(1+\pi_{W_{i}}\right)\left(1-\mu_{W_{i}}\right)
$$

where a smaller $\rho\left(W_{i}\right)$ represents stronger priority from the expert. The relative weight of each expert can be calculated by

$$
w_{i}=\frac{S\left(W_{i}\right)}{\sum_{i=1}^{n} S\left(W_{i}\right)}
$$

where

$$
S\left(W_{i}\right)=1-\rho\left(W_{i}\right)
$$

# 3.4.2. Calculation of the Experts' Opinion Similarity and Construction of the Opinion Similarity Matrix 

When the weights of all experts in the expert group are determined, the experts will be consulted to give the probability of occurrence of the root events in the BN as regards linguistic terms. These opinions are converted into the corresponding TpIFNs. The experts' opinion similarity can then be given by Equation (30).

$$
S\left(\widetilde{E}_{i}, \widetilde{E}_{j}\right)=\left\{\begin{array}{l}
\frac{E V\left(\widetilde{E}_{i}\right)}{E V\left(\widetilde{E}_{j}\right)}, E V\left(\widetilde{E}_{i}\right) \leq E V\left(\widetilde{E}_{j}\right) \\
\frac{E V\left(\widetilde{E}_{j}\right)}{E V\left(\widetilde{E}_{i}\right)}, E V\left(\widetilde{E}_{j}\right) \leq E V\left(\widetilde{E}_{i}\right)
\end{array}\right.
$$

where $E V\left(\widetilde{E}_{i}\right)$ is the expectation of the TpIFN converted from the $i$ th expert's linguistic opinion on the probability of a certain root event's occurrence, and it can be calculated by

Equation (10) in Section 2.3. $S\left(\bar{E}_{i}, \bar{E}_{j}\right)$ is the opinion similarity between the $i$ th expert and the $j$ th expert. If there are $m$ experts in the group, the similarity matrix $S_{m}$ is

$$
S_{m}=\left[\begin{array}{cccc}
1 & S_{21} & \cdots & S_{1 m} \\
S_{21} & 1 & \cdots & S_{2 m} \\
\vdots & \vdots & \ddots & \vdots \\
S_{m 1} & S_{m 2} & \cdots & 1
\end{array}\right]
$$

where $S_{i j}=S\left(\bar{E}_{i}, \bar{E}_{j}\right)$ when $i \neq j$, and $S_{i j}=1$ when $i=j$.

# 3.4.3. Calculation of the Weighted Agreement and Relative Agreement of Each Expert 

The weighted agreement degree of each expert's opinion can be calculated by

$$
W A\left(E_{i}\right)=\frac{\sum_{j=1}^{m} w\left(E_{j}\right) \cdot S\left(\bar{E}_{i}, \bar{E}_{j}\right)}{\sum_{j \neq i}^{m} w\left(E_{j}\right)}, i=1,2, \ldots, m
$$

where $E_{i}(i=1,2, \ldots, m)$ is the $i$ th expert, and then the relative agreement degree of each expert can be obtained by

$$
\operatorname{RAD}\left(E_{i}\right)=\frac{W A\left(E_{i}\right)}{\sum_{i=1}^{m} W A\left(E_{i}\right)}, i=1,2, \ldots, m
$$

### 3.4.4. Calculation of the Consensus Degree Coefficient of Experts and Aggregation of the Opinions

Since the relative importance of experts is variable, each expert has their own weight coefficient $w_{i}$. The consensus degree coefficient $\left(C D C_{i}\right)$ of the $i$ th expert can be considered as

$$
C D C_{i}=\beta \cdot w_{i}+(1-\beta) \cdot R A D_{i}
$$

where $\beta(0<\beta<1)$ is defined as the relaxation factor, which represents the importance of the average agreement of experts compared to the relative agreement. After that, the $\bar{R}$, which means the result of aggregation, can be confirmed as

$$
\bar{R}=\sum_{i=1}^{n}\left(C D C_{i}(\cdot) \bar{E}_{i}\right)
$$

where $(\cdot)$ is the multiplication operator of the TpIFNs.

### 3.5. Defuzzification of TpIFNs

After the occurrence possibility of each root event expressed as a TpIFN is obtained through TpIFN-SAM, the defuzzification process is required in order to gain the clear value of the possibility, which is called the possibility score (PS). In this work, the centroid method (see Equation (36)) is adopted to perform the defuzzification of a TpIFN $\bar{A}=\left(a, b, c, d ; a^{\prime}, b, c, d^{\prime}\right)$.

$$
P S=\frac{\left(d^{\prime}-a^{\prime}\right)\left(b+c-4 d^{\prime}-4 a^{\prime}\right)+(d-a)(2 a+b+c+2 d)+4\left(d^{\prime 2}-a^{\prime 2}\right)}{4\left(d^{\prime}-a^{\prime}+d-a\right)}
$$

# 3.6. Calculation of Failure Probability of the System through BN 

For the purpose of launching the analysis of the failure probability of the system using the BN, it is essential here to convert the PSs of the root nodes into conventional failure-probability values (FPs). In general, the formula proposed by Onisawa [47] can be adopted to translate PS into FP. However, this approach is not widely applicable due to the distinction in failure-probability classification standards in different industries, as well as the difference in the definition of linguistic scale for the failure probability [48]. Therefore, a corresponding further calculation method is adopted to convert PS into FP, and the formula is as follows [24]:

$$
F P=\left\{\begin{array}{cl}
\frac{1}{10^{K}}, & P S \neq 0 \\
0, & P S=0
\end{array}\right.
$$

where

$$
K=\left\{\begin{array}{l}
-0.72 \ln P S+2.839,0 \leq P S<0.2 \\
-\frac{1}{3} \times(10 P S-14), \quad 0.2 \leq P S \leq 0.8 \\
{\left[\frac{(1-P S)}{P S}\right]^{0.445} \times 3.705,0.8<P S \leq 1}
\end{array}\right.
$$

### 3.7. Sensitivity Analysis (SA) and Critical Importance Analysis (CIA)

Besides calculating the failure probability of a system using BNs, the identification and analysis of critical events affecting the system failure is also an important task in failure assessment. However, the results may be inaccurate if merely relying on prior or posterior probabilities to identify the most critical events. Therefore, this work presents several analysis methods, such as the ratio of variation (RoV), sensitivity analysis (SA), and criticality-importance analysis. RoV is used to measure the degree of the effect of root events in terms of system failure, and it can be calculated by [24]

$$
\operatorname{RoV}\left(X_{i}\right)=\frac{\varphi\left(X_{i}\right)-\phi\left(X_{i}\right)}{\phi\left(X_{i}\right)}
$$

where $\varphi\left(X_{i}\right)$ and $\phi\left(X_{i}\right)$ indicate the posterior and prior probability of the $i$ th event, respectively.
SA can provide a great degree of help in verifying the probabilistic parameters of BN. This is achieved by researching the influence of tiny changes in numerical parameters on the posterior probability. Highly sensitive parameters have a more significant effect on reasoning results. The sensitivity value is the partial derivative of the posterior output result of the hypothesis relative to the likelihood of a particular state of the evidence. From a mathematical perspective, for a hypothesis $\theta$ given evidence $e$ as a function of a probabilistic likelihood $x$, the posterior probability $P(\theta \mid e)(x)$ is the sensitivity function $f(x)$ of $x$. The sensitivity function is as follows [49]:

$$
f(x)=P(\theta \mid e)(x)=\frac{P\left(\theta^{*} e\right)(x)}{P(e)(e)}=\frac{J \cdot x+K}{M \cdot x+N}
$$

where the coefficients $J, K, M$, and $N$ originate from the original (unvaried) parameters of the BN.

The absolute value of the first derivative of the sensitivity function at the originallikelihood value can be used to express the sensitivity of the likelihood value, which can be represented by the $S V$ (sensitivity value),

$$
S V=\left|\frac{J \cdot N-K \cdot M}{(M \cdot x+N)^{2}}\right|
$$

The influence of the root events can also calculate the criticality importance of the roots in a fault-tree framework [29].

$$
\begin{gathered}
I^{C R}(i \mid t)=\frac{I^{P}(i \mid t) P_{i}(t)}{Q_{0}(t)} \\
I^{P}(i \mid t)=\frac{\partial Q_{0}(t)}{\partial P_{i}(t)}=Q_{0}\left(1_{i}, t\right)-Q_{0}\left(0_{i}, t\right)
\end{gathered}
$$

where $I^{C R}(i \mid t)$ is the criticality importance of the $i$ th root event when time $t$ is reached. $P_{i}(t)$ and $Q_{0}(t)$ are the probabilities when the $i$ th event and the top event occur, respectively. $Q_{0}\left(0_{i}, t\right)$ is the probability of the top event when the non-occurrence of the $i$ th root event is known, and $Q_{0}\left(1_{i}, t\right)$ is the probability of top event when the occurrence of $i$ th root event is known.

# 4. Application for Failure Assessment of a Coal Gasifier 

This section demonstrates the specific analysis process of the proposed method by taking a coal gasifier as an example. Figure 6 shows the process of the coal-gasification system. Firstly, the coal-water slurry is broken up, atomized, and sprayed into the gasifier under the action of a high-speed oxygen stream passing through the nozzle. The oxygen and the atomized water-coal slurry are subjected to high temperatures in the gasifier and then rapidly undergo a series of complex processes such as preheating, water evaporation, coal dry distillation, volatile pyrolysis combustion, and carbon gasification to produce wet gas with $\mathrm{CO}, \mathrm{H}_{2}, \mathrm{CO}_{2}$, and water vapor as the main components. Finally, the wet gas, slag, and unreacted carbon leave the reaction zone together and enter the cooling chamber. The molten slag is trapped in the water, falls into the slag tank, and is discharged periodically via the slag-discharge system, whereas the gas and saturated steam go to the next treatment system. In this system the gasifier is the central piece of equipment for the realization of the gasification process.
![img-5.jpeg](img-5.jpeg)

Figure 6. Flow chart of the coal-gasification system.

### 4.1. Construction of the BN for Analyzing the Failure Risk of the Gasifier

Based on the experts' suggestions and relevant literature, the FT of the gasifier was instituted. The failure of the gasifier was set as the top event, and it was primarily leaded by the abnormality of gasifier, equipment-corrosion, and human organization factors. Further analysis was executed due to the above sub-top events till all possible root events were considered. The FT of the gasifier and the corresponding event symbols in the FT are shown in Figure 7 and Table 4. The FT of the gasifier was then converted into the corresponding BN through the method presented in Section 2.5. The CPTs were determined for all the intermediate nodes according to the logic-gate rules and the BN model illustrated in Figure 8.

![img-6.jpeg](img-6.jpeg)

Figure 7. The fault-tree model of the coal gasifier.

Table 4. Description of the events in the fault tree of the coal gasifier.


![img-7.jpeg](img-7.jpeg)

Figure 8. The Bayesian network for the failure of the gasifier mapped from FT.

# 4.2. Collection of Experts' Opinions on the Failure of the Coal Gasifier

### 4.2.1. Definition of the TpIFN-Probabilistic Linguistic Scales

Based on experts' opinions and relevant literature, this study classified the failure probability of gasifiers into seven levels. Each level corresponds to a range of values for the failure probability of the gasifier, as Table 5 shows.

Table 5. Failure-probability rating of the coal gasifier.


In linguistic terms, intuitionistic fuzzy membership functions come in many forms to address the uncertainty and inaccuracy of expert judgments. Triangular and trapezoidal intuitionistic fuzzy membership functions are more efficient for risk analysis. Still, a triangle is a particular case of a trapezoid. Therefore, in this study, the membership and non-membership functions of TpIFNs were used to quantitate the probability of gasifier-failure-accident risk. Seven sets of TpIFNs were determined according to the given probability interval in the gasifier-failure-accident risk. Transformation of linguistic variables into corresponding TpIFNs was carried out by mapping relationship of trapezoidal intuitionistic fuzzy sets. The trapezoidal intuitionistic fuzzy sets produced the qualitive failure probabilities of risk events to quantify, as Table 6 shows. The membership and non-membership function curves of TpIFNs matching with seven linguistic variables are illustrated in Figure 9.

Table 6. Trapezoidal intuitionistic fuzzy number corresponding to failure possibility.


![img-8.jpeg](img-8.jpeg)

Figure 9. Membership and non-membership functions of probabilistic-language scales.

# 4.2.2. Expert's Opinions on Root Events of the BN 

Four experts with different professional backgrounds were selected to establish an expert group. To match up to the failure-probability ratings mentioned in Table 5, a sevenlevel linguistic-term set (QL, LO, OL, MO, OH, HI, QH) was used to express the experts' opinions on the occurrence possibility of each root event in the BN. Table 7 shows the experts' judgments of all root nodes.

Table 7. Experts' opinions on root events of the BN for the gasifier failure.


4.3. Aggregation of the TplFNs for Describing the Failure Probabilities of the Root Nodes
4.3.1. Calculation of the Experts' Weights

The IF-AHP method mentioned above was used for the computation of the experts' weights. The personal information of the experts is shown in Table 8.

Table 8. Basic information of the experts.


The judgment matrix for the three indices of professional position $\left(\mathrm{C}_{1}\right)$, education level $\left(\mathrm{C}_{2}\right)$, and service time $\left(\mathrm{C}_{3}\right)$ is shown in Table 9. The expert group's intuitionistic-preference relationships for $\mathrm{C}_{1}-\mathrm{C}_{3}$ are shown in Tables 10-12.

Table 9. The intuitionistic-preference relationship for the three indices $\left(\mathrm{C}_{1}-\mathrm{C}_{3}\right)$.


Table 10. The expert group's intuitionistic-preference relationship for professional position $\left(\mathrm{C}_{1}\right)$.


Table 11. The expert group's intuitionistic-preference relationship for education level $\left(\mathrm{C}_{2}\right)$.


Table 12. The expert group's intuitionistic-preference relationship for service time $\left(\mathrm{C}_{3}\right)$.


A consistency check of the preference relationships was then performed according to Equations (22) and (23). An example illustrated the consistency-test process of the intuitionistic preference relation $R$.

Through Equations (20) and (21), the intuitionistic fuzzy consistency judgment matrix $\bar{R}=\left(\bar{r}_{i j}\right)_{n \times n}$ was calculated according to $R$.

$$
\bar{R}=\left(\begin{array}{ccc}
(0.5,0.5) & (0.7,0.2) & (0.368,0.273) \\
(0.2,0.7) & (0.5,0.5) & (0.2,0.6) \\
(0.273,0.368) & (0.6,0.2) & (0.5,0.5)
\end{array}\right)
$$

Take $\bar{r}_{13}$ as an example:

$$
\begin{gathered}
\bar{\mu}_{13}=\frac{\mu_{12} \cdot \mu_{23}}{\mu_{12} \cdot \mu_{23}+\left(1-\mu_{12}\right)\left(1-\mu_{23}\right)}=\frac{0.7 \times 0.2}{0.7 \times 0.2+0.3 \times 0.8}=0.368 \\
\bar{v}_{13}=\frac{v_{12} \cdot v_{23}}{v_{12} \cdot v_{23}+\left(1-v_{12}\right)\left(1-v_{23}\right)}=\frac{0.2 \times 0.6}{0.2 \times 0.6+0.8 \times 0.4}=0.273
\end{gathered}
$$

The distance between $R$ and $\bar{R}$ calculated by Equation (19) was $d(\bar{R}, R)=0.232>$ 0.1 , indicating that the consistency check failed. We had to adjust the parameters with Equations (22) and (23) until the consistency test was passed. The fused intuitionistic preference relation $\widetilde{R}$ was obtained.

$$
\widetilde{R}=\left(\begin{array}{ccc}
(0.5,0.5) & (0.7,0.2) & (0.413,0.258) \\
(0.2,0.7) & (0.5,0.5) & (0.2,0.6) \\
(0.258,0.413) & (0.6,0.2) & (0.5,0.5)
\end{array}\right)
$$

where $\sigma=0.8$. According to Equation (24), the distance between $\widetilde{R}$ and $R d(\widetilde{R}, R)=0.0935<0.1$, and the consistency check was passed. The consistency checks for the intuitionistic-preference relationships $R_{i}(i=1,2,3)$ were also conducted according to the same process.

Next, the priority of each consistent intuitionistic-preference relationship was derived. For example, the priority vector of the $\vec{R}$ was calculated as $\varepsilon_{1}=(0.315,0.602), \varepsilon_{2}=(0.176$, 0.602 ), and $\varepsilon_{3}=(0.265,0.632)$ with Equation (25). Subsequently, all prioritization vectors were aggregated. Take $W_{1}$ as an example:

$$
\begin{gathered}
W_{1}=\sum_{j=1}^{4}\left(\varepsilon_{j} \times \varepsilon_{1 j}\right) \\
=(0.315,0.602) \times(0.284,0.622)+(0.176,0.602) \times(0.256,0.6)+(0.265,0.632) \times(0.223 \\
0.591) \\
=(0.182,0.607)
\end{gathered}
$$

Table 13 shows the aggregated intuitionistic fuzzy priority of $C_{i}$.
Table 13. The aggregated intuitionistic fuzzy priority of $C_{i}$.


Per Equations (28) and (29), $S\left(W_{1}\right)=1-\frac{\left(1+\pi_{W_{1}}\right)\left(1-\mu_{W_{1}}\right)}{\Sigma}=0.502$. Similarly, $S\left(W_{2}\right)=0.478$, and $S\left(W_{3}\right)=0.486, S\left(W_{4}\right)=0.484$. After normalization, the experts' weights were finally obtained: $w=\left(w_{1}, w_{2}, w_{3}, w_{4}\right)=(0.257,0.245,0.250,0.248)$.

# 4.3.2. Aggregation of the Experts' Opinions 

After obtaining the experts' weights and the TpIFNs were converted from the experts' opinions on the occurrence possibilities of the events, the proposed TpIFN-SAM was used to aggregate the opinions. To elaborate the specific process of the TpIFN-SAM, the root node $\mathrm{X}_{18}$ was treated as an example, and the calculation process is shown in Table 14.

Table 14. Detailed aggregation and FP calculation process of the node $\mathrm{X}_{18}$.


Table 14. Cont.


# 4.4. TpIFN-Defuzzification

### 4.4.1. Conversion of the TpIFNs into PSs

The aggregated results obtained by the TpIFN-SAM were still TpIFNs, so TpIFN Defuzzification was performed by Equation (36) to further convert the TpIFNs into PSs with crisp values.

### 4.4.2. Determination of the FPs of All Root Nodes

The PSs of the root nodes were not probability values. In order to implement probabilistic inference with the BN, the PSs were further converted into FPs according to Equations (37) and (38). Table 15 shows all root nodes of the FPs.

Table 15. The aggregated expert opinions and the corresponding failure probabilities of the root events in the BN.


Table 15. Cont.


# 4.5. BN Analysis 

### 4.5.1. Prediction of the Failure Probability of the Gasifier

Before the BN performs forward prediction, it is necessary to obtain the CPT of each relevant node. Each CPT in this case was obtained by expert evaluation. Table 16 shows the CPT of the intermediate node $\mathrm{I}_{1}$. The rest of the CPTs can be found in Appendix B.

Table 16. The CPT of event $\mathrm{I}_{1}$ in the BN model (Occ: occurred; Non: non-occurred).


The GeNIe software was used to analyze the established BN model of the coal gasifier. Figure 10 shows the prior probability of the failure of the gasifier through the forward

inference of the BN. The failure probability of the gasifier $\left(F P_{\mathrm{T}}\right)$ was 0.036 . To contrast the variations between the FT and the BN, the $F P_{\mathrm{T}}$ was also calculated through FT analysis, and the results show that the $F P_{\mathrm{T}}$ in the FT was 0.013 , which is nearly three times higher than that in the BN. This is because the BN takes into account the conditional dependencies between events and can more objectively report the features of the system.
![img-9.jpeg](img-9.jpeg)

Figure 10. The prior probability of each node in the BN of the coal gasifier.

# 4.5.2. Diagnosis of the Key Nodes for the Failure of the Coal Gasifier 

The backward inference of the BN was executed to update the occurrence probabilities of the root nodes to assess the extent to which the root nodes affect the failure of the gasifier. Figure 11 shows the posterior probability of each root node $P\left(\mathrm{X}_{i}=\right.$ Occur $\mid T=$ Occur) obtained by backward inference of the BN. In the case that the leaf node must occur, the posterior probability of the root nodes $\mathrm{X}_{20}$ (High $\mathrm{H}_{2} \mathrm{O}$ content), $\mathrm{X}_{22}$ (Anti-corrosion layer damaged), and $\mathrm{X}_{23}$ (Insulation layer damaged) are the most worrying ones. Therefore, the key nodes can be preliminarily determined.
![img-10.jpeg](img-10.jpeg)

Figure 11. The posterior probability of each node in the BN of the coal gasifier.

By comparing the prior and the posterior probability regarding each root node, as shown in Figure 12, the root nodes with large changes in occurrence probability can be obtained as $\mathrm{X}_{22}$ (Anti-corrosion layer damaged), $\mathrm{X}_{23}$ (Insulation layer damaged) and $\mathrm{X}_{25}$ (Improper operation), indicating that these three root events have a large contribution to the failure probability of the gasifier. The acquisition of the prior and the posterior probability shows the forward-inference (prediction) ability and backward-inference (diagnosis) ability of the BN, respectively, which completely reflects the superiority of the BN's bidirectionalinference ability. Meanwhile, this ability can be used to provide preliminary judgments and lay the foundation for subsequent analysis and determination of key nodes.
![img-11.jpeg](img-11.jpeg)

Figure 12. Prior and posterior probabilities of root nodes of the BN model.

# 4.5.3. SA and CIA 

The RoV of each root node was calculated with Equation (39). Figure 13 displays the calculation results of the importance of all basic events. The top six key root nodes were $\mathrm{X}_{25}$ (Improper operation), $\mathrm{X}_{24}$ (Pre-job training is not up to standard), $\mathrm{X}_{26}$ (Unattended/unsafe supervision), $\mathrm{X}_{27}$ (Deliberately damaged), $\mathrm{X}_{23}$ (Insulation layer damaged), and $\mathrm{X}_{21}$ (High flow rate).
![img-12.jpeg](img-12.jpeg)

Figure 13. RoV of the root node probability using the BN model for the coal gasifier.
For the purpose of further elucidating the devotion of all root nodes to the occurrence of accidents and identify the critical factors, SA and CIA were performed. Figure 14 shows the sensitivity value and the critical importance of each root node. For the BN, $\mathrm{X}_{25}$ (Improper operation), $\mathrm{X}_{24}$ (Pre-job training is not up to standard), $\mathrm{X}_{26}$ (Unattended/unsafe supervision), $\mathrm{X}_{27}$ (Deliberately damaged), $\mathrm{X}_{23}$ (Insulation layer damaged), and $\mathrm{X}_{22}$ (Anticorrosion layer damaged) were the top six key events for the gasifier failure. For the FT, the top six key factors included $\mathrm{X}_{22}$ (Anti-corrosion layer damaged), $\mathrm{X}_{23}$ (Insulation layer

damaged), $\mathrm{X}_{13}, \mathrm{X}_{17}$ (Temperature sensor damaged), $\mathrm{X}_{25}$ (Improper operation), and $\mathrm{X}_{21}$ (High flow rate). The results obtained by the two methods are discrepant. The reason for this is that the BN still considered conditional dependencies between events, whereas the FT did not capture them.
![img-13.jpeg](img-13.jpeg)

Figure 14. Comparison of sensitivity value and critical importance of the root nodes of the BN model for the coal gasifier.

From the results of the SA and CIA, it can be found that $\mathrm{X}_{25}$ (Improper operation) was considered the most critical factor on the failure of the coal gasifier. In addition, damage to anti-corrosion measures $\left(\mathrm{X}_{22}\right.$ and $\left.\mathrm{X}_{23}\right)$ was also a very important influencing factor. Therefore, more attention should be allocated to the management and training of operators, and special attention should be paid to regular inspection of the integrity of insulation and anti-corrosion layers to minimize the failure of the gasifier.

# 5. Conclusions 

In this study, a new integration framework was proposed to assess the failure risk of the process system. The improvements of this method compared with the previous method are as follows:

1. This framework combined the Bayesian network with the TpIFN-SAM to provide an alternative strategy for obtaining the prior probabilities of the root events in BNs.
2. A set of TpIFNs was defined to quantify the linguistic terms for describing the failure possibilities of the events in BNs, which are more general and expressive than TpIFNs.
3. The TpIFN-SAM can effectively aggregate the expert opinions on the prior probabilities of the root events in BNs and reduce the uncertain cumulative effect of the aggregation process by taking the effect of individual discrepancies into account for the consistency. The bidirectional reasoning of the BN coupled with sensitivity analysis can accurately calculate the system-failure probability and identify the key influencing factors that may lead to accidents.
Limitations also exist in this work. The basic probabilities of the root events in the BN were assumed to be constant in the proposed framework, but in many cases they are time dependent. Therefore, developing a BN approach for dynamic systems will be covered in future research work.

Author Contributions: Data curation, Q.L.; Software, Q.L.; Formal analysis, D.L.; Investigation, Y.Y.; Methodology, Y.L. and S.W.; Resources, Y.D. and W.W.; Writing-original draft, Y.L.; Writingreview and editing, Y.L. and W.W. All authors have read and agreed to the published version of the manuscript.
Funding: This research was funded by National Natural Science Foundation of China (No. 51605368) and Scientific Research Project of Shaanxi Provincial Department of Education (No. 20JK0944).

Data Availability Statement: Not applicable.
Acknowledgments: We appreciate the National Nature Science Foundation of China and the Northwest University.
Conflicts of Interest: The authors declare no conflict of interest.

# Appendix A 

If $E V(\widetilde{A})$ satisfies the following five fundamental theorems, then prove that $E V(\widetilde{A})$ is workable.

$$
\begin{gathered}
E V(k \widetilde{A})=k E V(\widetilde{A}) \\
E V(\widetilde{A}+\widetilde{C})=E V(\widetilde{A})+E V(\widetilde{C})
\end{gathered}
$$

If $b_{1}=a_{1}, b_{4}=a_{4}$, then

$$
E V(\widetilde{A})=\frac{a_{1}+a_{2}+a_{3}+a_{4}}{4}
$$

If $a_{2}-a_{1}=a_{4}-a_{3}, a_{2}-b_{1}=b_{4}-a_{3}$, then

$$
\begin{gathered}
E V(\widetilde{A})=\frac{a_{2}+a_{3}}{2} \\
E V(\lambda)=\lambda
\end{gathered}
$$

## Proof

A. When $k=0$, empty.
B. When $k>0$, let $\widetilde{A}=\left(a_{1}, a_{2}, a_{3}, a_{4} ; b_{1}, a_{2}, a_{3}, b_{4}\right)$ be a trapezoidal intuitionistic fuzzy number, and $k$ is a real number, which we can know by Definition 2:

$$
k \widetilde{A}=k\left(a_{1}, a_{2}, a_{3}, a_{4} ; b_{1}, a_{2}, a_{3}, b_{4}\right)=\left(k a_{1}, k a_{2}, k a_{3}, k a_{4} ; k b_{1}, k a_{2}, k a_{3}, k b_{4}\right)
$$

The expected value of $k \widetilde{A}$ is

$$
E V(k \widetilde{A})=\frac{k a_{1}+k b_{1}+2 k a_{2}+2 k a_{3}+k a_{4}+k b_{4}}{8}=k \cdot \frac{a_{1}+b_{1}+2 a_{2}+2 a_{3}+a_{4}+b_{4}}{8}=k \cdot E V(\widetilde{A})
$$

C. When $k<0$, same result as B. $\square$

Proof: Let $\widetilde{A}=\left(a_{1}, a_{2}, a_{3}, a_{4} ; b_{1}, a_{2}, a_{3}, b_{4}\right), \widetilde{C}=\left(c_{1}, c_{2}, c_{3}, c_{4} ; d_{1}, c_{2}, c_{3}, d_{4}\right)$ be two trapezoidal intuitionistic fuzzy numbers, which can be known by Definition 5:

$$
\widetilde{A}+\widetilde{C}=\left(a_{1}+c_{1}, a_{2}+c_{2}, a_{3}+c_{3}, a_{4}+c_{4} ; b_{1}+d_{1}, a_{2}+c_{2}, a_{3}+c_{3}, b_{4}+d_{4}\right)
$$

The expected value of $\widetilde{A}+\widetilde{C}$ is

$$
\begin{gathered}
E V(\widetilde{A}+\widetilde{C})=\left(\frac{\left(a_{1}+c_{1}\right)+\left(b_{1}+d_{1}\right)+2\left(a_{2}+c_{2}\right)+2\left(a_{3}+c_{3}\right)+\left(a_{4}+c_{4}\right)+\left(b_{4}+d_{4}\right)}{8}\right) \\
=\frac{\left(a_{1}+b_{1}+2 a_{2}+2 a_{3}+a_{4}+b_{4}\right)+\left(c_{1}+d_{1}+2 c_{2}+2 c_{3}+c_{4}+d_{4}\right)}{8} \\
=\frac{a_{1}+b_{1}+2 a_{2}+2 a_{3}+a_{4}+b_{4}}{8}+\frac{c_{1}+d_{1}+2 c_{2}+2 c_{3}+c_{4}+d_{4}}{8} \\
=E V(\widetilde{A})+E V(\widetilde{C})
\end{gathered}
$$

Proof: Let $\tilde{A}=\left(a_{1}, a_{2}, a_{3}, a_{4} ; b_{1}, a_{2}, a_{3}, b_{4}\right)$ be a set of trapezoidal intuitionistic fuzzy numbers; if $b_{1}=a_{1}$ and $b_{4}=a_{4}$, then

$$
E V(\tilde{A})=\frac{a_{1}+b_{1}+2 a_{2}+2 a_{3}+a_{4}+b_{4}}{8}=\frac{a_{1}+a_{2}+a_{3}+a_{4}}{4}
$$

Proof: By $E V(\tilde{A})=\frac{a_{1}+b_{1}+2 a_{2}+2 a_{3}+a_{4}+b_{4}}{8}$, if $\left(a_{2}-a_{1}=a_{4}-a_{3}\right) \rightarrow\left(a_{2}+a_{3}=a_{1}+a_{4}\right)$ and $\left(a_{2}-b_{1}=b_{4}-a_{3}\right) \rightarrow\left(a_{2}+a_{3}=b_{1}+b_{4}\right)$,

$$
E V(\tilde{A})=\frac{a_{2}+a_{3}}{2}
$$

Proof: Let $\lambda$ be a real number, then $\lambda=(\lambda, \lambda, \lambda, \lambda ; \lambda, \lambda, \lambda, \lambda)$, and

$$
E V(\lambda)=\left(\frac{\lambda+\lambda+2 \lambda+2 \lambda+\lambda+\lambda}{8}\right)=\lambda
$$

Specially, if $\lambda=0$, then $E V(\lambda)=E V(0)=0$.
The above five theorems are proven, so $E V(\tilde{A})$ is workable.

# Appendix B 

Table A1. The CPT of event $\mathrm{I}_{2}$ (Abnormal liquid level; Occ: occurred; Non: non-occurred).


Table A2. The CPT of event $\mathrm{I}_{3}$ (Abnormal temperature; Occ: occurred; Non: non-occurred).


Table A3. The CPT of event $\mathrm{I}_{4}$ (Too-high temperature; Occ: occurred; Non: non-occurred).


Table A4. The CPT of event $\mathrm{I}_{5}$ (Too-low temperature; Occ: occurred; Non: non-occurred).


Table A5. The CPT of event $\mathrm{I}_{6}$ (Internal corrosion; Occ: occurred; Non: non-occurred).


Table A6. The CPT of event $\mathrm{I}_{7}$ (Medium content; Occ: occurred; Non: non-occurred).


Table A7. The CPT of event $\mathrm{I}_{8}$ (External corrosion; Occ: occurred; Non: non-occurred).


Table A8. The CPT of event $\mathrm{I}_{2}$ (Unintentional destruction; Occ: occurred; Non: non-occurred).


Table A9. The CPT of event $\mathrm{T}_{1}$ (Gasifier abnormality; Occ: occurred; Non: non-occurred).


Table A10. The CPT of event $\mathrm{T}_{2}$ (Corrosion failure; Occ: occurred; Non: non-occurred).


Table A11. The CPT of event $\mathrm{T}_{3}$ (Human-organization factors; Occ: occurred; Non: non-occurred).


Table A12. The CPT of event T (Gasifier failure; Occ: occurred; Non: non-occurred).

