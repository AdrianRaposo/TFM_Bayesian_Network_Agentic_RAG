Title: Personalized Pancreatic Cancer Management: A Systematic Review of How Machine Learning is Supporting Decision-making

Running Head: Hope Is Replacing Hype But Challenges Remain

Authors: Alison Bradley, MRCSEd,* $\dagger$
Robert van der Meer, PhD,*
Colin McKay, FRCS, $\dagger$
*Department of Management Science, University of Strathclyde Business School,
Glasgow, Scotland
$\dagger$ West of Scotland Pancreatic Cancer Unit, Glasgow Royal Infirmary, Glasgow, Scotland

Address Correspondence to: Alison Bradley, 34 Nasmyth Avenue, Bearsden, Glasgow, G61 4SQ, United Kingdom (e-mail: bradley_alison@live.co.uk). Tel: 07763191494 Address:

Conflicts of Interests and Source of Funding: None

Abstract: This review critically analyzes how machine learning is being utilized to support clinical decision-making in the management of potentially resectable pancreatic cancer. Following PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analyses) guidelines, electronic searches of MEDLINE, Embase, PubMed and Cochrane Database were undertaken. Studies were assessed using the Checklist for critical Appraisal and data extraction for systematic Reviews of prediction Modeling Studies (CHARMS) checklist. In total 89,959 citations were retrieved. Six studies met the inclusion criteria. Three studies were Markov decisionanalysis models comparing neoadjuvant therapy versus upfront surgery. Three studies predicted survival time using Bayesian modeling $(\bar{n}=1)$, Artificial Neural Network ( $\bar{n}$ $=1$ ), and one study explored machine learning algorithms including: Bayesian Network, decision trees, $k$-nearest neighbor, and Artificial Neural Networks. The main methodological issues identified were: limited data sources which limits generalizability and potentiates bias, lack of external validation, and the need for transparency in methods of internal validation, consecutive sampling, and selection of candidate predictors. The future direction of research relies on expanding our view of the multidisciplinary team to include professionals from computing and data science with algorithms developed in conjunction with clinicians and viewed as aids, not replacement, to traditional clinical decision-making.

Key Words: Machine learning, pancreatic cancer, decision-analysis, predictive modeling, personalized medicine

# Introduction 

The management of pancreatic cancer is particularly challenging. 12 Surgical resection is the only potentially curative treatment yet despite advances in surgical technique and adjuvant therapies 10-year survival remains less than $1 \%$. $\frac{3}{5}$ Surgical risks remain high with any potential benefit often nullified by early disease reoccurrence. ${ }^{6,7}$

Several factors have aligned making decision-making in the management of pancreatic cancer more complex. The ageing population and obesity epidemic means patients are amassing a greater amount of clinical data to consider when making clinical decisions. ${ }^{8}$ Treatment options are expanding with the emergence of neoadjuvant approach as an alternative to upfront surgery. While some are optimistic about the role of neoadjuvant therapy, others feel the current body of evidence is at best ambiguous with its role in the management of resectable pancreatic cancer being particularly controversial. ${ }^{9,12}$ This is compounded by the current lack of randomized controlled trials comparing both upfront surgery and neoadjuvant treatment pathways. ${ }^{12}$ Furthermore through the emergence of precision medicine databases will expand to reflect our understanding of disease at genomic level, creating a further 'data explosion'. ${ }^{13}$ Patients therefore represent a big data challenge not only in amount of data amassed, but in being extremely complex data systems with multidimensional problems and interacting parameters with the rules governing behaviours within layers of these systems often unclear or simply unknown. ${ }^{14}$

Personalized predictive modeling has gained precedence as a means of supporting clinical decision-making. ${ }^{15}$ However, existing predictive models, mainly based on non-liner regression techniques are limited in scope and volume regarding prognosis

as an isolated event at a pre-determined time. ${ }^{15,16}$ Machine learning methods make predictions within complex systems against a background of competing risks and events. ${ }^{14}$ Machine learning achieves this in one of three ways. Firstly supervised learning, where the computer utilizes partial labeling of data. ${ }^{17,18}$ Alternatively unsupervised learning allows the computer to make predictions or explain data by utilizing structures detected within the data itself. ${ }^{17,18}$ Thirdly reinforcement learning whereby, similar to operant conditioning, ${ }^{19}$ the computer learns from its mistakes and successes to achieve a task. ${ }^{17,20}$ Commonly employed methods of machine learning include, but are not limited to: Bayesian networks (BN), artificial neural networks (ANN) and Fuzzy-logic (FL) modeling. ${ }^{14}$ Table 1 outlines the definition, strengths and limitations of these most commonly employed methods of machine learning.

In isolation the factors outlined as contributing to the complexity of decision-making may not be unique to pancreatic cancer. However, in the context of being one of the most challenging malignancies, ${ }^{1,2}$ with comparatively lower resection rates compared to other gastrointestinal malignancies, ${ }^{1,3}$ pancreatic cancer is the ideal vehicle to critically examine how successful machine learning is in dealing with complexity and uncertainty to support clinical decision-making.

The aim of this review is to use the Checklist for critical Appraisal and data extraction for systematic Reviews of prediction Modeling Studies (CHARMS) checklist ${ }^{21}$ to critically analyze the use of machine learning for decision-analysis, prognostic and predictive purposes to support clinical decision-making in the management of potentially resectable pancreatic cancer.

# METHODS 

The protocol for this review was published in the PROSPERO online database of systematic reviews (CRD42018108926). Electronic searches of MEDLINE, Embase, PubMed and Cochrane Database were undertaken with the entire databases included up to and including $14^{\text {th }}$ September 2018, with no further date restrictions or limits applied. Full search strategies are detailed in Supplementary Digital Content 1. This review followed the PRISMA checklist. ${ }^{22}$

## Study Selection

Manual screening was carried out after removal of duplicates, based on the title and abstract of articles identified in the database searches. Articles of probable or possible relevance were reviewed in full. This was decided based on the inclusion criteria of machine learning methods applied to pancreatic cancer management decision support, published in full-text in English language. This included predictive and prognostic modeling and decision-analysis studies. Application of machine learning to diagnosis, interpretation of diagnostic imagery, and risk of developing pancreatic cancer were excluded. The focus was on application of machine learning to support clinical decision-making in the management of pancreatic cancer, following diagnosis, including prediction of survival, quality adjusted survival, and complications of treatments. The reason for this focus is that it is anticipated that personalized predictive medicine will be able to forecast individualized outcomes across competing treatment strategies to facilitate clinical decision-making. Given the afore mentioned ambiguities and controversies regarding the best management pathways for potentially resectable pancreatic cancer, ${ }^{7-12}$ this is the ideal vehicle through which to assess the contribution of machine learning in supporting clinical decision-making under uncertainty across the ever evolving patient journey. Reference lists and

citations of all included papers were manually searched to identify any additional articles. This process was repeated until no new articles were identified.

# Data Extraction, Quality Assessment, and Data Analysis 

Search design and data extraction were performed by the lead reviewer and with second author performing independent quality assurance. Discrepancies were resolved by inter-reviewer discussion. For predictive models data was extracted according to the CHARMS checklist, which also includes assessment of risk of bias. ${ }^{23}$ This checklist is designed for appraisal of all primary prediction modeling studies including ANN and vector machine learning. ${ }^{24}$

## RESULTS

## Search Results

Abstracts of 89,959 citations were retrieved. Six studies met the inclusion criteria of machine learning methods applied to predictive modeling and decision-analysis related to pancreatic cancer management (Fig. 1).

Three studies were Markov decision-analysis models comparing two competing treatment options: neoadjuvant therapy versus upfront surgery. ${ }^{25-25}$ Three studies focused on predicting survival time. ${ }^{26-28}$ One of these studies also predicted lymph node ratio. ${ }^{26}$ One of these studies additionally explored prediction of Eastern Cooperative Oncology Group (ECOG) quality-of-life scores, surgical outcomes and tumour characteristics. ${ }^{27}$ One study performed direct comparison between predictive accuracy of machine learning techniques and linear and logistic regression. ${ }^{27}$ Three studies used Marko decision tree models, ${ }^{23-25} 1$ study used Bayesian modeling, ${ }^{26} 1$ study used ANN, ${ }^{28}$ and 1 study explored machine learning algorithms including: BN, decision trees, $k$-nearest neighbor, and ANN (Table 2). ${ }^{27}$

## Decision-analysis Models

Three studies attempted to employ Markov decision analysis to compare upfront surgery and neoadjuvant approach. ${ }^{23-25}$ Sharma et al ${ }^{24}$ used data drawn from 21 prospective phase II and III trials. De Gus et al ${ }^{23}$ also included data from retrospective studies compiled from a literature search from a single search engine. Both these studies, although reportedly analyzing strategies for resectable pancreatic cancer used studies that included borderline resectable and locally advanced pancreatic cancer in an intention-to-treat analysis. ${ }^{23,24}$ All 3 studies used an intention-to-treat approach to analysis and, although they reported a slight benefit from neoadjuvant approach, neither strategy was conclusively superior. ${ }^{23-25}$ All three existing studies were solely based on synthesized evidence from published trials therefore share the limitations of the existing body of evidence mainly: heterogeneity and small underpowered sample size. ${ }^{7,8}$

# Prediction Models 

A cohort design, commonly recommended for prognostic model development, ${ }^{29}$ was used for all 3 predictive models. ${ }^{26-28}$ Two studies used retrospective single center databases (ANN, $\underline{n}=219^{28}$; comparison study, $\underline{n}=91^{27}$ ), which can limit generalizability, and 1 study used cancer data registry (BN, $\mathrm{n}=6400$ ). ${ }^{26}$ Prospective cohort designed is recommended as it enables optimal measurement of predictors and outcome. ${ }^{20}$ Retrospective cohorts are thought to yield poorer quality data but do enable longer follow-up time. ${ }^{29}$

Participant recruitment with inclusion criteria and description of cohort characteristics were well reported, as were study dates in all 3 studies. ${ }^{26-28}$ Length of follow-up time was clear in 2 studies. ${ }^{26,28}$ Consecutive sampling was reported in 1 study ${ }^{28}$ but whether all consecutive participants were included, or number of participants who

refused to participate, could not be evaluated in any of the 3 studies. ${ }^{26-28}$ Nonconsecutive sampling can introduce a risk of bias. ${ }^{31-33}$

In all 3 studies outcomes were clearly defined with the same outcome definition and method of measurement applied to all patients. ${ }^{26-28}$ The interactive Bayesian model predicted 6 month, 1-, 3- and 5-year survival post resection and lymph node ratio. ${ }^{26}$ The ANN predicted 7-month mortality after resection. ${ }^{28}$ Hayward et al focused on data mining techniques but treated survival outcome as a time-dependent-event for resected and un-resected patients, with ECOG measured at 6 months post-resection. ${ }^{27}$ Number of candidate variables ranged from 7 to 19. The definition, method and timing of measurement of candidate predictors were clear in all 3 studies. ${ }^{26-28}$ How candidate predictors were selected were not made clear in 2 studies ${ }^{26,28}$ which may be illustrative of the non-transparent 'black-box' analysis sometimes employed by forms of artificial intelligence (AI). One study extensively explored algorithms for data mining and categorization of the datasets. ${ }^{27}$ The other two studies used backward elimination methods. ${ }^{26,28}$ The ANN used single hidden layer back propagation to train the model, ${ }^{28}$ and the Bayesian model employed backward step down selection process. ${ }^{26}$ All 3 studies used complete case analysis. ${ }^{26-28}$ This approach results in loss of statistical power and can introduce bias as missing data rarely occurs randomly and often pertains to participant or disease characteristics. ${ }^{30}$

None of the studies underwent external validation. The interactive Bayesian model ${ }^{26}$ and $\mathrm{ANN}^{28}$ employed random split technique between training and validation datasets. This points to a potential key weakness in the application of machine learning techniques as random split technique can result in over and under fitting of the model, particularly as details of cross validation were not given. ${ }^{34}$ Techniques of data splitting are poorly described and can result in a high degree of variance of

model performance. ${ }^{34}$ More sophisticated techniques of data splitting that exploit the structure of the data exist and provide more confident results, but at higher computational cost, ${ }^{34}$ Only the interactive Bayesian model reported calibration with goodness-of-fit statistic ( $P=0.300$ for prediction of lymph-node-ratio; $P=0.4847$ for survival prediction). ${ }^{26}$ The ANN reported discrimination as area under curve (AUC) of the receiver operated curve (ROC) (AUC, 0.6576; sensitivity, $91.30 \%$; specificity, $38.27 \%) .^{28}$ The interactive Bayesian model reported discrimination as $c$-statistic (0.65; 95\% confidence interval [CI], 0.63-0.66). ${ }^{26}$ Although commonly used, the $c$ statistic can be influenced by predictor value distribution and be insensitive to inclusion of additional predictors. ${ }^{23}$ The study by Hayward et al. compared machine learning to log regression and found that for survival prediction Bayesian modeling out performed log regression (accuracy 0.60 versus 0.42 ). ${ }^{27}$ Furthermore in predicting outcome for ECOG at 6 months post-resection log regression performance improved from $r$-squared value, 0.26 to 0.32 when modified with machine learning algorithm 'linear regression with bagging'. ${ }^{27}$

# DISCUSSION 

## Principal Findings

Our review found 6 studies applying machine learning techniques to support clinical decision-making in the management of pancreatic cancer. Three studies used Markov decision tree models to perform decision analysis. ${ }^{23-25}$ Three studies used machine learning methods for predictive modeling: 1 study used Bayesian modeling, ${ }^{26} 1$ study used $\mathrm{ANN},{ }^{28}$ and 1 study explored machine learning algorithms including: BN, decision trees, $k$-nearest neighbor, and ANN. ${ }^{27}$ The main issues identified with decision-analysis studies were reliance on data from a single database search and the quality of the existing studies pertaining to treatment of potentially resectable

pancreatic cancer being mainly small and underpowered with a high degree of heterogeneity. ${ }^{2,8}$ The issues identified with the predictive models were overreliance on single institution retrospective database, which could affect generalizability. There was also a lack of clarity as to whether consecutive sampling was employed and how candidate predictors were selected. A major issue identified was lack of external validation across all 3 predictive models. Although 2 studies used random-split technique, details of cross-validation were not provided which potentiates issues of over or under fitting. Only one study reported calibration of their model.

# Implications for Research and Practice 

Machine learning, although in its infancy, holds great potential in its application to decision-making under complexity. ${ }^{14,35}$ However the application of machine learning to predictive modeling pertaining to the management of pancreatic cancer is currently limited in number therefore no conclusion can yet be drawn as to superiority of either machine learning or traditional modeling approaches. Only one study directly compared machine-learning methods with traditional approach to modeling. ${ }^{22}$ Accuracy of machine learning predictions, particularly Bayesian modeling, were found to be superior and predictions form log regression approach were improved when combined with machine learning techniques. ${ }^{27}$ However, it is important to note that of existing predictive studies using machine learning limitations in methodological approach were identified using the CHARMS checklist. ${ }^{21}$ These issues are similar to issues highlighted in traditional approaches to predictive modeling and include: use of single centre database limiting generalizability, sample size, lack of blinding, transparency in candidate predictor selection, and lack of external validation. ${ }^{21,29-32}$

Whilst much optimism surrounds the growing use for AI in healthcare delivery, machine learning also carries limitations that must be addressed in future research. Machine learning usually requires large amounts of data, ${ }^{36}$ which in the case of management of potentially resectable pancreatic cancer can be difficult to obtain as the majority of patients present with advanced, unresectable disease. ${ }^{1-3}$ Whilst the creation of national shared databases may be one solution to increase the volume of data, this is not without issue including dimensionality, missing data and control of bias ${ }^{37,38}$ with minority groups often under represented in such databases. ${ }^{38}$ Furthermore simply increasing volume of data is not the solution as machine learning is not yet at a stage where it can distinguish correlation and causation. ${ }^{36}$ Future research should focus on better integration of machine learning with expert knowledge to overcome this challenge. ${ }^{36}$ This review found little evidence of machine learning being actively integrated into clinical practice. Whilst this is mainly due to such techniques being in their infancy, it must also be acknowledged that some machine learning techniques are not yet sufficiently transparent which breeds distrust and resistance to their clinical application. ${ }^{36}$ Machine learning requires high levels of technical skill and can be difficult to engineer with experts from medicine, computing and data sciences often speaking in different technical language and coming to problems from different perspectives which can inhibit shared understanding and limit achievement of its full potential. ${ }^{36}$ The solution therefore lies with clinicians expanding their view of the multidisciplinary team to include professionals from computing and data science backgrounds with algorithms developed in conjunction with clinicians and viewed as aids, not replacement, to traditional clinical decisionmaking. ${ }^{6}$

Despite these challenges the study by Hayward et al ${ }^{27}$ does however corroborate other studies where application of machine-learning methods to: breast, prostate and bladder cancers have demonstrated superiority in terms of accuracy of predictions over traditional log regression. ${ }^{39-42}$ Artificial Neural Networks have also been found to perform as well as or better than traditional log regression models and also improve the diagnosis and management of pancreatitis and diagnosis pancreatic cancer. ${ }^{35}$ Machine learning methods have also been shown to out perform log regression in: providing individualized prediction of the need for neonatal resuscitation, ${ }^{43}$ predicting early mortality risk in coronary artery bypass graft surgery ${ }^{44}$ and predicting severely depressed left ventricular ejection fraction following admission to intensive care unit. ${ }^{45}$

# Strengths and Limitations 

Although limited to studies available in English language, this review is the first of its kind and goes beyond the hype surrounding use of machine learning and AI in supporting clinical decision-making to ascertain what the current reality of its application to clinical practice in management of potentially resectable pancreatic cancer actually is. Furthermore it highlights limitations that should be addressed in future research. The current number of existing studies is limited therefore conclusions about superiority of machine learning over traditional predictive modeling techniques are limited.

## CONCLUSION

To conclude clinical decision-making is going to become increasingly complex as our understanding of disease and treatment response at genomic level grows, resulting in a further 'data explosion'. ${ }^{6,13,14}$ Utilizing this expanse of data to facilitate decisionmaking in a meaningful way for individual patients is beyond the capabilities of the

human mind working in isolation. ${ }^{6,14,35}$ It is in this context that machine learning holds the greatest potential by being able to handle large amounts of data and integrate large, complex and varied databases. ${ }^{35}$ However machine learning also carries limitations and, whilst initial studies are promising, its application has yet to be widely tested. ${ }^{36}$ The future direction of research therefore relies on expanding our view of the multidisciplinary team to include professionals from computing and data science backgrounds with algorithms developed in conjunction with clinicians and viewed as aids, not replacement, to traditional clinical decision-making. ${ }^{6}$

# FIGURE LEGENDS 

FIGURE 1. PRISMA Flow Chart

# Supplementary Digital Content 

Supplementary Digital Content 1.doc: List of search terms used

# Tables: 

TABLE 1. Summary of Common Methods of Machine Learning ![img-0.jpeg](img-0.jpeg)

TABLE 2.Summary of Included Studies


# PRISMA 2009 Flow Diagram 

![img-1.jpeg](img-1.jpeg)