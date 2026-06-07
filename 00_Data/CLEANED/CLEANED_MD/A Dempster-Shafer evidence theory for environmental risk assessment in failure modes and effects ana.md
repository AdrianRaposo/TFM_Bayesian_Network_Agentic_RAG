# A dempster-shafer evidence theory for environmental risk assessment in failure modes and effects analysis of oil and gas exploitation plant 

Gholamreza Shams, Seyed Morteza Hatefi*, and Shahla Nemati<br>Faculty of Engineering, Shahrekord University, P.O. Box 115, Shahrekord, Iran.

Received 11 June 2020; received in revised form 18 December 2021; accepted 24 January 2022

## KEYWORDS

Environmental risk assessment; Risk priority number; FMEA; Dempster-shafer theory of evidence; Uncertainty.


#### Abstract

The oil, gas, and petrochemical industries, as one of the largest sources of environmental pollutants, have different types and levels of pollution depending on the type of input materials, process steps, and output products. Various stages of exploration, extraction and processing of oil and gas have many environmental effects, such as those on soil, air, water, creatures, plants, and even humans. In this paper, a Failure Mode and Effects Analysis (FMEA) is employed to identify failures and environmental risks in an oil and gas exploitation plant. Dempster-Shafer (DS) theory of evidence is then proposed for environmental risk assessment due to its effectiveness in dealing with uncertain and subjective information. The assessment of experts and the confidence levels of their responses are employed to construct the Basic Probability Assignments (BPA) in DS theory of evidence. Furthermore, a new weighting method is proposed to obtain the discounted BPA which reduces the uncertainty in the information sources and improves the quality of information before combining different sources of information. Finally, the proposed method is applied to an oil and gas exploitation plant to assess environmental risks.


(c) 2024 Sharif University of Technology. All rights reserved.

## 1. Introduction

With the advent of technology and increased use of machinery, the risks and incidents have also increased in industrial environments. In gas refineries, operating units are exposed to high temperatures and pressures,

[^0]so there is a possibility of occurrence of accidents. Given the fact that oil, gas, and petrochemical storage tanks are major infrastructures, as well as due to their enormous environmental hazards, this industry has always been a concern for experts in the field of safety and the environment. Oil storage tanks are the most important industrial facilities that are always at risk of toxic emissions, fires, and explosions. The most common fires and explosions are the most important risks in storage tanks [1]. Also, due to the presence of


[^0]:    *. Corresponding author. Tel.: 03832324438
    E-mail addresses: g.shams@sku.ac.ir (Gh. Shams); smhatefi@sku.ac.ir (S.M. Hatefi); s.nemati@sku.ac.ir (Sh. Nemati)

volatile hydrocarbon contaminants and volatile organic compounds in the refinery, these pollutants are extensively active in the non-saturated soils and can pollute the soil around the reservoirs [2]. These lead to other environmental concerns, such as global warming, ozone depletion, water pollution, and species extinction.

Risk assessment is a systematic approach for identifying hazards and ranking them for decision making, prevention, and mitigation of risks [3,4]. The main objectives of the risk assessment are determining the degree of uncertainty of a studied system and its costs and providing risk and cost reduction solutions [5,6]. Risk assessment can be done in two qualitative and quantitative ways. A quantitative assessment is focused on risk factors and preventive actions, which control and eliminate or prevent failures. The qualitative assessment method requires a scientific approach to decision making, cost justification, risk prevention, and mitigation, and rapid risk control programs [7,8].

Many studies have been conducted on incidents and risks in storage tanks and their products. Chang and Lin [9] studied the incident in industrial storage tanks in the last 40 years. Their results showed that $74 \%$ of the incidents occurred in oil refineries, oil terminals, and storage. Wang et al. [10] investigated the effects of earthquakes on liquid gas storage tanks. The results indicated that the use of insulating layers in internal and external walls of reservoir design reduces the potential for vulnerability during an earthquake.

Failure Mode and Effects Analysis (FMEA) is one of the useful methods to define, identify, and eliminate potential failures in the oil and petrochemical industries. The Risk Priority Number (RPN) is widely used to determine the priority of failure modes [11,12]. Three risk factors, namely, Occurrence (O), Severity (S), and Detection (D) are used to calculate the RPN of a failure mode. The RPN of a failure mode is calculated by multiplying the values of three factors O, S, and D. Failures with higher RPNs are considered more important and are given higher priority.

RPN-based methods have a major disadvantage in which precise values cannot be assigned to the occurrence, severity, and detection factors. In many cases, these factors are faced with uncertainty, and it is a difficult task to assign the exact numerical value to risk factors. Fuzzy theory has been used in many studies to overcome this problem [13]. In this line of research, Wang et al. [14] obtain a fuzzy rating for the occurrence, severity, and detection of a failure and introduced a Fuzzy Risk Priority Number (FRPN), which is calculated by fuzzy weighted geometric mean of three risk factors. Kutlu and Ekmekçioğlu [15] proposed fuzzy FMEA by linguistic variables for risk assessment. Dağsuyu et al. [16] proposed a fuzzy FMEA to identify and prioritize hazards in a sterilization unit of a large hospital. Zhou and Thai [17]
applied both grey theory and fuzzy theory on FMEA to obtain RPN. The authors obtained RPNs for oil tanker equipment failures by both grey theory and fuzzy theory. The authors showed that the results of the two methods are similar. A fuzzy inference system is an efficient method for risk assessment of failure modes under uncertainty. Application of fuzzy inference system to obtain the RPN can be seen in [1820].

Assessment of experts is one of the most important steps in the risk assessment process. The subjective judgment of experts may lead to unpredictable uncertainty. The existing approaches such as fuzzy set theory and the Bayesian method cannot effectively handle uncertainty [21]. Fuzzy set theory is an effective tool to handle epistemic uncertainty, which comes from a lack of information. As mentioned earlier, applications of fuzzy set theory for risk assessment can be seen in [14-20]. However, fuzzy set theory cannot effectively reflect the conflicting information of multiple sources. The DS method is an efficient tool to support decisions when information is nonspecific, ambiguous, or conflicting.

The Bayesian method is another tool to address uncertainties in the risk assessment process. Applications of this method for risk assessment can be seen [22-25]. The Dempster-Shafer (DS) method is an extended form of the Bayesian method that has all its advantages. For instance, in the DS method, as in the Bayesian method, existing prior information can be incorporated into the inference of uncertain indices and inferential results. However, the use of prior information in the DS method is not mandatory. This is one of the advantages of the DS method. Second, the DS method, unlike other possible methods such as the Bayesian method, does not require a previous probability calculation. Third, it has a flexible and understandable mass function. Fourth, providing the mass function is easy and convenient. Fifth, the computational complexity of this method is much less than the Bayesian method. All aforementioned discussions show the reasons for choosing the DS theory of evidence for risk assessment under uncertainty.

Several applications of evidence theory can be seen in the concerned literature due to its effectiveness and flexibility in dealing with uncertain and subjective information [26,27]. Recently, valuable studies have been conducted on the use of evidence theory to solve Multi-Attribute Decision-Making (MADM) problems. For instance, Liu and Zhang [28] introduced a novel method based on DS evidence theory to eliminate the existing defects of utilizing intuitionistic linguistic numbers in MADM problems. Liu and Gao [29] proposed some applications of intuitionistic fuzzy power Bonferroni mean operators in the context of evidence theory to solve MADM problems. Various models and

approaches have been developed based on linguistic intuitionistic fuzzy numbers and DS evidence theory to handle MADM problems under various types of uncertainty. These models and approaches can be seen $[30-33]$.

In the subject literature, evidence theory has become very important to solve risk assessment problems. Yang et al. [34] introduced a modified DS evidence theory to obtain the RPN of failure modes of aircraft engine rotor blades under uncertainty. Su et al. [35] proposed an improved version of the DS evidence theory introduced by Yang et al. [34], in which the Basic Belief Assignments (BBA) were improved to get more flexible and reasonable results.

Jiang et al. [36] proposed a novel fuzzy evidential method for FMEA. The authors defined fuzzy membership degree for risk assessment of failure modes. Then fuzzy mapping is utilized to obtain the belief structure and generate a basic probability assignment of risk factors. Finally, DS evidence theory is employed to fuse the evidence of risk factors. Certa et al. [37] employed the DS theory of evidence to deal with the existing uncertainty in the risk assessment process and prioritize the failures of the propulsion system of a fishing vessel.

This paper proposes an evidential model based on the DS theory of evidence for environmental risk assessment in failure modes and effects analysis of the Oil and Gas Exploitation Plant. The proposed evidential model, in addition to the mentioned advantages compared with fuzzy theory and Bayesian network, has several advantages compared to studies that have used the DS evidence theory methods for risk assessment such as Yang et al. [34], Jiang et al. [36], Certa et al. [37], and Hatefi et al. [26]. According to these advantages, the initial motivations of the paper can be stated as follows:

- To effectively deal with various uncertainties involved in the risk assessment process, it introduces a practical way to extract the Basic Probability Assignments (BPA) from evaluation information of experts by expressing linguistic terms and confidence levels for rating probability, severity, and detection of failures;
- In the process of assessing and ranking failures, the relative weight of risk factors is not taken into consideration. The weight of the three factors is assumed to be equal, but this may not be the case in practical applications. This paper utilizes Deng entropy to determine the relative weight of risk factors and obtain the discounted BPA for risk factors.

The rest of the paper is organized as follows. In Section 2, the FMEA method is introduced briefly.

The basic concept of the DS evidence theory is briefly reviewed in Section 3. The proposed evidential model for environmental risk assessment, which is constructed based on the DS evidence theory, is presented in Section 4. A new weighting method is proposed in this section for obtaining the discounted BPA. The environmental risks in an oil and gas exploitation plant are identified in Section 5. The proposed evidential model is applied to the studied case to assess the environmental risks. Section 6 obtains concluding remarks.

## 2. Failure Modes and Effects Analysis (FMEA)

Nowadays, applications of risk assessment methods in different organizations and industries are increasing, so that various types of qualitative and quantitative methods are developed for risk assessment. These methods are commonly utilized to identify, control, and mitigate the impacts of hazards. Organizations and industries can use these methods to meet their needs. The most important goal of health and safety system management in any organization is to study all methods of risk assessment and select appropriate methods to implement. Therefore, every organization and industry must have an appropriate way of identifying and assessing the risks of occupational safety and health activities as well as products or services [38].

FMEA can be described as a set of organized activities that are used to identify and estimate potential failure modes in a product or process and specify the activities that can eliminate or reduce the chance and probability of potential failures. FMEA is an analytical technique used to identify, mitigate and eliminate potential failures in a system, product design, manufacturing process, or service [38].

In the FMEA method, after identifying the risks, the risk estimation is performed by calculating RPN for each potential failure. RPN is calculated by multiplying three factors of occurrence, severity, and detection by using the traditional score $R P N=S \times O \times D$. These three factors are rated on a scale of 1 to 10 . The scales used for these three factors are reported in Table 1. The RPN is the basis for prioritizing failure modes. Given that three factors can handle numbers between 1 and 10 , the RPN will have a number between 1 and $1000[34]$.

## 3. Preliminaries

### 3.1. DS theory of evidence

The theory of evidence was introduced by Dempster [39] and developed by Shafer [40]. This theory is related to information from multiple sources that can be uncertain, incomplete, and imprecise. The theory of evidence is introduced based on a belief that results

Table 1. Traditional ratings for probability, severity, and detection of a failure [34].


from evidence. The belief structure of evidence theory relates to the classical probability model. The following are some of the basic concepts regarding the theory of evidence.

### 3.1.1. Frame Of Discernment (FOD)

Suppose $\theta=\left\{E_{1}, E_{2}, \ldots, E_{N}\right\}$ be a finite nonempty set of mutually exclusive and exhaustive events. Notation $\theta$ is called the Frame Of Discernment (FOD). The power set $\Omega$ is represented by $2^{\theta}$ which has $2^{N}$ elements as follows (Dempster, 1967; Shafer, 1976) [39,40]:

$$
\begin{aligned}
2^{\theta}= & \left\{\phi\left\{E_{1}\right\}, \ldots\left\{E_{N}\right\},\left\{E_{1}, E_{2}\right\}, \ldots\right. \\
& \left.\left\{E_{1}, E_{2}, \ldots, E_{i}\right\}, \ldots, \theta\right\}
\end{aligned}
$$

where $\phi$ is the empty set. If $A$ is an element belonging to the power set of $2^{\theta}$, or $A \in 2^{\theta}$, then it is called a proposition.

### 3.1.2. Basic Probability Assignment (BPA)

A mass function is stated as a mapping from the power set $2^{\theta}$ to the interval $[0,1]$. The mass function is mathematically presented as $m(A): 2^{\theta} \rightarrow[0,1]$ and satisfies the following relations.

$$
m(\phi)=0, \quad \sum_{A \in 2^{\theta}} m(A)=1
$$

where $A$ is a member of the power set. If the mass function of proposition $A$ is greater than zero, $m(A)>0$, then $A$ is called a focal element. All focal elements form the Body Of Evidence (BOE). The mass function $m(A)$ expresses that how strongly the evidence supports proposition $A$. The mass function is also known as a BPA or a BBA.

### 3.2. Uncertainty measures in DS framework

Various uncertainty measures are developed in terms of the DS theory of evidence. For instance, Deng [41] developed a new entropy measure called Deng entropy, which is an extended version of Shanon entropy introduced by Shannon [42]. Deng entropy measure is denoted by $E_{d}(m)$ and formulated as follows:

$$
E_{d}(m)=-\sum_{A \subset X} m(A) \log _{2} \frac{m(A)}{2^{|A|}-1}
$$

where $E_{d}(m)$ denotes Deng entropy, $A$ is a proposition in mass function $m, m(A)$ denotes the mass function of $A,|A|$ denotes the cardinality of proposition $A$ and $X$ is the FOD. In the case where proposition $A$ has a single element, Deng entropy converts to Shanon entropy as follows [42]:

$$
E_{d}(m)=-\sum_{A \subset X} m(A) \log _{2} m(A)
$$

where $A$ shows a proposition in mass function $m, m(A)$ denotes the mass function of $A$. Zhou et al. [43] extend Deng entropy and introduced a new belief entropy that
considers uncertain information in a BOE. The belief entropy proposed by Zhou et al. [43] is denoted by $E_{M d}(m)$ and calculated as follows:

$$
E_{M d}(m)=-\sum_{A \subset X} m(A) \log _{2}\left(\frac{m(A)}{2^{|A|}-1} \times e^{\frac{|A|-1}{|X|}}\right)
$$

where $E_{M d}(m)$ denotes the belief entropy, $|A|$ denotes the cardinality of proposition $A$ and $X$ is the FOD. Term $e^{\frac{|A|-1}{|X|}}$ in the aforementioned belief entropy considers uncertain information in a BOE which has been neglected in Deng entropy [43].

### 3.3. Discounted BPA

When there are several sources of information for decision-making, information sources must be properly combined and finalized. Since each of these sources has different reliability and the impact of different resource information on the final decision is different, the discounting operator is used to obtain the discounted BPA as follows:

$$
\begin{aligned}
& m^{r}(A)=(1-r) \times m(A), \quad A \in \theta \\
& m^{r}(\theta)=(1-r)+r \times m(\theta)
\end{aligned}
$$

where $A$ is the focal element of the mass function $m$. Notations $r$ and $m^{r}($.$) denote the coefficient of$ discounting and the discounted BPA, respectively.

### 3.4. Dempster combination rule

A combination of two sources of information in the DS theory of evidence is performed by operator $\oplus$. Let $m_{1}$ and $m_{2}$ be two BPA. Dempster combination rule is written as $m=m_{1} \oplus m_{2}$ and formulated as follows [40]:

$$
\begin{aligned}
& m(A)=\frac{1}{1-k} \sum_{B \cap C=A} m_{1}(B) m_{2}(C) \\
& k=\sum_{B \cap C=\phi} m_{1}(B) m_{2}(C)
\end{aligned}
$$

where $k$ expresses the conflict between two mass functions $m_{1}$ and $m_{2}$.

Dempster combination rule can be extended for more than two mass functions. The extended Dempster combination rule can be formulated as follows:

$$
\begin{aligned}
m & =m_{1} \oplus m_{2} \oplus \cdots \oplus m_{L} \\
& =\left(\left(\left(\left(m_{1} \oplus m_{2}\right) \oplus m_{3}\right) \oplus \cdots\right) \oplus m_{L}\right)
\end{aligned}
$$

### 3.5. Pignistic probability transformation

The pignistic probability transformation transforms a BPA to a probability distribution to make a decision. Assume that $m$ is a BPA on the FOD $\theta$. The pignistic probability transformation for a singleton $x \in \theta$ can be obtained as follows $[28,30,44]:$

$$
\operatorname{Bet} P\{x\}=\sum_{x \in A \subset \theta} \frac{1}{|A|} \frac{m(A)}{1-m(\phi)}, \quad m(\phi) \neq 1
$$

where $|A|$ denotes the number of elements of proposition $A[29]$.

## 4. Environmental risk assessment using D-S evidence theory

In this section, the proposed method for environmental risk assessment based on the DS evidence theory is introduced. The proposed method has the following main steps for environmental risk assessment:

Step 1: Determine the linguistic terms of risk factors.

In the risk evaluation process, experts score all risk factors for a given environmental failure mode. In the first step, the linguistic terms including severity, occurrence, and detection must be scored based on the experts' opinions. Table 1 is utilized to obtain the ratings of severity, occurrence, and detection of environmental risks.
Step 2: Determine the confidence level for linguistic terms.

In the scoring process, experts assign a score for severity, occurrence, and detection based on their experience and subjective judgments. Since judgments may be associated with uncertainty, assigning a linguistic term to score a risk factor is difficult. Therefore, experts prefer to select one or more linguistic terms with appropriate confidence levels to assess risk factors. The numerical scale which states confidence levels is presented in Table 2 [21].
Step 3: Convert the experts' opinions to BPAs.
According to Table 1, there are ten elements in linguistic terms for rating risk factors. In DS theory of evidence, these elements can be considered as the FOD for severity, occurrence, and detection. Therefore, the FOD is presented as follows:

$$
\theta^{j}=\{1,2,3, \ldots 10\}, \quad j=S, O, D
$$

Table 2. Confidence levels and their scales [21].


The experts' rating for each risk factor including severity, occurrence, and detection, can be considered as focal elements and their respected confidence levels, which are determined based on Table 2, are used as the corresponding mass functions. Suppose that $x_{i j}$ denotes the rating of failure mode $i$ for risk factor $j(j=S, O, D)$. For instance, according to Table 1, the respected evaluation levels in $x_{i j}$ are $N, V M, M I, L, M O, S, M A, E, H W$, and $H W O$ for the severity of a failure, and the corresponding confidence levels are $a, b, c, d, e, f, g, h, I$, and $J$, respectively. Then, the respected BPA for severity can be written as follows $[31,32]$ :

$$
\begin{aligned}
& m(\{N\})=a \\
& m(\{V M\})=b \\
& m(\{M I\})=c \\
& \vdots \\
& m(\{W H O\})=J \\
& m(\theta)=1-a-b-c-\cdots-J
\end{aligned}
$$

Similarly, the BPAs can be constructed for the occurrence and detection of a failure. As an example, suppose a rating of an expert about severity for the first failure mode $\left(R_{1}\right)$ is low $(L)$ and moderate (MO) with confidence levels 0.2 and 0.3 , respectively. Then the respected BPA can be written as: $m(\{L\})=0.2$, $m(\{M O\})=0.3, m(\theta)=0.5$.
Step 4: Calculate the discounted BPA based on the new weighted discounting coefficient.

In this step, a new weighting method is proposed based on the belief entropy developed by Zhou et al. [43] for weighting BPAs. According to the DS combination rule, two sources of information that may have uncertainty can be combined. It is necessary to consider the quality of information and to reduce uncertainty when combining them. Since the high value of an uncertainty measure reduces the reliability of the results, it is necessary to reduce the uncertainty in the information sources before combining them. Therefore, to reduce uncertainty, the discounted BPA must be obtained based on the weights of that BPA. To introduce the new weighting method, let $B P A_{i}$ be the BPA of $i$ th failure mode for a given risk factor such as severity, occurrence, or detection. According to Eq. (5), $E_{M d}\left(B P A_{i}\right)$ denotes the uncertainty measure for $B P A_{i}$ which is calculated by Zhou et al. [43] method. The uncertainty measure needs to be normalized to take a value in the interval $[0,1]$ according to the following formulation:

$$
0 \leq \frac{E_{M d}\left(B P A_{i}\right)}{\max \left\{E_{M d}\left(B P A_{i}\right)\right\}} \leq 1
$$

where $\max \left\{E_{M d}\left(B P A_{i}\right)\right\}$ is calculated by the following formulation:

$$
\begin{aligned}
& \max \left\{E_{M d}\left(B P A_{i}\right)\right\}=-\sum_{i} m\left(F_{i}\right) \\
& \quad \log _{2}\left(\frac{m\left(F_{i}\right)}{2^{\left|F_{i}\right|}-1} \times e^{\frac{\left|F_{i}\right|-1}{|X|}}\right)
\end{aligned}
$$

where

$$
m\left(F_{i}\right)=\frac{2^{\left|F_{i}\right|}-1}{\sum_{i} 2^{\left|F_{i}\right|}-1}
$$

where $E_{M d}\left(B P A_{i}\right)$ denotes the belief entropy introduced by Zhou et al. [43], denotes the maximum value of the belief entropy, $F_{i}$ is a proposition in mass function $m, m\left(F_{i}\right)$ is the mass function of $F_{i}$, and $\left|F_{i}\right|$ presents the number of elements of $F_{i}$. Furthermore, notations $X$ and $|X|$ are the FOD, and its number of elements, respectively.

According to the weight derivation method in Shanon entropy, the normalized form of the degree of diversification can be considered as a weight value [41]. Therefore, according to this weight derivation method, the weight of $B P A_{i}$ can be calculated by the following formulation:

$$
w_{i}=1-\frac{E_{M d}\left(B P A_{i}\right)}{\max \left\{E_{M d}\left(B P A_{i}\right)\right\}}
$$

where $w_{i}$ denotes the weight of $B P A_{i}$. This weight factor can be used as a coefficient of discounting to obtain the discounted BPA. According to Eq. (6), the discounted $B P A_{i}$ can be rewritten as follows:

$$
\begin{aligned}
& m^{w}(A)=\left(1-w_{i}\right) \times m(A), \quad A \in \theta \\
& m^{w}(\theta)=\left(1-w_{i}\right)+w_{i} \times m(\theta)
\end{aligned}
$$

where $w$ and $m^{w}($.$) denote the coefficient of discount-$ ing and the discounted BPA, respectively.
Step 5: Combine the discounted BPAs using the Dempster combination rule.

In this step, the discounted BPAs are aggregated by the combination rule according to Eqs. (7) and (8).
Step 6: Apply the pignistic probability transformation.

As the combined results for discounted BPAs are in the form of focal elements with mass function values, the pignistic probability transformation is used to convert them into a singleton element. In this step, the pignistic probability transformation is provided for the linguistic terms. To get a numerical value for each risk factor, the probability distribution must be integrated. For doing so, suppose that we have $n$ linguistic terms with ratings $L_{1}, L_{2}, \ldots, L_{n}$ for evaluating a risk factor.

Furthermore, let $P_{1}, P_{2}, \ldots, P_{n}$ be the probability distribution concerning $n$ linguistic terms. Then the aggregated value, which is the mathematical expectation value of the risk factor, is calculated as:
Aggregated value $=L_{1} P_{1}+L_{2} P_{2}+\ldots+L_{n} P_{n}$.
Step 7: Calculate the RPN.
In this step, by utilizing the results obtained in Step 7, the RPN is calculated for each failure mode by the following equation [45]:

$$
R P N=S \times O \times D
$$

where RPN is the RPN of a failure. Notations $S, O$, and $D$ denote the severity, occurrence, and detection of a failure, respectively.

## 5. Case study

In this study, environmental risks were first identified by the FMEA in the exploitation plant of one of the oil and gas plants in Ahvaz, Iran. To implement FMEA, a team of experts familiar with the production processes and risk assessment methods completes the worksheet designed for different sections, based on technical experience, interviews with managers, and data collection. Identification of environmental risks and their consequences, survey of design features, the status of the existing environment, identification of pollutants and hazards, and determination of impacts on most affected areas have been done through interviews with experts. Failure modes, causes of failures, failure effects, risk causes, severity, occurrence, and detection, construct the FMEA columns form. As such, the risks are identified and estimated. After identifying the risks using screening, the remaining 11 risks are reported in Table 3. Table 3 shows the results of the implementation of the FMEA method in the studied plant. In this table, failure modes, cases of failure, environmental issues, and environmental impacts are reported.

To calculate the environmental RPN, the proposed evidential method introduced in Section 4 is applied. According to Steps 1 and 2, the rating of risk factors and their respected confidence levels are collected according to the opinions and judgments of experts. For doing so, three experts who are the top managers in the oil and gas exploitation plant are selected and the respected data are gathered. In the third step of the proposed method, data must be converted into the BPAs for applying DS evidence theory to obtain RPNs. The BPA values are obtained for three risk factors according to the judgments of the first expert and reported in Table 4.

In Step 4, the weight of BPAs is calculated and then the discounted BPAs are obtained according to

Table 3. Failure modes and environmental effects in the oil and gas plant.


formulation (15). For doing so, first, the belief entropy introduced by Zhou et al. [43] is obtained for each BPA according to Eq. (5). For example, according to Table 4 , consider the BPA of $R 1$ for occurrence. The belief entropy is calculated as follows:

$$
\begin{aligned}
& B P A(R 1): m(\{M, M H\})=0.5 \\
& m(\theta)=0.5 \\
& E_{M d}(m)=0.5 \times \log _{2}\left(\frac{0.5}{2^{2}-1} \times e^{\frac{2-1}{10}}\right)+0.5 \\
& \times \log _{2}\left(\frac{0.5}{2^{10}-1} \times e^{\frac{10-1}{10}}\right)=6.070
\end{aligned}
$$

The maximum belief entropy introduced by Zhou et al. [43] is calculated based on Eqs. (12) and (13) for the BPA with the following propositions:

$$
\begin{gathered}
\left(\{N I\}, \frac{2^{1}-1}{58025}\right),\left(\{R\}, \frac{2^{1}-1}{58025}\right) \\
\left(\{L\}, \frac{2^{1}-1}{58025}\right), \cdots,\left(\{E H\}, \frac{2^{1}-1}{58025}\right) \\
\left(\{N I, R\}, \frac{2^{1}-1}{58025}\right),\left(\{N I, L\}, \frac{2^{1}-1}{58025}\right) \\
\left(\{N I, R L\}, \frac{2^{1}-1}{58025}\right), \cdots,\left(\{V H, E H\}, \frac{2^{2}-1}{58025}\right) \\
\left(\{N I, R, L\}, \frac{2^{1}-1}{58025}\right),\left(\{N I, R, R L\}, \frac{2^{1}-1}{58025}\right) \\
\left(\{N I, R, M\}, \frac{2^{1}-1}{58025}\right), \cdots,\left(\{R F, V H, E H\}, \frac{2^{1}-1}{58025}\right) \\
\vdots \\
\left(\{N I, R, L, R L, M, M H, H, R F, V H, E H\}, \frac{2^{10}-1}{58025}\right)
\end{aligned}
$$

where $\{N I, R, L, R L, M, M H, H, R F, V H, E H\}$ denotes the FOD with respect to the probability of occurrence. The aforementioned propositions show the respected power set. The elements of the power set are shown as $\left(F_{i}, m\left(F_{i}\right)\right)$, in which $m\left(F_{i}\right)$ is calculated by $\frac{2^{\left[F_{i}\right]}-1}{\sum 2^{\left[F_{i}\right]}-1}$. To calculate the maximum value of the belief entropy, the expression:

$$
-m\left(F_{i}\right) \log _{2}\left(\frac{m\left(F_{i}\right)}{2^{\left[F_{i}\right]}-1} \times e^{\frac{\left[F_{i}\right]-1}{|X|}}\right)
$$

must be calculated for all propositions in the power set, and then the sum of all calculated expressions must be obtained according to Eq. (12). For example, the mentioned expression for the proposition $\left(\{N I\}, \frac{2^{1}-1}{58025}\right)$ is calculated as:

$$
-\frac{2^{1}-1}{58025} \log _{2}\left(\frac{\frac{2^{1}-1}{58025}}{2^{1}-1} \times e^{\frac{1-1}{1}}\right)=0.0003
$$

After obtaining this expression for all elements of the power set and summing them, the maximum belief entropy is calculated, whose value becomes 14.406 . The weight of is calculated based on Eq. (14) as follows:

$$
\begin{aligned}
w & =1-\frac{E_{M d}\left(B P A_{i}\right)}{\max \left\{E_{M d}\left(B P A_{i}\right)\right\}} \\
& =1-\frac{6.070}{14.406}=0.579
\end{aligned}
$$

Table 4. The constructed BPAs based on the first experts' evaluations for risk factors.


Table 5. The belief entropy and the weight of BPAs obtained by the first experts' opinions.


Table 6. The constructed BPAs based on the first experts' evaluations for risk factors.


Similarly, the weights of all BPAs are calculated. The belief entropy introduced by Zhou et al. [43] and the weights of BPAs are obtained and reported in Table 5.

After calculating the weights of BPAs, the discounted BPAs can be obtained by Eq. (15). The discounted BPAs for the first expert's opinions are reported in Table 6. Similarly, Steps 1 to 4 of the proposed method can be applied to the second and third experts' opinions to obtain the discounted BPAs for risk factors. In the fifth step of the proposed method, the discounted BPAs extracted from experts' opinions are combined

Table 7. The combined discounted BPAs based on the experts' evaluations.


according to the Dempster combination rule. For doing so, Eqs. (7) and (8) are used. The combined discounted BPAs for risk factors are reported in Table 7.

In Step 6, the combined discounted BPAs are converted into the probability distributions by applying the pignistic probability function shown in Eq. (9). To get the final score of risk factors, the probability distributions are aggregated based on Eq. (16). The respected results are reported in Table 8. Finally, the RPNs are calculated based on Eq. (17) and the results are reported in Table 9. According to the results, $R 2, R 7$, and $R 1$ gain the first to third ranks among environmental risks. Perforation of the pipeline when surplus water transfers from exploitation gas

Table 8. Bet $P$ and aggregate values for each failure mode under different risk factors.


Table 9. Risk priority number and rank of failure modes.


Table 10. Risk priority number and rank of failure modes.

Table 10. FMEA and fuzzy FMEA results.


unit to gravity coal reservoirs ( $R 2$ ), and pump failure $(R 7)$ and perforation of the pipeline when transmitting salt oil from exploitation unit to desalination unit are identified as three critical environmental risks.

As mentioned earlier, FMEA, as a risk prevention tool, is a good approach for all industries. This method is a surefire way to anticipate problems and identify the most effective and cost-effective preventive solution. Suggestions for corrective actions to address pipe piercing include: (a) provide proper pipeline coverage to prevent corrosion, (b) cathode protection to prevent corrosion, (c) technical inspection of pipelines by the Department of Corrosion and Metals, (d) periodic or annual testing of pipelines. The preventive actions are also recommended for pump failure: (a) intermediate repair by calibration tool group, (b) equipping the unit with spare pumps.

To highlight the advantages and rationality of the proposed method, it is compared with the FMEA and fuzzy FMEA methods for risk assessment. The traditional ratings for probability, severity, and detection of a failure are used to obtain the initial data in the FMEA method. Regarding the opinions of experts and Table 1, the linguistic expressions that have gained the highest level of confidence by the experts are considered as primary data for risk factors. In this regard, the numerical ratings corresponding to the mentioned linguistic expressions are obtained. The geometric mean is used to aggregate the assessment rating of experts. Columns first to fourth of Table 10 show the FMEA results including the aggregated value
of risk factors and the RPN value of failures.
To obtain fuzzy FMEA results, the linguistic expressions of experts about risk factors are used. Then fuzzy scales introduced in Dağsuyu et al. [16] are utilized to convert the linguistic expressions to the respected triangular fuzzy numbers. The geometric mean is utilized to aggregate the assessment of experts about risk factors. The sixth to eighth columns of Table 10 shows the aggregated fuzzy values of occurrence, severity, and detection, respectively. Multiplication of triangular fuzzy numbers is used to calculate the fuzzy RPN, which is shown in the ninth column of Table 10. Suppose, $(\alpha, \beta, \gamma)$ be a triangular fuzzy number, which shows the fuzzy RPN of a failure mode. The following formulation is used to obtain the defuzzified RPN.

$$
\text { Defuzzified } R P N=\frac{[(\gamma-\alpha)+(\beta-\alpha)]}{3}+\alpha
$$

According to the following formulation, the defuzzified RPNs are obtained that are reported in the last column of Table 10.

Table 11 shows the comparative results of FMEA, fuzzy FMEA, and the proposed evidential model. As mentioned earlier, the conventional RPN and fuzzy RPN are calculated by applying FMEA and fuzzy FMEA methods, respectively. The ranking results of FMEA, fuzzy FMEA, and the proposed evidential methods reveal that $R 1, R 2, R 3$, and $R 8$ are gained the same ranks by applying three methods. Furthermore, the remaining failures, except $R 7$, have obtained almost close ranks using three methods. For

Table 11. Comparing results of the FMEA, fuzzy FMEA, and proposed evidential method.


instance, $R 4$ has the fifth rank by utilizing the FMEA method, and the seventh rank by applying the fuzzy FMEA method, while it has the sixth rank regarding the proposed method.

## 6. Conclusion

In this paper, Failure Mode and Effects Analysis (FMEA) is first used to identify environmental risks in the oil and gas exploitation plant. 11 environmental risks with risk causes, environmental risk aspects, and environmental impacts are determined in the studied plant. The evidential model is then proposed based on Dempster-Shafer (DS) evidence theory for environmental risk assessment in the oil and gas exploitation plant. The proposed evidential model can effectively handle uncertain and subjective information and enables experts to express their opinions and confidence levels about risk factors. In the evidential model, the Basic Probability Assignments (BPA) are constructed based on the experts' opinions for risk factors. Furthermore, the new weighting method is developed to obtain discounted BPAs. The main advantages of the proposed weighting method are that it reduces uncertainty in BPAs and improves the quality of information and reliability of results when aggregating multiple BPAs. Finally, the proposed evidential model is employed to assess the environmental risks in the oil and gas exploitation plant.

The effectiveness of the proposed method is illustrated using a real case study in the oil and gas exploitation plant. In future research, the proposed method should be applied to more practice to further verify its feasibility. In this paper, the importance of experts' opinions is considered equally in the risk assessment process. But in real-world applications, decision-makers may have different knowledge back-
grounds, skills, and experiences. For future research, it is suggested to develop an evidential model based on DS evidence theory in which the importance of experts' opinions are considered based on their knowledge backgrounds, skills, and experiences.

## Acknowledgments

The authors are grateful for the valuable comments and suggestions of the editor-in-chief and the respected reviewers. These comments enhanced the strength and significance of our paper. This work has been financially supported by the research deputy of Shahrekord University. The grant number was 99GRN31M1759.

## Biographies

Gholamreza Shams is an Assistant Professor at faculty of engineering, Shahrekord University, Shahrekord, Iran. He received his PhD degree in Civil Engineering at the Delft University, Netherlands, Netherlands in 2014. His current research interests include: Risk management, Sediment Engineering: Flood Engineering, Earth Dams, and Hydraulic Structures.

Seyed Morteza Hatefi is currently an Associate Professor at faculty of engineering, Shahrekord University, Shahrekord, Iran. He received his PhD degree from the School of Industrial Engineering at the University of Tehran, in 2014. He received his BS in Statistics from Shahid Beheshti University, Tehran in 2006, and

MS in Industrial Engineering from University of Tehran at Tehran in 2009. His current research interests include: risk management, supply chain network design, logistics systems, multi-criteria decision making, data envelopment analysis, performance measurement and management, and operations research applications.

Shahla Nemati was born in Shiraz, Iran, in 1982. She received her BS degree in hardware engineering from Shiraz University, Shiraz, in 2005, her MS degree from
the Isfahan University of Technology, Isfahan, Iran, in 2008, and her PhD degree in computer engineering from Isfahan University, Isfahan, in 2016. Since 2017, she has been an Assistant Professor with the Computer Engineering Department, Shahrekord University, Shahrekord, Iran. She has written several articles in the fields of data fusion, emotion recognition, affective computing, and audio processing. Her current research interests include data fusion, affective computing, and data mining.