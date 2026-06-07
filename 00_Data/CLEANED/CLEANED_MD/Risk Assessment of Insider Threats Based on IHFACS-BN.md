# Article 

## Risk Assessment of Insider Threats Based on IHFACS-BN

Min Zeng ${ }^{\dagger}$, Chuanzhou Dian ${ }^{\dagger}$ and Yaoyao Wei *<br>School of Economics, Management and Law, University of South China, Hengyang 421001, China<br>* Correspondence: 2014002159@usc.edu.cn; Tel.: +86-181-6388-6283<br>+ These authors contributed equally to this work.


#### Abstract

Insider threats, as one of the pressing challenges that threaten an organization's information assets, usually result in considerable losses to the business. It is necessary to explore the key human factors that enterprise information security management should focus on preventing to reduce the probability of insider threats effectively. This paper first puts forward the improved Human Factors Analysis and Classification System (IHFACS) based on actual enterprise management. Then, the enterprise internal threat risk assessment model is constructed using the Bayesian network, expert evaluation, and fuzzy set theory. Forty-three classic insider threat cases from China, the United States, and Israel during 2009-2021 are selected as samples. Then, reasoning and sensitivity analysis recognizes the top 10 most critical human factors of the accident and the most likely causal chain of unsafe acts. The result shows that the most unsafe behavior was not assessing employees' familiarity with the company's internal security policies. In addition, improving the organizational impact of information security can effectively reduce internal threats and promote the sustainable development of enterprises.


Keywords: human factors; insider threat; bayesian network; human factor analysis and classification system

## 1. Introduction

With the development of information management technologies, such as the Internet and mobile applications, the information security problems faced by enterprises have become increasingly serious, and information security risks have penetrated into all aspects of enterprise operation and management. alit is well-know that every company has internal sensitive data types, such as business plans, core technology, customer information data, and intellectual property. Therefore, an attack on an organization's primary technical information may result in significant losses. The main sources of security threats for businesses today are insiders with access to sensitive data and systems-both malicious insiders and careless insiders [1]. IBM X-Force Threat Intelligence Index [2] showed that insider attacks were the most common type of cyberattack in 2017, around $60 \%$. The 2020 Insider Threat Report [3] finds that almost all organizations feel vulnerable to insider attacks ( $95 \%$ ), and $68 \%$ feel moderate to highly vulnerable to insider attacks. In addition, there are numerous causes of insider information security incidents, with human factors (HFs) dominating [4].

### 1.1. Insider Threat Definition

What is a definition of an insider threat? First, an insider has been legitimately empowered with the right to access or use organizational assets. Assets may involve privileged accounts, core technical data, and other sensitive information. Alternatively, as commonly stated, an insider includes an employee (current or former), trusted business partner, or subcontractor [5]. Additionally, an insider threat was defined as: "intentional or unintentional activities by an insider cause damage to the organization's assets and/or negatively affect

the confidentiality, integrity, or availability of the organization's information or information systems [6]."

# 1.2. Insider Threat Incidents 

Malicious or unintentional actions by insiders can cause equal harm to their organizations, leaking and deleting confidential internal data, or even giving external attackers an opportunity. Recently, a few internal accidents caused the company substantial financial loss and operational risk, which have aroused widespread concern. For example, an insider attack accident happened in a company at JD on 18 June 2021. This accident was caused by an intern programmer who maliciously deleted the project R\&D database, causing delays in the project. In September 2017, a Wells Fargo employee mistakenly sent an email that compromised the information of 50,000 customers due to carelessness [7]. The Bank of Bahrain went bankrupt after a serious internal security incident caused by an employee error that resulted in a loss of $\$ 1.4$ billion [8]. It can be seen from these examples that there are two main types of insider threats: intentional and malicious insider threats. The "unintentional insider threats" of human negligence and inadequate preparation, often the least detectable types of insider threats, may pose a more serious risk than the former [9]. In short, insider threats are essentially related to "human" factors [10]. The prevention and control of HFs can have a beneficial effect on decreasing insider threats in the enterprise.

This study aims to construct a human-causal analysis model of insider threats in an organization to gain insight into the various insecure behaviors and their influencing factors that lead to information security incidents within an organization. This paper will give important references for identifying what make insider threats in organizations happen and how to mitigate them more effectively.

The remainder of this paper is organized as follows: current research on insider threats examines various detection and preventive techniques in Section 2. Section 3 presents a hybrid model that integrates fuzzy set theory (FST), expert judgment, and an improved Human Factors Analysis and Classification System (IHFACS) into Bayesian networks (BN), called IHFACS-BN. Section 4 presents the application of the hybrid model in analyzing the key HFs that lead to insider threats in the enterprise and provides constructive comments based on the model's inference results. Section 5 concludes the research and advises future studies. Finally, future work is presented in Section 6. Figure 1 depicts the organizational structure of this article.
![img-0.jpeg](img-0.jpeg)

Figure 1. Article outline.

# 2. Related Work 

In recent years, the academic community has paid considerable attention to insider threats, and experts and scholars have proposed different solutions for insider threats in network information security. These methods can be separated into two primary categories: detection and prevention.

### 2.1. Detection Methods

Insider threat detection approaches are mainly technical and non-technical. Traditional insider threat detection techniques rely primarily on machine learning [11], user commands [12], and biometrics [13], with security events, such as Trojans and viruses, serving as the primary detection objects. With the diversification of insider attackers and attack methods, traditional threat detection techniques have long failed to meet the demand. Insider threat discovery methods are primarily used to detect insider threats through the finding of behavioral traces of insider users and constructing related insider user behavior models. As a result, current insider threat detection approaches are based on aberrant behavior and formal modeling [14].

The anomaly-based threat detection method mainly relies on big data and artificial intelligence technology to classify how users behave, then determine if there is any abnormal behavior that could be an insider threat. The approach may efficiently detect threats posed by unidentified patterns. Currently, it is the most used way. Lane et al. devised two methods based on instance learning and the hidden Markov model to solve this problem. The goal was to create a model of how system users typically work and find abnormal conditions as long-term deviations from expected behavior patterns. Both methods can identify anomalies well enough for low-level "focus of attention" detectors in multi-layer security systems, but they are not good enough for comprehensive security solutions [15]. Happa et al. modeled normal employee behavior using Gaussian mixture models with likelihood and criterion scores as anomaly detection metrics and incorporated pertinent expert knowledge, thereby improving the detection accuracy [16]. With the development of neural networks, deep learning techniques for analyzing the behavior of users and entities have become widespread for detecting insider threats. Zhang et al. proposed an insider threat detection model based on LSTM-Attention that takes full advantage of the LSTM (Long Short-term Memory) network and Attention to handle long sequences but also considers the unique characteristics of insiders [17]. Haq et al. developed two DL (Deep Learning) hybrid LSTM models integrated with Word2vec LSTM GLoVe (Global Vectors for Word Representation) LSTM and compared the performance of these models to detect insider threats with state-of-the-art ML (Machine Learning) models. It was found that ML-based models outperformed the DL-based ones [18]. Several studies have also begun to apply Feedforward Neural Networks [19] and Recurrent Neural Networks [20] to develop a new automatic anomaly detection method.

Insider threat detection methods based on anomalous behavior rely heavily on the accuracy and comprehensiveness of data acquisition and require a large amount of existing insider behavior data, which limits them. Applying non-technical detection methods (e.g., psychological, sociological) is also beneficial for reducing insider threats when there are few or no sample data available. However, the former can determine users' psychological states from their network or host use, and the latter can infer malicious motives from their social performance [21].

### 2.2. Prevention Methods

We found that most research has focused on using technology to "detect" threats rather than "prevent" them, so most enterprise cybersecurity programs tend to take a "detection-centric" approach to protection. The approaches for detecting insider threats described in the preceding section suffer from some drawbacks: they are inefficient and take a long time to discover and detect. Some research is theoretical and cannot be applied universally within organizations. Moreover, the primary limitation of a detection-centric

approach to security is that it is inherently reactive, acting only on threats that have been identified. A prevention-centric approach tries to stop insider attacks before they happen. As many cybersecurity threats result from human error or a lack of awareness, Rajamäki et al. proposed a proactive and resilient education framework to develop corresponding cybersecurity education and training programs for different categories of employees [22]. Chowdhury et al. [23] proposed a framework for enterprise network security training based on learning theory and the Delphi method.

When security technology cannot protect an organization from insider threats, the human element is usually the weakest link in the information security chain [24]. The current situation in enterprise security preparedness is that the human element is usually the most vulnerable part of the information security chain when the use of security technology fails to protect the organization from insider threats. Thus, human factors are receiving increasing attention. Although frameworks and assessment models for insider threats containing HFs have been proposed in the literature, they lack systematicity and relevance.

Effective accident prevention requires incorporating HFs into accident analysis models [25,26]. This study uses the HFACS model [27], which Shapell and Wiegmann developed to study HFs in accidents based on the Swiss cheese model by analyzing a large amount of aviation accident data. Due to its effective evaluation framework, content integrity, and practicability, the model has been applied in different fields, such as coal mines, maritime transport, and laboratory explosions [28,29,30]. Considering that insider threats are distinct from general safety incidents, this paper proposes an IHFACS framework for insider threat assessment items, adapted from the frameworks in the "Related Studies" section. At the same time, a hybrid model for insider threat HFs analysis is constructed based on BN. The hybrid model is then used to identify high-frequency human causes of insider threats and the causal relationships among HFs at each level to provide a reference for preventing insider threats and further reducing hazards and losses. The main novelties of this study are summarized as follows:

- An IHFACS framework is proposed to be applied to the HFs analysis of insider enterprise threats.
- An IHFACS-BN model is used to assess the risk of insecure behavior within the enterprise.
- HFACS, expert knowledge, the triangular fuzzy number estimation probability method, the Noisy-OR gate model, and BN are integrated into this model.
- BN-based reasoning identifies key risk factors and the interdependence of HFs at different and the same levels.
- Compared with traditional accident analysis methods, this method focuses more on the explicit and implicit correlations between HFs.


# 3. Material and Methods 

This section outlines the methodology used to develop the IHFACS-BN model. The model was developed using the HFACS framework, expert assessment method, triangular fuzzy number estimation probability method, and BN to comprehensively identify the risk factors of inside-the-business threats. To achieve better analysis results, the hybrid model combines qualitative and quantitative analysis methods.

### 3.1. IHFACS

It is well known that HFACS is a widespread and popular framework for human error analysis [28]. According to the HFACS model, "primary causes cause accidents, and potential causes cause primary causes," where the primary causes are analyzed at four levels: "unsafe human behavior, potential factors refer to the preconditions of unsafe behavior, unsafe supervision, and organizational influence" [31]. Figure 2 [31] shows that the primary causes are analyzed at four levels: "unsafe human behavior; potential factors referring to the preconditions of unsafe behavior; unsafe supervision; and organizational influence."

The HFACS model is highly flexible and adaptable to industry-specific characteristics [32]. In this paper, we examined the literature on insider threat, investigated the current state of information security management in enterprises, and conducted a thorough examination of insider threat survey reports. We found that insider threats are high-risk, hidden, and multiple; the types of enterprises, security management policies, and employee quality vary. It makes the risk transmission process strongly coupled, ambiguous, and dynamic. Therefore, the HFs classification of the original HFACS framework is not fully applicable to insider enterprise threats. For example, the original HFACS framework focuses on the lack of inadequate supervision of crew members in aviation accidents at the unsafe supervision level, while enterprise network security protection uses computer technology to monitor user behavior characteristics in real time. In light of the preceding, this paper revises some of the HFs of the HFACS model by collecting and analyzing data on security incidents and referencing relevant studies. In addition, experts in this field hold a safety meeting to investigate the root of incidents and briefly describe the HFs professionally. Finally, the IHFACS model for insider threat analysis in enterprises is developed.

![img-1.jpeg](img-1.jpeg)

Figure 2. HFACS framework.

# 3.2. Fuzzy Bayesian Network (FBN) 

### 3.2.1. Fuzzy Theory and Expert Elicitation

It is well known that, as a scientific consensus, the expert judgment method can be utilized to judge the identified HFs significantly. Analytic Hierarchy Process (AHP) has a strong ability to deal with complex decision-making problems [33,34,35]. However, because of the subjectivity of qualitative criteria, experts are commonly reluctant to express their opinions clearly and intuitively. Due to this, Laarhoven proposed this method, using fuzzy triangular numbers to calculate [36], and extended the AHP. A combination of FST and subjective opinion help raters more effectively estimate the impact rate of identified each HF $[28,35]$.

In fuzzy judgment, the expert language is quantified as TFN by the affiliation degree function. According to the definition of fuzzy number, the adopted TFN is denoted as $A=(a, m, b)$, and the affiliation degree function of TFN [35] can be expressed as follows:

$$
\mu \mathrm{A}(\mathrm{x})=\left\{\begin{array}{cc}
(\mathrm{x}-\mathrm{a}) /(\mathrm{m}-\mathrm{a}) & \mathrm{a} \leq \mathrm{x} \leq \mathrm{m} \\
(\mathrm{~b}-\mathrm{x}) /(\mathrm{b}-\mathrm{m}) & \mathrm{m} \leq \mathrm{x} \leq \mathrm{b} \\
0 & \text { otherwise }
\end{array}\right.
$$

In Formula (1), A denotes the fuzzy set on the specified universe $\mathrm{x}, \mu_{\mathrm{A}}(\mathrm{x})$ denotes the membership function of $x$ to the fuzzy set $A$, and $m$ denotes the mean value of the fuzzy number A , where a and b denote the upper and lower bounds of TFNs. In fuzzy judgment, the membership function is used to convert the qualitative linguistic expression of experts into fuzzy triangular numbers. When making preference judgments for pairs of elements in a group, as in AHP, the number of elements in a set should be limited to seven plus or minus two [37]. As a result, five linguistic variables are introduced: VL, L, M, H, and VH. The judgment results of TFNs are qualitatively described in Table 1.

Table 1. Judgment of triangular fuzzy numbers.


The weight factor is used to represent the quality of experts in order to ensure the reliability of experts' subjective evaluations. The experts' abilities are primarily evaluated based on four aspects $\left(S_{n}, n=1,2,3,4\right)$ : working years, education level, age, and professional positions, combined with the company's internal information security management practices. Depending on the background of the invited experts, the composite score $\mathrm{E}_{\mathrm{i}}$ of the ith expert can be obtained by Equation (2) using the scoring rules in Table 2. Then, the respective weights $\left(\omega_{E}^{i}\right)$ are determined according to the following Formulas (3) for five experts in different enterprise security fields.

$$
\begin{gathered}
E_{i}=S_{1}+S_{2}+S_{3}+S_{4} \\
\omega_{E}^{i}=E_{i} / \sum_{u=1}^{\lambda} E_{i} \quad(\lambda=1,2 \ldots, 5)
\end{gathered}
$$

Table 2. Weighting scores of experts.


After obtaining the corresponding fuzzy numbers for the linguistic variables of the experts, the opinions of different experts are aggregated according to the linear joint prior method, namely:

$$
P_{j}=\sum_{i=1}^{n}\left(q_{i j} \otimes \omega_{E}^{i}\right), \quad j=1,2, \ldots, \lambda
$$

In this formula: $P_{j}$ is the aggregated fuzzy number of nodes, $\omega_{E}^{i}$ is the weight of experts, $q_{i j}$ is the language evaluation of node $j$ given by expert $i, \lambda$ is the number of experts, n is the number of nodes.

In FST, the defuzzification process produces quantifiable results. Then, the method of Mean area method (MAM) can be used to get the fuzzy value of the node $\left(N^{*}\right)$, as the following Formula (5):

$$
N^{*}=(a+2 m+b) / 4
$$

In this paper, the prior probability of each node can be obtained by converting $N^{*}$ into probability of an impact rate (PIR) using the Formulas (6) and (7) [36].

$$
\begin{gathered}
K=2.301 \times\left(\frac{1}{N^{*}}-1\right)^{1 / 3} \\
P I R=\left\{\begin{array}{c}
10^{-k}, N^{*} \neq 0 \\
0, N^{*}=0
\end{array}\right.
\end{gathered}
$$

# 3.2.2. BN 

BN is a probabilistic reasoning-based graphical network with functions such as causal analysis, bidirectional reasoning, and prediction. Due to its ability to better simulate human thought processes, BN has become an increasingly popular modeling technology in network security, such as information security risk assessment and intelligent grid security [38,39]. Moreover, it has recently been used to study insider threats in models [40,41]. Therefore, we introduce a BN model to this study since its causal relationship is very suitable for the study and application of risk problems.

BN is usually composed of two parts: BN structure and BN parameters. (1) The structure of BN is also called a directed acyclic graph (DAG), which is mainly a qualitative analysis of the BN, consisting of nodes representing each event and directed edges connecting each node, as shown in Figure 3. There are three main types of nodes: target nodes, intermediate nodes, and evidence nodes. (2) The parameter of BN is also called the Conditional Probability Table (CPT), a quantitative analysis of BN that represents the strength of connections between network nodes. BN can be expressed as:

$$
\mathrm{B}=\langle\mathrm{G}, \mathrm{P}\rangle=\langle(\mathrm{V}, \mathrm{M}), \mathrm{P}\rangle
$$

where $(\mathrm{V}, \mathrm{M})$ is a DAG with n nodes, M is the direct edge of these nodes, P is the CPT of each node and $X=\{X 1, X 2, \ldots, X n\}$ is a set of random variables. The JPD (joint probability distribution) of BN is:

$$
P(X)=P\left(X_{1}, X_{2}, \cdots X_{n}\right)=\prod_{i=1}^{n} P\left(X_{i} \mid \pi\left(X_{i}\right)\right)
$$

where, $\pi\left(\mathrm{X}_{\mathrm{i}}\right)$ represents the parent node of $\mathrm{X}_{\mathrm{i}}$. In addition, this study will combine NoisyOR gate model and expert judgment to implement CPT.

![img-2.jpeg](img-2.jpeg)

Figure 3. Directed acyclic graph.

# 4. Application of the Methodology 

### 4.1. Application of HFACS Framework

To identify as many contributing factors to the insider threat as possible, we first compiled insider threat incidents from 2009 to 2021 in various countries using Weibo, Baidu, and the existing literature. We filtered the collected data to identify enterprise security incidents in which unsafe acts were the leading cause. This paper compiles 43 enterprise insider threat incidents in China and other nations (including the United States and Israel) between 2009 and 2021. Then, based on the direct and indirect causes in the incident reports and concerning related studies [41-46], the HFs of insider enterprise threats were categorized and aggregated according to the item categories of the IHFACS model. Second, a workshop on information security within enterprises was held to compensate for the dearth of sample data, with the participation of experts in the field, such as senior project supervisors, network management managers, and IT engineers from various businesses. The improved HFACS model adheres to the four levels of the original HFACS framework; only specific subcategories were revised. Finally, these failures were classified into four levels based on the HFACS model: organizational influence ( $\mathrm{N}=12$ ), unsafe supervision failures $(\mathrm{N}=13)$, preconditions for unsafe acts $(\mathrm{N}=8)$, and unsafe acts $(\mathrm{N}=9)$. It can be seen that unsafe supervision and organizational failure contribute to insider threats most frequently. Table 3 lists the IHFACS contributory failures, along with their compliance and specific manifestations.

### 4.2. Establishment of Interdependencies for the Identified HFs

For mapping the IHFACS model into BN, the identified HFs are transformed into a hierarchy of nodes in BN. In the traditional HFACS framework, it is generally considered that the relationship between the four levels is that the upper level influences the lower level. The bottom layer (unsafe behavior) directly determines the occurrence of the accident. It often ignores the connections between different levels and within the same level. In practice, we find that this interaction relationship has an important impact on the occurrence of insider threats.

This study proposes two hypotheses as a result. The first is that the higher-level HFs in IHFACS would influence the lower-level HFs, and the second is that HFs at the same level could influence one another. First, the human factors of 43 insider threat events were classified and counted using the established IHFACS model. The frequency of HFs was then calculated, followed by the probability of the layers interacting. For example, when A11 occurs, the frequency of C12 is 18, and the proportion of its total frequency (20) is 0.9 , indicating that A 11 and C 12 have a 0.9 correlation value. We establish the threshold value at 0.8 . Experts score ( $0-1$ ) the association between upper and lower levels with each same-level factor according to IHFACS and get the association probability by weighted average. Two sets of association probabilities were derived after expert scoring and statistical analysis of case data. There are three scenarios to consider.

Table 3: Symbols and descriptions of HFs in the IHFACS.


Scenario 1: When the case's association probability exceeds the threshold value, the factors are deemed highly associated regardless of whether the expert's scoring value for the group of factors is greater than or less than the threshold value. An edge links two nodes together.

Scenario 2: When the case data count a set of factors whose association values are all less than the threshold and the expert scores for that set of factors are also less than the threshold, this means that the pair of factors does not hold in both hypotheses and is not considered.

Scenario 3: When the calculated association value for the case is less than the threshold and the expert's scoring value for the group of factors' association is greater than the threshold, factor weighting is necessary to determine the analysis. The calculation is weighted with a ratio of 0.8:0.2. For example, the statistical value of $20 \%$ and the expert's score of $80 \%$ can be weighted independently. If the weighted value is less than the threshold value, the group of factors is deemed irrelevant or insufficient and is not considered. The graphical structure of BN is built according to the IHFACS hierarchy by connecting nodes between the upper and lower levels of HFACS and within the same level with edges, as shown in Figure 4. All directed edges connecting nodes in the model of Figure 4 are shown in Table A1.
![img-3.jpeg](img-3.jpeg)

Figure 4. Mapping identified HFs in IHFACS to BN.

# 4.3. Bayesian Network Assignment 

In BN of the information security incident risk, the state of each node is considered to have two states. "Yes" means it has an impact on the occurrence of the accident, and "No" means it has no impact on the accident. The next step is determining the nodes' prior

probabilities and CPTs. Due to the relatively general statistics of insider threat events, some qualitative influencing factors cannot be obtained through statistical data. Therefore, this paper adopts fuzzy, expert elicitation, and Noisy-OR gate model to obtain the prior probability of the evidence nodes and CPTs for intermediate nodes. For this purpose, a method of scoring rules is established to calculate the competence of each expert and assign their respective weights. The contents of the expert rating scale are in Table 2, and the expert weights are shown in Table 4. Table 5 summarizes all expert opinions on the likelihood of HFs failures, and corresponding defuzzified aggregated and PIR values.

Table 4. Weights of employed experts.


Table 5. Expert opinions for HFs, defuzzify aggregated, and probability value.


Table 5. Cont.


In this BN model, the conditional probability table of only one D1("violation") node requires $2^{5}=32$ CPTs. The amount of data required is too large. In order to reduce the required data, the Noisy-OR gate model is introduced to estimate the CPT in this study. In the BN based on the Noisy-OR gate model, each variable has only two states, that is, "yes" and "no," and each variable is independent of the other [47]. Meanwhile, only one variable $A_{i}$ is enough to cause the result $Y$ to appear when the other variables do not. Only $A_{i}$ is "yes", and the other parent nodes is "no." The probability expression of the occurrence of node Y is as in Equation (10), and then CPTs for the child node Y are calculated using Equation (11).

$$
\begin{gathered}
P_{i}=P\left(Y \mid \bar{A}_{1}, \bar{A}_{2}, \cdots A_{i}, \cdots, \bar{A}_{n}\right) \\
P\left(Y \mid A_{p}\right)=1-\prod_{i: A_{i} \in A_{n}}\left(1-P_{i}\right)
\end{gathered}
$$

# 4.4. Inverse Reasoning (IR) and Sensitivity Analysis (SA) 

The FBN model inputs the prior model and CPTs to make it simulated and run in the GeNIe 2.3 Academic program and get the risk probability inference result of accidents. Deductive reasoning is one of the unique and specific characteristics of BN, which can reason regarding HFs that are not fully reflected in accident investigation reports, thereby improving accident investigation reports and contributing to future accident prevention. According to the reverse inference rule of BN, the calculation result is obtained, and the probability that the accident state is "yes" is set to $100 \%$. As shown in Figure 5, the sum of the four probabilities of organizational influences (A), unsafe supervision (B), preconditions of unsafe acts (C), and unsafe acts (D) is significantly greater than 1, demonstrating the existence of interactions within all four HFACS levels and among their peers. Notably, the probability of unsafe behavior is the largest, followed by the premise of unsafe behavior. Continue to infer the reverse, assuming that the probability of bad conditions for accidents $\mathrm{A}, \mathrm{B}$, and C is $100 \%$, the results show that the probability of unsafe behavior is as high as $99 \%$, and A13 has the highest probability in parent nodes. The most likely cause-and-effect chain leading to unsafe behaviors is $\mathrm{A} 13 \rightarrow \mathrm{~A} 1 \rightarrow \mathrm{~A} \rightarrow \mathrm{D}$. The most likely causal chain that leads to unsafe behavior begins with a flawed security detection system, then passes to poor resource management and organizational influences.

Sensitivity analysis is used to determine the degree of influence of each factor on insider threat incidents. In Figure 6, the darker the node's color, the more sensitive the node is. The most sensitive events are A22, A11, A23, A24, C13, A13, A12, B13, D12, C12, and C11. Among them, the top five contributing root events are "managers don't pay enough attention to internal security organization (A22)," "insufficient safety education and training (A11)," "lack of humanistic care for employees who are inclined to leave (A23)," "enterprise talent mobility is large (A24)," and "competence (C13)." Moreover, it is worth noting that the largest proportion ( $60 \%$ ) of the accident occurrence comes from organizational influences (A) among the top 10 contributing HFs (Table 6).

# 4.5. Suggestions for Enterprise Information Security Management 

(1) For the most fundamental factor of imperfect security detection systems, enterprises, especially SMEs, should pay attention to their investment in insider threat detection technology and promptly update detection tools to strengthen database security management. Suggestions for the prevention of internal threats are made for key causal factors.
(2) At the organizational impact A level, enterprises should focus on preventing insider threats, setting up an internal information security management department, and establishing a sound internal attack emergency response mechanism. In addition, continuous information security awareness training and education are crucial to enterprise security management.
(3) Talent is the core resource for an enterprise's sustainable and healthy development. The loss of high-level talents can easily lead to the leakage of the enterprise's commercial secrets and core technologies. Focusing on humanistic care for employees is one of the most important ways to retain talent. In addition, it is building an early warning mechanism for high-level talent loss to prevent it before it happens.
![img-4.jpeg](img-4.jpeg)

Figure 5. Insider threat risk diagnostic inference results.

![img-5.jpeg](img-5.jpeg)

Figure 6. Sensitivity analysis results.
Table 6. Top 10 riskiest factors in insider threats.


# 5. Conclusions 

To identify and rank the most highly contributing HFs in insider threats, this paper proposes a hybrid model based on FST, BN, and IHFACS. The model facilitated the identification, characterization, and ranking of human factors from the perspective of accident causation. Deficiencies in resource management (e.g., A11, A12, and A13), poor organizational climate, technical detection vulnerabilities, and bad personal factors were the most critical root events related to the occurrence of insider threats. At the same time, behavior violation was the most important unsafe behavior leading to accidents, among which the factor with the most significant influence is "employees' familiarity with the company's internal safety policy/low level of mastery of safety skills" (D12).

The study's most striking finding was that organizational influence is the primary contributor to the top 10 basic events. In addition, the study discovered that HFs influencing different levels of insider threat have an influential relationship not only between factors at the next level associated with the previous level, but also between factors across levels and within the same level. The most likely causal chain for the occurrence of insecure behaviors was: "Inadequate detection system deployment and system access control settings $\rightarrow$ resource management failure $\rightarrow$ organizational management failure $\rightarrow$ insecure behaviors."

Despite the lack of available datasets to compare our methods, the results of other insider threat studies could be used to corroborate each other. Elmrabit et al. [48] proposed a BN-based insider threat risk prediction model, which predicts that cases with the highest likelihood of insider threats are due to a high level of risk in human factors, including capabilities, opportunities, and motivation. Small companies pay less attention to insider threats, invest less in technical factors, and have lower detection levels. Furthermore, inadequate occupational safety training, which leads to insufficient safety awareness among employees and predisposes them to unsafe behaviors, is an essential human factor prevalent in insider threats [23]. These were consistent with the results of this study.

Insider threat is one of the toughest challenges to the sustainable development of enterprises currently, and the insider threat risk assessment model proposed in this study has certain application value. Based on the obtained results, more reasonable control measures and improvement suggestions are put forward for the internal risk prevention of the enterprise.

## 6. Future Work

This paper has some limitations. Since insider threat incidents are corporate scandals, many security incident investigation reports are not publicly available, making the sample size of cases in this paper small. At the same time, because subjective factor data mostly involves personal privacy and corporate secrets, it is more difficult to obtain than objective factor data. Although the integration of expert judgment and fuzzy theory is used to solve the problem of insufficient historical data and help risk assessment overcome possible ambiguity, the reasoning process and results of the study are largely related to the completeness of the cases and the expertise of the expert group.

In our future work, we will design privacy and secret filtering protection mechanisms to ensure the threat pattern data is based on the user's or enterprise's concerns in response to the problem of difficult access to some data. Through this approach, we can collect as many different security events as possible within the enterprise to expand the sample size. Based on these data, we plan to incorporate machine learning into the BN model in order to improve the model's accuracy and credibility in risk assessment.

Author Contributions: Conceptualization, Y.W.; methodology, M.Z.; validation, M.Z.; formal analysis, M.Z.; investigation, M.Z.; resources, C.D.; data curation, C.D.; writing-original draft preparation, M.Z.; writing-review and editing, C.D. and Y.W.; funding acquisition, Y.W. and C.D. All authors have read and agreed to the published version of the manuscript.

Funding: This paper is supported by Philosophy and Social Science Foundation Youth Project of Hunan Province of China, grant number 19YBQ093, the Scientific research project of Education Department, grant number 20C1625, and the Special Funds for Student Innovation and Entrepreneurship Training Program, grant number S202010555082. The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript.

Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: The data presented in this study are available on request from the corresponding author.

Acknowledgments: We sincerely thank all the experts who participated in this research information security conference and Krista Chen for their contribution to this work.

Conflicts of Interest: The authors declare no conflict of interest.

# Appendix A 

Table A1. All directed edges connecting nodes in the model.

