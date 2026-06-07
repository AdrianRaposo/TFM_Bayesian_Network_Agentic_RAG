# 4 

## World Journal of

Gastroenterology

## Agresian network-based survival prediction model for patients having undergone post-transjugular intrahepatic portosystemic shunt for portal hypertension

Rong Chen, Ling Luo, Yun-Zhi Zhang, Zhen Liu, An-Lin Liu, Yi-Wen Zhang

Specialty type: Gastroenterology and hepatology

Provenance and peer review: Unsolicited article; Externally peer reviewed.

Peer-review model: Single blind

## Peer-review report's scientific quality classification

Grade A (Excellent): 0
Grade B (Very good): B
Grade C (Good): 0
Grade D (Fair): 0
Grade E (Poor): 0
P-Reviewer: Beeraka NM, India
Received: December 29, 2023
Peer-review started: December 29, 2023
First decision: January 9, 2024
Revised: February 1, 2024
Accepted: March 19, 2024
Article in press: March 19, 2024
Published online: April 7, 2024

Rong Chen, Ling Luo, Yun-Zhi Zhang, Zhen Liu, An-Lin Liu, Yi-Wen Zhang, Department of Infectious Diseases, Second Affiliated Hospital of Chongqing Medical University, Chongqing 400016, China

Corresponding author: Ling Luo, MNurs, Researcher, Department of Infectious Diseases, Second Affiliated Hospital of Chongqing Medical University, No. 288 Tianwen Avenue, Nanan District, Chongqing 400016, China. 117765@cqmu.edu.cn

## Abstract

BACKGROUND
Portal hypertension (PHT), primarily induced by cirrhosis, manifests severe symptoms impacting patient survival. Although transjugular intrahepatic portosystemic shunt (TIPS) is a critical intervention for managing PHT, it carries risks like hepatic encephalopathy, thus affecting patient survival prognosis. To our knowledge, existing prognostic models for post-TIPS survival in patients with PHT fail to account for the interplay among and collective impact of various prognostic factors on outcomes. Consequently, the development of an innovative modeling approach is essential to address this limitation.

## AIM

To develop and validate a Bayesian network (BN)-based survival prediction model for patients with cirrhosis-induced PHT having undergone TIPS.

## METHODS

The clinical data of 393 patients with cirrhosis-induced PHT who underwent TIPS surgery at the Second Affiliated Hospital of Chongqing Medical University between January 2015 and May 2022 were retrospectively analyzed. Variables were selected using Cox and least absolute shrinkage and selection operator regression methods, and a BN-based model was established and evaluated to predict survival in patients having undergone TIPS surgery for PHT.

## RESULTS

Variable selection revealed the following as key factors impacting survival: age, ascites, hypertension, indications for TIPS, postoperative portal vein pressure (post-PVP), aspartate aminotransferase, alkaline phosphatase, total bilirubin, prealbumin, the Child-Pugh grade, and the model for end-stage liver disease

(MELD) score. Based on the above-mentioned variables, a BN-based 2-year survival prognostic prediction model was constructed, which identified the following factors to be directly linked to the survival time: age, ascites, indications for TIPS, concurrent hypertension, post-PVP, the Child-Pugh grade, and the MELD score. The Bayesian information criterion was 3589.04, and 10-fold cross-validation indicated an average log-likelihood loss of 5.55 with a standard deviation of 0.16 . The model's accuracy, precision, recall, and F1 score were $0.90,0.92,0.97$, and 0.95 respectively, with the area under the receiver operating characteristic curve being 0.72 .

# CONCLUSION 

This study successfully developed a BN-based survival prediction model with good predictive capabilities. It offers valuable insights for treatment strategies and prognostic evaluations in patients having undergone TIPS surgery for PHT.

Key Words: Bayesian network; Cirrhosis; Portal hypertension; Transjugular intrahepatic portosystemic shunt; Survival prediction model
(C)The Author(s) 2024. Published by Baishideng Publishing Group Inc. All rights reserved.

Core Tip: This study introduces an advanced Bayesian network model to better understand the interrelationships among prognostic factors and their combined impact on prognosis, thus enhancing the accuracy of survival predictions for patients with cirrhosis-induced portal hypertension after the transjugular intrahepatic portosystemic shunt procedure. This approach potentially assists in refining and advancing current prognostic research.

Citation: Chen R, Luo L, Zhang YZ, Liu Z, Liu AL, Zhang YW. Bayesian network-based survival prediction model for patients having undergone post-transjugular intrahepatic portosystemic shunt for portal hypertension. World J Gastroenterol 2024; 30(13): 1859-1870
URL: https://www.wjgnet.com/1007-9327/full/v30/i13/1859.htm
DOI: https://dx.doi.org/10.3748/wjg.v30.i13.1859

## INTRODUCTION

Portal hypertension (PHT) is primarily characterized by a significant increase in venous pressure within the portal venous system. This condition often results in severe symptoms like refractory ascites and bleeding from esophageal and gastric varices, which exacerbate disease progression and profoundly impact survival prognosis[1]. Cirrhosis accounts for approximately $90 \%$ of PHT cases[2]. The transjugular intrahepatic portosystemic shunt (TIPS) procedure represents a crucial intervention in effectively managing PHT and its complications[3]. However, studies indicate that TIPS, while effective in lowering the portal vein pressure (PVP), may lead to complications like hepatic encephalopathy and stentrelated dysfunctions, thus influencing overall patient survival rates[4,5]. Therefore, it is crucial to actively identify and thoroughly analyze the prognostic factors and their interrelations after TIPS in PHT.

Previous research on prognostic factors for TIPS in PHT has shown that preoperative factors, including total bilirubin (TBIL) levels, serum creatinine (SCr), and sarcopenia, are correlated with patient survival after TIPS surgery[3,6,7]. Recent multivariate survival analyses, such as those by Huang et al[8], have used logistic regression to identify clinical variables that significantly affect post-TIPS outcomes in patients with cirrhosis, resulting in the creation of a support vector machine model focused on liver disease-related mortality. Sun et al[9] used a random forest algorithm in combination with variables including age and Child-Pugh scores to develop a model for predicting disease-free survival in cirrhotic patients having PHT who were treated with TIPS. Li et al[10] assessed the 5-year survival rates in Chinese patients with cirrhosis undergoing TIPS placement using Viatorr ${ }^{\circledR}$ stents, identified post-TIPS overt hepatic encephalopathy (OHE) and Child-Pugh grade as independent prognostic factors for mortality, and developed a nomogram-based predictive model for post-TIPS OHE. However, these studies did not explore the interrelationships and mechanisms of prognostic factors. Consequently, using more advanced modeling techniques to deeply investigate the interactions among these factors is crucial.

Bayesian networks (BNs), based on the Bayesian theorem, are a type of machine learning algorithm. They combine prior knowledge with data, illustrate variable relationships through directed acyclic graphs, and elucidate node connections using conditional probabilities[11]. By integrating probability and graph theories, BNs effectively demonstrate the interactions among independent variables and their complex relationships with dependent variables in factor analysis[12]. Consequently, BNs are a powerful tool for predictive, classificatory, and causal analyses in data mining. Recently, BNs have been extensively applied in risk assessment and prognosis prediction for various diseases. For example, Li et al[13] used several factors, such as age, carcinoembryonic antigen, and carbohydrate antigen 19-9, to develop a BN model predicting the prognosis of rectal cancer and achieved an area under the receiver operating characteristic curve (AUC) of 0.801 . Similarly, Wu et al[14] used parameters like age, pathological grade, and liver infiltration to develop a BN model for predicting survival in gallbladder cancer patients after radical cholecystectomy. This model

showed internal and external validation AUCs of 0.757 and 0.765, respectively, which exceeded the accuracy of traditional nomograms. However, to our knowledge, no research yet has used BNs to analyze the prognosis of patients having undergone TIPS surgery for PHT.

In this study, we focus on comprehensive analysis of factors affecting post-TIPS prognosis in patients with PHT, using BN approaches to fully assess preoperative factors. We herein aim to reveal the interdependencies among these factors and to develop a BN model that predicts patient survival after TIPS, thus providing substantial data support for clinical decision-making.

## MATERIALS AND METHODS

### Study participants

In this retrospective study, we collected data of 393 patients with cirrhosis-induced PHT who received their first TIPS treatment at the Second Affiliated Hospital of Chongqing Medical University between January 2015 and May 2022. Follow-up involved outpatient visits, hospital admissions, and phone calls, and we documented all-cause mortality and liver transplants during and after hospitalization until May 2023. The inclusion criteria were as follows: (1) Age ≥ 18 years; (2) meeting the diagnostic criteria for cirrhosis based on the “2019 Cirrhosis Diagnosis and Treatment Guidelines” [1]; (3) showing PHT-related complications like hepatic ascites and variceal hemorrhage; and (4) receiving TIPS treatment for the first time. The exclusion criteria were as follows: (1) Individuals with significant cardiac, pulmonary, or renal conditions; (2) PHT cases not related to cirrhosis; (3) patients with coexisting malignancies; and (4) patients having previously received TIPS or liver transplants.

### Data collection and processing

Data collection included patients' baseline information, disease-related metrics, laboratory results, and overall survival times. Following literature review and expert advice, 34 potential prognostic factors were identified for analysis. These include sex, age, etiology of cirrhosis, diabetes, hypertension, indications for TIPS, the portal vein thrombosis status, endoscopic therapy history, splenectomy history, ascites, preoperative hepatic encephalopathy, spontaneous bacterial peritonitis, type of stent, preoperative PVP (pre-PVP), postoperative PVP (post-PVP), the Child-Pugh grade, the model for end-stage liver disease (MELD) score, and laboratory values such as serum potassium, sodium (Na), SCr, blood urea nitrogen, albumin (ALB), alanine aminotransferase, aspartate aminotransferase (AST), alkaline phosphatase (ALP), gamma-glutamyl transferase, TBIL, prealbumin (PA), international normalized ratio, prothrombin time (PT), fibrinogen, hemoglobin, white blood cell count (WBC), and platelets. Missing data were imputed using maximum likelihood estimation, with continuous variables discretized for analysis. Considering varying follow-up durations among patients, 24 months was selected as a key time point, with clinical laboratory indicators discretized based on reference values. Child-Pugh grading was as follows: A (5-6 points), B (7-9 points), and C (10-15 points). MELD scores were as follows: > 18 (high risk), 15-18 (moderate risk), and ≤ 14 (low risk). Optimal cutoffs for patient age, pre-PVP, and post-PVP were determined using the X-tile software (Yale University, V3.6.1).

### Variable selection

Variable selection combined Cox analysis with least absolute shrinkage and selection operator (LASSO) regression. Variables showing an association with the outcome in univariate Cox regression analysis (P < 0.05) were then analyzed using LASSO regression to identify significant predictors of prognosis for BN development.

### Statistical analysis

Simple statistical descriptive analyses and survival analyses were performed using IBM SPSS 25 (IBM Corporation, Armonk, NY, United States). All categorical variables were expressed as numbers and percentages. Survival rates were calculated using the Kaplan-Meier method. Univariate analysis was performed through Cox regression; variables with a P value of < 0.05 were considered significant and included in further LASSO regression analysis. The execution of LASSO regression and the generation of survival curve were carried out using the Free Statistics analysis platform (Version 1.9, FreeClinical Medical Technology Co. Ltd. Beijing, China). The bnlearn package in RStudio (version 4.3.1) facilitated the development of BN models using a tabu search algorithm for structural learning, incorporating expert input for whitelist and blacklist settings, and learning network parameters through maximum likelihood estimation. Model performance assessment and validation used the Bayesian information criterion (BIC) and 10-fold cross-validation. Evaluation metrics included accuracy, precision, recall, F1 score, and AUC values. The BN's topological structure and conditional probability inferences were drawn by Netica 32.0 (Norsys Software Corp. Vancouver, BC, Canada).

## RESULTS

### Participant characteristics

The study included 393 patients with PHT, comprising 278 male (70.7%) and 115 female patients (29.3%). The median age at the time of surgery was 51 years (range, 45-58 years), with the predominant cause of cirrhosis being hepatitis B virus infection (64.6%), as detailed in Table 1. During the follow-up period, 68 patients died. The cumulative survival rates at 1, 3, and 5 years were 96.2%, 87.9%, and 76.6%, respectively, as shown in Figure 1.

Table 1: Baseline characteristics of the study cohort, n (%)



${ }^{1}$ Combined stent: Covered stent + bare stent.
TIPS: Transjugular intrahepatic portosystemic shunt; PVT: Portal vein thrombosis; pre-HE: Preoperative hepatic encephalopathy; SBP: Spontaneous bacterial peritonitis; pre-PVP: Preoperative portal vein pressures; post-PVP: Postoperative portal vein pressures; K: Potassium; Na: Sodium; SCr: Serum creatinine; BUN: Blood urea nitrogen; ALB: Albumin; ALT: Alanine aminotransferase; AST: Aspartate aminotransferase; ALP: Alkaline phosphatase; GGT: Gamma-glutamyl transferase; TBIL: Total bilirubin; PA: Prealbumin; INR: International normalized ratio; PT: Prothrombin time; FIB: Fibrinogen; Hh: Hemoglobin; WBC: White blood cell count; PLT: Platelets; MELD: Model for end-stage liver disease.
![img-0.jpeg](img-0.jpeg)

Figure 1 Overall survival of the study cohort.

# Variable selection results 

Univariate Cox regression analysis: A univariate Cox regression analysis was conducted on all collected variables potentially affecting post-TIPS survival in patients with PHT. Results indicated that factors of age, etiology of cirrhosis, hypertension, indications for TIPS, ascites, post-PVP, Na, ALB, AST, ALP, TBIL, PA, PT, WBC, the Child-Pugh grade, and the MELD score were associated with overall post-TIPS survival $(P<0.05)$, as shown in Table 2.

Least absolute shrinkage and selection operator regression analysis: Factors with a $P$ value of $<0.05$ in the univariate Cox regression were subjected to LASSO regression analysis. We selected the optimal lambda value (lambda.min $=0.027$ ). The results indicated that age, ascites, hypertension, indications for TIPS, post-PVP, AST, ALP, TBIL, PA, the Child-Pugh grade, and the MELD score were significantly related to overall patient survival, as shown in Figure 2.

## BN survival prediction model for patients having undergone TIPS surgery for PHT

The abovementioned 11 prognostic factors identified by univariate Cox and LASSO regression were incorporated into the BN model, and its topological structure is shown in Figure 3. The BN model in this study illustrated 12 nodes and 17 directed edges, wherein each node signifies a factor influencing the survival time after TIPS, and the directed edges

Table 2 Univariate survival analysis of patients having undergone transjugular intrahepatic portosystemic shunt surgery for portal hypertension


Post-PVP: Postoperative portal vein pressures; Na: Sodium; ALB: Albumin; AST: Aspartate aminotransferase; ALP: Alkaline phosphatase; TBIL: Total bilirubin; PA: Prealbumin; WBC: White blood cell count; MELD: Model for end-stage liver disease.
denote probabilistic dependencies among these factors. Percentages in the figure denote the prior probabilities of each node. For example, the prior probability of the survival, denoted as $P$ (survival time), was estimated to be $81.2 \%$. Within the BN framework, age, ascites, indications for TIPS, concurrent hypertension, post-PVP, the Child-Pugh grade, and the MELD score were the parent nodes directly linked to the survival time; the remaining variables are indirectly associated with the survival time.

# Model validation and assessment 

The BIC produced a score of -3589.04. Ten-fold cross-validation showed an average log-likelihood loss of 5.55 with a standard deviation of 0.16 . The model demonstrated an accuracy, precision, recall, and F1 score of $0.90,0.92,0.97$, and 0.95 , respectively, with an AUC value of 0.72 .

## Bayesian inference

BNs can infer unknown nodes based on known ones. In cases with moderate to severe ascites, the probability of refractory ascites as a TIPS indication increases to $26.40 \%$, the probability of PA levels being below $150 \mathrm{mg} / \mathrm{L}$ stands at $94.20 \%$, the likelihood of post-PVP exceeding $23.1 \mathrm{mmH}_{2} \mathrm{O}$ is at $82.1 \%$, the chance of having Child-Pugh grade C is $22.70 \%$, the probability of age being over 60 years is $33.7 \%$, and the 2 -year mortality rate is $28.30 \%$, as shown in Figure 4. In scenarios where patients have concurrent hypertension, are aged $\geq 60$ years, and present refractory ascites as a TIPS

![img-1.jpeg](img-1.jpeg)

Figure 2 Variable selection by least absolute shrinkage and selection operator regression. A: Dynamic graph of variable selection via the least absolute shrinkage and selection operator regression; B: Selection of optimal predictive variables through cross-validation method.
![img-2.jpeg](img-2.jpeg)

Figure 3 Bayesian network with 12 nodes and 17 directed edges. Nodes represent variables, and directed edges represent probabilistic dependence between connected nodes. The percentage in the figure represents the prior probability of each node. ALP: Alkaline phosphatase; AST: Aspartate aminotransferase; MELD: Model for end-stage liver disease; TBIL: Total bilirubin; TIPS: Transjugular intrahepatic portosystemic shunt; PA: Prealbumin; PVP: Portal vein pressures.

![img-3.jpeg](img-3.jpeg)

**Figure 4 Bayesian inference for patients with moderate-to-large ascites.** ALP: Alkaline phosphatase; AST: Aspartate aminotransferase; MELD: Model for end-stage liver disease; TBIL: Total bilirubin; TIPS: Transjugular intrahepatic portosystemic shunt; PA: Prealbumin; PVP: Portal vein pressures.

Indication, 82.50% of these patients are likely to experience moderate to severe ascites, 85.80% are likely to have PA levels below 150 mg/L, 80.10% are likely to have post-PVP exceeding 23.1 mmH₂O, and the 2-year mortality rate is predicted to increase to 49.60%, as shown in Figure 5. For patients aged 60 years or older with concurrent hypertension and TBIL levels exceeding 28 µmol/L, AST above 40 U/L, ALP greater than 135 U/L, and PA below 150 mg/L, there is a 76.40% probability of post-PVP exceeding 23.1 mmH₂O. In addition, these patients have a 44.20% likelihood of developing moderate-to-large ascites, a 36.50% chance of being classified as Child-Pugh grade C, an 8.42% probability of obtaining a high-risk MELD score, and a mortality rate that escalates to 52.40%, as detailed in Figure 6.

# DISCUSSION

PHT and its complications significantly impact the quality of life and prognosis of patients with cirrhosis[15]. Although TIPS is an essential therapeutic intervention that can effectively alleviate PHT-related symptoms, it can lead to postoperative complications that adversely affect patient survival. Consequently, developing an accurate prognostic prediction model is crucial for guiding clinical decision-making and enhancing patient management. Although studies like those by Huang *et al*[8], Sun *et al*[9], and Li *et al*[10] have focused on multiple prognostic factors, they have not comprehensively considered all relevant clinical variables and their interactions. For example, these studies did not thoroughly explore interrelations among factors like total TBIL, SCr, and sarcopenia and their collective impact on long-term patient survival. Conversely, our model is significantly more advantageous as it integrates complex prognostic factors and provides personalized predictions, thus capturing the multifaceted interactions of clinical variables. Our model not only covers a broader range of prognostic factors but also delves into their interactions and collective impact on long-term patient survival. In particular, our model reveals the dynamic changes and interdependencies among complex prognostic factors, an aspect not present in models like support vector machines, random forest algorithms, and nomograms. As an emerging modeling tool, BNs have shown significant potential in disease risk assessment and prognosis prediction[12]. This study marks the first application of BN methodology, which comprehensively considers various clinical variables and their relationships, provides more comprehensive and personalized prognostic information, and potentially improves treatment strategies and patient survival rates.

The study comprehensively assessed the biochemical markers of cirrhosis-induced PHT in patients, including liver function, renal function, coagulation status, and blood counts. It also considered various related variables, including ascites, PVP, concurrent diseases, and the etiology of cirrhosis. To select key determinants closely linked to post-TIPS survival, this study used a combination of Cox and LASSO regression methods, which facilitated the development of a model with improved explanatory power and enhanced predictive accuracy while concurrently minimizing the model's vulnerability to multicollinearity. The developed BN diagram illustrates the probabilistic dependencies among the post-TIPS survival time in patients with PHT and its predictive factors in a complex network. Various factors affect the post-TIPS survival time in patients with PHT *via* a network of complex interrelationships. This study's BN model revealed conditional dependencies among the variables of age, concurrent hypertension, ascites, indications for TIPS, post-PVP, the Child-Pugh grade, and the MELD score, which serve as parent nodes for the survival time and directly influence the overall survival of the patient. Age, functioning as a parent node, not only directly impacts the survival time but also indirectly influences it through its effect on the incidence of hypertension and ascites. The PA level, which is another parent node, is directly correlated with the ascites condition. Ascites is also a parent node, and it directly influences the survival time and additionally impacts it indirectly through the Child-Pugh grade, indications for TIPS, and post-PVP. AST and ALP, which are parent nodes for TBIL, directly influence its levels. TBIL is a parent node for the Child-Pugh grade and MELD score and indirectly impacts the survival time. An explanation of the reasons and mechanisms behind these interconnections is provided below.

![img-4.jpeg](img-4.jpeg)

Figure 5 Bayesian inference for patients aged ≥ 60 years with hypertension and refractory ascites as transjugular intrahepatic portosystemic shunt indications. ALP: Alkaline phosphatase; AST: Aspartate aminotransferase; MELD: Model for end-stage liver disease; TBIL: Total bilirubin; TIPS: Transjugular intrahepatic portosystemic shunt; PA: Prealbumin; PVP: Portal vein pressures.

![img-5.jpeg](img-5.jpeg)

Figure 6 Bayesian inference for patients aged ≥ 60 years with hypertension, alkaline phosphatase > 135 U/L, aspartate aminotransferase > 40 U/L, and prealbumin < 150 mg/L. ALP: Alkaline phosphatase; AST: Aspartate aminotransferase; MELD: Model for end-stage liver disease; TBIL: Total bilirubin; TIPS: Transjugular intrahepatic portosystemic shunt; PA: Prealbumin; PVP: Portal vein pressures.

With aging, patients often experience a decline in physiological functions and liver functional reserve, potentially leading to reduced surgical tolerance in older individuals and subsequently heightened surgical risks. Moreover, aging plays a critical role in the development of hypertension; the TIPS procedure modifies hepatic and portal vein hemodynamics, and the presence of hypertension can exacerbate cardiovascular strain, thus increasing postoperative risks and affecting patient survival prognosis[16]. In addition, aging may accompany alterations in other systems, such as drug metabolism and excretion, thus elevating the risk of ascites[17]. Ascites, often seen in advanced cirrhosis, is a marker of progression to a more severe liver disease stage and is closely associated with the survival time[18,19]. PA, which is synthesized by the liver and has a short half-life, is a sensitive indicator of both recent nutritional status and liver function[17]. Lower PA levels indicate reduced hepatic synthesis, suggesting a poor prognosis. When hepatic synthesis is impaired, the decrease in the level of PA may lead to a reduction in plasma colloid osmotic pressure, thus triggering or exacerbating ascites. Therefore, reduced PA levels play an important role in ascites development. In addition, ascites commonly occurs in patients with cirrhosis-induced PHT, with its severity closely linked to PVP. Although TIPS aims to reduce elevated PVP and alleviate ascites, the extent and severity of ascites indirectly affect post-PVP management. Increased post-PVP can increase the risk of postoperative complications like rebleeding, thus impacting patient survival prognosis[20,21]. Variceal bleeding and refractory ascites serve as primary indications for TIPS. Ascites influences the decision-making for TIPS, with refractory ascites indicating advanced-stage cirrhosis and poor prognosis[22]. AST and ALP, which are critical markers of liver function, signify liver cell damage or biliary obstruction when elevated[23,24], thus directly affecting bilirubin metabolism and leading to increased TBIL levels. TBIL levels, which reflect liver detoxification and excretion functions, play an important role in liver function assessments, such as the Child-Pugh grade and MELD score. Elevated TBIL levels imply diminished hepatic ability to process bilirubin, indicating advanced cirrhosis severity[25]. The Child-Pugh grade and MELD score are essential for assessing cirrhosis severity and prognosis[26,27]. These scores offer a comprehensive analysis of cirrhosis severity and survival prognosis by integrating various

parameters, including TBIL. Higher TBIL levels can lead to increased Child-Pugh grade and MELD score, signifying severe liver impairment and a worse prognosis, which could reduce the survival time. The study used a BN model to analyze factors affecting post-TIPS survival in patients with PHT; consequently, it uncovered various relationships, some of which are corroborated by existing research and others that require further validation. In the future, we will conduct prospective studies to more comprehensively validate these interrelationships.

In this study, we successfully developed and validated a BN-based model for accurately predicting post-TIPS survival outcomes in patients with PHT. The model demonstrated excellent performance, as evidenced by a BIC score of -3589.04, reflecting its high data fitting efficiency. Additionally, the model's robustness and reliability are corroborated by an average log-likelihood loss of 5.55 and a standard deviation of 0.16 from 10-fold cross-validation. Although the model demonstrates excellence in accuracy, precision, recall, and F1 score, an AUC value of 0.72 indicates potential for further enhancing its sensitivity and specificity in survival prognosis. Future efforts will aim to enhance the model's predictive power by expanding the training dataset, adjusting parameters, and optimizing the network structure. This study's focus on conditional probability inference highlights the BN's capacity to deduce unknown nodes from known ones, offering clinicians a powerful tool for precise patient health prediction and management. For example, the model can project risks of related health issues by analyzing existing patient clinical data, such as ascites severity and post-PVP changes. This accurate risk assessment enables more comprehensive evaluation of patient health by medical professionals, resulting in personalized treatment strategies. This approach is crucial for high-risk patients, allowing for proactive measures and strategic treatment adjustments to reduce specific complication risks. In addition, employing Bayesian inference strengthens the data-driven basis of clinical decision-making. Understanding these probabilistic dependencies empowers medical personnel to make more informed decisions during diagnosis and treatment. In particular, in predicting the postTIPS survival time, factors like the Child-Pugh grade and MELD score may significantly influence patient survival under certain conditions. This understanding of conditional dependencies helps medical staff integrate long-term health forecasts into treatment plans and improves patient communication, thus enhancing their understanding and engagement.

This study has certain limitations. First, as a single-center retrospective study with a limited sample size, the stability and generalizability of its predictions need to be further validated by larger, multi-center prospective studies. Second, certain potential risk factors, such as portal vein diameter and sarcopenia, which were identified to impact the prognosis of patients having undergone TIPS surgery for PHT in other studies were not incorporated in this study. In addition, although the BN model's predictive accuracy is good enough to provide some useful insights, an AUC value of less than 0.8 suggests that there is room for improvement in its predictive capacity. Our future goal is to conduct multi-center studies with larger sample sizes, extended follow-up periods, and additional parameters to enhance the BN model for more accurate prediction of survival prognosis in patients having undergone TIPS surgery for PHT.

# CONCLUSION 

In summary, this study signifies the first application of BN methodology in developing a survival prediction model for patients having undergone TIPS surgery for PHT. By incorporating numerous clinical variables, the model exposes the intricate conditional dependencies among these variables, showcasing its outstanding data fitting capabilities. It contributes to significantly enhancing the precision of survival prognosis for patients having undergone TIPS surgery for PHT while providing new analytical tools and strategies for patient evaluation, treatment planning, and disease management. Moreover, this study fills a critical gap in existing research by thoroughly exploring the interrelationships among various prognostic factors and their collective impact on patient outcomes, thus offering novel insights into the complex dynamics of PHT and its management after TIPS. Through this study, we aim to offer superior medical services to patients with PHT, ultimately improving their quality of life and survival rates. Finally, the application of BN in this study extends beyond mere survival outcome predictions, and it opens new perspectives and research directions for future clinical studies. Continuing this line of research will allow us to gain a deeper understanding of the risk factors associated with post-TIPS complications and their impact on patient outcomes, thus enabling the development of more scientific and effective treatment and management strategies for patients with PHT.

## ARTICLE HIGHLIGHTS

## Research background

Portal hypertension (PHT) secondary to cirrhosis leads to severe symptoms, exacerbating disease progression and adversely affecting survival rates. Transjugular intrahepatic portosystemic shunt (TIPS) is pivotal in managing PHT; however, its resultant complications can significantly impact patient prognosis. A thorough understanding of the interplay and mechanisms of various prognostic factors is crucial for enhancing treatment strategies and improving patient survival.

## Research motivation

There is a gap in existing research concerning the comprehensive exploration of the interrelationships and mechanisms of prognostic factors in PHT. We believe there is an urgent requirement for advanced modeling approaches to intricately analyze these interactions.

# Research objectives 

To use Bayesian network (BN) methodology for extensive analysis of factors influencing the prognosis of PHT patients after TIPS. The objective involves elucidating the interdependencies among these factors and developing a BN model to predict patient survival after TIPS, thus facilitating informed clinical decisions.

## Research methods

In this study, we included 393 patients and used Cox and least absolute shrinkage and selection operator regression to select variables most relevant to prognosis, and we established a new BN survival prediction model for patients having undergone TIPS surgery for PHT.

## Research results

We successfully developed a BN-based survival prediction model with good predictive capabilities. Key factors impacting survival were identified, and the model showed high accuracy, precision, recall, and F1 score, with an AUC of 0.72 , indicating its efficacy in survival prediction after TIPS in patients with PHT.

## Research conclusions

We developed a novel BN-based model for predicting survival in patients having undergone TIPS surgery for PHT. This model enhances the precision of survival prognosis and provides new analytical tools for patient evaluation, treatment planning, and disease management.

## Research perspectives

Data from other centers are essential for further validating the clinical usability of this novel model. Concurrently, continued research is imperative to deepen the understanding of post-TIPS complication risk factors and their impact on patient outcomes, thus guiding the development of more effective and scientific treatment strategies for patients with PHT.

## FOOTNOTES

Author contributions: Chen R designed the research, collected and organized the data, and wrote the initial draft of the manuscript; Zhang YZ guided the research design; Liu Z, Liu AL, and Zhang YW were involved in data collection and analysis; and Luo L managed the project and participated in the manuscript's review and editing; and all authors have read and approved the final version of the manuscript for publication.

Supported by the Chinese Nursing Association, No. ZHKY202111; Scientific Research Program of School of Nursing, Chongqing Medical University, No. 20230307; and Chongqing Science and Health Joint Medical Research Program, No. 2024MSXM063.

Institutional review board statement: This study was reviewed and approved by the Ethical Review Committee of the Second Affiliated Hospital of Chongqing Medical University (Approval No. 005, 2023).

Informed consent statement: Informed consent was waived due to the retrospective cohort design of this study. For privacy reasons, patients' identifying information was replaced with codes before data extraction.

Conflict-of-interest statement: Authors declare no conflict of interest for this article.
Data sharing statement: The datasets used and/or analyzed during the current study are available from the corresponding author upon reasonable request.

STROBE statement: The authors have read the STROBE Statement-checklist of items, and the manuscript was prepared and revised according to the STROBE Statement-checklist of items.

Open-Access: This article is an open-access article that was selected by an in-house editor and fully peer-reviewed by external reviewers. It is distributed in accordance with the Creative Commons Attribution NonCommercial (CC BY-NC 4.0) license, which permits others to distribute, remix, adapt, build upon this work non-commercially, and license their derivative works on different terms, provided the original work is properly cited and the use is non-commercial. See: https:// creativecommons.org/Licenses/by-nc/4.0/

Country/Territory of origin: China
ORCID number: Ling Luo 0009-0000-6855-7858.
S-Editor: Chen YL
L-Editor: A
P-Editor: Guo X
