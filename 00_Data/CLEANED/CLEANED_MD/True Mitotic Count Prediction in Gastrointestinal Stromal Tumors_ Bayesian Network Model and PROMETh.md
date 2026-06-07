# True Mitotic Count Prediction in Gastrointestinal Stromal Tumors (GIST): Bayesian Network Model and PROMETheus (PReOperative Mitosis Estimator Tool) App development. 

Salvatore Lorenzo Renne, Manuela Cammelli, Ilaria Santori, Marta TassanMangina, Laura Samà, Laura Ruspi, Federico Sicoli, Piergiuseppe Colombo, Luigi<br>Maria Terracciano, Vittorio Quagliuolo, Ferdinando Carlo Maria Cananzi

Submitted to: Journal of Medical Internet Research on: June 16, 2023

Disclaimer: (C) The authors. All rights reserved. This is a privileged document currently under peer-review/community review. Authors have provided JMIR Publications with an exclusive license to publish this preprint on it's website for review purposes only. While the final peer-reviewed paper may be licensed under a CC BY license on publication, at this stage authors and publisher expressively prohibit redistribution of this draft paper other than for review purposes.

# Table of Contents 

Original Manuscript ..... 5
Supplementary Files ..... 26
Figures ..... 27
Figure 1 ..... 28
Figure 2 ..... 29
Figure 3 ..... 30
Figure 4 ..... 31
Figure 5 ..... 32
Figure 6 ..... 33
Multimedia Appendixes ..... 34
Multimedia Appendix 0 ..... 35
Multimedia Appendix 0 ..... 35
Multimedia Appendix 1 ..... 35
Multimedia Appendix 2 ..... 35
Multimedia Appendix 3 ..... 35
Multimedia Appendix 4 ..... 35
Multimedia Appendix 5 ..... 35
Multimedia Appendix 6 ..... 35
Multimedia Appendix 7 ..... 35
Multimedia Appendix 8 ..... 35

# True Mitotic Count Prediction in Gastrointestinal Stromal Tumors (GIST): Bayesian Network Model and PROMETheus (PReOperative Mitosis Estimator Tool) App development. 

Salvatore Lorenzo Renne ${ }^{1,2}$ MD; Manuela Cammelli ${ }^{3 *}$ MD; Ilaria Santori ${ }^{3}$ MD; Marta Tassan-Mangina ${ }^{3}$ MD; Laura Samà ${ }^{4}$ MD; Laura Ruspi ${ }^{4}$ MD; Federico Sicoli ${ }^{4}$ MD; Piergiuseppe Colombo ${ }^{5}$ MD; Luigi Maria Terracciano ${ }^{5}$ MD; Vittorio Quagliuolo ${ }^{4}$ MD; Ferdinando Carlo Maria Cananzi ${ }^{4,3^{*}}$ MD

[^0]
## Abstract

${ }^{1}$ Department of Biomedical Sciences, Humanitas University Pieve Emanuele, Milan IT
${ }^{2}$ Pathology Department, IRCCS Humanitas Research Hospital Rozzano, Milan IT
${ }^{3}$ Pathology Department, IRCCS Humanitas Research Hospital via Manzoni 56, 20089 Rozzano, Milan IT
${ }^{4}$ Sarcoma, Melanoma and Rare Tumors Surgery Unit, IRCCS Humanitas Research Hospital via Manzoni 56, 20089 Rozzano, Milan IT ${ }^{5}$ Department of Biomedical Sciences, Humanitas University Via Rita Levi Montalcini 4, 20072 Pieve Emanuele, Milan IT ${ }^{7}$ these authors contributed equally


## Corresponding Author:

Salvatore Lorenzo Renne MD
Department of Biomedical Sciences, Humanitas University
Via Rita Levi Montalcini 4
Pieve Emanuele, Milan
IT

## Abstract

Background: Gastrointestinal Stromal Tumors (GISTs) present a complex clinical landscape, where precise preoperative risk assessment plays a pivotal role in guiding therapeutic decisions. Conventional methods for evaluating mitotic count, such as biopsy-based assessments, encounter challenges stemming from tumor heterogeneity and sampling biases, thereby underscoring the urgent need for innovative approaches to enhance prognostic accuracy.

Objective: The primary objective of this study was to develop a robust and reliable computational tool, PROMETheus, aimed at refining patient stratification through precise estimation of mitotic count in GISTs.

Methods: Leveraging advanced Bayesian Network methodologies, we constructed a Directed Acyclic Graph (DAG) integrating pertinent clinico-pathological variables essential for accurate mitotic count prediction on the surgical specimen. Key parameters identified and incorporated into the model encompassed tumor size, location, mitotic count from biopsy specimens, surface area evaluated during biopsy, and tumor response to therapy, when applicable. Rigorous testing procedures, including prior predictive simulations, validation utilizing synthetic datasets were employed. Finall, the model was trained on a comprehensive cohort of real-world GIST cases ( $\mathrm{n}=80$ ), drawn from the repository of IRCCS Humanitas Research Hospital, totaling 160 cases, were conducted.

Results: Our computational model exhibited excellent diagnostic performance on syntetic data, different model architecture were selected based on lower deviance and robust out-of-sample predictive capabilities. Posterior predictive checks (retrodiction) further corroborated the model's accuracy. Subsequently, the development of PROMETheus, an intuitive application dynamically computing predicted mitotic count and risk assessement on surgical specimens based on tumor-specific attributes, including size, location, surface area, and biopsy-derived mitotic count, using posterior probabilities derived from the model, was successfully achieved.

Conclusions: The deployment of PROMETheus might herald a significant advancement in preoperative risk stratification for GISTs, offering clinicians a precise and reliable means to anticipate mitotic counts on surgical specimens and a solid base to stratify patients for clinical studies. By facilitating tailored therapeutic strategies, this innovative tool is poised to revolutionize clinical decision-making paradigms, ultimately translating into improved patient outcomes and enhanced prognostic precision in the management of GISTs.
(JMIR Preprints 16/06/2023:50023)


[^0]:    ${ }^{1}$ Department of Biomedical Sciences, Humanitas University Pieve Emanuele, Milan IT
    ${ }^{2}$ Pathology Department, IRCCS Humanitas Research Hospital Rozzano, Milan IT
    ${ }^{3}$ Pathology Department, IRCCS Humanitas Research Hospital via Manzoni 56, 20089 Rozzano, Milan IT
    ${ }^{4}$ Sarcoma, Melanoma and Rare Tumors Surgery Unit, IRCCS Humanitas Research Hospital via Manzoni 56, 20089 Rozzano, Milan IT
    ${ }^{5}$ Department of Biomedical Sciences, Humanitas University Via Rita Levi Montalcini 4, 20072 Pieve Emanuele, Milan IT
    ${ }^{7}$ these authors contributed equally

DOI: https://doi.org/10.2196/preprints. 50023

# Preprint Settings 

1) Would you like to publish your submitted manuscript as preprint?
$\checkmark$ Please make my preprint PDF available to anyone at any time (recommended).
Please make my preprint PDF available only to logged-in users; I understand that my title and abstract will remain visible to all users. Only make the preprint title and abstract visible.
No, I do not wish to publish my submitted manuscript as a preprint.
2) If accepted for publication in a JMIR journal, would you like the PDF to be visible to the public?
$\checkmark$ Yes, please make my accepted manuscript PDF available to anyone at any time (Recommended).
Yes, but please make my accepted manuscript PDF available only to logged-in users; I understand that the title and abstract will remain visible.
Yes, but only make the title and abstract visible (see Important note, above). I understand that if I later pay to participate in <a href="http://

# Original Manuscript

# True Mitotic Count Prediction in Gastrointestinal Stromal Tumors (GIST): Bayesian Network Model and PROMETheus (PReOperative Mitosis Estimator Tool) App developement. 

Salvatore Lorenzo Renne ${ }^{1}$<br>Manuela Cammelli ${ }^{2}$<br>Ilaria Santori<br>Marta Tassan-Mangina<br>Laura Ruspi<br>Federico Sicoli<br>Laura Samà<br>Piergiuseppe Colombo<br>Luigi Maria Terracciano<br>Vittorio Quagliuolo<br>Ferdinando Carlo Maria Cananzi ${ }^{3}$<br>2024-05-13

[^0]
[^0]:    ${ }^{1}$ Corresponding author
    ${ }^{2}$ Co-first author
    ${ }^{3}$ Co-corresponding author

Background: Gastrointestinal Stromal Tumors (GISTs) present a complex clinical landscape, where precise preoperative risk assessment plays a pivotal role in guiding therapeutic decisions. Conventional methods for evaluating mitotic count, such as biopsy-based assessments, encounter challenges stemming from tumor heterogeneity and sampling biases, thereby underscoring the urgent need for innovative approaches to enhance prognostic accuracy. Objective: The primary objective of this study was to develop a robust and reliable computational tool, PROMETheus, aimed at refining patient stratification through precise estimation of mitotic count in GISTs. Methods: Leveraging advanced Bayesian Network methodologies, we constructed a Directed Acyclic Graph (DAG) integrating pertinent clinico-pathological variables essential for accurate mitotic count prediction on the surgical specimen. Key parameters identified and incorporated into the model encompassed tumor size, location, mitotic count from biopsy specimens, surface area evaluated during biopsy, and tumor response to therapy, when applicable. Rigorous testing procedures, including prior predictive simulations, validation utilizing synthetic datasets were employed. Finall, the model was trained on a comprehensive cohort of realworld GIST cases ( $\mathrm{n}=80$ ), drawn from the repository of IRCCS Humanitas Research Hospital, totaling 160 cases, were conducted. Results: Our computational model exhibited excellent diagnostic performance on syntetic data, different model architecture were selected based on lower deviance and robust out-of-sample predictive capabilities. Posterior predictive checks (retrodiction) further corroborated the model's accuracy. Subsequently, the development of PROMETheus, an intuitive application dynamically computing predicted mitotic count and risk assessement on surgical specimens based on tumor-specific attributes, including size, location, surface area, and biopsy-derived mitotic count, using posterior probabilities derived from the model, was successfully achieved. Conclusions: The deployment of PROMETheus represents a potential advancement in preoperative risk stratification for GISTs, offering clinicians a precise and reliable means to anticipate mitotic counts on surgical specimens and a solid base to stratify patients for clinical studies. By facilitating tailored therapeutic strategies, this innovative tool is poised to revolutionize clinical decision-making paradigms, ultimately translating into improved patient outcomes and enhanced prognostic precision in the management of GISTs.

# Introduction 

Gastrointestinal Stromal Tumor (GIST) is the most common sarcoma type [1]. The majority harbors activating mutation in KIT or PDGFRA [2-5]. Even if these mutations represent early events in carcinogenesis - being shared by clinically irrelevant and very aggressive GIST [6,7] - they are the molecular basis for the very active tyrosine-kinase-inhibitor (TKI) therapy [8-10]. TKI revolutionized GIST treatment and they have been used in all the disease stages since their introduction [11-14]. Notably, they can be administered as neoadjuvant treatment for patients with high-risk disease or to reduce the extent of the surgery in GIST in peculiar location (i.e. rectum and duodenum) [14-17]. Even if neo-adjuvant therapy with Imatinib is beneficial in patients with high risk disease [18], and in patients that will have not an R0 surgery or patients that can have a less mutilating, function-sparing surgery if there is a volumetric reduction [17], TKI has some issues: on the one hand it is likely to impair a correct - post operative - risk assessment: indeed if the tumor responds to therapy it will be not possible to correctly asses the risk [5]. Several risk assessments in GIST have been developed and they identify size, site and mitotic count as important features [19-21]. Indeed, mitotic count on the surgical specimen after TKI therapy can be greatly modified - especially in the case of tumor response - therefore in these patients the subsequent management will be guided by a risk assessment computed with the mitotic count from the biopsy, and this - we will see - can lead to mistreatment.

On the other hand, during initial patient management, identification of the high-risk patients can also fail: a very small amount of tissue on biopsy is required to make the diagnosis of GIST, since very good immunohistochemical markers (rather specific and sensitive) exist [22-25]. Therefore, whereas size and site can be accurately assessed by imaging, mitotic count on biopsy can be burdened by several limitations: some purely biological - such as tumor heterogeneity -, others more physical, i.e. the size of the specimen available

for counting (a classic example of sampling bias) [26-30]. Thus, it may happen to incorrectly classify the risk of a GIST preoperatively, and this might lead to surprises after the mitotic count on the surgical specimen is performed, often due to underestimation of the mitotic count [31-33].

These limitations underscore the critical need for innovative approaches to refine preoperative risk stratification in GIST, aiming to mitigate the risks of misclassification and subsequent therapeutic mismanagement. The discrepancies between preoperative risk assessments and postoperative findings underscore the imperative for precision tools that can dynamically estimate mitotic count on surgical specimens, enhancing the accuracy of patient stratification and treatment planning.

In line with this imperative, we aim to develop an advanced computational tool, termed PROMETheus, designed to predict mitotic count on surgical specimens. By leveraging state-of-the-art Bayesian modeling techniques and integrating comprehensive clinico-pathological variables, PROMETheus seeks to address the limitations of current risk assessment methodologies, offering clinicians a reliable means to anticipate postoperative mitotic counts and refine preoperative treatment strategies effectively.

# Materials and methods 

## Modeling strategy

Bayesian network and workflow. As modeling strategy we used Bayesian network with the aim of predicting the mitotic count on the surgical specimen. Of note, we use the term Bayesian network to indicate the graphical representation of the model and the collection of functions necessary to use it for statistical learning. This looser definition is often used in practice, however it's broader than the one indented by the term's inventor, Judea Pearl. In its Causality (2009) he basically identifies the directed acyclic graphs (DAGs, see main text) with the term Bayesian networks (BN): "Directed graphs, especially DAGs, have been used to represent causal or temporal relationships [...] and came to be known as Bayesian networks, a term coined [...] to emphasize three aspects: (1) the subjective nature of the input information; (2) the reliance on Bayes's conditioning as the basis for updating information; and (3) the distinction between causal and evidential modes of reasoning ..." - see p. 14 of the cited reference [34]. In the present paper, the meaning of BN is closer to the one of structural causal models (SCMs) [35]. Briefly, we designed a SCM of the variables, created a mock data-set, wrote a probabilistic program, validated it on the data simulation, fit the model to the data, and compared multiple models with different structures; these procedures are often collectively referred as the Bayesian workflow [36-39]. Causal modeling. The graphical representation of the Bayesian network was done with Directed Acyclic Graphs (DAG): the variables were represented by nodes and the conditional dependencies through directed edges. Based on the graphical representation we built a Structural Causal Model (SCM), that we used for data simulation and as the model for the fits. Probabilistic programming. We wrote and fit the models using R version 4.1.2 and Stan version 2.21.0 [40-43]. Stan is a probabilistic programming language that runs a No U-Turn sampler, an extension to Hamiltonian Monte Carlo (HMC)

sampling, which is itself a form of Markov Chain Monte Carlo (MCMC) [44]. To promote regularization and reduce overfitting, we used multilevel-hierarchical modeling strategy [39,45,46]. Distributions (likelihood and priors) were chosen with maximum entropy criteria [39]. To understand priors' implications, we run prior predictive simulations [37,38,46]. To minimize divergent transitions, we reparametrized the models with a non-centered equivalent form when appropriated [39,47]. To ensure a good representation of the sample space, we visually inspected the chains with traceplots and trankplots [48]. We then monitored the chains with post-modeling diagnostics such as the number of effective samples and the Gelman-Rubin convergence diagnostic $\hat{R}$ [45,48]. Of note, $\hat{R}$ as defined in the cited references is different from the classic definition by Gelman and Rubin (1992). All models' fits were plotted against the fitted data to ensure a good representation of the outcome space (posterior predictive check) [39,49,50]. Compatibility intervals (CIs) were calculated as Highest Posterior Density Interval (HDPI) [51]. Model selection. For the aim of pure prediction - as in our case - the best model can be selected based on information theory estimating model performance through Widely Applicable Information Criteria (WAIC, a generalization of Akaike information criteria) and Pareto Smooth Important Sampling Leave-One-Out Cross-Validation Criteria (PSIS-LOO-CV) [52-54]. We checked that the two statistics gave the same results to trust their results [39,55,56]. We selected the model with the lowest deviance in out of sample performance. Forecasting. The posterior probability density of the coefficients was then used to create an application that, given the chosen variables, computed the posterior probability distribution in the outcome space (i.e. the mitotic count on the specimen). Moreover, we programmed the app to calculate the risk class from this computed posterior distribution of the mitotic count.

# Study population 

Dataset. The cases came from a prospectively maintained database including all the patients who underwent surgery for primary sarcoma in IRCCS Humanitas Research Hospital (Rozzano (MI), Italy). This database comprises extended clinical and pathological information and contained 233 GISTs operated from January 2000 to March 2022. Inclusion Criteria. We included patients with pre-operative diagnostic biopsy, that underwent surgical resection, with informed consent to research and available histologic material of the biopsy and the surgical specimen. Exclusion criteria. Histology was reviewed by a sarcoma pathologist (SLR) and cases with diagnosis other than GIST were excluded.

## Pathology

Microscope calibration. We calibrated the microscope with a stage micrometer slide and calculated the number of high power fields (HPFs) needed to reach the size of $5 \mathrm{~mm}^{2}$ and - in line with published guidelines - the number of HPFs to evaluate was 23.5 [30,57-59]. Mitosis. We defined a mitosis as basophilic, dark, hairy material representing the chromosomes. A mitosis was counted when the chromosomes were either clotted (as in the beginning of metaphase), in a plane (as in metaphase and anaphase), or in separate clots (as in telophase), as previously described[60]. Biopsy measurement. We measured the surface available under the microscope counting HPFs filled by neoplastic

specimen up to $5 \mathrm{~mm}^{2}$; for very small biopsies we approximated the surface as fraction of a field of view. Tumor response. Some of the cases of the series underwent preoperative therapy. To use this cases without polluting the estimate for mitotic count coefficient, we also recorded the response to treatment; this had a different meaning from a classical pathological response and was defined as follows: if a mitotically active area was identified on the surgical specimen (regardless of the size) and the mitotic count in this area was equal to or more than the biopsy count the tumor was classified as no response. Therefore this mitotic count on the biopsy was used in the model as if the case did not undergo preoperative therapy. Conversely, if the count on the surgical specimen was less then the count on the biopsy, the tumor was classified as response and the count was used to estimate a different coefficient that we did not use for prediction (see model description in the result section and custom code for greater detail).

# Ethical Considerations 

Patients signed an institutional written informed consent to research. According to European regulation (UE2016/679) and Italian Privacy Code (D.Lgs.101/2018) retropective observational monocentric study do not require specific informed consent. Data were de-identified prior to analysis.

## Results

## Causal modeling

![img-0.jpeg](img-0.jpeg)

Figure 1: To determine the model covariates, we utilized a Directed Acyclic Graph (DAG). In this causal framework, several factors influence the mitotic count on the surgical specimen. Firstly, the dimension of the tumor impacts both the mitotic count on the biopsy and the surgical specimen. Larger tumors tend to exhibit higher mitotic activity. Secondly, the location of the tumor plays a crucial role in its growth pattern. For instance, gastric neoplasms often have more space to expand, leading to the development of symptoms with larger masses. Additionally, tumor location influences the accessibility of the biopsy site, as some sites are inherently more accessible than others. Lastly, the amount of surface area available on the biopsy directly impacts the accuracy of the mitotic count estimation. A larger surface area allows for more representative sampling of the tumor. This simplified causal model elucidates the relationship between various factors affecting GIST mitotic count. Please refer to the main text and supplementary materials for further details. In the model notation, $D$ represents the dimension of the tumor, $L$ denotes the location, $M_{R}$ signifies the mitotic count on the biopsy, $M_{S}$ indicates the mitotic count on the surgical specimen, and $S$ represents the surface area of the biopsy.

We designed a causal model to identify the covariates to be include in the model for estimating the mitotic count on the surgical specimen. We assumed that the true mitotic count is the one counted on the surgical specimen $\left(M_{S}\right)$. The more tumor cell replicates, the bigger the tumor is $(D)$. We also identified the anatomical location $(L)$ as a cause of tumor dimension $(D)$ in the sense that in certain locations the symptoms would appear earlier thus influencing the measured size at diagnosis. Moreover, location directly causes the total amount of tissue available for evaluation at biopsy (i.e. the measured biopsy surface, $S$ ): some sites are more difficult to reach than others. Lastly, mitotic count on the biopsy $\left(M_{B}\right)$ reflects the mitotic count on the surgical specimen $\left(M_{S}\right)$ and due to tumor heterogeneity and sampling bias the measurement on the biopsy also depends on the surface examined (S) (Figure 1 and also figure 8 for an extended version of the DAG).

# Probabilistic modeling 

Our inferential target was the mitotic count on the surgical specimen $\left(M_{S}\right)$; as the name suggests it is a count variable and we therefore chose a Poisson distribution to model it (Equation (1)).Poisson distributions have just one parameter, $\lambda$. It is the expected value and the expected variance of the count variable and it is the parameter used for the generalized linear model. It needs to be positive, and a common link function is to exponentiate the model. Given each patient $i$, we estimated a coefficient for the tumor dimension $(\beta)$ and for surface of the biopsy $(\gamma)$ for each location $(L)$ using a multilevel-hierarchical model for both of them ( $\beta_{i L}: D_{i}$ and $Y_{i L}: S_{i}$ respectively); the parameters $\delta$ and $\epsilon$ were alternatively switched on and off by the presence of response to therapy $R$, as defined in the methods section; and finally we set an intercept $\alpha$ (Equation (2)). To justify prior choice we used prior predictive simulation.


# Prior predictive simulation 

Prior predictive simulation
![img-1.jpeg](img-1.jpeg)

Figure 2: Prior predictive simulation of the $\lambda$ parameter, i.e., what the model anticipates before encountering the data. This plot displays 80 simulated cases derived from the priors. The majority of expected values indicate a very low mitotic count, aligning with real-world expectations. However, the model is not startled by higher mitotic counts, even though it anticipates encountering them in a minority of cases without prior training.
The majority of GISTs are clinically irrelevant, with a mitotic count less than $5 / 5 \mathrm{~mm}^{2}$. Few of them can have an higher mitotic count, even to a greater order of magnitude, however it is biologically implausible to expect many cases with mitotic count greater than 50 . Using this field specific knowledge, we chose normal distributions for model coefficients (Equations (3), (5), (4), (7), (8), (10), (11)) and exponential distributions for scalar coefficients (Equations (6), (9)). Through serial simulations we narrowed the numerical values. For a graphical representation of part of the coefficients see figure 9. The results of the prior predictive simulation show that the most of the simulated $\lambda$ have indeed values in keeping with the field specific knowledge (Figure 2).

# Fitting the mock data-set 

![img-2.jpeg](img-2.jpeg)

Figure 3: Posterior predictive simulation. The upper panel shows the imputed $\lambda$ parameter for each sample against the ground-truth; consider the logarithmic scale on the y-axis. The lower panel shows the same imputed $\lambda$ parameter against the fitted data. On average the mitotic count either on the surgical specimen or on the biopsy is lower than the expected value, this is due to the asymmetry of the Poisson distribution. The size of the $X$ is proportional to the biopsy surface, the size of the empty dots is proportional to the tumor size; the color of the background corresponds to the tumor site.
To test the model performance, we fitted it on a simulated data-set of 100 cases. The custom code to produce the mock data-set is available on the cited repository. The fit with a centered parameterization resulted in $2 \%$ of divergent transitions, we therefore rewrote the model in a non-centered form. Fit's diagnostics were satisfactory: $\hat{R}=1.00$ was obtained for all the parameters, the energy from the Hamiltonian had a Gaussian outlook and the trankplots of the log-probability showed a satisfactory convergence of the chains (Figure 10); all the parameters had a satisfactory number of effective samples and a good outlook of the trankplots (Figure 11); the posterior probability density for each coefficient is depicted in figure 12. To check the fitness of the model, we compared the inferred $\lambda$ by the model to the true $\lambda$ used for data simulation. This procedure revealed that the model regularized the values within each modeled site and was able to recover a value closer to $\lambda$ even if provided with lower values (Figures 3).

# Fitting the real data-set 

![img-3.jpeg](img-3.jpeg)

Figure 4: Posterior predictive simulation on the true dataset. The size of the $X$ is proportional to the biopsy surface, the size of the empty dots is proportional to the tumor size; the color of the background corresponds to the tumor site.
We hence fitted the model to the real data. We were able to fit it with the centered version of the model. Similarly to the simulated dataset, fit's diagnostics were satisfactory: $\hat{R}=1.00$ was obtained for all the parameters, the energy from the Hamiltonian had a Gaussian outlook and the trankplots of the log-probability showed a satisfactory convergence of the chains (Figure 13); moreover, all the parameters had a satisfactory number of effective samples and a good outlook of the trankplots (Figure 14); the posterior probability density for model coefficient is depicted in figure 15 and table 1 . The site ( $\downarrow$ ) was an index variable with values from 1 to 4 , representing coefficients for colon-rectum, duodenum, small-intestine and stomach, respectively. Of note the model posterior distribution for the biopsy count parameter $(\delta)$ is 1 , consistently with our expectations. As in the data simulation, in order to see what the model learnt, we moved to form the parameter space to the outcome space and simulated from the whole posterior distribution a $\lambda$ parameter - that tells us the expected value of the Poisson distribution - for each case and plotted it against the data fitted. This posterior predictive simulation is depicted in figure 4.

Table 1: Coefficients



# Model selection 

In general, adding parameters in multilevel modeling reduces overfitting and improves out-of-sample performance, whereas adding parameters without a hierarchical structure can reduce deviance within sample, but results in a lower out-of-sample performance (i.e. increases overfitting). We therefore computed the deviance using WAIC and PSIS-LOO-CVC on our model (that had a multilevel - hierarchical - structure for the tumor size $\beta_{1}$ and biopsy surface $\gamma_{1}$ parameters) and for alternative models having also the mitotic count on the biopsy with a hierarchical structure (see Equation (12)), only tumor size with a hierarchical structure (see Equation (13)), only tumor size and without accounting for biopsy surface (see Equation (14)), and no hierarchical structure without accounting for tumor size (see Equation (15)). The model with hierarchical structure for tumor size and biopsy surface parameters (Equation (2)) had the lowest out-of-sample deviance (Figure 5). We therefore chose the model with hierarchical structure for the tumor size and biopsy surface parameters for the App development.
![img-4.jpeg](img-4.jpeg)

Figure 5: Model Selection. The vertical line indicates the mean deviance of the reference model (the one with the lowest out of sample deviance). The filled dots are values within the sample. The empty dots represent mean the out of sample deviance with the bar indicating the $89 \% \mathrm{Cl}$; the triangle is the contrast between the model and the reference model.

# Application 

Using the posterior probabilities from the model, we developed PROMETheus (PReOperative Mitosis Estimator Tool), a web-based application freely available at https://slrenne.shinyapps.io/PROMETheus/. The user interface has an input panel to insert the tumor location, the tumor size, the mitotic count on the biopsy, and the available surface on the biopsy. Then the app dynamically computes the risk class according to Miettinen and Lasota. Moreover, using the inputted data and the full posterior distribution, the App computes the expected mitotic count on the surgical specimen (indicating also most probable rendered counts) and the predicted risk class for the new posterior distribution of $M_{s}$ provided (Figure 6).
![img-5.jpeg](img-5.jpeg)

Figure 6: The PROMETheus (PReOperative Mitosis Estimator Tool) App. The image shows a screenshot for a gastric GIST measuring 72 mm with a biopsy surface of 14.3 HPFs (about $3 \mathrm{~mm}^{2}$ ). With these biological characteristics the risk class is low. However the model shows that the mitotic count is likely to be underestimated, with the most probable count on the surgical specimen predicted to be between 5 to 8 mitoses in $5 \mathrm{~mm}^{2}$. Given this predicted mitotic count distribution, it is much more probable for the risk class to be high (more than 60\%). See text for further explanation.

## Development of the Preoperative Classification for GIST

To facilitate stage-adapted treatment planning and enhance data comparison across institutions, we developed a preoperative classification system for GIST based on the results of our computational model, PROMETheus. This classification system aims to provide a standardized definition of preoperative classification for GISTs, which can be used to guide therapeutic decisions and improve clinical trial designs (Table 2). The development of this classification included the probabilistic output of PROMETheus risk classification, important surgical parameters (such as site, size, etc.), and resectability.

Table 2: Proposed Preoperative Classification for GIST. ${ }^{4}$
Clinical


# Discussion 

## Principal Findings

Our study aimed to develop an innovative computational tool, PROMETheus, to accurately predict mitotic count on surgical specimens in Gastrointestinal Stromal Tumors (GISTs), thereby addressing the challenges associated with preoperative risk assessment and treatment planning. The primary objective was to bridge the gap between clinical judgment and computed risk class, empowering clinicians to make informed decisions in complex scenarios. Through the utilization of Bayesian Networks and rigorous covariate selection methodologies, we succeeded in achieving this objective, providing clinicians with a novel approach to preoperative risk stratification in GISTs.

Our findings represent a potential advancement in the field of oncology, particularly in the context of sarcomas, where precise risk assessment is paramount for optimal treatment outcomes. By accurately predicting mitotic count on surgical specimens, PROMETheus offers clinicians a tool to navigate the complexities of GIST management, enabling tailored treatment strategies based on individual patient characteristics. This approach aligns with the evolving paradigm of precision medicine, where treatment decisions are increasingly guided by molecular and pathological insights.

Mitotic count serves as a vital indicator of biological aggressiveness in oncology, playing a significant role in the grading systems of various tumors. With chemotherapy often administered to patients with high-grade tumors, mitotic count becomes a de facto predictive biomarker, providing valuable insights into treatment response. In the realm of Gastrointestinal Stromal Tumors (GISTs), alongside size and site, the number of

[^0]
[^0]:    ${ }^{4}$ Adapted from Cananzi et al. incorporating the probabilistic estimate of the Risk Class by our app PROMETheus [26].

mitoses holds utmost importance in current risk classifications [19-21]. However, unlike size and site, which can be easily assessed through imaging or endoscopy in the preoperative setting, accurately determining mitotic count poses challenges. Factors such as tumor heterogeneity and limited specimen size for counting (a classic example of sampling bias) hinder precise estimation during preoperative biopsy.

The introduction of effective therapies like Imatinib, which targets the molecular alterations driving GIST, has led to a clinical tendency to use this treatment preoperatively, even in cases where the risk of disease progression is not high. However, this approach has several drawbacks: Variable Response: not all patients exhibit a decrease in tumor size, which means the extent of the surgery may remain unchanged. Side Effects: Imatinib is not without side effects, highlighting the need for a tool to identify patients at genuine risk of metastasis who would benefit from neoadjuvant treatment. Risk Classification Post-Treatment: for patients treated with neoadjuvant Imatinib, it becomes challenging to perform risk classification on the surgical specimen, leaving uncertainty about the subsequent adjuvant therapy.

The integration of PROMETheus into clinical practice could have far-reaching implications for patient care. Not only does it could enable more precise risk stratification in GISTs, but it also could facilitate stageadapted treatment planning, ensuring that patients receive the most appropriate interventions based on their individual risk profiles. The preoperative classification system provided in Table 2 offers a common language for patient follow-up and treatment planning. It is a revision of previous work by our group [26], refined based on the insights gained from our current study. This classification could lay the foundation for improved data collection and comparison across institutions, fostering collaboration and advancing research efforts in the field of GIST management.

# Comparison to Prior Work 

Importantly, our study diverges from previous approaches that primarily focused on comparing biopsy and surgical specimens to evaluate the reliability of biopsy-based risk assessments. Instead, we recognized the inherent limitations of preoperative biopsy in predicting tumor grade, especially in the context of TKI therapyinduced tumor response. By focusing on predicting mitotic count directly, our approach transcends these limitations, providing clinicians with a more accurate and reliable tool for preoperative risk assessment.

There are many tools for risk stratification in oncological practice, also in the sarcoma field, mainly based on nomograms, that are usually employed to predict overall survival and the risk of metastasis [61]. While these tools have found utility in re-analyzing previous clinical studies and selecting patients for future trials [62], they are not tailored for Gastrointestinal Stromal Tumors (GISTs). Our innovative approach stands out in two crucial ways. First, our Bayesian methodology empowers clinicians by providing the full posterior probability, capturing the inherent uncertainty often overlooked by traditional frequentist approaches that focus on central estimates. Second, unlike prognostic prediction tools, our method solely aims to forecast the mitotic count on the surgical specimen, a distinctive objective.

# Strengths and Limitations 

Given the widespread use of mitotic count as a grading parameter, our approach holds potential for scalability across diverse clinical settings, such as breast cancer, solitary fibrous tumor, and soft tissue sarcoma [30,63] The integration of our posterior probability with other tools could enhance their effectiveness. However, our choice of prediction methods was largely constrained by the dataset's size, as machine learning methods like deep learning demand substantial computational resources and larger sample sizes [64], which are often limited in rare diseases. Bayesian networks offer an advantageous alternative with principled variable selection, interpretability, and no minimum sample size requirement, making them a fitting choice for our study.

Despite the promising findings of our study, several limitations warrant consideration.
First, our use of a complex multilevel hierarchical model, meticulously designed according to the Directed Acyclic Graph (DAG), introduces potential challenges in model efficacy and implementation. However, we addressed this complexity by subjecting the model to rigorous testing with simulated data, ensuring its robustness and reliability.

Second, the performance evaluation of PROMETheus is based on data from a relatively limited patient population, which may restrict the generalizability of our findings. However, unlike conventional approaches that rely solely on in-sample performance metrics for model selection, we employed PSIS-LOO-CV (Paretosmoothed importance sampling leave-one-out cross-validation) to identify the most effective model structure. Nonetheless, further validation on a larger and more diverse population is essential before considering the clinical deployment of PROMETheus, ensuring its efficacy and applicability across different clinical settings and patient demographics.

Third the development and deployment of PROMETheus as a web-based application are at an early stage. Although we have made the tool publicly available as an open-source resource to encourage validation and application by other researchers and clinicians, the current version may lack certain functionalities and userfriendly features (such as inclusion of risk classification other than Miettinen and Lasota). Future work should focus on enhancing the application's interface, usability, and integration with clinical workflows, as well as providing comprehensive user training and support to facilitate its adoption in clinical practice.

## Future Directions

We have developed a cutting-edge App that could revolutionizes the estimation of mitotic count on surgical specimens, not only providing accurate quantification but also addressing the uncertainty that clinicians face when encountering challenging cases. By bridging the gap between clinical judgment and computed risk class based on available parameters, our App empowers clinicians to make informed decisions in complex scenarios. While previous studies have primarily focused on comparing biopsy and surgical specimens to evaluate the reliability of the former as the gold standard, we diverge from this approach. Our study

transcends the limitations of preoperative biopsy in predicting tumor grade, shedding light on the underestimation of aggressiveness often associated with this method[65-68]. Embracing the widely accepted practice of causal modeling for covariate selection in epidemiological studies [69], we harness the power of Bayesian Networks to pioneer a novel tool capable of predicting mitotic count-a breakthrough unprecedented in existing literature.

In conclusion, our study represents a significant step forward in the development of precision tools for oncological risk assessment. By accurately predicting mitotic count on surgical specimens in GISTs, PROMETheus empowers clinicians to make informed treatment decisions, ultimately improving patient outcomes and advancing the field of sarcoma management. Moving forward, continued research and validation efforts will be essential to further refine and optimize the utility of PROMETheus in clinical practice, ultimately realizing its full potential in guiding personalized treatment strategies for patients with GISTs and other sarcomas.

# Acknowledgements 

We acknowledge the reSeARChOMA group of IRCCS Humanitas Research Hospital.

## Data availability

Data. De-identified patient data are available upon motivated request on the public repository Zenodo https:// zenodo.org/communities/humanitasirccs/. Code. Custom code for the analysis is available at www.github.com/slrenne/PROMETheus.

# Supplementary Files

# Figures

To determine the model covariates, we utilized a Directed Acyclic Graph (DAG). In this causal framework, several factors influence the mitotic count on the surgical specimen. Firstly, the dimension of the tumor impacts both the mitotic count on the biopsy and the surgical specimen. Larger tumors tend to exhibit higher mitotic activity. Secondly, the location of the tumor plays a crucial role in its growth pattern. For instance, gastric neoplasms often have more space to expand, leading to the development of symptoms with larger masses. Additionally, tumor location influences the accessibility of the biopsy site, as some sites are inherently more accessible than others. Lastly, the amount of surface area available on the biopsy directly impacts the accuracy of the mitotic count estimation. A larger surface area allows for more representative sampling of the tumor. This simplified causal model elucidates the relationship between various factors affecting GIST mitotic count. Please refer to the main text and supplementary materials for further details. In the model notation, D represents the dimension of the tumor, L denotes the location, $\mathrm{M}_{-} \mathrm{B}$ signifies the mitotic count on the biopsy, $\mathrm{M}_{-} \mathrm{S}$ indicates the mitotic count on the surgical specimen, and S represents the surface area of the biopsy.
![img-6.jpeg](img-6.jpeg)

Prior predictive simulation of the ? parameter, i.e., what the model anticipates before encountering the data. This plot displays 80 simulated cases derived from the priors. The majority of expected values indicate a very low mitotic count, aligning with real-world expectations. However, the model is not startled by higher mitotic counts, even though it anticipates encountering them in a minority of cases without prior training.
![img-7.jpeg](img-7.jpeg)

Posterior predictive simulation. The upper panel shows the imputed ? parameter for each sample against the ground-truth; consider the logarithmic scale on the y-axis. The lower panel shows the same imputed ? parameter against the fitted data. On average the mitotic count either on the surgical specimen or on the biopsy is lower than the expected value, this is due to the asymmetry of the Poisson distribution. The size of the X is proportional to the biopsy surface, the size of the empty dots is proportional to the tumor size; the color of the background corresponds to the tumor site.
![img-8.jpeg](img-8.jpeg)

Posterior predictive simulation on the true dataset. The size of the X is proportional to the biopsy surface, the size of the empty dots is proportional to the tumor size; the color of the background corresponds to the tumor site.
![img-9.jpeg](img-9.jpeg)

Model Selection. The vertical line indicates the mean deviance of the reference model (the one with the lowest out of sample deviance). The filled dots are values within the sample. The empty dots represent mean the out of sample deviance with the bar indicating the $89 \% \mathrm{CI}$; the triangle is the contrast between the model and the reference model.
![img-10.jpeg](img-10.jpeg)

The PROMETheus (PReOperative Mitosis Estimator Tool) App. The image shows a screenshot for a gastric GIST measuring 72 mm with a biopsy surface of 14.3 HPFs (about $3 \mathrm{~mm}^{*} 2$ ). With these biological characteristics the risk class is low. However, the model shows that the mitotic count is likely to be underestimated, with the most probable count on the surgical specimen predicted to be between 5 to 8 mitoses in $5 \mathrm{~mm}^{*} 2$. Given this predicted mitotic count distribution, it is much more probable for the risk class to be high (more than $60 \%$ ). See text for further explanation.
![img-11.jpeg](img-11.jpeg)

# Multimedia Appendixes

Supplementary materials.
URL: http://asset.jmir.pub/assets/0ccf552bbcb5ba46d3f8e070a6ed3d77.docx
Main paper with track changes.
URL: http://asset.jmir.pub/assets/9f91aa97a835d5b6ad1c8cd8c7afcd87.docx
A more elaborated DAG. During optimization cycles of modeling, we greatly simplified both the DAG and the probabilistic program used. Indeed, our first modeling attempts included several latent variables (circled) as the true mitotic rate (M) and the biologic aggressiveness (U), and modeled in detail the disease presentation (including symptoms among the variables), the therapy indication and its response; although this DAG is more accurate, its complexity impairs greatly the parameter estimation efficiency. Moreover, within the domain of Bayesian network, a different approach using system of equations that literally translate the SCM in the code for the fitting might have been used, however the choice of a more simplified approach (i.e., using the $\mathrm{M}_{-} \mathrm{S}$ as inferential target instead of as a variable) removes the need to refit the model to impute the value.
URL: http://asset.jmir.pub/assets/94596f48e5b31d116019ea651090e0c9.png
Prior predictive simulation for model coefficients. The coefficients for tumor size and surface (respectively ? and ?) show a wider (t) distribution compared to the biopsy count (? or ? if response to neoadjuvant therapy - NAC - is present).

URL: http://asset.jmir.pub/assets/574c005f419b5417d02e6d1de14430cf.png
Fit's diagnostics on the simulated dataset. The upper panel plots the number of effective samples against the R ?; the vertical gray line represents the total number of samples (half of the 8000 iterations - the first 4000 are discarded - multiplied for the 4 chains). The second panel shows the energy of the Hamiltonian, nicely following along a normal distibution (background blue line). The third panel shows a rank histogram plot (trankplot) for the log-probability of the model. Each of the four chains alternates in dominating the ranking; this indicates that the chains mixed and converged.
URL: http://asset.jmir.pub/assets/5ac0b0786912615a9b8182227c42c24d.png
Rank histogram plot (trankplot) for the all parameters. All the parameters have a nice mixing of the chains.
URL: http://asset.jmir.pub/assets/278b49b162fb7ae43aaf84f81e7cb8b8.png
Model coefficients from fitting the simulated data-set.
URL: http://asset.jmir.pub/assets/d59daacc45e0fd9795cd197ac37ddc2b.png
Fit's diagnostics on the real GIST cohort. The upper panel plots the number of effective samples against the R ?; the vertical gray line represents the total number of samples (half of the 4000 iterations - the first 2000 are discarded - multiplied for the 4 chains). The second panel shows the energy of the Hamiltonian, nicely following along a normal distibution (background blue line). The trankplot for the log-probability of the model shows a nice mixing of the chains.
URL: http://asset.jmir.pub/assets/9aefc3d20e56cd58b457dbfe3e10da62.png
Rank histogram plot (trankplot) for the all parameters. All the parameters have a nice mixing of the chains.
URL: http://asset.jmir.pub/assets/352de2e153a51e2cf1b8c3e4d3df4f3a.png
Model coefficients from fitting the simulated data-set.
URL: http://asset.jmir.pub/assets/34897f99899df5a31295b18b2a2dfc6c.png