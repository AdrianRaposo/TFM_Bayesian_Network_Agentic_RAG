# Uncertainty-aware Fusion of Probabilistic Classifiers for Improved Transformer Diagnostics 

Jose Ignacio Aizpurua, Member, IEEE, Victoria M. Catterson, Senior Member, IEEE, Brian G. Stewart, Member, IEEE, Stephen D. J. McArthur, Fellow, IEEE, Brandon Lambert, and James G. Cross Senior Member, IEEE


#### Abstract

Transformers are critical assets for the reliable operation of the power grid. Transformers may fail in service if monitoring models do not identify degraded conditions in time. Dissolved gas analysis (DGA) focuses on the examination of dissolved gasses in transformer oil to diagnose the state of a transformer. Fusion of black-box classifiers, also known as an ensemble of diagnostics models, have been used to improve the accuracy of diagnostics models across many fields. When independent classifiers diagnose the same fault, this method can increase the veracity of the diagnostics. However, if these methods give conflicting results, it is not always clear which model is most accurate due to their black-box nature. In this context, the use of white-box models can help resolve conflicted samples effectively by incorporating uncertainty information and improve the classification accuracy. This paper presents an uncertainty-aware fusion method to combine black-box and white-box diagnostics methods. The effectiveness of the proposed approach is validated using two publicly available DGA datasets.


Index Terms-Condition monitoring, transformer diagnosis, ensembles, classifiers, uncertainty.

## I. INTRODUCTION

TRANSFORMERS are critical assets in the power grid. The unexpected failure of a power transformer can lead to different consequences ranging from a lack of export capability to catastrophic failure [1]. Condition monitoring techniques examine the health of the system under study periodically with the aim to identify anomalies and avoid unexpected failures, e.g. [2], [3], [4]. The different components of a transformer can be monitored through different parameters [5]. This paper focuses on transformer insulation health assessment through dissolved gas analysis (DGA) [6]. The wide industrial acceptance and extended implementation of DGA monitors is the rationale and motivation to focus on DGA.

Operational and fault events generate gases which are dissolved in the oil that circulates through a transformer for cooling and insulation purposes. DGA is a mature and industry-standard method that focuses on the study of these gases [6]. The effective application of DGA enables timely diagnostics of possible insulation problems.

[^0]There are different industry-accepted classical DGA methods including Duval's triangle, Roger's ratios or Doernenburg's ratios [6]. These techniques classify transformer faults based on the predefined range of specific fault gas ratios. However, their accuracy is limited because they assume crisp decision bounds [7]. This leads to a decreased diagnostics accuracy and conflicting diagnostics outcomes among methods which do not help engineers in the decision-making process. So as to improve the classification accuracy a number of blackbox (BB) machine learning models have been proposed.

Comparisons among different DGA models are representative only when they are analysed in the same conditions. Focusing on the methods tested on the publicly available IEC TC 10 dataset [8], Mirowski and LeCun used k-nearest neighbor ( kNN ), support vector machine (SVM) and artificial neural network (ANN) models [9]. Wang et al. used deep learning methods through a continuous sparse autoencoder (CSA) [10]. The combined use of optimization and classification models has also been explored through gene programming (GP) and SVM, ANN and kNN models [11] or genetic algorithms (GA) and SVM models [12]. Table I reports the main characteristics.

TABLE I
MACHINE LEARNING MODELS TESTED ON THE IEC TC 10 DATASET.


The type of the classification problem has implications for decision-making purposes. Binary classifiers focus on identifying healthy or faulty samples, but they do not give more information about the type of fault present. Additionally, the number of training and testing samples directly influences the classification accuracy. The more samples that are used for training the greater will be the accuracy (e.g. [10]). However, the generalization of the diagnostics model is penalised when the testing set is much smaller than the training set.

There have been more DGA classification models tested on different proprietary datasets so as to improve the accuracy of classical methods such as fuzzy logic based DGA method [13], adaptive neuro fuzzy inference system (ANFIS) which combines ANN with fuzzy logic [14], SVM with resampling and boosting [15], differential evolution (DE) combined with extreme learning machines [16], or relevance vector machines combined with ANFIS [17].


[^0]:    J. Aizpurua, V. Catterson, B. Stewart \& S. McArthur are with the Inst. of Energy \& Environment, Univ. of Strathclyde, Glasgow, UK (e-mail: jose.aizpurua@strath.ac.uk; vic@ieee.com; brian.stewart.100@strath.ac.uk; s.mcarthur@strath.ac.uk);
    B. Lambert is with Bruce Power, Tiverton, Canada (e-mail: bran-don.lambert@brucepower.com;
    J. Cross is with Kinectrics Inc., Toronto, Canada (e-mail: james.cross@kinectrics.com).

Although the accuracy of these BB models tends to be high $(\sim 90 \%)$, there is no explainability of the results, i.e. they represent purely numerical connections and lack an interpretation of physical significance for an engineer. Additionally they do not integrate the uncertainty associated with the diagnostics outcome and assign either $100 \%$ belief to a single health state or a deterministic probability value. Therefore these techniques may be less desirable for engineering usage because there is no further information about the confidence in the result.

It is possible to specify subjective and imprecise information through fuzzy logic. However, fuzzy rules need to be specified manually based on experience and their diagnosis outcome is not a probability density function (PDF) which integrates uncertainty information. The work introduced in this paper focuses on data-driven Bayesian methods to determine decision bounds and deal with diagnostics uncertainties. Some fuzzy logic models have been designed to identify multiple fault conditions [13]. This work is focused on the identification of single fault conditions and multiple fault conditions will be considered as part of future work (see Section V).

Optimization methods along with BB models (GP in [11], GA in [12], DE in [16]) can increase the accuracy of the diagnosis model by selecting gas samples that minimize the error, or resampling the data space to generate more samples. Resampling methods generate synthetic data samples by analyzing the statistical properties of the inspection data (e.g, [11], [15]). However, this process may impact the adoption of these methods because with the extra data generation process there is a risk of losing information when undersampling and overfitting when oversampling [18]. For instance, it may have been the case that during the resampling process copies of the same data point may end up both in the training and testing set. So as to avoid any type of dependencies between the training and testing datasets this work only considers inspection data.

Ensembles of classifiers have been used to avoid the potential bias and risk of errors of individual classifiers and improve the diagnostics accuracy and prediction stability [19]. Ensemble models require post-processing the outcome of the source models so as to generate a consistent prediction. However, most of the transformer classification models have been focused on single classification algorithms and there are few works focused on ensembles, such as the fusion model in [20] which combines classical Roger, Duval, Doernenburg and IEC methods through a gating network, the hybrid approach in [21] which combines fuzzy logic with ANN through Dempster Shafer's (DS) theory, the multi-ANN approach in [22] which combines ANN models through majority voting, or the sequential combination of multiple gene expression programming models through an if-else process [23].

Ensemble strategies increase the veracity of the diagnostics when independent classifiers diagnose the same fault. Classical DGA and machine learning models can be combined through different methods (e.g. majority voting, weighted average, gating networks, DS). However, there is no way to further interpret the diagnostic outcome of these methods due to lack of uncertainty information associated with their outcome. Therefore, if these methods give conflicting results, it is not clear which model is most accurate, and in this situation, the
engineer will not know which diagnostic conclusion to trust. Accordingly, due to the lack of uncertainty modelling of BB and classical DGA models, the application of ensembles in the field has been limited. This research addresses this and improves the selection of the correct diagnostic conclusion.

From an engineering viewpoint, the disagreements among independent classifiers are the most important situations that need to be resolved effectively because conflicting diagnoses may imply very different maintenance actions. Therefore, it is critical to analyse and quantify the strength of classifiers in the presence of conflicting data. Uncertainty quantification is very important for condition monitoring systems [24]. For instance, assume that a model has been trained to classify certain faults. So long as the test data is comprised of faults which are similar to the trained model, it should return a prediction with high confidence. However, if the model is tested on an unseen class of fault, the model should be able to quantify this with uncertainty levels, which can convey information about the confidence of the diagnosis of the model. This information is completely lost with BB models. Conversely, white-box (WB) models capture expert knowledge either as a causal model or through first-principle models. They generate the uncertainty associated with the decision-making process by quantifying the PDF of the likelihood of different diagnostics states. This function represents the strength of the model's diagnosis, i.e. the wider the variance, the lesser the confidence in the diagnostics outcome and vice-versa.

In this context, it is possible to combine WB and BB models to resolve conflicting samples effectively, assist the engineer in the decision-making process, and improve the diagnostics accuracy. To the best of the authors' knowledge this is the first approach which complements the accuracy of BB models with the uncertainty information of WB models for improved transformer diagnostics. Particularly for transformer DGA the use of ensembles has been limited. Therefore, the proposed approach aims to cover both gaps by proposing a novel ensemble classification framework and improving the accuracy of DGA diagnosis. The main contribution of this paper is thus the proposal of a novel probabilistic framework for uncertainty-aware fusion of classifiers to assist engineers in the decision-making process. The effectiveness of the framework is validated using publicly available datasets.

The rest of this paper is organised as follows. Section II introduces the datasets. Section III defines the proposed approach. Section IV presents results and finally, Section V draws conclusions.

## II. IntroDUCTION TO THE DGA DATASETS

The proposed approach is tested and validated using two real datasets. The IEC TC 10 is a standard benchmark dataset used to validate DGA methods [8]. It contains sets of seven different gases: ethane $\left(\mathrm{C}_{2} \mathrm{H}_{6}\right)$, ethylene $\left(\mathrm{C}_{2} \mathrm{H}_{4}\right)$, hydrogen $\left(\mathrm{H}_{2}\right)$, methane $\left(\mathrm{CH}_{4}\right)$, acetylene $\left(\mathrm{C}_{2} \mathrm{H}_{2}\right)$, carbon monoxide $(\mathrm{CO})$, and carbon dioxide $\left(\mathrm{CO}_{2}\right)$ sampled from different transformers, and labelled with their corresponding fault mode. Faults are classified into Normal degradation samples, Thermal faults $\left(\mathrm{T}<700^{\circ} \mathrm{C}\right.$ and $\mathrm{T}>700^{\circ} \mathrm{C}$ ), Arc faults (low and high energy discharges), and partial discharge (PD) faults.

In order to generate this database, faulty equipment was removed from service, visually inspected by experienced engineers, and the fault clearly identified. The dataset also contains typical normal degradation values observed in several tens of thousands of transformers. In total, the dataset is comprised of 167 samples distributed as follows: 5.3% PD failure samples, 44.4% arcing failure samples, 20.4% thermal failure samples and 29.9% normal degradation samples.

In order to further validate the method another dataset is created comprised of C2H6, C2H4, H2, CH4 and C2H2 gas samples. This dataset is created by integrating datasets presented in [8], [25] [26] [27] and it is named Extended. In total it is comprised of 302 data samples: 3.3% PD, 40.4% arcing, 33.4% thermal and 22.9% normal degradation samples.

This work focuses on unbalanced classification problems without modifying the inspection data. So as to obtain statistically significant results Monte Carlo cross-validation (MCCV) also known as repeated random subsampling is used [28].

## III. UNCERTAINTY-AWARE ENSEMBLE FRAMEWORK

The proposed framework focuses on the diagnostics of transformer faults through a supervised learning process using a dataset, $DGA$, comprised of $n$ samples,

$$DGA = \{x_i, y_i\}_{i=1}^n \tag{1}$$

where the pair $\{x_i, y_i\}$ contains the data related to the $i$-th observation, $x_i \in X$, $y_i \in Y$. The matrix $X \in \mathbb{R}^{n \times p}$ contains the information $X = \{x_1, \ldots, x_n\}$ for $p$ fault gases, and the vector $Y \in \mathbb{R}^{n \times 1}$ contains the information about the health state of the transformer. In a binary classification problem the set of possible states of $y_i$ are limited to normal and fault states. However, in this case there are multiple states and the transformer state can be classified as: normal degradation, thermal fault, arc fault, and PD. Therefore, each output $y_i$ can take the following values: $y_i = \{normal, thermal, arc, PD\}$. Multiclass classification problems are more challenging than binary classification problems, but they also generate more useful information for maintenance planning.

Fig. 1 shows the proposed generic classification framework. The ensemble classifier takes as input the deterministic probability values of each classifier ($m_{classifier}$) and the uncertainty parameters inferred from the WB model ($m_w$).

![img-0.jpeg](img-0.jpeg)

Fig. 1. Proposed uncertainty-aware ensemble diagnostics framework.

ANN and SVM models will be used as BB classification models as they have shown a high accuracy on DGA data (Table I). For WB modelling Gaussian Bayesian networks (GBNs) will be used because they are able to capture the causality among random variables and infer uncertainty information [29]. Algorithm 1 defines the implemented algorithm.

Transformer diagnostic information does not reside in absolute gas values (expressed in parts per million units, ppm) but instead in the order of magnitude. Therefore the dataset is log-normalized [9]. Firstly, the logarithm of every gas sample for all fault gases $x_i \in X$ is taken. Then each fault gas variable in the dataset is scaled to mean zero and standard deviation one. This is done for each fault gas $\{1, \ldots, p\}$ by subtracting the mean value and dividing by the standard deviation, for each sample of the fault gas variable $\{1, \ldots, n\}$ (cf. line 2).

MCCV is used for the quantification of the results [28]. For each trial $i$ (cf. line 3), the log-normalized DGA data is randomly shuffled and then it is divided into 80% and 20% for training and testing (cf. lines 4-5). Then independent classifiers and ensemble models are trained and tested (cf. lines 6-12). The classification results of each trial $i$ for each of the classifiers ($\overrightarrow{m}$) are evaluated with the accuracy metric (cf. line 14), and after repeating this process $N$ times, the accuracy statistics are quantified (cf. lines 18-19) [28]:

$$\hat{a} = \frac{1}{N} \sum_{i=1}^{N} acc_i \quad sd_{\hat{a}} = \sqrt{\frac{1}{N} \sum_{i=1}^{N} (acc_i - \hat{a})^2} \tag{2}$$

The repeated random subsampling process trains and tests $N$ times all the models ensuring the generalization of the results.

Algorithm 1 Uncertainty-aware ensemble framework
1: i=1; m_acc=$\emptyset$; $\triangleright$ initialize variables
2: norm_data=lognorm(DGA); $\triangleright$ log-normalize DGA data
3: while $i < N$ do
4: rnd_dga=shuffle(norm_data); $\triangleright$ randomize data
5: [rnd_dga_{train}, rnd_dga_{test}]=split_TrainTest(rnd_dga);
6: $m_{SVM}$=SVM(rnd_dga_{train}, rnd_dga_{test});
7: $m_{ANN}$=ANN(rnd_dga_{train}, rnd_dga_{test});
8: $PDF_BN$=GBN(rnd_dga_{train}, rnd_dga_{test});
9: $m_BN$, $m_w$]=Parameterization($PDF_BN$);
10: $m_{DS}$=DS($m_BN$, $m_{ANN}$, $m_{SVM}$);
11: $m_{St}$=Stacking($m_BN$, $m_{ANN}$, $m_{SVM}$);
12: $m_{MDS}$=MDS($m_BN$, $m_{ANN}$, $m_{SVM}$, $m_w$);
13: $\overrightarrow{m_1}$=($m_{SVM}$, $m_{ANN}$, $m_BN$, $m_{DS}$, $m_{St}$, $m_{MDS}$)
14: $\overrightarrow{acc}$=$\overrightarrow{accuracy}$($\overrightarrow{m}$) $\triangleright$ accuracy for all the models
15: $m\_acc[i,]$=$\overrightarrow{acc}$ $\triangleright$ save i-th trial accuracy results
16: $i = i + 1$ $\triangleright$ increase trial counter
17: for each $m_{classifier}$ $\in \overrightarrow{m}$ do $\triangleright$ for each classifier
18: $\hat{a_1}$=mean($m\_acc[$, $m_{classifier}$)
19: $sd_{\hat{a_1}}$=sd($m\_acc[$, $m_{classifier}$)

Firstly Algorithm 1 trains and tests independent classifiers as follows (lines 4-9):

- Line 4: for each trial $i$, the log-normalized dataset norm_data is randomly shuffled.
- Line 5: the randomly shuffled dataset rnd_dga is divided into training and testing sets.

- Lines 6-7: SVM and ANN classifiers are trained by learning their corresponding hyperparameters. Subsequently, using the test data, their diagnostics outputs are obtained in matrix form comprised of $p$ columns (one for each class) and $|\text { test }|$ rows. SVM and ANN classifiers generate a matrix ( $m_{S V M}$ and $m_{A N N}$, respectively) of deterministic probability estimates of size $|\text { test }| \times p$, where each cell specifies the diagnostics probability for each possible health state.
- Line 8: The GBN classifier is trained and tested. In the training process its hyperparameters are learned. In the testing process the PDF information is generated, $P D F_{B N}$, which includes PDFs for each health state for each test sample, i.e. a matrix of PDFs of size $|\text { test }| \times p$.
- Line 9: the uncertainty information is inferred from the $P D F_{B N}$ outcome of the GBN model resulting in the maximum likelihood value matrix, $m_{B N}$, and the matrix of the selected uncertainty metric, $m_{u}$, such as standard deviation, entropy or kurtosis.
The test matrix $\left(m_{S V M}, m_{A N N}, m_{B N}\right)$ can be directly used for diagnostics by assigning the most likely status among all possible faults. However, when the different classifiers diagnose different faults with different probabilities for the same gas samples, the decision-making process is complex. There are some direct solutions that can be applied, e.g. weight the training accuracy of the classifiers and then weight test data accordingly. This strategy assumes that the training data mirrors the test data. Therefore, the performance of this method is directly linked to the similarity of training and testing data, which impacts negatively on the generalization of the method. Algorithm 1 operates as follows with the adopted fusion strategies that are able to combine different classifiers:
- Lines 10-11: evaluate Dempster Shafer's theory and Stacking fusion strategies using the outcome of ANN and SVM models along with the maximum likelihood matrix inferred from the GBN model.
- Line 12: evaluate the modified Dempster Shafer's theory using the outcome of ANN and SVM models along with the maximum likelihood matrix inferred from the GBN model and the associated uncertainty information.
- Lines 13-16: extract and save performance metrics for the i-th trial results and prepare for the next iteration.
- Lines 17-19: extract performance statistics for all the classifiers using all the $N$ results saved in Line 15.
Subsection III-A to Subsection III-C define training and testing strategies for ANN, SVM and GBN and Subsections III-D and III-E present the fusion methods.


## A. Artificial Neural Networks

Artificial neural networks (ANN) are BB models widely used for classification and regression [30]. The multilayer perceptron (MLP) feedforward model was used in this work. The MLP is a three-layer network (input, hidden, output) comprised of fully connected neurons. Each neuron performs a weighted sum of its inputs and passes the results through an activation function. All the designed ANN models use a sigmoid activation function for hidden and output nodes.

Model training is performed using a back-propagation algorithm. The goal is to learn the neuron weights so as to generate the transformer health state (network output) from DGA values (sample input), which minimizes the error with respect to the target transformer health state. Input and hidden layers may also have a bias unit analogous to intercept terms in a regression model. As part of the MCCV process, a number of networks were trained for each trial, using different gases and their ratios at the input layer and varying the number of hidden nodes. For each trial, the experiments were repeated 10 times so as to deal with the stochastic nature of ANN models [30]. Of the trained networks for each trial, the one with the highest mean accuracy was selected. For most of the trials best results were obtained with 20 hidden nodes with the inputs in Fig. 2, i.e. $\mathrm{C}_{2} \mathrm{H}_{6}, \mathrm{C}_{2} \mathrm{H}_{4}, \mathrm{H}_{2}, \mathrm{CH}_{4}$ and $\mathrm{C}_{2} \mathrm{H}_{2}$.
![img-1.jpeg](img-1.jpeg)

Fig. 2. ANN configuration.
Fig. 2 also shows the strength of the neuron weights with a black line for higher weights and a grey line for lower weights. Model training was performed using the R nnet library [31].

## B. Support Vector Machines

The SVM maps input data into a space using a kernel function [32]. The SVM learns the boundary separating one transformer health state from another with maximum distance. The kernel function aims to translate a problem that is nonlinearly separable into a feature space, which is linearly separable by a hyperplane. The hyperplane represents the transformer health state classification boundary.

The SVM is parametrized through the choice of kernel function. For a nonlinear problem, such as the transformer health state estimation, the RBF kernel is recommended [32]: $k\left(x, x^{\prime}\right)=\exp \left(-\gamma\left\|x-x^{\prime}\right\|^{2}\right)$, where $\gamma$ is the RBF width, $x$ and $x^{\prime}$ are training and testing data samples, and $\|d\|$ is the Euclidean norm. The SVM solves an optimization problem maximizing the distance from the transformer health classification hyperplane to the nearest DGA training point. Generally the dataset is not linearly separable and slack variables are used to allow wrongly classified samples. SVM penalizes the objective function with a cost variable $c$, which is a tradeoff between penalizing slack variables and obtaining a large margin for the SVM.

Therefore the SVM training consists of calculating the hyperparameters $c$ and $\gamma$. Grid search was used to find the optimal parameters of $c$ and $\gamma$ from a grid of values. Note also that there are other optimization algorithms for parameter selection, e.g. Bayesian optimization based on Gaussian processes [33]. Namely, for each trial model training was performed using the R e1071 package [34] and grid search was used to optimize $c$ and $\gamma$ within $c=\left[2^{-10}, 2^{10}\right]$ and $\gamma=\left[2^{2}, 2^{9}\right]$. A number of configurations were trained using all different gases and their ratios as input to the SVM. Of the trained SVMs, the one with the highest accuracy from the test data was selected as the choice for that output, which matches with the input data used for the ANN model (see Fig. 2).

## C. Gaussian Bayesian Networks

Bayesian networks (BN) [29] are statistical models that represent probabilistic dependencies among random variables (RVs). In a BN model, a directed acyclic graph represents graphically the causal relation between RVs. Statistically, dependencies are quantified through conditional probabilities. BNs are a compact representation of joint probability distributions. In probability theory, the chain rule permits the calculation of any member of the joint distribution of a set of RVs using conditional probabilities. When a BN is comprised of continuous RVs a widely implemented approach adopted in this paper is the use of Gaussian BNs (GBN) [29]. In a GBN the conditional distributions are defined through linear Gaussian distributions and local distributions are modelled through Normal RVs, whose PDF is defined as:

$$
f\left(x \mid \mu, \sigma^{2}\right)=\frac{1}{\sigma \sqrt{2 \pi}} \exp \left(-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^{2}\right)
$$

where $x$ is the variable under study, i.e. transformer health state, $\mu$ is the mean, and $\sigma^{2}$ is the variance, often denoted as $x \sim N\left(\mu, \sigma^{2}\right)$.

Local distributions are linked through linear models in which the parents, i.e. DGA samples, play the role of explanatory variables. Each node $x_{i}$ which represents one specific health state of the transformer is regressed over its parent nodes which are explanatory DGA samples. Assuming that the parents of $x_{i}$ are $\left\{u_{1}, \ldots, u_{k}\right\}$, then the conditional probability of each node can be expressed as $p\left(x_{i} \mid u_{1}, \ldots, u_{k}\right) \sim N\left(\beta_{0}+\right.$ $\left.\beta_{1} u_{1}+\ldots+\beta_{k} u_{k} ; \sigma^{2}\right)$, that is:

$$
p\left(x_{i} \mid u_{1}, \ldots, u_{k}\right)=\frac{1}{\sigma \sqrt{2 \pi}} \exp \left(-\frac{1}{2}\left(\frac{x-\left(\beta_{0}+\beta_{1} u_{1}+\ldots+\beta_{k} u_{k}\right)}{\sigma}\right)^{2}\right)
$$

where $\beta_{0}$ is the intercept and $\left\{\beta_{1}, \ldots, \beta_{k}\right\}$ are linear regression coefficients for the parent nodes $\left\{u_{1}, \ldots u_{k}\right\}$.

So as to select the input gas variables the Normality of the fault gases was analysed and those gases which follow a Normal distribution were selected so as to match with the underlying probabilistic model and maximize the inferred information. Fig. 3 shows the GBN model comprised of nodes and arrows, where the origin of the arrow is the parent node and the destination is its child node, e.g. the parent nodes of PD are $\mathrm{C}_{2} \mathrm{H}_{6}, \mathrm{C}_{2} \mathrm{H}_{2}, \mathrm{CH}_{4}, \mathrm{C}_{2} \mathrm{H}_{4}$ and $\mathrm{H}_{2}$.
![img-2.jpeg](img-2.jpeg)

Fig. 3. GBN configuration.

The parameter estimation for GBN models is based on the maximum likelihood (ML) algorithm. The ML expression is derived from the linear Gaussian density function and the closed-form solution can be obtained (see [29] for more details). This process is used to estimate the parameters for each node in the BN model, e.g. for the PD node (Fig. 3): $P\left(P D \mid C_{2} H_{6}, C_{2} H_{2}, C H_{4}, C_{2} H_{4}, H_{2}\right) \sim \mathcal{N}\left(\beta_{0}+\beta_{1} C_{2} H_{6}+\right.$ $\left.\beta_{2} C_{2} H_{2}+\beta_{3} C H_{4}+\beta_{4} C_{2} H_{4}+\beta_{5} H_{2} ; \sigma^{2}\right)$.
After learning the parameters, the estimation of the conditional probability of nodes, i.e. probability of a specific transformer health state given input DGA data, is based on inferences using the likelihood weighting algorithm [29]. When applied to the DGA dataset, for each of the analyzed transformer health state the outcome of the inference is a set of random samples from the conditional distribution of the transformer health state node given the test DGA samples. From the random samples density values are calculated through Kernel density estimates [35]. The GBN model was implemented using the bnlearn R package [36].

## D. Ensemble of diagnostics models

Research suggests that combining multiple classifiers can improve individual classifiers [19]. There are a number of different methods for creating ensembles.

1) Dempster Shafer's (DS) theory: DS builds beliefs of the true state of a process from distinct pieces of evidence [21]. Assuming a set of faults $\mathcal{F}$, where the i-th fault is denoted $f_{i}$, the set of possible states is called frame of discernment: $\mathcal{F}=\left\{f_{1}, \ldots, f_{i}, \ldots, f_{\mid F \mid}\right\}$. Pieces of evidence are formulated as mass functions, $m: 2^{\mathcal{F}} \longmapsto \mathbb{R}$, satisfying: $m\left(f_{i}\right) \geq 0$, $m(\emptyset)=0$, and $\sum_{f_{i} \subseteq \mathcal{F}} m\left(f_{i}\right)=1$.
The combined probability mass for the i-th fault, $f_{i}$, of two classifiers, denoted $c_{1}$ and $c_{2}$, is defined as

$$
m_{c_{1} c_{2}}\left(f_{i}\right)=\frac{1}{1-K} \sum_{\substack{A, B \subseteq \mathcal{F} \\ A \cap B=f_{i}}} m_{c_{1}}(A) m_{c_{2}}(B)
$$

$\forall f_{i} \subseteq \mathcal{F}, f_{i} \neq \emptyset$, where $K$ is the degree of conflict between two mass functions:

$$
K=\sum_{\substack{A, B \subseteq \mathcal{F} \\ A \cap B=\emptyset}} m_{c_{1}}(A) m_{c_{2}}(B)
$$

DS theory has been successfully applied to combine independent classifiers (Section I). However, one of its criticisms is the inability to handle some conflicting situations [21].

2) Stacking: The stacking method is based on the metalearner concept in which a stacking model learns which classifiers are reliable and which are not [19]. Instead of taking the original input variables, a stacked model takes as input the probabilistic outcomes generated from all the independent classifiers. These models are trained first and then tested with both training and testing data. The training and testing of a stacked model is based on the training and testing outcomes of the independent classifiers. Fig. 4 shows the stacking concept.
![img-3.jpeg](img-3.jpeg)

Fig. 4. Stacking configuration.
ANN and SVM models generate a deterministic probability value for each health state. The GBN model generates a PDF for each health state, and the maximum likelihood of each PDF is used in the stacking configuration.

As opposed to DS theory, in the stacking configuration a learning model is trained. An ANN model has been used in this work as a stacking model to aggregate independent classifiers. As part of the MCCV process, for each trial, a number of stacking models are trained varying the number of hidden nodes to select the one with the best performance. In most of the cases the best ANN model is comprised of 10 hidden nodes. The activation function is the sigmoid function.

## E. Reasoning under uncertainty with ensemble models

The methods outlined in Subsection III-D have been used for the fusion of black-box classifiers. However, they ignore any uncertainty information which may be generated by the classifiers. There is potential for this information to improve the performance of the ensemble, especially on conflicting samples.

Fixsen and Mahlen proposed the Modified DS (MDS) framework by merging DS theory and Bayesian approaches [37]. In this work the MDS framework is adapted for the particular case of evidence combination of different faults to integrate the uncertainty information generated by WB probabilistic classifiers.

Namely, assuming a set of faults $\mathcal{F}$ with a prior probability $\pi_{i}$ for each fault $(1 \leq i \leq|\mathcal{F}|)$, the fusion of different classifiers for each fault taking into account the prior information is calculated as follows:

$$
m_{c_{1} c_{2}}\left(f_{i} \mid \vec{\pi}\right)=\frac{m_{c_{1}}\left(f_{i}\right) \cdot m_{c_{2}}\left(f_{i}\right) \cdot \prod_{j=1}^{|\mathcal{F}| \backslash f_{i}} \pi_{j}}{\sum_{k=1}^{|\mathcal{F}|}\left(m_{c_{1}}\left(f_{k}\right) \cdot m_{c_{2}}\left(f_{k}\right) \prod_{l=1}^{|\mathcal{F}| \backslash f_{k}} \pi_{l}\right)}
$$

where $|\mathcal{F}|$ is the cardinality of the set of faults and $\vec{\pi}$ is the set of priors for each fault $\vec{\pi}=\left\{\pi_{1}, \pi_{2}, \ldots, \pi_{|F|}\right\}$.

The strength of the proposed reasoning framework is highlighted with conflicting data samples which are incorrectly
classified by independent classifiers. In this situation, the prior information is critical to weight the probabilities and decide which is the real cause of the fault. For example, for two faults $f_{1}$ and $f_{2}$, and two classifiers $c_{1}$ and $c_{2}$, (7) reduces to

$$
m_{c_{1} c_{2}}\left(f_{1} \mid \vec{\pi}\right)=\frac{m_{c_{1}}\left(f_{1}\right) \cdot m_{c_{2}}\left(f_{1}\right) \cdot \pi_{f_{2}}}{m_{c_{1}}\left(f_{1}\right) \cdot m_{c_{2}}\left(f_{1}\right) \pi_{f_{2}}+m_{c_{1}}\left(f_{2}\right) \cdot m_{c_{2}}\left(f_{2}\right) \pi_{f_{1}}}
$$

In the extreme case that both classifiers give the same probabilistic output for both faults, (8) reduces to

$$
m_{c_{1} c_{2}}\left(f_{1} \mid \vec{\pi}\right)=\frac{1}{1+\pi_{f_{1}} / \pi_{f_{2}}}
$$

From (9) one can observe that the probability mass of fault $f_{1}$ is dependent on the ratio between $\pi_{f_{2}}$ and $\pi_{f_{1}}$. Namely, the greater the uncertainty of $f_{2}$ with respect to $f_{1}$, the greater the assigned probability mass to $f_{1}$ and the lower the assigned probability mass to $f_{2}$. Usually the probability mass values of different faults and different classifiers are not equal, but the same reasoning process is generally applicable for all cases to reason under uncertainty. Therefore (7) creates a suitable framework to integrate uncertainty information in the ensemble of diagnostics classifiers.

The key assumption of this method is that the fusion method accepts a common prior for different mass values. That is, the uncertainty information inferred from a single classification method will be used to influence the combination of different classifiers. Therefore, the generation of representative uncertainty information will be critical. In the set of classifiers analyzed in this work, only the GBN model is able to generate uncertainty information from the classification output. Therefore, uncertainty parameters will be extracted from the density functions inferred by the GBN model so as to reason under uncertainty.

1) Uncertainty parameters: There are different metrics that can be used in order to extract uncertainty information from density functions such as standard deviation, kurtosis or entropy. Depending on the metric, the effect of the prior on the final accuracy is different. Best results were obtained with the standard deviation and weighted log-likelihood, wll, defined as follows:

$$
w l l=-\frac{1}{M} \sum_{i=1}^{M}\left(w_{i} \cdot p_{i}+\log \left(w_{i} \cdot p_{i}\right)\right)
$$

where $M$ denotes the total number of Kernel density samples, $p_{i}$ is the diagnosis probability of the fault $i$, and $w_{i}$ is the weight assigned to this probability.

## IV. CASE STUDIES

The proposed approach is tested on the datasets introduced in Section II. So as to validate and generalize the result all the models and ensemble strategies have been examined $\mathrm{N}=10^{3}$ times using the MCCV strategy. For each trial, firstly the dataset is shuffled, then it is divided into training and testing sets, and finally training and testing steps are completed. After randomly shuffling the dataset, different training and testing data proportions and data split strategies have been tested (cf. Algorithm 1, line 5):

- $80 \%-20 \%$ global: all the dataset is divided into $80 \%$ and $20 \%$ for training and testing, respectively. In the testing set there is always at least one sample of each state.
- $80 \%-20 \%$ class-by-class: each health state is divided into $80 \%$ and $20 \%$ for training and testing, respectively.
- $70 \%-30 \%$ class-by-class: each health state is divided into $70 \%$ and $30 \%$ for training and testing, respectively.
The $80 \%-20 \%$ global strategy reflects closely the real transformer operation. However, this strategy affects the number of samples for each health state in the testing set. The class-byclass strategies ensure the same amount of randomly sampled data samples per each group for each trial.

Generally there are four possible outcomes for a classifier. True positive (TP) when there is a fault and it is correctly diagnosed, false positive (FP) when there is no fault, but the classifier diagnoses a fault, true negative (TN) when there is no fault and the classifier does not diagnose any fault, and false negative ( FN ) when there is a fault and it is not correctly diagnosed. In addition to the accuracy indicator (cf. Algorithm 1, line 14), which quantifies the percentage of correct predictions over the total number of predictions, four complementary classification metrics have been analysed.

- Positive preditive value (PPV): $P P V=\frac{T P}{T P+F P}$
- Negative preditive value (NPV): $N P V=\frac{P N}{T N+F N}$
- False Positive rate (FPR): $F P R=\frac{F P}{F P+T N}$
- F1 score (F1): $F 1=\frac{2 T P}{2 T P+F P+F N}$

PPV and NPV quantify respectively the proportions of positive and negative results in diagnostics tests. PPV is different from accuracy because it considers only TP and FP events. The PPV is also known as precision and its complement is the false discovery rate. The complement of the NPV is the false omission rate. The complement of the FPR is the specificity. The F1 score is the harmonic mean of PPV and recall, which is commonly used for unbalanced classification problems.

For multiclass classification problems, the classifier outcomes and metrics are counted per class, and then they are averaged according to the prevalence of each class.

A number of independent classifiers and ensemble strategies have been examined:
\#1 Gaussian Bayesian Networks.
\#2 Support Vector Machines.
\#3 Artificial Neural Networks.
\#4 Stacking with ANN, SVM and GBN models aggregated with an ANN model.
\#5 Dempster-Shafer with ANN, SVM, and GBN models.
\#6 Modified DS with ANN, SVM, and GBN models using the standard deviation of GBN results as a prior.
\#7 Modified DS with ANN, SVM, and GBN models using the weighted log-likelihood of GBN results as a prior.

## A. Results \& Discussion

The accuracy results for the IEC TC 10 and Extended datasets are displayed in Table II. The best performing results with highest mean accuracy and lowest deviation are highlighted in bold.

Table II confirms that the overall accuracy of the proposed novel configurations (\#6, \#7) are higher than other fusion (\#4,
\#5) and machine learning methods (\#1-\#3) for both datasets. The order of the accuracy improvement of the proposed configurations with respect to other fusion and machine learning methods remains the same for both datasets, which confirms the validity and consistency of the proposed approach.

As for the data training and testing strategies, it is possible to see that the accuracy decreases for all the configurations across both datasets when decreasing the size of the training set from $80 \%$ to $70 \%$. Additionally, the class-by-class strategy reduces the standard deviation (SD) of the results by imposing a predefined number of samples in the testing set. For PD samples the SD is bigger compared with the rest of the states because the accuracy values for most of the trials are concentrated at one value with few outliers.

As for the comparison between datasets, in general the overall accuracy improves with the Extended dataset. This is due to an improved capability to detect Thermal and Arc faults, purely because the training dataset contains more examples of these fault types. Conversely, the accuracy of PD faults decreases with the Extended dataset. The trend of the PD samples on the IEC TC 10 dataset is predictable $\left(\mathrm{H}_{2} \simeq[10000-80000], \mathrm{CH}_{4} \simeq[1000-18000], \mathrm{C}_{2} \mathrm{H}_{6} \simeq[100-2000]\right.$, $\mathrm{C}_{2} \mathrm{H}_{2} \simeq[1-25], \mathrm{C}_{2} \mathrm{H}_{4} \simeq[1-25]$, all in ppm). However, with the Extended dataset the PD is more complex to diagnose due to the introduced additional data samples for all fault types. For instance, another PD sample is added $\left(\mathrm{H}_{2}=980, \mathrm{CH}_{4}=73\right.$, $\mathrm{C}_{2} \mathrm{H}_{6}=58, \mathrm{C}_{2} \mathrm{H}_{2}=0.1, \mathrm{C}_{2} \mathrm{H}_{4}=1.2$, all in ppm) [27], which is more complex to diagnose and therefore, the PD accuracy decreases.

As for the diagnostics capacity of specific models, it can be seen that the GBN has a good performance for identifying PD faults. Then, the classification outputs of the GBN model also have less uncertainty for this fault, which in turn leads to improving the ensemble models when including the prior, e.g. see PD diagnostics accuracy for the IEC TC 10 dataset. The improvements for Arc, Normal, and Thermal faults are similar for all the fusion methods, with slight improvements when including the uncertainty information in the ensemble.

For the Extended dataset the GBN model has a decreased accuracy for the Normal state. This affects the fusion strategies as the prior becomes less informative and the accuracy of the proposed fusion strategies for the Normal state becomes less accurate. In contrast, the GBN model has an increased accuracy for the Thermal state for the same dataset. In this case, this benefits the fusion strategies because the prior becomes more informative and the accuracy of the proposed fusion strategy for Thermal faults becomes more accurate.

Table III displays more performance metrics. For the overall metrics, the best models in terms of F1, PPV, NPV and FPR are the proposed fusion strategy results \#6 and \#7.

The PPV improvement of the proposed strategy results are in the same order of improvement as the accuracy results. The only difference with respect to the accuracy results in Table II is the increased percentage value of PPV results due to the definition of PPV, i.e. it only considers TP and FP events and no FN events. The NPV is very high for all the tested configurations. That is, these models are able to correctly detect when a fault class has not occurred. The FPR

TABLE II
CLASSIFICATION ACCURACY OF INDEPENDENT \& ENSEMBLE MODELS.


*A: IEC TC 10 dataset, B: Extended dataset. \#1: GBN, \#2: SVM, \#3: ANN, \#4: Stacking, \#5: DS, \#6: MDS with SD, \#7: MDS with WLL.

TABLE III
PERFORMANCE METRICS OF INDEPENDENT \& ENSEMBLE MODELS.


*A: IEC TC 10 dataset, B: Extended dataset. \#1: GBN, \#2: SVM, \#3: ANN, \#4: Stacking, \#5: DS, \#6: MDS with SD, \#7: MDS with WLL.
improvement of the proposed strategy is in the same order of improvement as the accuracy results. This is caused by the reduced number of FP events and increased number of TN events as confirmed by the NPV results. Finally, the F1 score is very similar to the accuracy results both in the order of improvement and absolute values. The F1 score is a combined metric of precision and recall and therefore it includes the number of correctly classified instances as well as FP and FN events.

As for the effect of different training and testing strategies on the performance results, the class-by-class strategy reduces the SD of the results as happened with the accuracy results in Table II. Concerning the effect of the size of the dataset, a decrease in the training set causes a decrease of F1 and PPV scores and an increase of the FPR score indicating a decreased accuracy and an increased false positive rate respectively, while the NPV score remains high for all the configurations. Finally, with respect to the performance comparison across datasets, the results are again consistent with the accuracy
results in Table II. That is, F1, PPV and NPV scores increase and FPR decreases with the Extended dataset due to the extended number of samples per health state.

Tables II and III agree that the accuracy and the performance of the proposed fusion strategies (\#6, \#7) are superior to other machine learning (\#1-\#3) and fusion (\#4, \#5) models. The main factor which makes a difference among these models is the post-processing and integration of the uncertainty information in the ensemble of classifiers. This is dependent on the used WB approach and the post-processed uncertainty information in the form of uncertainty metrics. These metrics along with the combination of machine learning methods enable the resolution of conflicting samples. As demonstrated in the next section, the order of improvement of the proposed method with respect to existing fusion methods is correlated with the amount of conflicting diagnostics samples. That is, the more conflicting samples the better the accuracy and performance of the proposed approach.

## B. Decision Making Under Uncertainty

From an engineering viewpoint the data samples which create disagreement among the source classifiers are the most important cases. Table IV displays the accuracy results considering only conflictive samples, i.e. data samples which create disagreements among GBN, ANN and SVM models.

TABLE IV
CLASSIFICATION ACCURACY FOR CONFLICTIVE DATA SAMPLES.


Results in Table IV are in agreement with the results in Table II. However, the overall accuracy is lower because consistently diagnosed data samples are removed, and the differences in the accuracy of the fusion methods are higher because only conflictive cases are taken into account. Under conflicting situations, the proposed uncertainty-aware fusion strategy is more effective due to the accuracy improvements for all health states (cf. Table II). This accuracy is a critical value for any ensemble approach because the strength of the method is highlighted when independent classifiers diagnose different faults and it is able to reason under uncertainty.

The proposed model is able to assist the engineer in the decision-making process. For instance, consider that after training the classifiers they are tested for the following absolute gas values [8]: $\mathrm{H}_{2}=26788 \mathrm{ppm}, \mathrm{C}_{2} \mathrm{H}_{4}=27 \mathrm{ppm}, \mathrm{C}_{2} \mathrm{H}_{6}=2111$ $\mathrm{ppm}, \mathrm{C}_{2} \mathrm{H}_{2}=1 \mathrm{ppm}, \mathrm{CH}_{4}=18342 \mathrm{ppm}$ and the observed fault type is PD. Table V displays probabilistic results for different classifiers, $m_{\text {classifiers }}$.

TABLE V
EXAMPLE A: DIAGNOSTICS RESULTS OF SOURCE CLASSIFIERS.


The results of the independent classifiers highlight their disagreement. BB models do not generate uncertainty information, but observing the output of the GBN the PDFs for different faults and the associated uncertainty can be inferred. Fig. 5 shows the GBN's output for the considered example. That is, ID \#1 in Table V without normalising probabilities.

The x -axis in Fig. 5 denotes random samples drawn from the conditional distribution of the node given the evidence, $P\left(f_{i} \mid C_{2} H_{6}, C_{2} H_{4}, H_{2}, C H_{4}, C_{2} H_{2}\right)$. The x -axis value of the peak density indicates the maximum likelihood value. The greater the peak density value, the narrower the variance, and the higher the confidence of the GBN model in the diagnostics.

For instance, the density function of the PD fault shows a narrow function with a high peak density value with a maximum likelihood value located at 0.7 . This suggests that GBN is very confident that PD is the type of fault present for these test gas values. Thermal fault has a maximum likelihood
value of 0.65 , but its standard deviation is greater than the PD fault, which indicates the decreased confidence of the GBN that this is the true fault. The density functions for the rest of faults located at lower x -axis probability values, indicate that they are not the cause of this fault.
![img-4.jpeg](img-4.jpeg)

Fig. 5. Example A: GBN diagnostics output.
It is possible to evaluate different uncertainty metrics in Fig. 5 and use them as priors in (7) so as to influence the fusion strategy. Using the standard deviation [Eq. (2)] and weighted log-likelihood [Eq. (10)] as the prior, Table VI displays the results of the analyzed ensemble strategies.

TABLE VI
EXAMPLE A: DIAGNOSTICS RESULTS OF ENSEMBLE MODELS.


The fusion methods stacking and DS (\#4, \#5 Table VI) do not identify the actual fault. However, the proposed approach (\#6, \#7) which uses the uncertainty information inferred from the GBN model is effective in resolving conflictive samples.

The crucial point of this method is the accuracy of the WB model and conflictive cases. The GBN model has a good performance for identifying PD faults. Therefore, this leads to improving the ensemble models when including the prior, because the uncertainty associated with the PD fault is lower. However, note also that the deterministic probability values of different classifiers count in the ensemble [cf. Eq. (7)], and therefore, the fusion is not biased by the potential poor performance of the GBN model. For instance, the GBN performs worse than ANN or SVM for Normal and Thermal faults, but the ensemble strategy improves the final accuracy.

In another test, the classifiers are tested for the following absolute gas values [8]: $\mathrm{H}_{2}=290 \mathrm{ppm}, \mathrm{CH}_{4}=966 \mathrm{ppm}$, $\mathrm{C}_{2} \mathrm{H}_{2}=57 \mathrm{ppm}, \mathrm{C}_{2} \mathrm{H}_{4}=1810 \mathrm{ppm}, \mathrm{C}_{2} \mathrm{H}_{6}=299 \mathrm{ppm}$ and the observed fault type is a Thermal fault. Table VII displays the classification results for different source classifiers.

In this case all the classifiers consistently diagnose a normally degrading transformer. Examining the output of the GBN model in Fig. 6 (i.e. \#1 in Table VII, normalised), it is possible to see the uncertainty information of the diagnosis.

TABLE VII
EXAMPLE B: DIAGNOSTICS RESULTS OF SOURCE CLASSIFIERS.


![img-5.jpeg](img-5.jpeg)

Fig. 6. Example B: GBN diagnostics output.

Although the Normal fault has the highest maximum likelihood value among all faults, the GBN's diagnostics for the Thermal fault has higher confidence with a slightly lower maximum likelihood value. Using the uncertainty information of the GBN model, Table VIII displays the fusion results.

TABLE VIII
EXAMPLE B: DIAGNOSTICS RESULTS OF ENSEMBLE MODELS.


Stacking and DS (\#4, \#5 in Table VIII) do not identify the actual fault. However, the proposed fusion strategy (\#6, \#7 in Table VIII) again is effective in resolving conflictive samples.

Consider the classifiers are tested for the following values [8]: $\mathrm{H}_{2}=250 \mathrm{ppm}, \mathrm{CH}_{4}=150 \mathrm{ppm}, \mathrm{C}_{2} \mathrm{H}_{2}=150 \mathrm{ppm}, \mathrm{C}_{2} \mathrm{H}_{4}$ $=150 \mathrm{ppm}, \mathrm{C}_{2} \mathrm{H}_{6}=250 \mathrm{ppm}$ and the observed health state is Normal. Table IX displays the classification results for the source classifiers.

TABLE IX
EXAMPLE C: DIAGNOSTICS RESULTS OF SOURCE CLASSIFIERS.


GBN and ANN diagnose an Arc fault (\#1, \#3 in Table IX), while SVM diagnoses a Normal transformer (\#2 in Table IX). Uncertainty information of the GBN's diagnosis is inferred from the GBN output in Fig. 7 (\#1 in Table IX, normalised).

The Arc fault has the highest maximum likelihood value and the Normal state has slightly higher confidence with a slightly lower maximum likelihood value. Using the uncertainty information of the GBN model, Table X displays fusion results.
![img-6.jpeg](img-6.jpeg)

Fig. 7. Example C: GBN diagnostics output.

TABLE X
EXAMPLE C: DIAGNOSTICS RESULTS OF ENSEMBLE MODELS.


The proposed fusion strategy effectively diagnoses the Normal state and this justifies why despite the accuracy of the GBN being lower, the fusion improves the final diagnosis accuracy (Table II). Note that the GBN diagnosis results in Figs. 5-7 show the non-normalized probabilities corresponding to different Monte Carlo trials and this results in different SD values.

Accordingly, results in Table IV report the accuracy of the ensemble taking into account only conflictive diagnostics of source classifiers and the presented examples focus on conflicts among the source classifiers. These examples can be individually analysed with classical DGA methods. For instance, in Fig. 5 the Duval's triangle correctly identifies a PD fault, Roger indicates normal degradation and Doernenburg does not give a diagnostics or in Fig. 7, the Duval's triangle incorrectly identifies an Arc fault, and Roger and Doernenburg do not give a diagnostics. Even if there is a correct diagnostics by some of the classical methods, their overall diagnostics accuracy is lower. There are other cases where classical methods do not diagnose the correct fault and all the analysed models consistently diagnose the correct fault and this causes the difference in the overall accuracy. Additionally, note that the classical methods are not probabilistic models [7], which makes it difficult to solve conflicts (see Subsection IV-C).

Note also that the density functions generated by the GBN model (e.g., Figs 5-7) do not only help to improve the accuracy of the ensemble, but they also represent a more intuitive visualization for understanding the conflicts. This representation should help to increase the trust of the engineer in the technique as opposed to deterministic probability values inferred from black-box models.

## C. Comparison to other methods

The results obtained by the proposed fusion framework are better than other models tested in the same conditions (in this paper) and very close to results obtained with the same dataset but tested in different conditions (reported in the literature). This demonstrates that despite the challenging conditions (multiclass, imbalanced inspection data), the performance is comparable to binary classifiers and to the techniques which use resampling methods (see Table I).

Results displayed in Table II confirm that the proposed fusion strategy improves the accuracy compared with other fusion methods (Dempster Shafer, Stacking) and classifiers (ANN, GBN, SVM). Table XI displays the accuracy of the classical methods using the $80 \%-20 \%$ global sampling strategy. There is no need to train classical models, but for direct comparisons with Table II, the same testing data samples have been used for machine learning and classical methods.

TABLE XI
COMPARISON WITH CLASSICAL METHODS.


The overall accuracy results of the proposed approach (cf. Table II) are better compared with the classical methods for both datasets. This is mainly caused by the detection of normally degrading transformers. Duval has an excellent accuracy for PD and Arc faults tested on the IEC TC 10 dataset. However, the overall accuracy is negatively affected because it is not able to diagnose normally degrading transformers. When testing the Extended dataset, the accuracy of the Duval's triangle for PD and Arc faults decreases and for the Thermal fault increases. This occurs because the boundaries between diagnostic regions of the triangle are fixed, as opposed to statistical learning strategies which can adapt to training data. The performance of Rogers and Doernenburg models is lower for both datasets compared with the Duval's triangle.

## V. CONCLUSIONS

Transformers are key assets for the reliable and costeffective operation of the power grid and DGA is an industryaccepted standard method used to monitor transformers. However, the use of classical DGA models or black-box classifiers may generate conflicting diagnostics outputs which are difficult to resolve due to the lack of uncertainty information generated by these models. This situation complicates the decision-making process for engineers.

In order to increase the confidence of the engineer in the decision-making process this paper presents a novel method which takes into account uncertainty information when integrating the output of different classifiers. Using the proposed method for DGA, the accuracy with respect to other fusion methods has improved and the model shows that it is effective
for correcting conflictive samples when the prior information inferred from probability density functions is informative.

The results obtained in this paper can be used as a benchmark to other techniques because the used datasets are publicly available. So as to extract general accuracy statistics the models were cross-validated using Monte Carlo cross validation and different proportions and sampling strategies for dividing training and testing strategies have been tested.

Future work can address the integration of other white-box methods or the extension of the approach to combine prior information from multiple sources. This extension may be able to create a more informative prior distribution by combining, e.g. uncertainty information with different fault gas indicators. Ultimately, this enhanced model may open the way for the identification of multiple simultaneous fault conditions.
