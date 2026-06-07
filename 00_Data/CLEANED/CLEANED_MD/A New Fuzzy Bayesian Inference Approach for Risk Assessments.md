# Article 

## A New Fuzzy Bayesian Inference Approach for Risk Assessments

Jintao Xu ${ }^{1,2,3}$, Yang Sui ${ }^{1,2, *}$, Tao Yu ${ }^{1,2, *}$, Rui Ding ${ }^{1}$, Tao Dai ${ }^{1,2}$ and Mengyan Zheng ${ }^{1,2}$

## check for updates

Citation: Xu, J.; Sui, Y.; Yu, T.; Ding, R.; Dai, T.; Zheng, M. A New Fuzzy Bayesian Inference Approach for Risk Assessments. Symmetry 2024, 16, 786. https://doi.org/10.3390/sym16070786

Academic Editor: Saeid Jafari
Received: 7 April 2024
Revised: 13 June 2024
Accepted: 17 June 2024
Published: 22 June 2024

## 0

Copyright: (c) 2024 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 School of Nuclear Science and Technology, University of South China, Hengyang 421001, China; xujt27@mail2.sysu.edu.cn (J.X.)
2 Hunan Engineering \& Technology Research Center for Virtual Nuclear Reactor, University of South China, Hengyang 421001, China
3 Sino-French Institute of Nuclear Engineering and Technology, Sun Yat-sen University, Zhuhai 519082, China

* Correspondence: suiyang@usc.edu.cn (Y.S.); yutao@usc.edu.cn (T.Y.)

Abstract: Bayesian network (BN) inference is an important statistical tool with additive symmetry. However, BN inference cannot deal with the uncertain, fuzzy, random, and conflicting information from experts' knowledge in the process of conducting a risk assessment. To tackle this issue, a new fuzzy BN inference approach for risk assessments was proposed based on cloud model (CM), interval type-2 fuzzy set (IT2 FS), interval type-2 fuzzy logic system (IT2 FLS), modified Dempster-Shafer (D-S) evidence theory (ET), and Latin hypercube sampling (LHS) methods along the following lines. Firstly, CM was integrated into IT2 FS, and CM-based IT2 FS (CM-IT2 FS) was defined in the IT2 FLS. Secondly, modified D-S ET was utilized to determine the CM-IT2 FS-based a priori probabilities, and the CM-IT2 FS-based BN model was established. Thirdly, the CM-IT2 FS-based a priori probabilities were reduced to the CM-IT1 FS-based ones using a type reducer in the IT2 FLS, LHS was applied to propose a new fuzzy BN inference algorithm, and then, the new algorithm was used in a typical case to perform the fuzzy BN positive inference for risk prediction and the fuzzy BN reverse inference for risk sensitivity analysis. Finally, the BN inference results were analyzed using the proposed algorithm and the two common BN inference algorithms, and the effectiveness of the proposed approach was validated. It can be concluded that the proposed approach was both accurate and promising.

Keywords: Bayesian network inference; risk assessment; information fusion; experts' knowledge

## 1. Introduction

Risk assessment is most beneficial for a complex system [1]. The aim of a risk assessment is to quantify the uncertain risks and to determine the probabilities of risk occurrence events and their impact on project objectives [2]. Therefore, assessing the risk of a complex system using a scientific tool is crucial.

The Bayesian network (BN) method is an advanced artificial intelligence tool [3]. BN inference is the procedure of combining the a priori probability and conditional probability, which can be obtained either using experts' knowledge or by data analysis [4], to calculate the updated probability of nodes [5,6]. It has characteristics with additive symmetry. The advantage of BN inference is that it can comprehensively utilize a priori and posteriori probabilities, and thus, it exhibits higher estimation accuracy and robustness [7]. BN inference includes BN positive inference and BN reverse inference. BN positive inference can be used to predict the occurrence probability for leaf nodes, which is a type of system failure, and BN reverse inference can be used to analyze the system sensitivity in the BN model [8]. BN inference has been explored as a potential valuable technique to conduct the risk assessment [9]. Recently, BN inference has been extensively employed for risk assessments in many complex systems that include nuclear power plants (NPPs) [10-12], petrochemical plants [13-16], construction projects [17-20], hazardous material transportation [21-24], etc. However, BN inference uses crisp probabilities; thus, it is challenging to deal with the uncertain information from experts' knowledge [25,26].

The type-2 fuzzy set (FS) (T2 FS) method, an extension of the type-1 FS (T1 FS) method, was first proposed by Zadeh in 1975 [27]. Based on the T2 FS, the type-2 fuzzy logic system (T2 FLS) was proposed by Karnik et al. in 1999 [28]. T2 FLS can be useful in dealing with highly uncertain information [29]. The reason for this is that the membership degree of T2 FS is a fuzzy value in the interval $[0,1]$ compared to that of T1 FS, which has a crisp value [30]; however, the computational complexity of T2 FLS is quite high [31]. As a restricted class of T2 FLS, interval T2 FLS (IT2 FLS) was proposed to avert the significant computational requirement that was mainly created by its type reducer [32]. Many researchers have recently been applying IT2 FLS to deal with the uncertain information from experts' knowledge for risk assessments [33,34,35]. Nonetheless, it is challenging to use IT2 FLS to deal with the fuzzy and random information from experts' knowledge [36].

The cloud model (CM) method based on the probability statistics theory and the traditional fuzzy set [37] provides a scientific way to solve the aforementioned challenging task. CM can be utilized to achieve the bidirectional conversion between qualitative linguistics and quantitative value and to characterize the fuzziness and randomness for a research object using digital characteristics [38]. CM is often used to deal with fuzzy and random information in risk assessments [39,40,41]. Consequently, to deal with the uncertain, fuzzy, and random information from experts' knowledge, CM should be integrated into interval T2 FS (IT2 FS) to define the CM-based IT2 FS (CM-IT2 FS) in the IT2 FLS. Unfortunately, this is still a gap in the current research.

Since experts provide risk assessment judgements based on their own professional knowledge, conflicting information is generated [42]. Thus, the CM-IT2 FS-based conflicting information should be fused. Currently, the Dempster-Shafer (D-S) evidence theory (ET) [43], which uses the information fusion rule to fuse conflicting information [44], can only be applied to fuse the T1 FS-based conflicting information, and this T1 FS-based conflicting information includes triangular fuzzy numbers [45], trapezoidal fuzzy numbers [46], interval-valued fuzzy sets [47], intuitionistic fuzzy sets [48], etc. Therefore, the D-S ET has to be modified to fuse the CM-IT2 FS-based conflicting information.

Considering that BN inference for risk assessments was to be improved by CM, IT2 FS, IT2 FLS, and modified D-S ET, the conventional BN inference algorithm is no longer suitable. Thus, an applicable BN inference algorithm should be defined. Presently, the Monte Carlo sampling (MCS) method and the variational inference (VI) method are the two main methods used to define the fuzzy BN inference algorithms in the T1FSs environment [49], in which MCS is used to randomly generate the samples through distribution functions of input random variables and VI is used to transform complicated inference issues into high-dimensional optimized ones. However, they are inefficient for large samples $[50,51]$.

The Latin hypercube sampling (LHS) method, a stratified random sampling technique [52], has attracted interest from academics. LHS can divide the range of cumulative distribution function (CDF) of each variable into equal probability intervals and randomly generate a sampling value for each interval $[53,54]$. The above process ensures that all the sampling values can cover the sampling intervals [55]. Evidently, LHS can produce a higher number of stable and precise results than MCS with the same sampling number [56]. However, it is difficult to apply LHS to propose a fuzzy BN inference algorithm in the CM-IT2 FS environment. One reason for this may be that there is no one-to-one mapping relationship between each variable and its CDF for the CM-IT2 FS. To obtain this one-to-one mapping relationship, the fused CM-IT2 FS-based conflicting information should be reduced to the CM-IT2 FS-based information. Fortunately, IT2 FLS can reduce the IT2 FS-based information to the IT1 FS-based information using a type reducer [57], and this provides a potential solution to overcome the above difficulty.

The above literature shows that there is still a research gap pertaining to the fuzzy BN inference for risk assessments with respect to the uncertain, fuzzy, random, and conflicting information from experts' knowledge. Therefore, the innovative purpose of this study is to propose a new fuzzy BN inference approach for risk assessment by studying the following

problems: (1) how to integrate CM into IT2 FS in order to define the CM-IT2 FS in the IT2 FLS; (2) how to utilize modified D-S ET to determine the CM-IT2 FS-based a priori probabilities in order to establish the CM-IT2 FS-based BN model; (3) how to apply LHS to propose a new fuzzy BN inference algorithm on the basis of the CM-IT1 FS-based a priori probabilities obtained by reducing the CM-IT2 FS-based ones using a type reducer in the IT2 FLS; and (4) how to conduct the fuzzy BN positive and reverse inferences for risk assessments using the proposed algorithm.

Three original contributions of this study can be summarized as follows:
(1) The CM-IT2 FS was defined in the IT2 FLS through Definitions 1 to 6, and the uncertain, fuzzy, and random information from experts' knowledge was dealt with accordingly.
(2) The CM-IT2 FS-based conflicting information from experts' knowledge was dealt with and fused using modified D-S ET, as shown in Equations (8)-(10), and then, the CM-IT2 FS-based BN model was established.
(3) A new fuzzy BN inference algorithm was proposed using LHS, as shown in Definition 13, and the risk prediction and risk sensitivity analysis were conducted by the proposed algorithm for a typical case.
This paper is outlined as follows. Section 2 introduces the preliminaries. Section 3 presents the proposed approach. Section 4 describes the case study. Section 5 validates and discusses the availability of the proposed approach. Section 6 concludes our study.

# 2. Preliminaries 

### 2.1. CM-IT2 FS in the IT2 FLS

Definition 1 [58]. IT2 FLS is composed of a fuzzifier, a rule, an inference engine, a type reducer, and a defuzzifier. The fuzzifier is responsible for converting the expert judgement information, which is qualitative linguistics, into a form of IT1 FS. The rule is used to perform the fuzzy operation. The inference engine provides a mapping from the IT1 FS to the IT2 FS. The type reducer converts the IT2 FS into the IT1 FS. The defuzzifier produces the crisp output. The general architecture of IT2 FLS is shown in Figure 1.
![img-0.jpeg](img-0.jpeg)

Figure 1. General architecture of IT2 FLS.
Definition 2 [59]. $B$ is a qualitative linguistic set in the domain; $x$ is assumed to be a random number that obeys a normal distribution with $x \in B$. The membership degree $\mu(x)$ of $x$ is a random number with a stable inclination and $\mu(x) \in[0,1]$.

Definition 3. In the CM-IT2 FS, $\widetilde{\tilde{r}}_{i j}$ represents the CM-IT2 FS-based membership degree of the $i$-th assessment index subordinating to the $j$-th risk level, and it can be defined as follows.

$$
\widetilde{\tilde{r}}=\left(\widetilde{r}^{L}, \widetilde{r}^{U}\right)=\binom{\left(r_{1}^{L}, r_{2}^{L}, r_{3}^{L}, r_{4}^{L} ; H_{1}\left(r^{L}\right), H_{2}\left(r^{L}\right)\right)}{\left(r_{1}^{U}, r_{2}^{U}, r_{3}^{U}, r_{4}^{U} ; H_{1}\left(r^{U}\right), H_{2}\left(r^{U}\right)\right)}
$$

where $\widetilde{r}^{L}$ and $\widetilde{r}^{U}$ are T1FSs, and they represent the lower and the upper membership degree functions of CM-IT2 FS, respectively; $r_{1}^{L}, r_{2}^{L}, r_{3}^{L}, r_{4}^{L}, r_{1}^{U}, r_{2}^{U}, r_{3}^{U}$, and $r_{4}^{U}$ represent the reference points for $\widetilde{\tilde{r}}$; $H_{1}\left(r^{L}\right)$ and $H_{2}\left(r^{L}\right)$, the upper and lower limits for the lower membership degree function, respectively; and $H_{1}\left(r^{U}\right)$ and $H_{2}\left(r^{U}\right)$ represent the upper and lower bounds for the upper membership degree function, respectively.

Definition 4. In the CM-IT2 FS, $\overline{\widetilde{R}}_{i}$ represents the CM-IT2 FS-based membership degree set of the $i$-th assessment index subordinating to all risk levels, and it is defined as follows:

$$
\overline{\widetilde{R}}_{i}=\left\{\widetilde{r}_{i l}, \cdots, \widetilde{r}_{i j}, \cdots, \widetilde{r}_{i j}\right\}=\left\{\left(\widetilde{r}_{L}^{i l}, \widetilde{r}_{U}^{i l}\right), \cdots,\left(\widetilde{r}_{L}^{i j}, \widetilde{r}_{U}^{i j}\right), \cdots,\left(\widetilde{r}_{L}^{i l}, \widetilde{r}_{U}^{i l}\right)\right\}
$$

where $j=1,2, \cdots, 5$.

# 2.2. CM-IT2 FS-Based BN Model 

Definition 5 [60,61]. BN is a directed acyclic graph, which is composed of nodes and arrows. The nodes represent the random variables. The arrows, which connect parent nodes and their child nodes, represent the conditional dependencies between different variables. The occurrence probability of root node is called the a priori probability. The probability of non-root node is called the conditional probability. Each node codifies a conditional probability distribution. The probability distribution of random variables is called the joint probability distribution, and can be defined as follows:

$$
P\left(X_{1}, \cdots, X_{i}, \cdots, X_{n}\right)=\prod_{i=1}^{n} P\left(X_{i} \mid p a\left(X_{i}\right)\right)
$$

where $X_{1}, \cdots, X_{i}, \cdots, X_{n}$ are the random variable set; $p a\left(X_{i}\right)$ is the parent node; and $P\left(X_{i} \mid p a\left(X_{i}\right)\right)$ is the conditional probability.

Definition 6 [62]. If a set $\Theta=\left\{u_{1}, \cdots, u_{i}, \cdots, u_{n}\right\}$ is a non-empty finite one with n mutually exclusive elements included, $\Theta$ is the framework of discernment. The power set of $\Theta$ is denoted by $P S(\Theta)$. A set function m: $P S(\Theta) \rightarrow[0,1]$ is regarded as an evidence source if it satisfies the following conditions:

$$
\left\{\begin{array}{l}
\sum_{u_{i} \subseteq P S(\Theta)} m\left(u_{i}\right)=1 \\
m()=0
\end{array}\right.
$$

where $m\left(u_{i}\right)$ represents the occurrence probability of $u_{i}$.
Definition 7. The CM-IT2 FS-based membership degree set in Definition 6 is defined as a basic belief assignment in the D-S ET using Equation (5).

$$
\overline{\widetilde{m}}\left(x_{i}\right)=\overline{\widetilde{R}}_{i}
$$

Definition 8 [63]. The traditional information fusion rule is defined to fuse the conflicting information from experts' knowledge using Equations (6) and (7).

$$
\begin{gathered}
K=\sum_{i=1}^{n} \prod_{e=1}^{s} m_{e}\left(x_{i}\right) \\
m^{*}\left(x_{i}\right)=\left\{\begin{array}{lr}
0, & x_{i}=\varnothing \\
\sum_{i=1}^{n} \prod_{e=1} m_{e}\left(x_{i}\right) \\
\frac{i-1}{1-K}, x_{i} \neq \varnothing
\end{array}\right.
\end{gathered}
$$

where $K$ denotes a measure of conflict as the coefficient; $m_{e}\left(x_{i}\right)$ represents the basic belief assignment of the $i$-th assessment index by e-th expert; and $m^{*}\left(x_{i}\right)$ is the fused evidence.

Definition 9 [64]. The modified information fusion rule is utilized to fuse the conflicting information from experts' knowledge using Equations (8)-(10), and the D-S ET is modified. In Equations (8)-(10), there is a high degree of conflict in the obtained evidence when $K \geq 0.95$, and no conflict in the evidence is observed when $0 \leq K<0.95$.

$$
\begin{gathered}
\widetilde{m}^{L}\left(x_{i}\right)=\left\{\begin{array}{l}
\frac{1}{1-K^{L}} \prod_{e=1}^{z} m_{e}^{L}\left(x_{i}\right), \quad K^{L}<0.95 \\
K^{L} \frac{1}{z} \sum_{e=1}^{z} m_{e}^{L}\left(x_{i}\right)+\prod_{e=1}^{z} m_{e}^{L}\left(x_{i}\right), K^{L} \geq 0.95
\end{array}\right. \\
\widetilde{m}^{U}\left(x_{i}\right)=\left\{\begin{array}{l}
\frac{1}{1-K^{U}} \prod_{e=1}^{z} m_{e}^{U}\left(x_{i}\right), \quad K^{U}<0.95 \\
K^{U} \frac{1}{z} \sum_{e=1}^{z} m_{e}^{U}\left(x_{i}\right)+\prod_{e=1}^{z} m_{e}^{U}\left(x_{i}\right), K^{U} \geq 0.95
\end{array}\right. \\
\widetilde{\bar{m}}^{*}\left(x_{i}\right)=\left(\widetilde{m}^{L}\left(x_{i}\right), \widetilde{m}^{U}\left(x_{i}\right)\right)
\end{gathered}
$$

where $K^{L}$ and $K^{U}$ are coefficients of lower and upper bounds for $m\left(x_{i}\right)$, respectively; $\widetilde{m}^{L}\left(x_{i}\right)$ and $\widetilde{m}^{U}\left(x_{i}\right)$ are lower and upper membership degree functions for $m\left(x_{i}\right)$, respectively; and $\widetilde{\bar{m}}^{*}\left(x_{i}\right)$ is the fused information.

Definition 10. The fused conflicting information is defined as the CM-IT2 FS-based a priori probability using Equation (11). Based on this, the CM-IT2 FS-based BN model is established.

$$
\widetilde{\widetilde{P}}\left(X_{i}\right)=\widetilde{\bar{m}}^{*}\left(x_{i}\right)
$$

# 2.3. New Fuzzy BN Inference Algorithm 

Definition 11 [65]. The CM-IT2 FS-based a priori probability is reduced to the CM-IT1 FS-based one using Equations (12)-(14) in the type reducer of the IT2 FLS.

$$
\begin{gathered}
r_{i}^{L}=\frac{\left(r_{i 4}^{L}-r_{i 1}^{L}\right)+\left(H_{1}\left(r_{i}^{L}\right) \times r_{i 2}^{L}-r_{i 1}^{L}\right)+\left(H_{2}\left(r_{i}^{L}\right) \times r_{i 3}^{L}-r_{i 1}^{L}\right)}{4}+r_{i 1}^{L} \\
r_{i}^{U}=\frac{\left(r_{i 4}^{U}-r_{i 1}^{U}\right)+\left(H_{1}\left(r_{i}^{U}\right) \times r_{i 2}^{U}-r_{i 1}^{U}\right)+\left(H_{2}\left(r_{i}^{U}\right) \times r_{i 3}^{U}-r_{i 1}^{U}\right)}{4}+r_{i 1}^{U} \\
\widetilde{P}\left(X_{i}\right)=\left(r_{i}^{L}, r_{i}^{U}\right)
\end{gathered}
$$

Definition 12. The fuzzy probability of occurrence for leaf node $T$ is defined using Equation (15) after determining the CM-IT1 FS-based a priori probabilities and conditional probabilities. The updated fuzzy a priori probability, called fuzzy posteriori probability, is defined using Equation (16). The fuzzy sensitivity performance measure (SPM), which denotes the sensitivity degree of root nodes, is defined using Equation (17).

$$
\begin{aligned}
\widetilde{P}(T) & \cong \sum_{i=1}^{n} \widetilde{P}\left(X_{i}\right) \otimes P\left(T \mid X_{i}\right) \\
\widetilde{P}\left(X_{i} \mid T\right) & \cong \widetilde{P}\left(X_{i}\right) \otimes P\left(T \mid X_{i}\right) \oslash \widetilde{P}(T) \\
S \widetilde{P} M\left(X_{i}, T\right) & \cong \sum_{j=1}^{V}\left(\widetilde{P}\left(T \mid X_{i j}=1\right) \ominus \widetilde{P}(T)\right) \oslash \widetilde{P}(T)
\end{aligned}
$$

where $\widetilde{P}(T)$ is the fuzzy occurrence probability; $\widetilde{P}\left(X_{i}\right)$ is the fuzzy a priori probability; $P\left(T \mid X_{i}\right)$ is the conditional probability; $\widetilde{P}\left(X_{i} \mid T\right)$ is the fuzzy posteriori probability; $\operatorname{SPM}\left(X_{i}, T\right)$ is the fuzzy SPM; and $\widetilde{P}\left(T \mid X_{i j}=1\right)$ is the updated fuzzy occurrence probability.

Definition 13. A new fuzzy BN inference algorithm is proposed using LHS. The proposed algorithm is as follows Algorithm 1:


# 3. Proposal of a New Fuzzy BN Inference Approach 

In this study, CM, IT2 FS, IT2 FLS, modified D-S ET, and LHS were applied to introduce a new fuzzy BN inference approach for risk assessments. Figure 2 illustrates its theoretical framework, comprising three stages and twelve relevant steps.

### 3.1. Stage 1: Define the CM-IT2 FS in the IT2 FLS

At stage 1, the CM-IT2 FS was defined in the IT2 FLS, which included five steps.

### 3.1.1. Create the Index System

The index system is the basis to assess the studied risk.

### 3.1.2. Obtain the Qualitative Linguistics for Each Assessment Index

It is assumed that the qualitative risk assessment standard is composed of five risk levels, including level 1 (very low risk), level 2 (low risk), level 3 (medium risk), level 4 (high risk), and level 5 (very high risk). The senior experts on risk assessments were invited to provide their qualitative linguistics for each assessment index according to the risk assessment procedure.

### 3.1.3. Transform the Qualitative Linguistics into the Quantitative Cloud Characteristics

The golden section method [66], as shown in Table 1, was applied to transform the qualitative linguistics into the quantitative cloud characteristics for each assessment index. Then, the CM-based membership degree set of each assessment index subordinating to five risk levels $\mu_{i}=\left\{\mu_{i 1}, \mu_{i 2}, \mu_{i 3}, \mu_{i 4}, \mu_{i 5}\right\}$ was obtained, where $\mu_{i j}=\left(E x_{i j}, E n_{i j}, H e_{i j}\right)$ and $j=1,2,3,4,5$.

Table 1. Golden section method.


Table 1. Cont.


Notes: Ex (expectation value), En (entropy value), and He (hyper-entropy value) are three digital characteristics of $\mathrm{CM} ; X_{\max }$ and $X_{\min }$ represent the upper and lower bounds for the given qualitative linguistics, respectively; $X_{\max }$ is taken from Table 2, and $X_{\min }$ takes a value of 0 ; and $E x_{0}, E n_{0}$, and $H e_{0}$ are the quantitative cloud characteristics for the middle cloud, taking values of $0.5,0.103$, and 0.005 , respectively.
![img-1.jpeg](img-1.jpeg)

Figure 2. Theoretical framework of the proposed approach.

Table 2. Value of Xmax in Table 1.


3.1.4. Transform the CM-Based Membership Degree Set of Each Assessment Index into the Fuzzy Input Set in the IT2 FLS

The fuzzifier in the IT2 FLS and Equations (18)-(20) [67] was used to transform the CM-based membership degree set of each assessment index for the CM-IT1 FS-based membership degree set $\widetilde{\mu}_{i}$, and $\widetilde{\mu}_{i}=\left\{\widetilde{\mu}_{i 1}, \widetilde{\mu}_{i 2}, \widetilde{\mu}_{i 3}, \widetilde{\mu}_{i 4}, \widetilde{\mu}_{i 5}\right\}$. The $\widetilde{\mu}_{i}$ was inputted into the IT2 FLS as the fuzzy input set.

$$
\begin{gathered}
\mu_{i j}^{L}=E x_{i j}-3 E n_{i j} \\
\mu_{i j}^{U}=1-E x_{i j}-3 E n_{i j} \\
\widetilde{\mu}_{i j}=\left(\mu_{i j}^{L}, \mu_{i j}^{U}\right)
\end{gathered}
$$

3.1.5. Define the CM-Based Rule in the IT2 FLS and Create the CM-IT2 Fuzzy Judgement Matrix

The CM-based rule in the IT2 FLS was defined using Equations (21) and (22). The $\widetilde{\mu}_{i}$ was iterated twice by the defined rule and inference engine in the IT2 FLS. Afterwards, the $\widetilde{\mu}_{i}$ was transformed as the CM-IT2 FS-based membership degree set $\widetilde{R}_{i}$, and $\widetilde{R}_{i}=\left\{\widetilde{\widetilde{r}}_{i 1}, \widetilde{\widetilde{r}}_{i 2}, \widetilde{\widetilde{r}}_{i 3}, \widetilde{\widetilde{r}}_{i 4}, \widetilde{\widetilde{r}}_{i 5}\right\}$. Then, the CM-IT2 fuzzy judgement matrix $\widetilde{W}$ for $n$ assessment indexes from one expert's knowledge was created using Equation (23), as follows:

$$
\begin{gathered}
\widetilde{r}_{i j}^{U}=\left(\widetilde{\mu}_{i j}\right)^{\alpha} \\
\widetilde{r}_{i j}^{L}=\left(\widetilde{\mu}_{i j}\right)^{\frac{1}{\alpha}}
\end{gathered}
$$

where $\alpha$ is the cut set, and it takes a value of 2 .

$$
\widetilde{W}=\left[\begin{array}{ccccc}
\widetilde{\widetilde{r}}_{11} & \widetilde{\widetilde{r}}_{12} & \widetilde{\widetilde{r}}_{13} & \widetilde{\widetilde{r}}_{14} & \widetilde{\widetilde{r}}_{15} \\
\vdots & \vdots & \vdots & \vdots & \vdots \\
\widetilde{\widetilde{r}}_{i 1} & \widetilde{\widetilde{r}}_{i 2} & \widetilde{\widetilde{r}}_{i 3} & \widetilde{\widetilde{r}}_{i 4} & \widetilde{\widetilde{r}}_{i 5} \\
\vdots & \vdots & \vdots & \vdots & \vdots \\
\widetilde{\widetilde{r}}_{n 1} & \widetilde{\widetilde{r}}_{n 2} & \widetilde{\widetilde{r}}_{n 3} & \widetilde{\widetilde{r}}_{n 4} & \widetilde{\widetilde{r}}_{n 5}
\end{array}\right]
$$

Through steps in Sections 3.1.2-3.1.5 in stage 1, the CM-IT2 FS was defined in the IT2 FLS.

# 3.2. Stage 2: Establish the CM-IT2 FS-Based BN Model 

At stage 2, the CM-IT2 FS-based BN model was established, and it included three steps.

### 3.2.1. Define the Nodes

The studied risk was defined as leaf nodes, and its causes were defined as middle nodes and root nodes, according to the analysis results.

### 3.2.2. Fuse the CM-IT2 FS-Based Conflicting Information and Determine the CM-IT2 FS-Based a Priori Probabilities

The CM-IT2 FS-based membership degree set in $\widetilde{W}$ was defined as a basic belief assignment using Equation (5). Afterwards, the evidence matrix $\widetilde{M}$ was created, as shown in Equation (24). Then, the CM-IT2 FS-based conflicting information was fused using

Equations (8)-(10), and the CM-IT2 FS-based a priori probabilities of root nodes were determined using Equation (11).

$$
\tilde{\tilde{M}}=\left[\begin{array}{ccccc}
\widetilde{\widetilde{m}}_{1}\left(x_{1}\right) & \cdots & \widetilde{\widetilde{m}}_{e}\left(x_{1}\right) & \cdots & \widetilde{\widetilde{m}}_{z}\left(x_{1}\right) \\
\vdots & \ddots & \vdots & \ddots & \vdots \\
\widetilde{\widetilde{m}}_{1}\left(x_{i}\right) & \cdots & \widetilde{\widetilde{m}}_{e}\left(x_{i}\right) & \cdots & \widetilde{\widetilde{m}}_{z}\left(x_{i}\right) \\
\vdots & \ddots & \vdots & \ddots & \vdots \\
\widetilde{\widetilde{m}}_{1}\left(x_{n}\right) & \cdots & \widetilde{\widetilde{m}}_{e}\left(x_{n}\right) & \cdots & \widetilde{\widetilde{m}}_{z}\left(x_{n}\right)
\end{array}\right]
$$

# 3.2.3. Determine the Conditional Probabilities 

Conditional probabilities of non-root nodes were determined based on the data analysis of the risk accident to be studied and the engineering experiences and knowledge from experts.

Through Sections 3.2.1-3.2.3 in stage 2, the CM-IT2 FS-based BN model was established.

### 3.3. Stage 3: Conduct the Fuzzy BN Inference

At stage 3, the new fuzzy BN inference was conducted, and it included four steps.

### 3.3.1. Reduce the CM-IT2 FS-Based a Priori Probabilities to the CM-IT1 FS-Based Ones

The CM-IT2 FS-based a priori probabilities were reduced to the CM-IT1 FS-based ones using a type reducer in the IT2 FLS and Equations (12)-(14).

### 3.3.2. Propose a New Fuzzy BN Inference Algorithm

A new fuzzy BN inference algorithm was proposed using LHS, as shown in Definition 13.

### 3.3.3. Conduct the Fuzzy BN Positive Inference

The fuzzy BN positive inference was conducted using the proposed fuzzy BN inference algorithm (Algorithm 1) to calculate the fuzzy occurrence probability of the risk to be studied so as to take scientific decisions to prevent the risk of accidents.

### 3.3.4. Conduct the Fuzzy BN Reverse Inference

The fuzzy BN reverse inference was conducted using the proposed fuzzy BN inference algorithm (Algorithm 1) to analyze the risk sensitivity in order to recognize the key risk factors. In reality, the risk management process should be enhanced according to the fuzzy SPM.

## 4. Case Study

A complex system, which was the NPP in Xudabo Nuclear Power Co., Ltd. (XNPCL), was selected as the case study. It adopts the VVER-1200 technology and is being constructed, at present, in Northeast China.

The deep foundation excavation engineering (DFEE) was selected as the research object in XNPCL. The DFEE has the characteristics of large investments, long engineering cycles, complicated techniques, and unpredictable risk factors [68]. Therefore, it is necessary to conduct the DFEE risk assessment for the NPP construction project.

The DFEE risk assessment was conducted by using the three stages presented in Section 3. Firstly, 10 experts with more than 10 years of experience in risk assessments for NPP construction projects were invited as the senior experts. Then, they conducted the on-site inspection and accessed the relevant information and data. Furthermore, they provided their qualitative linguistics according to the DFEE risk assessment procedure. Finally, the qualitative linguistics was converted into the quantitative value for the DFEE risk prediction and the DFEE risk sensitivity analysis.

# 4.1. Stage 1: Define the CM-IT2 FS in the IT2 FLS 

### 4.1.1. Create the Index System

The index system of the assessed DFEE risk was created on the basis of the DFEE risk assessment procedure in XNPCL, and it is shown in Table 3.

Table 3. Index system.


### 4.1.2. Obtain the Qualitative Linguistics for Each Assessment Index

The qualitative linguistics for each assessment index was provided by senior experts based on the DFEE risk assessment procedure.

### 4.1.3. Transform the Qualitative Linguistics into the Quantitative Cloud Characteristics

The qualitative linguistics was transformed into quantitative cloud characteristics for each assessment index, and then, the CM-based membership degree set of each assessment index subordinating to five risk levels was obtained through Section 3.1.3. Taking the qualitative linguistics for the assessment index $\mathrm{R}_{11}$ from the first expert as an example, its CM-based membership degree set was as follows: $\mu_{1}=\{(0.7,0.103,0.013),(0.85,0.045$, $0.008),(0.35,0.309,0.005),(0.15,0.045,0.008),(0,0.809,0.013)\}$.
4.1.4. Transform the CM-Based Membership Degree Set of Each Assessment Index into the Fuzzy Input Set in the IT2 FLS

The CM-based membership degree set of each assessment index was transformed into the CM-IT1 FS-based set $\tilde{\mu}_{i}$, and the $\tilde{\mu}_{i}$ was inputted into the IT2 FLS as the fuzzy input set through Section 3.1.4. Taking the CM-based membership degree set in Example 1 as an example, its corresponding fuzzy input set was as follows: $\tilde{\mu}_{1}=\{(0.156,0.500),(0.010$, $0.591),(0.156,0.500),(0.259,0.359),(0.156,0.500)\}$.
4.1.5. Define the CM-Based Rule in the IT2 FLS and Create the CM-IT2 Fuzzy Judgement Matrix

The CM-based rule in the IT2 FLS was defined, and then, the CM-IT2 fuzzy judgement matrix $\tilde{R}$ for eight assessment indexes from one expert was created through Section 3.1.5. Taking the CM-IT2 fuzzy judgement matrix $\widetilde{\widetilde{W}}$ for eight assessment indexes from the first expert as an example, the following matrix was established:

$$
\widetilde{\widetilde{W}}=\left[\begin{array}{cc}
\left(\begin{array}{cc}
(0.0000,0.0100,0.0100,0.3162 ; 0.9,0.9) \\
(0.1220,0.5910,0.5910,0.8768 ; 1.0,1.0)
\end{array}\right) & \cdots & \left(\begin{array}{cc}
(0.0625,0.0500,0.0500,0.8409 ; 0.9,0.9) \\
(0.0000,0.0010,0.0010,0.3162 ; 1.0,1.0)
\end{array}\right) \\
\vdots & \ddots & \vdots \\
\left(\begin{array}{cc}
(0.0006,0.1562,0.1562,0.6287 ; 0.9,0.9) \\
(0.0625,0.5000,0.5000,0.8409 ; 1.0,1.0)
\end{array}\right) & \cdots & \left(\begin{array}{cc}
(0.0625,0.5000,0.5000,0.8409 ; 0.9,0.9) \\
(0.0005,0.1562,0.1562,0.6287 ; 1.0,1.0)
\end{array}\right)
\end{array}\right)
$$

### 4.2. Stage 2: Establish the CM-IT2 FS-Based BN Model

4.2.1. Determine the Nodes

The DFEE risk for the construction project in XNPCL was defined as leaf nodes, and indexes and sub-indexes in Table 3 were defined as middle nodes and root nodes, respectively.

# 4.2.2. Fuse the CM-IT2 FS-Based Conflicting Information and Determine the CM-IT2 FS-Based a Priori Probabilities 

The evidence matrix $\widetilde{M}$ was created, the CM-IT2 FS-based conflicting information was fused, and the CM-IT2 FS-based a priori probabilities of root nodes were determined through the Section 3.2.2, and the results are shown as follows:
![img-2.jpeg](img-2.jpeg)

Taking the assessment index $\mathrm{R}_{11}$ as an example, its CM-IT2 FS-based a priori probability is shown in Table 4.

Table 4. CM-IT2 FS-based a priori probability.


### 4.2.3. Determine the Conditional Probabilities

The conditional probabilities of non-root nodes were determined through Section 3.2.3. Some conditional probabilities are shown in Table 5.

Table 5. Some conditional probabilities.


Table 5. Cont.


Through the above Sections 4.2.1-4.2.3, the CM-IT2 FS-based BN model, as shown in Figure 3, was created.
![img-3.jpeg](img-3.jpeg)

Figure 3. CM-IT2 FS-based BN model.
4.3. Stage 3: Conduct the fuzzy BN Inference
4.3.1. Reduce the CM-IT2 FS-Based a Priori Probabilities to the CM-IT1-FS-Based Ones

The CM-IT2 FS-based a priori probabilities were reduced to the CM-IT1 FS-based ones through Section 3.3.1. Taking the assessment index $R_{11}$ as an example, its CM-IT1 FS-based a priori probability is shown in Table 6.

Table 6. CM-IT1 FS-based a priori probability.


# 4.3.2. Propose a New Fuzzy BN Inference Algorithm 

The proposed new fuzzy BN inference algorithm from LHS is shown in Definition 13. The sampling number was set as 1000 .

### 4.3.3. Conduct the Fuzzy BN Positive Inference

The fuzzy occurrence probability of the DFEE risk was calculated using the proposed fuzzy BN inference algorithm (Algorithm 1), and Figure 4 shows the risk prediction result. The prediction result indicates that the DFEE risk was assessed as low risk (level 2).

![img-4.jpeg](img-4.jpeg)

Figure 4. Fuzzy occurrence probability of the DFEE risk.

# 4.3.4. Conduct the Fuzzy BN Reverse Inference 

The fuzzy SPM was calculated using the proposed fuzzy BN inference algorithm (Algorithm 1), and Figure 5 shows the boxplot of the fuzzy SPM of the assessment index $\mathrm{R}_{11}$.
![img-5.jpeg](img-5.jpeg)

Figure 5. Boxplot of fuzzy SPM.
As shown in Figure 5, the scatter plots of the fuzzy SPM for the assessment index $\mathrm{R}_{11}$ followed a normal distribution. The sampling numbers near the upper margin ( 0.2380 ) and the lower margin ( 0.1562 ) were quite small. The sampling numbers from the upper quartile ( 0.2089 ) to the lower quartile ( 0.1868 ) were large. The length from the upper

quartile to the lower quartile was short. The above analysis indicated that the fuzzy SPM for the assessment index $\mathrm{R}_{11}$ was ideal.

# 5. Validation and Discussion 

For the sake of validating the availability of the proposed fuzzy BN inference approach for risk assessments, we conducted the following two tasks.

### 5.1. The BN Positive Inference Results Were Analyzed

The CM-IT2 FS-based, CM-IT1 FS-based, and traditional CM-crisp value-based a priori probabilities were compared and analyzed. Taking the assessment index $\mathrm{R}_{11}$ as an example, its coefficient $K$ was 0.9986 , and this indicates that the information from experts' knowledge was highly conflicting. Modified D-S ET was utilized to fuse the above three kinds of a priori probabilities, and the fusion results are shown in Table 7.

Table 7. Comparison of fusion results.


Then, the BN positive inference was conducted, and the DFEE risk prediction results are shown in Figure 6. For high risks, the ranking of the obtained occurrence probabilities was as follows: proposed fuzzy BN inference algorithm ( $14.67 \%$ ) > CM-IT1 FS-based fuzzy BN inference algorithm $(10.39 \%)>$ traditional CM-crisp value-based BN inference algorithm $(6.82 \%)$.
![img-6.jpeg](img-6.jpeg)

Figure 6. DFEE risk prediction results. Note: Occurrence probabilities were obtained using the proposed fuzzy BN inference algorithm and the CM-IT1 FS based fuzzy BN inference algorithm, and they are the mean values of the sampling values.

The reasons for the above ranking were as follows. Most a priori probabilities obtained using the CM-IT1 FS-based fuzzy BN inference algorithm and the traditional BN inference algorithm were assigned to low and medium risks (levels 1, 2, and 3), but high risks (levels 4 and 5) were underestimated. When the realistic DFEE risk is high, the risk prediction result obtained using the proposed fuzzy BN inference algorithm can truly reflect the actual situation. This is of great help for decisionmakers to take timely corrective actions to avoid the risk of accidents.

# 5.2. The BN Reverse Inference Results Were Analyzed 

The BN reverse inference was conducted. The SPMs for each root node were calculated; the results are shown in Table 8, and the rankings of SPMs for each root node are shown in Table 9. In Tables 8 and $9, \mathrm{SPM}_{1}$ and $\mathrm{SPM}_{2}$ represent the obtained mean values of fuzzy SPMs using the proposed fuzzy BN inference algorithm and the CM-IT1 FS-based fuzzy BN inference algorithm, respectively, and $\mathrm{SPM}_{3}$ represents the obtained SPM using the traditional CM-crisp value-based BN inference algorithm.

Table 8. SPM calculation results.


Table 9. SPM rankings.


As shown in Table 8, the order of SPM was $\mathrm{SPM}_{3}>\mathrm{SPM}_{2}>\mathrm{SPM}_{1}$. As shown in Table 9, four risk factors containing $\mathrm{R}_{12}, \mathrm{R}_{21}, \mathrm{R}_{32}$, and $\mathrm{R}_{11}$ had a great impact on the occurrence of the DFEE accidents.

The reasons for the above results were as follows: When compared with the CMIT1 FS-based a priori probability and the CM-crisp value-based a priori probability, the CM-IT2 FS-based a priori probability had a wider range of values because it expressed more uncertain, fuzzy, random, and conflicting information. The comparative result is shown in Table 7. When calculating the fuzzy SPM of root node $X_{i}$ using the proposed fuzzy BN inference algorithm, we assumed that the a priori probability of $X_{i}$ subordinating to the $j$-th level was 1 , and the a priori probabilities subordinating to the other four risk levels were 0 , and this would change its fuzzy a priori probability. Meanwhile, in the process of random sampling for fuzzy a priori probabilities of other root nodes, it would produce some difference among sampling values and CM-crisp value-based a priori probabilities. This process compensated for the changing value of fuzzy a priori probability of root node $X_{i}$ to some extent, which caused little change in the fuzzy occurrence probability of leaf nodes, making $\mathrm{SPM}_{1}$ smaller than $\mathrm{SPM}_{1}$ and $\mathrm{SPM}_{3}$.

## 6. Conclusions

In our study, a new fuzzy BN inference approach for risk assessments was proposed on the basis of CM, IT2 FS, IT2 FLS, D-S ET, and LHS methods. The DFEE risk prediction and DFEE risk sensitivity analysis were conducted using the proposed fuzzy BN inference algorithm. The DFEE risk prediction result indicated that the DFEE risk was assessed as low risk, however, attention should be paid to the potential high risks. The DFEE risk sensitivity

analysis result indicated that four risk factors had a great impact on the occurrence of DFEE accidents, and this provided the clear direction for XNPCL to continuously improve the DFEE risk management process.

However, our study has the following two limitations: One is that we only analyzed the DFEE risk for the NPP construction project. The other is that we only used the proposed approach for a typical case. Therefore, in a future study, we will expand the studied risk to other risks, which include work at height, temporary electricity, occupational health, etc., to propose a universal fuzzy BN inference approach for safety-related risk assessments, and then we will use the proposed approach in other projects.

Author Contributions: Conceptualization, J.X.; methodology, R.D.; software, T.D.; validation, M.Z.; formal analysis, R.D. and M.Z.; resources, T.Y.; data curation, Y.S.; writing-original draft preparation, J.X.; writing-review and editing, Y.S.; visualization, T.D.; supervision, T.Y.; project administration, Y.S.; funding acquisition, Y.S. All authors have read and agreed to the published version of the manuscript.

Funding: This research was funded by the National Natural Science Foundation of China, grant number 52174189 and 11805094, and the Natural Science Foundation of Hunan Province, grant number 2023JJ10035.

Data Availability Statement: Data are contained within the article.
Conflicts of Interest: The authors declare no conflicts of interest.
