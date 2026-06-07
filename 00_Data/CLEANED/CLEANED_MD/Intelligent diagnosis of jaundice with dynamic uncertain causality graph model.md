Journal of Zhejiang University-SCIENCE B (Biomedicine \& Biotechnology)
ISSN 1673-1581 (Print); ISSN 1862-1783 (Online)
www.zju.edu.cn/zjus; www.springerlink.com
E-mail: jzus@zju.edu.cn

# Intelligent diagnosis of jaundice with dynamic uncertain causality graph model* 

Shao-rui $\mathrm{HAO}^{\ddagger 1}$, Shi-chao GENG ${ }^{\S 2,3}$, Lin-xiao $\mathrm{FAN}^{\S 1}$, Jia-jia $\mathrm{CHEN}^{1}$, Qin ZHANG ${ }^{\dagger \S 3}$, Lan-juan $\mathrm{LI}^{\dagger \S 1}$<br>${ }^{\dagger}$ State Key Laboratory for Diagnosis and Treatment of Infectious Diseases, Collaborative Innovation Center for Diagnosis and Treatment of Infectious Diseases, the First Affiliated Hospital, School of Medicine, Zhejiang University, Hangzhou 310003, China)<br>${ }^{\text {§ }}$ School of Communication, Shandong Normal University, Jinan 250014, China)<br>${ }^{\dagger}$ School of Computer Science and Engineering, Beihang University, Beijing 100191, China)<br>${ }^{\dagger}$ E-mail: zhangqin@buaa.edu.cn; ljli@zju.edu.cn<br>Received June 15, 2016; Revision accepted Oct. 17, 2016; Crosschecked Apr. 19, 2017


#### Abstract

Jaundice is a common and complex clinical symptom potentially occurring in hepatology, general surgery, pediatrics, infectious diseases, gynecology, and obstetrics, and it is fairly difficult to distinguish the cause of jaundice in clinical practice, especially for general practitioners in less developed regions. With collaboration between physicians and artificial intelligence engineers, a comprehensive knowledge base relevant to jaundice was created based on demographic information, symptoms, physical signs, laboratory tests, imaging diagnosis, medical histories, and risk factors. Then a diagnostic modeling and reasoning system using the dynamic uncertain causality graph was proposed. A modularized modeling scheme was presented to reduce the complexity of model construction, providing multiple perspectives and arbitrary granularity for disease causality representations. A "chaining" inference algorithm and weighted logic operation mechanism were employed to guarantee the exactness and efficiency of diagnostic reasoning under situations of incomplete and uncertain information. Moreover, the causal interactions among diseases and symptoms intuitively demonstrated the reasoning process in a graphical manner. Verification was performed using 203 randomly pooled clinical cases, and the accuracy was $99.01 \%$ and $84.73 \%$, respectively, with or without laboratory tests in the model. The solutions were more explicable and convincing than common methods such as Bayesian Networks, further increasing the objectivity of clinical decision-making. The promising results indicated that our model could be potentially used in intelligent diagnosis and help decrease public health expenditure.


Key words: Jaundice; Intelligent diagnosis; Dynamic uncertain causality graph; Expert system http://dx.doi.org/10.1631/jzus.B1600273

## 1 Introduction

The ability to more accurately predict and prevent disease has the potential to transform clinical practice. However, what limits the accuracy of disease predicting and prevention results from our limitation in understanding the link between clinical

[^0]presentation and disease progression (Madabhushi et al., 2010). Although vast amounts of data are collected in clinical practice, ranging from organ images to blood and genetic tests, there are challenges associated with analyzing, combining, and correlating these data to make diagnostic predictions. Currently, although the perception of evidence-based medicine is widely accepted and various sorts of clinical pathways and guidelines are put forward and renewed, the diagnostic method is still influenced by subjective factors and the correct diagnosis is largely correlated with doctors' comprehensive experience. Regional imbalances of health care and physician training in


[^0]:    ${ }^{\dagger}$ Corresponding authors
    ${ }^{\ddagger}$ The authors contributed equally to this work
    Project supported by the Medical and Health Research Program of Zhejiang Province (No. 2015KYB128) and the Zhejiang Provincial Natural Science Foundation (No. LQ15H030004), China
    ORCID: Shao-rui HAO, http://orcid.org/0000-0003-3455-7395
    (C) Zhejiang University and Springer-Verlag Berlin Heidelberg 2017

specializations have made diagnosis difficult in a complex clinical background. Intelligent diagnosis approaches have the potential to cover rare situations across a wide range of specialist domains, while no clinical expert can be expected to possess such an encyclopedic knowledge of disease manifestations. Recently, artificial intelligence diagnostic tools have given rise to more and more interest in the biomedical community, and offered a promising improvement in sensitivity and specificity of disease detection, diagnosis, and prognosis. Until now, various clinical expert systems based on rules, cases, fuzzy logic, Neural Networks, Bayesian Networks, or hybrid reasoning have been developed (Keith et al., 1995; Hatzilygeroudis and Prentzas, 2004; Malek et al., 2005; Sasikumar et al., 2007; Lee, 2008; Avci, 2012; Oladipupo et al., 2012; Siniscalchi et al., 2014; Shen et al., 2015), and have been used as diagnosis aids across a wide range of specialties, such as vertigo (Dong et al., 2014a), Alzheimer's disease (Suk et al., 2014), autism (Bhat et al., 2014), image diagnosis (Li et al., 2014), and pathological diagnosis (Kruk et al., 2014).

As a technical development, the dynamic uncertain causality graph (DUCG) method which deals with the causal link between uncertain information with graphical expression and probability measurement is proposed (Zhang et al., 2014; Zhang, 2015a). DUCG is a probabilistic graphical model which intuitively expresses a causal relationship among variables in an explicit pattern, and uses a "chaining" inference algorithm to achieve efficient reasoning. DUCG can propagate probabilities through causality chains, achieve dynamic reasoning either with or without spread of causality between time slices (Zhang and Geng, 2015), achieve reasoning in the case of logic circles (Zhang, 2015a), and handle fuzzy evidence (Zhang, 2015b). The greatest advantage of DUCG in clinical diagnosis is that it can display the reasoning process and results graphically, and make an inference with incomplete information and less accurate parameters than conventional methods such as Bayesian Networks. The DUCG model has been applied in the clinical diagnosis of vertigo (Dong et al., 2014a) and for troubleshooting in nuclear power station electric generators, spacecraft power systems, and chemical process systems (Dong et al., 2014b) with competitive results.

Jaundice is a common and complex clinical symptom with potential involvement in hepatology, general surgery, infectious diseases, pediatrics, genetic diseases, gynecology, and obstetrics, and it is fairly difficult to distinguish jaundice as a cause in clinical practice (Bhutani and Johnson-Hamerman, 2015; Gottesman et al., 2015). An intelligent diagnosis tool would greatly improve the general level of health care, decrease public health expenditure, and offer distinctive value in the less developed areas of the world. In this paper, we used the DUCG theory to build an intelligent diagnosis system for jaundice and tested its validity in clinical cases.

## 2 Methods

### 2.1 Graphical representation

DUCG as a newly developed framework of intelligent system represents complex causalities explicitly and easily with graphical symbols including logic gates. In DUCG, $X_{n k}$ is commonly used and represents any event variable state with the first subscript used to index the variable and the second subscript to index the state of the variable, between which a comma is used for separation and can be ignored when there is no confusion. The conditional probability between a child $X_{n k}$ and its parent $V_{i j}$ is replaced by the weighted causal functional events $F_{n k, i j}$ and their occurrence probabilities $f_{n k, i j}=\left(r_{n, i} / r_{n}\right) a_{n k, i j}$, where $a_{n k, i j}=\operatorname{Pr}\left\{A_{n k, i j}\right\}$ and $A_{n k, i j}$ is the virtual random event that $V_{i j}$ causes $X_{n k}, "$," is used to divide the subscripts of parent $V_{i}$ and the subscripts of child $X_{n}, r_{n, i}>0$ is the causal relationship intensity between $V_{i}$ and $X_{n}$, $r_{n} \equiv \sum_{i} r_{n, i}$. It is obvious that $a$-type parameters quantify the uncertain causality between $V_{i j}$ and $X_{n k}$ and $r_{n, i} / r_{n}$ is in effect the weighting factor of this causality. When we do not have samples, we can give parameters of $f_{n k, i j}$ directly according to the domain expert's knowledge.

A simple DUCG sub-graph is shown in Fig. 1, while the variable types used and their graphic meanings are shown in Table 1.

### 2.2 Development of jaundice knowledge base

A DUCG represents a causality structure among event variables. For a specific disease related to jaundice, it can be the sorting of the causality

![img-0.jpeg](img-0.jpeg)

Fig. 1 A simple sub-graph representing typical construction of DUCG

Table 1 Medical meaning of variables used in DUCG model


relationship among symptoms, signs, laboratory tests, disease, and pivotal complications. In the construction of a knowledgebase, symptoms, signs, and laboratory tests are expressed in separate sub-graphs, so that the medical knowledge base is easily understood. Firstly, a " $B$ "-type variable is created to represent a specific disease with a priori probability. Then, the corresponding integrated causal variable " $B X$ " is created to represent the integrated probability of the disease weighted by a combination of the disease incidence (" $B$ ") and the impact of the demographic information (" $X$ ") and risk factors (" $X$ ") along with $D$-type events. After that, categorical variables such as symptom, sign, and test were created and con-
nected to the " $B X$ " variable with weighted functional variable " $F$ " as its downstream part. The $\{b-, a-, r-\}$ type parameter values were adopted in the parameter setting where key symptom, sign, and test have a relatively high values depending on their clinical significance. A sum of 27 most common jaundicerelated diseases was contained in the knowledge base.

Five senior clinical experts were invited to help with the determination of each $F$-type causal functional event. First, reference research was performed to set up reference values for those widely accepted causal effect events such as risk factors, probability of a certain sign or symptom in a certain disease, or the positive rate of certain clinical testing or imaging in a certain disease. When published data were not available for some causal effect event, local research was done based on history cohorts to examine the primary value. After that, the five clinical experts evaluated the whole probability sheet separately, and if the primary value is not agreed, a new value will be demanded. When two or more experts disagreed with the primary value, it would be discussed in a meeting and the mean value would be chosen if no agreement was achieved.

### 2.3 Inference calculation

The inference calculation was performed in home-made DUCG diagnosis software where four key steps, i.e. simplification, decomposition, event expanding, and probability calculation, were carried out. The detailed algorithm has been demonstrated previously (Zhang, 2012; 2015a) and is briefly illustrated as follows.

The inference process is basically to analyze the causal logic with the information obtained and to determine whether a reasonable candidate hypothesis (a pair of $B$ and $B X$ events) is sufficient to account for current abnormalities.

The first step of DUCG inference is to simplify the graphical knowledge base conditional on observations before other calculations, so that the scale and complexity of the diagnosis process can be reduced exponentially. The simplification process is based on the 10 reduction rules of DUCG (Zhang, 2012), during which non-existent and non-sense variables and causal relationships are deleted. These rules can be applied repeatedly until no more simplification can be performed.

Then, the decomposition was performed aiming to reduce the scale of the causality structure during the diagnosis process. By assuming different disease $B_{i j}$, a large and complex DUCG can be divided into a set of sub-DUCG graphs, which are overall exhaustive. The DUCG model can find the symptoms associated with each $B$-type variable (disease) by the above strategy.

Before probabilistic calculation, the event expanding operations were conducted on the observed abnormal evidence $E=\prod_{n} X_{n k}$ based on each sub-DUCG to avoid redundant calculations and decrease the overall reasoning cost. Event expanding was performed according to Eq. (1) until reaching $B$-type events, during which the $B X$-type candidate hypotheses and hypothesis space $S_{\mathrm{H}}$ are obtained.

$$
X_{n k}=\sum_{i} F_{n k, i} V_{i}=\sum_{i}\left(r_{n, i} / r_{n}\right) \sum_{i} A_{n k, i j} V_{i j}
$$

where $V_{i}(V \in\{X, B, G, D\})$ are the parents of $X_{n k} . G$ represents logic gate variable type which is not used in this study. $H_{k, j}$ and $H_{k, j} E$ can also be expanded based on Eq. (1), where $H_{k, j}$ corresponds to $B X_{k, j}$ and then $B_{k, j}$. During the event expanding of $E$ and $H_{k, j} E$, logic operations, such as AND, OR, XOR, NOT, absorption, exclusion, and complement, are applied. The corresponding probability calculation of the logic expression is similar to

$$
x_{n k}=\sum_{i} f_{n k, i} v_{i}=\sum_{i}\left(r_{n, i} / r_{n}\right) \sum_{j} a_{n k, i j} v_{i j}
$$

where $a, f$, and $v$ represent corresponding probabilities.
Finally, probabilistic calculations were carried out according to

$$
\begin{gathered}
h_{k, j}^{*} \equiv \operatorname{Pr}\left\{H_{k, j} \mid E\right\}=\frac{\operatorname{Pr}\left\{H_{k, j} E\right\}}{\operatorname{Pr}\{E\}} \\
h_{k, j}^{*} \equiv \frac{h_{k, j}^{*}}{\sum_{H_{k, j} \in S_{\mathrm{H}}} h_{k, j}^{*}}=\frac{\operatorname{Pr}\left\{H_{k, j} E\right\}}{\sum_{H_{k, j} \in S_{\mathrm{H}}} \operatorname{Pr}\left\{H_{k, j} E\right\}}
\end{gathered}
$$

where $h^{*}$ and $h^{t}$ represent the posterior probability and rank probability of $H_{k, j}$, respectively.

### 2.4 Jaundice diagnostic model verification

Patients hospitalized in the First Affiliated Hospital of Zhejiang University (Hangzhou, China) with elevation of serum total bilirubin (twice as high as the upper limit) were selected. The study protocol was approved by the Human Ethics Committee of the First Affiliated Hospital, School of Medicine, Zhejiang University and a written informed consent to participate in the study was signed. In total 203 cases covering the 27 most common jaundice-related diseases were extracted from the hospital information system, accounting for $5.09 \%$ of qualified cases. Ten cases were randomly selected for each disease, and when fewer than 10 cases exist for a disease in the system of the hospital, all the cases were included.

Home-made information management software was used to collect and store the related demographic and medical information. The diagnosis of each case was performed with the DUCG jaundice diagnostic model. For each case, the calculation was performed twice with or without laboratory tests and imaging tests to verify the diagnostic power of symptoms and signs alone. After probabilistic calculation, posterior probability of possible diseases was calculated and sorted according to the rank probabilities $h_{k j}^{*}$ calculated by Eq. (4).

## 3 Results

### 3.1 Jaundice diagnostic model on DUCG

In sum, 421 variables and 1062 causes were included in the DUCG graph (Fig. 2). A sub-DUCG for hepatitis C is shown in Fig. 3 and the diagnosis process is explained in detail as follows. The diagnostic system can merge these sub-graphs to obtain the whole knowledge graph of jaundice as shown in Fig. 2. In the process of reasoning and calculation, the inference engine uses the whole knowledge graph.

The definitions of variables used in hepatitis C sub-DUCG graphs are outlined in Table 2. Hepatitis C is a common cause of liver dysfunction and elevation of bilirubin characterized by hepatitis C virus (HCV) infection and has a high prevalence in blood transfusion, hemodialysis, and intravenous drug abuse. The symptoms of hepatitis C are mostly non-specific, including loss of appetite, nausea, fever,

![img-1.jpeg](img-1.jpeg)

Fig. 2 DUCG graph for jaundice diagnosis
![img-2.jpeg](img-2.jpeg)

Fig. 3 Sub-DUCG for hepatitis C
jaundice, dark urine, and fatigue. The laboratory findings include specific testing (HCV RNA and antiHCV IgG), common liver dysfunction indexes (bilirubin, alanine transaminase (ALT), aspartate aminotransferase (AST), and urobilinogen), and findings related to its complications (leukopenia, thrombocytopenia, globulin, and $\alpha$-1-fetoprotein (AFP)). HCV cause complications such as liver cancer, fatty liver, and cirrhosis.

In one case, the symptoms, physical signs, laboratory and imaging tests are transformed into corresponding variable states as follows: $E_{\mathrm{S} 1}=X_{1,1}$;

Table 2 Variable definitions in the sub-DUCG of hepatitis C


$E_{\mathrm{S} 2}=X_{2,6} ; E_{\mathrm{S} 3}=X_{8,1} ; E_{\mathrm{S} 4}=X_{44,1} ; E_{\mathrm{S} 5}=X_{1032,1} ; E_{\mathrm{C} 1}=X_{3010,2} ;$ $E_{\mathrm{C} 2}=X_{3011,4} ; \quad E_{\mathrm{C} 3}=X_{3012,4} ; \quad E_{\mathrm{C} 4}=X_{3119,1} ; \quad E_{\mathrm{C} 5}=X_{3023,1} ;$ $E_{\mathrm{C} 6}=X_{3043,1} ; \quad E_{\mathrm{C} 7}=X_{3048,1} ; \quad E_{\mathrm{C} 8}=X_{3049,1} ; \quad E_{\mathrm{C} 9}=X_{3064,1} ;$ $E_{\mathrm{C} 10}=X_{3066,1}$. The symbol $E_{\mathrm{S} i}$ represents evidence

of symptoms and physical signs, and $E_{\mathrm{C} i}$ denotesrelevant evidence from laboratory and imaging tests. All knowledge base variables for symptoms, physical signs, and tests are in the normal state, while the statuses of intermediate variables such as complications are set in an "unknown" state. In the first step of diagnosis, only $E_{\mathrm{Si}}$ was included in the model and 19 possible diseases were inferred, among which common reasons of jaundice such as bile stone and druginduced liver injury were included. These have a higher probability rank (Table 3). "Jaundice during pregnancy" is excluded, because all its diseasespecific manifestations are negative; seven diseases, such as "hyperthyroidism" and "hepatolenticular nuclear lesions", are excluded because they cannot explain two or more abnormal symptoms. During the second step, the evidence of $E_{\mathrm{Si}}$ and $E_{\mathrm{C} i}$ was entered into the DUCG clinical diagnosis decision system and performed by DUCG software automatically. The result indicates hepatitis C as the only result (ranking as $100 \%$ ), and the simplified DUCG is shown in Fig. 4 that clearly explains the causalities of the disease and all related factors, symptoms, and test results.

### 3.2 Diagnostic performance

To verify the efficacy of the DUCG diagnostic system, we tested 203 jaundice-related cases. The

Table 3 DUCG inference results based on symptoms and physical signs


![img-3.jpeg](img-3.jpeg)

Fig. 4 DUCG diagnostic result of a "hepatitis C" example (a) The simplified DUCG of "hepatitis C" based on symptoms and physical signs only; (b) The simplified DUCG resulted from full evidence. The symbols are shown in Table 1. Blue circles represent decreased value lower than its lower normal limit, while yellow and orange circles represent moderate or high elevation to upper normal limit, respectively
overall diagnosis accuracy with evidence without laboratory or imaging tests was $83.33 \%$, while the accuracy was raised to $99.01 \%$ with laboratory and imaging tests. The number of cases and detailed diagnostic results are presented in Table 4.

## 4 Discussion

This study proposed a computer-aided diagnostic system of jaundice in primary clinics based on the DUCG model. Intelligent diagnosis can make up for personal knowledge limitations and specialty limitations, and this could increase diagnostic efficacy and accuracy.

Since the Bayesian Network is currently a widely recognized way of dealing with uncertain causal relations, the comparison between the Bayesian Network approach and DUCG should be noted. The Bayesian Network expresses the causal relationship among variables by means of graphs and structured forms, and expresses the conditional probability distribution through a conditional probability table (Pearl, 2009). The Bayesian Network can use the evidence to achieve the forward, reverse, or hybrid probability reasoning and possesses the advantages of intuitive graphical representation, clear physical meaning, strict probabilistic theory base, easy use of statistical data, localized calculation, and a rigorous theoretical system (Xu, 2012). However, the

Table 4 Overall accuracy of the DUCG diagnostic system


NAFLD: nonalcoholic fatty liver disease; PNH: paroxysmal nocturnal hemoglobinuria; AHE: autoimmune hemolytic anemia; IBDS: intrahepatic bile duct stone; DILI: drug-induced liver injury

Bayesian Network cannot deal with a static logic loop or a directed cyclic graph, and these are difficult to avoid in complex closed-loop feedback systems or interaction mechanisms in the field of complex disease diagnosis. This is because a directed cyclic graph cannot be established in Bayesian Network algorithm by its definition of a factorization graphic representation of the joint probability distribution of a set of variables. In addition, the Bayesian Network relies heavily on structural learning and parameter learning from the sample data, and when there are insufficient samples, the conditional probability table needs large and complete conditional probability parameters from domain experts, which is basically impossible to achieve. In addition, although the structure learning results of a Bayesian Network may be objective and can effectively match the sample data, it may not correspond to the knowledge structure of domain experts because its poor interpretability makes the result difficult to understand and accept by domain experts (Poole and Zhang, 2003).

In contrast, DUCG possesses the character of graphical representation and low parameter dependence, which perfectly fit the use for clinical diagnosis. DUCG uses a causal matrix to express causal effect probabilities, and does not require expression of the correspondence among all states of causal variables.

In other words, the expression of the conditional probability distribution can be incomplete, which means that in constructing the causal matrix of the DUCG knowledge base, only the concerned causal relationship and its uncertainty need to be expressed, and the "not concerned" relationship can be ignored, which greatly reduces the difficulty and complexity of DUCG knowledge base construction. In addition, the first step of DUCG reasoning calculation is a logic operation, during which the original DUCG knowledge base will be greatly reduced in size and complexity according to the input information, and qualitative possible result sets will be obtained. If the simplified DUCG knowledge base contains only one possible outcome, the inference computation is

completed without any numerical calculation. So the DUCG does not require high probability accuracy and has a high robustness and stability. The benefits of this study are listed as follows.

Firstly, other inference methods, such as the Bayesian Network, rely on complex conditional probability tables and the results are hard to translate into explainable clinical language. Taking the hepatitis C case we exhibited before as an example, the DUCG system can display which abnormalities are related to the proposed diagnosis for what logical reasons. In addition, it can also tell us which abnormalities are not explained in the model. Clinicians can evaluate the proposed diagnosis with their professional knowledge rather than facing an intricate diagnosis probability. This combination can further increase diagnostic accuracy and facilitate its clinical application.

Secondly, traditional diagnostic models rely heavily on precise probability parameters, and this might directly affect the result. In this study, the DUCG model can obtain a satisfactory result with most of parameters specified by the domain experts based on their knowledge and experience. In clinical practice, with the shift of demographic characteristics and social characteristics, fixed probability faces the need of constant updating which is time-consuming and of low efficacy. With the feature of a loose probability restriction, DUCG can perform a correct diagnosis under dynamic circumstances.

## 5 Conclusions

The DUCG model has the features of graphical representation and low-parameter dependence, which facilitate its application in medical diagnosis. The jaundice diagnostic system possesses the advantage of easy construction, fast computation, high accuracy, and universal scope of application.

Future work will be focused on integrating semantics recognition into this system, which will automatically analyze the nature of the language used and the variants of medical nomenclature, and translate the imaging testing description into a corresponding imaging diagnosis. Such a combination will improve diagnosis accuracy and efficacy, and reduce the burden on public health care resource.

## Contributors

Shao-rui HAO, Shi-chao GENG, and Lin-xiao FAN performed the experiments, analyzed data, and wrote the manuscript. Jia-jia CHEN helped with determination of $F$-type causal functional event. Qin ZHANG and Lan-juan LI conceived and supervised the study, and revised the manuscript.

## Compliance with ethics guidelines

Shao-rui HAO, Shi-chao GENG, Lin-xiao FAN, Jia-jia CHEN, Qin ZHANG, and Lan-juan LI declare that they have no conflict of interest.

All procedures followed were in accordance with the ethical standards of the Human Ethics Committee of the First Affiliated Hospital, School of Medicine, Zhejiang University and with the Helsinki Declaration of 1975, as revised in 2008. Informed consent was obtained from all patients for being included in the study.

## 中文篇要

题 目：基于动态不确定性因果图（DUCG）模型的黄疸待查智能诊断研究
目的：黄疸待查是一个常见而复杂的临床问题，涉及到内、外、妇、儿等多个学科。目前我国医学专家存在数量相对不足，分布不均匀等情况，导致了区域性和部门性医疗服务水平不足。本研究旨在建立一个客观的黄疸待查智能诊断系统，以提高医学诊断的正确性，提升基层医院及急诊的诊断水平，同时减少病人的花费。
创新点：本研究采用了国际先进的动态不确定性因果图 （DUCG）模型，建立了黄疸待查相关疾病的知识库，通过 203 例临床病例的测试，其准确率达 $99.01 \%$ 。文章以图形化的方式给出了疾病的诊断过程，方便医师理解和学习。
方法：本研究采用了 DUCG 模型进行疾病诊断，首先根据 DUCG 模型的定义和黄疸诊断思路建立了包含 27 种黄疸相关疾病（表 4）的知识库（图2），其中包括了疾病的危险因素、临床症状和体征、客观检查检验结果等。然后与根据 DUCG 算法 （公式 1-4）编写的推理软件相结合形成诊断系统，对 203 例临床黄疸患者进行智能诊断，准确率达 $99.01 \%$ 。最后对一例丙型病毒性肝炎患者的具体诊断过程进行了拆解阐述，体现了 DUCG模型适用于复杂逻辑关系、计算效率高、不依赖推理概率和结果易于理解等优点。
结论：DUCG 模型成功实现了对黄疸待查相关疾病的智能诊断，准确率高，实用性好。该方法具有在其他医学领域推广应用的价值。
关键词：动态不确定性因果图（DUCG）；人工智能；黄疸；智能诊断