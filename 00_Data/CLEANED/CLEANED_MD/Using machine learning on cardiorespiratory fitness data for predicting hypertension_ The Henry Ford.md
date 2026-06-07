# RESEARCH ARTICLE 

## Using machine learning on cardiorespiratory fitness data for predicting hypertension: The Henry Ford Exercise Testing (FIT) Project

Sherif Sakr ${ }^{1,2,7 *}$, Radwa Elshawi ${ }^{4,7}$, Amjad Ahmed ${ }^{1,2}$, Waqas T. Qureshi ${ }^{5}$, Clinton Brawner ${ }^{3}$, Steven Keteyian ${ }^{3}$, Michael J. Blaha ${ }^{6}$, Mouaz H. Al-Mallah ${ }^{1,2,3}$


#### Abstract

1 King Saud bin Abdulaziz University for Health Sciences, Riyadh, Saudi Arabia, 2 King Abdullah International Medical Research Center, Riyadh, Saudia Arabia, 3 Heart and Vascular Institute, Henry Ford Hospital System, Detroit, MI, United States of America, 4 Princess Nourah bint Abdulrahman University, Riyadh, Saudi Arabia, 5 Wake Forest School of Medicine, Medical Center Boulevard, Winston-Salem, NC, United States of America, 6 Johns Hopkins Medicine, Baltimore, Maryland, United States of America, 7 University of Taru, Taru, Estonia


* sakrs@ksau-hs.edu.sa


## Abstract

This study evaluates and compares the performance of different machine learning techniques on predicting the individuals at risk of developing hypertension, and who are likely to benefit most from interventions, using the cardiorespiratory fitness data. The dataset of this study contains information of 23,095 patients who underwent clinician- referred exercise treadmill stress testing at Henry Ford Health Systems between 1991 and 2009 and had a complete 10-year follow-up. The variables of the dataset include information on vital signs, diagnosis and clinical laboratory measurements. Six machine learning techniques were investigated: LogitBoost (LB), Bayesian Network classifier (BN), Locally Weighted Naive Bayes (LWB), Artificial Neural Network (ANN), Support Vector Machine (SVM) and Random Tree Forest (RTF). Using different validation methods, the RTF model has shown the best performance (AUC $=0.93$ ) and outperformed all other machine learning techniques examined in this study. The results have also shown that it is critical to carefully explore and evaluate the performance of the machine learning models using various model evaluation methods as the prediction accuracy can significantly differ.

## Introduction

Hypertension is a major condition that can lead to many severe illnesses such as stroke and heart disease [1]. Risk assessment of the disease is significantly complicated and depends on many factors and environmental conditions that can significantly raise blood pressure readings. According to the World Health Organization (WHO), high blood pressure causes one in every eight deaths and therefore Hypertension is considered the third leading killer in the world [2]. There are around a billion of hypertensive patients around the word and around four million patients die every year. In the Middle Eastern region, cardiovascular disease and stroke are the main cause of death and illness. They resulted in $31 \%$ of deaths and currently

Funding: Funding was provided by King Abdullah International Medical Research Center. Funding grant number SP16/100 to SS. The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript.

Competing interests: The authors have declared that no competing interests exist.
hypertension affects around $26 \%$ of the adult population in the region [3-6]. Currently there is no clear causes for high blood pressure however there are several factors and conditions may play an important role in its development such as smoking, obesity, lack of physical activity, salty diet, stress, age, family history, chronic kidney disease and thyroid disorders. The main goal of intervention is to reduce blood pressure and control the heart disease.

The Henry Ford Exercise Testing (FIT) Project [7] is a retrospective cohort that includes the information of 69,981 patients who had undergone physician referred treadmill stress testing at Henry Ford Hospital System in Detroit, MI from January 1, 1991- May 28, 2009. Briefly, the study population was limited to patients who are over the age of 18 years of age at the time of stress testing and excluded patients undergoing modified or non-Bruce protocol [8] stress tests. Information regarding the patient's medical history, demographics, medications, cardiovascular disease risk factors were obtained at the time the tests were done by nurses and exercise physiologists, as well as searches through the electronic medical records. All study patients underwent clinically indicated treadmill stress testing utilizing the standard Bruce Protocol. All stress tests were performed in accordance with standard American College of Cardiology/ American Heart Association Guidelines [9]. For the full details of The FIT Project, we refer the reader to [7]. Several studies [10-13] have used conventional statistical techniques to predict various medical outcomes using the FIT project data.

Machine learning (ML) [14, 15] is a modern data analysis technique with the unique ability to learn and improve its performance without being explicitly programmed and without human instruction. The main goal of supervised machine learning classification algorithms [16] is to explain the dependent variable in terms of the independent variables. The algorithms get adjusted based on the training sample and an error signal. ML algorithms automatically scan and analyze all predictor variables in a way that prevents overlooking any potentially important predictor variables even if it was unexpected. Therefore, ML is acknowledged as a powerful tool which dramatically changes accessibility of science, research and practice in all domains [17]. Medicine and Healthcare are no different [18-21]. In this study, we investigate and compare the performance of several machine learning techniques that use cardiorespiratory fitness data for predicting individuals at risk of developing hypertension who are most likely to benefit from interventions. We evaluate and compare six well-known machine learning techniques to come up with the best model to predict the risk of hypertension. The models have been evaluated using different metrics. The machine learning techniques used in this study are: LogitBoost (LB), Bayesian Network classifier (BN), Locally Weighted Naive Bayes (LWB), Artificial Neural Network (ANN), Support Vector Machine (SVM) and Random Tree Forest (RTF). Different validation techniques and evaluation metrics are compared and reported.

## Materials and methods

## Henry Ford FIT dataset

The dataset was collected from patients who underwent treadmill stress testing by physician referrals at Henry Ford Affiliated Hospitals in metropolitan Detroit, MI in the U.S. The FIT Project data has been obtained from the electronic medical records, administrative databases, and the linked claim files and death registry of the hospital [7]. Study participants underwent routine clinical treadmill exercise stress testing using the standard Bruce protocol between January 1st, 1991 and May 28th, 2009. The day the treadmill test was performed served as the baseline for this study. The exercise stress test would be terminated by the supervising clinician if the patient had exercise-limiting chest pain, shortness of breath, or other limiting symptoms independent of the achieved heart rate. Furthermore, testing could also be terminated early at

Table 1. Dataset description.


https://doi.org/10.1371/journal.pone.0195344.t001
the discretion of the supervising clinician for significant arrhythmias, abnormal hemodynamic responses, diagnostic ST-segment changes, or if the participant was unwilling or unable to continue [22].

The total number of patients included in this study is $(\mathrm{n}=23,095)$. The data set includes 43 attributes containing information on vital signs, diagnosis and clinical laboratory measurements. The baseline characteristics of the included cohort are shown in Table 1. The data set contains 23,095 individuals ( 12,694 males ( $55 \%$ ) and 10,401 ( $45 \%$ ) females) with ages that range between 17 and 96 . Half of the patients have a family history of cardiovascular diseases. During the 10 -years follow-up, around $35 \%$ of the patients experienced hypertension. Male hypertension patients represent around $55 \%$ of the total hypertension patients while female patients represent around $44 \%$ of the total hypertension patients.

# Data preprocessing 

One of the main steps that affects the performance and quality of prediction of machine learning models is data quality and data preprocessing. Data preprocessing includes handling missing values, smooth noisy data, identify or remove outliers, normalization, transformation, etc. Therefore, several steps have been applied to handle some issues on the dataset.

- Outliers: a value of an attribute is considered as an outlier if it deviates from the expected value for this attribute. Outliers has been handled using inter-quartile range (IQR). The IQR

identifies outliers in the dataset by identifying over ranging data in data. The $I Q R$ is a good choice for handling the outliers since the dataset used in this study is nearly symmetric means that its median equals its midrange. The $I Q R$ is evaluated as $I Q R=Q 3-Q 1$ where $Q 3$ and $Q 1$ are the upper and lower quartiles, respectively. Outliers are records that fall below $Q 1-\left(1.5^{\circ} I Q R\right)$ or above $Q 3+\left(1.5^{\circ} I Q R\right)$. The number of records identified as outliers or extreme values and has been removed in the dataset used in this work is 192 records.

- Missing values: The only attribute that has missing values is Peak Diastolic blood pressure and the number of individuals with missing Peak Diastolic blood pressure is 72 . All the values for this attribute are replaced by the mean value of this attribute.
- Discretization: Aims to reduce the number of values for continuous attributes. This is done by splitting the range of the continuous attribute into intervals. Discretization reduces the time needed to build the prediction model and improve the prediction results [23]. The following attributes have been discretized: Age, METS, Resting Systolic blood pressure, Resting Diastolic blood pressure, The Percentage of Heart Rate Achieved, Peak Heart Rate and Peak Diastolic blood pressure.
- Sampling: The dataset used in this study consists of 23,095 with 8,090 patients with experienced hypertension and the rest did not. The most common metric used to evaluate machine learning techniques is accuracy. This measure does not work properly when the data is imbalanced (the variance between patients who experienced hypertension and those who did not experience hypertension is considerably high). However, the nature of our prediction problem requires a high rate of correct detection of patients who are at high risk of developing hypertension. In general, there are two different method to address the imbalanced dataset and obtain a balanced dataset (the number of patients who experienced hypertension is close to the number of patients who did not experienced hypertension). The first method is over-sampling the minority class (patients who experienced hypertension) [24] and the second method is under-sampling the majority class [25]. In this study, we used both under-sampling and over-sampling to handle the imbalanced data problem and compare the performance of both techniques. We used the Synthetic Minority Over-sampling (SMOTE) Technique [26]. It is an over-sampling techniques in which the minority class is over-sampled by creating "synthetic" examples rather than by over-sampling with replacement. SMOTE selects the minority class samples (patients experienced hypertension) and creates "synthetic" samples along the same line segment joining some or all k nearest neighbors belonging to the minority class. More precisely, the over-sampling is done as follows:
- Take sample of the dataset and find its nearest neighbors.
- To create a synthetic data point, take the vector between a one of the data points $P$ in the sample dataset and one of $P$ k-nearest neighbors.
- Multiply this vector by a random number $x$ which lies between 0 and 1 .
- Add this to $P$ to create the new synthetic data point.

The percentage of SMOTE instances created in our experiment is $30 \%$ (2,427 records from the minority class). In addition, we used the spread Sub-sample instance method as an under-sampling technique [25]. The spread sub-sample method outputs a random sub-sample of a dataset. This instance method allows you to mention the maximum "spread" between the minority and majority classes. You may specify that there is at most 2:1 difference in the frequency of the majority and minority classes. In this study, we used this method to maintain equal ratio between the majority and minority classes.

# Feature selection 

Feature selection is an essential part of building a good prediction model for many reasons [27]. For example, it implies some degree of cardinality reduction by reducing the number of attributes used to build the model. That can be done by only choosing the most important attributes that improves the prediction accuracy. Another advantage of the feature selection process is reducing the resources (time and space) needed to build the model.

In this study, we used an automated R-based ML feature selection algorithm that ranks the attributes based on their Information Gain [28], which evaluates the importance of an attribute by measuring the entropy gain with respect to the outcome, and then ranks the attributes by their individual evaluations [27]. Only attributes that have information gain $>0$ were subsequently used in building the machine learning models considered in this study.

## Machine learning classification models

Using the data of this study, we evaluated and compared six different classification techniques for predicting the Hypertension outcome: Artificial Neural Network (ANN), LogitBoost (LB), Locally Weighted Naive Bayes (LWB), Random Tree Forest (RTF), Sup- port Vector Machine (SVM) and Bayesian Network (BN).

Artificial Neural Network (ANN) [29] attempts to mimic the human brain to learn complex tasks. It is modeled as interconnected group of nodes in a way which is like the vast network of neurons in the human brain. Each of the network receives inputs from another source, combines them in some way, performs a generally nonlinear operation on the result and outputs the result. We train the Neural Networks with gradient descent back-propagation. We vary the number of hidden units $\{1,2,4,8\}$ and the momentum $\{0,0.2,0.5\}$.

LogitBoost (LB) [30] is a boosting algorithm that was originally developed to improve the classification performance of many weak classifiers. The LogitBoost classifier is based on AdaBoost procedure [30]. The adaBoost procedure trains the classifier on weighted versions of the training data and assigns higher weights for those training records that are misclassified. Such procedure is done for a sequence of weighted samples. Then the final classifier is defined to be a liner combination of the classifiers from each stage. LogiBoost uses an adaptive Newton algorithm to fit an adaptive multiple logistic regression model. LogiBoost is superior in handling noisy data.

Locally Weighted Naive Bayes (LWB) [31] is an instance-based learner that performs classification by comparing a test instance to a data set of pre-classified instances. The main assumption is that similar instances should have similar classifications. LWB is considered an enhancement of Naive Bayes where a linear regression model is fit to the data based on a weighting function centered on the instance for which a prediction is to be generated.

Bayesian Network (BN) [32] is a simple probabilistic classifier that is considered a generalization of the Naive Bayes classifier that removes the dependencies between variables. BN is designed for modeling under uncertainty where the nodes represent variables and arcs represent direct connections between them. BN model allows probabilistic beliefs about the variables to be updated automatically as new information becomes available. We used different search algorithms K2 [33], Hill Climbing [34], Repeated Hill Climber [35], LAGD Hill Climbing [36], TAN [37], Tabu search [38] and Simulated annealing [38].

Support Vector Machine (SVM) [39] represents the instances as a set of points of 2 types in $N$ dimensional place and generates a $(N-1)$ dimensional hyperplane to separate those points into 2 groups. SVM attempts to find a straight line which separates those points into 2 types and is situated as far as possible from all those points. Training the SVM is done using Sequential Minimal Optimization algorithm [15]. We use Weka implementation of SMO [40].

We test SVM using polynomial, normalized polynomial, puk kernels and vary the complexity parameter $\{0.1,10$, and 30$\}$. The value of the complexity parameter controls the tradeoff between fitting the training data and maximizing the separating margin.

Random Tree Forest (RTF) [41, 42] is a classification algorithm that works by forming multitude decision trees at training and at testing it outputs the class that is the mode of the classes (classification). Decision tree works by learning simple decision rules extracted from the data features. The deeper the tree, the more complex the decision rules and the fitter the model. Random decision forests overcome the problem of over fitting of the decision trees. All ML algorithms have been conducted using Weka Software (Version 3.8) (http://www.cs.waikato.ac. $\mathrm{nz} / \mathrm{ml} / \mathrm{weka} /$ ) and R-based ML packages (Version 3.3.1) (https://www.r-project.org/).

# Model evaluation and validation 

To evaluate our models, we used two main methods: the hold out [43] method and the 10 -fold cross-validation method [44]. In principle, the main idea of the holdout method is to split the data into training set and test set. The training set is used by the classifier for the training process and the testing set is used to estimate the prediction error rate of the classifier after learning. For the holdout method, we have been using two data splits:

1. Training with $70 \%$ of the dataset and Testing with $30 \%$ of the dataset.
2. Training with $80 \%$ of the dataset and Testing with $20 \%$ of the dataset.

The main idea of the 10 -fold cross validation is to partition the data set into 10 partitions. Each time one of the 10 partitions are used for testing the model and the other 9 partitions are used for training the model. So, each instance in the data set is used once in testing and 9 times in training. All results of the different metrics are then averaged to return the result. In general, the main advantage of the 10 -fold cross-validation evaluation method is that it has a lower variance than a single hold-out set evaluator. It reduces this variance by averaging over 10 different partitions, therefore, it is less sensitive to any partitioning bias on the training or testing data.

In practice, the outcome of any binary classifier is one of the following four results:

- True Positive (TP) refers to the number of high risk patients who are classified as high risk.
- False Negative (FN) refers to the number of high risk patients who are classified as low risk patients.
- False Positive (FP) refers to the number of low risk patients who are classified as high-risk patients.
- False Negative (FN) refers to the number of low risk patients who are classified as low risk patients.

For all classifiers, the following evaluation metrics were calculated:

- Sensitivity: True Positive recognition rate

$$
\text { Sensitivity }=\mathrm{TP} /(\mathrm{TP}+\mathrm{FN})
$$

- Specificity: True Negative recognition rate

$$
\text { Specificity }=\mathrm{TN} /(\mathrm{TN}+\mathrm{FP})
$$

- Precision: It represents the percentage of tuples that the classifier has labeled as positive are actually positive

$$
\text { Precision }=\mathrm{TP} /(\mathrm{TP}+\mathrm{FP})
$$

- F-score: It represents the harmonic mean of precision and sensitivity

$$
\text { F-score }=2 * \mathrm{TP} /\left(2 * \mathrm{TP}+\mathrm{FP}+\mathrm{FN}\right)
$$

- Root Mean Squared Error (RMSE): It is defined as the square root of the mean square error that measures the difference between values predicted by the model and the actual values observed, where $y^{\prime}$ is a vector of $n$ predictions and $y$ is the vector of $n$ observed (actual) values
- Receiver Operating Characteristic (ROC) Curve: It is a way to quantify the diagnostic value of a test over its whole range of possible cutoffs for classifying patients as positive vs. negative [45]. In each possible cutoff, the true positive rate and false positive rate is calculated as the $X$ and $Y$ coordinates in the ROC Curve.


# Results 

Fig 1 illustrates the flowchart of the training and testing of the ML based techniques for predicting the risk of hypertension using the cardiorespiratory fitness data. First, dataset is preprocessed then SMOTE is applied on the dataset by creating synthetic examples of the class "yes" (patients experienced hypertension). The percentage of SMOTE instances created is $30 \%$. Next, we apply the feature selection process where we rank the variables of the dataset according to their information gain and select the subset with the highest gain. Finally, we examine different machine learning models and evaluate their performance using the two main methods, hold out ( $70 / 30$ and 80/20) and 10 -fold cross-validation, based on different evaluation metrics.

As an outcome of the feature selection process, using the information gain ranking criteria, 13 attributes out of 49 were selected according to their information gain rank [28] for the Hypertension prediction. Age was the highest ranked feature for hypertension prediction. For our models, we selected the top ranked attributes that do not clinically contain collinear information: Age, METS, Resting Systolic Blood Pressure, Peak Diastolic Blood Pressure, Resting Diastolic Blood Pressure, HX Coronary Artery Disease, Reason for test, History of Diabetes, Percentage HR achieved, Race, History of Hyperlipidemia, Aspirin Use, Hypertension response (See Fig 2).

We compared the impact of using SMOTE and Spread Subsample methods. We applied them with different percentage of synthetic examples. Fig 3 shows the area under the curve of six different models trained using LogitBoost (LB), Bayesian Network classifier (BN), Locally Weighted Naive Bayes (LWB), Artificial Neural Network (ANN), Support Vector Machine (SVM) and Random Tree Forest (RTF) with $0 \%, 10 \%$ and $30 \%$ of synthetic examples created using the SMOTE and evaluated using the 10 -fold cross validation method. The results show that the performance of the RTF and SVM models using SMOTE has shown great improvement. The RTF and SVM achieve AUC of 0.91 and 0.71 respectively using the sampled dataset with $30 \%$ synthetic examples created in comparison to 0.9 and 0.57 respectively using the dataset without sampling. In contrast, the LWB and BN models show no improvement using

![img-0.jpeg](img-0.jpeg)

Fig 1. A flowchart of our experimental process.
https://doi.org/10.1371/journal.pone.0195344.g001

SMOTE achieving both AUC of 0.7. LB and ANN models have shown a slight improvement using SMOTE by achieving AUC of 0.69 and 0.63 respectively without sampling and AUC of 0.7 and 0.67 using SMOTE with $30 \%$ created synthetic examples. In Spread Subsample technique, all the minority class instances ( 8015 instances) are used while some instances of the majority class are removed randomly until both classes are equally balanced.

![img-1.jpeg](img-1.jpeg)

Fig 2. The information gain ranking of the attributes of the dataset.
https://doi.org/10.1371/journal.pone.0195344.g002

Fig 4 presents the AUC of six different models trained using LB, BN, LWB, ANN, SVM and RTF. All models are evaluated using 10 -fold cross validation. The results show that all models without using the Spread Subsample techniques outperforms the ones with sampling except for the SVM model. The RTF without sampling achieves 0.9 and dropped down dramatically to 0.68 using Spread Sampling. The SVM has shown a slight improvement using Spread Subsample by achieving AUC of 0.65 with sampling compared to 0.57 without sampling.

Table 2 presents the performance of the SVM using different kernels (polynomial kernel, normalized polynomial kernel and puk kernel) and complexity parameters (C) ( $0.1,10$ and 30) is tested and evaluated using 10 -fold cross validation. The results show that the AUC increased as the complexity parameter increased up to 30 . In addition, the SVM using puk kernel outperforms the SVM using other kernels achieving AUC of 0.71 . The results show that using that using that puk kernel with complexity parameter equals 0.1 achieves the highest AUC of 0.59 evaluated using 10 -fold cross validation.

![img-2.jpeg](img-2.jpeg)

**Fig 3. AUC of different models with different percentage of synthetic examples created using SMOTE evaluated using 10-fold cross validation.**

https://doi.org/10.1371/journal.pone.0195344.g003

![img-3.jpeg](img-3.jpeg)

**Fig 4. AUC of the different ML models using Spread Subsample technique.**

https://doi.org/10.1371/journal.pone.0195344.g004

**Table 2. Comparison of the performance of Support Vector Machine (SVM) classifier with sampling using polynomial, normalized polynomial and puk kernels using complexity parameters 0.1, 10 and 30 using 10-fold cross validation using SMOTE.**


https://doi.org/10.1371/journal.pone.0195344.t002

Table 3. Comparison of the performance of Artificial Neural Networks (ANN) classifier with gradient descent back-propagation using hidden units $\{1,2,4,8\}$ and the momentum $\{0,0.2,0.5\}$ using 10 -fold cross validation using SMOTE.


https://doi.org/10.1371/journal.pone.0195344.t003

Table 3 presents the performance of Neural Networks with gradient descent back-propagation using hidden units $\mathrm{H}={1,2,4,8}$ and the momentum $\mathrm{M}={0,0.2,0.5}$ using SMOTE evaluated using 10 -fold cross validation. The number of hidden units and momentum rate that gives better AUC value is considered here. We achieve the highest AUC of 0.64 using $\mathrm{H}=4$ and $\mathrm{M}=0$. The performance of the Naïve Network Classifier using SMOTE evaluated using 10 -fold cross validation is shown in Table 4. Seven different search algorithms (K2, Hill Climbing, Repeated Hill Climber, LAGD Hill Climbing, TAN, Tabu and Simulated Annealing) are evaluated as shown in Table 4. Bayesian Network classifier using Simulated Annealing algorithm achieves the highest AUC value of 0.70 .

Fig 5 shows the AUC curves of the different models using the balanced dataset which were generated using SMOTE and validated using 10 -fold cross-validation method. Figs 6 and 7 show the ROC curves of the different models using the balanced dataset which were generated using SMOTE and validated using two splits of the holdout methods: 70/30 and 80/20, respectively. Among the different evaluation methods, the Random Tree Forest (RTF) model achieves the highest AUC using the 10 -fold cross-validation method (0.93), holdout method $70 / 30(0.83)$ and holdout method $80 / 20(0.88)$.

Table 5 summarizes the performance of the different machine learning techniques on sampled data using SMOTE using 10 -fold cross validation while Tables 6 and 7 summarize the performance of the different models on sampled data using SMOTE evaluated using the two splits of the holdout methods $70 / 30$ and $80 / 20$, respectively. For each metric (row) in the tables, we highlighted the highest value in bold font and underlined the lowest value.

We have evaluated the different models using different methods and various evaluation metrics. In general, the Random Tree Forest (RTF) model significantly outperformed all other models for the Specificity (91.7\%), Precision (81.69\%), F-score (86.7\%), AUC (0.93) and Root Mean Squared Error (0.34) metrics evaluated using 10 -fold cross validation.

Table 4. Comparison of the performance of Bayesian Network classifier (BN) using different search algorithms K2, Hill Climbing, Repeated Hill Climber, LAGD Hill Climbing, TAN, Tabu and Simulated Annealing using 10 -fold cross validation using SMOTE.


https://doi.org/10.1371/journal.pone.0195344.t004

![img-4.jpeg](img-4.jpeg)

**Fig 5. AUC Curves for the Different Machine Learning Models using SMOTE evaluated using 10-fold cross-validation.**

<https://doi.org/10.1371/journal.pone.0195344.g005>

- **Sensitivity metric**: The ANN and LB showed very comparable performance and came in the second place by achieving 30.06% and 31.28% respectively.
- **Specificity metric**: The LB and ANN showed a very comparable performance and came in the first place achieving 88.56% and 88% respectively. The SVM showed the worst performance (78.97%).

![img-5.jpeg](img-5.jpeg)

**Fig 6. AUC Curves for the Different Machine Learning Models using SMOTE and evaluated using holdout (70/30).**

<https://doi.org/10.1371/journal.pone.0195344.g006>

![img-6.jpeg](img-6.jpeg)

**Fig 7. AUC Curves for the Different Machine Learning Models using SMOTE and evaluated using holdout (80/20).**

<https://doi.org/10.1371/journal.pone.0195344.g007>

**Table 5. The performance of the Different Machine Learning Models evaluated using the 10-fold cross validation method using SMOTE.** The RTF model achieves the highest AUC (0.93), F-Score (86.70%), sensitivity (69.96%) and Specificity (91.71%).


<https://doi.org/10.1371/journal.pone.0195344.t005>

**Table 6. The performance of the Different Machine Learning Models evaluated using the Hold Out method (70/30) using SMOTE.** The RTF model achieves the highest AUC (0.88), Sensitivity (74.30%), Precision (73.50%) and F-Score (73.90%).


<https://doi.org/10.1371/journal.pone.0195344.t006>

Table 7. The performance of the Different Machine Learning Models evaluated using the Hold Out method (80/20) using SMOTE. The RTF model achieves the highest AUC (0.89), Sensitivity (75\%), Precision (73\%) and F-Score (74\%). The SVM model achieves the highest Specificity (88.9\%).


https://doi.org/10.1371/journal.pone.0195344.t007

- Precision metric: The RTF has the highest precision of $81.69 \%$ followed by the SVM achieving $61.95 \%$. The ANN and BN have comparable performance an achieving $57.43 \%$ and $57 \%$ respectively. The LWB showed the worst performance (55.67\%).
- F-score: The RTF took first place by achieving $86.70 \%$ while ANN came at the last place at only $39.46 \%$. The LB has the highest RMSE of 0.54 .

The two data splits (70/30 and 80/20) of the hold out evaluation method showed different and comparable results from the 10 -fold cross-validation method. For both data splits, the Random Tree Forest (RTF) showed the best performance of the Sensitivity, Specificity, Precision, F-score, AUC and Root Mean Squared Error metrics. For the two data splits, The BN showed the lowest performance for the Specificity metric. The Support Vector Machine (SVM) showed the lowest performance for the F-score, Sensitivity and Root Mean Squared Error metrics, for both data splits. The LWB showed the lowest performance for the Precision metric. In general, for all metrics, the results show that it is not necessarily that complex machine learning models such as Support Vector Machine (SVM) and Artificial Neural Networks (ANN) can always outperform simpler models such as the Random Tree Forest (RTF) model and the Bayesian Network classifier (BN) [46].

In principle, parametric models (e.g., SVM, ANN) tend to perform well in high-dimensioned classification problems that may have over hundreds of thousands of dimensions, which is not the case in this study. In addition, such models do not tend to perform well if the classes of the problem are strongly overlapping. In such cases, they can suffer from remembering local groupings as by their nature they summarize information in a way. ANN can usually outperform other methods if the dataset is very large and if the structure of the data is complex (e.g., they have many layers) [46]. On the other hand, Random Forest can be considered as an ensembling techniques which uses fully grown decision trees and combines them in a way that improve the accuracy of predictions by reducing variance. In addition, it inherently contains some underlying decision trees that omit the noise generating variable/feature(s). The Bayesian network classifier (BN) has the advantages of using very simple assumptions about the independence of the variables and shows superior performance in capturing interactions among input variables $[47,48]$.

# Discussion

Several studies have been conducted for predicting the risk of hypertension using statistical and machine learning techniques [49-52]. Samant and Rao presented a Levenberg-Marquardt back-propagation neural network model to predict hypertension. The dataset used was collected over 10 years at the Hemorheology Laboratory of the Indian Institute of Technology Bombay (IITB) hospital in Mumbai, India. The predictors used in building the model are blood pressure, serum proteins, albumin, hematocrit, cholesterol, triglycerides,

and hemorheological parameters. The authors evaluated the performance of the model using different number of nodes in the hidden layer and they concluded that using 20 nodes in the first hidden layer and 5 nodes in the second hidden layer achieves the best accuracy of $92.85 \%$.

Ture et al. [53] reported about the performance of four statistical models and two artificial neural networks models on predicting the risk of hypertension using a dataset consisting of 694 records. The predictors used in building the models are age, sex, family history, smoking habits, lipoproteins, triglycerides, uric acid, cholesterol, and BMI. Based on the sensitivity and specificity analysis of the models, the study shows that the artificial neural networks model based on Radial Basis Function [45] outperforms all the models achieving sensitivity of $95.20 \%$ and specificity of $66.70 \%$.

Al-Nozha et al. [54] determined the prevalence of hypertension among Saudis of both gender aged between 30 to 70 years in rural communities over the period between 1995 and 2000 using a dataset of 17,230 records. They proposed a predictive model for hypertension using Logistic regression. The prevalence of hypertension in males and females were $28.6 \%$ and $23.9 \%$ respectively. Predictive models for hypertension using support vector machine (SVM) using several kernel functions were compared in [55]. Three medical datasets of size 6000 were used and collected from the Department of Health Examination from those seeking an annual physical health check-up at Chang Gung Memorial Hospital in Tao-Yuan, Taiwan). In addition to nine datasets from the UCI repository [56] (census income, shuttle, mushroom, letter, ionosphere, vehicle silhouettes, spambase, vowel, and sonar), the largest dataset among these datasets is Census income and consists of 32,561 records. Results show that the SVM using multiplication kernel outperforms other approaches archiving average accuracy of $84.29 \%$ and $93.39 \%$ using large datasets (greater than 5000 records) and small datasets (fewer than 5000 records) respectively.

This study is designed to take advantage of the unique and rich clinical research dataset consisting of 23,095 patients, collected by the FIT project to investigate the relative performance of different machine learning classification techniques for predicting the individuals at risk of developing hypertension using medical records of cardiorespiratory fitness. To the best of our knowledge, this is the first study that compares the performance of six different ML models for predicting the individuals at risk of developing hypertension using cardiorespiratory fitness data. Using different validation methods, the RTF model on our dataset has shown the best performance $(\mathrm{AUC}=0.93)$ which outperforms the models of the previous studies.

# Conclusion 

Machine learning techniques have been shown to provide solid prediction capabilities in various application domains including medicine and healthcare [18, 22]. In this study, we presented an evaluation and comparison of six popular machine learning techniques on predicting the patients who could be at risk of developing hypertension using medical records of Cardiorespiratory Fitness from the Henry Ford Testing (FIT) Project. The results show that it is not necessarily that the more complex the machine learning model, the better prediction accuracy that can be achieved. Simpler models can perform better in some cases as well. The results have also shown that it is critical to carefully explore and evaluate the performance of the machine learning models using various model evaluation methods as the prediction accuracy can significantly differ. These results confirm the explorative nature of the machine learning process that requires iterative and explorative experiments in order to discover the model design that can achieve the target accuracy for a specific problem.

# Ethical approval 

The FIT project is approved by the IRB (ethics committee) of Henry Ford Hospital (IRB \#: 5812).

## Author Contributions

Conceptualization: Sherif Sakr, Amjad Ahmed, Mouaz H. Al-Mallah.
Data curation: Amjad Ahmed, Waqas T. Qureshi, Clinton Brawner, Steven Keteyian, Michael J. Blaha, Mouaz H. Al-Mallah.

Formal analysis: Sherif Sakr, Radwa Elshawi.
Investigation: Clinton Brawner, Steven Keteyian, Michael J. Blaha, Mouaz H. Al-Mallah.
Project administration: Mouaz H. Al-Mallah.
Software: Radwa Elshawi.
Writing - original draft: Sherif Sakr.
Writing - review \& editing: Sherif Sakr.
