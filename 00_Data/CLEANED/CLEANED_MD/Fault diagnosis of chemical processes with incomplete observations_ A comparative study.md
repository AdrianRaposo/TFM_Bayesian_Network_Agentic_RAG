# Fault Diagnosis of Chemical Processes with Incomplete Observations: A Comparative Study 

M. Askarian ${ }^{a 1}$, G. Escudero ${ }^{b}$, M. Graells ${ }^{c^{*}}$, R. Zarghami ${ }^{a}$, F. Jalali-Farahani ${ }^{a}$, N. Mostoufi ${ }^{a}$<br>${ }^{a}$ School of Chemical Engineering, College of Engineering, University of Tehran, PO Box 111554563, Tehran, Iran.<br>${ }^{b}$ Computer Science Department. Universitat Politècnica de Catalunya. EUETIB, Comte d'Urgell 187, 08028-Barcelona, Spain.<br>${ }^{c}$ Chemical Engineering Department. Universitat Politècnica de Catalunya. EUETIB, Comte d'Urgell 187, 08028-Barcelona, Spain.


#### Abstract

An important problem to be addressed by diagnostic systems in industrial applications is the estimation of faults with incomplete observations. This work discusses different approaches for handling missing data, and performance of data-driven fault diagnosis schemes. An exploiting classifier and combined methods were assessed in TennesseeEastman process, for which diverse incomplete observations were produced. The use of several indicators revealed the trade-off between performances of the different schemes. Support vector machines (SVM) and C4.5, combined with $k$-nearest neighbourhood ( $k \mathrm{NN}$ ), produce the highest robustness and accuracy, respectively. Bayesian networks (BN) and centroid appear as inappropriate options in terms of accuracy, while Gaussian naïve Bayes (GNB) is sensitive to imputation values. In addition, feature selection was explored for further performance enhancement, and the proposed contribution index showed promising results. Finally, an industrial case was studied to assess informative level of incomplete data in terms of the redundancy ratio and generalize the discussion.


KEYWORDS: Fault diagnosis, Missing data, Incomplete observations, Classification, Imputation, Machine learning.

[^0]
[^0]:    ${ }^{1}$ Chemical Engineering Department. Universitat Politècnica de Catalunya. EUETIB, Comte d'Urgell 187, 08028-Barcelona, Spain.

    * Corresponding author. Tel.: +34 9341372 75.E-mail address: moises.graells@upc.edu

# 1. INTRODUCTION 

Due to the increasing complexity of modern industrial processes, preventive monitoring and fault diagnosis (FD) have become essential to ensure safe operation, improve product quality and sustain economic profit of manufacturing. A new generation of digital instruments, data processing devices, automation systems and high-performance computing tools, have promoted the development of a smart platform for plant monitoring and diagnosis. In addition, various methodologies have been developed to address the FD challenge (Venkatasubramanian et al., 2003). Among them, data-driven diagnosis methods offer appropriate solutions to many difficulties arising in this field (MacGregor and Cinar, 2012; Qin, 2012; Yin et al., 2012). This work investigates the performance of different data-driven FD approaches submitted to increasing loss of data.

FD is mainly a classification problem and machine learning provides various tools for classification. Based on the decision boundaries (hypothesis space source), classification approaches have 4 major types as listed below (Marquez et al., 2007):

- Distance based methods. e.g. $k$-nearest neighbourhood ( $k \mathrm{NN}$ ) (Duda et al., 2001) and centroid (Salton, 1989);
- Rule based methods. e.g. C4.5, as an extension of decision tree (Quinlan, 1993), and AdaBoost (Schapire and Singer, 1999);
- Probabilistic methods. e.g. Bayesian network (BN) (Pearl, 1988) and Gaussian naïve Bayes (GNB) (Friedman et al., 1997);
- Margin based methods. e.g. support vector machines (SVM) (Cristianini and Taylor, 2000) and artificial neural networks (Duda et al., 2001).

Performance of classifiers is affected by the quality of data, and there are potential factors that may cause incomplete data sets. Figure 1 shows the typical flow of data in a chemical plant and potential causes of missing data. In fact, chemical systems include different blocks, such as process, control, data acquisition, FD systems and human interface. Generally, sensors readings, off-line analyses, and records of actuators status constitute the input data source of the FD system in a chemical plant. These data are also called features or observations in the classification literature and they are used indistinctly. Furthermore, there are various types of media for transmitting data, such as wire, wireless (satellite and radio) and fiber-optic. In any case, different hardware, software or administrative problems

are likely to disrupt access of the FD system to complete datasets. Sensors and actuators are subject to different occasional failures due to wear, abrasion, exposure to physical damage or lack of energy supply (Kadlec et al., 2009; Zhao and Fu, 2015). They may be out of service due to maintenance or removal. In addition, improper calibration of sensors or control valves leads to unreliable or out of range data (Wang et al., 2007). Thus, the records may be automatically deleted by the preprocessing block of the monitoring system (e.g. outlier detection). Furthermore, different types of measurements and sampling rates (e.g. off-line analysis vs. on-line sensing) may produce sparse datasets (Kadlec et al., 2009) and information may be delayed by administrative issues (Warne et al., 2004). Moreover, temporary unavailability of data may happen due to malfunction or disruption of the data acquisition system, which have various causes such as higher bit rate error, short circuit of cables, break of circuit, induced current or even harsh weather (ISO, 1994; Ji and Elwalid, 2002; Rodriguez et al., 2002).

Based on the above discussion, in an industrial practice it is necessary to deal with incomplete datasets and unknown measurements, while continuously demanding useful and reliable information to support decision-making. Complexity of this issue depends on the mechanism of missing data and the informative level of the process database. Three standard mechanisms are usually considered (Rubin, 1976): missing completely at random (MCAR), missing at random (MAR), not missing at random (NMAR). MCAR and MAR are called ignorable mechanisms, and it is not required to take into account causes of missing data in the analysis of the datasets (Schafer, 1997). However, the NMAR mechanism leads to loss of valuable information that cannot be properly compensated (García-Laencina et al., 2010). On the other hand, the informative level of a database depends on the existence of co-linear variables, partial redundancy or duplication of data, which can simplify the analysis of missing data (Kadlec et al., 2009). Determining the informative level of a dataset was studied by Auffarth et al. (2010) and Peng et al. (2005)

Considering the above-mentioned facts, the performance of different FD methodologies to cope with incomplete input datasets needs to be examined. Since most diagnostic systems cannot assign a fault to incomplete features, it is required to consider additional procedures along with conventional classifiers. Indeed, FD with missing data concerns two different problems, handling missing values and classification. As shown in Figure 2, reported

approaches for solving these problems can be grouped into four types (García-Laencina et al., 2010; Scheffer, 2002; Sharpe and Solly, 1995)

- Deletion of the incomplete feature vectors, and classification of the complete data portion only;
- Development of a multi-classifier corresponding to all combination of feature subsets, and classification of incomplete data using the model trained by the same available features;
- Imputation or estimation of missing data, and classification using the edited set;
- Implementation of exploiting procedures for which classification can be still accomplished in the presence of missing variables.

In the first and third approaches, handling missing values (deletion and imputation, respectively) and classification are two problems that should be solved separately. In contrast, the second and fourth approaches are able to directly handle incomplete input datasets (Ahmad and Tresp, 1993; Huang, 2008). The first alternative is too simplistic and may be unacceptable in many applications. The second approach (multi-classifier) requires a set of training models based on all possible combinations of features. Sharpe and Solly (1995) have reported this promising approach to be more efficient than others while dealing with very limited number of faults and features. Although numerous features exist in chemical processes, this approach quickly explodes in terms of complexity and number of classifier models (Gabrys, 2002). Therefore, this work addresses and discusses the last two approaches (grey boxes in Fig. 2).

Estimation of missing values of a dataset, which is a preliminary step in the third approach, can be accomplished via various methodologies (Fortuna et al., 2007; Gonzalez, 1999; Little and Rubin, 2014). Generally, they can be grouped into four types in spite of the overlap between some basic principles:

- Regression: e.g. least squares (Chen and Chen, 2000), auto-regression and movingaverage models (Palit and Popovic, 2006) as well as $k \mathrm{NN}$ (Batista and Monard, 2002);

- Statistical method: e.g. mean (García-Laencina et al., 2010), maximum-likelihood (ML) and expectation-maximization algorithms (EM) (Ibrahim, 1990; Walczak and Massart, 2001b), principal component analysis (PCA) and partial least squares (PLS) (Kadlec et al., 2011; Nelson et al., 2006; Walczak and Massart, 2001a);
- Soft computing: e.g. artificial neural network (ANN) (Abdella and Marwala, 2005; Bishop, 1995) and fuzzy inference system (FIS) (Atkeson et al., 1997; Luo and Shao, 2006);
- Phenomenological models: e.g. first principle models such as energy and mass balance (Chéruy, 1997) and adaptive observers (Bastin and Dochain, 1990).

Moreover, attention has also been paid to hybrid methods (Kadlec et al., 2009). However, phenomenological models require deep understanding of the underlying physical and chemical phenomena, and are usually limited to ideal steady states. On the other hand, faults often lead to transient and/or unsteady state in chemical processes. Therefore, this work covers data-driven imputation models which readily reflect real conditions of process systems (grey boxes in Fig. 2).

Nelson et al. (1996) studied process monitoring in the presence of missing measurements using principal component analysis (PCA) and partial least squares (PLS). They presented three approaches for estimating scores: a single component projection method, a method of simultaneous projection to the model plane, and conditional mean imputation. Their analysis of a Kamyr pulp digester with 22 measurements and up to $20 \%$ missing data revealed that the conditional mean replacement method is generally superior to the other approaches. Subsequently, uncertainty intervals were derived for assessing the performance of monitoring applications with incomplete observations. The size of uncertainty regions helped to distinguish between situations where model performance with missing measurements was acceptable or not (Nelson et al., 2006).

The last approach of FD with missing data is exploiting procedures that have robust algorithms when coping with missing features. They can keep on classifying even in the presence of incomplete input data. For example, ID3 is an extension of the decision tree algorithm that handles an unknown feature by generating an additional edge for the unknown value. Thus, the classification of an incomplete dataset is fulfilled by taking into

account an unknown edge like other values (Sharpe and Solly, 1995). Nevertheless, the results have revealed that ANN is superior to ID3 in terms of classification performance. Furthermore, Huang (2008) proposed to take advantage of BN and the fact that it needs no change in the model and the network setup to cope with incomplete datasets. However, the reported results cannot be generalized to other cases due to generating redundant information by feature extension in that work. In other words, robustness of the BN was assessed in terms of missing artificial features rather than missing original data. Thus, a more comprehensive framework for evaluation of performance is required.

The aim of the above mentioned works was producing reliable diagnosis from new incomplete observations. However, developing an FD system from incomplete training data has also attracted researchers' attention. In this regard, various algorithms have been developed, including Bayesian PCA (BPCA) (Ge and Song, 2011), Hopfield neural networks (Wang, 2005) and training-estimation-training (TEST) (Yoon and Lee, 1999). This issue is important for developing a model with small sample size or online updating of the model. Nevertheless, since there exists a large amount of historical data in chemical plants, it is possible to provide a complete training dataset, because observations with missing values can be discarded from the training subset based on the assumption that observations are independent. Thus, designing a diagnostic system for chemical plants with training data contained missing measurements may not be a critical issue. Hence, this work is focused on the FD with new incomplete observations.

FD of chemical processes with missing data has not been satisfactorily addressed in the literature. Therefore, there is a need to provide an appropriate FD framework dealing with incomplete data. Comprehensive assessment of various tools, as well as identification of their advantages and limitations is required. In the present work, standard centroid, C4.5, GNB, and SVM methods, as representative of each type of classification approaches (Marquez et al., 2007), were investigated while missing values were artificially produced in the datasets. Diagnosis performance of the exploiting procedure (BN), facing incomplete data, was specified. Imputation was accomplished using mean, PCA, $k \mathrm{NN}$ and ANN as statistical, regression, and soft computing methods, respectively. Combinations of different imputation and classification models were examined. Various indexes, such as accuracy, robustness and sensitivity, were defined for an evaluation purpose. Moreover, enhancing

the performance of the classification was explored through feature extraction. Finally, a new index was proposed to determine the level of redundancy, which facilitates handling of incomplete data.

# 2. METHODOLOGY 

### 2.1. Tools

In this section, classification and imputation methods used in the subsequent sections are introduced.

### 2.1.1. Classification

Different types of classifiers are listed in Section 1. In the present work, FD systems are developed by following methods:

- Centroid (distance based), which is based on "mean difference" as a simple and intuitive concept of discrimination (Jiang et al., 2009).
- C4.5 (rule based), which builds decision trees consisting of sets of ordered rules based on information entropy (Amarnath et al., 2013). Then, the decision tree that best matches a new observation in terms of highest weight reflects the type of fault.
- GNB and BN (probabilistic), which consist of maximizing the conditional probability of a particular fault given a set of observations (Liu et al., 2010; Verron et al., 2007). A Gaussian probability and a conditional probability table (CPT) are assigned to each variable using GNB and BN, respectively.
- SVM (margin based), which discriminates different fault instances, as positive and negative points, using a kernel function (hyperplane) that maximizes the margin (Yélamos et al., 2009).


### 2.1.2. Imputation

Most monitoring or diagnosis algorithms fail in case of missing data, and imputation is suggested as an alternative solution (Fig. 2). In this study, four imputation options are examined to edit an incomplete dataset: the mean imputation and PCA, which are statistical methods, the $k \mathrm{NN}$ imputation, which is a regression, and ANN, which is a soft computing method.

The mean imputation is the earliest and easiest approach that fills the missing point by the average value of that variable in the historical records. Another statistical alternative is an iterative algorithm based on PCA. It consists of initial estimation of missing values, decomposition to principal components, reconstruction of features, and replacing of prediction in missing variables until convergence (Walczak and Massart, 2001a). Multilayer perceptron (MLP), which is one of the most popular ANN-based models, utilizes supervised learning technique, called back-propagation. Thereafter, it is used for estimation of missing values based on other available values. The $k \mathrm{NN}$ method is a distance based method, in which $k$ (number of nearest neighbours) donors are selected from the complete historical database, so that they minimize a distance function. Then, the average of corresponding variable in the $k$ donors is replaced in the missed point.

It is worth noting that although the $k \mathrm{NN}$ method is usually implemented for classification purposes, in the present work it is used for regression. Furthermore, it is more advantageous to apply the $k \mathrm{NN}$ method rather than conventional regression methods, in which explicit model should be trained. Based on the "lazy learning" approach of $k \mathrm{NN}$ that locally approximates the distance function, no training model construction is required (Zhang and Zhou, 2007). In this way, the $k \mathrm{NN}$ method can be easily applied even if various measurements are missed at each time step.

# 2.2. Design of Experiments 

Figure 3 illustrates the general procedure for evaluation of FD performance whenever datasets are incomplete. The procedure is described as follows:
Step 1: The original data are arranged in a matrix in which each row represents the time series of a measured variable. For each state of the system (faulty and normal), $T^{f}$ samples of $V$ variables are recorded in the matrix:

$$
\mathbf{X}^{f}=\left[\begin{array}{cccccc}
x_{11}^{f} & x_{12}^{f} & \cdots & & \\
x_{21}^{f} & x_{22}^{f} & \cdots & & \\
\vdots & \vdots & \ddots & \vdots & \\
x_{t-1}^{f} & x_{t-2}^{f} & \cdots &
\end{array} \quad \mathbf{X}^{f} \in R^{V \times T} ; \quad v=1,2, \ldots, V \quad t=1,2, \ldots, T^{f}\right.
$$

where $x^{f}{ }_{v t}$ is the value of the $v^{t h}$ measured variable at the sampling time $t$ in the $f^{t h}$ state of the system. Then, the collection of $F$ various states are considered as a labelled process dataset:

$$
\boldsymbol{X} \cdot \mathbf{L}=\left\{\mathbf{X}^{f} \mid f=1,2, \ldots, F\right\} \quad \boldsymbol{X} \cdot \mathbf{L} \in R^{F \times V \times T^{f}}
$$

Step 2: The labelled process dataset, $\mathbf{X} \mathbf{L}$, is split into training matrix, $\mathbf{X} \mathbf{L}$, and a test matrix, $\mathbf{X}$, which are used for fitting the parameters of the models and estimating of unknown faults, respectively. For the sake of simplicity, in the subsequent sections, the $f^{\text {th }}$ index of measurements is ignored (e.g. $x_{\mathrm{vr}}$ ) whenever dealing with the test dataset.
Step 3: The training matrix, $\mathbf{X} \mathbf{L}$, is standardised as follows, to make the algorithm less sensitive to particular variables:

$$
\begin{aligned}
& \dot{\sim} \quad \frac{\mu_{v}}{v_{v}} \\
& \mu_{v}=\frac{\sum_{f=1}^{F} \sum_{i=1}^{v} x_{v i}^{f}}{\sum_{f=1}^{F} v_{v}} \\
& \sigma_{v}=\sqrt{\frac{\sum_{f=1}^{F} \sum_{i=1}^{v}\left(x_{v i}^{f}-\mu_{v}\right)^{2}}{\sum_{f=1}^{F} v_{v}}}
\end{aligned}
$$

where $\bar{I}$ is the number of training samples for each fault.
Step 4: Parameters of each classifier, mentioned in section 2.1, are fitted based on the standardised training matrix, $\mathbf{X} \mathbf{L}$, obtained in the previous step.
Step 5: Some measurements are artificially deleted from the complete test dataset, $\mathbf{X}$. In particular, 4 incomplete test matrices were produced in this work by random deletion of $10 \%, 20 \%, 30 \%$ and $40 \%$ of measurements. All test matrices are scaled using mean (Eq.4) and variance (Eq.5) of the training dataset.

Step 6: Imputation methods are applied to configure an estimated full test dataset, $\mathbf{X}^{\prime}$, based on the complete training dataset, $\mathbf{X}^{\prime} \mathbf{L}$. The BN, as an exploiting method, can skip the imputation step to predict faults with incomplete data.
Step 7: The efficiency of different imputation methods is evaluated by the Pearson correlation as the predictive accuracy (PAC) index:

$$
P A C=\frac{\sum_{n=1}^{N} C}{\sqrt{\sum_{n=1}^{N} C} \cdot \frac{1}{1_{n=1}}}
$$

where $N$ is the number of missing values; $\because$ and $\because$ are true (in $\mathbf{X}^{\prime}$ ) and imputed (in $\mathbf{X}^{\prime}$ ) values of the $v^{\text {th }}$ variable, respectively; and $i$ and $i$ are the means of the true and imputed values of the $v^{\text {th }}$ variable, respectively. A good imputation method will produce a PAC value close to 1 .

Step 8: The snapshot of the test dataset at each time step, [ $\because$, is assigned to the fault that is predicted by the classifier.

Step 9: The performance of classifiers is evaluated by comparing predicted faults and true faults for each snapshot. In this order FD outcomes are arranged in a confusion matrix as presented in Table 1 (Yélamos et al., 2007). Then, performance indexes including accuracy, precision, recall, and $F 1$ are calculated as follows:

$$
\begin{aligned}
& \text { Accuracy }=\frac{a+d}{a+b+c+d} \\
& \text { Precision }=\frac{a}{a+b} \\
& \text { Recall }=\frac{a}{a+c} \\
& F 1=\frac{2 \times \text { Precision } \times \text { Recall }}{\text { Precision }+ \text { Recall }}
\end{aligned}
$$

where $a$ is the number of samples corresponding to faulty situations and diagnosed as such (true positive); $b$ is the number of samples diagnosed as faulty but were not (false positive); $c$ is the number of samples corresponding to faulty but not diagnosed situations (false negative) and $d$ is the number of samples not happened and not diagnosed (true negative). The classifier performance regarding each individual fault is assessed through $F 1$, which can be interpreted as a weighted average of the precision and recall. The accuracy index is appropriate for global evaluation.

# 3. TEP CASE STUDY 

The Tennessee-Eastman process (TEP) proposed by Downs and Vogel (1993) is widely used for testing diagnosis techniques. The dynamic simulation of this process includes a

control strategy created by Ricker (1996). Figure 4 illustrates the process and instrumentation diagram of the TEP, which consists of five major unit operations, including a reactor, a product condenser, a vapour-liquid separator, a recycle compressor and a product gas stripper. Two products ( $G$ and $H$ ) are produced by two simultaneous gas-liquid exothermic reactions and a byproduct $(F)$ is generated by two additional exothermic reactions from reactants $A, C, D$ and $E$. This process has 12 manipulated variables, 22 continuous measurements and 19 composition measurements. The 20 predefined faults of the TEP are presented in Table 2. The TEP includes random error and white noises that impact on diagnosis complexity.

The original datasets, $\mathbf{X}^{f}$, were generated by the simulation of a 30-h operation horizon for each fault and the normal situation. Sampling every 0.1 h resulted in a labelled process data matrix, $\mathbf{X} \cdot \mathbf{L} \in R^{21 \times 53 \times 300}$. Training dataset, $\mathbf{X} \mathbf{L} \in R^{21 \times 53 \times 180}$, and test dataset, $\mathbf{X} \in R^{21 \times 53 \times 120}$, were built by randomly splitting samples ( $60: 40$ ratio). After standardising the training dataset, the 5 FD systems, centroid, C4.5, BN, GNB, and SVM (default radial based function) were used and assessed. In order to compare their raw performance in case of incomplete observations no parameter tuning was attempted to the standard methods.

# 4. RESULTS AND DISCUSSION OF THE TEP CASE STUDY 

### 4.1. Performance

As discussed in section 1, the BN is able to exploit all available information, complete or incomplete, to estimate the state of the system (Huang, 2008). In the first stage, the capability of this FD approach was evaluated on the TEP to produce a reference result for subsequent comparison. The performance index, F1, for each fault is given in Appendix A. Figure 5 illustrates how the global accuracy of the BN degrades with missing data. The global accuracy of the BN drops below 0.10 , while more than $20 \%$ of data are not available. On the other hand, simple mean imputation can recover accuracy of the BN to some extent. Furthermore, pre-treatment of the incomplete test data with 3 NN imputation shows significant performance improvement of the BN.

From algorithmic point of view, the BN can keep inference of the state of the system even with incomplete data, as mentioned before. Despite its apparent robustness, the BN classifier has performed poorly in the presence of missing data. The main reason is

existence of numerous faults in the TEP case study that burden the classification. However, BN performance was enhanced when combined with imputation (Fig. 5). When partial data are missing, most methodologies require imputation to edit the test dataset before classification. Subsequently, the performance of centroid, C4.5, BN, GNB and SVM, coupled with different imputation methods, mean, PCA, ANN and 3NN, were analysed. Figure 6 illustrates the global accuracy of these methodologies as a function of data incompleteness. FD methods can be ranked in terms of global accuracy as follows: C4.5, GNB, SVM, BN and centroid when data are complete ( $0 \%$ missing data). This can be taken as a reference for further comparative purposes. In addition, despite the type of classifier, 3 NN and ANN imputation keeps the performance higher than other imputations due to higher accuracy in terms of PAC (Appendix A).

The accuracy loss due to missing data also depends on the classification along with the imputation choice. In order to quantify this effect, the robustness index is introduced as:

$$
\text { Robustness }=\frac{\text { Accuracy }^{\text {mix }}}{\text { Accuracy }^{\text {comp }}}
$$

where Accuracy ${ }^{\text {comp }}$ and Accuracy ${ }^{\text {mix }}$ are the accuracies obtained by each method when missing data in the test sets, $\mathbf{X}$, is $0 \%$ and $40 \%$, respectively. Hence, Figure 7 compares the fault diagnosis methods in terms of robustness. Generally, 3 NN imputation is shown to provide the highest robustness, regardless of the type of classifier. Despite high accuracy of C4.5 in case of complete observations (Fig. 6), it does not keep this behaviour whenever faced with incomplete observations (Fig. 7). In other words, C4.5 is not robust respect to missing data.

Furthermore, the imputation approaches, mean, PCA, ANN and 3NN, have different impact on the accuracy. The sensitivity of each integrated methodology can be assessed by the following index:

$$
\text { Sensitivity }=\text { Accuracy }^{\max }- \text { Accuracy }^{\min }
$$

where Accuracy ${ }^{\text {max }}$ and Accuracy ${ }^{\text {min }}$ are maximum and minimum accuracies obtained by the corresponding classifier when the test sets suffer $40 \%$ missing data. Sensitivities of different approaches are compared in Figure 8. This figure shows that SVM and centroid methods are less sensitive than other algorithms.

This behaviour can be explained by the principles (space source hypothesis) of these methods. In the training stage, decision boundaries that can discriminate faults are determined. Training of SVM and centroid includes a loop that determines the optimal boundary in terms of maximum margin. However, training of other methods terminates once a decision boundary is determined. The optimal decision boundary of SVM and centroid allows to better discriminate the feature space regardless of the imputation method. In other words, the widest margin surrounding the boundary increases the tolerance limit of the feature space. This is in accordance with the fact that learning bias has proved to have good properties in terms of generalization bounds for the classifier (Marquez et al., 2007).

# 4.2. Computational time 

The computer configuration used in this work was a core i7-3770@3.40GHz processor with 8GB RAM. Computational times of all models, considering various ratios of missing data, are given in the Appendix A. In general, results reveal that CPU times for classification models are negligible in comparison with imputation models. In terms of increasing CPU time, imputation methods rank as follows: mean, PCA, 3NN, ANN. On the other hand, 3 NN and ANN have higher accuracy in terms of PAC compared with mean and PCA. Furthermore, Figure 7 shows that integration of any classifiers with 3NN imputation guarantees the highest robustness of the fault diagnosis. However, 3NN and ANN require higher computational effort than mean and PCA imputation.

The performance of imputation would be greatly improved if the computational burden can be reduced, and reduction of the search space seems worthy of being explored towards this end. In other words, decreasing the number of variables can help finding the nearest neighbour sooner. Therefore, the subset of measurements that are highly affected by different faults should be selected as the significant feature set. The contribution index (CI ) is introduced in this work for the feature selection as:

$$
C I_{v}^{f}=1-\frac{\sum_{i=1}^{F} \sum_{t=1}^{t}\left\|x_{v t}^{f}-x_{v t}^{i}\right\|}{\sum_{i=1}^{F} \sum_{j=1}^{i} \sum_{t=1}^{t}\left\|x_{v t}^{j}-x_{v t}^{i}\right\|} \quad \forall f, \forall v \quad \mathbf{C I} \in R^{F \times F}
$$

The deviation of the measurements corresponding to each fault at each time step is assessed by the Euclidean distance. Then, a subset of variables, $\mathrm{V}^{f}$, consisting of the $S$ elements having the highest $C I_{i}^{f}$ is selected as the collection of significant features for each fault:

$$
\begin{aligned}
& I=\{1,2, \ldots, V\} \\
& v^{f}=\left\{A^{f} \subset I \quad\left|A^{f}\right|=\mathcal{S}^{-}, \min _{\substack{i \in A^{f} \\
i \in A^{f}}}\left\{\geq \max _{\substack{j \in I \backslash A^{f}}}\left\{C I_{j}^{f}\right\}\right\} \quad \forall f\right.
\end{aligned}
$$

A set of significant features, $\mathbf{V}$, is the union of these subsets:

$$
\mathbf{V}=\bigcup \mathrm{V}
$$

In the TEP case study, the set $\mathbf{V}$ includes 41 measurements while $S$ is 15 . Therefore, variables of the significant feature matrix would be reduced from 53 to 41 , i.e., $\mathbf{x}^{\prime} \mathbf{L} \in R^{21 \times 41 \times 300}$. Then steps 2-9 of the procedure described in section 2.2 were implemented on the matrix $\mathbf{x}^{\prime} \mathbf{L}$. Figure 9 shows how this feature reduction can substantially decrease the computational effort of the 3 NN imputation. In addition, Figure 10 demonstrates the effect of this feature selection on the accuracy of the different fault diagnosis approaches examined. Generally, higher accuracy and lower CPU time are achieved by feature selection regardless of imputation methods (Appendix A). Therefore, significant improvements can be achieved by appropriate feature selection, although further investigation is required to assess and compare other feature selection techniques.

# 4.3. Comparison assessment of TEP 

In sections 4.1 and 4.2, different algorithms were evaluated using various criteria in the presence of missing measurements. This section presents an overall comparison of the methods through the following normalized indexes:

$$
A=\frac{\text { Accuracy }- \text { Accuracy }^{\min }}{\text { Accuracy }^{\max }- \text { Accuracy }^{\min }}
$$

$$
\begin{aligned}
& T_{i}=1-\frac{C P U_{\text {imputation }}}{C P U_{\text {imputation }}^{\max }} \frac{-C P U_{\text {imputation }}}{-C P U_{\text {imputation }}^{\min }} \\
& T_{c}=1-\frac{C P U_{\text {classification }}}{C P U_{\text {classification }}^{\max }} \frac{-C P U_{\text {classification }}^{\min }}{-C P U_{\text {classification }}^{\min }} \\
& S=1-\frac{\text { Sensitivity }- \text { Sensitivity }^{\text {min }}}{\text { Sensitivity }^{\text {max }}- \text { Sensitivity }^{\text {min }}} \\
& R=\frac{\text { Robustness }- \text { Robustness }^{\text {min }}}{\text { Robustness }^{\text {max }}- \text { Robustness }^{\text {min }}}
\end{aligned}
$$

In each index, minimum and maximum performance criteria correspond to the best and worst results calculated in previous sections. In this way, the capability of each tool in terms of each index is normalized and scaled to facilitate the comparison. The spider plots of indexes for each integrated methodology based on the significant feature matrix are illustrated in Figure 11, in which rows and columns correspond to the classification and imputation methods, respectively. Each axis of the spider plots represents an index (Eqs.17-21). For comparative assessment, it should be noted that closeness of indexes to one or zero reflects superiority and inferiority of a correspond method, respectively.

The selection of an appropriate fault diagnosis methodology depends on the process monitoring requirements, but accuracy is imperative because a false alarm may mislead operators. Hence, centroid and BN are not recommended in terms of accuracy. On the other hand, C4.5-3NN guarantees the highest accuracy (Eq. 17), and is applicable while FD computational time is not important issue, e.g. in case of offline monitoring, root case analysis or availability of a high-performance computing system. Otherwise, a flexible FD approach enabling the operator to select and switch imputation methods could be considered. In this way, the classification combined with PCA imputation allows quickly inferring the state of the system (Eq. 18), and more reliable results would be obtained through 3 NN imputation. Thus, the GNB, which is too sensitive to imputation values, is not an appropriate choice (Eq. 20). Furthermore, SVM performs better than C4.5 and GNB in terms of robustness (Eq. 21), which is an important issue in case of increasing loss of data. Finally, Figure 12 demonstrates an FD scheme that can tolerate missing data for a general application. It represents interactions between various blocks including: feature extraction, classification and imputation.

# 5. INDUSTRIAL CASE STUDY 

Data from an industrial gas sweetening unit was used for further validation and discussion of the proposed model. Most gas processing plants include a sweetening unit for removing sour gas components from the gas stream, using chemical solvents such as amines (Fig. 13). The acid gas constituents $\left(\mathrm{H}_{2} \mathrm{~S}\right.$ and $\left.\mathrm{CO}_{2}\right)$ react with an aqueous solution in a highpressure absorber. Subsequently, the acid constituents are stripped from the solvent in a regenerator at high temperature.

One of the most frequent problems in a gas sweetening unit is amine foaming in the absorber, which results in loss of proper vapour-liquid contact, solution hold up and poor solution distribution. The adverse consequences include off-specification product, excessive amine loss, reduced gas-treating capacity and energy loss. Some root causes of foaming, which are considered as faults, are accumulation of heavy hydrocarbon, solid particle in amine and surface active agents in the feed fluid. Therefore, in this work there are four different states, including the mentioned faults and the normal case.

Records of 48 on-line sensors in significant parts of a gas sweetening unit were available from a gas refinery. Among them, 3, 5, 8 and 11 sensors for pressure, level, flow and temperature were selected based on CI (Eq. 13). The database, $\boldsymbol{x} \boldsymbol{\mathbf { L }} \in R^{4 \times 27 \times 1250}$, was provided by the 27 sensors and consisted of 1250 sample points for each individual state of the system, which include normal, presence of surface active agents, solid particles in the system, and hydrocarbon accumulation in the column. The time interval between samples was 1 min .

A training dataset, $\mathbf{X} \mathbf{L} \in R^{4 \times 27 \times 625}$, which had complete records of measurements, was selected. In order to evaluate the proposed procedure, five different testing subsets, $\mathbf{X} \in R^{4 \times 27 \times 125}$, were considered. Two test datasets suffered $11 \%$ and $26 \%$ missing data during operation of the real plant. It is worth mentioning that missing data were not artificially induced. Moreover, artificial incomplete data is required to provide a reference for evaluation of the real mechanism. Thus, $0 \%, 11 \%$ and $26 \%$ measurements were randomly deleted from the other three complete test datasets.

# 6. RESULTS AND DISCUSSION OF THE INDUSTRIAL CASE STUDY 

In the TEP case study, missing data had a random mechanism. Herein, it was intended to evaluate the diagnostic performance when dealing with a real case. The accuracy of prediction of missing data and FD performance extremely depend on the informative level of data. When some features highly depend on each other or their duplication or partial redundancy exist, the imputation methods may accurately estimate missing values based on the available values (Kadlec et al., 2009). Consequently, discrimination efficiency of the FD system is not expected to significantly degrade if redundant features exist. In order to assess this important issue, an index, called redundancy ratio, is introduced here.

In order to calculate the redundancy level of a dataset, it is required to evaluate dependency of variables. It is usually characterized in terms of mutual information (Sayood, 2012), which is obtained based on the training dataset as follows:

$$
M I_{i j}=\sum_{t=1}^{V} \sum_{j=1}^{V} \sum_{f=1}^{F} \sum_{t=1}^{f} P\left(x_{i t}^{f}, x_{j t}^{f}\right) \log \left[\frac{P\left(x_{i t}^{f} \mid x_{j t}^{f}\right)}{P\left(x_{i t}^{f}\right)}\right] \quad M I \in R^{V \times V}
$$

Thereafter, inherent informative level of an original database in terms of redundancy can be quantified by the redundancy index, $R I$, which has been introduced by Peng et al. (2005):

$$
R I=\frac{1}{|\mathbf{X}|^{2}} \sum_{x_{i t}, x_{j t} \in \mathbf{X}} M I_{i j}
$$

In case of incomplete dataset, the redundant information is disturbed. Degradation of informative level of data due to missing data can be characterized by the redundancy ratio, $R R$, as follows:

$$
R R=\frac{|\mathbf{X}|^{2}}{\left|\mathbf{X}_{N a N}^{c}\right|^{2}} \sum_{x_{i t}, x_{j t} \in \mathbf{X}} \frac{M I_{i j}}{\sum_{x_{i t}, x_{j t} \in \mathbf{X}} M I_{i j}}
$$

where $\mathbf{X}_{N a N}$ and $\mathbf{X}_{N a N}^{c}$ are incomplete and complete subsets of $\mathbf{X}$.

This analysis was implemented on the dataset of the sweetening unit. $M I \in R^{27 \times 27}$ was determined based on the training subset using Eq. (22). Then, redundancy ratios of the complete and incomplete testing subsets were achieved based on Eq. (24) which are shown in Figure 14 by solid lines. The negative slopes of these lines show that the missing data degrades the informative level of the data (have measured in terms of redundancy ratio). Furthermore, the effect of the real mechanism of missing data was more adverse than that of the random mechanism which led to the lowest redundancy ratio. It is expected that estimation of missing data might be burden with lower informative level of the real case study. Thereafter, incomplete data was edited by the 3 NN imputation, which is an efficient approach according to the TEP case study (Fig. 11). Then, accuracy of the 3 NN imputation in terms of PAC was assessed, as shown in Figure 14 by dashed lines. Although the real mechanism of missing data has led to a lower PAC in comparison with the random mechanism, the impact is minor.

Next, the FD system was developed based on $\mathbf{X} \mathbf{L}$ using C4.5-3NN, which was shown to be the most accurate classifier among the others (refer to Section 4.3). Performance of the FD system for real and random mechanisms of missing data was evaluated in terms of accuracy and the results are presented in Figure 15. The minor deviation of accuracy due to mechanisms reveals that this industrial case study has approximately a random mechanism. Consequently, the cause of missing data is ignorable. Therefore, the results of TEP case study can be generalized to this case as well.

# 7. CONCLUSION 

Fault diagnosis of chemical process systems with missing data, which is a common problem in the industrial practice, was investigated. Machine learning provides tools to cope with this challenge rather than ignoring incomplete observations, but they need to be assessed and compared. This work undertakes this comparative study using the TEP benchmark, for which missing values were artificially produced in the datasets.

First, the BN, as a promising exploiting option, was evaluated. This technique can directly infer the state of the system even in case of incomplete information. However, the alternatives of editing the incomplete observations using imputation were shown to produce better performance. Then, the combination of various classifiers -centroid, SVM,

GNB, BN, and C4.5- with imputation methods -mean, PCA, ANN and $k \mathrm{NN}-$ was investigated. It was found that C 4.5 integrated with 3 NN imputation results in the highest accuracy. BN and centroid are not appropriate selection in terms of accuracy. The combination of SVM with 3 NN is highly robust to missing measurements. In addition, SVM was shown to be scarcely sensitive to the imputation method, while the GNB is very sensitive.

The trade-off between performance indicators, including accuracy, robustness, sensitivity and computational effort, was discussed and practical guidelines are proposed. However, the best approach should be selected based on the most important requirements of each practical application. Finally, the feature reduction, by means of the proposed contribution index (CI), was examined to reduce the computation effort, and the promising results obtained encourage future work to assess and compare further feature selection techniques.

Sweetening gas unit of an industrial plant was studied to explore the effect of mechanism of missing data. The real incomplete datasets have a low deviation from the random missing mechanism in terms of redundancy ratio. Thus, the original cause of missing data can be ignored in the analysis. Therefore, results and guidelines obtained in the TEP case study can be also implemented for this case.

# NOMENCLATURE 



# Greek symbols 

$\mu_{v} \quad$ mean of the $v^{t h}$ variable in the training dataset
$i$ mean of true values of the $v^{t h}$ variable in the test dataset
$i$ mean of a imputed the $v^{t h}$ variable in the test dataset
$\sigma_{\mathrm{v}} \quad$ variance of the $v^{t h}$ variable in the training dataset

## Acronyms

ANN artificial neural network
BN Bayesian network
Cond condensate
CPU central processing unit
CWS cold water stream
DCS distributed control system
EM expectation-maximization
FD fault diagnosis


# ACKNOWLEDGEMENTS 

Financial support from the Iranian ministry of science, research and technology, as well as South Pars Gas Complex is acknowledged. Also, Financial support from the Spanish MICINN/MINECO and FEDER funds (Projects EHMAN, DPI2009-09386 and SIGERA, DPI2012-37154-C02-01) and the Generalitat de Catalunya (2014 SGR 1092) is fully appreciated.

# Appendix A. Supplementary data 

Supplementary data associated with this article can be found, in the online version.

# List of Tables: 

Table 1: Confusion matrix
Table 2: Pre-defined process faults in the Tennessee-Eastman process.

## List of Figures:

Figure 1: Flow of data in chemical plants and potential causes of incomplete data.
Figure 2: Different approaches for FD with missing data (scope of this work is in grey).

Figure 3: Procedure of experiment for FD with incomplete data.
Figure 4: Process and instrumentation diagram of Tennessee-Eastman chemical process (Downs and Vogel, 1993).

Figure 5: Performance of BN for FD, exploiting method vs. imputation methods.
Figure 6: Impact of missing data on performance of different classifiers coupled with imputation methods (a)mean; b)PCA; c)ANN; d)JNN).

Figure 7: Robustness of different FD methodologies.
Figure 8: Sensitivity of different integrated FD systems to imputation approaches.
Figure 9: CPU of $k \mathrm{NN}$ imputation for different sizes of the feature matrix.
Figure 10: Accuracy of classifiers for different sizes of the feature matrix.
Figure 11: Comparative assessment of integrated methods for FD.
Figure 12: General scheme of FD using combination methods which can tolerate missing data.

Figure 13: Process flowsheet of the sweetening unit of the gas refinery.
Figure 14: Redundancy ratio of incomplete datasets and corresponding PAC using 3NN imputation.

Figure 15: Diagnosis accuracy of real and random mechanisms of missing data.