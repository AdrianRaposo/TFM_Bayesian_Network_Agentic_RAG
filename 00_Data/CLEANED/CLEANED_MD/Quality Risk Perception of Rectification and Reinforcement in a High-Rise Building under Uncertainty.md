# Article 

## Quality Risk Perception of Rectification and Reinforcement in a High-Rise Building under Uncertainty

Liangtao Bu * and Hui Yue *


#### Abstract

College of Civil Engineering, Hunan University, Changsha 410082, China * Correspondence: plt63@hnu.edu.cn (L.B.); yuehui@hnu.edu.cn (H.Y.)


#### Abstract

There are many complex and uncertain factors in the process of building rectification and reinforcement that can easily lead to construction quality failures. This study develops a novel hybrid risk analysis approach to perceive the construction quality risk under uncertainty by integrating the extension theory (ET), the cloud model (CM), the Dempster-Shafer (D-S) evidence theory and the dynamic Bayesian network (DBN). The extended cloud model (ECM) combining the ET and the CM is not only effective in avoiding information loss, but is also capable of dealing with the ambiguity and randomness in risk assessment. The ECM is employed to construct the basic probability assignments (BPA) of risk factors across different risk states. The improved D-S evidence theory considering the expert importance coefficient is used for the fusion of expert judgments. A DBN model integrating monitoring indicators is established to predict the dynamics of overall quality risk during rectification and reinforcement. Then, the measured data of settlement difference and settlement rate are fed back to the DBN model to update the risk assessment results in real time. Finally, a case study of the rectification and reinforcement in a high-rise building is taken to verify the feasibility and validity of the developed risk analysis approach. The risk assessment results better reflect the unexpected risk events in actual construction. The proposed approach provides a research paradigm for quality risk assessment of similar rectification and reinforcement projects.


Keywords: building rectification; risk analysis; extension theory; cloud model; D-S evidence theory; dynamic Bayesian network

## 1. Introduction

With the continuous development of urbanization and the improvement of construction technology, the proportion of high-rise and super high-rise buildings is increasing. Due to human influence or natural disaster damage, buildings may be tilted or deformed during construction or use. For most inclined buildings, if it is proved by testing and appraisal that they still have value for continuous use, then by adopting rectification and reinforcement measures to restore their functions, huge economic losses can be recovered. China has gradually shifted the development direction of the construction industry from new buildings to the reinforcement and renovation of existing buildings, so as to achieve the purpose of reducing costs, shortening construction periods and saving resources. In addition, a series of environmental and social problems can be avoided. However, the lack of specialized guidance on rectification and reinforcement for buildings has led to endless cases of failure. Therefore, the construction risk of such projects has always been high, especially for high-rise buildings [1]. It is not uncommon for high-rise buildings to experience superstructure damage, wall cracking, tilting and even collapse. The large loads, small foundation area, and high center of gravity make inclined high-rise buildings have large additional overturning moments, which make them very sensitive to external disturbances. The rectification and reinforcement of high-rise buildings are huge challenges for engineers. Risk is inherent in project execution and it cannot be completely eliminated; rather, it can be effectively managed to mitigate impacts that may hinder project success [2].

If the potential risks are identified, evaluated and monitored at the initial stage, and preventive and corrective risk response measures are taken, the probability of project success can be significantly improved.

# 2. Literature Review 

For the rectification and reinforcement of existing buildings, Wang and Li [3] conducted a risk assessment based on Bayesian networks for rectification and reinforcement of an 11-story high-rise building. Zhou et al. [4] used the integrated bundling technique for the first time to correct the deviation of the pagoda body of Dinglin Temple in China. Peng et al. [5] introduced a special technique to rectify the deviation of the building near the foundation pit, and investigated the performance of the technique through field tests. Xiao et al. [6] proposed two under-excavation calculation formulas for hole spacing and hole diameter applicable to general deviation rectification projects and verified them by examples. Xiao et al. [7] introduced plane strain numerical simulation to systematically probe the under-excavation mechanism for building rectification, and derived the two key parameters of optimal hole spacing and hole diameter. Chai et al. [8] estimated the jacking force required for the rectification of rigid inclined piles in cohesive soil using the $F L A C^{3 D}$ numerical method and carried out a detailed parametric analysis, which provided a basis for safer and more economical rectification design. The above literature focuses on the research at the technical level: one is to propose an innovative rectification and reinforcement scheme based on the analysis of the causes of uneven settlement of the foundation under complex conditions [4,5]; the other is to pay more attention to the mechanism behind the deviation rectification and provide scientific theoretical formulas for the rectification design [6,7,8]. However, there have been very few studies on the identification of potential risk factors for building rectification and reinforcement and the impact of these risk factors on construction quality.

The quality state of the rectification and reinforcement system will be affected by a variety of factors. For risk modeling of complex engineering systems, probabilistic risk analysis (PRA) can not only be used to identify possible failure scenarios, but can also be used to estimate the probability of failure occurrence [9]. The PRA provides access to critical risk factors and related causality, which can help to provide decision support for quality or safety assurance in advance. PRA has been widely used in complex systems with various risk factors under uncertainty, such as construction projects, operating subways and other civil infrastructure systems [10,11]. Fault tree analysis (FTA), event tree analysis (ETA) and Bayesian networks (BNs) are common methods in PRA [12]. However, FTA faces difficulties in establishing dependencies for events, updating probabilities, and handling uncertainty, and ETA cannot handle complex dependency models well to obtain success or failure probabilities [13]. As the fault tree or event tree grows, its structure becomes not intuitive and the computational complexity increases. The limitations of FTA and ETA necessitate the utilization of BNs, a probabilistic graphical model, to effectively capture causal relationships between risk factors through conditional probability tables (CPT). Due to its ability to update and correct probabilities, BNs can perform predictive and diagnostic reasoning to support decision making on construction risk management measures [14]. Wu et al. [15] conducted a dynamic safety analysis of tunnel-induced pavement damage based on dynamic Bayesian networks. Zhang et al. [16] analyzed the safety performance of buried pipelines adjacent to the Wuhan Yangtze River Tunnel Project using the fuzzy Bayesian network (FBN). Wang and Chen. [17] evaluated the safety risk of a metro construction project based on fuzzy comprehensive Bayesian networks (FCBN). Pan et al. [18] conducted a risk analysis on the structural health status of operating subway tunnels based on the combination of interval-valued fuzzy sets, the D-S evidence theory and FBN. Guan et al. [19] adopted the fuzzy Bayesian belief network (FBBN) approach to systematically assess the risk of an international engineering project. Xiang et al. [20] established a Bayesian network based on real case data from a Canadian pipeline operator and existing

fault trees in the literature to assess the risk probability of third-party excavation activities damaging existing pipelines.

Remarkably, traditional BNs can only be constructed based on crisp sets and probabilities. Due to the lack of data and incomplete knowledge, it is difficult to obtain accurate information from complex systems [21]. As a supplement to the measurement data, domain experts can roughly estimate the probability with a series of linguistic terms, and then convert the linguistic terms into quantitative values to improve the traditional BNs. There are three main ways to achieve this transformation: Cantor set, fuzzy set and extension set. The range of Cantor sets is $\{0,1\}$, where 0 and 1 indicate whether an element belongs to a set, so Cantor sets are often used to solve binary problems. By introducing the concept of membership degree, fuzzy sets can not only describe whether an element belongs to a certain set, but can also describe its degree by the number between 0 and 1 . Therefore, fuzzy sets are able to deal with the problem of unclear boundaries of linguistic concepts. Extension sets extend the range of values to $(-\infty,+\infty)$, making it possible to use raw data directly without normalization, which effectively avoids information loss [22]. The extension theory (ET) can solve the contradiction problem by adding the description of matter properties. However, it cannot address the uncertainty caused by the change in risk factors and the fuzziness of prior knowledge. The cloud model (CM) can realize the conversion between qualitative concepts and quantitative representations through a cloud generator, and has been demonstrated to be an effective approach for dealing with the uncertainty of stochasticity and ambiguity [23]. Therefore, the integration of the ET and the CM can not only resolve the paradoxical problem of standardizing raw data, but can also double the uncertainty during the conversion of qualitative concepts and quantitative values.

Another issue that needs attention is how to integrate the judgments from different experts in a more effective way. The Dempster-Shafer (D-S) evidence theory, one of the most exemplary information fusion techniques, has been widely used in expert systems to integrate a wide range of knowledge and data into a generalized framework due to its excellent performance in dealing with cognitive uncertainty, conflict, and bias [24]. The prevalence of evidence conflicts is the biggest obstacle to the greater application of the evidence theory, which results in counterintuitive outcomes. In recent years, some studies have improved the evidence theory from the evidence itself [25] and the fusion rules [18,26]. However, another problem is how to allocate conflicts when the contribution of experts to the decision results is different. Most of the existing studies use an averaging of the evidence set to eliminate conflicts [18,27], while few studies focus on the importance of different evidence sources.

With the development of construction informationization, a large amount of data has been collected during construction, such as digging data and monitoring data. How to effectively use these data to control the occurrence of construction quality accidents is the key issue of current research [28]. Most scholars utilize the patterns of monitoring data to validate the reasonableness of the assessment results [29,30], without directly combining monitoring data with risk analysis [31]. Wu et al. [32] determined the risk factors through the data learning method based on the existing monitoring data to parameterize the risk assessment model. However, the model could not update the risk assessment results in real time according to the newly acquired monitoring data, and the relationship between the acceptance criteria for risk assessments and the early warning of monitoring indicators was not clear. Practice has shown that the risk early warning results calculated by risk assessment models are often inconsistent with the warning results when monitoring indicators reach thresholds. The single use of monitoring indicators for early warning cannot reflect the overrun of monitoring fluctuations generated by accidental factors during construction, which is easy to miss the report and affect the construction process. Therefore, it is necessary to incorporate the monitoring indicator thresholds into the risk assessment model to establish a unified early warning model to facilitate dynamic risk management of the construction process by project managers.

Existing research focuses on exploring the innovative implementation and scientific design of rectification and reinforcement techniques, and a gap still exists in the body of knowledge related to risk analysis under uncertainty. Therefore, this study attempts to construct a novel hybrid analysis approach for the quality risk perception of building rectification and reinforcement. This approach focuses on (a) constructing basic probability assignments (BPA) for multisource evidence using the ET and the CM, (b) improving the D-S evidence theory by taking into account expert contributions, and (c) incorporating monitoring indicators and their thresholds into the DBN model.

The structure of the rest of this paper is as follows: Section 3 provides the theoretical basis for risk assessment; Section 4 describes the proposed risk assessment model; Section 5 conducts a case empirical study; Section 6 analyzes and discusses the results of the risk assessment; and Section 7 presents the conclusions and future perspectives.

# 3. Methods 

### 3.1. The Cloud Model

Let $U=\{X\}$ be a quantitative domain represented by exact values, and $T$ be a qualitative concept related to $U$. The affiliation $\mu_{T}(x)$ of the element $x$ in $U$ to the qualitative concept $T$ is a random number with a stable tendency, which is valued in $[0,1]$. A cloud is composed of numerous cloud droplets. Each cloud droplet $\left(x, \mu_{T}(x)\right)$ is a point where the qualitative concept maps to the number field space [33].

Expectation $\left(E_{x}\right)$, entropy $\left(E_{n}\right)$ and hyperentropy $\left(H_{e}\right)$ are used to characterize the fuzziness, randomness and discreteness of human knowledge and objective things, reflecting the quantitative characteristics of qualitative concepts [34]. $E_{x}$ reflects the central position of the cloud droplets, which is the most representative point of the qualitative concept $T . E_{n}$ is a characterization of the uncertainty of the qualitative concept $T$, which dictates the scope of values that can be considered in the domain. $H_{e}$ reflects the discretization of the cloud droplets and is an uncertainty measure for $E_{n}$. The digital characteristics of the cloud is denoted as $T=\left(E_{x}, E_{n}, H_{e}\right)$. Given these three numerical characteristics, it is possible to generate cloud droplets by the forward cloud generator, from which cloud models belonging to different grades for a particular attribute can be established. The above mathematical concepts can be expressed as follows:

$$
\begin{gathered}
\mu_{T}(x): U \rightarrow[0,1] \forall x \in U, x \rightarrow \mu_{T}(x) \\
\mu_{T}(x)=\exp \left(-\frac{\left(x-E_{x}\right)^{2}}{2 E_{n}^{\prime 2}}\right)
\end{gathered}
$$

### 3.2. The Extension Theory

Things with qualitative description and quantitative attributes in the objective world can be modeled with matter elements. The matter element is defined as an ordinal group with three basic elements (i.e., name $N$, characteristic $C$, and characteristic value $V$ ), denoted as $R=(N, C, V)$. Matter element is a crucial concept in the extension theory (ET). It can fully consider the quality and quantity of matter, and transform the change in matter into the change in matter elements. The ET provides a formal tool for solving contradictory problems by quantitative and qualitative methods [22]. Suppose the matter $N$ possesses $n$ characteristics $c_{1}, c_{2}, \ldots, c_{n}$, corresponding to $n$ characteristic values $v_{1}, v_{2}, \ldots, v_{n}$ and $n$ value intervals $\left(a_{i}, b_{i}\right)$, then the matter element $R$ can be extended to an $n$-dimensional matter element as in Equation (3):

$$
R=(N, C, V)=\left[\begin{array}{cccc}
N & c_{1} & v_{1} \\
& c_{2} & v_{2} \\
& \vdots & \vdots \\
& c_{n} & v_{n}
\end{array}\right]=\left[\begin{array}{cccc}
N & c_{1} & \left(a_{1}, b_{1}\right) \\
& c_{2} & \left(a_{2}, b_{2}\right) \\
& \vdots & \vdots \\
& c_{n} & \left(a_{n}, b_{n}\right)
\end{array}\right]
$$

# 3.3. The D-S Evidence Theory 

The Dempster-Shafer (D-S) evidence theory was first proposed by Dempster, A.P. [35] and then further popularized and developed by Shafer, G. [36]. The D-S evidence theory has been widely used in the fields of multisensor information fusion [37], uncertain reasoning [38], and pattern recognition [39]. Suppose that the recognition framework $\Theta=\left\{A_{1}, A_{2}, \ldots, A_{k}\right\}$ is a finite nonempty set of mutually exclusive and common exhaustive events. Given the discernment frame $\Theta$, the mass function $m: 2^{\Theta} \rightarrow[0,1]$ is called the basic probability assignment (BPA) when it satisfies the conditions of Equation (4).

$$
\left\{\begin{array}{l}
m(\varnothing)=0 \\
\sum_{A \in 2^{\Theta}} m(A)=1
\end{array}\right.
$$

where $\varnothing$ is the empty set; $2^{\Theta}$ is a power set of $\Theta$; and $m(A)$ is referred to as the mass function of $A(A \subseteq \Theta)$, which denotes the confidence of subset $A$ as a belief measure in the interval $[0,1]$.

Based on Dempster's combination rule, the fusion result of $n$ independent evidences $m_{1}, m_{2}, \ldots, m_{n}$ is:

$$
\begin{aligned}
& m(A)=\left\{\begin{array}{lr}
\frac{1}{1-K} \sum_{A_{i} \cap A_{j} \cap \ldots \cap A_{k}=A} m_{1}\left(A_{i}\right) m_{2}\left(A_{j}\right) \ldots m_{n}\left(A_{k}\right) A \neq \varnothing \\
0 & A=\varnothing
\end{array}\right. \\
& \text { with } 0<K=\sum_{A_{i} \cap A_{j} \cap \ldots \cap A_{k}=\varnothing} m_{1}\left(A_{i}\right) m_{2}\left(A_{j}\right) \ldots m_{n}\left(A_{k}\right)<1
\end{aligned}
$$

where $i, j, k$ stand for the $i$ th, $j$ th, and $k$ th hypotheses; and $K$ is the conflict coefficient between $n$ independent evidences, with a larger value of $K$ indicating a greater degree of conflict.

### 3.4. Bayesian Networks

The Bayesian network (BN) is a robust probabilistic model composed of a directed acyclic graph (DAG) and a conditional probability table (CPT). The DAG consists of nodes and directed edges, where nodes represent variables and directed edges between nodes indicate interactions between factors. The CPT is used to denote the relationship between a node and its parent nodes, which plays an important role in obtaining the marginal and posterior probabilities. A possible value of a discrete variable is called a state of the node.

Assume that a set of random variables $X=\left\{X_{1}, X_{2}, \ldots, X_{n}\right\}$ are the $n$ root nodes in the BN model. In accordance with the chain rule under the assumption of conditional independence, the joint probability distribution of all variables is defined as Equation (6). The edge probability of a node can be determined by the fuzzy marginalization rule as shown in Equation (7), which allows for the prediction of the probability of a risky event. Sensitivity analysis is used to explore the effect of small changes in inputs on system performance, quantified by the sensitivity performance measure (SPM), as shown in Equation (8). When SPM is close to $1, X_{i}$ is more likely to be the direct cause of accident $Y$. Therefore, the focus of risk control should be on risk factors with large SPM values. According to Bayes' rule, when the probability of the leaf node $Y$ being in the state $y$ is known, the posterior probability of the risk factor $X_{i}$ can be diagnostically inferred from Equation (9). The inference results can be updated based on the new observational evidence $X_{k}=e$ through Equation (10).

$$
P\left(X_{1}, X_{2}, \ldots, X_{n}\right)=\prod_{i=1}^{n} P\left(X_{i} \mid p a\left(X_{i}\right)\right)
$$

where $p a\left(X_{i}\right)$ represents the set of the parent nodes of $X_{i}$; and $P\left(X_{i} \mid p a\left(X_{i}\right)\right)$ is the CPT of $X_{i}$.

$$
P(Y=y)=\sum_{i=1}^{n} P\left(X_{i}=x_{i}\right) \times P\left(Y=y \mid X_{i}=x_{i}\right)
$$

where $y=\left\{y_{1}, y_{2}, \ldots, y_{p}\right\}$ is the $p$ states of the leaf node $Y$; and $x_{i}=\left\{x_{i}^{1}, x_{i}^{2}, \ldots, x_{i}^{q}\right\}$ is the $q$ states of the root node $X_{i}$.

$$
\operatorname{SPM}\left(X_{i}\right) \cong \frac{1}{q} \sum_{r=1}^{q}\left|\frac{p\left(Y=y \mid X_{i}=x_{i}^{r}\right)-p(Y=y)}{p(Y=y)}\right|
$$

where $q$ is the total number of risk levels for factor $X_{i}$.

$$
\begin{gathered}
P\left(X_{i}=x_{i} \mid Y=y\right)=\frac{P\left(X_{i}=x_{i}\right) \times P\left(Y=y \mid X_{i}=x_{i}\right)}{P(Y=y)} \\
P\left(X_{i} \mid e\right)=\frac{P\left(X_{i}, e\right)}{P(e)}=\frac{\prod_{i=1}^{n} P\left(X_{i} \mid P a\left(X_{i}\right), e\right)}{\sum_{X_{i} \backslash X_{k}} P\left(X_{i}, e\right)}
\end{gathered}
$$

# 3.5. Dynamic Bayesian Networks 

In practice, the probability of a risk event occurs dynamically over time, but Bayesian networks cannot reflect the time-varying nature of node states. The dynamic Bayesian network (DBN) is an extension of static BN in the time dimension to characterize the change in the probability of occurrence of risk events over time. The DBN is composed of the initial network $B_{0}$ and the transfer network $B_{\rightarrow}$ [40]. $B_{0}$ is a static BN, a priori network for the DBN. $B_{\rightarrow}$ is a state transfer network between two adjacent time slices. The transfer probability of any two adjacent time segments is defined as Equation (11). The DBN is usually assumed to satisfy the stability and Markovianity of Equations (12) and (13) [41].

$$
P\left(X_{t} \mid X_{t-1}\right)=\prod_{i=1}^{N} P\left(X_{t}^{i} \mid P a\left(X_{t}^{i}\right)\right)
$$

where $X_{t}^{i}$ is the $i$ th node on the $t$ th time slice; $P a\left(X_{t}^{i}\right)$ is the set of parent nodes of $X_{t}^{i}$; and $N$ denotes that there are $N$ nodes.

$$
\begin{gathered}
P\left(X_{t} \mid X_{t-1}\right)=P\left(X_{t+1} \mid X_{t}\right) \\
P\left(X_{t} \mid X_{1}, X_{2}, \ldots, X_{t-1}\right)=P\left(X_{t} \mid X_{t-1}\right)
\end{gathered}
$$

When building BNs for complex projects, the number of terms in the CPT increases exponentially with the number of parent nodes. The Noisy-OR gate model can greatly reduce the workload of experts by making the number of terms in the CPT increase linearly [42]. In addition, this study showed that the reasoning results of BNs built based on the Noisy-OR gate model and those built directly based on the experts' experience present no statistically significant difference [43]. Thus, the Noisy-OR gate model can be used instead of the empirical method to calculate the conditional probabilities. It is worth noting that the Noisy-OR gate model can only compute binary variables. The Noisy-MAX model is a generalization of the Noisy-OR gate model to multiple factors, where nodes can be multiple states [44]. The model assumes that the variable $Y$ must be a sequential variable and the influences are mutually independent. The conditional probability of a risk event can be calculated from Equations (14) and (15).

$$
\begin{gathered}
P(Y \leq y \mid X)=\prod_{i}\left[\sum_{Y \leq y} P\left(Y=y \mid X=x_{i}\right)\right] \\
P(Y \mid X)=\left\{\begin{array}{cl}
P(Y \leq y \mid X)-P(Y \leq y-1 \mid X) & y \neq y_{\min } \\
P(Y \leq y \mid X) & y=y_{\min }
\end{array}\right.
\end{gathered}
$$

# 4. Construction of the Improved DBN Risk Assessment Model with the ECM and the D-S Evidence Theory 

### 4.1. Risk Factors Identification

In order to return the tilted building to normal use, two aspects of work are required: one is to make the tilt rate of the building meet the code requirements by correcting the tilt, and the other is to prevent the structure from re-tilting or reverse tilting by reinforcing the foundation. The commonly employed methods for deviation rectification can be categorized into the forced settlement method, lifting method, lateral loading method, and reservation method based on their underlying principles. The pressure grouting method and the static pressure pile method are extensively used for foundation reinforcement. This study focuses on the potential quality risk of the forced settlement method combined with the pressure grouting method for the rectification and reinforcement of a high-rise building. On the basis of literature research and typical case analysis, the risk factors in the process of building rectification and reinforcement are classified and summarized to form the initial risk assessment index system by comprehensively considering geological conditions, design, construction and management. Through the actual construction investigation, the corresponding risk checklist is established. The checklist is an effective way to provide an overall understanding of project issues and centrally manage all available resources [45]. Then, the risk indicators are further supplemented, merged and deleted according to the opinions of the expert group. Finally, combined with the specification review, a quality risk evaluation index system consisting of 14 factors for 3 key processes is determined, as shown in Figure 1.
![img-0.jpeg](img-0.jpeg)

Figure 1. Construction quality risk assessment index system.

### 4.2. Quantification of Risk Levels

In a complex system without sufficiently precise data and quantifiable factors, domain experts are expected to provide evaluations based on their experience and knowledge. In fact, the experts are accustomed to describing characteristics in the form of natural language expressions, such as words and sentences. For example, the level of risk is often depicted as "Low", "High" or "Very High". Utilizing the advantages of the CM in dealing with uncertainty, the linguistic terms of risk level are numerically represented by cloud digital characteristics. In the risk assessment of building rectification and reinforcement, $E_{x}$ denotes

the quantitative point that best represents the risk level. $E_{n}$ reflects the randomness and ambiguity of the evaluation results. $H_{e}$ reflects the uncertainty of the risk assessment model. The digital characteristics of the CM are computed through the quantized intervals of the comment set. The specification requires the acceptance of construction quality based on the principle of maximum safety assurance. Therefore, the range of intervals in the hazardous state is slightly larger than that in the safe state [46]. Table 1 presents the comment set of risk level and its quantification interval. The interval is denoted as $\left(C_{\min }, C_{\max }\right)$, where $C_{\text {min }}$ and $C_{\text {max }}$ represent the interval limits. The numerical characteristics of the standard cloud model are obtained through Equation (16). $k$ is a constant, usually set to 0.1 . Figure 2 illustrates the cloud models for nine risk levels.

$$
\left\{\begin{array}{l}
E_{x}=\left(C_{\min }+C_{\max }\right) / 2 \\
E_{n}=\left(C_{\max }-C_{\min }\right) / 6 \\
H_{e}=k E_{n}
\end{array}\right.
$$

Table 1. Linguistic terms and cloud numerical characteristics of risk levels.


![img-1.jpeg](img-1.jpeg)

Figure 2. Cloud models of nine risk levels.

# 4.3. Construction of the BPA by the ECM 

By integrating the CM and the ET, the ECM is proposed to analyze the uncertainty in risk assessment. Specifically, the CM is used to replace the value interval in the ET, as shown in Equation (17). The cloud numerical characteristics $\left(E_{x}, E_{n}, H_{e}\right)$ can be seen as the quantized values of $C$ with respect to the matter element $N$.

$$
R=[N, C, V]=\left[\begin{array}{cc}
N & c_{1} & \left(E_{x, 1}, E_{n, 1}, H_{e, 1}\right) \\
& c_{2} & \left(E_{x, 2}, E_{n, 2}, H_{e, 2}\right) \\
& \vdots & \vdots \\
& c_{n} & \left(E_{x, n}, E_{n, n}, H_{e, n}\right)
\end{array}\right]
$$

For each risk indicator in the ECM, its risk level evaluation value is considered to be a cloud droplet satisfying the normal distribution $N \sim\left(E_{x, i}, E_{n, i}^{2}\right)$. The membership degree of the measured value $v_{i}$ of the risk index $X_{i}$ to the $j$ th risk level is considered as the BPA, which can be calculated by Equation (18). Since $\sum_{A \in \Theta} m(A)=1$, the BPA of each piece of evidence is required to be normalized before data fusion.

$$
\begin{aligned}
& m_{i}\left(A_{j}\right)=\mu_{i j}=\exp \left(-\frac{\left(x_{i}-E_{x, i i}\right)^{2}}{2\left(E_{n, i}^{\prime}\right)^{2}}\right) \\
& (i=1,2, \ldots, 14 ; j=1,2, \ldots, 9)
\end{aligned}
$$

# 4.4. The Improved D-S Evidence Theory 

In reference to the hybrid evidence fusion rule proposed by Zhang, L. et al., evidence conflicts were judged by the threshold of $K$ [47]. The threshold was set to 0.95 because a $5 \%$ measurement error is acceptable in practical construction and $p>0.05$ is usually defined as a significant difference. In the general hybrid fusion rule, all evidence is considered equal and the weight of the individual pieces of evidence is ignored. By considering the expert title $(\alpha)$, education $(\beta)$, and working years $(\chi)$, an expert importance coefficient $\eta$ is proposed to reveal the expert's ability to evaluate a given proposition. The specific scoring criteria are shown in Table 2. The weights of the experts can be determined by Equation (19). The improved D-S evidence rule is given in Equation (20).

$$
\begin{gathered}
w_{i}=\frac{\eta_{i}}{\sum_{i=1} \eta_{i}}=\frac{\alpha_{i} \times \beta_{i} \times \chi_{i}}{\sum_{i=1} \alpha_{i} \times \beta_{i} \times \chi_{i}} \\
m(A)=\left\{\begin{array}{cl}
\frac{1}{1-K} \sum_{A_{i} \cap A_{j} \cap \ldots \cap A_{k}=A} m_{1}\left(A_{i}^{1}\right) m_{2}\left(A_{j}^{2}\right) \ldots m_{n}\left(A_{k}^{n}\right) & K<0.95 \\
\sum_{A_{i} \cap A_{j} \cap \ldots \cap A_{k}=A} m_{1}\left(A_{i}^{1}\right) m_{2}\left(A_{j}^{2}\right) \ldots m_{n}\left(A_{k}^{n}\right)+f(A) & K \geq 0.95 \\
\text { with } K=\sum_{A_{i} \cap A_{j} \cap \ldots \cap A_{k}=\varnothing} m_{1}\left(A_{i}^{1}\right) m_{2}\left(A_{j}^{2}\right) \ldots m_{n}\left(A_{k}^{n}\right)
\end{array}\right.
\end{gathered}
$$

where $f(A)=K \cdot \sum_{i=1}^{k} w_{i} m_{i}(A)$ is the probability distribution function of evidence conflict, that is, the conflict between evidence is assigned to each element of the discernment frame $\Theta$, and thus $f(A)$ satisfies $\sum_{A \subset \Theta} f(A)=K$.

Table 2. Expert importance coefficient scoring criteria.


The hybrid evidence fusion rule, which retains the advantages of classical D-S while overcoming its shortcomings in fusing high-conflict evidence, has been successfully applied in the field of construction safety [18,27]. The proposed improved hybrid fusion rule further takes into account the differences in expert contributions, which helps to obtain more convincing fusion results.

### 4.5. BN-Based Pre-Construction Risk Assessment

The BN model is determined by the network structure and the network parameters. The network structure can be built directly based on causal relationships between risk fac-

tors. Since the statistical data of construction risks are difficult to obtain, this study utilizes explicit and implicit engineering quality management knowledge from technical documents and domain experts to determine network parameters. GeNIe 3.0 is a powerful and easy-to-use software package for Bayesian modeling and inference, where the node type can be directly set as "NoisyMax" to simplify the calculation of conditional probabilities.

The rectification and reinforcement of buildings should be monitored throughout the entire process, mainly for settlement deformation of the foundations. Settlement deformation includes two control values: cumulative change amount and change rate. The cumulative settlement can help to judge whether the foundation is lifting on one side and falling on the other side, and at the same time prevent the corrected amount from exceeding the expected or the settlement at different locations from varying too much, resulting in new local uneven settlement and cracking damage. The settlement difference can be used to intuitively describe the rectification effect. The settlement rate can help to determine whether the foundation settlement reaches a stable state. Therefore, this study adopts the two monitoring indicators of settlement difference $\Delta S$ and settlement rate $V$ combined with the 14 risk factors of risk identification to establish the initial BN model. The BN model can predict the probability of occurrence of risky events through the forward reasoning technique of Equation (7), thus providing guidance for the development of preventive measures before failures occur.

# 4.6. DBN-Based Construction Dynamic Risk Assessment 

The BN model established in the above section is used as the initial network. The overall quality risk $Y$ of building rectification and reinforcement is set as a transfer node. Set the settlement difference $\Delta S$ and settlement rate $V$ as observation nodes. Take the update time of the monitoring data as the time segment, thereby extending the static BN into the DBN, as shown in Figure 3. When there are sufficient data, the transfer probability can be directly obtained by parameter learning based on methods such as maximum likelihood estimation or Bayesian estimation [48]; when the evolution mechanism of the risk probability is explicit, the transfer probability can be defined based on the Markov process or the C-K equation [49]; and when there are insufficient data and the evolution mechanism is unclear, the transfer probability is determined by expert experience [15]. Due to the lack of risk incident data, this study calculates conditional probabilities based on expert assessments. The model sets up time slices according to the observation date and updates the risk assessment results in real time with the monitoring data during the observation period.
![img-2.jpeg](img-2.jpeg)

Figure 3. DBN model structure.
The settlement difference $\Delta S$ refers to the difference of the settlement of the measuring points on both sides of the building foundation, which should meet the allowable value of the differential settlement. The Code for the Design of Building Foundation (GB50007-2011) stipulates the maximum allowable inclination rate of buildings at different heights [50]. According to the principle of similar triangles, the target settlement differences at the corresponding measurement points on both sides of the foundation with different widths

are different. The wider the foundation, the greater the allowable settlement difference. Set the maximum inclination of the foundation to $2.5 \%$. According to the distance between the corresponding monitoring points on both sides of the foundation, the maximum settlement difference allowable value can be calculated from Equation (21). Then, take the most unfavorable value 14.75 mm (rounded to 15 mm ) as the critical value of $\Delta S$.

$$
\Delta S=S_{A}-S_{B}=\alpha \cdot L
$$

where $S_{A}$ and $S_{B}$ are the settlement of points $A$ and $B$ in the inclined direction of the foundation; $L$ is the distance between points $A$ and $B$.

According to the value range of settlement rate when the settlement deformation of the building reaches a steady state as stipulated in the Code for deformation measurement of building and structure (JGJ 8-2016), $0.01 \mathrm{~mm} / \mathrm{d}$ and $0.04 \mathrm{~mm} / \mathrm{d}$ are taken as the critical values of the settlement rate $V[51]$.

According to the characteristics of construction monitoring, the settlement difference $\Delta S$ is set into five states: $\Delta S$ exceeding the measured control value is set as level V risk; exceeding $85 \%$ of the control value but not exceeding the control value is set as level IV risk; exceeding $70 \%$ of the control value but not exceeding $85 \%$ of the control value is set as level III risk; greater than $1 / 3$ of the control value less than $70 \%$ of the control value is set as level II risk; and less than $1 / 3$ of the control value is set as level I risk. The settlement rate $V$ is set into three states: $V$ greater than the maximum control value is set as level III risk, between two control values is set as level II risk, and less than or equal to the minimum control value is set as level I risk. The risk status of these two observed variables is shown in Table 3.

Table 3. Status division of observed variables.


When modeling, the settlement difference and settlement rate of each monitoring point in the monitoring data are first discretized into five states and three states according to the thresholds determined in Table 3. According to the maximum envelope principle, the most unfavorable state of the monitoring point is taken as the observational evidence inputted into the model to update the assessment results.

# 5. Case Study 

### 5.1. Project Profile

The main structure of building 2\#, located in a neighborhood of $X$ city in China, was completed in May 2020, with 32 floors above ground and 3 floors underground. The residential building is divided into two units, left (west) and right (east), both of which adopt shear wall structure, while the right unit partly adopts frame-supported shear wall structure with the conversion floor as the second floor. The foundation of the main building is reinforced concrete raft slab foundation with holding layer of grouted pebble soil, and the non-main building area (commercial podium on the south side and basement area on the north side) adopts reinforced concrete bored piles by rotary drilling.

In August 2020, the building 2\# was ready to install the elevator. During the measurement of the elevator shaft, it was found that the verticality of the elevator shaft was too large. Through on-site detection, the maximum verticality deviation was 310 mm , and the overall tilt in the north direction had exceeded the allowable value of $2.5 \%$. It has been demonstrated by experts that the main reason for the tilt of building $2 \#$ is the

uneven settlement of raft foundation. Considering that the building 2\# was inclined before it was put into use, making the elevator unable to be installed, and that the inclination was deteriorating, it was imperative to correct and reinforce it.

The project has been monitored continuously since 29 January 2021. The rectification and reinforcement of building \#2 began on 27 February 2022 and were substantially completed by 2 September 2022. The layout of the settlement deformation monitoring points is shown in Figure 4. The cumulative settlement changes and settlement velocity at each measurement point during construction are shown in Figures 5 and 6.
![img-3.jpeg](img-3.jpeg)

Figure 4. Layout of monitoring points.
![img-4.jpeg](img-4.jpeg)

Figure 5. Cumulative settlement at each measurement point.

![img-5.jpeg](img-5.jpeg)

Figure 6. Settlement velocity at each measurement point.

# 5.2. Questionnaire Survey 

For ensuring the credibility of the questionnaire data, the invited experts need to have professional knowledge and management experience related to building rectification and reinforcement. Furthermore, the participation of experts with high education and long working experience is encouraged. In terms of the number of experts, it is recommended that 3-5 experts be involved, as the marginal gains diminish as the number of experts increases [52,53]. In this study, three experts were invited to participate in the questionnaire and their basic information is shown in Table 4. The selected experts have effectively participated in various reinforcement and renovation projects, of which two experts are the main principals of the rectification and reinforcement project of this high-rise building. Therefore, their experience is of great help to the empirical study of this case.

Table 4. Profile of the three experts.


The experts conducted a systematic risk assessment for the 14 risk factors based on the comment set provided in Table 1, giving the corresponding quality risk levels, as shown in Table 5. The quantified values of the nine risk levels are defined as $0.1,0.2,0.3,0.4,0.5,0.6$, $0.7,0.8$, and 0.9 .

Table 5. Judgments from the three experts.


Table 5. Cont.


# 5.3. Fusion of Expert Judgements 

Regarding expert judgment as multiple evidence sources, the objective of information fusion is to integrate all the evidence to derive the quality risk level for each risk factor. Before fusion, BPAs are constructed using the ECM. Specifically, the BPAs for the 14 risk factors can be calculated by Equation (18) based on the cloud number characteristics corresponding to the comment set in Table 1 and the risk level evaluation value $x$ in Table 5. The expert weight vector determined from Equation (19) is ( $0.4371,0.4371,0.1258$ ). Then, the BPAs are fused in different ways according to the threshold of $K$ based on the improved D-S evidence theory. The fusion results are shown in Table 6.

Table 6. Fusion results of expert judgment.


### 5.4. Quality Risk Perception under Uncertainty

According to the dynamic risk assessment process described in Section 3, a static BN is established. The fused BPAs of 14 risk factors are used as the observation node values of the BN model, and the pre-construction risk assessment is carried out based on the prediction principle of Equation (7), as shown in Figure 7. In current construction practice, when an accident occurs for the first time, the decision maker may have organized experts to discuss the immediate cause of the accident before proposing control measures, which is likely to miss the critical time to deal with the problem and result in more serious damage. Sensitivity analysis attempts to calculate the likelihood of a consequence caused by certain causes. Once an accident occurs, it can be used to identify suspicious causes for real-time fault diagnosis. The sensitivity analysis is demonstrated in Figure 8.

![img-6.jpeg](img-6.jpeg)

Figure 7. Pre-construction risk assessment.
![img-7.jpeg](img-7.jpeg)

Figure 8. Sensitivity analysis.

Based on the initial BN, a DBN model is established to evaluate the dynamic changes in construction risk. The state transition probability of node $Y$ is set as in Table 7 to characterize the enhancement of risk over time. In the table, $t-1$ denotes the previous time segment of the $t$ th time segment. The rectification and reinforcement period of the building is divided into seven time slices based on the observation date. The most unfavorable values of the foundation settlement difference $\Delta S$ and settlement rate $V$ at the 16 monitoring points are input into the DBN model as observational evidence, which is then fed back to the transfer node $Y$ via Equation (10) to correct the risk assessment results and update the network in real time. Table 8 shows the settlement difference calculated from the cumulative settlement of the monitoring points on both sides of the foundation.

Table 7. State transition probability.


Table 8. Settlement difference of corresponding monitoring points.


# 6. Results and Discussion

From Figure 7, it can be concluded regarding the overall risk perception that there is nearly a $40 \%$ probability to rate the quality risk level for the rectification and reinforcement of this high-rise building at VH (Very High). That is to say, the prediction technology can indicate a profile and related evolution of the risk level in the process of building rectification and reinforcement before the construction quality failures occur, which works well even in the absence of a clear picture of the actual status of the risk factors. The construction of this high-rise building is in a very dangerous state overall, with $P(Y=H)+$ $P(Y=V H)+P(Y=E H)=59 \%$. Therefore, relevant risk control measures must be taken in advance to minimize the risk level and even prevent quality failures during rectification and reinforcement. Once the risk factor $\left(X_{i j}\right)$ is adjusted and optimized, the overall risk state $(Y)$ of the construction will also be updated. Eventually, the desired $P(Y)$ can be obtained with the continuous updating of the relevant risk factors. Set $X_{1}, X_{2}, X_{3}$, and $Y$ as the target nodes. $X_{3}$ is considered to be the most unfavorable risk group leading to construction quality failures. $X_{11}, X_{13}$ and $X_{25}$ are identified as the most sensitive risk factors. Therefore, more attention needs to be paid to these sensitivity indicators during

the rectification and reinforcement process of this high-rise building, aiming to manage the risks in a more effective way.

Figure 9 illustrates the dynamic changes in the probability of construction risk for the period 27 February-2 September. With the advancement of the rectification and reinforcement process, the possibility of the overall quality risk being in the VH (Very High) and EH (Extremely High) grades is increasing and the possibility of being in the H (High) and below grades is decreasing. When the rectification and reinforcement are essentially complete, the probability of the overall quality risk occurring gradually tends to be stable. The construction dynamic risk probability based on observational evidence is depicted in Figure 10.
![img-8.jpeg](img-8.jpeg)

Figure 9. Dynamic risk probability without evidence input.
![img-9.jpeg](img-9.jpeg)

Figure 10. Dynamic risk probability when inputting evidence.

Prior to 1 April, the construction risk level was at SL (Slightly Low), that is, there was a slight risk. Risks at this stage were pervasive, and some damage was acceptable and needed to be managed. In the early stage of the project, construction preparations inevitably caused some disturbance to the inclined building. To prevent the building from continuing to tilt northward and reduce the risk of subsequent construction, two rows of steel pipe piles were added to widen the north- and west-facing raft foundations. As can be seen in Figures 5 and 6, the fluctuation of settlement $S$ and settlement rate $V$ from 27 February to 1 April is relatively stable, with $\Delta S$ at approximately 5 mm and $V$ less than $0.2 \mathrm{~mm} / \mathrm{d}$.

From 1 April to 2 May, the construction risk rose to H level. It is necessary to strengthen management and take preventive measures. From 2 May to 14 July, the risk of rectification and reinforcement of the building reached VH level. Moreover, the probability of being at VH and EH levels was increasing, indicating an elevated likelihood of construction quality failures. The construction risk at this stage was high and damage was unacceptable, requiring increased monitoring and close attention to the dynamics of the risk probability. The middle of the project was in a critical period for the rectification and reinforcement of the building, and there were large-scale construction activities. Once a certain process was not operated properly, it would inevitably pose a great threat to the tilted building. This phase mainly involved the construction of high-pressure rotary spray piles and the tensioning of prestressing anchor cables. High-pressure jet grouting piles were added around the raft foundation to stabilize the geotechnical strata around the building, which inevitably induced significant disturbance to the underlying foundation soil. And since the construction needed to be carried out on the original foundation cap, it was impossible to avoid damage to its original bottom and upper steel bars during the drilling process. The deviation rectification of the building was achieved by first anchoring the prestressed anchor cable into the raft foundation, and then using the jack to apply the downward tension to the side of the raft foundation with small settlement to force the two sides of the raft foundation to reach balance. The tensioning process of prestressed anchor cable was technically complex, which required synchronous control of multiple hydraulic jacks and graded tensioning. Moreover, the settlement change in the main structure of the building under each level of load was uncertain. After each level of load was applied, the settlement must be observed until it is stable to carry out the next level of loading. It can be seen from Figures 5 and 6 that the fluctuation of settlement $S$ and settlement velocity $V$ gradually increases. From 7 April to 6 May, the fluctuation is relatively slow, with $\Delta S$ less than 10 mm and $V$ maximum $0.24 \mathrm{~mm} / \mathrm{d}$. From 6 May to 14 July, the fluctuation increase significantly, with $\Delta S$ exceeding 15 mm and $V$ maximum $0.55 \mathrm{~mm} / \mathrm{d}$.

From 14 July to 2 September, the probability of being at each risk level increased or decreased at a slower rate, but the building remained in a dangerous condition. In the later stage of the project, the rectification and reinforcement results were further consolidated and improved. The foundation beneath the raft slab was further reinforced through highpressure inclined hole grouting. The shear walls on the negative one and negative two floors were strengthened with R100 reactive powder concrete (RPC) by increasing the crosssection, while interspersing crack reinforcement and repair work on the original walls, beams, slabs and other components of the main structure. From Figures 5 and 6, it can be seen that the settlement $S$ shows a slight increase, and the settlement velocity $V$ gradually decreases to within $0.1 \mathrm{~mm} / \mathrm{d}$. It should be noted that the building had not yet fully stabilized after the rectification and reinforcement were completed. Subsequent monitoring should be continued to ensure that the settlement deformation trend of each measurement point has been stabilized without significant sudden changes, and that the settlement rate has reached the judgment standard for the stability of settlement deformation of buildings.

The dynamic changes in construction quality risk presented in Figure 10 are generally consistent with the actual rectification and reinforcement process and the fluctuating status of monitoring indicators. Therefore, the established improved DBN risk assessment model can timely and accurately reflect the dynamic change characteristics of construction risk,

and provide real-time decision support for the quality management of building rectification and reinforcement.

In the pre-construction phase, decision makers can employ the prediction technique to optimize the initial construction scheme by continuously adjusting the corresponding construction parameters to reduce the quality risk level of the system. The reinforcement company should prepare emergency supplies, equipment and personnel in advance to respond to very likely risk events. During the construction phase, abnormal contingencies can be diagnosed in real time based on the dynamic change characteristics of risks. It should be noted that the monitoring frequency should meet the requirements of real-time feedback analysis of measured data. Must be based on the feedback information to decide whether to proceed to the next procedure, adhere to the "dynamic design, information construction". By taking effective risk prevention and control measures, the rectification and reinforcement of buildings can be carried out smoothly. After the completion of the rectification and reinforcement, the overall verticality of the building should meet the requirements of the current relevant national specifications (inclination rate $\leq 2.5 \%$ ), and does not affect the later use of the building.

# 7. Conclusions 

The rectification and reinforcement of high-rise buildings are difficult, technically demanding and comprehensive, thus high-risk engineering. To evaluate the risk level of construction quality, this study proposes a novel hybrid risk analysis approach by integrating the ECM, the improved D-S evidence theory and the DBN. Important risk issues are empirically analyzed in the context of the rectification and reinforcement for a high-rise building. The main conclusions are as follows:

Based on the analysis of the rectification and reinforcement scheme adopted by the project, three key construction processes are screened out and 14 risk factors prone to inducing quality failures are identified, from which a construction quality risk assessment index system is constructed.

The proposed hybrid risk analysis approach combines the advantages of the ET, the CM, the D-S evidence theory and the DBN, which is expected to enrich risk management in the field of building rectification and reinforcement. The ECM can not only address the ambiguity and randomness in risk assessment, but can also avoid the loss of potential information. The improved D-S evidence theory takes into account differences in the contributions of different experts to the fusion results when resolving evidence conflicts, which helps to reduce errors caused by ignoring individual differences. The DBN model integrating the monitoring indicators realizes the unification of risk early warning, which can timely and accurately reflect the dynamic changes in construction risk and the dynamic impact of unexpected events on the probability of risk occurrence.

The construction quality risk perception results validate the applicability and effectiveness of the proposed risk analysis approach. The approach can also be used as a decision-support tool for systematic risk analysis of other complex projects with multiple evaluation indicators and high uncertainty.

It is important to note that the risk assessment index system determined in this study is for a specific project, and there are some differences under different rectification and reinforcement methods. The knowledge and experience of domain experts have made important contributions to the development of the risk assessment model in this study. However, the process is laborious and relies heavily on domain experts. How to establish an information management system in the field of construction engineering to realize the automatic integration of different knowledge resources is a problem to be solved.

Author Contributions: Conceptualization, L.B. and H.Y.; methodology, H.Y.; software, H.Y.; validation, L.B. and H.Y.; formal analysis, H.Y.; investigation, L.B.; resources, L.B.; data curation, H.Y.; writing—original draft preparation, H.Y.; writing—review and editing, L.B. and H.Y.; supervision, L.B.; project administration, L.B.; funding acquisition, L.B. All authors have read and agreed to the published version of the manuscript.

Funding: This research received no external funding.
Data Availability Statement: The original contributions presented in this study are included in this article, further inquiries can be directed to the corresponding authors.

Acknowledgments: The authors are grateful to the anonymous reviewers for their constructive comments.
Conflicts of Interest: The authors declare no conflicts of interest. The funders had no role in the design of the study; in the collection, analyses, or interpretation of data; in the writing of the manuscript; or in the decision to publish the results.
