# Bayesian process mapping for intraoperative decision making in laparoscopic cholecystectomy 

Isaac Tranter-Entwistle ${ }^{1}$ (D) Bill Wilson ${ }^{2}$ (D), Tim Eglinton ${ }^{1,3}$, Saxon Connor ${ }^{1}$ (D)<br>${ }^{1}$ Department of Surgery and Critical Care, The University of Otago Christchurch, Christchurch 8140, New Zealand.<br>${ }^{2}$ Te Whatu Ora Waitaha, Christchurch, Canterbury 8140, New Zealand.<br>${ }^{3}$ Department of General Surgery Christchurch Hospital, Christchurch, Canterbury 4710, New Zealand.

Correspondence to: Dr. Isaac Tranter-Entwistle, Department of Surgery and Critical Care, The University of Otago Christchurch, 36 Cashel Street, Christchurch Central, Christchurch 8140, New Zealand. E-mail: tranter.isaac@gmail.com

How to cite this article: Tranter-Entwistle I, Wilson B, Eglinton T, Connor S. Bayesian process mapping for intraoperative decision making in laparoscopic cholecystectomy. Art Int Surg 2024;4:77-91. https://dx.doi.org/10.20517/ais.2024.04

Received: 17 Jan 2024 First Decision: 26 Mar 2024 Revised: 5 Jun 2024 Accepted: 5 Jun 2024 Published: 21 Jun 2024
Academic Editor: Andrew A. Gumbs Copy Editor: Dong-Li Li Production Editor: Dong-Li Li


#### Abstract

Aim: Surgeon's intraoperative decisions significantly impact patient outcomes. In the reconciliation cycle, interoperative decisions are guided by probabilistic reasoning, which is informed by the evolving intraoperative features. This paper aims to compare the utility of a traditional logistic regression (LR) model for critical view of safety (CVS) achievement to Bayesian network (BN) maps using intraoperative features. It hypothesizes that BN mapping better integrates with surgeon heuristics.


Methods: Using prospectively gathered intraoperative data, BN maps were developed and tested to determine their ability to predict critical view of safety achievement. Performance was compared to traditional logistic regression models to consider their utility in practice.

Results: In total, 4,663 patients were identified. Of these patients, 2,837 (61\%) presented acutely and 3,122 (67\%) were female. CVS was achieved in 4,131 (92\%) of patients. In total, four BN were developed. Optimal performance was seen in model 2 with an AUC of $0.879(0.798-0.960)(P<0.001)$. Selecting a cut-off of 0.6 gave an optimized sensitivity of $99 \%$ and a specificity of $45 \%$ for CVS achievement. In comparison to this, for the combined acute LR model, ROC curve analysis gave an AUC of $0.829(0.787-0.872)(P<0.001)$. A cut-off of $75 \%$ probability resulted in a sensitivity of $95 \%$ and a specificity of $38 \%$ for CVS achievement.

Conclusion: The present study illustrates how BN modeling can map to surgeon decision making to facilitate
(c) The Author(s) 2024. Open Access This article is licensed under a Creative Commons Attribution 4.0 International License (https://creativecommons.org/licenses/by/4.0/), which permits unrestricted use, sharing, adaptation, distribution and reproduction in any medium or format, for any purpose, even commercially, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made.

reasoning in complex environments. Further work is needed to facilitate data capture and implementation. Despite this, they represent a promising avenue for intuitive decision support tools.

Keywords: Operative process, laparoscopic cholecystectomy, artificial intelligence, Bayesian networks

# INTRODUCTION 

Surgeon's intraoperative decisions significantly impact patient outcomes. In the model described by Cristancho et al., interoperative decisions are guided by probabilistic reasoning, which is informed by the evolving intraoperative features ${ }^{[1]}$. Traditional decision support models using logistic regression analysis to generate odds ratios fail to capture these probabilistic accumulations and inter-related probabilities ${ }^{[2]}$. In contrast to this, Bayesian network (BN) maps generate conditional probabilities among a set of connected variables ${ }^{[3]}$. This mirrors the intraoperative decision-making process described by Cristancho et al. ${ }^{[1]}$. BN maps, therefore, have the potential as intraoperative decision support tools ${ }^{[4,5]}$.

BNs are useful in probabilistic causal and risk modeling due to their transparency, as well as their ability to cope with missing observations and noisy data. The node probability tables required to inform BNs can be supplied via expert judgment, learned from training data, or a combination of expert judgment and empirical data. However, BNs are computationally intensive, and only recently have advances in computing power and the underlying algorithms made BNs more accessible to researchers in many domains, including medical research ${ }^{[6]}$. In a scoping review of BNs in healthcare, McLachlan et al. found BNs referencing twenty-one categories of medical condition. The four most common, in descending order, were (i) cardiac conditions, (ii) cancer, (iii) psychological and psychiatric disorders, and (iv) lung and breathing disorders. Of note, there has been little focus on intraoperative decision making ${ }^{[7]}$. A crucial decision in laparoscopic cholecystectomy arises if hostile intraoperative findings necessitate a bailout strategy where a critical view of safety (CVS) cannot be safely achieved ${ }^{[8]}$. Current clinical guidelines lack clear indications for this decision ${ }^{[9-11]}$. BN mapping providing updated real-time probabilities using salient intraoperative features may inform this decision, providing clearer indications for when to proceed with a CVS or to perform a bailout approach. This paper aims to compare the utility of a traditional logistic regression (LR) model for CVS achievement to BN maps using intraoperative features. It hypothesizes that BN mapping better integrates with surgeon heuristics.

## METHODS

## Data capture

Data were prospectively captured from patients presenting to Christchurch Hospital for laparoscopic cholecystectomy between 2016 and 2022 using "Solutions Committed to Operative Procedure Excellence" (scOPe) (Scope Solutions Ltd), a perioperative workflow solution ${ }^{[12]}$. Data capture was routinely completed by the attending clinical team throughout the patient's operative journey. Specifically, intraoperative data were recorded by the primary surgeon at the time of the operation using synoptic operation reports. Data captured included demographics, time of booking, date of admission, and postoperative complications.

## Ethics

Ethical approval was deemed out of scope by the National Health and Disability Ethics Committee. Locality approval was sought and granted through the Canterbury District Health Board low-risk pathway (RO22146).

# Outcomes 

The primary outcome was critical view of safety achievement. Achievement of CVS was determined by the operating surgeon at the time of the operation. Achievement of CVS was defined using the SAGES consensus guidelines for safe cholecystectomy ${ }^{[8]}$ :

1. The hepato-cystic triangle was cleared of fat and fibrous tissue.
2. The lower one-third of the gallbladder was separated from the liver to expose the cystic plate.
3. Two and only two structures are seen entering the gallbladder.

## Univariate analysis and factor selection

A literature review in conjunction with expert review of the local data set was conducted to identify those factors impacting the likelihood of achieving the $\mathrm{CVS}^{[2,13-15]}$. In keeping with BN development best practice, the risk idiom was identified and used for network generation, as the research objective was to understand the relative influence of several risk factors, both individually and in temporal combinations. Factors shown to significantly impact the risk of not achieving a CVS were then included. Liver function tests were excluded due to variation in performance $<24 \mathrm{~h}$ preoperatively to ensure dataset completeness. Factors identified included:

- Admission: acute or elective
- Patient sex: male or female
- Patient age: quartiles
- White cell count: quartiles
- C-reactive protein (CRP): quartiles
- Liver appearances: normal or cirrhotic, fibrotic, fatty
- Rouviere's sulcus: visible or not visible
- Ease of gallbladder retraction: straightforward retraction or requiring dissection of adhesions
- Operative grade: Straight forward as defined by North Shore Difficulty Grade 1 and 2 or challenging as defined by North Shore Difficulty Grade 3 and 4

To assess for the significance of these factors in predicting CVS achievement, statistical analysis was conducted using IBM SPSS for Windows version 22 (IBM Corp., Armonk, N.Y., USA). Factors were dichotomized or divided into quartiles for the purposes of the BN model. Contingency tables stratifying the impact of these factors on CVS achievement were generated and Chi-square testing performed. Statistical significance was considered at $P<0.05$.

For the development and assessment of the BN model, data were split, with $70 \%$ used for model training and $30 \%$ used for model testing. For the logistic regression, data were again split, allocating $70 \%$ for model training and $30 \%$ for model testing. Patients with missing data points were excluded.

## BN model development

BNs are a method to formally represent conditional probability and causal relationships among a set of variables. Using Bayes' theorem, BNs facilitate both causal and diagnostic (inverse) reasoning based on the probability distributions of the phenomena of interest ${ }^{[16]}$. A BN consists of a directed acyclic graph, where no node can be the parent of itself, with associated node probability tables (NPT) for each node within the graph. The nodes represent each variable and edges connect dependent variables. An edge from node A to node B represents a causal assumption that node A has a causal or influential function on node B . Node A is often described as a parent of node B. The NPT is the probability distribution of the node, given the parent nodes. For nodes without parents, the NPT is just the probability distribution of the node ${ }^{[6,16]}$.

The recommended best practice for constructing BNs is to build up small network fragments using appropriate reasoning idioms ${ }^{[17]}$. General reasoning idioms include notions such as cause-consequence, definition, and measurement ${ }^{[16]}$. Specific medical idioms have also been identified as helpful in building BN through medical reasoning ${ }^{[17]}$. Examples of medical reasoning idioms include manifestation, pathogenesis, risk, treatment, complications, and comorbidities. For the Critical View of Safety BN, the risk idiom was identified as the most appropriate, as the research objective was to understand the relative influence of several risk factors, both individually and in temporal combinations.

To construct the BN, expert judgment (SC and IT-E) and relevant literature were used to identify the risk factors ${ }^{[2,18]}$. The identified risk factors serve as the nodes of the BN. These nodes can be configured to suit category, Boolean, ordinal, continuous, or integer interval data. For this research, the use of Boolean nodes supported the underlying decision-making focus of the research. The information of interest is not a specific value, but whether that value has reached a threshold for a required action. Expert clinical input also recommended separating the data into acute and elective cohorts, given the differing presentation pathways. This decision was also influenced by the differences in the available data for these two cohorts.

The options for the structural relationship of the nodes began with the simplest hypothesis, with all the predictor variables treated as independently influencing the outcome predictor variable - the critical view of safety being achieved (CVSA). A second hypothesis proposed by the surgeons was the role of the gall bladder visible inflammation grade as a mediating variable between the patient history risk factors and the outcome. Identifying such a mediating variable would provide an early warning indicator that CSVA was at risk. White cell count and CRP were hypothesized as directly influencing the inflammation grade, without additional causal paths to the outcome variable. Age and Gender were considered to have this mediating path while also retaining a direct path to the CVSA outcome. To assess these two different causality hypotheses for two patient cohorts, four BN models were built using the AgenaRisk software application (https://www.agena.ai/). The four BN models tested are summarized in Table 1, and the structural relationships between variables for each model are shown in Figures 1-4.

Having constructed the BN graphs, the NPTs for each model were trained by importing the relevant training data set. The BN uses the empirical data to define the NPT parameters for each node, by determining a joint probability distribution that best explains the relationships between the predictor and outcome variables in the data. The data contained some null values. For data with missing values, the AgenaRisk software runs an expectation maximization algorithm to achieve maximum likelihood estimation ${ }^{[16]}$. Simply put, maximum likelihood estimates the parameters of an assumed probability distribution to give the highest likelihood of the observed data ${ }^{[16]}$.

The authors followed the recommendations of Kyrimi et al. (2021) for aiding the reproducibility and usefulness of the BN models ${ }^{[2]}$. Specifically: (i) the potential clinical benefits have been explained; (ii) the BN structure and variables have been provided, with the data sets and AgenaRisk models available on reasonable request; (iii) an assessment of accuracy has been provided, and (iv) consideration of the model use in practice.

# Logistic regression model 

Significant features $(P<0.05)$ from the univariate analysis were included in the logistic regression model developed using IBM SPSS Data Modeller v18.4 (IBM Corp., Armonk, N.Y., USA). Models were considered for the combined, acute, and elective data sets.

Table 1. Differences between the four critical view of safety BN models developed


BN: Bayesian network.
![img-0.jpeg](img-0.jpeg)

Figure 1. Critical view of safety: model 1 (acute presentations only).
![img-1.jpeg](img-1.jpeg)

Figure 2. Critical view of safety: model 2 (elective presentations only).

# Validation 

Internal validation for both the BN and LR models was performed on the partitioned test set. For the LR model, AUC testing performance was assessed by generating receiver operating characteristic (ROC) curves to determine the area under the curve (AUC) and optimal sensitivities and specificities ${ }^{[18]}$. This methodology is in keeping with literature comparing BN and LR models ${ }^{[4,5]}$.

![img-2.jpeg](img-2.jpeg)

Figure 3. Critical view of safety: model 3 (acute presentations only).
![img-3.jpeg](img-3.jpeg)

Figure 4. Critical view of safety model 4 (elective presentations only).

# RESULTS 

In total, 4,663 patients were identified. Of these patients, 2,837 (61\%) presented acutely and 3,122 (67\%) were female. CVS was achieved in 4,131 (92\%) patients. Data set characteristics following division of the data into training and test sets are provided in Table 2 and the univariate analysis in Table 3.

Table 2. Demographic factors


CRP: C-reactive protein; WCC: white cell count; CVS: critical view of safety.

# Logistic regression model training 

## Combined data set

Dividing the data into a training set comprising $70 \%$ and a remaining $30 \%$ yielded a final training set of 2,636 patients, excluding those with missing variables. Logistic regression modeling produced a McFadden's pseudo R-squared of $0.206(P<0.001)$ [Table 4]. The single most significant factor in predicting whether CVS was achieved was the operative grade with an $\operatorname{Exp}(B)$ of $4.2764(P<0.001)$. Other significant factors included the youngest age quartile, easy liver retraction, and elective procedures [Table 4].

## Acute data set

When considering the acute data set separately, 1,102 patients were included in the training set once patients with missing data points were excluded. Logistic regression modeling produced a McFadden's pseudo R-squared of $0.185(P<0.001)$. CRP was the most significant factor in predicting the likelihood of CVS achievement, with a CRP in the first quartile having an $\operatorname{Exp}(B)$ of $10.87(P<0.001)$. Other significant

Table 3. Univariate analysis


CVS: Critical view of safety; CRP: C-reactive protein; WCC: white cell count.
factors included operative grade, the visibility of Rouviere's sulcus, and ease of gallbladder retraction [Table 4].

# Elective data set 

When considering the elective data set separately, 1,005 patients were included in the training set once patients with missing data points were excluded. Logistic regression modeling produced a McFadden's pseudo R-squared of $0.314(P<0.001)$. Age was the most significant factor in predicting the likelihood of CVS achievement, with an age in the second quartile having an $\operatorname{Exp}(B)$ of $12.09(P<0.001)$. Other significant factors included operative grade, the visibility of Rouviere's sulcus, and ease of gallbladder retraction [Table 4].

## Logistic regression model testing

For the combined regression model, the final $30 \%$ test split resulted in 1,207 patients in the test data set. ROC curve analysis gave an AUC of $0.829(0.787-0.872)(P<0.001)$. A cut-off of $75 \%$ probability resulted in a sensitivity of $95 \%$ and a specificity of $38 \%$. The significant class imbalance seen in the rate of CVS achievement precluded ROC curve analysis for the acute and elective subsets.

## Bayesian models

To assess for the impact of different variables on network performance, four network models were developed and assessed [Figures 1-4]. The relative importance of each feature can be seen in Figure 5.

Table 4. Logistic regression models


CRP: C-reactive protein; WCC: white cell count; NA: not applicable.

# Model 1

Model 1 is seen in Figure 1, with an AUC of $0.780(0.726-0.833)(P<0.001)$ [Figure 2]. An optimal cut-off of 0.69 gave an optimized sensitivity of $96 \%$ and a specificity of $30 \%$. Comparing model 1 to model 3 gave a Bayes factor of 1.026 [Table 5].

Table 5. Model comparison*


*Comparing the predictive models using Bayes factors. The same assumptions apply to the prior probability distribution for each model (H1 and H2), so the prior probabilities are set to 1 . The probability for the evidence (E) from the test data set is also the same for each model. In these circumstances, the Bayes factor is simply the likelihood ratio. The results in Table 1 show Bayes factors ranging from 1.0 to 1.13 which is regarded as very weak evidence. There is no basis to favour one hypothesis (model) over the other. Risk scenario R12 is an example with multiple risk factors. Further Risk scenarios are included in the Supplementary Material. CVS: Critical view of safety.

# Model 2 

Model 2 is seen in Figure 2, with an AUC of $0.879(0.798-0.960)(P<0.001)$. Selecting a cut-off of 0.6 gave an optimized sensitivity of $99 \%$ and a specificity of $45 \%$. Comparing model 2 to model 4 gave a Bayes factor of 1.001 [Table 5].

## Model 3

Model 3 is seen in Figure 3, with an AUC of $0.785(0.734-0.836)(P<0.001)$. Selecting a cut-off of 0.77 gave an optimized sensitivity of $96 \%$ and a specificity of $30 \%$.

## Model 4

Model 4 is seen in Figure 4, with an AUC of $0.879(0.798-0.960)(P<0.001)$. Selecting a cut-off of 0.6 gave an optimized sensitivity of $99 \%$ and a specificity of $45 \%$.

## DISCUSSION

BN performance was comparable to the logistic regression models, with AUCs ranging from 0.780 to 0.879 $(P<0.001)$. This is in keeping with prior literature showing comparable performance between regression and Bayesian models ${ }^{[4]}$. Performance across all BN models was comparable, as evidenced by the Bayes factors [Table 5] ${ }^{[26]}$. Across both acute and elective models, operative grade was the most consistent factor predicting CVS achievement [Figure 5 and Table 4]. This is in keeping with earlier work reaffirming the importance of considering operative technical difficulty when assessing operative process ${ }^{[13,21,22]}$. The performance of elective models was most likely superior due to reduced operative process variance. To the authors' knowledge, this is the first study illustrating the utility of BN using intraoperative features to predict an intraoperative outcome. The comparable performance across both LR and BNs depicts the potential utility of BN mapping to support intraoperative decision making. For clinical utility, higher sensitivity and specificity are needed. Achieving this will require both a better understanding of operative processes and variable capture. If improved data performance is achieved, prospective model testing in an offline manner is required before multicentre validation.

![img-4.jpeg](img-4.jpeg)

Figure 5. Tornado graph for models 1-4.

The persistent rate of common bile duct injury in the era of laparoscopic cholecystectomy has led to concerted efforts to increase the rate of CVS achievement ${ }^{[4]}$. A significant amount of this work has focused on surgeon education and improved documentation as a means of increasing achievement rates ${ }^{[11,23]}$. This has been achieved at the authors' local institution through the implementation of a standard process, resulting in a high rate of CVS achievement and excellent outcomes ${ }^{[24]}$. Increasingly, it is recognized that intraoperative factors significantly impact the ability of surgeons to achieve CVS ${ }^{[2,18]}$. This is reflected in the present study, which shows the significant impact of operative grade, gallbladder retraction and ability to identify Rouviere's sulcus on the likelihood of CVS achievement [Table 4 and Figure 5]. When looking at the tornado graphs in figure 5 for patients undergoing acute laparoscopic cholecystectomy, the ability to retract the liver had the most impact on the likelihood of CVS achievement. For elective patients, the predominant driver was inflammation grade. These findings suggest a systematic difference in the reasons for not achieving a CVS between elective and acute operations. Consequently, different operative processes might be needed to optimize the rates of achievement. These findings evidence how specific operative features impact decision making and outcomes. Generalization of this approach across different operations may lead to broader insights into optimizing operative techniques.

The clinical utility of BN models in operative decision-making lies in their ability to mirror the operative thought process of surgeons. This is in contrast to traditional LR models that provide fixed probabilities that do not integrate intuitively with clinical workflow. Additionally, given that associations between predictor variables are accounted for by BN models, they are not subject to the same issues with multicollinearity encountered in regression models ${ }^{[25]}$. Furthermore, their ability to incorporate patients with missing data further facilitates their application in clinically uncertain environments. Cristancho et al.'s model breaks intraoperative decision making into the steps of assessing the information, reconciling this with known information, and implementing a plan of action ${ }^{[1]}$. In this model, the surgeon proceeds with the plan of action that has the highest probability of success. This is currently implicit, but by mirroring this process, BN can make these probabilities explicit, with probabilities at each step of the operation updated as more information becomes available, as illustrated in the Supplementary Material. This stepwise process also illustrates the significance of each factor [Supplementary Material]. For senior surgeons, these probabilities would supplement the current decision-making process, while for surgical trainees, BNs could act as prompts to consider all available evidence and facilitate reasoning in an uncertain environment. This is likely to be highly beneficial to trainees who have not yet had the procedural experience to develop the rich process maps and high-level heuristics of surgical consultants ${ }^{[26,27]}$. Alternatively, post-procedure reflection could be informed using counterfactual probabilities generated from the BN. These could provide prompts for discussing the possible impact of different steps taken during the operation.

To achieve this, however, high-accuracy models using well-validated, broad data sets will be required. Currently, models have a high sensitivity and low specificity for CVS achievement. This is reflective of the significant class imbalance in the present data set, with a $92 \%$ chance of achieving a CVS. This contrasts with the broader literature which shows a variable rate of CVS achievement, especially when this is externally reviewed ${ }^{[10,11]}$. In the present data set, a subtotal cholecystectomy was frequently performed when a CVS could not be achieved. This, coupled with the low McFadden's pseudo R-squared values seen in the regression models, would suggest that a considerable number of factors influencing decision making have not been captured in the current models. This is more marked in the acute setting with an R-squared of 0.185 compared to 0.314 for the elective patients. It is likely that this is due to elective patients representing a more homogenous range of pathophysiological status and a smaller amount of variation in process compared to acute patients ${ }^{[22]}$. This is driven by operative technical difficulty with previous work identifying a higher proportion of grade 3 and 4 operative findings in acute patients ${ }^{[13,24]}$. Taken together, these findings

suggest that the significant class imbalance seen could be addressed through subgroup analysis of subtotal cholecystectomy. Focused video analysis of these patients may identify significant factors driving intraoperative decision making. Given the lack of clear indications for subtotal cholecystectomy included in current guidelines, this would contribute significantly to standardizing practice and improving patient care.

Despite a significant clinical interest in the study of BNs, there is no literature concerning their implementation into practice or gold standard for model development ${ }^{[1]}$. Early work has demonstrated their utility in personalized risk prediction for malignancy in patients with Barrett's oesophagus. This reflects both challenges in development, data set requirements, and the significant barriers around testing and implementation. In the present study, BN models were developed by reviewing existing literature and expert opinion of features predicting CVS achievement. These were then arranged hierarchically using an iterative improvement process. Initial model development concerned the impact of setting an observation on a causal path. By creating a causal pathway as soon as the inflammation grade value was defined in an observation, the parent nodes such as age and gender were blocked. To correct this, a revised model was developed, including a direct and indirect path between the parent nodes, and the outcome variable (CVSA) was generated. A more effective means of developing BN maps may be using cognitive task analysis. Work by Hashimoto et al. has illustrated that surgeon knowledge can be made explicit through process mapping ${ }^{[26]}$. Such an approach may increase model performance by enabling the capture of a wider variety of data points.

A weakness of the present study was the lack of granularity seen across the network maps. Initially ranked nodes were felt to offer more granular insight than Boolean nodes. However, even with a large data set, the number of possible combinations resulted in insufficient procedures among the training and test data. Converting all nodes to Boolean helped but did not completely eliminate this problem. For eight Boolean predictor variables, there are 256 possible combinations that subdivide the data. This precluded the inclusion of specific surgeons as factors in predicting the likelihood of CVS achievement. In the present study, over 40 surgeons undertook one of the documented operations. The inclusion of each surgeon in the BN would have resulted in a vast number of probability pathways. This highlights a problem in BNs in general and is representative of a broader issue in applying machine learning techniques to healthcare. Given the huge volume of data generated by healthcare, the bottleneck lies not in its generation but rather in its capture and organization. This is further reflected in the scant examples of ML-based decision support tools in clinical practice in contrast to the rapidly increasing literature touting their potential utility. Integration of these tools into practice will require a re-imagining of the clinical workflow to enable data to be captured as part of workflow. Doing so will allow for the development, application, and validation of these novel tools.

In keeping with AI model development, the current paper represents a proof of concept. Further clinical work, along with more refined data sets, is imperative to enable better prediction. Upon achieving this offline, prospective validation is needed to ensure the safety of application. Following confirmation, realtime risk prediction becomes feasible. However, model development should progress using multicentre data to ensure generalizability. Subsequent local testing is then necessary to validate the model's applicability within its specific environment.

The present study illustrates how BN modeling can map surgeon decision making to facilitate reasoning in complex environments. Additional efforts are required to facilitate data capture and implementation. Nevertheless, they present a promising avenue for intuitive decision support tools.

# DECLARATIONS 

## Authors' contributions

Conceived, performed data gathering, drafted and reviewed the present study: Tranter-Entwistle I
Conceived, drafted and reviewed the present study, participated in video annotation for an unrelated study, contributed to the development of a freely available educational application around laparoscopic cholecystectomy: Connor S
Conceived, drafted and reviewed the present study: Wilson B
Drafted and reviewed the present study: Eglinton T

## Availability of data and materials

Data and materials are available upon reasonable request.

## Financial support and sponsorship

None.

## Conflicts of interest

Tranter-Entwistle I has received funding from Medtronic to pursue a PhD. Connor S has provided pro bono consultancy for Digital Surgery LTD. Wilson B declares no conflicts of interest. Eglinton T has provided consultancy for Digital Surgery Ltd, which is separate from the present study.

## Ethical approval and consent to participate

Ethical approval was deemed out of scope by the National Health and Disability Ethics Committee. Locality approval was sought and granted through the Canterbury District Health Board low risk pathway (RO\#22146). Patients were consented for their procedures and data prospectively captured.

## Consent for publication

Not applicable.

## Copyright

(c) The Author(s) 2024.
