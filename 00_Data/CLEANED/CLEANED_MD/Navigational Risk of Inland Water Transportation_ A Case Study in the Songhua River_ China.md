# LJMU Research Online 

Xia, G, Wang, X, Feng, Y, Cao, Y, Dai, Z, Wang, H and Liu, Z<br>Navigational Risk of Inland Water Transportation: A Case Study in the Songhua River, China

http://researchonline.ljmu.ac.uk/id/eprint/23834/

## Article

Citation (please note it is advisable to refer to the publisher's version if you intend to cite from this work)

Xia, G, Wang, X, Feng, Y, Cao, Y, Dai, Z, Wang, H and Liu, Z (2023)
Navigational Risk of Inland Water Transportation: A Case Study in the Songhua River, China. Journal of Risk and Uncertainty in Engineering Systems. Part A: Civil Engineering. 9 (4).

LJMU has developed LJMU Research Online for users to access the research output of the University more effectively. Copyright © and Moral Rights for the papers on this site are retained by the individual authors and/or other copyright owners. Users may download and/or print one copy of any article(s) in LJMU Research Online to facilitate their private study or for non-commercial research. You may not engage in further distribution of the material or use it for any profit-making activities or any commercial gain.

The version presented here may differ from the published version or from the version of the record. Please see the repository URL above for details on accessing the published version and note that access may require a subscription.

For more information please contact researchonline@ljmu.ac.uk

# Navigational Risk of Inland Water Transportation: A Case Study in 

the Songhua River, China

Guoqing Xia ${ }^{1}$, Xinjian Wang ${ }^{2 *}$, Yinwei Feng ${ }^{3}$, Yuhao Cao ${ }^{4}$, Zhichao Dai ${ }^{5}$, Huanxin Wang ${ }^{6}$, Zhengjiang Liu ${ }^{7}$


#### Abstract

Compared with ocean transportation, Inland Waterway Transportation (IWT) has issues such as low configuration standard of navigation equipment, insufficient crew knowledge and skills, and relatively more complex hydrographic environment of inland waterways. To recognize and quantify the risk of IWT, this study proposes a novel risk assessment method. Firstly, the text mining by Python is applied to recognize the risk influential factors (RIFs) from Marine Accident Investigation Reports (MAIRs), and a risk evaluation hierarchy system is established. Secondly, a risk assessment model which integrated Failure Mode and Effects Analysis (FMEA), Belief Rule-based Bayesian Network (BRBN) and Evidential Reasoning (ER) is proposed to quantify the risk level of influential factors. Finally, a case study in the Songhua River is carried out to verify the feasibility and practicality of the established risk evaluation index system and research methods. The targeted preventive measures are proposed to improve the safety of IWT. This study shows that "Misobservation" and "Poor safety awareness" are the most important human factors affecting the safety of IWT, while the


[^0]
[^0]:    1. Guoqing Xia, Master student, Navigation College, Dalian Maritime University, Dalian 116026, PR China. Email: 1981538641@qq.com
    2*. Corresponding author, Xinjian Wang, Associate Professor, Navigation College, Dalian Maritime University, Dalian 116026, PR China. Email: wangxinjian@dlmu.edu.cn
    2. Yinwei Feng, Master student, Navigation College, Dalian Maritime University, Dalian 116026, PR China. Email: fyinwleo@dlmu.edu.cn
    3. Yuhao Cao, PhD student, Liverpool Logistics, Offshore and Marine (LOOM) Research Institute, Liverpool John Moores University, Liverpool L3 3AF, UK. Email: Y.Cao@ljmu.ac.uk
    4. Zhichao Dai, Accident Investigation Officer, Harbin Maritime Safety Administration, Harbin 150010, PR China. Email: 18246182789@163.com
    5. Huanxin Wang, Associate Professor, Navigation College, Dalian Maritime University, Dalian 116026, PR China. Email: wanghxdmu@dlmu.edu.cn
    6. Zhengjiang Liu, Professor, Navigation College, Dalian Maritime University, Dalian 116026, PR China. Email: liuzhengjiang@dlmu.edu.cn

organizational factors have relatively low risk priority. It is suggested that the stakeholders should strengthen the assessment of crew members and improve their ability to recognize hazards.

Key words: Maritime safety; Inland water transportation; Hazard identification; Risk assessment; Text mining; Bayesian network; Evidential reasoning

# Introduction 

As the global pandemic is brought under control, the shipping industry is entering a new phase of development, presenting new opportunities for growth and advancement (Hu et al., 2020). It is reported that, at the end of 2021, China has obtained over 125, 000 vessels with a net deadweight of about 285 million tons, representing an increase of $5.1 \%$ over last year (Ministry of Transport of China, 2022). As the shipping industry continues to expand, there is a rising demand for increased traffic volume and ship activity, which, in turn, heightens concerns regarding water transportation safety and the associated risks of ship accidents (Cao et al., 2023b; Wang et al., 2021a). Marine accidents can result in significant economic losses, as well as cause severe environmental pollution and immeasurable casualties (Wang et al., 2021b). Therefore, enhancing the prevention of water traffic accidents is not only a matter of national and people's livelihood, but also an important task of water traffic safety management.

As a major power in international trade, China has developed a water transportation system that includes inland, coastal and ocean shipping over the past few decades (Zhang et al., 2022a). Specifically, IWT plays a crucial role in the national economy due to its advantages of high profitability, accessibility and speed (Yan et al., 2019). By the end of 2021, the number of inland waterway ships has reached 113,600, accounting for 90 percent of the national water transport ships. Compared with ocean waters, the inland waterway channels are relatively narrower, especially in the waters with high density and complicated routes. Due to some historical reasons, the technology and management of IWT is still insufficient, making the inland waterway more prone to accidents (Sui et al., 2023).

The typical RIFs affecting the safety of IWT can be summarized in the following four aspects: 1) The current and water level of inland rivers are generally affected by factors such as season, rainfall, and siltation of the river channel. If the ships are failed to adapt to the change situations of water current and water level in time during navigation, accidents such as grounding may occur (Maternova et al., 2022). 2) Compared with ocean waters, inland waterways are usually narrow and curved, with

limited navigational space. If ship operators are unskilled in ship maneuvering, the chances of collision with other ships or riverbanks are increased (Deng et al., 2022). 3) Navigational obstacles such as bridges, locks, and docks in inland waterways may exist, greatly increasing the complexity of the navigational environment (Wu et al., 2017a). 4) Higher density of ships and frequent navigational traffic on inland waterways increase the probability of ship collisions and marine traffic jams (Zhang et al., 2013a). The above risks represent not only typical risk factors affecting ships on inland waterways, but also unique risk factors that differ from those of ocean navigation.

The Songhua River, as one of the major shipping channels of IWT in China, faces a significant traffic safety challenge. For example, in the second quarter of 2021, Songhua River witnessed 4 maritime accidents, resulting in 14 distressed ships, 1 sinking accident, 11 people in distress, and 9 fatalities. Therefore, it is necessary to conduct a comprehensive investigation into and mitigate the navigational risks associated with IWT in Songhua River. This includes improving the emergency response ability of vessels, enhancing the risk prevention and control system, and ensuring a stable development situation of IWT safety (Christensen et al., 2022).

Risk assessment is an effective method to prevent accidents (Aydin et al., 2022; Cao et al., 2023b; Fan et al., 2020; Yu et al., 2020). In order to enhance the safety of IWT on Songhua River, this study firstly employs the text mining technology and expert judgment to identify RIFs. Then, a risk evaluation hierarchy system is established. Secondly, the RIFs are quantitatively analysed by using a combined method of FMEA, BRBN and ER. Finally, suggestions and effective measures for IWT safety in Songhua River are proposed.

The remaining sections of this study are presented as follows. Section 2 provides a literature review of IWT, highlights the current research limitations and discusses the contributions of this study. Section 3 introduces the hazard identification methods of IWT. Section 4 proposes a risk assessment approach that combines FMEA, BRBN, and ER, along with methods for validating the model's dependability. Section 5 focuses on a case study of IWT in the Songhua River, where the RIFs are calculated, sensitivity

analysis is conducted, and the results are analysed and discussed. Finally, Section 6 provides a summary of the study and its key findings.

# Literature review 

## Hazard identification of IWT

Identifying the RIFs of IWT is a prerequisite for its risk assessment (Callesen et al., 2021). For inland waterways, the commonly used hazard identification methods include Formal concept analysis (FCA) (Hashemi et al., 2004), Event Tree Analysis (ETA) (Xing et al., 2011), Causality diagrams (Maternova et al., 2022), and so on. For example, Hashemi et al. (2004) studied the marine accidents on the Mississippi River using FCA method and identified river level and traffic volume as important indicators of accident occurrence. Xing et al. (2011) developed an ETA-based wreck probability risk assessment model for shipwreck accidents in coastal and inland waterways, and identified risk factors for ship-wreck collisions including multiple environmental attributes. Maternova et al. (2022) conducted a systematic study of the Danube accidents using causality diagrams and risk matrices to clarify the reasons and effects.

Most of the above methods identify hazards and RIFs by manual analysis of MAIRs, while the traditional methods of hazard identification are actually time consuming and laborious (Hellton et al., 2022). With the development of accident investigation technology, the International Maritime Organization and national maritime agencies continue to pay attention to expand the size of the data set of MAIRs (Yan et al., 2023). Specifically, as a novel technique for text mining has been widely applied in various fields, especially in the railroad industry (Hughes et al., 2018) and the construction industry (Feng and Chen, 2021). For the field of water transportation, Yan et al. (2023) developed a text mining-based marine accident analysis model which can provide a reliable tool for maritime safety studies. Shi et al. (2019) used the R language and text mining methods to conduct the RIFs of inland vessel collisions, providing a theory for the prevention of collisions.

## Risk assessment of IWT

Evaluating the risk of ship accidents is a key point of maritime safety studies (Zhang et al., 2021). For risk assessment of IWT, most of the quantitative analysis is carried out from the probability aspect, where BN is one of the most commonly applied risk assessment method (Lan et al., 2023; Zhang et al., 2022b). BN is commonly used to analyse inland waterway vessel collision consequences and risks (Zhang et al., 2013b), decision support solutions for stranded vessels (Wu et al., 2017b), and the risk of inland waterway congestion (Zhang et al., 2014). For example, Zhang et al. (2013b) used a combination of Formal Safety Assessment and BN to assess the risk of vessels sailing on the Yangtze River from both qualitative and quantitative perspectives. The results showed that vessel type was the parameter that had the greatest impact on the accident consequences. Yan et al. (2019) constructed a BN to assess the navigational hazards of unmanned vessels in inland waterways. Through this study, the navigational risks and the influential factors of unmanned vessels were identified and quantified. Wu et al. (2021) proposed an emergency decision model for single-ship collisions in the Yangtze River based on BN. It was found that distressed vessels running aground in the nearby shallow water was the best choice in marine accident emergency response.

The construction of BN requires input of prior probabilities, which are usually hard to obtain during the risk assessment process (Aydin et al., 2021). Moreover, BN is unable to deal with situations where assessment information is incomplete (like missing data or the infeasibility of the expert knowledge) (Yang and Xu, 2002; Yang et al., 2008). To address this issue, the ER algorithm can be applied. The ER method is an evidential reasoning algorithm which is developed by the multi-attribute assessment framework and the evidence combination rules of D-S theory (Yang and Xu, 2002). The algorithm can handle uncertain subjective data, aggregating attributes of multilevel structures to produce more reliable results (Zhang et al., 2013b). For example, Zhang et al. (2016) proposed a risk assessment method that combines ER algorithm with fuzzy theory techniques. The method was applied to the study of inland river shipping system. By transforming quantitative indexes into qualitative indexes, the method enabled a multi-level risk assessment process, progressing from lower-level evaluations to higher-level assessments. Chang et al. (2021) integrated ER and Rule-

based Bayesian networks (RBN) to evaluate the risk magnitudes of major risks associated with maritime autonomous surface ships (MASS). The results of this study provided valuable insights into the primary hazards and made notable contributions to enhance the general safety of MASS.

# Research gap and contribution 

An extensive literature analysis clearly shows that there is few research on the risk assessment of IWT, and most existed studies are on the "Yangtze River". By comparison, the traffic situation is more complicated in the Songhua River, which is located in northern China. For example, the Songhua River enters the freezing period in November every year and the thawing period is in March of the following year. During the two periods, especially the thawing period, there will be ice flowing on the river surface, which will cause certain impact to the moored ships and the risk of hull damage. Therefore, the previous studies may not necessarily applicable to the Songhua River. Based on the above, this study proposes a risk evaluation method for IWT using a combination of text mining techniques, FMEA, BRBN, and ER to identify and evaluate the RIFs of IWT on the Songhua River, and then proposes targeted risk prevention and control measures. The main research contributions of this study are as follows:
(1) The text mining method was applied to the process of inland water risk identification for the first time, and a risk identification method applicable to different waters was developed, which saves workload compared to identifying risk factors through literature review.
(2) A hybrid risk modelling and evaluation method is proposed in this study which combines FMEA, BRBN and ER to achieve reasoning from risk parameters to risk status under uncertainty.
(3) The proposed risk assessment method is used to carry out a case study, evaluate the RIFs of Songhua River in Harbin section under uncertain conditions.

## Hazard identification of IWT

To effectively extract the RIFs of IWT, based on Python text mining and expert judgment, the navigation risk of IWT is taken as the evaluation objective, and the grade evaluation structure of IWT is constructed. Secondly, the weights of RIFs are determined by Analytic Hierarchy Process (AHP). Finally, a risk assessment framework for IWT is established, as shown in Fig. 1.
![img-0.jpeg](img-0.jpeg)

Fig. 1. IWT risk identification model.

# Text mining based on Python 

Python is a programming language oriented towards concise syntax. Python can be tightly integrated with other high-level languages due to the rich library features. The main applications of Python are image processing, data mining and analysis, natural language processing, etc. Python is widely applied to text mining because of its efficient and precise scientific computing and natural language processing capabilities (Shi et al., 2019).

In this study, 341 MAIRs in 10 jurisdictions of Harbin Maritime Safety Administration (Harbin MSA) are selected as the original data information for text mining. The confusion of historical information makes it difficult to analyse inconsistent data effectively. In order to establish a reasonable database, the data must be normalized. Therefore, this study normalizes the historical accident reports based on the latest accident statistics of the Ministry of Transportation, China. In the process of

accident data processing, there are 65 MAIRs with unknown causes and 5 with ambiguous causes. The data of marine accidents with unknown causes and ambiguous causes are eliminated, and the final database of 271 marine accidents is obtained.

Then, the data is formatted to complete the construction of the corpus by extracting the causes of accidents from MAIRs and combining them with specialized vocabulary in the fields of "water transportation engineering", "safety engineering", "shipping" and "meteorology". While building the corpus, the separation of words is a very crucial step. By introducing the Jieba function library, the analysis of text content can be achieved (Yan et al., 2023). The Jieba Chinese word splitting package in Python is used to load a custom professional word bank to merge the word list. The causes of the marine accidents are then processed through word segmentation. Subsequently, word frequency statistics, word cloud generation and keyword extraction are employed to investigate the causes of marine accidents, the above steps are shown in Fig. 2.
![img-1.jpeg](img-1.jpeg)

Fig. 2. Text mining process.

In accident investigation reports, similar risk factors may differ depending on how they are recorded. Therefore, similar risk factors need to be combined. To improve the accuracy of Jieba for Chinese word separation and combination of similar risk factors, the causes of marine accidents are classified and added to a custom professional dictionary using a single line of text. Subsequently, the Jieba dictionary is upgraded and updated in UTF-8. Depending on the actual situation, the processing of the sub-words

is modified accordingly, and the words with similar semantics are combined. For example, "Improper lookout", "Inappropriate lookout", "did not maintain a proper lookout", "abnormal lookout" unified combined into "Inappropriate lookout". Subsequently, the high-frequency words in the database are obtained by means of word separation and word frequency statistics, and the results of the statistics are optimized by using stop word tables and custom word tables. Finally, the statistics of causal factors of marine accidents in Harbin section of Songhua River are shown in Table 1.

Table 1 Statistical analysis of marine accident cause factors of IWT.


# Determine evaluation indexes 

Research has shown that the accident causes of inland waterway are complicated, mainly resulting from the coupling of human factors, ship factors, environmental factors and management factors (Cao et al., 2023a). Therefore, it is not scientific to determine the risk only by the frequency of the causal factors. Accounting for the complexity and diversity of navigational risks of IWT, this study uses a combination of objective analysis and subjective judgment to investigate the safety of IWT. Based on Table 1, the Delphi method is used to organize experts to analyse the RIFs of IWT. Experts in the field are invited to score the feasibility of the indexes in Table 1 in the form of a Likert scale from 1 (highly feasible) to 5 (highly unfeasible). The indexes with an average score higher than 3 are retained and used to establish an index hierarchy system. In this study, 21 experts from Harbin MSA, managers of shipping companies and researchers from Harbin Navigation School are invited to complete the questionnaire. Among them, 4 experts are from administrative department, 11 are from law enforcement department, 4 are from shipping company and 2 are from research institution. The details are shown in Appendix A. Considering other studies (Huang et al., 2021; Wang et al., 2023; Yan et al., 2019), it is confirmed that the selected RIFs are reasonable and appropriate for the study.

With all the RIFs identified, this study divides these factors into two levels. Level I includes four aspects, which are "human factors", "organization factors", "ship factors" and "environmental factors". Level II includes 13 sub-indexes such as "Inappropriate lookout" and "Insufficient communication". This hierarchy system contributes to the clarification of the hierarchical relationship between different influential factors and provides a basis for the quantitative evaluation of RIFs. The detailed information is shown in Table 2.

Table 2 The risk assessment index hierarchy system of IWT.



# Determine Index weight based on AHP 

AHP is a method for measuring the relative significance of different objectives through the experience of decision makers, which is generally used in multi-option or multi-objective decision making process (Arslan and Turan, 2009). It provides a simple decision-making method for solving complex multi-option or multi-objective decision issues by mathematizing the decision-making process with less quantitative information based on the established hierarchy of influencing factors (Cui et al., Forthcoming). In this study, the risk indexes of different levels of IWT are compared, and the comparison matrix is constructed accordingly, and the weight of RIFs is determined through calculating the relative weights of each element. The evaluation index weights are shown in Table 3, and the specific process is shown in Appendix B.

Table 3 Relative weight of the RIFs.


## Risk Assessment of IWT

For the purpose of comprehensive and scientific analysis of RIFs of IWT, this

study proposes a risk assessment method that integrates FMEA, BRBN and ER, as shown in Fig. 3, to rank the RIFs of IWT. BRBN method enables the organic combination of belief rule base and BN. By building an effective rule base, BRBN can complete the inference from risk parameters to risk status in the form of conditional probabilities. ER can aggregate data on risk status under uncertainty and address the issues such as missing and omission of meaningful information caused by traditional data aggregation methods. Finally, the concept of utility value $U$ is proposed to translate the confidence distribution of risk status into a value expression form to obtain the ranking of the overall hazardous degree of RIFs.
![img-2.jpeg](img-2.jpeg)

Fig. 3. Risk assessment process of IWT.

# FMEA and BRBN 

FMEA is a comprehensive analysis method that aims to analyse various failure modes and their effects. The method is mainly used in the reliability engineering to obtain the impact of failures on the system from the bottom up (Shafiee and Animah, 2022; Wang et al., 2023). In this study, three risk parameters are defined as $L$ (likelihood of occurrence), $C$ (severity of consequences), and $P$ (undetected risk probability). To reach a high level of parameter discriminability, five levels of evaluation are established for each risk parameter, corresponding to the fuzzy linguistic variables shown in Table 3 of the work (Wang et al., 2023), and the definitions of each linguistic rating can be found in Table 5 of work (Chang et al., 2021).

Table 5 The inference results of RIFs.


The risk parameter $L$ refers to the likelihood of occurrence of RIFs. It serves as the primary risk parameter in the evaluation process and is an intuitive expression of the occurred probability of a risk event. The severity of consequences $C$ shows the hazards and losses caused by the occurrence of RIFs, which may result in threats to human lives, property damage, environmental damage, and adverse international impacts. The probability of failure to check the risk $P$ is an observed characteristic that prevents the occurrence of risk events and is an important index for risk management (Wan et al., 2019).

Since the FMEA approach fails to analyse risk attributes other than $L, C$ and $P$ as well as the relative significance, Yu et al. (2021b) proposed a fuzzy rule Bayesian network method for the reasoning from input variables to output variables. The $k^{\text {th }}$ IF - THEN rule $R_{k}$ in the classical rule base can be represented by Eq. (1).

$$
R_{k}: \text { If } A_{1}^{k} \wedge A_{2}^{k} \wedge \cdots A_{M_{k}}^{k}, \text { Then } D_{k}
$$

where $R_{k}$ is the risk status at the condition $k, A_{i}^{k}\left(i=1,2, \cdots, M_{k}\right)$ indicates the $i^{\text {th }}$ input condition in the $k^{\text {th }}$ rule; $M_{k}$ is the number of input conditions in the $k^{\text {th }}$ rule; $D_{k}\left(D_{k} \in D\right)$ indicates the output result of the $k^{\text {th }}$ rule; $D=\left\{D_{j}, j=1,2, \cdots, N\right\}$ indicates the set consisting of evaluation results, " $\wedge$ " indicates the logical "with" relationship.

IF-THEN rules are mainly divided into two parts: input conditions and output

results. Generally, such rules need to tackle the knowledge experience of experts and give inferred results (Yu et al., 2021a). However, this rule expression cannot reflect the detailed differences of input conditions in the result. In view of this, a new expression of knowledge for rule bases has been proposed by introducing the concept of degree of belief to solve the uncertainty problem in the process of system research (Alyami et al., 2014). On the basis of Eq. (1), a belief rule can be obtained by transforming the rule, considering all possible outcomes with the belief degree. Compared with the rule base in the traditional sense, the confidence distribution of its output results represents the comprehensive judgment of the expert on various possible situations (Wang et al., 2023; Yang et al., 2009), as shown in Eq. (2).

$$
\begin{aligned}
& R_{k}: \quad I F\left\{A_{1}^{k} \wedge A_{2}^{k} \wedge \cdots A_{M_{k}}^{k}\right\} \\
& \text { THEN }\left\{\left(D_{1}, \beta_{1, k}\right),\left(D_{2}, \beta_{2, k}\right), \cdots,\left(D_{N}, \beta_{N, k}\right)\right\}
\end{aligned}
$$

where $\beta_{j, k}(j=1, \cdots, N)$ denotes the belief of $D_{j}$ in $R_{k}$ as the output results when the input satisfies premise $A . N$ is the number of results. When $\sum_{j=1}^{N} \beta_{j, k}=1$, the belief rule information is complete; otherwise, the information is absent.

Based on the establishment of a belief rule base for risk factors, this study completes the inference of risk status through Bayesian networks. The method is applicable to nonlinear conditional expressions, where the original belief rules need to be expressed through the conditional probability form, when the rule statements are able to be transformed into Eq. (3).

$$
p\left(R_{n} \mid A_{1}^{k}, A_{2}^{k}, \cdots, A_{M}^{k}\right)=\left(\beta_{1, k}, \beta_{2, k}, \cdots, \beta_{N, k}\right)
$$

Eq. (3) can be paraphrased as follows: "when the risk parameter is $A_{1}^{k}, A_{2}^{k}, \cdots, A_{M}^{k}$, the probability of the risk status $R_{n}(n=1,2, \cdots, N)$ of the risk factor is $\left(\beta_{1, k}, \beta_{2, k}, \cdots, \beta_{N, k}\right)$ at different evaluation levels, respectively". Where, the " |" symbol indicates the conditional probability.

The existing belief rules are converted into a BN consisting of one child node from the output results and $M$ parent nodes from the input conditions. In this case, the risk inference based on the belief rule base is reduced to the calculating the edge probabilities of the sub-nodes. The prior probability of each parent node is determined by the evaluation information of the risk parameters. On this basis, an edge probability of the sub-node, which is risk status of the RIFs, can be obtained based on Eq. (4).

$$
\sum_{j=1}^{J}, \cdots, \sum_{k=1}^{K} p\left(R_{n} \mid A_{i}, B_{j}, \cdots, C_{k}\right) \times p\left(A_{i}\right) p\left(B_{j}\right), \cdots, p\left(C_{k}\right)
$$

where, $A, B, \cdots, C$ represents the premise parameters (such as $L, C$, and $P$ ); $I, J, \cdots, K$ represents the number of reference values for each premise attribute; $p\left(A_{i}\right)$ represents the probability that premise parameter $A$ takes the $i^{\text {th }}$ reference value; $p\left(\bar{R}_{n}\right)$ is the probability that the risk status (such as $R$ ) takes the $n^{\text {th }}$ reference value.

# Evidential Reasoning Algorithm 

ER method has been continuously improved and developed, and is widely used in risk analysis of complex systems, especially for assessment grade sets based on Likert scales (Wang et al., 2023; Yu et al., 2021b). In this study, the method is used to implement the aggregation operation for risk status belief. Assuming that the risk status set of factor $A$ is $\bar{R}_{A}$, the status set of factor $B$ is $\bar{R}_{B}$, and the output set of risk status obtained by aggregation operation for both is $\bar{R}_{A B}$. All the above three sets contain five levels, which are represented as Eq. (5):

$$
R_{N}=\left\{\left(R_{1}, \beta_{N}^{1}\right),\left(R_{2}, \beta_{N}^{2}\right),\left(R_{3}, \beta_{N}^{3}\right),\left(R_{4}, \beta_{N}^{4}\right),\left(R_{5}, \beta_{N}^{5}\right)\right\}
$$

where, $\beta$ is the belief distribution of different levels in the risk status; $N=(A, B, A B)$.
In the process of risk evaluation, the normalized weights of factors $A$ and $B$ are noted as $\omega_{A}$ and $\omega_{B}$. According to the definition of $\bar{R}_{A}$ and $\bar{R}_{B}$, the weighted belief parameters $M_{n}^{m}(n=A, B)$ is shown in Eq. (6).

$$
M_{n}^{m}=\omega_{n} \beta_{n}^{m}
$$

where, $m$ is the number of levels in the risk status set $m=(1,2,3,4,5)$.
$\bar{H}_{n}(n=A, B)$ is the parameter of other RIFs, $\bar{H}_{n}(n=A, B)$ is the information incompleteness parameter of $\bar{R}_{A}$ and $\bar{R}_{B}$, these two partial parameters can be obtained from Eqs. (7) and (8).

$$
\begin{gathered}
\bar{H}_{n}=1-\omega_{n} \\
\bar{H}_{n}=\omega_{n}\left(1-\sum_{m=1}^{5} \beta_{n}^{m}\right)
\end{gathered}
$$

The belief degree not assigned to $M_{n}^{m}$ can be obtained from Eq. (9).

$$
H_{n}=\bar{H}_{n}+\bar{H}_{n}
$$

$K$ is the normalization coefficient, which can be obtained from Eq. (10).

$$
K=\left(1-\sum_{s=1}^{5} \sum_{\substack{t=1 \\ t \neq s}}^{5} M_{A}^{s} M_{B}^{t}\right)^{-1}
$$

where, $M_{A}^{s}$ is the weighted belief parameter of risk influential factor $A, s=(1,2,3,4,5)$; $M_{B}^{t}$ is the weighted belief parameter of risk influential factor $B, t=(1,2,3,4,5)$.

The new belief distribution $\beta^{m}$ is obtained by aggregating risk factors $A$ and $B$ through the original data as shown in Eq. (11).

$$
\beta^{m}=\frac{K\left(M_{A}^{m} M_{B}^{m}+M_{A}^{m} H_{B}+M_{B}^{m} H_{A}\right)}{1-K\left(\bar{H}_{A} \bar{H}_{B}\right)}
$$

The calculation procedure for aggregating two pieces of evidence is given above. Considering that the ER algorithm conforms to the law of exchange and the law of combination, the evidence can be aggregated in any order when aggregating multiple risk status belief distribution data, remaining the same results (Huang et al., 2021; Loughney et al., 2021).

# Utility ranking 

In order to translate the belief distribution of risk status into a quantitative expression, the concept of utility value $U$ is required to be introduced. In this study, each risk parameter $(L, C, P)$ is provided with five evaluation levels, so the risk status R is also divided into five levels, set as $R_{1}$ to $R_{5}$, and the priority levels of risk utility values are assigned as Eq. (12):

$$
\begin{aligned}
& U\left(R_{1}\right)=R S\left(L_{1}\right) \times R S\left(C_{1}\right) \times R S\left(P_{1}\right)=1^{3}=1 \\
& U\left(R_{2}\right)=R S\left(L_{2}\right) \times R S\left(C_{2}\right) \times R S\left(P_{2}\right)=2^{3}=8 \\
& U\left(R_{3}\right)=R S\left(L_{3}\right) \times R S\left(C_{3}\right) \times R S\left(P_{3}\right)=3^{3}=27 \\
& U\left(R_{4}\right)=R S\left(L_{4}\right) \times R S\left(C_{4}\right) \times R S\left(P_{4}\right)=4^{3}=64 \\
& U\left(R_{5}\right)=R S\left(L_{5}\right) \times R S\left(C_{5}\right) \times R S\left(P_{5}\right)=5^{3}=125
\end{aligned}
$$

where, $R S$ is the quantitative assignment score for different levels of risk parameters.
Finally, the risk priority index (RPI) is calculated to achieve a precise ranking of risk factor priorities, as shown in Eq. (13), where a higher RPI value of a risk influential factor means a higher overall risk level.

$$
R P I=\sum_{h=1}^{5} p\left(R_{h}\right) \times U\left(R_{h}\right)
$$

# Validation 

The reliability of the risk assessment model applied in this study is verified through sensitivity analysis. The way to test its sensitivity is by examining how the RPI values of the risk influencing factors respond to changes in the premise attributes. If the analysis results satisfy the following three axioms, then the risk assessment model proposed in this study can be proved to be reasonable and valid. (Alyami et al., 2019; Loughney et al., 2021; Wang et al., 2023).

Axiom 1: The RPI of RIFs increases/decreases with small increase/decrease in the belief degree.

Axiom 2: If the premise attribute of RIFs is given the same varying range, the variation of RPI is proportional with the weight of the premise attribute.

Axiom 3: For the impact level of the RPI, varying combination of prerequisite attributes is greater than any subset of that combination.

## Case study

## Characteristics of water transportation in Songhua River

The Songhua River is one of the seven major shipping channels in China, located in the northern part of northeast China. It has a total length over 1900 km and an area of 556,800 square kilometres. The main channel of this river is a Chinese Class III channel with a width of 70 m and a depth of 1.7 m . The channel has a minimum bend radius of 500 m and can pass 1000 t class vessels. The inland river vessels in the river are mainly divided into cargo ships and passenger ships. Cargo ships are mainly barges, which are suitable for bulk cargo transportation. Passenger ships are used for river-toriver ferries and water tours. According to statistics of Harbin MSA, the annual average passenger traffic on the water in the Songhua River will reach 1.42 million people, the annual average cargo volume will reach 4.93 million tons during 2017 to 2021 (Huang et al., 2023).

## Calculate the risk values of level II indexes

In this study, the method of subjective belief assignment is used to carry out the collection of risk evaluation information. Subjective belief is an expert's subjective judgment about the confidence that a risk parameter belongs to a specific linguistic variable, which directly reflects the expert's knowledge and experience. During the

questionnaire survey, experts give their opinions on scoring the 13 RIFs of Level II in the hierarchy system from those three parameters. For instance, an expert's evaluation data for a parameter $L$ (likelihood of occurrence) of a risk influential factor is $\left\{p\left(L_{1}\right), p\left(L_{2}\right), p\left(L_{3}\right), p\left(L_{4}\right), p\left(L_{5}\right)\right\}$, where $\sum_{h=1}^{5} p\left(L_{h}\right) \leq 1$. The evaluation represents the occurrence probability. "Very low" is $p\left(L_{1}\right)$, "Low" is $p\left(L_{2}\right)$, "Average" is $p\left(L_{3}\right)$, "High" is $p\left(L_{4}\right)$, "Very high" is $p\left(L_{5}\right)$. The same evaluation scale is used for parameters $C$ and $P$.

In view of the similar expertise and industry experience of the investigated expert groups, in order to reflect the generality, the same weight is given to them in the process of comprehensive expert evaluation data, which means that the confidence distribution merging is completed in the form of arithmetic mean calculation. Finally, the evaluation results of RIFs ( $L, C$, and $P$ ) in level II are obtained, and the evaluation results of "Environmental factors ( $E_{4}$ )" are shown in Table 4.

Table 4 Evaluation results of RIFs in $E_{4}$.


Using the rules established in Eqs. (1) and (2), a belief rule base is established to convert experts' beliefs regarding specific RIFs, following the approach described in the study of Chang et al. (2021). The establishment of the belief rule base requires the input of the relative weights of risk parameters L, C and P. For the sake of generality, this study sets the weights of the risk parameters to the same value, which is $1 / 3$ for L , C, and P. Subsequently, the IF-THEN rule is utilized to deduce the conditional probability table for RIFs of Level II.

Calculating the risk status of the factors in Level II by using Eq. (4), taking the index " $e_{11}$ " in Table 4 as an example, the risk status can be obtained as $R\left(e_{11}\right)=(0.15,0.24,0.29,0.17,0.15)$. Similarly, the risk status of all RIFs in Level II can

be calculated, as shown in Table 5.

# Aggregate the risk values based on ER 

After calculating the risk values of RIFs of Level II, the aggregation of risk data is accomplished using the ER method by combining the weights among the indexes given in Table 3. The risk status of the Level II risk factor is used as input and the risk status of the corresponding Level I risk influential factor is used as output of the method. The risk status of " $E_{l}$ " can be calculated by Eqs. (5)-(11) as:

$$
R\left(E_{1}\right)=(0.1347,0.1744,0.2985,0.2327,0.1597)
$$

The value calculation process is explained in detail in Appendix C. According to the same method, the risk status of each risk influential factor of Level I is finally obtained by aggregating risk status from Level II to Level I, as shown in Table 6.

Table 6 Risk status of RIFs in level I.


## Calculation and analysis of the RPI

In order to compare the risk rank of Level I and Level II, the belief distribution of the risk status is converted into clear values by using the utility function for risk ranking. Taking the risk influential factor "Inappropriate lookout" for example, the RPI of the factor can be obtained by utilizing Eq. (13) and the risk values in Table 6, as shown below.

$$
\begin{aligned}
R P I\left(e_{1}\right) & =\sum_{h=1}^{5} p\left(R_{h}\right) \times U\left(R_{h}\right) \\
& =0.10 \times 1+0.14 \times 8+0.27 \times 27+0.28 \times 64+0.21 \times 125 \\
& =52.68
\end{aligned}
$$

In this way, the risk utility values for Level I and Level II can be calculated. The risk values for Level I are summarized in Fig. 4 and the risk values for Level II are summarized in Fig. 5. As shown in Fig. 4, the overall risk values of Level I RIFs are "Human factors $\left(E_{l}\right)$ ", "Ship factors $\left(E_{3}\right)$ ", "Environmental factors $\left(E_{4}\right)$ " and "Organization factors $\left(E_{2}\right)$ " in descending order. As shown in Fig. 5, the top five RIFs

for Level II are "Inappropriate lookout $\left(e_{1}\right)$ ", "Poor visibility $\left(e_{13}\right)$ ", "Bad weather $\left(e_{12}\right)$ ", "Weak safety awareness $\left(e_{4}\right)$ " and "Poor ship condition $\left(e_{9}\right)$ ".
![img-3.jpeg](img-3.jpeg)

Fig. 4. RPI values of the indexes in Level 1.
![img-4.jpeg](img-4.jpeg)

Fig. 5. RPI values of the indexes in Level 2.

# Validation 

## Sensitivity analysis of BRBN

The BRBN model proposed in this study is validated based on the three axioms in Section 4.4.

Axiom 1: Take the risk factor " $e_{6}$ " as an example: On the basis of original model, the subjective probability is reassigned to other levels with the largest increase in RPI value. When the subjective probability of the risk parameter $L_{1}$ decreases by 0.1 and $L_{5}$ increases by 0.1 , the risk status of this risk influential factor turns out to be: $R\left(e_{6}\right)=(0.03,0.18,0.28,0.25,0.16)$. The RPI value increases from 41.19 to 45.39 . The test procedure for parameters $C$ and $P$ is the same. This analysis is applied to determine the effect of changes in the subjective probability distribution between any of the three risk parameters on the RPI values. The test results for all RIFs in Level II are in accordance with axiom 1. Meanwhile, there are no outliers in the magnitude of changes in RPI values, indicating that the BRBN method used in this study has a strong logic and consistency.

Axiom 2: For each risk parameter, a subjective probability of 0.02 is reassigned each time with the largest increase in RPI value, and the change in RPI value is examined in the process of increasing the subjective probability in the interval $[0,0.1]$. Taking the risk influential factor " $e_{6}$ " for example, the calculation results are shown in Fig. 6. The comparison shows that since the belief rule base was developed giving the same weight to $\mathrm{L}, \mathrm{C}$ and P (all $1 / 3$ ), which means that the three risk parameters have the same degree of influence on the RPI values. Therefore, the test result is in accordance with axiom 2, which indicates that the BRBN method used in this case has good robustness.

![img-5.jpeg](img-5.jpeg)

Fig. 6. Sensitivity analysis of the risk parameters for results impact.

Axiom 3: The combination of three risk parameters $\left(C_{3}^{1}+C_{3}^{2}+C_{3}^{3}\right)$ is divided into three categories, and the number of risk parameters to be reassigned with subjective probabilities is 1,2 and 3 . The first category only considers the change of the probability value of a single risk parameter. The second category considers the combination of the change of the probability value of two risk parameters. The third category considers the case when the probability values of all three risk parameters change. Taking the risk factor "es" for example, each risk parameter redistributes the subjective probability of 0.1 among the different levels. The probabilities are assigned with the largest increase in RPI values, and the results of the correlated changes in RPI values are shown in Table 7.

Table 7 The influence of various risk parameter combinations on RPI.


By comparing the data in Table 7, it is possible to determine the effect of the combination of probabilistic changes. Taking combination 4 for example, the variation

value of RPI value is 7.43 . The subsets of this combination are labelled as combination 1 and combination 2. The corresponding changes in RPI value for both subsets are 3.71 and 3.72 , respectively. Both values are lower than 7.43 , thus confirming compliance with axiom 3. Similarly, through the comparative analysis between other RIFs of Level II or other combination methods, the test results are all consistent with Axiom 3, indicating that the BRBN method used in this study has sufficient reliability and rationality.

# Sensitivity analysis of ER 

On the basis of the previous validation idea, a sensitivity analysis is performed on the ER algorithm to complete the risk status aggregation operation. The sensitivity analysis in this section is conducted using the Level I risk influential factor "E4" as an example.

Axiom 1: The Level II risk factors for $E_{4}$ are "Poor channel environment (eII)", "Bad weather (eI2)" and "Poor visibility (eI3)". Redistributing the 0.1 belief degree to the different levels of $R\left(e_{I I}\right)$ in the way that worsens the risk status the most, the RPI value of " $e_{I I}$ " increases by 5.81 when the $R_{I}$ belief degree decreases by 0.1 and the $R_{5}$ belief degree increases by 0.1 . Similarly, the risk status aggregation process for the other risk factors of Level I is tested and analysed, and all results are consistent with axiom 1 , indicating that the ER aggregation algorithm used in this study is logically sound and the output results are highly sensitive.

Axiom 2: In the reassignment process, a belief degree of 0.1 is allocated to each indicator of Level I. The RPI value of Level II is then recalculated by increasing it in the direction of the maximum increment with a step of 0.02 . As shown in Fig. 7, the belief degree changes of the indexes of Level I have a significant difference in the magnitude of the effect on RPI values. The magnitude of the effect is strongly associated to the weight of the indexes of Level II in Table 3. Table 8 gives the specific RPI change values of different indexes with their corresponding weights. It remains consistent with that introduced in Axiom 2.

![img-6.jpeg](img-6.jpeg)

Fig. 7. Sensitivity analysis of the risk status for results impact.

Table 8 The change in RPI and its proportion.


Axiom 3: Taking the risk influential factor of Level I "Ship factors" as an example, the corresponding RIFs of Level II are "Poor channel environment ( $e_{11}$ )", "Bad weather $\left(e_{12}\right)$ "and "Poor visibility $\left(e_{13}\right)$ ". The possible combinations of risk factor belief changes $\left(C_{3}^{1}+C_{3}^{2}+C_{3}^{3}\right)$ are divided into three categories. For each risk status, the belief degree of 0.1 is redistributed among the different levels with the maximum increase of the RPI value for each risk parameter. The specific RPI value changes are shown in Table 9.

Table 9 The influence of various RIFs combinations on RPI.


Note: "O" represents the choice of different combinations of risk parameters

In Table 9, the subset of combination 4 includes combination 1 and combination 2. The change in RPI values corresponding to combination 1 and combination 2 are 5.81 and 4.19 , respectively, both smaller than the change in RPI value corresponding to combination 4 of 10.04 . Taking combination 7 for example, the variation value of combination 7 is 13.12 , which is larger than the change values of all subsets under this combination. The change value of combination 7 is larger than the change values of combinations 1-6, which is in accordance with axiom 3. It shows that the ER aggregation operation developed in this study is reasonable and effective, and the method has good feasibility and practicality.

# Discussion and implications 

The study shows that the top three RIFs in the Level I are "Human factors $\left(E_{1}\right)$ ", "Ship factors $\left(E_{3}\right)$ " and "Environment factors $\left(E_{4}\right)$ ", and the risk influential factor "Organization factors $\left(E_{2}\right)$ " has relatively less negative impact than the top three RIFs. Therefore, based on the above four aspects, this study selects the corresponding higher RIFs of Level II for in-depth analysis, and proposes safety measures to prevent the occurrence of marine accidents on the Songhua River.

The first is "Human factors". Among the RIFs corresponding to "Human factors", "Inappropriate lookout $\left(e_{1}\right)$ " has the largest RPI and ranks highest among the other Level II risk factors. Due to the complicated channel condition of Songhua River, when the crew is inattentive and "Inappropriate lookout", the ship is prone to danger in the process of navigation. Therefore, in order to reduce the impact of "Inappropriate lookout" for IWT safety, the captain can arrange the crew on duty reasonably to ensure that the crew can get enough rest time and prevent fatigue. The local government should also encourage all ships to install AIS through financial incentives to ensure that rescue work can be carried out quickly in case of emergency situations.

The RIFs of Level II corresponding to "Human factors": "Weak safety awareness (e4)", "Insufficient communication (e2)" and "Poor handling skills (e3)" objectively reflect the poor overall quality of inland river crew. The result is due to the underdeveloped economy of the Songhua River shipping and the poor working conditions of the crew, so most of the students graduated from the local shipping

schools go to work on the ocean vessels, and the foreign crew basically will not come to work locally. In addition, more than $70 \%$ of the crew in the Songhua River waters are over 50 years old, and the aging of the crew is serious, which increases the seriousness of these problems. Therefore, shipping enterprises should be fully aware of the importance of safety and should be alerted to possible dangers in time in their daily operation. At the same time, the maritime authority should also strengthen the practical assessment of crew and set up a standardized and rigorous selection and training mechanism. In terms of training, training sectors need focus on the practical teaching process of students, and strengthen the cultivation of the crew's practical ability. Resolutely do not allow the seafarer whose ability is not sufficient, the attitude is not correct engaged in water transportation.

Secondly, among the RIFs of Level II corresponding to the "Ship factor", the RPI value of "Poor ship condition ( $e_{9}$ )" is the highest, which indicates that the condition of vessels engaged in transportation along the Songhua River is poor. The shipping company should timely update the old ships, conduct systematic management of the existing ships and make detailed maintenance plan for the ships. The crew should report to the company in time if they find any problem on the equipment in their daily work, and if the situation is serious, they should suspend the operation in time.
"Environmental factors" is an objective cause, and the RPI value ranks third. The RIFs of Level II corresponding to "Environmental factors" are "Poor Visibility ( $e_{13}$ )", "Bad weather $\left(e_{12}\right)$ " and "Poor channel environment $\left(e_{11}\right)$ ". Due to the location of the Songhua River in northern China, there are freezing and thawing phenomena in this water, which seriously affects the safe navigation of ships. Therefore, maritime authority should strengthen information communication with emergency management departments, flood control office, meteorology office, water conservancy and other departments, pay close attention to the changes in water conditions, timely release of early warning information, scientific assessment of navigational conditions. When the appearance of dangerous environment, the authority should timely take measures to prohibit navigation and restrict navigation activities to ensure the safety of water transportation.

The final is the "Organization factors". To promote the marine safety of Songhua River, the main responsibility of shipping enterprises should be implemented. In the pursuit of profit, the shipping company must establish and improve the company's safety system, improve the crew training system, enhance the crew's sense of responsibility and mission, in order to keep all personnel always maintaining a sense of safety. Taking production and operation as the starting point, the safety work of shipping companies should strengthen the propaganda and education for crew members and improve their awareness of safety precautions through extensive organizational forms. The way of safety education also should be expanded, a sound safety management system should be built, to minimize the effects of RIFs of "insufficient crew" and "inadequate supervision" on IWT.

This study contributes to the improvement of the safety level on the Songhua River, and its theoretical and practical significance is shown below. In the theoretical level, this study innovatively applies text mining based on Python to the process of establishing a hazard identification framework, establishes a hazard identification framework and risk assessment model for IWT, identifies the RIFs, provides a quantitative and comprehensive evaluation of risk for stakeholders, reveals the current problems of inland water transportation, and proposes effective measures to improve the safety of IWT. In the practical level, the ranking of risk utility values helps stakeholders to realize the risk values of different factors, providing valuable insights for the improvement of water safety. This study also provides targeted recommendations for the safety of IWT. Firstly, it is necessary to strengthen the practical assessment of the crew, improving the overall quality and safety awareness of the inland river crew. Secondly, the personnel on board need to carry out daily maintenance of the ship, preventing the ship's equipment from breaking down, ensuring safe navigation. Finally, relevant management agencies have to pay close attention to environmental changes, alert to possible dangers in time, building a perfect safety management system.

# Conclusion 

Based on Python text mining of MAIRs, this study proposes a framework applicable to risk analysis of inland water accident, determines the risk indexes hierarchy system during ship navigation and develops a new integrated risk modelling and evaluation method. This method incorporates FMEA, BRBN and ER to infer risk status from risk parameters under uncertainty, perform aggregation operation of risk status, and comprehensively rank risk factors. The results of the study show that in Level I, human factors are the dominant RIFs affecting the safety of IWT. In Level II, the top five risk factors affecting the safety of IWT are "Inappropriate lookout", "Poor visibility", "Bad weather", "Weak safety awareness ", and "Poor ship condition ". The axiom-based validation analysis of the risk assessment model proposed in this study shows that the model is reliable and applicable.

Based on the analysis results, this study proposes targeted recommendations to promote the safety of IWT. The proposed risk assessment model for IWT can help stakeholders understand the RIFs and possible losses from the accidents, which can be used for risk control and emergency response of shipping companies as well as maritime authority, and provide scientific guidance for the development of reasonable risk control measures. However, due to the limited number of accident reports collected in this study, the interactions between the influential factors are not investigated. In the future, methods such as the data-driven BN or N-K models can be used to study the coupling relationships of risk factors.

## Appendix A: List of experts

As shown in Appendix A-Table 1.

Appendix A-Table 1 Information about experts in the risk factor questionnaire.



# Appendix B Illustration of the AHP 

For example, expert A scored the weights of "Poor channel environment", "Bad weather" and "Poor visibility" in Level II risk factors: Expert A makes a two-by-two comparison of risk factors, gives importance assignments using a 1-9 scale, and constructs a judgment matrix F based on evaluation data as follows.

$$
F=\left[\begin{array}{ccc}
1 & 6 & 6 \\
1 / 6 & 1 & 1 \\
1 / 6 & 1 & 1
\end{array}\right]
$$

This results in the weights of "Poor channel environment", "Bad weather" and "Poor visibility". Normalizing the vectors, we can obtain

$$
\bar{W}=\left(\bar{W}_{1}, \bar{W}_{2}, \bar{W}_{3}\right)^{T}=(0.749,0.126,0.126)^{T}
$$

The eigenvectors of the resulting judgment matrix, which are the weights of the three RIFs. Afterwards, by calculating the consistency index (R) of this matrix, the degree of inconsistency of the matrix is considered to be within an acceptable range ( R $<0.01$ ), so there are no logical errors in the use of this method.

# Appendix C Illustration of risk aggregation based on ER 

The risk status of "equipment maintenance is not timely" is $R_{A}$ and the risk status of "ship overload" is $R s, R_{A}$ and $R s$ can be expressed as:

$$
\begin{aligned}
& R_{A}=\left\{\left(R_{1}, 0.13\right),\left(R_{2}, 0.18\right),\left(R_{3}, 0.28\right),\left(R_{4}, 0.25\right),\left(R_{5}, 0.16\right)\right\} \\
& R_{B}=\left\{\left(R_{1}, 0.16\right),\left(R_{2}, 0.17\right),\left(R_{3}, 0.31\right),\left(R_{4}, 0.19\right),\left(R_{5}, 0.17\right)\right\}
\end{aligned}
$$

The relative weights A, B calculated from Table 3. The weighted belief parameters can be obtained from Eq. (6) as follows.

$$
\begin{aligned}
& M_{A}^{1}=\omega_{A} \beta_{A}^{1}=0.62 \times 0.13=0.0806 \\
& M_{A}^{2}=\omega_{A} \beta_{A}^{2}=0.62 \times 0.18=0.1116 \\
& M_{A}^{3}=\omega_{A} \beta_{A}^{3}=0.62 \times 0.28=0.1736 \\
& M_{A}^{4}=\omega_{A} \beta_{A}^{4}=0.62 \times 0.25=0.155 \\
& M_{A}^{5}=\omega_{A} \beta_{A}^{5}=0.62 \times 0.16=0.0992 \\
& M_{B}^{1}=\omega_{B} \beta_{B}^{1}=0.38 \times 0.16=0.0608 \\
& M_{B}^{2}=\omega_{B} \beta_{B}^{2}=0.38 \times 0.17=0.0646 \\
& M_{B}^{3}=\omega_{B} \beta_{B}^{3}=0.38 \times 0.31=0.1178 \\
& M_{B}^{4}=\omega_{B} \beta_{B}^{4}=0.38 \times 0.19=0.0722
\end{aligned}
$$

$$
M_{B}^{5}=\omega_{B} \beta_{B}^{5}=0.38 \times 0.17=0.0646
$$

The unassigned beliefs $H_{A}$ and $H_{B}$ are calculated by Eqs. (7)-(9).

$$
\begin{gathered}
\overline{H_{A}}=1-\omega_{A}=1-0.62=0.38 \\
\overline{H_{B}}=1-\omega_{B}=1-0.38=0.62 \\
H_{A}=\omega_{A}\left(1-\sum_{m=1}^{5} \beta_{A}^{m}\right)=0.62 \times(1-0.13-0.18-0.28-0.25-0.16)=0 \\
H_{B}=\omega_{A B}\left(1-\sum_{m=1}^{5} \beta_{B}^{m}\right)=0.38 \times(1-0.16-0.17-0.31-0.19-0.17)=0 \\
H_{A}=\overline{H_{A}}+H_{A}=0.38+0=0.38 \\
H_{B}=\overline{H_{B}}+H_{B}=0.62+0=0.62
\end{gathered}
$$

The normalization factor $K$ is calculated by Eq. (10).

$$
\begin{aligned}
& K=\left(1-\sum_{s=1}^{5} \sum_{t=k}^{5} M_{A}^{s} M_{B}^{t}\right)^{-1} \\
& =\left(\begin{array}{l}
1-0.0806 \times 0.0646-0.0806 \times 0.1178-0.0806 \times 0.0722-0.0806 \times 0.0646 \\
-0.1116 \times 0.0608-0.1116 \times 0.1178-0.1116 \times 0.0722-0.1116 \times 0.0646 \\
-0.1736 \times 0.0608-0.1736 \times 0.0646-0.1736 \times 0.0722-0.1736 \times 0.0646 \\
-0.1550 \times 0.0608-0.1550 \times 0.6460-0.1550 \times 0.1178-0.1550 \times 0.0646 \\
-0.0992 \times 0.0608-0.0992 \times 0.0646-0.0992 \times 0.1178-0.0992 \times 0.0646
\end{array}\right)^{-1} \\
& =1.228
\end{aligned}
$$

The aggregated results of the two risk status beliefs can be derived from Eq. (11):

$$
\begin{aligned}
\beta^{1^{\prime}} & =K\left(M_{A}^{1} M_{B}^{1}+M_{A}^{1} H_{B}+M_{B}^{1} H_{A}\right) \\
& =1.228 \times(0.0806 \times 0.0608+0.0806 \times 0.62+0.060 \times 0.38) \\
& =0.0957 \\
\beta^{2^{\prime}} & =K\left(M_{A}^{2} M_{B}^{2}+M_{A}^{2} H_{B}+M_{B}^{2} H_{A}\right) \\
& =1.228 \times(0.1116 \times 0.0646+0.1116 \times 0.62+0.0646 \times 0.38) \\
& =0.1240 \\
\beta^{3^{\prime}} & =K\left(M_{A}^{3} M_{B}^{3}+M_{A}^{3} H_{B}+M_{B}^{3} H_{A}\right) \\
& =1.228 \times(0.1736 \times 0.1178+0.1736 \times 0.62+0.1178 \times 0.38) \\
& =0.2123
\end{aligned}
$$

$$
\begin{aligned}
\beta^{4^{\prime}} & =K\left(M_{A}^{4} M_{B}^{4}+M_{A}^{4} H_{B}+M_{B}^{4} H_{A}\right) \\
& =1.228 \times(0.155 \times 0.0722+0.155 \times 0.62+0.0722 \times 0.38) \\
& =0.1654 \\
\beta^{5^{\prime}}= & K\left(M_{A}^{5} M_{B}^{5}+M_{A}^{5} H_{B}+M_{B}^{5} H_{A}\right) \\
= & 1.228 \times(0.0992 \times 0.0646+0.0992 \times 0.62+0.0646 \times 0.38) \\
= & 0.1135 \\
& \beta^{1}=\frac{\beta^{i}}{1-\bar{H}_{U}}=\frac{0.0957}{1-0.2893}=0.1347 \\
& \beta^{2}=\frac{\beta^{2}}{1-\bar{H}_{U}}=\frac{0.1240}{1-0.2893}=0.1744 \\
& \beta^{3}=\frac{\beta^{5}}{1-\bar{H}_{U}}=\frac{0.2123}{1-0.2893}=02985 \\
& \beta^{4}=\frac{\beta^{4}}{1-\bar{H}_{U}}=\frac{0.1654}{1-0.2893}=0.2327 \\
& \beta^{5}=\frac{\beta^{5}}{1-\bar{H}_{U}}=\frac{0.1135}{1-0.2893}=0.1597
\end{aligned}
$$

$\sum_{n=1}^{5} \beta^{n}=1, \beta^{I I}=0$, It means that the data of the belief distribution of the two risk status are complete. In the case of $\sum_{n=1}^{L} \beta_{n} \neq 1, \beta_{I I}$ is the residual value of the calculated belief.

Therefore, the risk status of Level I risk factor "ship factor" can be expressed as follows:

$$
R_{A B}=\left\{\left(R_{1}, 0.1347\right),\left(R_{2}, 0.1744\right),\left(R_{3}, 0.2985\right),\left(R_{4}, 0.2327\right),\left(R_{5}, 0.1597\right)\right\}
$$

# Data Availability Statement 

All data, models, or code that support the findings of this study are available from the corresponding author upon reasonable request.

## Acknowledgements

The authors gratefully acknowledge support from the National Natural Science Foundation of China [grant no. 52101399], Bolian Research Funds of Dalian Maritime University (Grant No. 3132023617), and the Fundamental Research Funds for the Central Universities (grant No. 3132023138). This work was also supported by the EU

# H2020 ERC Consolidator Grant program (TRUST Grant No. 864724). 

## References:

Alyami, H., Lee, P.T.-W., Yang, Z., Riahi, R., Bonsall, S., Wang, J., 2014. An advanced risk analysis approach for container port safety evaluation. Maritime Policy \& Management 41 (7), 634-650. https://doi.org/10.1080/03088839.2014.960498
Alyami, H., Yang, Z., Riahi, R., Bonsall, S., Wang, J., 2019. Advanced uncertainty modelling for container port risk analysis. Accident Analysis \& Prevention 123, 411-421. https://doi.org/10.1016/j.aap.2016.08.007
Arslan, O., Turan, O., 2009. Analytical investigation of marine casualties at the strait of istanbul with swot-ahp method. Maritime Policy \& Management 36 (2), 131-145. https://doi.org/10.1080/03088830902868081
Aydin, M., Akyuz, E., Turan, O., Arslan, O., 2021. Validation of risk analysis for ship collision in narrow waters by using fuzzy bayesian networks approach. Ocean Engineering 231, 108973. https://doi.org/10.1016/j.oceaneng.2021.108973
Aydin, M., Uğurlu, Ö., Boran, M., 2022. Assessment of human error contribution to maritime pilot transfer operation under hfacs-pv and slim approach. Ocean Engineering 266, 112830. https://doi.org/10.1016/j.oceaneng.2022.112830
Callesen, F.G., Blinkenberg-Thrane, M., Taylor, J.R., Kozine, I., 2021. Container ships: Fire-related risks. Journal of Marine Engineering \& Technology 20 (4), 262-277. https://doi.org/10.1080/20464177.2019.1571672
Cao, Y., Wang, X., Wang, Y., Fan, S., Wang, H., Yang, Z., Liu, Z., Wang, J., Shi, R., 2023a. Analysis of factors affecting the severity of marine accidents using a data-driven bayesian network. Ocean Engineering 269, 113563. https://doi.org/10.1016/j.oceaneng.2022.113563
Cao, Y., Wang, X., Yang, Z., Wang, J., Wang, H., Liu, Z., 2023b. Research in marine accidents: A bibliometric analysis, systematic review and future directions. Ocean Engineering 284, 115048. https://doi.org/10.1016/j.oceaneng.2023.115048
Chang, C.-H., Kontovas, C., Yu, Q., Yang, Z., 2021. Risk assessment of the operations of maritime autonomous surface ships. Reliability Engineering \& System Safety 207, 107324. https://doi.org/10.1016/j.ress.2020.107324
Christensen, M., Georgati, M., Arsanjani, J.J., 2022. A risk-based approach for determining the future potential of commercial shipping in the arctic. Journal of Marine Engineering \& Technology 21 (2), 82-99. https://doi.org/10.1080/20464177.2019.1672419

Cui, R., Liu, Z., Wang, X., FUCHI, M., KONISHI, T., Zhou, Y., Tao, J., Yang, Z., Fan, S., Zhao, Z., Forthcoming. The evaluation of seafarer fatigue as a performance shaping factor in the maritime-hra method. ASCE-ASME Journal of Risk and Uncertainty in Engineering Systems, Part A: Civil Engineering. https://doi.org/10.1061/AJRUA6/RUENG-1092
Deng, J., Liu, S., Xie, C., Liu, K., 2022. Risk coupling characteristics of maritime accidents in chinese inland and coastal waters based on n-k model. Journal of Marine Science and Engineering 10 (1). https://doi.org/10.3390/jmse10010004

Fan, S.Q., Blanco-Davis, E., Yang, Z.L., Zhang, J.F., Yan, X.P., 2020. Incorporation of human factors into maritime accident analysis using a data-driven bayesian network. Reliability Engineering \& System Safety 203, 107070. https://doi.org/10.1016/j.ress.2020.107070
Feng, D., Chen, H., 2021. A small samples training framework for deep learning-based automatic information extraction: Case study of construction accident news reports analysis. Advanced

Engineering Informatics 47, 101256. https://doi.org/10.1016/j.aei.2021.101256
Hashemi, R.R., Le Blanc, L.A., Kobayashi, T., 2004. Formal concept analysis for investigation of normal accidents. International Journal of General Systems 33 (5), 469-484. https://doi.org/10.1080/03081070412331283789
Hellton, K.H., Tveten, M., Stakkeland, M., Engebretsen, S., Haug, O., Aldrin, M., 2022. Real-time prediction of propulsion motor overheating using machine learning. Journal of Marine Engineering \& Technology 21 (6), 334-342. https://doi.org/10.1080/20464177.2021.1978745
Hu, Y.C., Zhang, Q., Park, G.K., Yang, X.F., Ieee, 2020. Automatic identification of ship navigation risk for collision accidents using uncertain regression model, Chinese Automation Congress (CAC), Shanghai, PEOPLES R CHINA, pp. 3111-3116.
Huang, D., Loughney, S., Wang, J., 2021. Identification of china's strategic transport passages in the context of the belt and road initiative. Maritime Policy \& Management, 1-26. https://doi.org/10.1080/03088839.2021.2017037
Huang, D., Wang, Y., Yin, C., 2023. Selection of co2 emission reduction measures affecting the maximum annual income of a container ship. Journal of Marine Science and Engineering 11 (3). https://doi.org/10.3390/jmse11030534
Hughes, P., Shipp, D., Figueres-Esteban, M., van Gulijk, C., 2018. From free-text to structured safety management: Introduction of a semi-automated classification method of railway hazard reports to elements on a bow-tie diagram. Safety Science 110, 11-19. https://doi.org/10.1016/j.ssci.2018.03.011
Lan, H., Ma, X., Qiao, W., Deng, W., 2023. Determining the critical risk factors for predicting the severity of ship collision accidents using a data-driven approach. Reliability Engineering \& System Safety 230, 108934. https://doi.org/10.1016/j.ress.2022.108934
Loughney, S., Wang, J., Bashir, M., Armin, M., Yang, Y., 2021. Development and application of a multiple-attribute decision-analysis methodology for site selection of floating offshore wind farms on the uk continental shelf. Sustainable Energy Technologies and Assessments 47, 101440. https://doi.org/10.1016/j.seta.2021.101440
Maternova, A., Materna, M., David, A., 2022. Revealing causal factors influencing sustainable and safe navigation in central europe. Sustainability 14 (4), 2231. https://doi.org/10.3390/su14042231
Ministry of Transport of China, 2022. Transport industry development statistical bulletin, 2021, Beijing, China.
Shafiee, M., Animah, I., 2022. An integrated fmea and mcda based risk management approach to support life extension of subsea facilities in high-pressure-high-temperature (hpht) conditions. Journal of Marine Engineering \& Technology 21 (4), 189-204. https://doi.org/10.1080/20464177.2020.1827486
Shi, S., Zhang, D., Su, Y., Zhang, M., Sun, M., Yao, H., Ieee, 2019. Risk factors analysis modeling for ship collision accident in inland river based on text mining, 5th International Conference on Transportation Information and Safety (ICTIS), Liverpool, ENGLAND, pp. 602-607.
Sui, Z., Wen, Y., Huang, Y., Song, R., Piera, M.A., 2023. Maritime accidents in the yangtze river: A time series analysis for 2011-2020. Accident; analysis and prevention 180, 106901-106901. https://doi.org/10.1016/j.aap.2022.106901
Wan, C., Yan, X., Zhang, D., Qu, Z., Yang, Z., 2019. An advanced fuzzy bayesian-based fmea approach for assessing maritime supply chain risks. Transportation Research Part E-Logistics and Transportation Review 125, 222-240. https://doi.org/10.1016/j.tre.2019.03.011

Wang, H., Liu, Z., Wang, X., Graham, T., Wang, J., 2021a. An analysis of factors affecting the severity of marine accidents. Reliability Engineering \& System Safety 210, 107513. https://doi.org/10.1016/j.ress.2021.107513
Wang, L.K., Huang, R.L., Shi, W.M., Zhang, C.Y., 2021b. Domino effect in marine accidents: Evidence from temporal association rules. Transport Policy 103, 236-244. https://doi.org/10.1016/j.tranpol.2021.02.006
Wang, X., Xia, G., Zhao, J., Wang, J., Yang, Z., Loughney, S., Fang, S., Zhang, S., Xing, Y., Liu, Z., 2023. A novel method for the risk assessment of human evacuation from cruise ships in maritime transportation. Reliability Engineering \& System Safety 230, 108887. https://doi.org/10.1016/j.ress.2022.108887
Wu, B., Wang, Y., Zong, L., Soares, C.G., Yan, X., Ieee, 2017a. Modelling the collision risk in the yangtze river using bayesian networks, 4th International Conference on Transportation Information and Safety (ICTIS), Banff, CANADA, pp. 503-509.
Wu, B., Yan, X.P., Yip, T.L., Wang, Y., 2017b. A flexible decision-support solution for intervention measures of grounded ships in the yangtze river. Ocean Engineering 141, 237-248. https://doi.org/10.1016/j.oceaneng.2017.06.021
Wu, B., Zhao, C., Yip, T.L., Jiang, D., 2021. A novel emergency decision-making model for collision accidents in the yangtze river. Ocean Engineering 223, 108622. https://doi.org/10.1016/j.oceaneng.2021.108622
Xing, H., Duan, S.L., Yu, H.L., Liu, Q.A., 2011. The study on accident probability risk assessment methods for shipwrecks in inland waterways, International Conference on Civil Engineering and Transportation (ICCET 2011), Jinan, PEOPLES R CHINA, pp. 1027-1031.
Yan, K., Wang, Y., Jia, L., Wang, W., Liu, S., Geng, Y., 2023. A content-aware corpus-based model for analysis of marine accidents. Accident Analysis and Prevention 184, 106991. https://doi.org/10.1016/j.aap.2023.106991
Yan, Y., Jin, H., Zhang, Y., Wang, J., Guo, J., Ieee, 2019. Statistical analysis of typical ship accidents in past 4 years and review of salvage equipment in china, 5th International Conference on Transportation Information and Safety (ICTIS), Liverpool, ENGLAND, pp. 1081-1085.
Yang, J.B., Xu, D.L., 2002. On the evidential reasoning algorithm for multiple attribute decision analysis under uncertainty. Ieee Transactions on Systems Man and Cybernetics Part a-Systems and Humans 32 (3), 289-304. https://doi.org/10.1109/tsmca.2002.802746
Yang, Z., Bonsall, S., Wang, J., 2008. Fuzzy rule-based bayesian reasoning approach for prioritization of failures in fmea. Ieee Transactions on Reliability 57 (3), 517-528. https://doi.org/10.1109/tr.2008.928208
Yang, Z.L., Wang, J., Bonsall, S., Fang, Q.G., 2009. Use of fuzzy evidential reasoning in maritime security assessment. Risk Analysis 29 (1), 95-120. https://doi.org/10.1111/j.15396924.2008.01158.x

Yu, Q., Liu, K., Chang, C.-H., Yang, Z., 2020. Realising advanced risk assessment of vessel traffic flows near offshore wind farms. Reliability Engineering \& System Safety 203, 107086. https://doi.org/10.1016/j.ress.2020.107086
Yu, Q., Liu, K., Yang, Z., Wang, H., Yang, Z., 2021a. Geometrical risk evaluation of the collisions between ships and offshore installations using rule-based bayesian reasoning. Reliability Engineering \& System Safety 210, 107474. https://doi.org/10.1016/j.ress.2021.107474
Yu, Q., Teixeira, A.P., Liu, K., Rong, H., Soares, C.G., 2021b. An integrated dynamic ship risk model

based on bayesian networks and evidential reasoning. Reliability Engineering \& System Safety 216. https://doi.org/10.1016/j.ress.2021.107993

Zhang, D., Yan, X., Yang, Z., Wang, J., 2013a. An accident data-based approach for congestion risk assessment of inland waterways: A yangtze river case. Proceedings of the Institution of Mechanical Engineers, Part O: Journal of Risk and Reliability 228 (2), 176-188. https://doi.org/10.1177/1748006X13508107
Zhang, D., Yan, X., Yang, Z., Wang, J., 2014. An accident data-based approach for congestion risk assessment of inland waterways: A yangtze river case. Proceedings of the Institution of Mechanical Engineers Part O-Journal of Risk and Reliability 228 (2), 176-188. https://doi.org/10.1177/1748006x13508107
Zhang, D., Yan, X., Zhang, J., Yang, Z., Wang, J., 2016. Use of fuzzy rule-based evidential reasoning approach in the navigational risk assessment of inland waterway transportation systems. Safety Science 82, 352-360. https://doi.org/10.1016/j.ssci.2015.10.004
Zhang, D., Yan, X.P., Yang, Z.L., Wall, A., Wang, J., 2013b. Incorporation of formal safety assessment and bayesian network in navigational risk estimation of the yangtze river. Reliability Engineering \& System Safety 118, 93-105. https://doi.org/10.1016/j.ress.2013.04.006
Zhang, M., Kujala, P., Hirdaris, S., 2022a. A machine learning method for the evaluation of ship grounding risk in real operational conditions. Reliability Engineering \& System Safety 226, 108697. https://doi.org/10.1016/j.ress.2022.108697

Zhang, M., Zhang, D., Fu, S., Kujala, P., Hirdaris, S., 2022b. A predictive analytics method for maritime traffic flow complexity estimation in inland waterways. Reliability Engineering \& System Safety 220. https://doi.org/10.1016/j.ress.2021.108317

Zhang, X., Wang, C., Jiang, L., An, L., Yang, R., 2021. Collision-avoidance navigation systems for maritime autonomous surface ships: A state of the art survey. Ocean Engineering 235, 109380. https://doi.org/10.1016/j.oceaneng.2021.109380