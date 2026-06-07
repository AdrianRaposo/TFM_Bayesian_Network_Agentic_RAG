# Comparison of machine learning techniques to predict all-cause mortality using fitness data: the Henry ford exercise testing (FIT) project 

Sherif Sakr ${ }^{1}$, Radwa Elshawi², Amjad M. Ahmed ${ }^{1}$, Waqas T. Qureshi ${ }^{3}$, Clinton A. Brawner ${ }^{4}$, Steven J. Keteyian ${ }^{1}$, Michael J. Blaha ${ }^{5}$ and Mouaz H. Al-Mallah ${ }^{1,4 *}$ (D)


#### Abstract

Background: Prior studies have demonstrated that cardiorespiratory fitness (CRF) is a strong marker of cardiovascular health. Machine learning (ML) can enhance the prediction of outcomes through classification techniques that classify the data into predetermined categories. The aim of this study is to present an evaluation and comparison of how machine learning techniques can be applied on medical records of cardiorespiratory fitness and how the various techniques differ in terms of capabilities of predicting medical outcomes (e.g. mortality). Methods: We use data of 34,212 patients free of known coronary artery disease or heart failure who underwent clinician-referred exercise treadmill stress testing at Henry Ford Health Systems Between 1991 and 2009 and had a complete 10-year follow-up. Seven machine learning classification techniques were evaluated: Decision Tree (DT), Support Vector Machine (SVM), Artificial Neural Networks (ANN), Naïve Bayesian Classifier (BC), Bayesian Network (BN), K-Nearest Neighbor (KNN) and Random Forest (RF). In order to handle the imbalanced dataset used, the Synthetic Minority Over-Sampling Technique (SMOTE) is used. Results: Two set of experiments have been conducted with and without the SMOTE sampling technique. On average over different evaluation metrics, SVM Classifier has shown the lowest performance while other models like BN, BC and DT performed better. The RF classifier has shown the best performance (AUC $=0.97$ ) among all models trained using the SMOTE sampling. Conclusions: The results show that various ML techniques can significantly vary in terms of its performance for the different evaluation metrics. It is also not necessarily that the more complex the ML model, the more prediction accuracy can be achieved. The prediction performance of all models trained with SMOTE is much better than the performance of models trained without SMOTE. The study shows the potential of machine learning methods for predicting all-cause mortality using cardiorespiratory fitness data.


Keywords: FIT (Henry ford Exercise testing) project, All-cause mortality, Machine learning

[^0]
[^0]:    * Correspondence: AlMallahMo@ngha.med.sa; mouaz74@gmail.com

    * King AbdulAziz Cardiac Center, Ministry of National Guard, Health Affairs, King Abdulaziz Medical City for National Guard - Health affairs, King Abdullah International Medical Research Center, King Saud bin Abdulaziz University for Health Sciences, Department Mail Code: 1413, P.O. Box 22490, Riyadh 11426, Kingdom of Saudi Arabia
    *Division of Cardiovascular Medicine, Henry Ford Hospital, Detroit, MI, USA Full list of author information is available at the end of the article

Background

Using data to make decisions and predications is not new. However, the nature of data availability is changing and the changes bring with them complexity in managing the volumes and analysis of these data. The marriage between mathematics and computer science is driven by the unique computational challenges of building predictive models from large data sets and getting into untapped hidden knowledge. Machine learning (ML) [1, 2] is a modern data analysis technique with the unique ability to learn and improve its performance without being explicitly programmed and without human instruction. The main goal of supervised ML classification algorithms [3] is to explain the dependent variable in terms of the independent variables. The algorithms get adjusted based on the training sample and the error signal. In general, conventional statistical techniques commonly rely on the process of hypothesis testing. This process is very user-driven where user specifies variables, functional form and type of interaction. Therefore, user intervention may influence resulting models. With ML techniques, the primary hypothesis is that there is a pattern (rather than an association) in the set of predictor variables that will identify the outcome. ML algorithms automatically scan and analyze all predictor variables in a way that prevents overlooking potentially important predictor variables even if it was unexpected. Therefore, it has been acknowledged as a powerful tool which dramatically changes the mode and accessibility of science, research and practice in all domains [4]. Medicine and Healthcare are no different [5--7].

The Henry Ford exercIse Testing (FIT) Project [8] is a retrospective cohort that included 69,985 patients who had undergone exercise cardiopulmonary treadmill stress testing at Henry Ford Health System in Detroit, MI from January 1, 1991- May 28, 2009. Briefly, the study population was limited to patients over 18 years of age at the time of stress testing and excluded patients undergoing modified or non- Bruce protocol [9] exercise stress tests. Information regarding a patient's medical history, demographics, medications, cardiovascular disease risk factors were obtained at the time of testing by nurses and exercise physiologists, as well as searches through the electronic medical records. For the full details of The FIT Project, we refer to prior work by Al-Mallah et al. [8]. Several studies [10--13] have used conventional statistical techniques to predict various medical outcomes using the FIT project data. In general, ML is an exploratory process, where there is no one-model-fits-all solution. In particular, there is no model that is known to achieve the highest accuracy for all domains, problem types or datasets [14]. The best performing model varies from one problem to another based on the characteristics of the variables and observation. In this study, we evaluate and compare seven popular supervised ML algorithms in terms of its accuracy of prediction for mortality based on exercise capacity (e.g. fitness) data. In particular, we conducted experiments using the following ML techniques: Decision Tree (DT), Support Vector Machine (SVM), Artificial Neural Networks (ANN), Naïve Bayesian Classifier (BC), Bayesian Network (BN), K-Nearest Neighbor (KNN), and Random Forest (RF). We applied the 10-fold cross-validation evaluation method

Table 1 Baseline Characteristics for Included Study Cohort


mmHg millimeter mercury, bpm beat per minute, CAD coronary artery disease All the data are presented as: ${ }^{a}$ Mean and standard deviation and ${ }^{b}$ frequencies and percentages

for all techniques where several evaluation metrics are compared and reported. The study shows the potential of machine learning methods for predicting all-cause mortality using cardiorespiratory fitness data.

## Methods

### Cohort study

In this study, we have excluded from the original registry of the FIT project the patients with known coronary artery disease (n = 10,190) or heart failure (n = 1162) at the time of the exercise test or with less than 10-year follow-up (n = 22; 890). Therefore, a total of 34,212 patients were included in this study. The baseline characteristics of the included cohort are shown in Table 1 and indicate a high prevalence of traditional risk factors for cardiovascular disease. After a follow-up duration of 10 years, a total of 3921 patients (11.5%) died as verified by the national social security death index. All included patients had a social security number and were accounted for. In this study, we have classified the patients into two categories: low risk of all-cause mortality (ACM) and high risk of ACM. In particular, patients were considered to have high risk for ACM if the predicted event rate is more than or equal to 3%.

![img-0.jpeg](img-0.jpeg)

**Fig. 1** The ranking of the variables based on the outcome of the Feature Selection Process

**Table 2** Comparison of the performance of Decision Tree (DT) classifier with sampling using confidence parameter (*Conf*) equals 0.1, 0.25, 0.5, 0.75 and 1


### Data Preprocessing

Data preprocessing is a crucial step in ML. Data that have not preprocessed carefully may lead to misleading prediction results. In our study, we have conducted the following preprocessing steps.

- **Outliers:** The dataset used has been preprocessed by removing outliers (values that deviate from the expected value for a specific attribute) using the statistical measure namely inter-quartile range (IQR) [15]. The authors in [1] compare different outlier detection methods on biomedical datasets. The results show that the IQR is the fastest method in detecting all outliers correctly. Since the dataset used in this study is nearly symmetric, its mean equals its median equals its midrange, then the IQR is a good choice for handling outliers. The IQR measure is used to preprocess and identify the outliers from the training dataset. The IQR finds the outliers from the dataset by identifying the data that is over ranging from the dataset. The IQR is evaluated as IQR = Q3-Q1 where Q3 and Q1 are the upper and lower quartiles, respectively. The number of records that are identified as outliers and has been removed is 808 records.
- **Missing values:** It has been noted that some attributes such as the Percentage of Achieved Heart Rate and Metabolic Equivalent (METS) have missing values. The missing data for such attributes has been handled by replacing the missing values by the attribute mean.

**Table 3** Comparison of the performance of Decision Tree (DT) classifier without sampling using confidence parameter (*Conf*) equals 0.1, 0.25, 0.5, 0.75 and 1


Table 4 Comparison of the performance of Support Vector Machine (SVM) classifier with sampling using polynomial, normalized polynomial and puk kernels using complexity parameters 0.1, 10 and 30


## Feature selection

The FIT project dataset includes 49 demographic and clinical variables. ${ }^{1}$ In general, it is a common case that a few or several of the variables used in ML predictive models are in fact not associated with the response. In practice, including such irrelevant variables leads to unnecessary complexity in the resulting model. Therefore, before developing our model, we utilized an automated R-based popular feature selection algorithm, information gain [16], to choose the most effective attributes in classifying the training data. In particular, this algorithm assesses the weight of each variable by evaluating the entropy gain with respect to the outcome, and then ranks the variables according to their weights. Only attributes with information gain $>0$ were subsequently used in model building.

## Sampling

One of the main issues we encountered with the dataset used in this study is that it is imbalanced. In particular, the dataset included 3946 records with class label Yes (high risk of all-cause mortality) and 30,985 records with class label No (low risk of all-cause mortality). In general, the predication accuracy is significantly affected with imbalanced data [17]. In practice, there are two ways to handle the imbalanced class problem. One way is assign distinct costs to examples in the training dataset [18]. The other way is to either oversampling the minority class or to under-sampling the majority class [19-22]. In order to handle the imbalanced dataset used in this study, we use Synthetic Minority Over-sampling (SMOTE) Technique [23]. It is an over-sampling technique in which the minority class is over-sampled by creating synthetic examples rather than by over-sampling with replacement. SMOTE selects the minority class samples and creates "synthetic" samples along the same line segment joining some or all $K$ nearest neighbors belonging to the minority class [24, 25]. In other words, the oversampling is done as follows:

1. Take sample of the dataset and find its nearest neighbors
2. To create a synthetic data point, take the vector between a data point $P$ in the sample dataset and one of $P$ 's k-nearest neighbors.
3. Multiply this vector by a random number $x$ which lies between 0 and 1 .
4. Add this to $P$ to create the new synthetic data point.

The percentage of SMOTE instances created in our experiment is $300 \%$ ( 11,838 records from the minority class).

## Machine learning classification techniques

In our experiments, we studied the following seven popular ML classification techniques: Decision Tree (DT), Support Vector Machine (SVM), Artificial Neural Networks (ANN), Naïve Bayesian Classifier (BC), Bayesian Network

Table 5 Comparison of the performance of Support Vector Machine (SVM) classifier without sampling using polynomial, normalized polynomial and puk kernels using complexity parameters 0.1, 10 and 30


Table 6 Comparison of the performance of Artificial Neural Networks (ANN) classifier with gradient descent backpropagation using hidden units [1, 2, 4, 8, 32] and the momentum (0,0,2,0,5,0,9) using sampling


Table 7 Comparison of the performance of Artificial Neural Networks (ANN) classifier with gradient descent backpropagation using hidden units [1, 2, 4, 8, 32] and the momentum (0,0,2,0,5,0,9) without using sampling


(BN), K-Nearest Neighbor (KNN) and Random Forest (RF). We explore the space of parameters and common variations for each machine learning algorithm as thoroughly as is computationally feasible.

Decision Tree (DT) [26] is a model that uses a tree-like graph to predict the value of a target variable by learning simple decision rules inferred from the data features. We use J48 decision tree algorithm (Weka implementation of C4.5 [27]). We tested the J48 classifier with confidence factor of $0.1,0.25,0.5,0.75$ and 1 . The confidence factor parameter tests the effectiveness of post-pruning and lowering the confidence factor decreases the amount of post-pruning.

Support Vector Machine (SVM) [28] represents the instances as a set of points of 2 types in N dimensional place and generates a $(\mathrm{N}-1)$ dimensional hyperplane to separate those points into 2 groups. SVM attempts to find a straight line that separates those points into 2 types and is situated as far as possible from all those points. Training the SVM is done using Sequential Minimal Optimization algorithm [2]. We used Weka implementation of SMO [29]. We tested SVM using polynomial, normalized polynomial, puk kernels and varied the complexity parameter $\{0.1,10$, and 30\}. The value of the complexity parameter controls the tradeoff between fitting the training data and maximizing the separating margin.

Artificial Neural Network (ANN) [30] attempts to mimic the human brain in order to learn complex tasks. It is modeled as an interconnected group of nodes in a way that is similar to the vast network of neurons in the human brain. Each node of the network receives inputs from other nodes, combines them in some way, performs a generally nonlinear operation on the result and outputs the final result. We trained the Neural Networks with gradient descent backpropagation. We varied the number of hidden units $\{1,2,4,8,32\}$ and the momentum $\{0,0.2,0.5,0.9\}$.

Naïve Bayesian Classifier [31] applies Bayes' theorem [32] with the naive assumption of independence between every pair of features. We use Weka implementation of Multilayer Perceptron [33]. We try three different Weka options for handling continuous attributes: modeling them as a single normal, modeling them with kernel estimation, or discretizing them using supervised discretization. Bayesian Network [34] is designed for modeling under uncertainty where the nodes represent variables and arcs represent direct connections between them. BNs model allows probabilistic beliefs about the variables to be updated automatically as new information becomes available. We tried different search algorithms including K2 [33], Hill Climbing [35], Repeated Hill Climber, LAGD Hill Climbing, TAN [36], Tabu search [53] and Simulated annealing [37].

Table 8 Comparison of the performance of Naïve Bayesian classifier (BC) using three different Weka options for handling continuous attributes: single normal, kernel estimation and supervised discretization using Sampling


K-Nearest Neighbors (KNN) [38] identifies from the neighbors, K similar points in the training data that are closest to the test observation and classifies it by estimating the conditional probability of belonging to each class and choosing the class with the largest probability. We varied the number of $\mathrm{k}\{1,3,5,10\}$ neighbors. We considered three distance functions: Euclidean distance, Manhattan distance and Minkowski distance.

Random Forest (RF) [39, 40] is a classification algorithm that works by forming multiple decision trees at training and at testing it outputs the class that is the mode of the classes (classification). Decision tree works by learning simple decision rules extracted from the data features. The deeper the tree, the more complex the decision rules and the fitter the model. Random decision forests overcome the problem of over fitting of the decision trees. We use Random Forest Weka implementation. We varied the forests to have 10,50 , and 100 trees. The size of the feature set considered at each split is 1 , $2,4,8$, and 12 .

## Model evaluation and validation

In order to evaluate our models, we used the 10 -fold cross-validation [39] evaluation method where the data are randomly partitioned into 10 mutually exclusive subsets $\left\{\mathrm{D}*{1}, \mathrm{D}*{2}, \ldots, \mathrm{D}_{\mathrm{K}}\right\}$ with approximately equal size. The

Table 9 Comparison of the performance of Naïve Bayesian classifier (BC) using three different Weka options for handling continuous attributes: single normal, kernel estimation and supervised discretization without using Sampling


Table 10 Comparison of the performance of Bayesian Network classifier (BN) using different search algorithms: K2, Hill Climbing, Repeated Hill Climber, LAGD Hill Climbing, TAN, Tabu and Simulated Annealing using Sampling


testing operation is then repeated 10 times where at the $\mathrm{i}^{\text {th }}$ evaluation iteration, the $\mathrm{D}*{\mathrm{i}}$ subset is used as the test set and the others as the training set. In general, a main advantage of the 10 -fold cross-validation evaluation method is that it has a lower variance than a single hold-out set evaluator. In particular, it reduces this variance by averaging over 10 different partitions, therefore, it is less sensitive to any partitioning bias on the training or testing data. For each iteration of the evaluation process, the following metrics are calculated:

- Sensitivity: True Positive recognition rate

Sensitivity $=\mathrm{TP} / \mathrm{TP}+\mathrm{FN}$

- Specificity: True Negative recognition rate

Specificity $=\mathrm{TN} / \mathrm{TN}+\mathrm{FP}$

- Precision: It represents the percentage of tuples that the classifier has labeled as positive are actually positive

Precision $=\mathrm{TP} / \mathrm{TP}+\mathrm{FP}$

- F-score: It represents the harmonic mean of precision and sensitivity $F$-score $=2 * \mathrm{TP} / 2 * \mathrm{TP}+\mathrm{FP}+\mathrm{FN}$
- Root Mean Squared Error (RMSE): It is defined as the square root of the mean square error that measures the difference between values predicted by the model and the actual values observed, where $y$ is a vector of $n$ predictions and $y$ is the vector of $n$ observed (actual) values

$$ R M S D=\sqrt{\left(\frac{1}{n} \sum_{i=1}^{n}\left(y_{i}-y_{i}\right)^{2}\right)} $$

- ROC: Receiver Operating Characteristic (ROC) Curve [40] is a way to quantify the diagnostic value of a test over its whole range of possible cutoffs for classifying patients as positive vs. negative. In each possible cutoff, the true positive rate and false positive rate is calculated as the X and Y coordinates in the ROC Curve.

True Positive (TP) refers to the number of high risk patients who are classified as high risk, whereas False Negative (FN) refers to the number of high risk patients who are classified as low risk patients. On the other hand, False Positive (FP) refers to the number of low risk patients who are classified as high-risk patients and False Negative (FN) refers to the number of low risk patients who are classified as low risk patients. All results of the different metrics are then averaged to return the final result.

Table 11 Comparison of the performance of Bayesian Network classifier (BN) using different search algorithms: K2, Hill Climbing, Repeated Hill Climber, LAGD Hill Climbing, TAN, Tabu and Simulated Annealing without using Sampling


Table 12 Comparison of the performance K-Nearest Neighbor classifier (KNN) using different values of k (1, 3, 5, 10) neighbors and using different distance functions; Euclidean distance, Manhattan distance and Minkowski distance using sampling


The results show that the value 1 for the K parameter achieves the highest AUC (0.88) using Euclidean distance

## Results

As an outcome of the feature selection process, the ML models have been developed using only 15 variables where Age, METS, Percentage HR achieved, HX Hypertension, Reason for test are ranked as the top significant five variables. The full list of the outcome variables is presented in Fig. 1.

Tables 2 and 3 show the performance of the DT classifier, with confidence parameter (Conf) equals $0.1,0.25$, $0.5,0.75$ and 1 , using sampling and without using sampling, respectively. The results show that the AUC increased as the confidence factor increased up to about 0.75 at a peak of 0.88 AUC using sampling and up to about 0.25 at a peak of 0.73 AUC without using sampling, after which the classifier exhibited effects of over-training. These effects are seen by a decrease in the AUC value with a confidence factor above 0.75 using sampling and above 0.25 without using sampling.

The results of the SVM classifier using sampling and without using sampling are reported in Tables 4 and 5, respectively. Different kernels (polynomial kernel, normalized polynomial kernel and puk kernel) and complexity parameters (C) ( $0.1,10$ and 30) are tested. The results show that the AUC increased as the complexity parameter increased up to 30 using sampling. In addition, the SVM using puk kernel outperforms the SVM using other kernels achieving AUC of 0.80 using sampling and 0.59 without using sampling with complexity parameter $C=30$.

Tables 6 and 7 show the performance of Neural Networks with gradient descent backpropagation using hidden units $H=[1,2,4,8,32]$ and the momentum $M=[0,0.2,0.5,0.9]$ using sampling and without using sampling, respectively. The number of hidden units and momentum rate that gives better AUC value is considered here. For neural networks, the highest performance is achieved when $H=4$ and $M=0.5$ for the case of using sampling ( $\mathrm{AUC}=0.82$ ) while when $H=8$ and $M=0$ for the case of not using sampling ( $\mathrm{AUC}=0.80$ ).

The performance of the Naïve Bayesian Classifier using sampling and without using sampling is reported in Tables 8 and 9, respectively. Three different Weka options for handling continuous attributes are explored (single normal, kernel estimation and supervised discretization). Results show that BC using supervised discretization achieves the highest AUC value of 0.82 using sampling and without using sampling. The performance results of the Bayesian Network classifier with different search algorithms (K2, Hill Climbing, Repeated Hill Climber, LAGD Hill Climbing, TAN, Tabu and Simulated Annealing) using sampling and without using sampling are reported in Tables 10 and 11, respectively. Bayesian Network classifier using Tan search algorithm achieves the highest AUC value of 0.84 using Sampling and 0.83 without using sampling.

Tables 12 and 13 report the performance of the KNN classifier, with different values of $\mathrm{k}(1,3,5,10)$ neighbors,

Table 13 Comparison of the performance K-Nearest Neighbor classifier (KNN) using different values of k $(1,3,5,10)$ neighbors and using different distance functions; Euclidean distance, Manhattan distance and Minkowski distance without using sampling


The results show that the value 10 for the K parameter achieves the highest AUC (0.74) using Euclidean distance

Table 14 Comparison of the performance of Random Forest (RF) classifier having 10, 50 and 100 trees with different feature set considered at each split (1, 2, 4, 8, and 12) using sampling


and using sampling and without using sampling. In our experiments, we used different distance functions; Euclidean distance, Manhattan distance and Minkowski distance. The results show that the KNN classifier using sampling has its best performance ( $\mathrm{AUC}=0.88$ ) with K value equals 1 using any of the three distance functions while the KNN classifier without using sampling has its best performance ( $\mathrm{AUC}=0.74$ ) with K value equals 10 using any of the three distance functions.

Tables 14 and 15 report the performance of the Random Forest (RF) classifier using 10, 50 and 100 trees. The size of the feature set $(F)$ considered at each split is $1,2,4,8$, and 12 . The results show that the highest AUC (0.97) is achieved using a forest of 50 trees with a feature set of $1,2,4,8$ or 12 using sampling whereas the highest AUC (0.82) is achieved using a forest of 100 trees with a feature set of 4 .

We compared the impact of using different percentage of synthetic examples of the class "yes" (patients who are considered to have high risk for ACM). Figure 2 shows the area under the curve of seven different machine learning models trained using Decision Tree (DT), Support Vector Machine (SVM), Artificial Neural Networks (ANN), Naïve Bayesian Classifier (BC), Bayesian Network (BN), K-Nearest Neighbor (KNN) and Radom Forest (RF). All the models have been evaluated using datasets with $100 \%, 200 \%$ and $300 \%$ of synthetic example created using the SMOTE sampling technique on the training dataset and evaluated using 10 -fold cross validation. The results show that increasing the percentage of synthetic examples improves the prediction accuracy for all models except for the BC. For example, the SVM model achieves AUC of 0.62 using the sampled dataset with $100 \%$ synthetic examples compared to 0.72 using the sampled dataset with $200 \%$ synthetic examples. Increasing the percentage of synthetic examples to $300 \%$ improves the AUC of the BN to achieve 0.8 . The performance of KNN, DT and RTF models using SMOTE has shown great improvement. The RF has shown the best improvement using SMOTE achieving 0.83 using $100 \%$ synthetic examples compared to 0.95 and 0.97 using $200 \%$ and $300 \%$ synthetic examples respectively. In our experiments, further increasing the synthetic examples to $400 \%$ and $500 \%$ did not show any improvement in the performance of the prediction models.

In order to evaluate the impact of using the SMOTE sampling techniques in handling the problem of the imbalanced dataset, we build different prediction models with and without SMOTE. Tables 16 and 17 show the prediction performance of different prediction models using various evaluation metrics without and with the SMOTE sampling technique ( $300 \%$ ), respectively. For each metric (row), we highlighted the highest value in bold font and underlined the lowest value. As shown in Tables 16 and 17, after applying the 10 -fold cross-validation on the training dataset, the AUC and sensitivity for all

Table 15 Comparison of the performance of Random Forest (RF) classifier having 10, 50 and 100 trees with different feature set considered at each split (1, 2, 4, 8, and 12) without using sampling


![img-1.jpeg](img-1.jpeg)

models used SMOTE have been significantly improved over the training results without SMOTE except for the BC. In addition, the performance of each model can differ from one metric to another. In general, the Random Forest (RF) classifier using SMOTE sampling achieves the best performance improvement. In particular, it achieves the best performance in terms of Sensitivity (95.07%), RMSE (0.18), F-Score (84.55%) and AUC (0.97). However, the same model without using SMOTE achieves Sensitivity of (59.09%), RMSE of (0.29), F-Score (29.35%) and AUC of (0.82). The KNN models using SMOTE achieve the best performance in terms of Specificity (96.98%) and Precision (77.18%). The KNN model without SMOTE achieves Specificity of 89.31%% and Precision of 11.12%. This improved performance of the prediction models is due to the imbalanced data size. It is noted that all the models with SMOTE achieve a more balanced sensitivity. Figure 3(a) and (b) illustrate the ROC curves for the different ML models with and without using SMOTE, respectively.

# Discussion

Using machine learning methods to predict different medical outcomes (e.g., diabetics, hypertension and death) from medical datasets is gaining an increasing attention in the medical domain. This study is designed to take advantage of the unique opportunity provided by our access to a large and rich clinical research dataset, a total of 34,212 patients, collected by the FIT project to investigate the relative performance of various machine learning classification methods for predicting all-cause mortality (ACM) using medical records of cardiorespiratory fitness. The large number of attributes of the dataset, 49 attributes, is used to uncover new potential predictors of ACM. To the best of our knowledge, this is the first study that compares the performance of ML model for predicting ACM using cardiorespiratory fitness data. We have evaluated seven models trained with and without SMOTE using various evaluation metrics.

Knuiman et al. [41] presented an empirical comparison of four different techniques for estimating the risk of death using mortality follow-up data on 1701 men. The four techniques used are binary tree, logistic regression, survival tree and Cox regression. The Cox regression outperformed the other three techniques achieving area under the AUC of 0.78 followed by logistic regression (AUC = 0.72), survival tree (AUC = 0.71) and binary tree (AUC = 0.66), respectively. Vomlel et al. [42] presented a

Table 16 Comparison of the performance of the different classification models without using the SMOTE sampling method


The models are: Decision Tree (DT), Support Vector Machine (SVM), Artificial Neural Networks (ANN), Naïve Bayesian Classifier (BC), Bayesian Network (BN), K-Nearest Neighbor (KNN) and Random Forest (RF). The results of this experiment show that BN achieves the highest AUC (0.83). The BC model achieves the highest precision (51.32%) and the highest specificity (93.32%)

Table 17 Comparison of the performance of the different classification models using the SMOTE sampling methods. The models are: Decision Tree (DT), Support Vector Machine (SVM), Artificial Neural Networks (ANN), Naïve Bayesian Classifier (BC), Bayesian Network (BN), K-Nearest Neighbor (KNN) and Random Forest (RF)


The results of this experiment show that the RF model achieves the highest AUC (0.97), the lowest RMSE (0.18) and the highest sensitivity (94.65\%) predictive model for mortality using five different machine learning techniques on a data of 603 patients from University Hospital in Olomouc. The machine learning techniques used are logistic regression, decision tree, Naive Bayes classifier, Artificial Neural Network and Bayesian Network classifier. Using 10- fold cross validation logistic regression achieves the highest area under curve of 0.82 , whereas the decision tree has the lowest AUC value of 0.61. Allyn et al. [43] compared the performance of logistic regression model and different machine learning models to predict the mortality in-hospital after elective cardiac surgery. The study includes database of 6520 patients from December 2005 to December 2012, from a cardiac surgical center at University Hospital. Five different machine learning models have been evaluated: logistic regression, gradient boosting machine, random forest, support vector machine and naive bayes. The area under the ROC curve for the machine learning model ( $\mathrm{AUC}=0.795$ ) was significantly higher than the logistic regression model ( $\mathrm{AUC}=0.742$ ). Taylor et al. [44] studied the prediction of mortality of 4676 patients with sepsis at the emergency department using logistic regression and machine learning model. The machine learning model (AUC 0.86) outperforms the logistic regression model (AUC 0.76). Sherri [45] studied the Physical Performance and Age-Related Changes in Sonomans (SPPARCS) to predict death among 2066 residents of Sonoma, California over the period between 1993 and 1995. In this study, a super learner has been used for death prediction. A super learner is an ensembling machine learning approach that combines multiple machine learning algorithms into a single algorithm and returns a prediction function with the best cross-validated mean squared error. The super learner outperforms all single algorithms in the collection of algorithms, although its performance was quite similar to that of some algorithms. Super learner outperformed the worst algorithm (neural networks) by $44 \%$ with respect to estimated crossvalidated mean squared error. In principle, the datasets of both studies (Knuiman et al. [41] and Allyn et al. [43]) are considered to be relatively small in comparison to the number of patients for our dataset. In general, in

![img-2.jpeg](img-2.jpeg)

Fig. 3 The ROC curves of the different machine learning classification models. The models are: Decision Tree (DT), Support Vector Machine (SVM), Artificial Neural Networks (ANN), Naïve Bayesian Classifier (BC), Bayesian Network (BN) and K-Nearest Neighbor (KNN). The results show that without using the SMOTE sampling method (a), BC and BN achieves the highest AUC (0.81) while with using the SMOTE sampling method (b), the KNN model achieves the highest AUC (0.94)

Machine Learning, the bigger the size of the dataset, the higher the accuracy and robustness of the developed prediction models. In these studies, the highest AUC achieved by the developed prediction models is 0.86. In our experiments, the Random Forest (RF) model using SMOTE sampling achieved AUC of 0.97 which significantly outperform the models of both studies.

Sullivan et al. [46] investigated the literature related to the comparisons made between established risk prediction models for perioperative mortality used in the setting of cardiac surgery. Meta-analysis was conducted to calculate a summary estimate of the difference in AUCs between models. The comparisons include 22 studies. The authors noted that all he investigated studies relied on relatively small datasets. This highlights the strengths and uniqueness of our study which is relying on large datasets reflected on the number of patients and the number of variables.

In general, an important observation from the results of our experiments is that for all metrics, the results show that it is not necessarily that the complex ML models (e.g. Support Vector Machine (SVM), Artificial Neural Networks (ANN)) can always outperform simpler models (e.g. Decision Tree (DT) model [47]). In particular, the Decision Tree (DT) model has been outperforming the complex models in terms of all evaluation metrics. The RF and KNN classifiers are considered to be less complex than SVM and ANN. However, it achieved the best performance for all metrics for model trained using SMOTE. In general, KNN is a non-linear classifier, therefore, it tends to perform very well with a lot of data points. It is also very sensitive to bad features (variables). Therefore, effective feature selection [27] is an important step before using the KNN classifier and tends to improve its results. The Decision Tree (DT) model benefits from the feature selection and removing colinear variables steps as well. In general, decision trees do not require any assumptions of linearity in the data and thus they work well for nonlinearly related variables.

On the other hand, the SVM model tends to perform well in high-dimensioned classification problems that may have over hundreds of thousands of dimensions, which is not the case of this study. In addition, the SVM model does not tend to perform well if the classes of the problem are strongly overlapping. In general, parametric models (e.g. SVM, Bayesian Network) can suffer from remembering local groupings as by their nature they summarize information in some way. ANN can usually outperform other methods if the dataset is very large and if the structure of the data is complex (e.g. they have many layers). This is an advantage for the KNN classifier which makes the least number of assumptions regarding the input data.

The results also show that the performance of the KNN and ANN classifiers, similar to the other models, can be very sensitive for the values of its parameters and thus these parameters need to be carefully explored and tuned in order to reach an adequate configuration. For example, the results show that setting the K parameter to the value of 1 achieves the best performance for all the evaluation metrics. For example, for K = 1, the model achieves AUC of (0.94) while for K = 3, 5 and 10, the model achieves the accuracy of (0.93), (0.91) and (0.90), respectively. In general, increasing the value of the K parameter has a mostly negative impact on the performance of the classifier for all metrics. The risk of model overfilling by using a low K value has been overcome by using the 10-fold cross-validation evaluation method. However, clearly, the optimal value of the K parameter can significantly differ from one problem to another.

## Conclusion

ML techniques have shown solid prediction capabilities in various application domains including medicine and healthcare. In this study, we presented an evaluation and comparison of seven popular ML techniques on predicating all-cause mortality (ACM) using medical records of Cardiorespiratory Fitness for the Henry Ford Testing (FIT) Project. The results show that various ML techniques can significantly vary in terms of its performance for the different evaluation metrics. It is also not necessarily that the more complex the ML model, the more prediction accuracy can be achieved. Simpler models can perform better in some cases as well. Therefore, there is no one-size-fits-all model that can be well performing for all domains or datasets. Each problem and dataset need to be carefully evaluated, modeled and studied in order to reach an effective predictive model design. The results have also shown that it is critical to carefully explore and evaluate the performance of the ML models using various tuned values for their parameters. These results confirm the explorative nature of the ML process that requires iterative and explorative experiments in order to discover the model design that can achieve the target accuracy.

## Endnotes

1The detailed descriptions of the variables of the dataset are available on the appendix of the article.

ACM
All-cause mortality
ANN
Artificial Neural Networks
BC
Naïve Bayesian Classifier
BN
Bayesian Network
CRF
Cardiorespiratory Fitness
DT
Decision Tree
KNN
K-Nearest Neighbor
ML
Machine Learning
RF
Random Forest
SMOTE
Synthetic Minority Over-Sampling Technique (SMOTE)
SVM
Support Vector Machine

The authors thank the staff and patients involved in the FIT project for their contributions.

## Availability of data and material

The FIT project includes data from a single institution which was collected under IRB approval and did not utilize public funding or resources. Resources from Henry Ford Hospital were utilized in this project. The IRB approval clearly stated that the data will remain with the PI (Dr. Mouaz Al-Mallah mouaz74@gmail.com) and the study investigators. We would like to note that there many ongoing analyses from the project. Data sharing will be only on a collaborative basis after the approval of the all the investigators who have invested time and effort on this project. This also has to be subject to IRB approval from Henry Ford Hospital and data sharing agreements.

## Funding

Funding was provided by King Abdullah International Medical Research Center. Funding grant number SP16/100. The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript.

## Authors' contributions

SS: Data analysis and manuscript drafting. RE: Data analysis and manuscript drafting. AA: Data collection, critical review of manuscript. WQ: Data collection, critical review of manuscript. CB: Data collection, critical review of manuscript. SK: Data collection, critical review of manuscript. MB: Data analysis, critical review of manuscript. MA: Data collection, Data analysis and critical review of manuscript. All authors read and approved the final manuscript.

## Ethics approval and consent to participate

This article does not contain any studies with human participants or animals performed by any of the authors. The FIT project is approved by the IRB (ethics committee) of HFH hospital (IRB #: 5812). Informed consent was waived due to retrospective nature of the study. The consent to participate is not required.

## Consent for publication

Not applicable. The manuscript doesn't contain any individual identifying data.

## Competing interests

The authors declare that they have no competing interests.

## Publisher's Note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## Author details

${ }^{1}$ King AbdulAziz Cardiac Center, Ministry of National Guard, Health Affairs, King Abdulaziz Medical City for National Guard - Health affairs, King Abdullah International Medical Research Center, King Saud bin Abdulaziz University for Health Sciences, Department Mail Code: 1413, P.O. Box 22490, Riyadh 11426, Kingdom of Saudi Arabia. ${ }^{2}$ Princess Nourah bint Abdulrahman University, Riyadh, Saudi Arabia. ${ }^{3}$ Wake Forest School of Medicine, Medical Center Boulevard, Winston-Salem, NC, USA. ${ }^{4}$ Division of Cardiovascular Medicine, Henry Ford Hospital, Detroit, MI, USA. ${ }^{5}$ Johns Hopkins University, Baltimore, MD, USA.

## Received: 5 April 2017 Accepted: 22 November 2017 Published online: 19 December 2017

## Submit your next manuscript to BioMed Central and we will help you at every step:

- We accept pre-submission inquiries
- Our selector tool helps you to find the most relevant journal
- We provide round the clock customer support
- Convenient online submission
- Thorough peer review
- Inclusion in PubMed and all major indexing services
- Maximum visibility for your research

Submit your manuscript at www.biomedcentral.com/submit
(1) BioMed Central