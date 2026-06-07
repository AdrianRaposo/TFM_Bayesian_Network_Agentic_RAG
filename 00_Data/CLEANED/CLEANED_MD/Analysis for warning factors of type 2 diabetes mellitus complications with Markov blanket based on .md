# Analysis for warning factors of type 2 diabetes mellitus complications with Markov blanket based on a Bayesian network model 

Article

Accepted Version

Liu, S., Zhang, R., Shang, X. and Li, W. ORCID:
https://orcid.org/0000-0003-2878-3185 (2020) Analysis for warning factors of type 2 diabetes mellitus complications with Markov blanket based on a Bayesian network model.
Computer Methods and Programs in Biomedicine, 188. 105302. ISSN 1872-7565 doi:
https://doi.org/10.1016/j.cmpb.2019.105302 Available at https://centaur.reading.ac.uk/88400/

It is advisable to refer to the publisher's version if you intend to cite from the work. See Guidance on citing.

To link to this article DOI: http://dx.doi.org/10.1016/j.cmpb.2019.105302
Publisher: Elsevier

All outputs in CentAUR are protected by Intellectual Property Rights law, including copyright law. Copyright and IPR is retained by the creators or other copyright holders. Terms and conditions for use of this material are defined in the End User Agreement.

# www.reading.ac.uk/centaur 

## CentAUR

Central Archive at the University of Reading
Reading's research outputs online

# Analysis for warning factors of type 2 diabetes mellitus complications 

with Markov blanket based on a Bayesian network model

Siying Liu ${ }^{\mathrm{a}}$, Runtong Zhang ${ }^{\mathrm{a}}$, Xiaopu Shang ${ }^{\mathrm{a}}$, Weizi $\mathrm{Li}^{\mathrm{b}}$<br>${ }^{\text {a }}$ School of Economics and Management, Beijing Jiaotong University, Beijing 100044, PR China<br>${ }^{\mathrm{b}}$ Informatics Research Center, University of Reading, Berkshire RG6 6AH, United Kingdom


#### Abstract

Background and objective: Type 2 diabetes mellitus (T2DM) complications seriously affect the quality of life and could not be cured completely. Actions should be taken for prevention and self-management. Analysis of warning factors is beneficial for patients, on which some previous studies focused. They generally used the professional medical test factors or complete factors to predict and prevent, but it was inconvenient and impractical for patients to self-manage. With this in mind, this study built a Bayesian network (BN) model, from the perspective of diabetic patients' selfmanagement and prevention, to predict six complications of T2DM using the selected warning factors which patients could have access from medical examination. Furthermore, the model was analyzed to explore the relationships between physiological variables and T2DM complications, as well as the complications themselves. The model aims to help patients with T2DM self-manage and prevent themselves from complications.


Methods: The dataset was collected from a well-known data center called the National Health Clinical Center between 1st January 2009 and 31st December 2009. After preprocess and impute the data, a BN model merging expert knowledge was built

with Bootstrap and Tabu search algorithm. Markov Blanket (MB) was used to select the warning factors and predict T2DM complications. Moreover, a Bayesian network without prior information (BN-wopi) model learned using 10-fold cross-validation both in structure and in parameters was added to compare with other classifiers learned using 10-fold cross-validation fairly. The warning factors were selected according the structure learned in each fold and were used to predict. Finally, the performance of two BN models using warning features were compared with Naïve Bayes model, Random Forest model, and C5.0 Decision Tree model, which used all features to predict. Besides, the validation parameters of the proposed model were also compared with those in existing studies using some other variables in clinical data or biomedical data to predict T2DM complications.

Results: Experimental results indicated that the BN models using warning factors performed statistically better than their counterparts using all other variables in predicting T2DM complications. In addition, the proposed BN model were effective and significant in predicting diabetic nephropathy (DN) (AUC: 0.831), diabetic foot (DF) (AUC: 0.905), diabetic macrovascular complications (DMV) (AUC: 0.753) and diabetic ketoacidosis (DK) (AUC: 0.877) with the selected warning factors compared with other experiments.

Conclusions: The warning factors of DN, DF, DMV, and DK selected by MB in this research might be able to help predict certain T2DM complications effectively, and the proposed BN model might be used as a general tool for prevention, monitoring, and self-management.

Keywords: Bayesian network, Type 2 Diabetes Mellitus complications, prevention, self-management, warning factors

# 1. Introduction 

Diabetes Mellitus (DM) is associated with various metabolic disorders, heavily enlarging the charge of non-communicable diseases [1], and chronic hyperglycemia due to insufficient insulin action is the main feature [2]. Type 2 diabetes mellitus (T2DM) accounts for $85 \%$ to $90 \%$ of all diabetic cases, which imposes the burden on not only individuals but the healthcare system [1,3]. Moreover, T2DM leads to complications such as kidney failure, blindness, cardiovascular diseases, nerve damage, ketoacidosis and foot problems, which seriously affect the quality of life, cause significant economic burdens to family and society, and even result in death [4-9]. The number of people with T2DM complications has been increasing, especially for young populations, which yearly increases the socio-economic societal burden of them [10]. According to a research carried out by Chapman et al. [11], the microvascular complications contribute extensively to the economic burden, and with the condition has been being more serious, the overall cost was exceeding $£ 70$ million over the two years. Therefore, the prevention of T2DM complications is significant for hospitals and patients with diabetes.

There are two methods of preventing complications that continuous medical care and long-term self-management. T2DM could not be cured completely but be controlled by medication, diet, and lifestyle changes [12-13]. In other words, the longterm prevention of complications is necessary for the patients with T2DM. However, nowadays, healthcare resources are limited and costly, especially in the impoverished area [14-15]. It is impractical to rely entirely on the medical care in the hospital. Moreover, doctors are more likely to advise patients to do diabetic self-care at home if the symptom is not severe. Consequently, actions should be taken for prevention and self-management.

Warning factors are strong contributors to certain outcome variables, which could be used widely to predict and support decision making in medical informatics [16-17]. For patients, warning factors could prevent them from the presence of a particular disease. In other words, analysis for warning factors plays a vital role in disease prevention. Machine Learning has been developing rapidly in recent years, and simulation models built with it are increasingly applied to derive predictions and analyze the warning factors of T2DM complications. Cho et al. [18] compared the prediction results of diabetic nephropathy between several classification methods with 39 features and showed the effect of each feature on the decision using the visualization tool. A fuzzy classification model was employed to predict heart and kidney complications with six attributes of clinical data [19]. Leung et al. [20] using 10 clinical attributes and 5 genetic attributes built different models with seven machine learning methods to predict warning patterns in diabetic kidney disease. There are also some studies suggesting the biomedical factors such as endostatin [21-22], microRNAs (miRNAs) [23] and red blood cell deformability index [24] to predict T2DM complications or predict the T2DM development in certain patients.

It is essential for diabetic patients to self-manage and to improve self-care skills with known warning features so that they can prevent themselves from complications to avoid severe conditions [25]. Therefore, the selection of the features from datasets is significant. It is inconvenient and unpractical for patients to obtain the features referring to professional medical test indicators and to input all features to the models that not dealing with the incomplete data sets when they take actions to self-manage and make prevention. However, there are few studies analyzing warning factors of T2DM complications from the perspective of diabetic patients' self-management and prevention, and most of them only focus on one complication.

Bayesian networks (BNs) representing the conditional probability between random variables graphically is an increasingly popular method that deals with uncertain and complex fields. They are more capable of dealing with incomplete data sets with better performance than many other models and revealing the causal relationships between variables [26-27]. Our paper mainly aims to build a Bayesian network (BN) model to

find out and analyze the warning factors of T2DM complications with Markov blanket (MB) and use them to predict complications of T2DM. The warning features consist of urine test data, glycated hemoglobin (HbA1c) and biochemical parameters, which patients could have access from medical examination. We analyze the model to explore the relationships between physiological variables and T2DM complications, as well as the complications themselves. The model could probably be beneficial for prevention, monitoring and self-management, and that might be more convenient and manageable for patients. Besides, the model is probably capable of applying in different scenarios based on hypothetical cases when new observations are instantiated according to the patients' situation.

This paper is organized as follows. Section 2 explains the collected data used in this study and its processing methods, displays the flow of building a BN model, and analyzes the final T2DM complications model and the warning features selection. Section 3 adds a Bayesian network without prior information model (BN-wopi), and describes the comparison results with the other three models used in the diagnosis and presents the effectiveness of the previous studies' prediction to demonstrate the performance of warning factors of the BN model in prediction further. Section 4 discusses the warning factors of T2DM complications using MB and several specific scenarios. We conclude the study and suggest our future topics and applications in the last section.

# 2. Materials and Methods 

In this section, we will demonstrate some concepts of methods we used in the study and the learning flow of our BN model in detail. First, we will describe the data collected and the approaches of preprocessing and imputation. Then, we will introduce BNs and MB, and some related basic concepts of connection and separation in BNs. After that, the process of building a T2DM complication model will be presented, and the structural and parametric learning approaches of the model will be described in

detail. We will describe the final T2DM complications model and analyze the warning features of complications with MB in the last section.

Our models are developed in RStudio, with mice, vice, bnlearn and ROCR packages mainly. The BNs model is operated in Netica to analyze the warning features of T2DM complications.

# 2.1 Data Collection 

Based on data from a well-known data center called the National Health Clinical Center, we learned the structure and the probability distributions of our BN model. All inpatient sample databases related complications of diabetes were provided by the General Hospital of the People's Liberation Army (PLAGH), and they were extracted for the period 1st January 2009 to 31st December 2009. The original data collected particularly from the Hospital Information System (HIS) were followed the principle of authenticity and professional characteristic that is recording the accurate and unprocessed value of each test and real information about the inpatients. Each case was taken down after diagnosis during hospitalization. It could be classified into three categories according to the property of data: basic information, physiological information, and complications information. Specifically, physiological information consists of urine test variables, HbA1C test variables and biochemical test variables.

In this data set, there are 43 features in all. To protect the privacy of patients, we removed the ID column. Moreover, we also removed lipase (LPS), ferrum (Fe) and unsaturated iron-binding capacity (TIBC) variables because of the large portion of missing values. Therefore, the dataset we used in this study to build the model and assess the warning feature contains 39 features including age and gender, 13 items related to the urine test, glycated hemoglobin (HbA1c) and 23 items related to the biochemical test. There are six complications variables, which are diabetic nephropathy (DN), diabetic retinopathy (DR), diabetic foot (DF), diabetic macrovascular complications (DMV), diabetic peripheral neuropathy (DPN), and diabetic ketoacidosis (DK) in this study.

Considering the readability, the convenience of training model using these data,

and the influence of outlier on the result, we integrated the information of each patient into one case and then removed the value of the same variable that was contradictory during one stay in the hospital, which leads to the independence between the cases. The contradictory value here means that the ones of discretized variables, and there are three situation (for one patient in one stay in the hospital): (i) if there are less $30 \%$ values of the variable in other states, whereas other values are in the certain state, the value of the variable is regarded as in this state. If there are more than $30 \%$ of values are abnormal values, we are concerned about them; (ii) If the abnormal values are in the same state, such as Low or High, the value of the variable is regarded as in this state; (iii) if the abnormal values are in a different state, the value of the variable is regarded as a missing value. As a result, the total number of data used in the model is 1485 and the records with complications are 755 .

# 2.2 Data Preprocessing and Imputation 

We decided to rely on discrete state BNs. Thus each continuous variable has to be discretized. According to the criterion of age provided by the World Health Organization and the age distribution in the dataset, we set three cut-offs of it. For variables present nominally, we indexed them with the discrete values directly. In addition, for variables with normal range values, we set two or three discrete values of normal and high or low normal and high. The details and the abbreviations of variables are listed in Table 1.

Table 1: List of variables and their relative states.




There are three types of missing data prevalent in statistics literature [28], (a) Missing Completely at Random (MCAR), (b) Missing at Random (MAR) and (c) Missing Not at Random (MNAR). The probability of missing data classified as "MCAR" is independent of observed values and missing data. The probability of missing data classified as "MAR" does not depend on the missing values but the observed data of other features, while the probability of missing data classified as "MNAR" depends on both of them. In our dataset, we could regard all of the missing data as "MCAR" and "MAR" under the assumption that something like the staff in hospital deleted values on purpose or patients refused to do the tests would not happen. It means that we could use some imputation methods to process the missing data.

Multiple imputations are proved to be preferable rather than removing data entirely in some areas [29]. It is used in some literature for preprocessing missing values where the method called predictive mean matching usually presents the best performance when there are fewer than 50 percent cases including missing values [30-33]. Observing some missing values in the dataset, we used the VIM package embedded in RStudio to evaluate the distribution of missing values (refer to Figure 1). The red line takes up a part of the area, meaning that most of the missing values are about HbA1C and HighDensity Lipoprotein (HDL), which, however, take up fewer than 50 percent cases reported in Table 1 specifically.

![img-0.jpeg](img-0.jpeg)

Figure 1: Distribution of missing values.
Consequently, we did multiple imputations with predictive mean matching (PMM) for missing data [34-35]. Using the MICE package embedded in RStudio, we set the number of iterations to 50 to reduce the impact of random factors. The density of difference between before and after imputation is shown in Figure 2. It is worth noting that a good fitting effect is reported, so the dataset after processing could be used for model training.
![img-1.jpeg](img-1.jpeg)

Figure 2: Density plot.

For the discrete and orderly value of all variables, data are analyzed using Kendall rank correlation coefficient. As clear showed in Figure 3, the correlation between multiple variables reveals nearly linear independence, whereas the linear correlation shows between others. The Bayesian network is a method that can deal with the complex correlation between the variables and indicate more information about data. Therefore, we build the T2DM complication model based on it.
![img-2.jpeg](img-2.jpeg)

Figure 3: Maps of the correlation coefficients of variables.
The dataset was split into ten subsets of approximately equal size using 10 -fold cross-validation [36], namely nine subsets used for training and the rest one subset for testing in turn for ten times. It aims to prevent the BNs model from overfitting through learning the model with the training sets and using the test to measure its performance. In our study, we used all data with the bootstrap approach (refer to Section 2.4.1) to learn the structure of BNs and used the training set with 10 -fold cross-validation to do the parameters learning of BNs, calculating the mean values as the learning results. Ten times of probability prediction will be presented through some validation parameters as the final validation, with the purpose of a robust and effective model.

# 2.3 Bayesian Networks and Markov Blanket 

Bayesian networks (BNs) is annotated directed graphs that represent a set of variables as nodes in a network, connected by edges representing the conditional

probabilistic relations between them. A pair $(G, T)$, where $G$ represents a directed acyclic graph (DAG) and $T$ is the set of parameters quantifying the network, specifies a Bayesian network (BN) [37-38]. A Bayesian network $B$ always defines a joint probability distribution that could be factorized as a result of several conditional distributions over a set of random variables [39-40]:

$$
P_{B}\left(X_{1}, \cdots, X_{n}\right)=\prod_{i=1}^{n} P_{B}\left(X_{i} \mid \pi_{X_{i}}\right)=\prod_{i=1}^{n} \theta_{\left(X_{i} \mid \pi_{X_{i}}\right)}
$$

Note that $\Pi X_{i}$ denotes the parent nodes of the random variable $X_{i}$ and $\theta$ represents the conditional probability. It suggests that any node given the value of its parent nodes is conditionally independent of other all nodes that are not its descendants. This is known as Markov property [41]. The Markov blanket (MB) is the smallest subset of Bayesian network instantiating the property that all variables outside the MB could be deleted without influence on the target node and thus will have no impact on the accuracy of classification. It could be displayed as the following equation [42]:

$$
P(T \mid Y, M B(T))=P(T \mid M B(T)) \propto P\left(\pi_{T}\right) P\left(T \mid \pi_{T}\right) P\left(D_{T} \mid T\right) P\left(D_{T} \mid \pi_{D_{T}}, T\right) P\left(\pi_{D_{T}}\right)
$$

$M B(T)$ is the Markov blanket of target node $T . \pi_{T}$ represents the set of parent nodes of $T$ whose child nodes are illustrated as $D_{T}$, and thus $\pi_{D_{T}}$ describes the other parent nodes of $D_{T}$ except the node $T$. Hence, MB is usually used in the feature selection [4344]. There are three types of connections and d-separation in MB. One of the connections is called serial $(X \rightarrow Z \rightarrow Y$ or $X \leftarrow Z \leftarrow Y)$, known as the intermediate cause where $Z$ makes $X$ and $Y$ independent. The diverging connection is $X \leftarrow Z \rightarrow Y$, where $X$ is independent with $Y$ if $Z$ is instantiated and vice versa. That is known as the common cause. If a trail is shown as $X \rightarrow Z \leftarrow Y$ and $Z \rightarrow R$, it is regarded as a converging connection. It makes $X$ and $Y$ independent only if not knowing neither of $Z$ and $R$, which means common effect. The independence between $X$ and $Y$ reported above could be called that $X$ and $Y$ are d-separated. It could be concluded that if $X$ and $Y$ are d-separated by $Z, X$ and $Y$ are conditionally independent given by $Z$. Therefore, it is apparent that any node in the BN is d-separated of the nodes included in the nonMarkov blanket given its Markov blanket.

# 2.4 Learning Bayesian Networks 

There are two necessary steps to obtain a BN model: (i) structural learning to find the global optimum global structure proved as an NP problem, and (ii) parametric learning to estimate the conditional probability among nodes given a DAG. The entire process of building a T2DM complication model based on BN is presented in Figure 4.

![img-3.jpeg](img-3.jpeg)

Figure 4: The implementation flow of the T2DM model.

# 2.4.1 Structural Learning 

BNs learns the real probability distribution by updating the posterior distributions

according to the observed evidence, based on prior knowledge. Therefore, we focus on combining data-driven evidence with prior knowledge derived from previous research when learning the BN structure.

Sharma et al. [45] reported that total cholesterol (TC) and high-density lipoprotein (HDL) are related to cardiovascular diseases. According to Doliba et al. [46], Na+ levels may associate with the pathology of diabetic cardiomyopathy. Consequently, we assume that HDL, TC, and Na are related to DMV. Furthermore, Yang et al. [47] explored that $\mathrm{Na} v 1.3$ and $\mathrm{Na} v 1.7$, which are encoded by the Sodium ( Na ), contribute to the cause-effect relation between diabetes and painful neuropathy. Fadini et al. suggested that lower TRIG may protect kidney function from lip toxicity [48]. In other words, Na also seems to play an important role in the development of DPN and TRIG probably has an impact on DN.

Based on the prior knowledge mentioned above, we created a whitelist, which is summarized in Table 2. It presents the forced edges on outcome nodes in our structure. In addition, age and gender are the variables not determined by the model. More in general, the state of the two factors does not depend on the rest of the model. Therefore, we put the edges from two nodes to other nodes into a blacklist. The whitelist and the blacklist are integrated into the structure learning of BN classifier, which we will present in the following details.

Table 2: Forced edges on outcome nodes.


Two options could be chosen if several candidates' models can be accessed. One option is the most effective model, and the other is the average model that average over

the other models. The final structure of our model was obtained with the approach called bootstrap by repeating 500 times structure learning, namely 500 BNs were learned. Each network was explored with a Tabu Search algorithm (tabu) [49] according to the likelihood-equivalence Bayesian Dirichlet score with uniform priors (BDeu), merging the whitelist listed above and the blacklist where age and gender variables were never the parent nodes. We set the length of the Tabu list to 100 and the Tabu search iterations to 15 [50]. To ensure the robustness of the model, the network learned the averaged the arc strength of 500 models calculated by the conditional probability of two connected nodes. Consequently, arcs, whose strengths are above 0.8 , remained in the final structure given a threshold valued $80 \%$ (refer to Figure 5).
![img-4.jpeg](img-4.jpeg)

Figure 5: The network of T2DM complications model.

# 2.4.2 Parametric Learning 

Parameters are the probabilities distribution of all variables. As mentioned above, 10 -fold cross-validation was used to split the dataset into the training sets and test sets in parameter learning and make the estimation of the model accuracy. We can see the process of parametric learning in Figure 4. With ten subsets of approximately equal size divided in the beginning, the process repeated 10 times. There were nine subsets to train the model parameters with Maximum Likelihood Estimate (MLE) [51], and the rest subset was to validate the model performance with predicting probability using warning factors. After repeating for ten times, we calculate the average of conditional

probabilities $(\theta)$ of every node as the result of parameter learning and there were validation sets consisted of each test set and their predicting probability.

# 2.5 T2DM Complications Model and Warning Feature Analysis. 

To obtain a legible and unambiguous graphical representation from the structure and parameters of the T2DM complications model learned with bnlearn package in R language, we operated the BN in Netica (refer to Figure 6). As shown in Figure 6, the number of edges is high. Note that BNs structure learned by data-driven integrated with expert knowledge might have the ability to demonstrate more relationships between T2DM complications and physiological variables.
![img-5.jpeg](img-5.jpeg)

Figure 6: T2DM complications model operated in Netica.

As we can observe in Figure 6, the joint probability distribution of the BN model is factorized in 45 conditional probability tables (CPTs) where each table is for each node conditioned to the set of its parent nodes and presents the mean and standard deviation. It is worth noting that T2DM complications model seems to split the decision nodes and require two separate sub-networks to represent the original data distribution. Out of six T2DM complications, DR has no relationship with urine test items, HbA1c

and biochemical test items. In other words, urine test, HbA1c and biochemical test could not be able to predict DR, which would be explored in other features to examine the warning factors.

As for the other five complications, DK and DN variables are the child nodes of DMV variable, which is known as a common cause, and the connection between DK variable and DN variable is broken if DMV variable is initiated. Moreover, DMV variable is connected to DPN variable and DF variable through Na and HDL respectively.

The Market blanket of a variable consists of the set of its parent nodes, child nodes and the parent nodes of its child nodes as previously mentioned. The MB of DN variable is Age, TRIG, Cr and DMV variables, all of which are its parent nodes. That means the connection to DN variable via common cause trial and intermediate cause trial is broken if the MB is given. For DF and DPN variables, only the variables called HDL and Na are their MB respectively, which broke the trail to DMV variable. There are 10 variables including Age, TRIG, TC, Na, HDL that are parent nodes while DK and DN are child nodes. U-GLU, U-KET, Cr make the Markov blanket of DMV variables. As for DK variable, U-GLU, U-KET and DMV variables compose the MB. Table 3 summarizes the MB of five T2DM complications clearly.

Table 3: The Markov blanket of T2DM complications variables.


# 3. Results 

To ensure the effectiveness and robustness of our T2DM complication model, we have two kinds of performance comparison in this section. The first part refers to the

different baseline models including the Naïve Bayes model (NB) [52], Random Forest model (RF) [53], the C5.0 Decision Tree model (C5.0) [54]. We compare the performance from the perspective of several parameters with Area Under Curve (AUC) [55], $95 \%$ Confidence interval ( $95 \% \mathrm{CI}$ ), sensitivity and specificity. Following the formula described in (3) and (4), we could calculate sensitivity, which is also known as the true positive rate, and specificity which is known as true negative rate. Then we compare our validation parameters, especially AUC, with those in existing studies using some other variables in clinical data or biomedical data predicting T2DM complications to validate the performance of warning factors in the BN model in prediction in the second part.

$$
\begin{aligned}
& \text { Sensitivity }=\frac{T P}{T P+F N} \\
& \text { Specificity }=\frac{T N}{F P+T N}
\end{aligned}
$$

# 3.1 Performance Comparison between Models 

After the model learning, we validated the performance of prediction of the BN model using warning factors, and compared it with the NB, RF, and C5.0, which were used in the prediction of diseases with 10 -fold cross-validation. In order to make a comparison with other classifiers fair, a Bayesian network without prior information (BN-wopi) model was studied, where both structural learning and parametric learning were performed using 10 -fold cross-validation. The warning factors were selected according to the structure learned in each fold and were used to predict. The parameters of RF were set as follows: the number of variables randomly sampled as candidates at each split is set to three, and there are 100 trees allowed to grow. In relation to C5.0, the number of iteration was set to five. Note that warning factors were used to predict each outcome variable in the BN model and BN-wopi model, whereas all variables except the outcome variable were applied in classification tasks in NB, RF, and C5.0.

Because of dataset distribution and the number of positive cases and negative cases, it is not reasonable to take the threshold as 0.5 then calculate the confusion matrix or error ratio. However, AUC is a preferable method to validate the effect of models [56]

that takes the different predicted probabilities as the threshold and calculates the sensitivity and specificity respectively. Then there will be a Receiver Operating Characteristic Curve (ROC) and the area under it is the AUC.

We added the prediction probability and test data of each fold of different models to four lists in two columns respectively. Accomplished with each iteration, the prediction probability column in training datasets was taken as the threshold one by one, except the same value, to calculate the sensitivity, specificity and AUC, which were used together with $95 \%$ CI to illustrate the predictive effect of models in the last. Figure 7 describes the AUC, sensitivity and specificity indices of five models predicting the five complication variables each fold. In general, the two BN models outperformed other models in AUC and sensitivity.
![img-6.jpeg](img-6.jpeg)

Figure 7: Fold by fold comparison in AUC, sensitivity and specificity. From top to bottom and left to right, the complications are DN, DF, DMV, DPN and DK orderly.

The analysis of variance (ANOVA) test indicated that at least two models for the all evaluated indices are statistically significantly different ( $\mathrm{p}<0.05$ ) with 10 folds. Then, the p -values of the paired test regarding the AUC are summarized in Table 4. The statistical analysis indicated that two BN models performed statistically better than or similar to their counterparts. By comparing BN model and BN-wopi model, though there is a statistically significant difference in predicting some of the complications, they show basically equally powerful prediction.

In addition, as shown by the paired test results in Table 5, the sensitivity of two BN models are better than the other three models generally, whereas both BN models performed statistically similarly. In relation to specificity, other models statistically outperformed the BN models. However, note that their sensitivity reached a lower rate, which is undesirable for T2DM complications prediction using waring factors especially for self-management of patients. On the other hand, BN-wopi performed statistically better than or similar to BN model in the specificity of most of the complications except DPN complications.

Table 4 : The p-values of the paired test for the AUC in the prediction of five complications (DN and DMV are in the upper triangular part, DF, DPN and DK are in the lower triangular part). The symbols in parentheses denote: (=) not statistically different; $(+)$ statistically different, where the row is superior to the column; and $(-)$ statistically different, where the row is inferior to the column.




Table 6 lists detailed comparison result and Figure 8 shows the AUC of four models predicting the five complication variables. In relation to the different performance

between the two BN models, BN-wopi outperformed the BN model with prior information in the variables of DPN and DK. It is most likely because the expert knowledge was not reflected in the dataset consisting of a limit number of cases so that the fitting between data and structure of the model is not very well in the BN model. Moreover, the performance in sensitivity and specificity between the two BN models is opposite in the variables of DN and DF. The BN model performed better in sensitivity, whereas BN-wopi performed better in specificity. The values of sensitivity and specificity of a model depend on the point which is the closest to $(1,1)$ in order to maximize both of them on the coordinate plane (refer to Figure 8). To some extent, they are inverse. Due to the different structures, it is possible for two BN models that performed differently in sensitivity and specificity, which has little impact on the result of the comparison. Out of the four models learned using 10-fold cross-validation totally, it is clear that the BN-wopi model performs the best. When the confidence level is identical, narrower confidence intervention leads to the higher significance the AUC is. For the variables of DN, DPN and DK, the $95 \% \mathrm{CI}$ of BN-wopi model is the narrowest, and for DMV variable, BN-wopi model performs the second best. Therefore, the AUC could represent the effectiveness of models to some extent, which means BN models using warning factors could give the best classification performances out of the other three models.

Table 5: The p-values of the paired test for the sensitivity (upper triangular part) and specificity (lower triangular part) indices. The symbols in parentheses denote: $(=)$ not statistically different; $(+)$ statistically different, where the row is superior to the column; and $(-)$ statistically different, where the row is inferior to the column.



Table 6: Performance of different models. The value only in bold performs the best in the row out of the last four models. The value in bold and italic performs the best in the row out of all models and is from the BN model.



Consequently, our T2DM complications model with the Bayesian network classifies the condition of patient T2DM complications with the best performance using fewer variables. Furthermore, their graphical representation is very informative.

![img-7.jpeg](img-7.jpeg)

Figure 8: AUC of four models in five complication variables.

# 3.2 Performance Comparison with Other Experiments 

In order to demonstrate the performance of the BN model further in prediction and the ability of complications warning using features selected by MB methods, we summarize the performance of other experiments conducted previously in predicting T2DM complications.

There are some related studies in Table 7 and most of them validate the performance with AUC of about $80 \%$. For DK variables in five studies, more features demonstrate better effectiveness rather than one feature which needs to be examined

through the professional test. However, more feature means more resources are needed. In our model, there are four features that are available in medical examination to predict DK. Although the AUC in different models or studies does not have comparability of suggesting a better model, the AUC of $0.831[95 \% \mathrm{CI}: 0.7947-0.8665]$ is capable of proving that our model performs well in predicting DK. Moreover, the prediction of DF in our T2DM complications model are confirmed to be well with AUC of $0.905[95 \% \mathrm{CI}$ : $0.8841-0.9268]$, sensitivity of 1.0 , and specificity of 0.891 , while Irene et al. explored two methods with AUC of $0.776[95 \%$ CI: $0.702-0.849]$, sensitivity of 0.83 , specificity of 0.50 , and AUC of $0.816[95 \%$ CI: $0.757-0.874]$, sensitivity of 1.0 , specificity of 0.32 , respectively. Our model has a higher AUC of DMV prediction than AUC in existing related studies that is 0.75 on average. In other words, prediction in DMV also performs effectively with sensitivity of 0.827 , higher than other related studies' listed in Table 7. However, the AUC of 0.545 in prediction in DPN means that the Na variable does not predict DPN very well, whereas Lin et al revealed that serum uric acid demonstrates stronger predictive power to DPN. Few studies predict DK with clinical data or biomedical factors. Nevertheless, AUC of $0.877[95 \%$ CI: $0.8182-0.9362]$ could be seen as a well-formed model in general. Figure 9 shows the comparison of AUC of different related studies. Warmer color in the spectrum means a higher number of features.

Therefore, our model is proven to be effective in predicting DN, DF, DMV and DK based on the dataset. It might be beneficial in the prevention and self-management of diabetic patients in daily life.

Table 7: Performance and application of other relative studies



![img-8.jpeg](img-8.jpeg)

Figure 9: Comparison with AUC of different studies.

# 4. Discussion 

Following the results explored above, the BN model in this study is beneficial and useful to aid diabetic patients in preventing from four kinds of complications and to make self-care with just a few features that could be obtained in general medical examination. Moreover, we could instantiate some variables in the MB of every complication variable to attain more information about them.

First, we focus on the DN variable. It is worth noting that the people aged between 20 and 55 are more likely to have the DN complications with the probability of $18.5 \%$, whereas the probability is under $14 \%$ in the other age categories. In addition, if the Cr variable has an abnormal value, the probability for DN will increase from $13.9 \%$ to above $40 \%$ (refer to Figure 10). When the TRIG variable is instantiated to Chyle, Figure 10 shows the highest probability of DN variable of $41.8 \%$. Besides the impact of feature variables, DMV variable is also associated with DN variable. When the DMV is in positive state, there is a probability of $4.4 \%$ at having DN at the same time.

Consequently, diabetic patients could pay more attention to Cr and TRIG, especially for young people aged between 20 and 55 .

Because the positive cases of DF are below $3 \%$ of the sample size, the probability of DF in positive state is only $0.59 \%$. HDL is the only variable that needs to be paid attention to, which in high condition will lead to a rise to $3.43 \%$ in the probability of DF (refer to Figure 11).
![img-9.jpeg](img-9.jpeg)

Figure 10: Part of the T2DM complications model focus on DN variable and its MB.

![img-10.jpeg](img-10.jpeg)

Figure 11: Part of the T2DM complications model focus on DF variable and its MB.
Note that for DMV, there is a probability of $39.8 \%$ in the positive state of DMV in the people aged over 70 years old, which is the group of the highest probability. Furthermore, if TC, Na, HDL variables are in High state and TRIG variable is in Chyle state respectively, there is always a rise in the probability of DMV. As we can see in Figure 12, the state of DN variable has no impact on DMV when the TC, Na, HDL variables are in High state, TRIG variable is in Chyle state, and Age variable is in the category of 56-69 state or over 70 whereas DK in the positive condition could have negative relationship with the DMV variable. In other words, it is just a little possibility for an elder to have DK and DMV at the same time when TC, Na, HDL, TRIG are all in a poor state. Diabetic patients who are in the condition would not focus on the DN and Cr variables. Then, both of U-GLU and U-KET variables could have a positive influence on DMV when DK is in negative condition.
![img-11.jpeg](img-11.jpeg)

Figure 12: Part of the T2DM complications model focus on DMV variable and its MB.

For the DK variable, U-KET is the most important factor that the probability of DK increases from $3.24 \%$ to $11.6 \%$ when the state of U-KET is in positive. U-GLU also has a positive impact on DK variables (refer to Figure 13).
![img-12.jpeg](img-12.jpeg)

Figure 13: Part of the T2DM complications model focus on DK variable and its MB.
The data we used to build the model is from the inpatients who have already been diagnosed with various kinds of T2DM complications followed the principle of authenticity and professional characteristic, which means that the warning factors in BN model might be applied to self-monitoring of T2DM patients and the assistant treatment of T2DM complications. The model built in this paper aims to predict the condition of complications with warning features. Therefore, the analysis for warning factors of T2DM complications may be helpful to avoid or limit as much as possible two situations: (i) patients worried about T2DM complications may have access to ambulatory visit and health care services unnecessarily too often, and (ii) patients with no realization wait too long before they go to hospital and complications may occur.

The one probable application scenario is that patients with T2DM use warning factors to predict the probability of T2DM complications. There is a certain threshold for each outcome variable in the model to distinguish the positive state and negative state, which means the highest accepted negative value. If the conditional probability of one of the complications is higher than the threshold when patients instantiate the warning factors, they are more likely to have had complications. It is advised for patients to see the doctor and do the relevant examination so that they could detect the complications or treat the disease as early as possible.

In addition, it might be beneficial for diabetic patients to focus on the warning features and use warning features to monitor their physical condition related to

complications before entering the hospital. If the warning features are at a normal level but close to the threshold value of the high or low, taking actions to control them around the average normal level might be beneficial. A diabetic patient, for example, finds that his HDL is $1.5 \mathrm{mmol} / \mathrm{L}$ close to the threshold of high state. It might be good for him to do some exercise or have a more healthy diet to decrease the level of HDL which is related to DMV.

Furthermore, the warning features could be obtained easily in medical examinations, which is convenient for diabetic patients to do self-management in daily life.

# 5. Conclusions 

Analysis of warning factors of T2DM complications is necessary and significant. In this study, the warning factors of T2DM complications including urine test data, glycated hemoglobin (HbA1c) and biochemical test data with MB based on a BN model were found out and analyzed, and T2DM complications were predicted in a T2DM cohort. It was learned from the dataset related to complications of T2DM provided by PLAGH. According to the missing value, we did multiple imputations with PMM and split the dataset into the training set and testing set with 10 -fold cross-validation. For different variables, we set two, three or four thresholds.

Based on the prior knowledge, the structure of the BN model was built with Bootstrap and Tabu search algorithm merging data information and expert knowledge, which made a strong foundation of warning factors analysis. In addition, parameters of the model are learned with MLE and 10 -fold cross-validation was used to learn 10 times. The MB is used to select the warning features.

We also compared the performance of BN model and BN without prior information model using warning factors with the Naïve Bayes model, the Random Forest model, and C5.0 Decision Trees model using all other variables in prediction from the perspective of AUC, $95 \% \mathrm{CI}$, sensitivity and specificity. Finally, the two BN models

predicting the warning factors of outcome variables was proved the best. Then the comparison with other experiments was also carried out, the result of which indicated that the prediction in DN, DF, DMV and DK variables with warning factors was practically significant based on the dataset. Moreover, we made inferences of outcome variables with warning factors and reported the context of potential clinical assistant treatment of T2DM complications.

Due to the limitation of sources and ways of collecting data, we could not get the further dataset on which we could make a prediction and perform the assessment. Besides, the method used in imputation which created correlations between samples leading to independent folds could be prompted. In terms of future directions, we intend to use more T2DM complication cases to test our model and train our model again and again to analyze warning factor more deeply, and improve our health management system in predicting tasks with these warning factors. The methods of processing missing data also needed to be explored further to make model building and assessment more reasonable. In addition, more features that are easy to be accessed to will be considered in our model to make predictions with warning features more convenient and reliable.

# Conflicts of interest 

We declare that we do not have any commercial or associative interest that represents a conflict of interest in connection with the work submitted.

## Acknowledgments

This research is supported by the National Natural Science Foundation of China (key program) (Grant number 71532002, 61702023), a major project of the National Social Science Foundation of China with grant number 18ZDA086, and a key project of Beijing Social Science Foundation Research Base (Grant number 18JDGLA017).
