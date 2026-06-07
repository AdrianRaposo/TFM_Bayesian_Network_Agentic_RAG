# UNIVERSITYOF 

FORWARD THINKING WESTMINSTER ${ }^{\text {M }}$

WestminsterResearch<br>http://www.westminster.ac.uk/westminsterresearch

## Ensemble Risk Model of Emergency Admissions (ERMER) <br> Mesgarpour, M., Chaussalet, T.J. and Chahed, S.

NOTICE: this is the authors' version of a work that was accepted for publication in International Journal of Medical Informatics. Changes resulting from the publishing process, such as peer review, editing, corrections, structural formatting, and other quality control mechanisms may not be reflected in this document. Changes may have been made to this work since it was submitted for publication. A definitive version was subsequently published in International Journal of Medical Informatics, doi: 10.1016/j.ijmedinf.2017.04.010, 2017.

The final definitive version in International Journal of Medical Informatics is available online at:
https://dx.doi.org/10.1016/j.ijmedinf.2017.04.010
© 2017. This manuscript version is made available under the CC-BY-NC-ND 4.0 license http://creativecommons.org/licenses/by-nc-nd/4.0/

The WestminsterResearch online digital archive at the University of Westminster aims to make the research output of the University available to a wider audience. Copyright and Moral Rights remain with the authors and/or copyright owners.

Whilst further distribution of specific materials from within this archive is forbidden, you may freely distribute the URL of WestminsterResearch: ((http://westminsterresearch.wmin.ac.uk/).

In case of abuse or copyright appearing without permission e-mail repository@westminster.ac.uk

# Accepted Manuscript 

Title: Ensemble Risk Model of Emergency Admissions (ERMER)

Author: Mohsen Mesgarpour Thierry Chaussalet Salma Chahed

PII: S1386-5056(17)30088-6
DOI: http://dx.doi.org/doi:10.1016/j.ijmedinf.2017.04.010
Reference: IJB 3501
To appear in: International Journal of Medical Informatics
Received date: $\quad 21-12-2016$
Revised date: $\quad 11-4-2017$
Accepted date: $\quad 14-4-2017$
Please cite this article as: Mohsen Mesgarpour, Thierry Chaussalet, Salma Chahed, Ensemble Risk Model of Emergency Admissions (ERMER), $<$ ![CDATA[International Journal of Medical Informatics]]> (2017), http://dx.doi.org/10.1016/j.ijmedinf.2017.04.010

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Ensemble Risk Model of Emergency Admissions (ERMER) 

Mohsen Mesgarpour ${ }^{1, *}$, Thierry Chaussalet ${ }^{1, *}$, Salma Chahed ${ }^{1, *}$<br>HSCMG, Faculty of Science and Technology, University of Westminster, 115 New Cavendish Street, W1W 6UW London, UK


#### Abstract

Introduction: About half of hospital readmissions can be avoided with preventive interventions. Developing decision support tools for identification of patients' emergency readmission risk is an important area of research. Because, it remains unclear how to design features and develop predictive models that can adjust continuously to a fast-changing healthcare system and population characteristics. The objective of this study was to develop a generic ensemble Bayesian risk model of emergency readmission.


Methods: We produced a decision support tool that predicts risk of emergency readmission using England's Hospital Episode Statistics inpatient database. Firstly, we used a framework to develop an optimal set of features. Then, a combination of Bayes Point Machine (BPM) models for different cohorts was considered to create an optimised ensemble model, which is stronger than the individual generative and non-linear classifications. The developed Ensemble Risk Model of Emergency Admissions (ERMER) was trained and tested using three time-frames: 1999-2004, 2000-05 and 2004-09, each of which includes about $20 \%$ of patients in England during the trigger year.

Results: Comparisons are made for different time-frames, sub-populations, risk cut-offs, risk bands and top risk segments. The precision was $71.6 \%$ to $73.9 \%$, the specificity was $88.3 \%$ to $91.7 \%$ and the sensitivity was $42.1 \%$ to $49.2 \%$ across different time-frames. Moreover, the Area Under the Curve was $75.9 \%$ to $77.1 \%$.

Conclusions: The decision support tool performed considerably better than the previous modelling

[^0]
[^0]:    *Corresponding authors

    Email addresses: mohsen.mesgarpour@gmail.com (Mohsen Mesgarpour), T.Chaussalet@westminster.ac.uk (Thierry Chaussalet), S.Chahed@westminster.ac.uk (Salma Chahed)

approaches, and it was robust and stable with high precision. Moreover, the framework and the Bayesian model allow the model to continuously adjust it to new significant features, different population characteristics and changes in the system.

Keywords: Hospital Episode Statistics, Readmission, Ensemble, Bayesian, Framework, Inpatient

# 1. Introduction 

The cost of care is increasing at a rate that is unaffordable in the current economy. This is mainly due to the impact of ageing population, population growth, deprivations, the increase in emergency admissions, increased expectations, and the cost of treatment and technology (NHS, 2013; DH, 2013; Lewis et al., 2011). The current system is unsustainable and unfair, and the current financial options available to support people in meeting care costs are limited.

The National Health Service (NHS) spends an estimated $£ 11$ billion per year on emergency admissions in England (Lewis et al., 2011). According to the Nuffield Trust report in 2012 (Nuffield Trust, 2012), about $8 \%$ of discharged patients are readmitted within 30 days, costing an estimated $£ 2.2$ billion a year. Based on a retrospective study by Clarke et al. (2012) (Clarke et al., 2012), about half of the 30-day emergency readmissions were potentially preventable between 2004 and 2010.

Four major risks have contributed to the increase in emergency (or unplanned) readmissions to hospitals (HSCIC, 2013; Lewis et al., 2011): ageing population (Caley and Sidhu, 2011), patients with long-term conditions (DH, 2012), premature discharge and unpredictable accidents and emergency (Clarke et al., 2012). While discharging patients provides a way of freeing beds in healthcare systems, premature discharge could still increase the risk of emergency readmissions. Often hospital admission or readmission can be avoided by providing adequate care (Bardsley et al., 2012).

Therefore, developing and implementing a robust decision support tool for admitted patients is critical. Predictive risk models can help patients and carers obtain appropriate support services in clinical decision-making. In addition, such models can improve care quality and reduce the costs of inappropriate admissions to hospital and accident and emergency (A\&E).

In 2005, the UK Department of Health (DoH) commissioned the Patients at Risk of Re-hospitalisation (PARR) (Lewis, 2011; Billings et al., 2006) algorithm and the PARR++ software for Primary Care

Trusts (PCTs) (Lewis et al., 2011; The King's Fund, 2016). The aim of the PARR model was to identify individuals at high risk of emergency readmission to a hospital within a year based on the inpatient data from the Hospital Episode Statistics (HES) database. Thereafter, in 2006, to address the need for identifying the patient risk along a continuum, the DoH released the Combined Predictive Model (CPM) which was based on General Practice (GP) and the HES data (DH, 2006).

In 2011, the DoH commissioned an upgrade to the PARR and the CPM models (Nuffield Trust, 2012; DH, 2011). The Patients at Risk of Readmission within 30 days (PARR-30) model was developed as an upgrade to be run by acute hospitals. The PARR-30 model was based on a broad range of measures used in the PARR (Billings et al., 2012).

After the controversies of the 2012 Heath and Social Care Act (Timmins, 2013), the care system moved towards developing new models of integrated care. The NHS's strategic five-year forward view (NHS, 2014) outlines that commissioners, the NHS and other providers will co-design the services based on a model of integrated care that targets specific cohorts, with their own exemplars, potential benefits, risks and transition cost.

In the NHS, patients' interactions with hospital services are recorded on statutorily defined datasets, known as the Secondary Uses Service (SUS). The SUS data are cleaned and combined on a national basis to create HES data. The HES contains administrative hospital data for all inpatient, outpatient and accident and emergency (A\&E) admissions in England. And, they hold admission, clinical, utilisation and demographics details in format of episodes and spells (HSCIC, 2016a).

In this research, performances of the PARR, the CPM and the CPM update were used as the benchmark, since these tools use the HES data and are still being used by commissioners across England. These decision support tools help to rank and group patients based on anticipated intervention level, including case management, disease management, supported care, prevention and wellness promotion.

Most existing decision support tools based on hospital administrative data use logistic regression or Coxian Phase-type Distribution models (Paton et al., 2014; Kansagara et al., 2011; Lewis et al., 2011; DH, 2011; ACI, 2014; Bardsley, 2012; Bottle et al., 2014; Mesgarpour et al., 2016b; Adeyemi et al., 2013). Although these models are simple and popular, they have limited power, because of

algorithm shortfalls, restricted assumptions and weak variable selection strategies. In the area of healthcare risk modelling research, there have been many successful implementations of machine learning methods (Green et al., 2006; Nilsson et al., 2006; Song et al., 2004; Peelen et al., 2010; Lee et al., 2012). However, few studies used a Bayesian approach to address emergency hospital readmission problems (Álvaro-Meca et al., 2012; Demir and Chaussalet, 2011; Cui et al., 2015; Helm et al., 2015; Gupta et al., 2014; Huws et al., 2008).

This study develops an ensemble generative risk model of emergency readmission within a year to hospitals in England. The machine learning ensemble method is a powerful technique, which uses a finite set of weaker models and an algorithm to combine and optimise the performance of the ensemble model. The HES inpatient data was extracted from English hospitals and maintained by the Health and Social Care Information Centre (HSCIC) (HSCIC, 2016c). Based on a preprocessing framework (Mesgarpour et al., 2016a), features were cleaned, generated, filtered and ranked. Thereafter, a number of sub-models based on population characteristics were trained using a Bayes Point Machine (BPM) approach. Afterwards, an optimised ensemble model of these sub-models was generated. The proposed model, the Ensemble Risk Model of Emergency Admissions (ERMER), was trained, tested and validated using three different time-frames.

The paper is structured as follows. Firstly, we describe the data and then the process of selecting a minimal number of features. Thereafter, the applied BPM algorithm is defined and the ensemble model is presented. Finally, we discuss the results of training, testing and benchmarking the ERMER, against the CPM (DH, 2006), the PARR (Billings et al., 2006) and the CPM update by Billings et al. (2013) (Billings et al., 2013) models.

# 2. Methods 

### 2.1. Data

Administrative databases are used to monitor healthcare systems in the UK, the USA and other countries. Furthermore, healthcare data, such as inpatient, A\&E, outpatient and GP records are used in predictive modelling problems (Jensen et al., 2012; Mullins et al., 2006). In addition, clinical databases compliment administrative databases, but they are expensive and not usually open to

the public. According to a study (Raftery et al., 2005), the cost per record for clinical data can range from $£ 10$ to $£ 60$, compared to $£ 1$ per record for the HES database.

In this research, only the HES inpatient data was used. The available snapshot of the database includes records from April 1995 to April 2010. The inpatient table consists of 206,528,432 episodes. This excludes 39,403 episodes with invalid admidate (admission date) and 11,212,871 episodes with invalid hesid (patient ID). In addition, similarly to the PARR model, each sample covers about $20 \%$ of unique patients within the trigger year of the selected time-frame (Table 1).

Table 1
Selected samples from the HES Inpatient database.


Before the modelling stage, four stages of data preprocessing were carried out (Mesgarpour et al., 2016a). Firstly, the extracted data was sorted by patients and the order of episodes. Then, invalid records were excluded. Thereafter, several corrections and imputations were carried out on dates, Healthcare Resource Groups (HRG) and demographics. Finally, some of the continuous features were converted into discrete to better capture non-linear interactions with other features. And, some of the discrete features were categorised into bigger groups to reduce sparseness and overfitting risks.

Similarly to the PARR model, the data was divided into three years of prior history, one year of trigger admission and one year of prediction period (time horizon). Then, half of each sample was used for training (train sub-sample) and the rest was used for testing (test sub-sample). Furthermore, spells were grouped into superspells based on the admission dates. A patient superspell is as a unit of care for the patient, which is the combination of all same-day episodes by any provider.

In this study, different combinations of the train sub-samples and the test sub-samples were used, but train and test have fixed definitions throughout the analyses (Table 4). The train sub-samples are used for training, learning-curve and complexity analysis. The test sub-samples are used for testing, cross-validation and benchmarking. Furthermore, no separate validation sub-sample is defined, since different modelling methods are not being compared.

# 2.2. Features 

Based on previous studies (Billings et al., 2006, 2013, 2012; NHS, 2011; Mullins et al., 2006; Bardsley et al., 2013) and additional exploratory analyses, four main groups of features were initially generated from the inpatient database: three years cross-sectional, one year cross-sectional, 90 days cross-sectional and trigger-point features. In total, 738 summary features were generated, which the main categories are presented in Table 2.

Table 2
Main categories of all the initially defined features.


Usually, Kernel classifiers, such as the BPM and the Support Vector Machine (SVM), are resistant to over-fitting, because of a weight regularisation implementation (Cawley and Talbot, 2007, 2010). However, since the number of generated features was very high, a feature reduction strategy was needed. Based on the framework developed in the previous stage of our research (Mesgarpour et al., 2016a), four steps of feature filtering were carried out, in order to reduce the number of features and to better capture the underlying structure.

Initially, highly stationary features were removed (constant count $\geq 95 \%$ ). Then, features that were highly linearly correlated were excluded (linear correlation coefficient $\geq 80 \%$ ). Thereafter, based on the average importance, initially, the three-year cross-sectional features were included, and then other features were added. Next, the features were sorted based on importance across train subsamples using two different methods: a random-forest importance score and an SVM importance ranking. Finally, a step-wise BPM procedure was developed using a forward-selection approach (micro average precision $\geq 0.01 \%$ ).

The applied random-forest algorithm is a non-linear method and is an implementation of Breiman's algorithm (Breiman, 2001), which applies significance test criteria (Hothorn et al., 2010). It performs recursive univariate splitting and selects covariates based on the significance test. The sig-

nificance test approach, unlike the maximising information, does not suffer a systematic tendency towards covariates with many possible splits or many missing values. However, highly similar features and linearly correlated features were excluded in the prior step, because the applied algorithm is sensitive to correlated features.

Moreover, the SVM Recursive Feature Extraction (SVM-RFE) algorithm proposed by Guyon (Guyon et al., 2002) is applied to rank features recursively using SVM. The SVM-RFE algorithm ranks the features by training an SVM with a linear kernel and removing the features with the smallest ranking criterion.

# 2.3. Modelling Approach 

Logistic regression, neural network, decision trees, Bayesian models and kernel methods, such as SVM and Gaussian processes, are often used in healthcare data mining. In this research, the Bayes Point Machines (BPM) method was chosen, since it is not prone to overfitting, highly efficient in approximating the Bayesian average classifier.

BPMs (Herbrich et al., 2001; Minka, 2001a) are a type of nonlinear classification algorithm, that identify an average classifier known as a Bayes Point in a version space. A version space can be defined as a set of hypotheses, each of which is an approximation of the main hypothesis class. Similar to SVMs, BPMs are more geometrically motivated and they try to find a hyperplane with an optimal margin between classes. In contrast, logistic regression maximises the probability of data by optimising the distance of each point to the decision boundary.

The soft margin SVM can be thought of as an approximation to BPMs (Herbrich et al., 2001). SVMs (Vapnik and Vapnik, 1998) use a mapping to indirectly transform data into higher dimensional space using a kernel function. Then, they use quadratic programming to optimise the classification's hyperplanes using support vectors and margins. However, the complexity of SVMs are characterised by the number of support vectors, and are only efficient for a symmetric version space.

On the other hand, BPMs sample the Bayesian posterior (Eq. 1) for a nonlinear classification in a kernel space. Then, they approximate the centre of the version space, which is a set of consistent hypothesis, and the effective size is determined from the training sample. BPMs minimise the generalisation error over a set of hypotheses according to a prior probability, instead of maximising

the classification boundary margin explicitly, as SVMs do. The predictive distribution can be thought of as a linear discriminant function, which is assumed to have the following parametric density:

$$
p(y \mid x, w)=p\left(y \mid s=w^{T} x\right)
$$

where $w$ is the weight or latent parameter vector, $x$ is the fully observed feature vector, and $s$ is the score function. BPMs use the kernel trick to find an optimised $w$, and the centre mass of the version space is approximated using an average of the weight vectors while minimising the average generalisation error. The derived scores are subject to additive Gaussian noise to allow for measurement or labelling errors (Eq. (2)).

$$
\begin{gathered}
p(y \mid s, \varepsilon)=(y s+\varepsilon>0) 1 \\
\text { , with } p(\varepsilon)=N(\varepsilon \mid 0,1), \wedge 1(\alpha>0)= \\
\begin{array}{l}
1 \\
0
\end{array} \quad \text { if } \alpha>0 \\
\text { if } \alpha \leq 0
\end{gathered}
$$

In this research, Microsoft's Infer.Net library (Microsoft Research, 2016) was used to construct the BPM model. The applied algorithm uses the original version of the BPM, with two main modifications. Firstly, it uses a mixture of Gamma-Gamma, a heavy-tailed prior probability distribution for the precision of weights and features. Secondly, it applies the Expectation Propagation (EP) message passing to infer posterior probabilities, which has been demonstrated (Minka, 2001b,a) in Gaussian mixture problems to be better than approximation techniques. Therefore, it is invariant to parameter rescaling or shifting, unlike logistic regression or SVM. Moreover, active Bayesian training can allow continuous updates of the model and account for changes in the prior probabilities. Furthermore, the BPM can efficiently handle a relatively larger number of features.

# 2.4. Ensemble Model 

Firstly, one main model (cond_main) and four conditional sub-models were specified with significantly diverse populations which represent unique clinical and behavioural categories (Fig. 1). The conditional sub-models includes: prior 12-month acute spells (Cond_Prior-Acute-12-month), prior

![img-0.jpeg](img-0.jpeg)

Fig. 1. The Ensemble model.

12-month operation (Cond_Prior-Oper-12-month), prior spells (Cond_Prior-Spells) and age 65+ (Cond_Age-65p).

Afterwards, they were trained and tested across the sub-sample combinations (Table 4). Considering that the filtered features are more relevant for the main model, the sub-models have very different performances but with stable weights.

Then, to improve the performance of the decision support system, we decided to use an ensemble model (Algorithm 1). Three main challenges in ensemble modelling were: method of constructing sub-classifiers, weighting the classifier and optimisation. Based on background research and multiple trials, a weighted average ranking method was constructed, in addition to a heuristic method to optimise the weights of sub-classifiers (Sewell, 2008; Rokach, 2010; Sammut and Webb, 2011; Zhou, 2012; Murphy, 2012).

In another word, the ERMER partitions the data instance space, based on some populations similarities (sub-models). Then, it uses data envelop analysis methodology (Charnes and Cooper, 1984) to assign weights to different classifiers (Rokach, 2005). In this research, we refer to this weight function as the cost function, because we applied a search technique to optimise the weights that are assigned to each sub-model.

The cost function for the optimisation was defined as a normalised combination of four performance metrics: ACC (Accuracy), AUC, RMSE (Root Mean Square Error) and SAR (Squared error, Accuracy and ROC area) (Brown, 2011; Alvarez, 2011; Fukunaga, 2013). The applied ensemble algorithm (Algorithm 1) uses a bidirectional hill-climbing algorithm with a greedy initial solution set (models ${ }_{\text {ensemble }}$ ) to generate an optimised ensemble model from the sub-models.

Firstly, it generates an initial solution based on the main model and one other sub-model with the highest Area Under Curve (AUC) of the Receiver Operating Characteristic (ROC). Then, a bidirectional hill-climbing (Russell and Norvig, 2002) heuristic was applied to optimise the average of the four performance metrics, through iterations, trials (trials) and across samples (samples).

The hill-climbing method is a greedy sequential search with forward and backward passes, where the learning rate for each performance metric can be tuned manually prior to the execution. The learning rate in the algorithm (Algorithm 1) defined using alpha ${ }_{\text {ensemble }_{\text {min }}}$ for the performance indicators (Fukunaga, 2013; Caruana et al., 2004; Opitz and Maclin, 1999).

The sub-models in the ensemble heuristic are selected using a bagging ensemble (selection with replacement). Then, the sub-models are combined using a mean combiner, which is the approximate posterior probability based on the weighted average of the risk scores, without any additional training. When the first run of the algorithm, with the defined iterations, trails and train subsamples, is finished; then, the second run, with less sensitive limits and thresholds, is executed using the best solutions of the first round.

$$
\begin{aligned}
\text { model }_{\text {ensemble }}= & \text { Mean }\{\text { Cond_Main }+ \text { Cond_Age- } 65 p_{0}+ \\
& 9 \text { Cond_Age- } 65 p_{1}+4 \text { Cond_Prior-Oper-12-month } \\
& \left.2 \text { Cond_Prior-Oper-12-month }_{1}\right\}
\end{aligned}
$$

Finally, the best performing ensemble model, with the minimum number of unique sub-models is selected. The optimised Ensemble Risk Models of Emergency Admissions (ERMER) based on our data sets is defined in Eq. (3). In this equation, a sub-model subscript represents the conditional state, and the coefficients represent the weights in the ensemble mean combiner.

# 3. Results 

### 3.1. Goodness of fit

Four stages of performance checks were performed across test sub-samples to access the goodness of fit. Firstly, a learning-curve plot of training micro-average errors versus the number of training

points for sub-models was generated. The learning-curve is a function of the number of training points and the prediction accuracy rate, and it allows investigating the effect of sample sizes on the performance of models (Nordhausen, 2009; Murphy, 2012). Fig. 2a demonstrates that the train subsample size greater than 40,000 patients contributes very little to sub-models performances.

Table 3
The top significant features in the sub-models.


Moreover, the effects of complexity levels were investigated for the main model (Cond_Main) using F-score versus the number of features. The plot of the effects of complexity levels shows how the step-wise addition of top features changes the prediction performance of a model. Fig. 2b shows that adding up to 18 features (Table 3) from the sorted selected features improves the model's performance significantly; however, the gains then become very small (on average 0.005 change in AUC percentage). The presented learning-curve plot and complexity plot are for Sample-1 train sub-sample, although the results are consistent across all other time-frames.

Thereafter, the convergences of the sub-models were tested using an iterative fitting, using train sub-samples, in order to assess over-fitting and variations in convergence. Fig. 3a shows that after the first few iterations, all sub-models converge quickly and after 40 iterations, the weights differences become very small.

Furthermore, a $k$-fold cross-validation (Murphy, 2012) algorithm was implemented for all the three test sub-samples (Table 4). Each test sub-sample was split into five equal-sized random samples. Then, $K-1$ folds was used for training and the $K$-th fold was used for validation. The final performance was generated after the cross-validation cycled through all the $K$ combinations of splits. Fig. 3b exhibits very small standard deviations in the accuracy, the mean of negative log-probability and the AUC for the sub-models' cross-validations.

![img-1.jpeg](img-1.jpeg)
(a) Learning-curve of sub-models, micro-average error versus number of training points.
![img-2.jpeg](img-2.jpeg)
(b) Complexity analysis of sub-models, the F-score versus number of features.

Fig. 2. Learning-curve and complexity analysis plots of sub-models (train sub-sample from Sample-1).

Finally, the profiling was done using the three test sub-samples, based on population characteristics and performance indicators (Table A. 1 and Table A.2). Table A. 3 demonstrates the weights of the features for each sub-model, as well as the features definitions, encoded categories and temporal states. In the following section the benchmark is discussed.

# 3.2. Benchmark 

Admission risk models are limited by the characteristics of the selected subpopulation and data quality issues, such as missing diagnoses for outpatients and A\&E patients (Billings et al., 2013), delayed death registration (ONS, 2014) and the number of registered or consented patients. Moreover, models developed by researchers usually have different settings and assumptions; hence, comparisons become more subjective.

The developed ERMER model is benchmarked against the CPM (DH, 2006; Paton et al., 2014), the PARR (Billings et al., 2006) and Billings et al. (2013) (Billings et al., 2013) models using the reported performance statistics.

![img-3.jpeg](img-3.jpeg)

Fig. 3. Summary statistics of convergence and cross-validation tests for all sub-models (test sub-samples).

For the testing, validation and benchmarking phase, three data settings were considered: Sample1's train and test sub-samples, Sample-2's train and test sub-samples, and finally a rolling window setting with Sample-1's train sub-sample and Sample-3's test sub-sample (Table 4). The rolling window is configured as the one-year gap in admission trigger year, to better assess the stability of the model over time. In addition, for better comparison against the benchmark models, three different subpopulations were selected from the outputted test results (Sub_PARR-2-Settings, Sub_ IPAEOPGP and Sub_Any-Acute).

Table 4
Combinations of test and train sub-samples.


For comparison, numerical summaries beyond the ROC and abstract statistical summaries must be used to avoid misinterpretation (Steyerberg et al., 2010; Pencina et al., 2008; Cook, 2007). In addition to the ROC (Fig. 4), the profiling is presented using three forms of presentations: summary

![img-4.jpeg](img-4.jpeg)

Fig. 4. ROC of the PARR model (reported figure) against the ERMER model (test sub-samples).
statistics for three risk cut-off points (Table 6) against the previous models (Table 5), summary statistics for 20 risk bands (Table A.1) and the profile of top risk segments (Table A.2).

The ERMER model made considerable improvement to the previous models. For instance, according to Table 6, the ERMER model with subpopulation Sub_Any-Acute has precision 0.719 and AUC of 0.771 with Sample-1 as the test set, compared to $0.529,0.73$ for the Billings et al. (2013) model with inpatient (IP) data.

# 4. Discussion 

In this study, a set of significant features was initially developed using a framework. Then, several predictive models were trained based on different subpopulations. The defined sub-models were fitted using a BPM algorithm, with Gamma priors, and EP message passing for the inference of the posterior. Furthermore, an optimised ensemble of five sub-models was produced based on the age group sub-models, the 1-year prior operation sub-models and the general model.

Table 5
The benchmark of the previous emergency readmission models (reported statistics)


Table 6
The benchmark of the ERMER model for different sub-populations using test sub-samples.


${ }^{a}$ Population setting for the PARR-2 model: age: 65+; Trigger admission: Emergency.
${ }^{\text {b }}$ Population setting for the Billings et al. (2013) model: Age: 18-95; Trigger admission: Emergency.
${ }^{\text {c }}$ All the population for the selected sample: Trigger admission: Emergency admission.

Thereafter, the developed decision support tool, Ensemble Risk Model of Emergency Admissions (ERMER), was benchmarked against the PARR, the CPM and Billings et al. (2013) models, with very similar settings. The proposed model outperforms other models for any-emergency readmissions and the subpopulation of 18 to 95 -year-old patients. The ROC of any-emergency readmission

is between 0.759 and 0.771 , compared with the PARR, which is 0.69 with an age restriction (65+) and an HRG restriction (reference conditions). In addition, the performance is very close to the CPM and Billings et al. (2013) models, which predict any-emergency admissions using inpatient, outpatient, A\&E and GP data.

# 4.1. Data 

Firstly, the feature preparation is the most time-consuming part of many analyses. There are three main layers of difficulties in the preparation of features: correlations, recategorisations and selections (Mihaylova et al., 2011; Walpole et al., 2014; Yang et al., 2005). In this study, the variables were generated and selected based on the previously developed preprocessing framework (Mesgarpour et al., 2016a). Based on this framework, a large pool of variables was generated and reduced based on a set of defined criteria. Then, these were ranked and top features were inputted into the model.

Capturing high-risk patients using diagnoses can be difficult owing to variate coding practices, under-reporting of diagnostic variables, incomplete coding of transferred patients and comorbidities' complexity (Bottle et al., 2011; Billings et al., 2013; Reimer et al., 2016). Therefore, only high-level diagnoses groups were included and the remaining detailed codes were aggregated.

In this study, a recent version of Charlson index was used, which is actively maintained by the HSCIC and Dr Foster unit (Aylin et al., 2010; Bottle et al., 2011). Comorbidity scoring is usually used to distinguish the conditions present on admission from complications. But, poor coding and disregarding the effects of population characteristics can introduce bias (constant risk fallacy) (Nicholl, 2007; Fischer et al., 2011). Other criticisms of scoring originate from choosing small cohorts, using additive risk models of different medical conditions, ignoring important factors, such as the length-of-stay and the presence of different valid principal diagnoses across different cohorts (Quan et al., 2005; Bottle and Aylin, 2011).

Moreover, left-censored and right-censored observations introduce bias in the features and predicted risk estimates (Singer and Willett, 2003). According to Table 1, about $8 \%$ to $15 \%$ of patients do not have any admissions after the trigger event. In addition, about $28 \%$ to $51 \%$ of patients do not have any other prior admissions before the trigger event.

Finally, it has been speculated that many of the variations in readmission can be due to the delivery of the care method, which cannot be quantified using an administrative database only (Bottle et al., 2014; Billings et al., 2013; DH, 2006).

# 4.2. Model 

There is always scepticism about machine learning because of the hypes or failures of inappropriate modelling approaches. For instance, Bottle et al. (2014) (Bottle et al., 2014) stated that machine learning methods, particularly Neural Networks (NN) and SVMs, did not offer noticeably better predictions for readmission risk compared to linear regression, and were relatively harder to implement. But, we believe there were four main possible flaws: missing influencing features in the Principal Component Analysis (Yang et al., 2005); using highly interdependent features, small training sets or a weak network design for the NN (Matignon, 2005); ignoring the temporal dimension and prior probabilities; and linearity and homogeneity assumptions (Congdon, 2010).

In general, accuracy and efficiency of a Bayesian model depend on five main design choices: the representation of features, fitness algorithm, inference approximation, assignment and update of prior probabilities, and the framework of system states.

Firstly, the features were carefully generated, selected and ranked before generating the models. The initial prototype models, without the aforementioned feature selection strategies, have shown very high sensitivity to intercorrelations, sparsity and noisy features. As a result, these caused non-convergence, weight decay and performance degradation.

Moreover, in comparison with the SVM, the BPM method is demonstrated (Herbrich et al., 2001) to provide a better solution for an asymmetric version space, to efficiently handle large datasets and to provide a smoother decision boundary.

Furthermore, Microsoft's version of the BPM algorithm (Microsoft Research, 2016) uses EP message passing, which in Gaussian mixture problems is demonstrated (Minka, 2001b,a) to be better than approximation techniques, such as the Markov Chain Monte Carlo, Laplace and Variational Bayes techniques. The EP does not guarantee convergence, but in practice in many cases, it does, especially if the features are not highly interdependent to become trapped in a region of local optima.

Finally, the choice of prior probability distributions of the weights and features can have a significant impact on the robustness of the algorithm. The applied algorithm uses a heavy-tailed prior, which is more robust towards outliers of the weight distributions. Also, the incremental Bayesian training of the ERMER allows it to incorporate the effects of changes in prior distributions.

# 4.3. Performance 

All the sub-models are stable in the convergence and cross-validation testing. However, the features are initially selected based on the main model's population. The weights are very similar, proportionally, for all sub-models owing to very similar feature distributions, except for two: the sub-model with no prior spell (Cond_Prior-Spells ${ }_{0}$ ) and the sub-model with no prior operation (Cond_Prior-Oper-12-month ${ }_{0}$ ).

Furthermore, the applied BPM algorithm can handle a large number of features and a moderately large number of observations in comparison to logistic regression. On average, it takes about two to eight minutes ${ }^{1}$ to train a sub-model with 100 features.

Also, the models performances are consistently high across all the test sub-samples. The performance of the main sub-models improves the ROC (Fig. 4), sensitivity, specificity and precision percentage by $2.83,0.50,1.26$, and 2.83 , respectively (Table 6 ).

Furthermore, the populations of readmitted patients are very low; therefore, the samples are significantly unbalanced in terms of the dependent variable. The main models have 3 to 4.5 times less, and sub-models have between 1 to 10 times less readmitted patients compared to non-readmissions. Therefore, based on the sensitivity, precision, and the ROC, models can more confidently identify low-risk patients, and avoid unnecessary interventions.

In addition, it improves the previous model (Mesgarpour et al., 2016a), which does not use the ensemble of subpopulations. The ROC and precision percentage of the any-acute model increase by 2.83 and 7.16 , respectively, and sensitivity decreases in consequence.

Moreover, the features were selected based on the main model, which considers all the emergency admission population. Therefore, the PARR subpopulation under-performs. However, compared

[^0]
[^0]:    ${ }^{1}$ Windows 10 machine with Intel i7 2 GHz quad-core CPU and 8 GB 1600 MHz RAM.

to the PARR model, the predicted high-risk patients have less number of prior-admission for all the subpopulations, which makes it considerably harder to predict.

In addition, based on the population profile of the top 1000 risk segments (Table A.2), the model (Any-Acute) predicts more patients with chronic obstructive pulmonary disease (COPD), depression, diabetes, coronary heart disease (CHD), congestive heart failure (CHF) and smaller average age as high-risk, than the CPM and the PARR models did. On the other hand, cancer that is highly predictable and manageable has a smaller share among the high-risk patients.

Because sensitivity and precision vary across risk scores, and the costs of interventions or readmissions are not zero, it is better to define a profit function. However, owing to a lack of necessary variables for mapping costs, this was not considered

Finally, additional work is necessary to improve the comorbidity risk scoring and to dynamically adjust for temporal patterns.

# 5. Conclusion 

In conclusion, the ERMER provides a generic approach in modelling readmission emphasising on robustness and feature discovery. Moreover, based on a large number of iterations for performance assessment across different settings, the ERMER maintained its high discriminatory performance. Consequently, the ERMER can bring a significant improvement to the current decision support system in use, improve care quality and reduce the costs.

Future research should aim to better adjust for comorbidity risk and temporal patterns.

# ACCEPTED MANUSCRIPT 

## Summary Points

What is already known?

- Avoidable emergency hospital admission can be an indicator of suboptimal care quality.
- Identification of high-risk patients for intervention can substantially improve care quality and reduce costs.
- Designing features and developing predictive models that can adjust continuously to a fast-changing health care system and population characteristics are very challenging.

What this paper adds?

- The optimised ensemble model of sub-populations was proved to increasingly improve the risk model.
- The combination of using a nonlinear Bayesian model and applying a preprocessing framework for feature generation and selection can effectively create a highly adaptable predictive model.
- The ensemble of generative models is a new effective way to predicts patients with harder predictability, such as patients with chronic conditions and patients with fewer prior hospitalisation records.


## Authors' Contributions

MM preprocessed data, designed the model, drafted the manuscript and submitted the article. TC and SC provided valuable insights in the design and interpretation of results, revised the article critically and issued the final approval.

## Acknowledgements

This work was supported by the HSCMG at the University of Westminster.

## Conflicts of Interest

Authors do not have any conflicts of interest or financial interests to declare.

# ACCEPTED MANUSCRIPT 

DH, Dec. 2006. Combined predictive model - final report and technical documentation. [Retrieved 02.09.2016].

URL http://www.kingsfund.org.uk
DH, Aug. 2011. Risk stratification and next steps with DH risk prediction tools: Patients at risk of re-hospitalisation and the combined predictive model. [Retrieved 02.09.2016].
URL https://www.gov.uk
DH, Apr. 2012. Long term conditions compendium of information (third edition). [Retrieved 02.09.2016].

URL https://www.gov.uk
DH, 2013. Business case: for the health and care modernisation transition programme. [Retrieved 02.09.2016].

URL https://www.gov.uk
HSCIC, Sep 2010. Hes data dictionary. [Retrieved 02.09.2016].
URL http://www.hscic.gov.uk
HSCIC, Dec. 2013. Hospital episode statistics, emergency readmissions to hospital within 28 days of discharge - financial year 2011/12. [Retrieved 02.09.2016].
URL http://www.hscic.gov.uk
HSCIC, Jan. 2016a. Hospital episode statistics (HES). [Retrieved 02.09.2016].
URL http://www.hscic.gov.uk
HSCIC, 2016b. Summary hospital-level mortality indicator. [Retrieved 02.09.2016].
URL http://www.hscic.gov.uk
HSCIC, 2016c. What HES data are available? [Retrieved 02.09.2016].
URL http://www.hscic.gov.uk
Microsoft Research, 2016. Infer.net software solution. [Retrieved 02.09.2016].
URL http://research.microsoft.com
NHS, Oct. 2011. Scottish patients at risk of readmission and admission (SPARRA) - version 3 (developing risk prediction to support preventative and anticipatory care in scotland). [Retrieved

# ACCEPTED MANUSCRIPT 

02.09.2016].
URL http://www.isdscotland.org
NHS, 2013. NHS england publishes CCG funding allocations for next two years following adoption of new formula. [Retrieved 02.09.2016].
URL http://www.england.nhs.uk
NHS, Oct. 2014. Five year forward view. [Retrieved 02.09.2016].
URL https://www.england.nhs.uk
Nuffield Trust, Aug. 2012. Predicting risk of hospital readmission with PARR-30. [Retrieved 02.09.2016].

URL http://www.nuffieldtrust.org.uk
ONS, Jul. 2014. Quality and methodology information: Mortality statistics in england and wales. [Retrieved 02.09.2016].
URL http://www.ons.gov.uk
The King's Fund, 2016. Predicting and reducing re-admission to hospital. [Retrieved 02.09.2016].
URL http://www.kingsfund.org.uk
Mesgarpour, M., Chaussalet, T., Chahed, S., June 2016a. Risk modelling framework for emergency hospital readmission, using hospital episode statistics inpatient data. In: 2016 IEEE 29th International Symposium on Computer-Based Medical Systems (CBMS). pp. 219-224.

Mesgarpour, M., Chaussalet, T., Worrall, P., Chahed, S., June 2016b. Predictive risk modelling for integrated care: A structured review. In: 2016 IEEE 29th International Symposium on ComputerBased Medical Systems (CBMS). pp. 42-47.

Mihaylova, B., Briggs, A., O'Hagan, A., Thompson, S. G., 2011. Review of statistical methods for analysing healthcare resources and costs. Health economics 20 (8), 897-916.

Minka, T. P., 2001a. Expectation propagation for approximate bayesian inference. In: Proceedings of the Seventeenth conference on Uncertainty in artificial intelligence. Morgan Kaufmann Publishers Inc., pp. 362-369.

Minka, T. P., Sep. 2001b. A family of algorithms for approximate bayesian inference. [Retrieved 02.09.2016].

URL http://research.microsoft.com
Mullins, I. M., Siadaty, M. S., Lyman, J., Scully, K., Garrett, C. T., Miller, W. G., Muller, R., Robson, B., Apte, C., Weiss, S., et al., 2006. Data mining and clinical data repositories: Insights from a 667,000 patient data set. Computers in biology and medicine 36 (12), 1351-1377.

Murphy, K. P., 2012. Machine learning: a probabilistic perspective. MIT press.
Nicholl, J., 2007. Case-mix adjustment in non-randomised observational evaluations: the constant risk fallacy. Journal of epidemiology and community health 61 (11), 1010-1013.

Nilsson, J., Ohlsson, M., Thulin, L., Höglund, P., Nashef, S. A., Brandt, J., 2006. Risk factor identification and mortality prediction in cardiac surgery using artificial neural networks. The Journal of thoracic and cardiovascular surgery 132 (1), 12-19.

Nordhausen, K., 2009. The Elements of Statistical Learning: Data Mining, Inference, and Prediction, Second Edition by Trevor Hastie, Robert Tibshirani, Jerome Friedman. Blackwell Publishing Ltd.

Opitz, D., Maclin, R., 1999. Popular ensemble methods: An empirical study. Journal of Artificial Intelligence Research, 169-198.

Paton, F., Wilson, P., Wright, K., 2014. Predictive validity of tools used to assess the risk of unplanned admissions: A rapid review of the evidence. [Retrieved 02.09.2016].
URL https://www.york.ac.uk
Peelen, L., de Keizer, N. F., de Jonge, E., Bosman, R.-J., Abu-Hanna, A., Peek, N., 2010. Using hierarchical dynamic bayesian networks to investigate dynamics of organ failure in patients in the intensive care unit. Journal of biomedical informatics 43 (2), 273-286.

Pencina, M. J., D'Agostino, R. B., D'Agostino, R. B., Vasan, R. S., 2008. Evaluating the added predictive ability of a new marker: from area under the ROC curve to reclassification and beyond. Statistics in medicine 27 (2), 157.

Quan, H., Sundararajan, V., Halfon, P., Fong, A., Burnand, B., Luthi, J.-C., Saunders, L. D., Beck, C. A., Feasby, T. E., Ghali, W. A., 2005. Coding algorithms for defining comorbidities in ICD-9-CM and ICD-10 administrative data. Medical care, 1130-1139.

Raftery, J., Roderick, P., Stevens, A., 2005. Potential use of routine databases in health technology assessment. Health Technology Assessment 9 (20), 1-106.

Reimer, A. P., Milinovich, A., Madigan, E. A., 2016. Data quality assessment framework to assess electronic medical record data for use in research. International journal of medical informatics $90,40-47$.

Rokach, L., 2005. Ensemble methods for classifiers. In: Data mining and knowledge discovery handbook. Springer, pp. 957-980.

Rokach, L., 2010. Pattern classification using ensemble methods. Vol. 75. World Scientific.
Russell, S. J., Norvig, P., 2002. Artificial intelligence: a modern approach (International Edition). \{Pearson US Imports \& PHIPEs\}.

Sammut, C., Webb, G. I., 2011. Encyclopedia of machine learning. Springer Science \& Business Media.

Sewell, M., 2008. Ensemble learning. RN 11 (02).
Singer, J. D., Willett, J. B., 2003. Applied longitudinal data analysis: Modeling change and event occurrence. Oxford university press.

Song, X., Mitnitski, A., Cox, J., Rockwood, K., 2004. Comparison of machine learning techniques with classical statistical models in predicting health outcomes. Stud Health Technol Inform 107 (Pt 1), 736-40.

Steyerberg, E. W., Vickers, A. J., Cook, N. R., Gerds, T., Gonen, M., Obuchowski, N., Pencina, M. J., Kattan, M. W., 2010. Assessing the performance of prediction models: a framework for some traditional and novel measures. Epidemiology (Cambridge, Mass.) 21 (1), 128.

Timmins, N., may 2013. Never again? the story of the health and social care act 2012.
Vapnik, V. N., Vapnik, V., 1998. Statistical learning theory. Vol. 1. Wiley New York.

Walpole, R., Myers, R., Myers, S., Ye, K., 2014. Probability and Statistics for Engineers and Scientists. Pearson.

Yang, Y., Webb, G. I., Wu, X., 2005. Discretization methods. In: Data mining and knowledge discovery handbook. Springer, pp. 113-130.

Zhou, Z.-H., 2012. Ensemble methods: foundations and algorithms. CRC press.

# ACCEPTED MANUSCRIPT 

Algorithm 1 The ensemble modelling algorithm
![img-5.jpeg](img-5.jpeg)

# A. Additional Analyses Settings and Outputs 

## Table A. 1

The risk bands statistics of the ERMER for different test sub-samples.



Table A. 2 The top risk segments profile of the predicted high-risk patients across test sub-samples.

|  Risk
Seg. ${ }^{a}$ | Model
Risk ${ }^{b}$ | Sub-population | Min
Risk ${ }^{b}$ | Asthma
c | COPD
d | Depress.
e | Diab.
f | Hyper.
g | Cancer
h | CHD ${ }^{i}$ | CHF ${ }^{j}$ | Avg.
Age $^{k}$ | Avg.
LoS ${ }^{l}$ | 5-9
Meds $^{m}$ | 10+ Meds $^{n}$  |

${ }^{a}$ The top predicted risk segment. ${ }^{\mathrm{b}}$ The minimum predicted risk in the segment. ${ }^{\text {c }}$ The percentage of patients with a history of Asthma diagnosis (ICD-10: J45-J46). ${ }^{\text {d }}$ The percentage of patients with a history of Chronic Obstructive Pulmonary Disease (COPD) diagnosis (ICD-10: J20, J41-J44, J47). ${ }^{\text {e }}$ The percentage of patients with a history of Depression diagnosis (ICD-10: I10-I15). ${ }^{\text {f }}$ The percentage of patients with a history of Diabetes diagnosis (ICD-10: E10.0, E10.1, E10.6, E10.8, E10.9, E11.0, E11.1, E11.6, E11.8, E11.9, E12.0, E12.1, E12.6, E12.8, E12.9, E13.0, E13.1, E13.6, E13.8, E13.9, E14.0, E14.1, E14.6, E14.8, E14.9, E10.2-E10.5, E10.7, E11.2-E11.5, E11.7, E12.2-E12.5, E12.7, E13.2-E13.5, E13.7, E14.2-E14.5, E14.7). ${ }^{\text {g }}$ The percentage of patients with a history of Hypertension diagnosis (ICD-10: I10-I15, I27, I6, I87.0, I87, I97, K76.6, H35.0, R03, O13, O14, O16, O10, G93.2, H40.0, P202, P293). ${ }^{\text {h }}$ The percentage of patients with a history of Cancer diagnosis (ICD-10: C00-D49). ${ }^{\text {i }}$ The percentage of patients with a history of Coronary Heart Disease (CHD) diagnosis (ICD-10: I20-I25). ${ }^{\text {j }}$ The percentage of patients with a history of Congestive Heart Failure (CHF) diagnosis (ICD-10: I09.9, I11.0, I13.0, I13.2, I25.5, I42.0, I42.5-I42.9, I43.x, I50.x, P29.0). ${ }^{\text {k }}$ The average age of patients at the trigger event. ${ }^{\text {l }}$ The average length of stay of patient at the trigger event. ${ }^{\text {m }}$ The percentage of patients with 5-9 medication prescription. ${ }^{\text {n }}$ The percentage of patients with 10+ medication prescription.

Table A. 3
The average importance of features and average weights of features in sub-models.


# ACCEPTED MANUSCRIPT 


# Highlights: 

- Using a Bayes Point Machine method, which has no hyper-parameter and is adaptive to changes in prior distributions of features, to predict the risk of emergency readmission to hospitals in the English National Health Service.
- Using an ensemble model to improve the performance of risk prediction and allow sensitivity and precision to be adjusted based on a cost function.
- Using a framework to collect a pool of features.
- Using a minimal amount of administrative data to capture the underlying structure better.

Graphical Abstracts (for review)

![img-6.jpeg](img-6.jpeg)

# Generating Features

- **Exploratory Factor Analysis**
- **Likelihoods Review**
- **Generating Feature Pool**
- **Excluding Near Zero Variance**
- **Excluding Highly Linearly Correlated**
- **Random Forest Rank**
- **SVM Rank**
- **Select Features**

# Bayes Point Machine

- **Features**
  - **Gamma**
  - **Rate's Rate**
  - **Gamma**
  - **Common Precision**
  - **Dividend**
  - **Mean = 0**
  - **Weight Precision**
  - **Normal**
  - **Weight**
- **Gamma**
- **Intercept**
- **Gamma**
- **Intercept**
- **Gamma**

# Ensemble Model

- **Main Model**
- **Conditional: Prior 12-Month Acute Spells**
- **Conditional: Age**
- **None**
- **<65**
- **Optimisation Cost Function: (Δ ACC + Δ ROC + Δ RMSE + Δ SAR) / 4**
- **None**
- **None**
- **1+**
- **1+**
- **1+**
- **1+**

- **Conditional: Prior Spells**
- **Conditional: Prior 12-Month Operations**