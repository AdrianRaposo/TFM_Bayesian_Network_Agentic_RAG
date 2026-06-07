# Mining causal relationships among clinical variables for cancer diagnosis based on Bayesian analysis 

LiMin Wang ${ }^{1,2}$

Correspondence: wanglim@jlu.edu.cn
${ }^{1}$ Key Laboratory of Symbolic
Computation and Knowledge
Engineering of Ministry of
Education, Jilin University, 130012
ChangChun, P. R. China
${ }^{2}$ State Key Laboratory of Computer Science, 100080 Beijing, P. R. China


#### Abstract

Background: Cancer is the second leading cause of death around the world after cardiovascular diseases. Over the past decades, various data mining studies have tried to predict the outcome of cancer. However, only a few reports describe the causal relationships among clinical variables or attributes, which may provide theoretical guidance for cancer diagnosis and therapy. Different restricted Bayesian classifiers have been used to discover information from numerous domains. This research work designed a novel Bayesian learning strategy to predict cause-specific death classes and proposed a graphical structure of key attributes to clarify the implicit relationships implicated in the data set.


Results: The working mechanisms of 3 classical restricted Bayesian classifiers, namely, NB, TAN and KDB, were analysed and summarised. To retain the properties of global optimisation and high-order dependency representation, the proposed learning algorithm, i.e., flexible $K$-dependence Bayesian network (FKBN), applies the greedy search of conditional mutual information space to identify the globally optimal ordering of the attributes and to allow the classifiers to be constructed at arbitrary points (values of $K$ ) along the attribute dependence spectrum. This method represents the relationships between different attributes by using a directed acyclic graph (DAG) model. A total of 12 data sets were selected from the SEER database and KRBM repository by 10 -fold cross-validation for evaluation purposes. The findings revealed that the FKBN model outperformed NB, TAN and KDB.
Conclusions: A Bayesian classifier can graphically describe the conditional dependency among attributes. The proposed algorithm offers a trade-off between probability estimation and network structure complexity. The direct and indirect relationships between the predictive attributes and class variable should be considered simultaneously to achieve global optimisation and high-order dependency representation. By analysing the DAG inferred from the breast cancer data set of the SEER database we divided the attributes into two subgroups, namely, key attributes that should be considered first for cancer diagnosis and those that are independent of each other but are closely related to key attributes. The statistical analysis results clarify some of the causal relationships implicated in the DAG.

Keywords: Causal relationship, Cancer diagnosis, Restricted Bayesian classifier

# Background 

Cancer is the second leading cause of death around the world after cardiovascular diseases. Predicting the outcome of cancer is one of the most interesting and challenging tasks for data mining applications. To realise such a task, medical research groups collect large volumes of medical data and employ computers with automated tools. Thus data mining techniques have become a popular research tool among medical researchers for identifying and exploiting patterns and relationships among numerous variables, interpreting complex diagnostic tests and predicting the outcome of a disease by historical data sets. The rapid progress of data mining research has led to the development of medical diagnostic support systems, which are now extensively applied across a wide range of medical area, such as cancer research, gastroenterology and heart diseases. Pena and Sipper [1] indicated that effective diagnostic systems should provide high-accuracy disease identification. Effective systems should also confidently indicate the accuracy of the diagnosis with some levels. Another major important aspect of competent systems is their interpretability, i.e., providing information on the steps followed to obtain outcomes.

Cancer diagnosis has received considerable attention from researchers, and many classical data mining algorithms have been used in medical data analysis. Decision trees can be easily understood and interpreted for domain experts. This area has been extensively explored for the past few years. Learned trees can be represented as a set of "if-then rules" that improve human readability. C5.0 is one of the most important algorithms in the decision tree family. Rafe et al. [2] used the C5.0 algorithm to develop a model for Clementine software and to form a confusion matrix. The database used for the experimental study was "Wisconsin Breast Cancer database", which contains 10 attributes and 699 instances. By using the boosting method, the precision of the final model can be increased to decrease the percentage of error. Khan et al. [3] proposed a hybrid prognostic scheme based on weighted fuzzy decision trees(FDT). Such a scheme is an effective alternative to crisp classifiers that are applied independently. A hybrid prognostic scheme analyses the hybridisation of accuracy and interpretability in terms of fuzzy logic and decision trees. They used the Surveillance Epidemiology and End Results (SEER) database (1973 to 2003) of the National Cancer Institute, which consists of 162,500 records with 17 variables after pre-processing. The resulting AUC values were 0.69 and 0.77 for FDT and weighted FDT, respectively. Carefully designed pre-processing procedures help achieve the removal/modification/splitting of key attributes. Agrawal et al. [4] discovered 2 of the 11 derived attributes that have significant predictive power. These researchers employed the ensemble voting of 5 decision tree-based classifiers and meta-classifiers to acquire the best prediction performance in terms of accuracy and area under the ROC curve. The experimental study was performed on the pre-processed data along with various data mining optimisations and validations.

Artificial neural networks (ANNs) are commonly known as biologically inspired, highly sophisticated analytical techniques that can model extremely complex non-linear functions. ANNs have been proven to be an effective classification tool even in hidden operations within a network structure. Motalleb [5] incorporated a multilayer feedforward neural network with an error back-propagation algorithm to develop a predictive model. The input parameters of the model were virus dose, week and tamoxifen citrate. Tumour weight was included in the output parameter. Two different training algorithms, namely, quick propagation and and Levenberg-Marquardt, were used to train ANN.

To minimize user effort, Vukicevic et al. [6] applied genetic algorithms to achieve the best prognostic performances relevant for clinicians (i.e., correctness, discrimination and calibration). The only 2 user dependent tasks were data selection (input and output variables) and the evaluation of the ANN threshold probability with respect to regret theory (RT). After optimally configuring ANNs with respect to these criteria, the clinical usefulness was evaluated by the RT Decision Curve Analysis. Tsao et al. [7] developed an ANN model to predict prostate cancer pathological staging in patients prior to receiving radical prostatectomy. This experimental study examined the cases of 299 patients undergoing retro-pubic radical prostatectomy. In this investigation, the validation was assessed by using the current Partin Tables for the Taiwanese population. ANN induced larger AUCs and provided a more accurate prediction of the pathologic stage of prostate cancer.

Bayesian networks (BNs) are characterised by the use of the probabilistic approach in solving problems and encompass the uncertainty of specific occurrences. The origin of BNs is based on probability distribution, which can be graphically depicted. Alexander et al. [8] applied the SEER database (1969 to 2006) to form a clinical decision support system for the real-time estimation of the overall survival (OS) rate of colon cancer patients. The BN model accurately estimated OS with an area under the receiver-operating characteristic curve of 0.85 . They significantly improved upon the existence of AJCC stage-specific OS estimates. Furthermore, they determined the significant differences in OS between low- and high-risk cohorts. Khan et al. [9] used Bayesian method to derive the posterior density function for the parameters and the predictive inference for future survival times from the exponentiated Weibull model, assuming that the observed breast cancer survival data follow such type of model. The Markov chain Monte Carlo method was used to determine the inference for the parameters. They found that the exponentiated Weibull model fits the male survival data. Mean predictive survival times, $95 \%$ predictive intervals, predictive skewness and kurtosis were obtained. Jong et al. [10] introduced a hybrid model that combined ANN and BN to obtain a good estimation of prognosis and a good explanation of the results. In this research, the SEER database (1973 to 2003) was employed to construct and evaluate the proposed models. Nine clinically acceptable variables were selected to be incorporated into the nodes of the proposed models. Consequently, the hybrid model achieved the highest area under the curve value of 0.935 , and the corresponding values of ANN and BN were 0.930 and 0.813 , respectively.

Other machine learning models have also been applied to solve the problems in predicting cancer survivability. Molina et al. [11] suggested that an incremental learning ensemble of a support vector machine (SVM) must be implemented to adapt to the working conditions in medical applications and to improve the effectiveness and robustness of the system. These studies calculated the probability estimation of cancer structures by using SVM and performed the corresponding optimisation with a heuristic method together with a three-fold cross-validation methodology. Mahmoodian et al. [12] developed a new algorithm on the basis of fuzzy association rule mining to identify fuzzy rules and significant genes. In this study, different subsets of genes that have been selected by different methods were used to separately generate primary fuzzy classifiers. Subsequently, the researchers administered their proposed algorithm to mix the genes associated with the primary classifiers and to generate a novel classifier.

Only a limited number of conditional probabilities can be encoded into BN because of time limitation and space complexity. The restricted BN classifier family can offer different trade-offs between structure complexity and prediction performance. The conditional independence assumption and different levels of extra dependencies between predictive attributes signify that some learning algorithms (e.g., Naive Bayes (NB) [13,14], treeaugmented Naive Bayes (TAN) [15] or $K$-dependence BNs (KDB) [16,17] are popular ever since they were developed both for learning BN parameters and data structures. An optimal Bayesian classifier should capture all or at least the most important dependencies among attributes that exist in a database. In the next section, the working mechanisms of three popular restricted BN classifiers (i.e., NB, TAN and KDB) are summarised. Consequently, the proposed learning algorithm, namely, the flexible $K$-dependence Bayesian network (FKBN), applies greedy search in conditional mutual information (CMI) space to maximise the information flow between attributes and to globally describe causal relationships while maintaining high dependency representation. The proposed algorithm also allows the construction of classifiers at arbitrary points (values of $K$ ) along the attribute dependence spectrum. We compare these classical Bayesian models that predict the survivability of patients diagnosed with breast cancer. In this study, such a prediction is addressed by a classification problem that predicts whether the patient belongs to the group of those who survived after a specified period. We aim to determine an accurate and stable classification model that will allow medical oncologists to make efficient decisions for treating cancer patients.

# Materials and methods 

## Data

For this experimental study, 12 data sets are selected and collected to clarify the clinical implications of the causal relationship among clinical variables and to discuss the application of the proposed method to the high-dimensional genomic data. Table 1 summarises the characteristics of each data set, including the numbers of instances, attributes and classes. The first 6 data sets are collected from the SEER database [18], which is a unique, reliable and essential resource for investigating the different aspects of cancer. Moreover, this database combines patient-level information on cancer site, tumour pathology, stage

Table 1 Data sets for experimental study


The first six data sets are selected from the SEER database, the next six data sets are selected from Kent Ridge Bio-medical (KRBM) repository.

and cause of death. The remaining 6 data sets (e.g., gene expression, protein profiling and genomic sequence that are related to classification) are acquired from the Kent Ridge Bio-Medical (KRBM) repository [19].

# Restricted Bayesian classifier 

Bayes' chain rule can be used to form a classifier for an input vector $X=\left\{X_{1}, \cdots, X_{n}\right\}$ and class variable $C$.

$$
P(c \mid x)=\frac{P(c) P(x \mid c)}{P(x)} \propto P(c) P(x \mid c)=P(c) P\left(x_{1} \mid c\right) P\left(x_{2} \mid x_{1}, c\right) \cdots P\left(x_{n} \mid c, x_{1}, \cdots, x_{n-1}\right)
$$

Where the lower case letters represent the possible values taken by the corresponding attributes. If Eq.(1) is represented by Bayesian model, the attribute vector $\left\{C, X_{1}, \cdots, X_{i-1}\right\}$ is considered the parent attribute of $X_{i}$, i.e., $P a_{i}$.

- NB (0-dependence classifier). In NB, class label $c^{*}$ will be inferred from a Bayesian model of an $n$-dimensional attribute (input) vector $X$, which is conditionally independent given class variable $C$

$$
c^{*}=\arg \max P(c) P(x \mid c)=\arg \max P(c) \prod_{i=1}^{n} P\left(x_{i} \mid c\right)
$$

Corresponding belief network is graphically depicted in Figure 1(a). Each predictive attribute node in NB has the class variable as its only parent. Therefore, NB enjoys the benefit of not being required to learn the structure, and probabilities $P(c)$ and $P\left(x_{i} \mid c\right)$ can be easily estimated from training instances. Figure 1(b) illustrates that all causal relationships among the predictive attributes are removed; thus, NB is the simplest form of BNs. However, the conditional independence assumption made by NB is rarely valid in reality.

- TAN (1-dependence classifier). In effectively weakening the conditional independence assumption of NB, structure extension is the most direct procedure for improving NB because attribute dependencies can be explicitly represented by arcs. TAN introduces
![img-0.jpeg](img-0.jpeg)

Figure 1 The 0-dependence relationship among attributes of NB model and corresponding $P a_{i}$ of each attribute $X_{i}$ are as (a) and (b) show, respectively. The attributes annotated with symbol "-" represent those redundant ones for NB. For simplicity, class label is not included in $P a_{i}$.

more dependencies by allowing each attribute node to have at most one parent. An example of the network structure of TAN with five attributes and with corresponding causal relationships are depicted in Figure 2(a) and (b), respectively. By developing a maximum weighted spanning tree, TAN achieves a globally optimal trade-off between the complexity and learnability of the model. However, the number of dependencies that can be represented is limited, and this algorithm cannot be extended to handle high-dependence relationships. The weight of arcs is calculated by using $\operatorname{CMI}\left(X_{i}, X_{j} \mid C\right)$.

- KDB ( $K$-dependence classifier). The probability of each attribute value in KDB is conditioned by the class and other $K$ attributes. The KDB algorithm adopts a greedy strategy to identify the graphical structure of the resulting classifier. KDB also achieves the weights of the relationship between attributes by computing CMIs that can be illustrated in a matrix. Figure 3 demonstrates the format of the matrix and an example of KDB with four predictive attributes. KDB is guided by a rigid order that is obtained by applying mutual information between predictive attributes and class variables. Mutual information does not consider the interaction among predictive attributes. This marginal knowledge may result in suboptimal order. Without loss of generality, the attribute order is assumed to be $\left\{X_{1}, \cdots, X_{4}\right\}$ by comparing mutual information. Figure 4(a) indicates the corresponding network structure of KDB when $K=2$, and the causal relationships are depicted in Figure 4(b). Although the causal relationship between $X_{2}$ and $X_{1}$ is the weakest, the latter is selected as the parent attribute of the former. By contrast, the strong causal relationship between $X_{4}$ and $X_{1}$ is neglected.


# The FKBN Algorithm 

By considering more attributes as possible parent attributes, prediction performance will be improved because the chain rule is approximately achieved. FKBN applies greedy search in CMI space to represent the strongest causal relationships and to retain the privileges of TAN and KDB (i.e., global optimisation and higher dependency representation). On the basis of this condition, FKBN adds high dependencies at arbitrary points (values of $K$ ) along the attribute dependence spectrum such as KDB. The newly added arc corresponds to the strongest relationship that is not implicated in the existing tree structure.
![img-1.jpeg](img-1.jpeg)

Figure 2 The 1-dependence relationship among attributes of TAN model and corresponding $P a_{i}$ of each attribute $X_{i}$ are as (a) and (b) show, respectively. The attributes annotated with symbol "-" represent those redundant ones for TAN. For simplicity, class label is not included in $P a_{i}$.


(a)


(b)

Figure 3 The format and an example of $C M I$ matrix are as (a) and (b) show, respectively. Because of the symmetrical characteristic of conditional mutual information, only the lower triangular matrix is shown.

The direction of each arc should point outward to ensure the characteristic of the directed acyclic graph. In this research, we also use CMI to measure the weight of the relationship between attributes. Assuming that $\left\{X_{1}, X_{2}, \cdots, X_{n}\right\}$ are $n$ attributes and $C$ is the class variable, the learning algorithm of FKBN is depicted as follows:

# Algorithm 1: FKBN 

Input: A database of pre-classified instances, DB, and the $K$ value for the maximum allowable degree of attribute dependence.
Output: A $K$-dependence Bayesian classifiers with conditional probability tables determined from the input data.

1. Compute the $C M I$ between each pair of attributes and build the $C M I$ matrix. Compute the mutual information $I\left(X_{i} ; C\right)$ for each attribute $X_{i}$.
2. Repeat until $B N$ includes all domain attributes

- Add a node to $B N$ representing $X_{i}$.
- Add an arc from $C$ to $X_{i}$ in $B N$.

3. Select the one $I\left(X_{i} ; X_{j} \mid C\right)$ that corresponds to the largest value in CMI matrix and set $X_{i}$ as the root attribute $X_{\text {root }}$ if $I\left(X_{i} ; C\right)>I\left(X_{j} ; C\right)$.
4. Repeat until at most $K$ parent attributes can be selected for each attribute.

- Select the one $I\left(X_{i} ; X_{j} \mid C\right)$ that corresponds to the largest value that remains in CMI matrix.
- Transform the undirected arc $X_{i}-X_{j}$ to a directed one by setting the direction to be outward from $X_{\text {root }}$.
- Add the directed arc to $B N$.
- Remove $I\left(X_{i} ; X_{j} \mid C\right)$ from the CMI matrix.

5. Compute the conditional probability tables inferred by the structure of $B N$ using counts from DB, and output $B N$.

In the above description of the algorithm, Step 4 requires the selection of most $K$ parents for each attribute. We set $K=2$ in the following discussion. When $K=2$, Figure 5(a) shows the network structure of FKBN corresponding to the CMI matrix shown in Figure 3. The causal relationships in this case are depicted in Figure 5(b). All strong causal relationships are implicated in the final network structure.

The experimental research has been performed with the approval of the ethics committee of JiLin University of China.

![img-2.jpeg](img-2.jpeg)

Figure 4 The $K$-dependence relationships among attributes inferred from KDB and an example of CMI matrix are as (a) and (b) show, respectively. The unused causal relationship in (b) is annotated in pink.

# Software and programs 

The following algorithms are compared:

- NB, standard Naive Bayes.
- TAN[20], Tree-augmented Naive Bayes applying incremental learning.
- KDB, standard $K$-dependence Bayesian classifier.

The experimental system is implemented in C++. The missing values for the qualitative and quantitative attributes are replaced with modes and means from the training data, respectively. For each benchmark data set, numeric attributes are discretised by using MDL discretisation[21]. Base probability estimates $P(c), P\left(c, x_{i}\right)$ and $P\left(c, x_{i}, x_{j}\right)$ are smoothed by using the Laplace estimate:
![img-3.jpeg](img-3.jpeg)

Figure 5 The $K$-dependence relationships among attributes inferred from FKBN and an example of CMI matrix are as (a) and (b) show, respectively. The unused causal relationship in (b) is annotated in pink.

$$
\left\{\begin{array}{l}
\hat{P}(c)=\frac{F(c)+1}{K_{i}+k} \\
\hat{P}\left(c, x_{i}\right)=\frac{\hat{F}\left(c, x_{i}\right)+1}{K_{i}+k_{i}} \\
\hat{P}\left(c, x_{i}, x_{j}\right)=\frac{\hat{F}\left(c, x_{i}, x_{j}\right)+1}{K_{i j}+k_{i j}}
\end{array}\right.
$$

where $F(\cdot)$ is the frequency with which a combination of terms appears in the training data, $K$ is the number of training instances for which the class value is known, $K_{i}$ is the number of training instances for which both the class and attribute $X_{i}$ are known, $K_{i j}$ is the number of training instances for which all of the class, and attributes $X_{i}$ and $X_{j}$ are known. $k$ is the number of attribute values of class $C, k_{i}$ is the number of attribute value combinations of $C$ and $X_{i}$, and $k_{i j}$ is the number of attribute value combinations of $C, X_{j}$ and $X_{i}$.

# Results 

In machine learning, one of the standard measures of predicting the performance of trained models is zero-one loss, which is a powerful tool from sampling theory statistics used for analysing supervised learning scenarios [22]. Suppose $c$ and $\hat{c}$ are the true class variable and the outcome of a learning algorithm, respectively, the zero-one loss function is construed as follows:

$$
\xi(c, \hat{c})=1-\delta(c, \hat{c})
$$

where $\delta(c, \hat{c})=1$ if $\hat{c}=c$ and 0 otherwise. When the zero-one loss is lower, the prediction performance of a corresponding classifier is better. If the amount of data is satisfactorily large, the average zero-one loss can be estimated by using computer intensive resampling methods such as cross-validation. Cross-validation mimics the use of training and test sets by repeatedly training the algorithm $N$ times with a fraction $1 / N$ of training examples left out for testing purposes. Table 2 presents the comparative results of zero-one loss estimated by 10 -fold cross-validation to accurately estimate the average performance of an algorithm.

Table 2 Experimental results of zero-one loss and standard deviation


The first six data sets are selected from the SEER database, the next six data sets are selected from Kent Ridge Bio-medical (KRBM) repository.

Friedman proposed a non-parametric measure [23], Friedman test $(F T)$, which ranks the algorithms for each data set separately by comparing zero-one loss. The best performing algorithm getting the rank of 1 , the second best rank $2, \cdots$. In case of ties, average ranks are assigned. Let $r_{i}^{j}$ be the rank of the $j$-th of $k$ algorithms on the $i$-th of $N$ data sets. $F T$ compares the average ranks of algorithms, $R_{j}=\frac{1}{N} \sum_{i} r_{i}^{j} \cdot F T$ helps to compare and evaluate the overall prediction performance of different learning algorithms when dealing with numerous data sets. A difference is considered to be significant when the outcome of a two-tailed binomial sign test is less than 0.05 . The experimental results of $F T$ are shown in Table 3. By comparing average $F T$ we can see that, the order of these algorithms is \{FKBN, KDB, TAN, NB\}.

The prediction superiority of FKBN to the other classifiers is remarkably obvious especially when dealing with large data sets. The main reason for such a condition may be the case that, when data size is large enough for probability estimation and relational dependency representation, the credible conditional dependencies among attributes extracted based on information theory play a key role in prediction. By generating a maximal spanning tree, TAN can achieve a trade-off between the model and computational complexity. Therefore, although TAN is restricted to have at most one parent node for each predictive attribute, its structure is more reasonable than NB and can relatively exhibit relationship between attributes. FKBN further relaxes the assumption by allowing at least two attributes to be parents and to increase the robustness of the final model. Furthermore, FKBN can fully extract the causal relationship between attributes by applying a dynamic searching strategy in the early building stage to identify the optimal attribute order. In this event, the final model is significantly flexible and credible.

From the viewpoint of dependency complexity, NB expresses zero-dependence because no dependency relationship exists between attributes. Similarly, TAN is a one-dependence based-Bayesian classifier. KDB and FKBN are two-dependence basedBayesian classifiers. The KRBM data sets are exceedingly small; thus, the conditional dependencies measured by the CMI are weak. Accordingly, all high-dependence Bayesian classifiers (e.g., TAN, KDB or FKBN) degenerate to be NB. The results of zero-one loss reveal that they perform almost the same when dealing with KRBM data sets.

Table 3 Experimental results of Friedman test


A difference is considered to be significant when the outcome of a two-tailed binomial sign test is less than 0.05 .

# Discussion

Breast cancer is the second leading cancer responsible for the highest mortality rate among women. Early detection and diagnosis are proven to be the only means of curbing this disease and of reducing its mortality rate. Physicians must have access to a smart system for predicting this illness on time before it is too late to be treated. Predicting the outcome of cancer and detecting dependencies among clinical variables or attributes play a pivotal role in cancer diagnosis and therapy. Over the past decades, many data mining studies have tried to predict the five-year survival rate of breast cancer patients. However, even the most accurate predictive forecasts have limited value unless they can also provide clear action procedures to induce the desired results.

To clarify the FKBN algorithm more clearly, we also choose 20 attributes as described in [24] from breast cancer data set in SEER database. The detailed information of the selected attributes is shown in Table 4 and is employed to develop the Bayesian model. Cause-specific death prediction is used as the class label. The graph model of the predictive attributes in the breast cancer data set (Figure 6) is generated on the basis of the results of the FKBN analysis. Figure 6 demonstrates that the attributes $X_{\text {key }}=$ $\left{X_{13}, X_{11}, X_{5}, X_{15}, X_{16}, X_{17}, X_{3}, X_{7}, X_{2}, X_{10}, X_{14}\right}$, which correspond to $\left{R x\right.$-SummSurg-/-Rad-Seq, Rx-SummSurg-Prim-Site, Grade, SEER-historic-stage-A, SEER-Summary-Stage1977, Number-of-primaries, Primary-Site, EOD-Extension, Age-at-diagnosis, Regional-Nodes-Examined and CS-Schema-v0203), play key roles for prediction. These attributes have the same characteristics (i.e., they are affected by other attributes and also act on

Table 4 Attributes available for analysis


![img-4.jpeg](img-4.jpeg)
other attributes). The other attributes are not parents of any other attributes and play a secondary role. For example, attribute $X_{1}$, i.e. Sex, is dependent on $X_{2}$ (Age-at-diagnosis) and $X_{14}$ (CS-Schema-v0203). The causal relationships among these attributes are summarised in Figure 7. From the viewpoint of medical diagnosis, the key attributes should be considered first. Subsequently, the non-key attributes, which are dependent on key attributes, should then be extensively analysed. For example, the local dependent and independent structures of $X_{17}$ are shown in Figure 8. Attribute $X_{17}$ is directly dependent


Figure 7 The causal relationships inferred from breast cancer data set of SEER database. Attributes $\left\{X_{0}, X_{1}, \cdots, X_{18}\right\}$ correspond to clinical variables Race, Sex, Age, Primary-Site, Histologic-Type, Grade, EOD-Tumor-Size, EOD-Extension, EOD-Lymph-Node-Involve, Regional-Nodes-Positive, Regional-Nodes-Examined, Rx-Summ-Surg-Prim-Site, Rx-Summ-Sur-Oth-Req, Rx-Summ-Surg-/-Rad-Seq, CS-Schema-v0203, SEER-historic-stage-A, SEER-Summary-Stage-1977, Number-of-primaries and First-malignant-primary-indicator, respectively.

![img-5.jpeg](img-5.jpeg)

**Figure 8** The local independent and dependent network structure of attribute *X*<sub>17</sub> on SEER data set are as **(a)** and **(b)** show, respectively. Attributes {*X*<sub>0</sub>, *X*<sub>1</sub>, *X*<sub>2</sub>, *X*<sub>5</sub>, *X*<sub>7</sub>, *X*<sub>8</sub>, *X*<sub>9</sub>, *X*<sub>10</sub>, *X*<sub>11</sub>, *X*<sub>14</sub>, *X*<sub>15</sub>, *X*<sub>16</sub>, *X*<sub>17</sub>} correspond to clinical variables *Race, Sex, Age, Grade, EOD-Extension, EOD-Lymph-Node-Involve, Regional-Nodes-Positive, Regional-Nodes-Examined, Rx-Summ-Surg-Prim-Site, Rx-Summ-Surg-/-Rad-Seq, CS-Schema-v0203, SEER-historic-stage-A, SEER-Summary-Stage-1977, Number-of-primaries* and *First-malignant-primary-indicator*, respectively.

on attributes {*X*<sub>16</sub>, *X*<sub>15</sub>} (Figure 8(a)), which are dependent on {*X*<sub>11</sub>, *X*<sub>5</sub>}. In this case, *X*<sub>13</sub> is the final cause. Doctors can follow this order to lower the time cost for diagnosis and expenditure on unnecessary physical examination. On the other hand, Figure 8(b) demonstrates that the attributes {*X*<sub>0</sub>, *X*<sub>7</sub>} are directly dependent on *X*<sub>17</sub> and their values may be affected by *X*<sub>17</sub>. Furthermore, {*X*<sub>2</sub>, *X*<sub>8</sub>} and then {*X*<sub>9</sub>, *X*<sub>10</sub>, *X*<sub>1</sub>, *X*<sub>14</sub>} will be affected by *X*<sub>17</sub> indirectly. In the following discussion, we will clarify Figure 6 with respect to several common relationships *Sex/Age, Race/SEER-Summary-Stage* and *Tumor Size/Race*, respectively.

*Sex/Age*: Approximately 343,919 cases of breast cancer were expected to be diagnosed in women, along with 2,398 cases in men. Figure 6 indicates that a direct relationship exists between the *Sex* (*X*<sub>1</sub>) and *Age* (*X*<sub>2</sub>). Accordingly, *Age* should be considered a complementary factor of *Sex* for cancer diagnosis. A statistical analysis of the breast cancer data set reveals that incidence rate begins to increase when the woman is 40 years old and reaches its maximum between 54 and 68 years old. This event may be due to tumours diagnosed at younger ages being more aggressive and/or less responsive to treatment. The age of 40 is also a turning point for mortality rate. The mortality rate of women decreases when their age increases from 0 to 40. The mortality rate will then remain stable when the age is between 40 and 70. When the age increases from 70 to 110, the mortality rate will increase and reach its maximum. Older patients may reflect lower rates of screening, detection of cancers via mammography and/or incomplete detection. In this research, the determined median age at the time of breast cancer diagnosis was 60.78. This finding implies that half of women who developed breast cancer were 61 years old or younger at the time of diagnosis. Meanwhile, similar to female breast cancer, the cause-specific mortality rates of male breast cancer generally increase with age. Given the infrequency of male breast cancer, which accounts for less than 1% of all breast cancer cases, remarkably less confident information can be inferred to predict the outcome of such a disease.

Race/SEER-Summary-Stage: The American Cancer Society has determined notable differences in breast cancer mortality rates between different states across various socioeconomic strata and between different racial/ethnic groups. The statistical analysis of breast cancer data set illustrates that Caucasian women are more likely to develop breast cancer. In fact, Caucasian women account for $84.92 \%$ of all breast cancer cases and African-American women account for only $10.23 \%$ of all cases. However, a substantial racial gap can be observed in mortality rate. In particular, the findings of this research indicated that the morality rate for Caucasian and African-American women were 7.68\% and $13.47 \%$, respectively. Figure 6 specifies that a causal relationship exists between Race $\left(X_{0}\right)$ and SEER-Summary-Stage $\left(X_{16}\right)$. This survival disparity is attributed to the latter stage of detection among African-American women, who have the highest morality rate among any racial or ethnic group. The presence of additional illnesses, lack of health insurance and disparities in receipt of treatment probably contribute to the differences in breast cancer survival.

Tumor Size/Race: The incidence rates of breast cancer by tumour size greatly differ. American women are less likely to be diagnosed with middle-sized tumours and more likely to be diagnosed with larger ( $>5.0 \mathrm{~cm}$ ) or smaller tumours ( $<1.5 \mathrm{~cm}$ ). Mortality rate increases with increasing tumour. The mortality rate corresponding to smaller tumours is $6.02 \%$, and the mortality rate corresponding to middle-sized tumours and larger tumours are $9.86 \%$ and $13.21 \%$, respectively. Figure 6 demonstrates that a causal relationship exists betweenTumour Size $\left(X_{6}\right)$,Race $\left(X_{0}\right)$ and SEER-Summary-Stage $\left(X_{16}\right)$. For smaller tumours, the incidence rate is $17.72 \%$ among Caucasian women, but $11.84 \%$ among African-American women. The incidence rate for larger tumours ( $>5.0 \mathrm{~cm}$ ) is $8.74 \%$ among Caucasian women, but $10.95 \%$ among African-American women. This incidence disparity can also be attributed to both later cancer stages at detection and poorer stage-specific survival among African-American women. Poverty, low education and unequal access to medical care are associated with low breast cancer incidence.

# Conclusion 

BNs can graphically describe conditional dependency among attributes and have been previously identified as computationally efficient approaches for further reducing prediction error. The proposed algorithm, namely, FKBN, offers a trade-off between probability estimation and network structure complexity. With enough instances to detect reliable dependencies among predictive attributes, the findings of this study are helpful in diagnostic practice and drug design. Possible extensions of this investigation should involve applying the novel computational framework in categorising other diseases and detecting properties that can be targeted for cancer therapy. Moreover, computational advancement will require improving the prediction accuracy of the proposed methodology by updating it to existing algorithms.

## Competing interests

The authors declare that they have no competing interests.

## Acknowledgements

This work was supported by the National Science Foundation of China (Grant no. 61272209), Postdoctoral Science Foundation of China (Grant no. 20100481053, 2013MS30980).

## Submit your next manuscript to BioMed Central and take full advantage of:

- Convenient online submission
- Thorough peer review
- No space constraints or color figure charges
- Immediate publication on acceptance
- Inclusion in PubMed, CAS, Scopus and Google Scholar
- Research which is freely available for redistribution

Submit your manuscript at www.biomedcentral.com/submit
(1) BioMed Central