# Article 

## Human Reliability Analysis for Fishing Vessels in Korea Using Cognitive Reliability and Error Analysis Method (CREAM)

Donghun Lee ${ }^{1}$ (D), Hyungju Kim ${ }^{1, *}$ (D), Kwiyeon Koo ${ }^{2}$ (D) and Sooyeon Kwon ${ }^{3}$


#### Abstract

check for updates Citation: Lee, D.; Kim, H.; Koo, K.; Kwon, S. Human Reliability Analysis for Fishing Vessels in Korea Using Cognitive Reliability and Error Analysis Method (CREAM). Sustainability 2024, 16, 3780. https:// doi.org/10.3390/su16093780


Academic Editors: Sean Loughney and Özkan Uğurlu

Received: 15 March 2024
Revised: 26 April 2024
Accepted: 28 April 2024
Published: 30 April 2024

## (0)

Copyright: (c) 2024 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 Department of Mechanical and Industrial Engineering, Norwegian University of Science and Technology, 7034 Trondheim, Norway; dnglee10@gmail.com
2 Department of Microsystems, University of South-Eastern Norway, 3184 Borre, Norway; kwi.y.koo@usn.no
3 Department of Fishing Vessel Safety Research, Korea Maritime Transportation Safety Authority, Sejong-si 30100, Republic of Korea; kissiny@komsa.or.kr

* Correspondence: hyung-ju.kim@ntnu.no

Abstract: In this paper, we introduce a model designed to predict human error probability (HEP) in the context of fishing boat operations utilizing the cognitive reliability and error analysis method (CREAM). We conducted an analysis of potential accidents on fishing boats and calculated the cognitive failure probability (CFP) for each identified accident. The common performance conditions (CPCs) from the original CREAM were adapted to better reflect the conditions on fishing boats, with the adapted CPCs' validity confirmed through expert consultations. To apply CREAM, data were gathered via a survey of fishermen, with the uncertainty in the collected data addressed through the application of fuzzy set theory (FST). We then established a Bayesian network (BN) model to elucidate the relationship between the fuzzy data and HEP, utilizing a weighted sum algorithm to determine conditional probabilities within the BN. Both basic and extended versions of CREAM were applied to analyze the most common accidents among fishermen, calculating the CFP for each type of accident. According to our analysis, the poorer the dynamic CPC, the higher the probability that a fall accident will occur inside the boat due to human error, necessitating a countermeasure. The paper proposes safety enhancements for small fishing boats and illustrates the increased precision of human reliability analysis (HRA) models in forecasting human error by incorporating quantitative methods. It calls for further data collection and refinement of the model for more accurate operational risk assessments.

Keywords: human reliability analysis; CREAM; fishing boats; human error probability; cognitive failure probability

## 1. Introduction

Fishing is one of the industries carried out for human livelihood, and numerous fishermen work at sea every day. However, working on fishing boats is an industry with a remarkably high accident rate. Among the marine accidents that occurred in Korea from 2018 to 2022, there were 9401 fishing boat accidents, which account for $65.4 \%$ of all marine accidents. The number of casualties reached 1908 [1]. Table 1 illustrates the accident frequency by ship type, indicating the probability of an accident occurring, and the individual risk, which denotes the probability of a fatality on that specific ship type. The data reveal that the frequency of accidents involving fishing vessels in Korea is comparable to those of other commercial vessels globally, suggesting a similar rate of accident occurrences among these categories. However, when considering individual risk (IR) and the Potential Loss of Life (PLL), Korean fishing vessels exhibit a marked difference, with the IR being three to seven times greater than that of other commercial vessels. This disparity indicates that the risk of mortality for individual fishermen on board is significantly elevated compared to other vessel types. Therefore, although the incidence


rate of fishing vessel accidents in South Korea aligns with the global average for commercial vessels, the individual risk faced by fishermen is substantially higher.

Table 1. Comparison of accidents involving fishing vessels in Korea and other commercial vessels. Source: IMO [2-6], KMST [1,7], KOSIS [8].

Furthermore, Table 2 outlines the probability of an individual perishing in an accident on a fishing vessel, segmented by country. Notably, Korea exhibits an exceptionally high accident fatality rate in comparison to other nations with robust fishing industries. Specifically, the individual risk in Korea is seven times higher than that in Norway. To address this issue, it is crucial to develop guidelines capable of forecasting and mitigating potential human errors in fishing boat operations. Consequently, this paper involves a survey of fishermen in Korea-a country where accidents on fishing boats often result in fatalities-to identify the conditions under which human error is most likely to occur.

Table 2. Comparison of individual risks of fishing vessels in Korea and other countries. Source: $\operatorname{IMO}[2-6]$.


In particular, the main cause of human casualties is human error [9]. Human errors that occur during maritime operations can directly lead to accidents, implying that there are many risks involved in the various tasks required in the fishing industry. Accidents that frequently occur on fishing boats include getting caught in equipment, slipping while moving, falling, and getting caught in fishing nets, all of which can result in significant casualties. Work at sea is highly affected by the weather, and the performance of equipment is often compromised by seawater. Therefore, it is particularly important to present guidelines that can predict and prevent potential human errors in work performed on fishing boats.

In this paper, human error is defined as "an out-of-tolerance action, or deviation from the norm, where the limits of acceptable performance are defined by the system" [10,11]. This definition is commonly utilized in the nuclear field. Such errors can stem from issues related to sequencing, timing, knowledge, interfaces, procedures, and other factors. By analyzing the causes of these human errors and identifying contributing factors to accidents, it is possible to prevent incidents in specific fields, ultimately leading to a reduction in human casualties.

One of the most commonly used methods in recent research to evaluate and mitigate human error is human reliability analysis (HRA). HRA can be used to identify potential human errors and quantify the probability of an accident based on the cause. Additionally, through quantified probability, it is possible to identify the most serious causes and prepare measures to prevent them in advance. HRA is divided into first-generation and secondgeneration methods. The first-generation methods do not consider the context of the task and have inherent problems of underestimating human information processing systems, so they are not widely used these days. Representative first-generation HRA methods include the technique for human error rate prediction (THERP) [12], the human error assessment and reduction technique (HEART) [13], and the simplified plant analysis risk human relia-

bility assessment (SPAR-H) [14]. The second-generation HRA methods are used in various industries by considering human information processing systems and situational factors, and representative methods include a technique for human event analysis (ATHEANA) [15] and the cognitive reliability and error analysis method (CREAM) [16]. Unlike ATHEANA, which specializes in the field of nuclear power plants, CREAM is widely used to evaluate human error in various industries such as petrochemicals (Mazlomi et al. [17]), power plants (Tang et al. [18], Lin et al. [19]), marine (Ung [20], Chen et al. [21]), and aviation (Lam et al. [22], Lin et al. [23]), etc.

HRA methods have been applied to various fields where human error can lead to accidents. Chen et al. [24] investigate the influence of worker states on unsafe behaviors in coal mine accidents through a Bayesian network (BN) approach. The study identifies poor states, including inadequate safety awareness and mental fatigue, as significant contributors to unsafe behaviors such as violations and decision errors. It concludes that insufficient experience and poor fitness for duty are the primary factors leading to unsafe behaviors. The study highlights the utility of BN in analyzing the complex relationships between worker states and unsafe behaviors, advocating for real-time monitoring of worker states to mitigate risks. Mohsin et al. [25] identify and rank the main risk factors affecting Pakistan's fisheries sector using the fuzzy Analytic Hierarchy Process (AHP) and Importance-Performance Analysis (IPA). Management risk is highlighted as the most critical, suggesting the need for effective management strategies to mitigate risks for sustainable fisheries development. The study emphasizes comprehensive legislative frameworks and the adoption of sustainable practices to counteract overfishing and enhance the sector's management. Focusing on a thermal power plant, Ogmen et al. [26] employ a hybrid approach that combines the HEART with fuzzy AHP and step weight assessment ratio analysis (SWARA) methods for a detailed human reliability analysis. By tailoring the analysis to specific operational contexts and enhancing the assessment of error probabilities, the study aims to improve safety measures within the power generation sector. It emphasizes the significance of human error in operational safety and proposes a novel, practical approach to mitigating such errors in coal-fired thermal power plants.

HRA has also found numerous applications within the maritime sector. Sheng et al. [27] proposed a Bayesian spatial multinomial logistic model (BSMNL) using geographic information obtained from historical maritime accidents. The proposed BSMNL model can be used to investigate the determinants of human errors associated with maritime accidents. Human error was evaluated by inputting accident data that occurred in six areas of Fujian waters into the proposed model, and it was determined that bad weather and the intervention of fishing boats were the causes of human error leading to accidents at sea. Antão et al. [28] evaluated the contribution of human error to ship accidents under various weather conditions and the impact of high wave heights on the occurrence of specific accident types. They developed a Bayesian Belief Network model that includes variables related to various wave conditions as well as marine accidents. As a result of the verification using data from 857 marine accidents, weather and wave height were perceived as extremely dangerous factors among fishing boat crews and insignificant risk factors among recreational boats. Obeng et al. [29] proposed a new human factor analysis model to analyze small fishing boat operations, and this model was combined with a BN and tested, focusing on small fishing boats operating in the Atlantic Canada region. They estimated that the main causes of accidents were the operator's actions, the natural and technological environment, unsafe management of operations, and factors associated with the vessel itself. In this way, HRA cases applied to the marine field showed a strong tendency to identify the causes of collisions or accidents that occurred during specific tasks.

Analytical research on fishing boat accidents was also actively conducted. Wang et al. [30] collected and reviewed accident data related to fishing boats and conducted an analysis to identify the most common causes of fishing boat accidents. This study found that accidents increased due to differences in language, education, training, and mindset resulting from the hiring of multinational crew members. To increase safety in fisheries where these

characteristics are present, they suggest ways to develop a safety culture at all levels of the industry's infrastructure and to include human factors in safety assessment frameworks in a feasible manner. Alwi et al. [31,32] listed risks and their consequences in all aspects and stages of fishing and identified aspects related to fisher safety management in all institutional parts existing regulations, and human resources, working environment conditions, and designing work safety models. They also identified through HRA that the largest number of accidents can occur in fishing gear operations. Irvana et al. [33] analyzed the risk of fishing boat accidents using the Formal Safety Assessment method and attempted to improve the safety of maritime transportation. As a result of the analysis, they found that the risks were high in the following order: mechanical failure, vessel foundering, and falling overboard. Prior studies have emphasized the dangers of working on fishing boats and found that accidents can be caused by a variety of factors depending on the area in which the fishing boat operates or the fishing method.

As an example of applying CREAM to the marine field, Yang et al. [34] proposed a modified CREAM that integrates fuzzy evidential reasoning and Bayesian inference logic to facilitate human reliability quantification in marine engineering. They used evidential reasoning to establish fuzzy IF-THEN rules containing belief structures and used a Bayesian inference mechanism to aggregate all rules relevant to the work of marine engineers to estimate failure probabilities. The proposed method was applied to an oil tanker COP (cargo oil pumps) shutdown scenario to verify its feasibility. Ghasemi et al. [35] performed task analysis through hierarchical task analysis to predict the probability of human error in the hydrocarbon road tanker loading operation and calculated HEP using a method integrating FST, BN, and CREAM. As a result of the HEP calculation, investigating the internal parts of the tanker and attaching the ground rode clamp were the tasks with the highest HEP, and working conditions and crew collaboration were identified as the CPCs that contributed the most to human error. Ung [36] proposes a novel risk assessment study evaluating the human error contribution to oil tanker grounding, incorporating expert judgment and a combination of Fault Tree Analysis (FTA), fuzzy CREAM, and Bayesian reasoning. By establishing a logical safety structure for oil tanker grounding and integrating expert judgments with a novel application of FTA, fuzzy CREAM, and Bayesian reasoning, the study offers a comprehensive assessment of human error probabilities. It identifies fatigue and Collision Regulation (COLREG) violations as key factors in ship groundings. The study's approach, emphasizing the logical connection between CPC observations and contextual control mode (COCOM), provides a systematic methodology for evaluating and understanding the human error aspects of maritime safety. Zhou et al. [37] presented an HRA method based on fuzzy logic theory, BN, and CREAM. They modified the CPCs used in the original CREAM to suit the situation of shipboard oil tanker work. They used the results of a CPC survey of eighteen sailors of various positions, and they obtained results showing that HEP varies depending on position and showed that most of the crew members were in tactical control mode and were reliable.

In prior research, because the CPC of the original CREAM was used as is, there was a limitation in that it was not optimized for the application field. This study seeks to overcome such limitations by tailoring the CPCs to the demanding conditions of the marine environment. Superfluous CPCs for the fishing industry were eliminated, dynamic conditions were incorporated, and the CPC levels were refined based on fishermen's input, ensuring a better fit for the study's context. Furthermore, previous investigations lacked the inclusion of conditional probability tables (CPT) that would reflect expert insights, frequently defaulting to merely classifying control modes in CREAM without attributing specific values to the probability of human error. This approach highlighted the inherent qualitative limitations of CREAM and the difficulties in managing the uncertainties intrinsic to human error analysis within diverse sectors, such as marine operations and the petrochemical industry.

To address these challenges, our study employs a hybrid technique that combines FST, BN, and CREAM. By integrating FST, the model gains the ability to manage the

uncertainties surrounding CPCs with greater nuance, assigning multiple states to CPCs based on varying degrees of membership. This adaptability substantially improves the model's capability to navigate the complexities of real-world scenarios, where the precise condition of a CPC is often ambiguous. Additionally, the use of BN enhances the model by mapping out the dependencies among CPCs, control modes, and HEPs, providing a visual and intuitive depiction of intricate systems. This integration not only surpasses the static nature of traditional HRA methods but also enables comprehensive reasoning encompassing both forward and backward perspectives. Such capabilities are instrumental in identifying and prioritizing measures for accident prevention, marking a significant advancement in the quantification and mitigation of human error across various industries.

In this paper, we introduce a model that employs FST and BN, grounded in CREAM, to predict HEPs based on crew experience and types of accidents on small fishing boats. The study focuses on two principal areas: estimating HEP relative to crew experience and calculating the cognitive failure probability (CFP) for the five most common accidents on fishing boats. Surveys were conducted with fishermen possessing over 20 years of experience to ascertain levels for each CPC, applying FST with triangular and trapezoidal membership functions to mitigate uncertainty. The data refined by FST served as inputs for a BN, constructed around CPCs, to compute HEP. This network delineated the relationships between CPCs and HEPs, utilizing the Center of Area (COA) method to derive crisp values (CV) and HEPs from the Bayesian analysis outcomes. The investigation of fishing boat accidents, combined with dynamic CPC assessments, facilitated CFP calculations across diverse conditions-categorized as worst, normal, and best. Both basic and extended CREAM methodologies were used to calculate incident-related CFP, and the results were compared.

In summary, this research significantly advances the quantification and analysis of human error probability (HEP) by addressing the limitations of current HRA methods and introducing a hybrid model that integrates FST and BN. It enhances the scientific grasp of human errors in high-risk tasks and lays the groundwork for devising effective safety enhancement and accident prevention strategies. The methodologies and insights generated promise wider applicability across diverse sectors, paving the way for more secure operational settings. This paper aims to ascertain human error probabilities by examining experience and accident types, thereby facilitating the consideration of preventive measures.

# 2. Methodology 

### 2.1. CREAM (Cognitive Reliability and Error Analysis Method)

CREAM is a method introduced by Hollnagel [16]. It is a second-generation HRA method and is currently used in various industrial fields. The key elements that make up the CREAM are CPCs and control mode. Because the core of CREAM is that human error is not viewed as probabilistic but rather determined by the context of the task, it identifies nine CPCs for a task. CPC is a factor related to operator, technology, and status, as follows: adequacy of organization, crew collaboration quality, working condition, number of simultaneous goals, available time, time of day, training and experience, man-machine interface (MMI) and operational supports, availability of procedures and plans. Each CPC is divided into levels that affect human behavior and reliability. Time of day and number of simultaneous goals have only negative and neutral effects, and the other 7 CPCs have all negative, neutral, and positive effects.

Konstandinidou et al. [38] suggested modifications or changes to optimize CPC for each industry. Therefore, in this paper, CPCs that are not necessary for fishing were removed and additional necessary CPCs were added. The modified CPC and each CPC level are shown in Table 3, and their validity was verified by industry experts.

Table 3. CPCs and Their levels.


The CPC that has changed from the original CPC is environmental conditions, technical conditions, and fatigue. The criterion for organization adequacy was omitted because small fishing boats are not managed or supported by specific organizational management. Furthermore, the adequacy of MMI and operational support was replaced with technical conditions because the condition of the equipment itself has a more important impact than the interface for using the equipment. Working conditions were divided into environmental conditions and fatigue, considering the difficulty of working in a marine environment. This refinement reflects the unique circumstances of fishermen, who often operate at sea with minimal crew and contend with harsh marine conditions, unlike on land. According to a study by Sheng et al. [27], when the contributing factors to human error were investigated using the BSMNL model, season, visibility, and time of day could affect the probability of human error occurring. Therefore, we decided that adding environmental conditions as a new CPC would be effective in calculating human error in the fishing industry.

Control mode is a characteristic determined by CPC and indicates how well an operator can solve problems in a specific situation and plan future operations. Control mode includes four modes: strategic, tactical, opportunistic, and scrambled. The meaning of each mode is shown in Table 4.

Table 4. CPC control modes and their probability intervals. Source: Hollnagel [16].


The control mode determined according to the nine CPC levels appears as shown in Figure 1, where the $x$-axis represents the number of CPCs with negative effect, and the $y$-axis represents the number of CPCs with positive effect. Each intersection represents a control mode.
![img-0.jpeg](img-0.jpeg)

Figure 1. Control modes of the CREAM corresponding to various CPC states. Source: Authors, adapted form Hollnagel [16].

Similar to the probability interval of action failure in Table 4, the original CREAM method inaccurately estimates the probability of human error, and only the approximate probability for each mode can be known. In this paper, we defined the relationship between CPC and HEP in fishing boat operations and used three methods to accurately calculate HEP. Basic CREAM and extended CREAM were used to calculate and compare CFP according to accidents that may occur on fishing boats, and a model combining FST, BN, and CREAM was used to calculate HEP according to the fisherman's experience. Figure 2 is a graphical representation of the relationship between each method applied in this paper and the process of obtaining the results to be calculated.

![img-1.jpeg](img-1.jpeg)

Figure 2. Flow chart showing the relationship between the methods applied in this paper.

# 2.1.1. Basic CREAM 

To calculate CFP in basic CREAM, the context influence index (CII) must be calculated [39]. When CII is defined as $\beta$, it is calculated by Equation (1).

$$
\beta=X-Y=\sum_{\text {reduced }} C P C-\sum_{\text {improved }} C P C
$$

It is easier to find the control mode according to the influence of CPC by using $\beta$ than by identifying the control mode in Figure 1. Table 5 shows the control mode according to the $\beta$.

Table 5. Relations between the context influence index and the control mode.


If the value of $\beta$ is 0 , it means that the number of CPCs with negative effects and the number of CPCs with positive effects are the same. A higher $\beta$ implies a predominance of CPCs with negative effects, while a lower $\beta$ means there are more CPCs with positive effects. In addition, changes in the reliability of human interactions can be explained by a logarithmic function with changes in external conditions [40]. Therefore, the relationship between CFP and $\beta$ can be expressed by Equation (2).

$$
\log \left(C F P / C F P_{0}\right)=k \beta
$$

In Equation (2), $k$ is a constant and can be calculated through Equations (3)-(5). By rearranging Equation (3) for CFP, Equation (6) can be obtained.

$$
\begin{gathered}
\log \left(C F P_{\max } / C F P_{0}\right)=k \beta_{\max } \\
\log \left(C F P_{\min } / C F P_{0}\right)=k \beta_{\min } \\
k=\log \left(C F P_{\max } / C F P_{\min }\right) /\left(\beta_{\max }-\beta_{\min }\right) \\
C F P_{0}=C F P_{\max } / 10^{k \beta_{\max }}
\end{gathered}
$$

There are 9 CPCs with negative effects and 7 CPCs with positive effects, so $\beta_{\max }=9$, $\beta_{\min }=-7$. To calculate $k$, the values of $C F P_{\max }$ and $C F P_{\min }$ are required. It is reasonable in HRA to assume that $C F P_{\max }=1.0$, and $C F P_{\min }=0.0001$. Therefore, $k=0.25$ is calculated, and by substituting this into Equation (6), $C F P_{0}=0.000562$ can be obtained. The final CFP

is as in Equation (7). This is a calculation method based on the assumption that performance reliability is affected by the number of CPCs with negative or positive effects.

$$
C F P=C F P_{0} \times 10^{k \beta}=0.00562 \times 10^{0.25 \beta}
$$

# 2.1.2. Extended CREAM 

The primary goal of the basic CREAM method is to identify a reliable indicator for the probability of an interaction rather than pinpoint an exact failure probability. However, the breadth of the ranges in Table 4 limits their utility for preliminary assessments, as they lack the precise differentiation needed at this initial stage. Furthermore, the CFP in Basic CREAM is influenced solely by the count of positive or negative CPCs, which masks the specific impact of each CPC. To enable a more precise assessment of human error, it is suggested to assign weights to the various levels of CPCs and compute the CFP by summing these weighted factors.

The extended version of CREAM is designed for a more comprehensive analysis of human interactions that follow the initial assessment. The insights gained from the basic application of CREAM serve as a crucial foundation for this extended analysis. Human actions that are identified as sensitive and potentially significant through the HRA screening process can then be examined more closely with the extended method to achieve more accurate outcomes for those actions. In extended CREAM, the performance influence index (PII) is weighted according to the level of CPC [39]. When PII is $\rho, \beta$ is calculated using Equation (8). The value of $\rho_{i}$ are provided in Table 6.

$$
\beta=\sum_{i=1}^{9} \rho_{i}
$$

Table 6. Performance influence index for CPCs.


In Table 6, the values of PII were determined based on expert opinions. Specifically, for PII values related to fatigue, technical condition, and environmental condition, which are CPCs that were not in the original CREAM, they were set based on surveyed data. The survey was conducted on fishermen with more than 20 years of experience, and they were asked to give a score between 0 and 10 regarding the positive and negative impact of each CPC. For the results obtained through the survey, the average value, excluding the maximum and minimum values, was adjusted to match the scale of PII. Table 7 shows the survey results and the calculated PII.

Table 7. PII for added CPCs.


In Extended CREAM, CFP remains consistent with Equation (7) but is calculated by substituting the nominal value in Table 8 into $C F P_{0}$. Therefore, CFP can be calculated by determining which generic failure type each accident belongs to and calculating $\beta$ using PII. Utilizing Extended CREAM allows for the consideration of each CPC's effect when evaluating human error in a task or accident, enabling a more quantitative assessment compared to Basic CREAM, which solely accounts for the count of CPCs.

Table 8. Nominal values for 13 generic cognitive failure types.


# 2.2. Fuzzy Set Theory 

Introduced by Zadeh [41], fuzzy logic offers a logical framework that describes ambiguous and unclear states with multiple values, departing from the binary approach of true or false. This is particularly relevant in industries where determining the precise status of CPC for each task is challenging for workers. CPC data, often qualitative and gathered through surveys, encompasses uncertainties and typically falls between the categories of appropriate, neutral, or inappropriate, rather than fitting neatly into one. Choosing a single category might lead to biases or errors in the HRA process. Given the lack of statistical data on vital parameters and the subjective complexity of seafarers' operations, fuzzy logic becomes essential for overcoming the limitations of imprecise data collection. The application of fuzzy logic involves three steps: fuzzification, which transforms inputs into

a fuzzy set; fuzzy sets and fuzzy inference, which use membership functions to produce fuzzy output; and defuzzification, which translates the fuzzy output back into a CV.

# 2.2.1. Fuzzification 

Fuzzification entails generating multiple fuzzy perceptions by decomposing input values into one or more fuzzy sets. Fuzzy numbers have a membership degree between 0 and 1 , and the most commonly used fuzzy numbers are triangular and trapezoidal fuzzy numbers. We applied that fuzzy number, and when performing the fuzzification process, we set all nine CPCs to have three levels: appropriate, neutral, and inappropriate. Given that the value of each CPC is between 0 and 100, the universes of discourse of the fuzzy sets for CPC can be defined as [0,50], [10, 90], and [50, 100]. CPCs with values falling within this range are converted to values between 0 and 1 through the membership function. A converted CPC value of 1 indicates complete membership in the fuzzy set, while a value of 0 implies exclusion from the fuzzy set. The universes of discourse for the fuzzy sets concerning control mode are detailed in Table 9. This value can be obtained by taking the base 10 logarithm of the probability interval of action failure value provided in Table 4.

Table 9. The universes of discourse of the fuzzy sets for the control modes.


### 2.2.2. Fuzzy Sets and Fuzzy Inference

After the input is decomposed into fuzzy sets, a set of fuzzy if-then-else rules is used for fuzzy output. Each membership function determines the condition of the input value, sets a function for that condition, and returns a fuzzy output value for the input value.

$$
\begin{aligned}
& f_{1}(x)=\left\{\begin{array}{cc}
1 & x \leq 10 \\
(50-x) / 40 & 10 \leq x \leq 50 \\
0 & x \geq 50
\end{array}\right. \\
& f_{2}(x)=\left\{\begin{array}{cc}
0 & x \leq 10, x \geq 90 \\
(x-10) / 40 & 10 \leq x \leq 50 \\
(90-x) / 40 & 50 \leq x \leq 90
\end{array}\right. \\
& f_{3}(x)=\left\{\begin{array}{cc}
0 & 50 \leq x \\
(x-50) / 40 & 50 \leq x \leq 90 \\
1 & x \geq 90
\end{array}\right.
\end{aligned}
$$

Membership function $f_{1}(x), f_{2}(x), f_{3}(x)$ represent three CPC levels, respectively. $f_{1}(x)$ is inappropriate, $f_{2}(x)$ is neutral, and $f_{3}(x)$ is appropriate. Figure 3 shows the degree of membership in the CPC. Based on 50, the left and right solid lines represent functions $f_{1}(x)$ and $f_{3}(x)$, respectively, and the dotted line represents function $f_{2}(x)$. By substituting the results of a survey of CPC into $f_{1}(x), f_{2}(x)$, and $f_{3}(x)$, a fuzzified value of the effect of CPC on human reliability can be obtained, and this value will be used as an input value for BN.

Based on the probability interval of action failure in Table 4, it becomes evident that each control mode also has an overlapping section in failure probability. Consequently, a membership function that applies the range of the probability interval of action failure can be obtained, and the graph for this is shown in Figure 4. Each range of the membership function corresponds to a value calculated in Table 9, and when the middle value of the range is substituted, the result of the function is 1 . Equations (12)-(15) are the membership function for each control mode.

$$
\begin{gathered}
f_{S t r}(x)=\left\{\begin{array}{cc}
(x+5.3) / 1.65 & -5.3 \leq x \leq-3.65 \\
(-x-2) / 1.65 & -3.65 \leq x \leq-2 \\
0 & x \leq-5.3, x \geq-2
\end{array}\right. \\
f_{T a c}(x)=\left\{\begin{array}{cc}
x+3 & -3 \leq x \leq-2 \\
-x-1 & -2 \leq x \leq-1 \\
0 & x \leq-3, x \geq-1
\end{array}\right. \\
f_{O p p}(x)=\left\{\begin{array}{cc}
(x+2) / 0.85 & -2 \leq x \leq-1.15 \\
(-x-0.3) / 0.85 & -1.15 \leq x \leq-0.3 \\
0 & x \leq-2, x \geq-0.3
\end{array}\right. \\
f_{S c r}(x)=\left\{\begin{array}{cc}
2 x+2 & -1 \leq x \leq 0.5 \\
-2 x & -0.5 \leq x \leq 0 \\
0 & x \leq-1, x \geq 0
\end{array}\right.
\end{gathered}
$$

![img-2.jpeg](img-2.jpeg)

Figure 3. Membership functions for each CPC.
![img-3.jpeg](img-3.jpeg)

Figure 4. Membership functions for each control mode.

# 2.2.3. Defuzzification 

Defuzzification is the process of converting fuzzy conclusions into CVs. Since the CV is a value calculated using the probability of the control mode, which is a change due to external conditions, CV and HEP have a logarithmic relationship. There are many defuzzification methods, but in this study, center of the area (COA) [42], which has relatively high accuracy, was used. According to the COA method, the center of the area of the membership function is determined using Equation (16).

$$
C V=\frac{\int x f(x) d x}{\int f(x) d x}
$$

In Equation (16), CV is the crisp value, and $f(x)$ represents the sum of the membership functions of the control modes as in Equation (17). Each membership function is as shown in Equations (12)-(15). Since CV and HEP are logarithmic functions, HEP can be obtained through Equation (18).

$$
\begin{gathered}
f(x)=f_{S t r}(x)+f_{T a c}(x)+f_{O p p}(x)+f_{S c r}(x) \\
H E P=10^{C V}
\end{gathered}
$$

### 2.3. Bayesian Network

A Bayesian network, a probabilistic graphical model, utilizes a directed acyclic graph (DAG) to illustrate the conditional dependencies among a set of variables, where unconnected nodes represent conditionally independent variables and connected nodes incorporate parent node variables as inputs. BN excels at managing probabilistic information within events characterized by complex causal relationships to forecast event outcomes under specific conditions. While the original CREAM method offers only a range for action failure and control modes for assessing HEP, it faces challenges in quantitatively measuring HEP due to its inability to account for the uncertainty surrounding CPC and control modes.

To address these limitations and enhance the precision of HEP assessment, BN has been integrated into CREAM to mitigate its uncertainties, establishing connections between CPC and HEP. This integration allows for the determination of the probability distribution of control modes by treating each CPC as a parent node and computing conditional probabilities at the child node for each input from the parent node. This approach not only facilitates a quantitative understanding of each control mode's probability but also enables accurate HEP calculations through the application of the COA method and defuzzification analysis of the control mode values obtained. Consequently, this augmented methodology, combining the strengths of fuzzy logic theory and BN techniques within CREAM's analytical framework, provides a robust solution for quantifying HEP in the fishing industry, thereby improving the evaluation of seafarers' human reliability by capturing the nuanced relationships between numerous variables.

When modeling BN, conditional probability tables (CPT) must be defined to quantify the relationships of each node [43]. However, if all 9 CPCs are connected to the control mode node, the number of conditional probabilities that need to be defined becomes very large. Since each CPC has three levels: appropriate, neutral, and inappropriate, there are $3^{9}=19,683$ conditions. It is very difficult to define conditional probabilities for all these conditions, so three nodes were added to the BN. Nine CPCs, including the CPC added in this study, were divided into three categories according to type. The added nodes are the human reliability condition, which varies depending on the human condition, the job condition, which is related to work conditions, and the dynamic condition, which changes conditions every time the ship sets sail. By adding nodes, the number of items that experts need to evaluate and the amount of computation inside the network are reduced.

To calculate the conditional probability of newly added nodes, the weighted sum algorithm developed by Das was used [44]. This method calculates the conditional probability by assigning a weight to each parent node and evaluating the probability of the child node

according to the status of the three parent nodes. In this paper, to obtain the value of CPT, the opinions of four experts, including professors and inspectors with more than 10 years of experience, were collected by asking the following questions:
(1) What is the weight of each CPC for a given condition?
(2) What is the probability distribution over the states of the child node given the parental configuration?
When an expert fills out the table for the above question, the conditional probability is calculated using Equation (19).

$$
\begin{aligned}
& P\left(y_{m} \mid x_{k 1}^{1}, \ldots, x_{k i}^{i}, \ldots, x_{k n}^{n}\right) \\
& \left.=\left[w_{1} \cdot\left\{\operatorname{Comp}\left(x_{k 1}^{1}\right)\right\}\right]+\ldots+\left[w_{1} \cdot\left\{\operatorname{Comp}\left(x_{k i}^{i}\right)\right\}\right]+\ldots \\
& +\left[w_{1} \cdot\left\{\operatorname{Comp}\left(x_{k n}^{n}\right)\right\}\right]
\end{aligned}
$$

$y_{m}$ is the state of the child node, $w_{n}$ is the weight of each parent node, and $x_{k n}^{n}$ is the state of the parent node. This process was equally applied to the relationship between each condition node and the control mode node. The BN modeled based on this is shown in Figure 5.
![img-4.jpeg](img-4.jpeg)

Figure 5. BN structure to obtain the probability distribution of the control mode.
The node in the first layer is a CPC node and utilizes the fuzzified value of the survey results as an input value. The node in the second layer is a condition node set to reduce calculations. The node of the third layer is the control mode, which is the output node. Through this structure, the probability distribution of the control mode can be calculated according to the level of each CPC.

# 2.4. Data Collection 

To obtain data for applying the method introduced above, a survey was conducted with seven fishermen with more than 20 years of experience. The main area of activity for fishermen is the southern coast of Korea, and they operate small fishing boats of less than 10 tons. The details of the investigation are as follows;

- Top 5 accidents that occur most frequently on fishing boats
- CPC impact level for each accident
- Effectiveness score of CPC for operations on fishing boats

Despite the limited number of survey respondents in this study, fishermen with over 20 years of experience are deemed adequate for evaluating the proposed model. Their extensive knowledge and firsthand insights into fishing risks and operational challenges render them expert informants. Their prolonged exposure to the fishing environment equips them to offer responses that are likely to yield a reliable and detailed understanding of accidents, CPC impact levels, and the efficacy of operational practices. Nonetheless, the small sample size presents a limitation that necessitates future enhancement, a point that will be further addressed in Section 5.

## 3. Results

In this section, we applied the survey responses to each method introduced in Section 2 and analyzed the outcomes when the proposed model was implemented in actual cases. Initially, basic CREAM and extended CREAM were applied to the survey results to calculate CFP for each accident. Subsequently, FST was applied using CPC scores for work on fishing boats, and HEP for each crew member was calculated through BN modeling.

### 3.1. CFP of Basic CREAM

Fishermen identified the following five accidents as the most common occurrences on fishing boats: collision while sailing, getting caught in equipment, slipping on the deck, falling inside the boat, and getting caught in fishing nets. Table 10 shows the results of a survey investigating the effect of each CPC on accidents. After combining the opinions of all seven people, the level with the highest frequency was used. The complete results of the survey are provided in the Supplementary File.

Dynamic conditions were omitted from the results as they vary with each sailing. Instead, we utilized the human reliability condition and job condition from the survey results. Dynamic conditions were categorized into all inappropriate states/all neutral states/all appropriate states, and HEP was calculated to find out how much influence changing conditions have on work on a fishing boat.

From the results presented in Table 10, $\beta$ values can be obtained for CPC numbers 1 to 6 by applying basic CREAM to 'collision': $\beta=0-1+0+0+1+1=1$. Additionally, $\beta$ values were determined for all dynamic conditions to be inappropriate, neutral, and appropriate, resulting in $\beta_{i}=4, \beta_{n}=1, \beta_{a}=-1$. By substituting this value into Equation (7), CFP according to dynamic conditions can be calculated. Table 11 shows the results of repeating this process for all accident types.

Due to the CFP of basic CREAM being solely influenced by the number of CPCs, the CFP was calculated the same for accidents with the same $\beta$ regardless of the type of CPC. As a result of the calculation, the probability of human error occurring was highest in falling, and the probability was lowest in collision. The reason is that in the case of falling, the effect of adequacy of training and experience and crew collaboration quality was negative compared to other accidents. In the case of a collision, the impact of fatigue was more positive than in other accidents. The reason the above result occurred is because falling caused by the shaking of the ship during sailing is difficult to solve with training, experience, or the help of other sailors. In addition, fishermen perceived that physical fatigue had a low impact on the probability of collisions occurring. For the remaining

accidents, the HEP was calculated to be the same, which can be seen as the fishermen's perception that the probability of the accident occurring is similar.

Table 10. Results of a survey on the effect of CPC on each accident.


Table 11. CFP results using basic CREAM.


Analyzing the results based on dynamic conditions, based on the best conditions, the CFP was 3.1 times higher when the conditions were neutral and 17.8 times higher when the conditions were the worst. These findings highlight that bad weather, poor equipment conditions, and untimely sailing times significantly increase the probability of human error. In particular, because time of day has only two levels, neutral and negative, the difference between neutral and worst appears larger than the difference between best and neutral.

# 3.2. CFP of Extended CREAM 

From the results presented in Table 10, $\beta$ values can be obtained for CPC numbers 1 to 6 by applying extended CREAM to 'collision': $\beta=0-1.4+0+0+1.2+2.4=2.2$. Similar to the calculation method of basic CREAM, calculating all $\beta$ according to dynamic conditions is as follows: $\beta_{i}=5.2, \beta_{n}=2.2, \beta_{a}=0.3$. To define $C F P_{0}$, each accident was

classified into an appropriate generic failure type. Collisions while sailing most often occur due to poor forward observation, and getting caught in equipment occurs due to contact with the body at an inappropriate time during equipment operation. Slipping on the deck occurs when a human does not recognize a deck with stagnant water, and falling inside the boat is likely to occur due to incorrect actions while sailing. Accidents involving fishing nets occur due to incorrect actions while working with fishing nets. Table 12 shows the classified failure types, the corresponding $C F P_{0}$, and the calculated CFP.

Table 12. CFP results using extended CREAM.


In Extended CREAM, the calculated CFP for all accidents differed from basic CREAM due to the influence of $C F P_{0}$. Upon examining the overall probability, the CFP was highest in the order of falling accidents, followed by slipping, getting caught, collisions, and getting caught in fishing nets. This means that even for accidents with the same $\beta$, the CFP varies depending on which failure type it belongs to.

The results concerning dynamic conditions were similar to basic CREAM, based on the best conditions, the CFP was three times higher when the conditions were neutral and 16.7 times higher when the conditions were the worst. In the worst case of dynamic conditions, the CFP of falling is calculated as a number exceeding 1. In extended CREAM, if the CFP exceeds 1, the probability of occurrence of the incident is calculated as 1 [39]. This means that as the dynamic condition worsens, the probability of falling increases significantly.

Table 13 shows the comparison results of CFP between basic and extended CREAM. Except for getting caught in fishing nets, the extended method calculated a higher CFP than the basic method, and this is a result of the fact that unlike the basic, which simply considers only the level of CPC, the extended method considers the quantitative impact of each CPC. Additionally, in extended CREAM, the probability of getting caught in a fishing net was relatively low due to the influence of $C F P_{0}$ depending on the failure type. Therefore, for accurate quantitative analysis, the precise setting of the accident's failure type is crucial.

Table 13. Comparison of CFP results using basic CREAM and extended CREAM.


# 3.3. HEP of Bayesian Network 

To calculate CPT, the average value of the results received from one university professor and three Korea Maritime Transportation Safety Authority (KOMSA) inspectors was utilized. Table 14 shows experts' opinions on the impact on human reliability conditions according to the level of the fatigue node. This process was carried out for all CPCs, and the impact on human reliability conditions, job conditions, and dynamic conditions was

investigated according to the level of each CPC. The weight value of each CPC surveyed by experts is presented in Table 15.

Table 14. Probabilities gained from experts for calculating the CPT of the human reliability condition node.

|  CPC Name
(Parents Node) | Level | Condition |   |

Table 15. Weight value for each CPC.


All conditional probabilities can be calculated by substituting the probabilities according to the level in Table 14 and the weight values in Table 15 into Equation (19). Equation (20) is the probability of having a supportive influence on the fatigue condition when the level of fatigue is appropriate, the level of adequacy of training and experience is acceptable, and the level of crew collaboration quality is inappropriate.

$$ P=0.35 \times 0.85+0.225 * 0.6+0.425 * 0.0275=0.444 $$

By repeating this process for all nodes, the required conditional probability can be calculated at the condition node of the BN. Table 16 shows the CPT of the human reliability condition node.

Table 16. Conditional probability table of the human reliability condition node computed using the weighted sum algorithm.


The fuzzified survey results were employed as input for BN. Table 17 presents the results of the survey regarding the fisherman's career and their work on the fishing boat, rated on a scale from 0 to 100. Each CPC number is the same as in Table 15. The closer the score is to 100, the more effective the CPC is. Table 18 shows the fuzzified input values.

Table 17. Survey results of seven fishermen.


Table 18. Input values for a Bayesian network.


The results of inputting the data of fisherman No. 1 into the BN network in Figure 5 are shown in Figure 6. The process of calculating the control mode for each fisherman remains consistent. CV can be obtained by applying the COA method of Equation (16) to the probability of the control mode, which is the output value of BN , and going through the defuzzification process. Finally, HEP can be calculated by substituting CV into Equation (18). This process was iterated for all fishermen, and Table 19 presents the probability, CV, and HEP of the control mode.

![img-5.jpeg](img-5.jpeg)

Figure 6. Bayesian network reasoning results for fisherman 1.
Table 19. Results of the probability distribution for the control modes and HEP.


Comparing with Table 15, the HEP of fisherman 7, who rated all CPCs with scores of 50 or higher and perceived them to positively impact human reliability, was estimated to be the lowest. Conversely, the HEP of fisherman 6, who gave scores of 50 or less on all but two CPCs and evaluated that CPC had a generally negative effect on human reliability, was estimated to be the highest. The most dominant control mode among the fishermen surveyed is the strategic mode. This indicates that all fishermen are well aware of the situation and how work is progressing and are able to plan actions when problems arise. In addition, since the dominant control mode and the calculated HEP are the same as the failure probability range according to the control mode in Table 4, they match the probability interval of the original CREAM and can provide a more accurate HEP. In these results, it was difficult to find a correlation between experience and HEP, which is presumed

to be because the survey subjects were all veterans with more than 20 years of experience. This is the same reason why all control modes are strategic.

# 4. Discussion 

In this paper, we introduce a model aimed at enhancing the accuracy of HEP inference by integrating existing HRA methods. This effort was designed to deepen our understanding of risks in the fishing industry by incorporating dynamic conditions into the original CREAM framework's CPC and utilizing FST and BN. The effectiveness of the model was validated through its application in a real-world survey. Consequently, this study presented five novel contributions to the understanding of human errors in fishing vessels, which have the potential to mitigate human errors in a variety of industries.

### 4.1. Approaches for Comprehensive Understanding of Human Error

The basic CREAM method calculates CFP based solely on the number of CPCs, making the calculation insensitive to the specific impacts of each CPC. This lack of differentiation could obscure the distinct risks associated with different accidents. Conversely, extended CREAM reflects the severity of conditions through PII, with inappropriate CPC levels correlating with higher CFP. If the type of failure related to work or accidents is accurately classified, it becomes possible to calculate the CFP with higher accuracy than with basic CREAM. However, the method's reliance on a predefined set of failure types, limited to 13 categories, may not encompass all accident or work types.

Our combined FST and BN approach for calculating HEP took into account all fishermen's ratings of dynamic conditions, revealing a predominance of strategic control modes among seasoned fishermen. This suggests that experienced fishermen possess adequate skills to manage tasks and respond to accidents effectively. This model provided a clearer understanding of the CPC-HEP relationship, offered quantitative HEP calculations, and reduced uncertainties in survey results compared to using basic or extended CREAM alone.

### 4.2. Identification of the Most Critical CPC for Fishing Vessels

CREAM was originally developed for the nuclear power industry. In the nuclear industry, human errors are mostly analyzed, assuming a controlled and static state. However, in industries and activities that take place in dynamic and uncontrolled environments, such as aviation, construction, and maritime, it is necessary to analyze human error by considering dynamic conditions. Therefore, we identified factors that affect humans engaging in fishing activities.

The study conducted by Abaei et al. [45] demonstrates that the reliability of human performance decreases over time in harsh conditions, highlighting the need to consider environmental data and ship motions to assess human performance accurately. The study concludes that this model can significantly aid in planning and decision-making processes to improve the safety of human life during marine operations in various weather conditions. According to Antão et al. [28], adverse weather conditions can increase the probability of human error on fishing boats. His research utilized Bayesian Belief Networks to examine the impact of wave height on maritime accidents, concluding that weather conditions significantly influence the probability of specific types of accidents occurring. Rezaee et al. [46,47] underscored the importance of incorporating specific weather conditions into safety regulations and practices to mitigate risks associated with severe weather. Previous research on human reliability in the fishing industry has concluded that weather conditions increase the probability of human error. This finding supports the effectiveness of our approach in calculating human error probability by incorporating dynamic conditions into the CPC.

### 4.3. New CPCs for Labor-Intensive Human Activities

We modified the CPC of the original CREAM to be more suitable for the fishing sector, following the suggestions of Konstandinidou et al. [38]. Given the absence of

large organizations within fishing operations, 'Adequacy of Organization' was removed. Additionally, recognizing the greater importance of the condition of equipment over its interface, 'Adequacy of MMI and Operational Support' was replaced with 'Technical Condition'. 'Working Condition' was subdivided into 'Environmental Condition' and 'Fatigue', reflecting the harshness of the marine environment. The nine revised CPCs were thus categorized into human reliability conditions, job conditions, and dynamic conditions. While human reliability and job conditions can be enhanced through human efforts, factors such as adverse weather, sudden equipment failure due to seawater exposure, and fishing times dictated by target fish species are less controllable. We observed that these dynamic conditions, which vary with each fishing expedition, significantly impact the CFP for prevalent accidents on fishing boats. The revised CPC proposed in this study is expected to be applicable not only to fishing activities but also to small-scale labor-intensive activities or industries.

# 4.4. Dynamic Aspects of Human Errors 

We categorized the newly added CPCs, technical conditions and environmental Conditions, and the existing CPC, time of day, by grouping them into dynamic conditions. This CPC is an item to consider the impact of human error due to sudden equipment failure, wave height or wind factors, and fishing time, depending on the target fish species. These three items have something in common: they are factors that humans cannot control. To check the impact of the newly classified dynamic conditions, CFP was calculated by dividing the conditions into worst, neutral, and best conditions.

The findings underscored a marked disparity in CFP under varying dynamic conditions. For all accident types, the average CFP was calculated to be 0.4716 when conditions were the worst and 0.0281 when conditions were the best. This means that when dynamic conditions are the worst, the risk of human error is approximately 16.7 times higher. Especially according to the results of Extended CREAM, when the dynamic condition is at its worst, the CFP value for the accident of "falling inside the boat" is calculated to be 1.5927. This indicates that such accidents are almost certain to occur. Therefore, it is recommended to avoid fishing under these conditions. Wu et al. [48] determined that the probability of accidents related to fishing activities escalates during specific periods, in certain areas, and under particular weather conditions, based on an analysis of accident data. This finding aligns with the conclusion of this paper, which posits that the worse the dynamic CPC, the higher the probability of human error occurring. Even if other conditions are optimal, a poor dynamic CPC significantly increases the probability of human error, necessitating the implementation of countermeasures. And the dynamic aspect we have added is a factor worth considering when analyzing human error in various industries/activities that are dynamic and uncontrolled.

### 4.5. Extended Application of the Proposed Method

Although the study was based on Korean fishermen, the identified accident categories and CPCs are broadly applicable to global fishing activities. The method proposed in this study did not include elements limited to specific regions, except for the survey. The proposed model is versatile and could be adapted for fishermen in other regions with minor modifications to survey questions, dynamic CPC, or accident classifications.

The modified CPCs can also be used in other industries. If the accident category is changed to suit each industrial field, HEP can be calculated using the method proposed in this study, targeting marine facility repairs, construction, agriculture, and port workers, which are jobs affected by the external environment. Since these occupations have a high probability of making mistakes due to weather, equipment condition, and worker fatigue, it is reasonable to apply modified CPC.

Nevertheless, the model's complexity limits its immediate usability by fishermen and officials. Lazakis et al. [49] and Antão et al. [50] find that human factors significantly contribute to fishing vessel incidents, with issues such as inadequate training and poor

communication being prevalent. These papers emphasize the importance of addressing these human factors through improved safety training and protocols to reduce the risk of accidents. Our goal, therefore, is not direct application by these stakeholders but rather to utilize the insights gained from the model's analysis to develop and disseminate a safety checklist tailored for fishermen. This checklist, designed to be used before, during, and after sailing, will include critical items that need monitoring to enhance safety at sea. By focusing on these key areas, the checklist is expected to play a crucial role in accident prevention, helping fishermen remain vigilant about potential hazards.

Furthermore, the application of our model facilitates the identification of conditions under which human errors are most likely to occur and the types of accidents that are most common. Such insights are invaluable for pinpointing specific areas where crew training and safety measures onboard fishing vessels require reinforcement. By addressing these focal points, we anticipate a significant reduction in accidents attributable to human error, fostering a culture of increased caution, especially under adverse dynamic conditions. This approach aligns with our overarching goal of improving safety in the fishing industry through strategic analysis and intervention.

# 5. Limitations and Future Works 

There are two disadvantages to the model constructed in this study. Firstly, the accuracy of the survey results presents a challenge. Given that fishermen may not possess the same level of education as more highly trained sailors or engineers, conveying the survey's intricacies and ensuring comprehension can be problematic. This difficulty is compounded by instances where fishermen might select identical levels for all accidentrelated CPCs, thereby complicating the differentiation of responses. Although the CPT relies on subjective expert opinions, which inherently carry a risk of bias, the expertise of our survey respondents-comprising professors and engineers with over a decade of experience-lends a degree of reliability to the data collected.

Secondly, our survey exclusively involved fishermen with more than 20 years of experience, limiting our ability to draw comparisons between the HEP of these veterans and that of less experienced fishermen. This homogeneity among respondents restricts the generalizability of our findings across the broader fishing community.

In future research, addressing the challenges encountered in survey-based assessments of accident risks and human error probabilities among fishermen will be crucial. To enhance the reliability and validity of such studies, we propose two methodological improvements: increasing the sample size and precisely defining the target subgroup within the fishing community.

An increased sample size is vital for achieving more representative and generalizable findings across the diverse fishing industry. A larger pool of participants will allow for a finer analysis of human error probabilities, leading to more accurate and nuanced risk assessments. This approach also promises to increase the statistical power of the research, yielding results with higher precision and less vulnerability to random variations.

Simultaneously, focusing on a well-defined subgroup of fishermen-selected based on specific criteria such as the type of fishing, geographic area, or particular risk factors faced-will enable a more detailed exploration of the unique challenges and safety issues pertinent to that group. This targeted approach will not only ensure that the survey questions are highly relevant to the respondents' experiences, thereby reducing recall and response biases, but also facilitate the collection of in-depth data on the nuanced aspects of fishing operations that influence safety and accident rates.

Future studies should consider these methodological strategies to mitigate common survey research challenges, such as sampling bias and the imprecision of data collection. Implementing these approaches will contribute to the development of a more robust and comprehensive understanding of the factors affecting human error and safety in the fishing industry. This, in turn, will inform the creation of targeted interventions

and policies designed to enhance safety practices and reduce the incidence of accidents among fishermen.

# 6. Conclusions 

In this paper, an HRA on work on fishing boats was conducted based on a survey of fishermen operating small fishing boats of less than 10 tons. CREAM was employed for HRA, and improved CREAM was utilized to address the uncertainties and non-quantitative disadvantages of the original CREAM. CFP, according to the accident, was calculated using Basic CREAM and Extended CREAM. The HEP of each fisherman was calculated using CREAM, a combination of FST and BN. The conclusions obtained through HRA are as follows:
(1) When comparing the results using basic CREAM and extended CREAM, it was found that more detailed calculations were possible when using extended CREAM, and the difference in probability depending on the accident was clearly revealed. However, due to the significant impact of the failure type on the results, it is crucial to accurately identify the specific failure type associated with each accident or operation. Among accidents involving collision while sailing, getting caught in equipment, slipping on the deck, falling inside the boat, and getting caught in fishing nets, the category with the lowest risk of error was collision while sailing, and the category with the highest was falling inside the boat. In particular, when the dynamic CPC was the worst, the CFP of falling exceeded 1 . Therefore, in small fishing boats, it is necessary to prevent falling by reinforcing railings or handles, and it is recommended not to fish in bad weather or when the equipment is in poor condition. The analysis shows that changes in dynamic conditions have a significant effect on the probability of human error in fishing boats.
(2) FST was applied to reduce uncertainty in the survey results, and the fuzzified survey results were then used as input to BN. To quantify the conditional probability of BN, we collected expert opinions and calculated CPT using a weighted sum algorithm. As a result of BN, we obtained the probability distribution of each control mode rather than one control mode. CV and HEP were calculated through a defuzzification process applying the COA method to this probability distribution. As a result of the calculation, the dominant control mode of all surveyed fishermen was strategic, and each HEP range was identical to the probability intervals of the original CREAM. All HEPs were lower than 0.002 , which shows that skilled fishermen have sufficient ability to perform tasks and respond to accidents. Through this process, it was verified that the model presented in this paper has appropriate performance for calculating the HEP.
In this study, we illustrated how CFP and HEP vary depending on the status of dynamic CPC in the ocean, where the working environment is harsh, especially for small fishing boats that are greatly affected by weather and working hours. The accuracy of HEP inference was improved by creating a quantitative HRA model combining FST, COA, BN, and CREAM, and the accuracy of the model can be further augmented by securing data through additional surveys and improving CPT.

Supplementary Materials: The following supporting information can be downloaded at: https: //www.mdpi.com/article/10.3390/su16093780/s1. Results of a survey on the effect of CPC on each accident.

Author Contributions: Conceptualization, H.K., K.K. and S.K.; methodology, H.K. and D.L.; formal analysis, D.L. and H.K.; investigation, H.K. and S.K.; data curation, D.L. and H.K.; writing-original draft preparation, D.L.; writing-review and editing, H.K. and K.K. All authors have read and agreed to the published version of the manuscript.
Funding: This research was supported by the 'Development and demonstration of data platform for AI based safe fishing vessel design (20220210)' funded by the Ministry of Oceans and Fisheries (MOF, Republic of Korea).

# Institutional Review Board Statement: Not applicable. 

Informed Consent Statement: Not applicable.
Data Availability Statement: Data are contained within the article.
Conflicts of Interest: The authors declare no conflicts of interest.
