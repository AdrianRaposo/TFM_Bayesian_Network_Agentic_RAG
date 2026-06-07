Document downloaded from:
http://hdl.handle.net/10251/120548
This paper must be cited as:
Mujalli, R.; López-Maldonado, G.; Garach, L. (2016). Bayes classifiers for imbalanced traffic accidents datasets. Accident Analysis \& Prevention. 88:37-51.
https://doi.org/10.1016/j.aap.2015.12.003
![img-0.jpeg](img-0.jpeg)

The final publication is available at
http://doi.org/10.1016/j.aap.2015.12.003

Copyright Elsevier

Additional Information

# Bayes Classifiers for Imbalanced Traffic Accidents Datasets 

Randa Oqab Mujalli ${ }^{\mathrm{a}, \mathrm{a}}$, Griselda López ${ }^{\mathrm{b}}$, Laura Garach ${ }^{\mathrm{b}}$<br>${ }^{a}$ Department of Civil Engineering, The Hashemite University, 13115 Zarqa, Jordan<br>${ }^{\mathrm{b}}$ Department of Civil Engineering, University of Granada, ETSI Caminos, Canales y Puertos, c/ Severo Ochoa, s/n, 18071 Granada, Spain<br>${ }^{a}$ Corresponding author, The Hashemite University, 13115 Zarqa, Jordan, Phone: +96253903333-4777<br>e-mail: randao@hu.edu.jo


#### Abstract

Traffic accidents data sets are usually imbalanced, where the number of instances classified under the killed or severe injuries class (minority) is much lower than those classified under the slight injuries class (majority). This, however, supposes a challenging problem for classification algorithms, since they are often biased towards the majority class and therefore this may cause obtaining a model that well cover the slight injuries instances whereas the killed or severe injuries instances are misclassified frequently. Researchers proposed many solutions to deal with class imbalance misclassification, such as the external approaches that preprocess the data in order to diminish the effect of their class imbalance where it has been found to overcome the class imbalance problem.


Based on traffic accidents data collected on urban and suburban roads in Jordan for three years (2009-2011); three different data balancing techniques were used: under-sampling which removes some instances of majority class, oversampling which creates new instances of the minority class and a mix technique that combines both. In addition, different Bayes classifiers were compared for the different imbalanced and balanced data sets: Averaged One-Dependence Estimators, Weightily Average One-Dependence Estimators, and Bayesian networks in order to identify factors that affect the severity of an accident. The results indicated that using the balanced data sets, especially those created using oversampling techniques, with Bayesian networks improved classifying a traffic accident according to its severity and reduced the misclassification of killed and severe injuries instances. On the other hand, the following variables were found to contribute to the occurrence of a killed causality or a severe injury in a traffic accident: number of vehicles involved, accident pattern, number of directions, accident type, lighting, surface condition, and speed limit. This work, to the knowledge of the authors, is the first that aims at analyzing historical data records for traffic accidents occurring in Jordan and the first to apply balancing techniques to analyze injury severity of traffic accidents.

Keywords: Bayesian networks; Traffic accidents; urban area; imbalanced data set; SMOTE

## 1. INTRODUCTION

Reducing accidents severity is an effective way to improve road safety (Qiu et al., 2014). Recent road traffic safety studies have focused on analysis of risk factors that affect fatality and injury level (severity) of traffic accidents. However, many risk factors are waiting to be discovered or analyzed (Kwon et al., 2015).

Traffic accidents are considered one of the most important and dangerous problems that encounter societies all around the world where it consumes many human and monetary resources. World Health Organization (WHO) statistics indicated that traffic accidents fatalities are estimated to be 1.2 million persons annually worldwide, as well as resulting in twenty to fifty million injuries. Cost of traffic accidents is estimated to be 518 billion US dollars representing (1-3\%) of Gross Domestic Product (GDP) worldwide (WHO, 2013).

Jordan is considered a developing country which has both rapid population and vehicles growth; population statistics of 2013 issued by Department of Statistics (DOS) indicated that Jordan has 6.53 million inhabitants with $1,263,754$ registered vehicles ( 1 vehicle/ 5 persons) (DOS, 2013).

According to Police Traffic Department (PTD) reports for 2013; 107,864 traffic accidents occurred in Jordan with 768 fatalities, 2,258 severe injuries and 13,696 slight injuries, where $94.74 \%$ of accidents were collisions ${ }^{1}$, resulting in $43 \%$ of fatalities and $50 \%$ of severe injuries (PTD, 2013). Also, $69 \%$ of traffic accidents and $71 \%$ of collisions occurred in the capital city of Amman, which is considered an urban area having nearly $39 \%$ of Jordan's population ( $2,528,500$ inhabitants). In addition, the cost of traffic accidents in Jordan, using unit cost approach to estimate traffic accidents cost in a socioeconomic perspective, is estimated to be 365 million US dollar (PTD, 2013), noting that Jordan's GDP for 2013 is estimated to be 33.641 billion US dollar, in which traffic accidents cost represents $1.2 \%$ of Jordan's GDP (DOS, 2013).

Urban and rural accidents characteristics are different (Khorashadi et al., 2005; Theofilatos et al., 2012). Khorashadi et al. (2005) identified significant differences between urban and rural accidents due to differing driver, vehicle, environmental, road geometry and traffic characteristics. Moreover, they estimated that the severe/fatal injury is nearly eight times more likely to occur in an urban area and about 2.5 times more likely in a rural area than other types of injures (i.e. no injury, complaint of pain, or visible injury). Theofilatos et al. (2012) investigated road accident severity with particular focus on the comparison between inside and outside urban areas. They found that factors affecting road accident severity inside urban areas included young driver age, bicyclists, intersections, and collision with fixed objects, whereas factors affecting severity outside urban areas were weather conditions, head-on and side collisions. This demonstrated the particular road users and traffic situations that should be focused on for road safety interventions for the two different types of networks (inside and outside urban areas).

Many modeling techniques have been in use to analyze the injury severity of traffic accidents. The most used models were the logit and probit (Al-Ghamdi, 2002; Milton et al., 2008; Savolainen et al., 2011; Mujalli and De Oña, 2012). However, most of them have their own model assumptions and pre-defined underlying relationships between dependent and independent variables (Chang and Wang, 2006). Recently, many researchers have used methods based on data mining techniques. For example, association rules (Pande and Abdel-Aty, 2009; Montella et al., 2012) or Decision Trees (López et al., 2012a; Abellán el at., 2013; De Oña et al., 2013) have been used for identifying accident patterns. Bayesian networks (BNs) have also been used to study traffic accidents' severity. De Oña et al. (2011) employed BNs to model the relationship between injury severity and variables related to driver, vehicle, roadway, and environment characteristics. They concluded that BNs could be used for classifying traffic accidents according to their injury severity. In addition, Mujalli and De Oña (2011) presented a simplified method based on BNs and variable selection algorithms to predict the injury severity in a traffic accident. Recently, Kwon et al. (2015) used two classification methods, the Naive Bayes and the Decision Tree classifier, for ranking of risk factors.

Traffic accidents datasets usually have fewer records for fatal and severe injury accidents than for slight injury accidents (Montella et al., 2012). A dataset is considered to be imbalanced if one of the classes (called a minority class) contains a much smaller number of examples than the remaining class (majority class) (Stefanowski and Wilk, 2008). According to Li and Sun (2012) if the proportion of minority class samples constitutes less than $35 \%$ of the dataset, the dataset is considered to be imbalanced. Data mining algorithms when learning from imbalanced data tend to produce high predictive accuracy over the majority class, but poor predictive accuracy over the minority class (Thammasiri et al., 2014). Many solutions have been proposed to this problem which can be categorized into two major groups (López et al., 2012b): the internal approaches that create new algorithms or modify existing ones, and the external approaches that preprocess the data in order to diminish the effect of the class imbalance. The pre-processing approach (or resampling techniques) seems to be the more straight forward approach that has greater promise to overcome the class imbalance problem (Thammasiri et al., 2014).

Resampling techniques can be categorized into three groups: the first group consists of the under-sampling methods, which aim to balance the class populations through removing data samples from the majority class

[^0]
[^0]:    ${ }^{1}$ Collisions exclude all of: run-off-road accidents, pedestrian related accidents and property damage only accidents

until the classes are approximately equally represented. Under-sampling methods randomly eliminate instances from the majority class until a required degree of balance between classes is reached. The second group includes the oversampling methods, which aim to balance class populations through creating new samples from the minority class and adding them to the training set. Finally, the third group comprises the Mix methods, which combine both sampling approaches, integrating oversampling of selected minority class instances with removing the most harmful (i.e. noise, and borderline instances that are close to the boundary between the positive and negative classes regions) (Stefanowski and Wilk, 2008, Błaszczyński and Stefanowski, 2015).

In this work, factors affecting injury severity of urban and suburban traffic accidents in Jordan are analyzed. For this purpose, Bayes classifiers are used in the original dataset and in the three balanced datasets (balanced with random under-sampling, with oversampling and with mix methods). Finally, the models developed are compared, and the results for the best model are described.

The paper is organized as follows: Section 2 presents the methodology, the data used, a brief description of Bayes classifiers used, and a description of the performance measures used to evaluate the models. In Section 3, the results and their discussion are presented. Finally, conclusions are given in Section 4.

# 2. METHODOLOGY 

In this paper, an imbalanced data set was first obtained and used to develop models applying different popular Bayes classifiers: Efficient Lazy Elimination for Averaged One-Dependence Estimators (AODEsr) (Zheng and Webb 2006), Weightily Averaged One-Dependence Estimators (WAODE) (Jiang and Zhang, 2006) and Bayesian networks (BNs), where different scores and search algorithms were employed for BNs. Moreover, three balanced datasets were created from the imbalanced data set using three balancing techniques: random under-sampling, oversampling and mix sampling. The same Bayes classifiers used to develop models form the imbalanced data set were also used to develop models from the three balanced data sets. Furthermore, Bayes classifiers were used to analyze injury severity of collisions on urban and suburban roads. The developed models were compared to each other using 10- folds cross validation method, where each data set was first divided into 10 subsets, nine were used to train the model and the remaining one subset was used to test the model. The process was repeated ten times and the average was obtained. As a result, 11 models were developed and compared. Figure 1 shows the procedure employed.
[Insert here Figure 1]

### 2.1. Data

Records for traffic accidents, which occurred on urban and suburban roads in Jordan were obtained from the Jordanian Police Traffic Department (PTD) for a period of 3 years (2009-2011). The total number of accidents obtained for this period was 49,693 . Considering that the main objective of this study was to identify the key factors that contribute to the occurrence of a specific severity in collisions; accidents with property damage only (PDO), Pedestrian and Run-Off-Road were excluded. In this study, only accidents with collisions were analyzed, and as a result, the total number of records used was 16,815 .

To identify the main factors that affect urban and suburban collisions severity, fourteen independent variables were analyzed (see Table 1). The variables chosen were based on variables available in the original dataset and the variables used in literature (Theofilatos et al., 2012; Pahukula et al., 2015). The data included variables describing the prevailing conditions at the time of the occurrence of the accident:

- Roadway information: characteristics of the roadway on which the accident occurred such as number of directions, number of lanes, horizontal alignment, grade, pavement type, and pavement surface condition.
- Context information: weather and lighting conditions when the accident occurred.
- Accident information: contributing circumstances such as type of accident and accident pattern.

- Vehicle data: number of vehicles involved.
[Insert here Table 1]
The class variable was the resulting severity of the accident. Following previous studies (Chang and Wang, 2006; De Oña et al., 2013; Abellán et al., 2013) the injury severity was determined according to the level of injury to the worst injured occupant. Herein, the severity was categorized in to two levels of severity: accidents with slight injuries (SLIG) and accidents with killed or severe injuries (KSEV).

The original distribution of records (also called instances) was 13,725 slight injuries and 3,090 killed or severe injuries. The target variable (severity) was predominantly imbalanced, with the majority of instances belonging to SLIG ( $77 \%$ ), and only a small percentage of KSEV (23\%).

# Data preprocessing 

The variables obtained from the PTD were preprocessed prior to analysis, where they were first discretized into distinct values following previous studies (Simoncic, 2004; Helai et al., 2008; De Oña et al., 2011).

The unsupervised variable filter for replacing missing values was used to deal with missing data. The filter replaces a missing data with the mean if the variable was numeric or mode if the variable was nominal of all known values of that attribute in the class where the instance with missing data belongs.

Overall, out of fourteen independent variables, the following variables: PAT, TRAME, GRADE, SPE and DIR were used as they appeared in the original dataset. The rest of the variables values were discretized in order to enable working with them. For instance, in the original dataset, the variable ACT had twelve categories, six of them have been grouped in only one category; collision with fixed object (this category included collision with guardrail, barrier, concrete barrier, pole, parked vehicle and traffic control device). Other variables such as PAV had five categories (asphalt, concrete, dirt, gravel and metal), and was grouped into three categories. Table 1 gives a description of the variables used for the analysis and their distribution between classes of severity.

## Re-sampling techniques

A dataset is said to be imbalanced, if the number of instances in each category of the target variable is not approximately equal (Crone and Finlay, 2012). The classification problems based on imbalanced data occur often in applications when the events of interest are rare, such as the resulting outcomes of severe injuries or being killed in a traffic accident.

The class imbalance problem exists in many fields, and it was found that it caused deterioration in the performance of machine learning methods, especially classifiers performance, since they assume a balanced dataset to exist (Japkowicz, 2000). Examples of such problems were encountered in many fields such as; inflight helicopter gearbox fault monitoring (Japkowicz et al., 1995), the detection of fraudulent telephone calls (Fawcett and Provost, 1997), the detection of oil spills in satellite radar images (Kubat et al., 1998), credit scoring (Brown and Mues, 2012) or student retention (Thammasiri et al., 2014).

In many real-world applications, the class distribution of instances is most often imbalanced and the costs of misclassification are different. Thus, class-imbalance and cost-sensitive learning have attracted much attention from researchers. Sampling is one of the widely used approaches in dealing with the class imbalance problem, which alters the class distribution of instances so that the minority class is well represented in the training data (Thammasiri et al., 2014).

Re-sampling techniques apply a preprocessing step in order to balance the original imbalanced data. In this paper, three balancing techniques were used. Weka's preprocess supervised filter (Witten and Frank, 2005) was used to perform the re-sampling on the dataset. The re-sampling techniques used were (López et al., 2012b):under-sampling, oversampling and mix. A brief description of each of them is given below:

- Random under-sampling: a non-heuristic method that aims to balance class distribution through the random elimination of majority class instances. The elimination of majority class instances is performed in order to try to balance out the data set in an attempt to overcome the idiosyncrasies of the machine learning algorithm. The major drawback of random undersampling is that this method can discard potentially useful data that could be important for the induction process. In addition, once undersampling the majority class is performed, the sample can no longer be considered random. This is due to the fact that when using classifiers on some data set, there is no predefined known probability distribution of target population, and since that distribution is unknown, sample distribution is used in attempt to try to estimate the population distribution, and as long as the sample is drawn randomly, the sample distribution can be used to estimate the population distribution from where it was drawn (Kotsiantis et al., 2006)
- Synthetic minority oversampling technique (SMOTE): This is a heuristic method which creates a subset of the original dataset by creating synthetic minority examples; the minority class is oversampled by taking each minority class sample and introducing synthetic examples along the line segments joining any/all of the (k) minority class nearest neighbors. Depending upon the amount of oversampling required, neighbors from the (k) nearest neighbors are randomly chosen and one sample is generated in the direction of each. Synthetic instances are generated in a less applicationspecific manner, by operating in "variable space" rather than "data space". More specifically, synthetic samples are generated by taking the difference between the variable vector (sample) under consideration and its nearest neighbor and multiplying this difference by a random number between zero and one, and then adding it to the variable vector under consideration. This causes the selection of a random point along the line segment between two specific variables and hence effectively forces the decision region of the minority class to become more general (Chawla, et al., 2002).
- Mix method: This method combines both sampling techniques used in under-sampling and oversampling. In this method, the minority class instances are randomly duplicated while randomly discarding the majority class instances in order to modify the class distribution until the number of instances belonging to each class is roughly the same, preserving the original data set size. (Witten and Frank, 2005).


# 2.2. Bayes classifiers 

Statistical inference such as classifications in data processing could be performed successfully using the Bayes principle. A Bayes classifier is based on the idea that the role of a class is to predict the values of variables for members of that class, where instances are grouped in classes because they have common values for the variables (Poole and Mackworth, 2010).

### 2.2.1. Naïve Bayes Classifiers

Naive Bayes (NB) classifier is considered the simplest of Bayes classifiers, which makes the independence assumption that the input variables are conditionally independent of each other given the classification. The NB classifier results could be illustrated using a particular belief network, in which each variable is represented as a node (called child) and the class variable is the only parent for all the other variables.

Let $X_{i},(i=1,2, \ldots, n$ for n variables $)$ and each variable has values of $x_{1}, x_{2}, \ldots, x_{n}$ that describe each instance. The most probable target value is described as $v_{M A P}$, while $V$ is a finite set building on every target value $v_{j}$. In order to assign the most probable target value of the test instance using Bayes approach for classification, one set of training instances with a specific class is given, a classifier must be learned to predict the class distribution of an instance with its class unknown. The Bayes classifier is defined as (Wu and Cai, 2011):

$v_{M A P}=\arg \max _{v_{j} \in V} P\left(v_{j}\right) \prod_{i=1}^{n} P\left(x_{1}, x_{2}, \ldots, x_{n} \mid v_{j}\right)$
NB classifier is best suited when the independence assumption is valid, that is, when the class is a good predictor of the other variables and the other variables are independent given the class, then the NB can be used:

$$
v_{N B}=\arg \max _{v_{j} \in V} P\left(v_{j}\right) \prod_{i=1}^{n} P\left(x_{i} \mid v_{j}\right)
$$

Each variable node in NB has the class node as its parent, but does not have any parent from variable nodes. In many fields including traffic accidents analysis, assuming independence between contributing variables is unrealistic. When two variables are related, NB may place too much weight on the influence from the two variables, and too little on the other variables, which can result in classification bias, however, deleting one of these variables may have the effect of alleviating the problem (Zheng and Webb, 2006).

In order to improve NB's accuracy by weakening its variable independence assumption, Semi-NB classifiers can be used to enhance NB by relieving the restriction of conditional independence amongst variables. One of the techniques used to relieve this restriction is the Aggregate One-Dependence Estimators (AODE), which achieves a higher accuracy by averaging over a constrained group of 1-dependence NB models developed on a small space (Webb et al., 2005).

In AODE, a one-dependence classifier is developed for each variable, where the variable is set to be the parent of all other variables. Then, AODE directly averages the aggregate consisting of many special tree augmented naive Bayes. AODE maintains the simplicity and direct theoretical foundation of NB without incurring the high time, in addition to having good classification performance (Wu et al., 2011).

The AODE classifier is defined as follows (Webb et al., 2011):
$v_{\text {AODE }}=\arg \max _{v_{i} \in V}\left(\sum_{i: 1 \leq i \leq i \leq n \wedge F\left(v_{i}\right) \geq m} P\left(x_{i}, v_{i}\right) \prod_{j=1, j \neq i}^{n} P\left(x_{j} \mid x_{i}, v_{j}\right)\right)$

Where $F(v i)$ is a count of the number of training instances having variable-value $x_{i}$ and is used to enforce the limit $m$ that they place on the support needed in order to accept a conditional probability estimate. $n$ is the number of variables.

An improved AODE called AODE with Subsumption Resolution (AODEsr) utilizes the tables of probability estimates formed at training time to efficiently detect and address a special form of dependency between two variable-values at classification time. AODEsr relaxes the variable independence assumption in which each variable depends upon the class and at most one other variable.

The specialization-generalization relationship is one extreme type of interdependence. For two variable values $v_{i}$ and $v_{j}$ if $\mathrm{P}\left(x_{j} \mid x_{i}\right)=1.0$ then $x_{j}$ is a generalization of $x_{i}$ and $x_{i}$ a specialization of $x_{j}$. AODEsr deletes generalization variable-values if a specialization is detected, and aggregates the predictions of all qualified classifiers using the remaining variable-values (Zheng and Webb, 2006).

Another semi-NB classifier is the Weightily Averaged One-Dependence Estimators (WAODE), which weighs the averaged 1-dependence classifiers by the conditional mutual information, which significantly outperforms the AODE (Jiang and Zhang, 2006).

WAODE is an extended NB classifier that relaxes the conditional independence assumption of NB, and consists of multiple one-dependence estimators. One-dependence estimator (ODE) is a classifier with a

single variable that is the parent of all other variables. In WAODE, ODEs are constructed for each variable, and a different weight is assigned for each ODE. WAODE averages the aggregate of the weighted ODEs (Jiang and Zhang, 2006).

If an instance $E$ is represented by $E=\left(x_{1}, \ldots, x_{n}\right)$ where $x_{i}$ is the value of variable $X i$. The WAODE classifier is defined as:
$v(E)=\operatorname{argmax}_{v \in V}\left(\frac{\sum_{i=1}^{n} W_{i} P\left(x_{i}, v\right) \prod_{j=1, j \neq i}^{n} P\left(x_{j} \mid x_{i}, v\right)}{\sum_{i=1}^{n} W_{i}}\right)$

Where $W i$ is the weight of the ODE in which variable $X i$ is the parent of all other variables.
In WAODE, in order to determine the weight $W i$, mutual information between variable $X i$ and class $V$ is used:
$W_{i}=\sum_{x_{i}, v} P\left(x_{i}, v\right) \log \frac{P\left(x_{i}, v\right)}{P\left(x_{i}\right) P(v)}$
Where the probabilities $\mathrm{P}(x i, v)$ and $\mathrm{P}(x i / x i, v)$ are estimated as follows:
$P\left(x_{i}, v\right)=\frac{F\left(x_{i}, v\right)+1.0 /\left(n_{i} \cdot k\right)}{N+1.0}$
$P\left(x_{j} \mid x_{j}, v\right)=\frac{F\left(x_{j}, x_{i}, v\right)+1.0 / n_{j}}{F\left(x_{i}, v\right)+1.0}$
Where $F($.$) is the frequency with which a combination of terms appears in the training data, N$ is the number of training instances, $n_{i}$ is the number of values of variable $X i$, and $k$ is the number of classes.

# 2.2.2. Bayesian networks classifiers 

BNs applications have grown extensively into different fields, with theoretical and computational developments in many areas (Mittal et al., 2007). These include: modeling knowledge in bioinformatics, medicine, document classification, information retrieval, image processing, data fusion, decision support systems, engineering, gaming, and law.

Let $X=\left\{X_{1}, \ldots, X_{n}\right\}, n \geq 1$ be a set of variables. BN over a set of variables $X$ is a network structure, which is a Directed Acyclic Graph over $X$ and a set of probability tables $B_{p}=\left\{p\left(X_{i} \mid p a\left(X_{i}\right), X_{i} \in X\right)\right\}$ where $p a\left(X_{i}\right)$ is the set of parents or antecedents of $X_{i}$ in BN and $i=(1,2,3, \ldots, n)$. A BN represents joint probability distributions $P(X)=\prod_{X_{i} \in X} p\left(x_{i} \mid p a\left(x_{i}\right)\right)$.

Relationships between variables based on the theory of BN (Neapolitan, 2009) are represented by arcs in the graph, and could represent causality, relevance or relations of direct dependence between variables. However, for the purpose of this research, we do not assume a causal interpretation of the arcs in the networks such as in Acid et al. (2004). Consequently, the arcs are interpreted as direct dependence relationships between the linked variables, and the absence of arcs means the absence of direct dependence between variables; however, indirect dependence relationships between variables could exist.

The classification task consists in classifying a variable $V=v_{i}$, called the class variable, given a set of variables $X=X_{1} \ldots X_{n}$, called attribute variables. A classifier $h: X \rightarrow V$ is a function that maps an instance

of $X$ to a value of $V$. The classifier is learned from a data set $D$ consisting of samples over $(X, V)$. The learning task consists of finding an appropriate BN given a data set $D$ over $X$.

In order to learn the structure in BNs, two approaches are available: 1 . The constraint based, which performs tests of conditional independence on the data and searches for a network that is consistent with the observed dependences and independences. 2. The score based, which defines a score that evaluates how well the dependences or independences in a structure match the data and search for a structure that maximizes the score.

In this study, we used the following Bayes Classifiers AODE, WAODE and BNs in order to build different models and to compare their results in terms of their ability to correctly classify traffic accidents according to their injury severity into either KSEV or SLIG.

When building the models using BNs, three search methods were used: hill climber, hill climber algorithm restricted by an order on the variables (K2) and simulated annealing search algorithm. Also, three different score metrics functions were used: BDe score metric (BDeu); Minimum Description Length (MDL) and the Akaike Information Criterion (AIC).

The search algorithms and the scores were applied in this study mainly because, besides being widely used and being relatively quick, they produce good results in terms of network complexity and accuracy (Madden, 2009). Data sets used, models developed, and their descriptions are presented in Table 2.
[Insert here Table 2]

# 2.3. Performance evaluation measures 

In order to evaluate the performance of the different developed models, a number of common performance measures were used. These performance measures were calculated using the confusion matrix (see Table 3). In the binary class problem, this matrix shows the results of correctly and incorrectly predicted instances for each class. Where the True Positives (TP) denotes the number of positive (in our case SLIG) instances correctly classified, True Negatives (TN) denotes the number of negative (in our case KSEV) instances correctly classified, False Positives (FP) denotes the number of positive instances incorrectly classified, and False Negatives (FN) denotes the number of negative instances incorrectly classified.
[Insert here Table 3]
The performance measures used in this study were accuracy, sensitivity, specificity and F-measure. Their equations are:
$A c c u r a c y=\frac{T P+T N}{T P+F P+T N+F N}$

Sensitivity $=\frac{T P}{T P+F N}$
Specificity $=\frac{T N}{T N+F P}$
Precision $=\frac{T P}{T P+F P}$
$F-$ measure $=\frac{2 * \text { Precesion } * \text { Sensitivity }}{\text { Precesion }+ \text { Sensitivity }}$

Accuracy is the proportion of instances that were correctly classified among all instances. Accuracy only gives information on the classifier's overall performance. In cases where there is a highly skewed data distribution, the overall accuracy is not sufficient. In this case, accuracy might give a false indication that a classifier performance is high, where in fact the classifier is only predicting all samples as belonging to one class value, in which case it is biased in its results to majority class. Sensitivity and specificity are usually adopted to monitor classification performance on two classes separately. Sensitivity represents the proportion of correctly predicted as SLIG among all the observed as SLIG. Specificity represents the proportion of correctly predicted as KSEV among all the observed KSEV. F-measure represents the harmonic mean of precision and sensitivity. F-measure is frequently used in imbalanced dataset (Wang et al., 2015).

However, a trade-off exists between sensitivity and specificity. Therefore, the area under a Receiver Operating Characteristic (ROC) curve is also used as a target performance measure. ROC curve represents the true positive rate (sensitivity) vs. the false positive rate (1-specificity). ROC curves are more useful as descriptors of overall performance, reflected by the area under the curve, with a maximum of one describing a perfect test and a ROC area of 0.50 describing a valueless test.

For the analysis of traffic accident injury severity and in order to determine the optimal dataset-classifier, the measures described above were first calculated: accuracy, sensitivity, specificity, F-measure and ROC area. Later, the best Bayes classifier model found in terms of these measures was used for analysis.

# 2.4. Bayes network inference 

Inference in BNs consists of computing the conditional probability of some variables, given that other variables are set to evidence. Inference may be done for a specific state or value of a variable, given evidence on the state of other variable(s). Thus, using the conditional probability table for the BN developed; their values can be easily inferred. See De Oña et al. (2011) for a detailed explanation and examples. When using BNs, inference is necessary to interpret the results from road safety perspective.

## 3. RESULTS

In this section, an analysis was performed to determine the performance of the different alternatives used for the imbalanced data set classification. The aim was to analyze three different issues:

- The improvement obtained by resampling data sets using three different resample techniques: undersampling, oversampling and mix versus the original imbalanced data set.
- The possible resulting differences between balanced and imbalanced data sets as measured by applying the different Bayes classifiers and their resulting performance evaluation measures.
- The risk factors that are significantly associated with the occurrence of a killed or a severe injury in a traffic accident were extracted using the classifier that presented the best performance in terms of evaluation measures.

First, the experimental framework with the data set employed in the analysis is presented and then, the performance of the different classifiers that will allow supporting the extracted findings is shown. Finally, the main issues that arise from the aforementioned analysis are discussed.

### 3.1. Imbalanced versus balanced data sets

The original dataset contained 16,815 accidents in which the injury severity distribution was: 13,725 slight injuries and 3,090 killed or severe injuries, and in which the target variable (severity) was predominantly imbalanced.

To deal with the imbalanced data set problem, three new balanced data sets were developed using three different resample techniques: under-sampling, oversampling and mix. Table 4 shows the total number of records (instances) in all the datasets used and their distribution amongst different severity classes.
[Insert here Table 4]
As shown in Table 4, when the random under-sampling technique was used, the dataset was reduced to the size of the minority class, in this case to killed or severe class ( 3,090 instances for slight class as shown in Table 1). While when using SMOTE oversampling, the number of the instances in the resulting dataset was increased to the size of the majority class ( 13,725 instances for killed or severe class). Finally, in the mix sample, the resulting dataset preserved the original number of instances ( 16,815 accidents), however, the majority class instances were reduced to 8,414 instances and the minority class was increased to 8,401 instances.

# 3.2. Bayes classifiers and data sets 

The different Bayes classifiers described in section 2 were used to build different models. For each dataset (original, oversample, under-sample and mix), eleven models were developed. Each model was first divided into ten subsamples, nine were used to train the model and the last was used to test the model, and the process was repeated ten times (runs) for each subsample (ten-fold cross-validation). The description of all the models developed is shown in Table 2.

The results of the models developed for each balanced dataset were then compared with those obtained using the original dataset models. In order to perform this comparison, the results of the evaluation measures used to compare the models developed are summarized in Table 5. The comparison is based on the performance measures of accuracy, sensitivity, specificity, ROC Area and F-measure (the results shown are the averages of the ten runs).
[Insert here Table 5]
Table 5 shows the average results of the performance measures used for the different models developed, where a corrected paired t-test was used to test their statistical significance. To that end, forty-four models were developed using a combination of datasets with different classifiers. With respect to the results obtained by the testing set, the following findings were extracted:

- None of the balanced datasets showed a statistical significant improvement when compared to the original dataset based on accuracy, sensitivity, and F-measure. This result however was expected, since these measures are highly biased to the majority class (SLIG) as seen in their equations presented in section 2.3 .
- The results obtained by specificity showed that the original dataset had the worst results in which the models used were completely incapable of classifying KSEV correctly, and where the highest result obtained using this measure on the original dataset was when using k2.AIC with a result of 0.030 which shows a drastic incapability of classification. On the other hand, most of the balanced datasets showed a statistically significant improvement when compared to the original dataset, where the highest result obtained was when using the following dataset/model respectively: Oversample/k2.AIC with a result of 0.650 .
- ROC Area indicated that the following model/dataset showed the highest significant statistical improvement when compared to the original dataset: Oversample/ Hillclimber.AIC with a result of 0.680, Oversample/k2.AIC with a result of 0.680, Oversample/ Simulated.AIC with a result of 0.680 .

- The total number of wins shown in the last row in Table 5 represents the total number of the times the dataset used had a statistical significant improvement when compared to the original dataset. As seen, the oversample dataset had twenty-two wins indicating the best performance when compared to under-sample dataset having a total of eleven wins and the mix dataset having a total of sixteen wins

Based on the aforementioned results, balanced datasets performed better than the original in terms of its ability to classify the minority class (KSEV), with the best models obtained using the oversample dataset.

In addition, performance of the models developed using BNs was superior to those developed using other classifiers; consequently, BNs performance was compared with WAODE and AODEsr. Table 6 shows the comparison of two models developed with Bayes classifiers (AODErs and WAODE) versus the rest of the BNs in both oversample and original data sets.
[Insert here Table 6]
Based on Table 6, the following results were extracted:

- The best performing classifiers that obtained a statistically significant improvement in terms of accuracy in the original data set were Bayes.Hill.Bdeu and Bayes.Hill.MDL where they both scored 0.816 when compared to AODEsr and WAODE, and where in the oversample data set Bayes.Simulated.AIC and WAODE had values of 0.628 and 0.627 respectively when compared to AODEsr. This result is due to the fact that in imbalanced data sets, accuracy is not a proper measure since it does not distinguish between the numbers of correctly classified instances of different classes and may lead to erroneous conclusions. Lopez et al. (2013) stated that a classifier achieving an accuracy of $90 \%$ in a dataset with an imbalanced data set is not accurate if it classifies most examples as belonging to the class with more instances.
- In terms of sensitivity, again the best performing classifiers in the original data set were Bayes.Hill.Bdeu and Bayes.Hill.MDL where they both had a value of one when compared to AODEsr and WAODE, while in the oversample data set; AODEsr had a value of 0.663 when compared to WAODE. Since sensitivity measures the capability of the classifier to classify SLIG, and the original data set is biased to SLIG, therefore, the performance obtained reflected this fact.
- Specificity results for the original data set indicated that the best performance was obtained using Bayes.k2.AIC, with a value 0.029 when compared to AODEsr and WAODE. On the other hand, in the oversample data set, the best classifier was the Bayes.k2. AIC, with a value of 0.655 when compared to both AODEsr and WAODE. Here it is evident that none of the used classifiers in the original data set was capable of classifying KSEV correctly, while in the balanced data set, all classifiers showed a remarkable improved capability of classifying KSEV.
- Regarding F-measure, the results indicated that both Bayes.Hill.Bdeu and Bayes.Hill.MDL had a statistically significant improvement when compared to both AODEsr and WAODE in the original data set with a value of 0.899 . On the contrary, none of the classifiers in the oversample data set showed any statistically significant improvement. According to Wang et al. (2015), F-measure is frequently used in imbalanced datasets, however, Daskalaki et al. (2006) indicated that higher Fmeasure means that the model performs better on positive class (i.e. SLIG).
- A well-known approach to unify these measures is the ROC area, which provides a single measure of a classifier's performance for evaluating which model is better on average (López et al., 2013). Herein, more than one BN model obtained high ROC area value with statistically significant improvement where the highest values were obtained for Bayes.Hill. AIC, Bayes.k2.AIC, and Bayes.Simulated.AIC with values of $0.676,0.677$, and 0.680 respectively in the oversample data set. On the contrary, none of the classifiers in the original data set had any statistically significant improvement.

Based on the results obtained in Table 6 and the discussion above, none of the classifiers in the original data set was capable of correctly classifying KSEV. However, all the oversample's BNs presented an improved performance, indicating their ability to classify KSEV better.

In order to better illustrate the results obtained, table 7 shows the total number of times each classifier had statistically significant improvement when compared to either AODEsr or WAODE (total no. of wins) in both the original and the oversample data sets.
[Insert here Table 7]
As shown in Table 7, the classifiers in the original data set that had the highest number of wins were Bayes.Hill.BDeu and Bayes.Hill.MDL, however their wins were in the evaluators whose results are sensitive to imbalanced data sets (accuracy, sensitivity, and F-measure). On the other hand, the classifiers in the oversample data set that had the highest number of wins were Bayes.K2.AIC and Bayes.Simulated.AIC, where they both had an improvement in specificity and ROC area, which means that their capability of correctly classifying KSEV (as measured using specificity) and their overall performance (as measured using ROC area) was considerably higher than the models developed using the original data set.

Thus, using the oversample data set in combination with Bayes.K2.AIC or Bayes.Simulated.AIC obtained improved results in comparison with the original data set.

# 3.3. Injury severity analysis 

Based on the aforementioned results, BNs were used in order to identify the main factors that contribute to classifying an accident according to a specific injury severity. As shown in Table 8 and based on BNs developed using Bayes.Simulated.AIC and Bayes.K2.AIC in both original and oversample datasets, the complexity (number of arcs) of the developed BNs was calculated. In addition, the direct dependence relationships between severity (SEV) and the rest of the variables as well as interdependences amongst the different variables were illustrated. Furthermore, relationships were grouped so that they take into account whether or not the relation was directly related with severity.
[Insert here Table 8]
As illustrated in Table 8, only three variables had direct dependence with SEV in the original data set in Bayes.k2.AIC, whereas only two variables in Bayes.k2.AIC had direct dependence with SEV, where the only common variable between the two models was speed (SPE). In the oversample data set, eleven variables had a direct dependence relationship with SEV in the Bayes.Simultaned.AIC models, whereas in the model Bayes.K2.AIC all the thirteen variables presented this direct relation with SEV.

Thus, variables that were found to be directly related to SEV in both models were: vehicles involved (VEH), accident type (ACT), accident pattern (PAT), direction (DIR), number of lanes (LANE), grade (GRADE), pavement type (PAV), surface condition (SUP), speed (SPE), traffic control (CONT) and lighting conditions (LIG). The fact that these variables appeared in the two models indicates that these variables have a strong dependence with SEV.

Many researchers also found that these variables were of the influencing factors that affect injury severity, such as Manner and Wünsch-Ziegler (2013) and Kadilar (in press) where they found that road condition and speed limit both affected injury severity. Accident type was also found to affect injury severity by De Oña et al. (2011), Theofilatos et al. (2012), Kadilar (in press) and most recently by Manner and Wünsch-Ziegler (2013). According to Kadilar (in press) and Kockelman and Kweon (2002) the number of vehicles contributes significantly to the resulting injury severity, while lighting was found to be significant by both (Ma et al., 2009) and De Oña et al. (2011). Ma et al., (2009) found that, amongst other variables, road alignment was one of the contributing variables that affect severity while Theofilatos et al. (2012) showed that time of accident had also a significant effect.

On the other hand, in the original data set, Bayes.k2.AIC had a complexity of twenty-three with only one new interdependence, which was between horizontal alignment (TRAME) and LANE; whereas Bayes.Simulated.AIC had a complexity of twenty-one with three new interdependences between horizontal alignment (TRAME) with DIR, and SUP with both LIG , SEV.

Regarding complexity in the oversample data set, Bayes.K2.AIC had more arrows than all the other models (thirty-two arrows) with two new dependences between variables not found in the other models, which were the dependences between SEV with both TRAME and weather conditions (CATM). Bayes.Simulated. AIC had thirty-one arrows with seven new interdependences, which were between the following variables: DIR with PAV; PAT with LIG; ACT with SPE; SPE with CONT; LIG with DIR; LIG with GRADE and finally LIG with CATM.

# 3.4. Bayesian networks inference: 

Inference was used to determine the most significant variables that were associated with the occurrence of KSEV in traffic accidents. Table 9 presents values of variables that contributed the most to the occurrence of a KSEV outcome in a traffic accident. For each variable, the probability of a value was set to be one (setting evidence) and the other values of the same variable were set to be zero. Consequently, the associated probabilities of severity were calculated.

Table 9 shows the values of variables in which the probability of a KSEV was found to be higher than that of a SLIG. For example, this table shows that assigning a probability of one to the value VEH=1 (only one vehicle was involved in a traffic accident), results in a probability of KSEV of 0.5875 in K2.AIC model and 0.5877 in Simulated.AIC model when using the oversample data set.

These probabilities were calculated from the conditional probability table of the BN developed, and since it was intended to determine which values of variables contributed the most to the occurrence of a KSEV in a traffic accident, Table 9 did not include the variables in which the values of probabilities of SLIG were always higher than those of KSEV.

It should be mentioned that none of the variables values in the original data set was found to be significantly affecting KSEV; however, and for comparison purposes only, values of variables in the original data set were shown for the same values which were found to be significant in the oversample data set.

Setting evidences for the values of variables used to build the BN indicated that VEH, PAT, DIR, ACT, LIG, SUP, and SPE were found to be significant. A detailed discussion of the most significant variables that were found to contribute to the occurrence of a killed or severe injury (KSEV) in a traffic accident is given below.
[Insert here Table 9]
For both models in the oversample data set, accidents in which there was only one vehicle involved (VEH=1) were found to be associated with KSEV occurrence. This result was consistent with accident pattern variable (which also identified single vehicle as more significant in KSEV accidents) and accident type variable in which the categories more associated with KSEV (collision with fall off vehicle, collision with fixed object and collision with animals) involved only one vehicle. Manner and Wünsch-Ziegler (2013) concluded that accidents due to collision with a roadside object tend to be more severe than others. In addition, Theofilatos et al. (2012) showed that collision with fixed objects was one of the most affecting factors of road accident severity in urban areas.

Undivided roads were associated with KSEV injuries; this result was consistent with the findings of Hosseinpour et. al., (2014). Their results indicated that the presence of a median increased the probability of non-injury outcomes by $37 \%$, while the probabilities of slight, severe, and fatal injuries decreased by $8.4 \%$, $22.7 \%$, and $5.9 \%$, respectively.

The results also showed that when pavement surface value was others (conditions in which pavement was covered with mud, oil or sand) the severity of accident increased. Other researchers found that there was a relation between the surface status and resulting injury severity. Li, et al., (2013) used skid resistance amongst other variables to investigate injury severity of accidents in Texas, they used a skid score, which is a value between one (least skid resistance) and ninety-nine (most skid resistance), that describes the overall skid resistance of the data collection section. They stated that the tests did not show many meaningful relationships for different groups of crashes; however, results obtained suggested that there was a significant correlation between skid scores and crash severity outcomes for highways with dry surface condition, where pavements with lower skid resistance scores had more severe crashes than other skid scores.

According to Nevarez-Pagan (2008), driver crash involvements on locations with low skid resistance accounted for $28.56 \%$ of the severe injuries (total crashes) and $30.87 \%$ of the severe injuries (wet pavement crashes), however, the author recommended that the nature of these crashes (especially for wet pavement) should be further investigated. Herein, it should be emphasized that this specific condition was not prevalent (see Table 1), thus, it is suggested that the association between pavement surface condition and injury severity be further investigated.

In addition, it was found that accidents that occurred in dark lighting condition were mostly associated with KSEV, this was also found by Yannis et al. (2013) where they concluded that the absence of street lighting during nighttime had the highest impact on the number of fatalities and severe injuries. Haleem and Gan (2011) analyzed traffic accidents on urban roadways; they concluded that the afternoon peak period showed the highest reduction in fatality/severity relative to night off-peak. On the other hand, compared to dark lighting conditions, daylight had the highest reduction. This result was consistent with results obtained by Ma et al. (2009), where they showed that night without lighting led to a higher risk of accident severity.

Speed values higher than $70 \mathrm{~km} / \mathrm{h}$ were found to contribute to the occurrence of KSEV. This result was consistent with Manner and Wünsch-Ziegler (2013). Haleem and Gan (2011) also concluded that high speed limit sections experienced a significant increase in the occurrence of fatality/severity; where, Kadilar (in press) found that the drivers travelling at speeds of more than $111 \mathrm{~km} / \mathrm{h}$ have three times more risk than those travelling at speeds of less than $56 \mathrm{~km} / \mathrm{h}$.

# 4. CONCLUSIONS 

The study presented in this paper investigated the possibility of using sampling techniques on imbalanced traffic accidents data sets prior to using different Bayes classifiers in order to develop models used to predict severity level of a traffic accident. All the data used in the study was obtained for urban and sub- urban roads in Jordan.

The overall conclusion that can be drawn from this study is that using balanced data sets improved the ability of Bayes classifiers to classify killed and severe injuries correctly while keeping the classification ability of the other class (i.e. slight injuries) in an acceptable level. On the other hand, Bayes models developed using imbalanced data set were incapable of determining which values of variables were the most influencing to a killed or severe injury outcome in an accident.

Moreover, the results obtained using the original dataset were biased towards the majority class (i.e. slight injuries class) because of the dominating effect of the majority class, and so the classifier classified most instances as belonging to slight injuries class. However, the cost of misclassifying instances belonging to killed or severe injuries class far outweighs the cost of misclassifying the instances belonging to slight injury class. When using the classifier with balanced data set, the problem of costly misclassifications is much reduced to the extent that there was almost no bias towards any of the classes; more importantly, prediction of instances belonging to killed or severe injuries class was enhanced remarkably, especially when using oversampling approach.

It was also found that models developed using BNs, specifically those developed using K2 and simulated annealing search algorithms were the best among other Bayes classifiers. Vehicle involved, accident type, accident pattern, direction, number of lanes, road section, grade, pavement type, surface condition, atmospheric condition, speed, traffic control and lighting conditions were all found to have a significant effect on severe outcomes in an accident.

In addition, inference was used to determine which specific values of variables contributed the most to the occurrence of a killed or severe injury in traffic accidents. The results of inference indicated that the following values of variables were found to be associated with higher probabilities of accidents with casualties including killed or severe injuries: single vehicles accidents, two way undivided roads, fall off vehicle, fixed object collisions, collision with animals, accidents occurring during dark lighting conditions, pavement surface covered with mud, sand or oil, and speed limit higher than $70 \mathrm{~km} / \mathrm{h}$. In general, these results were consistent with the literature (Haleem and Gan, 2011; Theofilatos et al., 2012; Manner and Wünsch-Ziegler, 2013; Hosseinpour et. al., 2014).

Imbalanced data sets can be used to extract important knowledge when balanced, and since sampling techniques have proved their effectiveness in different research areas, this work indicated that they could also be applied in the domain of traffic accident when used in conjunction with BNs. Their effectiveness has been found to be similar to other techniques used to model severity in traffic accidents. Compared with other well-known statistical methods, the main advantage of using sampling techniques and BNs seems to be their complex approach where misclassification cost is higher in one class than in the other and when there is no pre-defined underlying relationship between target variable and predictors needed (Chang and Wang, 2006; Chawla, 2005).

# 5. Recommendations 

It should be emphasized that the effect of driver-related factors should be investigated to find out what implications they have on the severity of a traffic accidents along with the factors studied herein. In addition, authors recommend balancing traffic accidents data sets when learning from Bayes classifiers.

The results obtained herein might be used as guidance for PTD in order to develop countermeasures that aim to reduce traffic accidents severity in urban areas. They can also be used in safety awareness campaigns.

Authors of this research believe that collaboration between academic institutions and PTD is essential to help both apply and develop models that are used in the analysis of traffic accidents in order to determine the most influencing factors that contribute to the occurrence of a specific injury severity.

## Acknowledgements

The authors are grateful to the Police Traffic Department in Jordan for providing the data necessary for this research. Griselda López wishes to express her acknowledgement to the regional ministry of Economy, Innovation and Science of the regional government of Andalusia (Spain) for their scholarship to train teachers and researchers in Deficit Areas, which has made this work possible. The authors appreciate the reviewers' comments and effort in order to improve the paper.
