# Article 

## A Comparison of Machine-Learning Methods to Select Socioeconomic Indicators in Cultural Landscapes

Ana D. Maldonado ${ }^{1,1}$ (D)D, Darío Ramos-López ${ }^{2,1}$ (D) and Pedro A. Aguilera ${ }^{1, *, 1}{ }^{(D)}$<br>1 Department of Biology and Geology, University of Almería, 04120 Almería, Spain; ana.d.maldonado@ual.es<br>2 Department of Applied Mathematics, Rey Juan Carlos University, 28933 Madrid, Spain; dario.ramos.lopez@urjc.es<br>* Correspondence: aguilera@ual.es; Tel.: +34-950-015933<br>$\dagger$ These authors contributed equally to this work.

Received: 31 October 2018; Accepted: 15 November 2018; Published: 21 November 2018
check for
updates


#### Abstract

Cultural landscapes are regarded to be complex socioecological systems that originated as a result of the interaction between humanity and nature across time. Cultural landscapes present complex-system properties, including nonlinear dynamics among their components. There is a close relationship between socioeconomy and landscape in cultural landscapes, so that changes in the socioeconomic dynamic have an effect on the structure and functionality of the landscape. Several numerical analyses have been carried out to study this relationship, with linear regression models being widely used. However, cultural landscapes comprise a considerable amount of elements and processes, whose interactions might not be properly captured by a linear model. In recent years, machine-learning techniques have increasingly been applied to the field of ecology to solve regression tasks. These techniques provide sound methods and algorithms for dealing with complex systems under uncertainty. The term 'machine learning' includes a wide variety of methods to learn models from data. In this paper, we study the relationship between socioeconomy and cultural landscape (in Andalusia, Spain) at two different spatial scales aiming at comparing different regression models from a predictive-accuracy point of view, including model trees and neural or Bayesian networks.


Keywords: cultural landscapes; socioeconomic indicators; multiple linear regression; model trees; neural networks; probabilistic graphical models

## 1. Introduction

Cultural landscapes are the result of the slow coevolution between human activity and the environment [1], which integrates ecological, socioeconomic, and cultural needs. The dehesa agroforestry in the Iberian Peninsula is a well-known example of a cultural landscape [2]. As a result of the long-lasting human activity on Earth, landscapes have been shaped with different degrees of human influence [2]. Cultural landscapes are rarely uniform or monotonous [3]. On the contrary, they are composed of a mosaic of patches with different ecological maturity, providing a broad spectrum of ecosystem services that can be modified through abandonment or intensification processes, both mainly related with socioeconomic changes [4]. Therefore, socioeconomic variables can be considered as drivers of landscape change. In this sense, it is necessary to select the variables that play a role as indicators.

Cultural landscapes can be understood as complex adaptive socioecological systems [5-7], having properties common to complex systems [8]: cross-scale linkages, emergence, heterogeneity, nonlinear dynamics, system memory, and prediction uncertainty. The management of cultural landscapes requires interventions that take into account heterogeneity at multiple scales to support resilience and adaptive capacity. This approach involves observation and monitoring of the

socioecological system, and the use of predictive decision support tools that consider future uncertainty $[8,9]$.

Numerical analyses have been applied to study the relationships between socioeconomic structure and landscape in different cultural landscapes from a socioecological perspective, with linear regression being frequently found in the literature [3,5,10,11]. Due to the nonlinear dynamics that complex systems show, alternative methods have been receiving growing attention in recent years [12]. In particular, the machine-learning field has been gaining popularity among the environmental modelers due to the development of sound methods and algorithms able to deal with complex systems without making assumptions of linearity.

Machine-learning [13,14] techniques are now fundamental tools in many research areas. This field comprises a large amount of mathematical and statistical methods that have proven to be useful in a vast number of applications, such as animal behavior [15], biological invasions [16], species distribution [17-19], food webs [20,21], ecosystem services [4,22], air pollution [23-25], groundwater pollution [26-28], surfacewater pollution [29-31], or land-cover classification [32-34]. The research in these topics has become highly active in the few last years. An especially important part of the machine-learning field is so-called deep learning [35], with neural networks being its most relevant tool [36,37]. Deep-learning models can be very complex, combining multiple variables along the multiple levels of their hidden layers in an extremely nonlinear way [38]. Models built with deep-learning techniques generally have outstanding predictive capacity in practice [39], being able to learn extremely complex patterns in the data, which has favored their tremendous popularity in specific applications [40-42].

Another relevant area is probabilistic machine learning [13,14,43,44], in which probabilistic graphic models (PGMs) [44] play a relevant role. They allow the integration of expert knowledge in the design and improvement of models [45,46]. An essential difference between deep learning and probabilistic machine learning is the number of parameters in their models, which is generally much smaller in the case of the latter [47]. This means that probabilistic machine-learning models can often be adjusted sufficiently well with a small amount of data, as opposed to deep-learning models. Other advantages are their flexibility, allowing the inclusion of missing data, or their robustness when using noisy data. Moreover, PGMs are naturally "open-box" models, with the possibility of interpreting their structure and parameters in a relatively simple way, which is barely possible in deep-learning models. PGMs also incorporate probabilistic reasoning and Bayesian statistics in a natural way [46,48,49], which equips them with a high capacity to easily model uncertainty.

The purpose of this work is to make a comparative analysis of various machine-learning techniques in order to select socioeconomic indicators of cultural landscapes. In particular, this work focuses on cultural landscapes in Andalusia (Spain), which are represented as the percentage of heterogeneous lands, i.e., pieces of land mixing grassland with forest and crops with natural vegetation. The remainder of the paper is organized as follows: Section 2 describes the study area, the variables considered to build the models, the methods applied to analyze the data, the variable selection procedure, and the model validation method followed. The performance of the models is analyzed in Section 3. The paper ends with the discussion in Section 4.

# 2. Methodology 

### 2.1. Study Area

The study focuses on the cultural landscapes of Andalusia, a region in southern Spain that occupies an area of $87,000 \mathrm{~km}^{2}$, and whose latitude and longitude are between $36^{\circ} \mathrm{N}-38^{\circ} 44^{\prime} \mathrm{N}$ and $3^{\circ} 50^{\prime} \mathrm{W}-0^{\circ} 34^{\prime}$ E. The cultural landscapes of Andalusia are mainly located in the Baetic system and the Sierra Morena mountain range. The Sierra Morena mountain range is characterized by having a high emigration rate, low birth rate, and high death rate; it is mainly covered by rainfed crops and dehesa [50], a heterogeneous system containing different states of ecological maturity, with shepherding

being the principal economic activity. The Baetic System has the highest elevation and steepness in the study area and is mainly covered by natural vegetation and, secondarily, by extensive woody crops. Its inaccessibility discourages the introduction of intensive agricultural practices.

# 2.2. Data Description 

Variables describing the social and economic characteristics of the study area, as well as the percentage of heterogeneous lands, were incorporated into a geographic information system, ArcGIS (ESRI ${ }^{\circledR}$ ArcMap ${ }^{\mathrm{TM}} 10.2 .2$ ). Social and economic descriptors were provided by the Multiterritorial Information System of Andalusia (SIMA) (http://www.juntadeandalucia.es/ institutodeestadisticaycartografia/sima/) at the municipality scale, whereas land-use information was collected from the Andalusian Environmental Information Network (http://www.juntadeandalucia. es/medioambiente/site/rediam) in the vectorial shapefile format. The co-ordinate system of the ecological information is based on the European Terrestrial Reference System 1989 (ETRS89).

Two different scales were used as the unit of analysis: (1) the municipality and (2) a $5 \times 5 \mathrm{~km}$ grid (Figure 1). The first dataset is composed of 603 polygons corresponding to partial or complete municipalities (some municipalities are composed of spatially disconnected polygons, i.e., their area is split into separate polygons) located in the Sierra Morena mountain range or the Baetic System. Only a polygon with at least $50 \%$ of its area falling in these regions were included in the dataset. On the other hand, a $5 \times 5 \mathrm{~km}$ grid was used to calculate the value of each variable within each cell. Those cells occupied by less than $50 \%$ of cultural landscapes were removed, obtaining a dataset of 2433 records. Finally, 24 variables evaluated over each record of both datasets were considered to build the models (Table 1).
![img-0.jpeg](img-0.jpeg)

Figure 1. The region of Andalusia divided into its four main geomorphological units (a). Study area is focused on the cultural landscapes of Andalusia, which are mainly located in the Baetic System and the Sierra Morena mountain range. (b,c) Units of analysis: the municipality and the $5 \times 5 \mathrm{~km}$ grid, respectively.

Table 1. Data description.


# 2.3. Methods 

There is a wide variety of methods aimed at solving regression tasks, including linear regression, model trees, neural networks, and Bayesian networks. The regression problem consists in obtaining a numerical prediction $\hat{y}$ for the response variable $Y$, given a set of explanatory variables $\mathbf{X}=\left\{X_{1}, \ldots, X_{n}\right\}$. In this case of study, the response variable is the percentage of heterogeneous land and the explanatory variables are the social and economic features described in Table 1, all of them being continuous.

2.3.1. Multiple Linear Regression

In multiple linear regression (MLR), response variable $Y$ is modeled as a linear combination of explanatory variables $\mathbf{X}=\left\{X_{1}, \ldots, X_{n}\right\}$, so that

$$
Y=\beta_{0}+\beta_{1} x_{1}+\cdots+\beta_{n} x_{n}
$$

where $\beta_{0}, \ldots, \beta_{n}$ are the regression coefficients.
Parameters $\boldsymbol{\beta}$ are estimated in order to obtain the best fit to the data. In our experiments, we used the glm function of the R [51] package stats to fit the linear regression model. This function uses iteratively reweighted least squares (IWLS) to find the maximum likelihood estimate of the parameters.

# 2.3.2. Model Trees 

In model trees (MT), the sample space of the explanatory variables is partitioned according to some splitting criteria (branches) that are found in order to minimize the learning error; then, a different model is fit in the terminal node of each split (leaf).

In this work, regression trees were fitted according to the M5P algorithm [52]. We used the implementation available in the R package RWeka [53]. An M5P model combines a decision tree along with multiple linear regression models on the leaves. This linear model on each leaf is defined with a different subset of variables, with the aim of minimizing the regression error. Therefore, the resulting model is a piecewise linear model in the variables' domain (see Figure 2).

Table 2. Variables used to compute some variables in Table 1 but not included the models.


![img-1.jpeg](img-1.jpeg)

Figure 2. Example of a model tree with six explanatory variables $\left(X_{1}, \ldots, X_{6}\right)$ and five leaves.

2.3.3. Neural Networks

Neural networks (NN) are a widely used tool for predictive purposes. They are intensely used in the Big Data and deep-learning fields, where datasets comprise vast amounts of both variables and observations, and there is the need to fit a predictive model. A typical neural network is composed of an input layer (with the explanatory variables), an output layer (with the response variables; it might contain more than one), and a certain number of hidden layers, which are placed between the input and the output layer (see Figure 3). At each layer, every variable is connected to all the variables in the previous layer. Every hidden node transforms its several inputs $\left\{I_{(j)}\right\}_{i=1}^{n}$ into a single output value $P$ according to a specific transfer or propagation function $\Phi$ (typically a nonlinear transformation), so that $P=\Phi\left(I_{(1)}, \ldots, I_{(n)}\right)$. This propagation function depends on a number of parameters (called weights). Once these weights have been learned for every node with the training dataset, the neural network can be used for making predictions on new data.

![img-2.jpeg](img-2.jpeg)

Figure 3. Example of a neural network (multilayer perceptron) with five input variables $\left(X_{1}, \ldots, X_{5}\right)$, a single hidden layer with three nodes $\left(h_{1}, \ldots, h_{3}\right)$, and a single output variable $(Y)$. The weights and propagation function have been omitted here for the sake of clarity.

In our experiments, we used the R package neuralnet [54] with a single hidden layer containing three hidden nodes (these models are often referred to as multilayer perceptrons, see Figure 3), and made five replications with different random initializations of the weights. We chose these parameters by trial and error; using a larger number of hidden nodes often caused convergence issues in the learning algorithm and might lead to overfitting as well.

# 2.3.4. Bayesian Networks 

Bayesian networks (BNs) are compact representations of the joint probability distribution over a set of variables $\mathbf{X}=\left\{X_{1}, \ldots, X_{n}\right\}$ whose independence relations are encoded by the structure of an underlying directed acyclic graph (DAG) [55]. Formally, a BN is defined as a pair $(\mathcal{G}, \mathcal{P})$, where $\mathcal{G}$ is a DAG and $\mathcal{P}$ is a set of conditional probability distributions (CPDs). $\mathcal{G}$ is composed of nodes that represent random variables $(\mathbf{X})$ and links between pairs of nodes, representing statistical dependence between them. Each node $X_{i}$ has a distribution $p\left(x_{i} \mid p a\left(x_{i}\right)\right)$ attached, where $p a\left(x_{i}\right)$ represents the

parents of $X_{i}$ in $\mathcal{G}$. The joint probability distribution over all the variables in the network is defined as the product of the CPDs attached to each node, that is:

$$
p\left(x_{1}, \ldots, x_{n}\right)=\prod_{i=1}^{n} p\left(x_{i} \mid p a\left(x_{i}\right)\right) \quad \forall x_{1}, \ldots, x_{n} \in \Omega_{x_{1}, \ldots, x_{n}}
$$

where $\Omega_{x_{i}}$ represents the set of all possible values of variable $x_{i}$.
There are different ways to represent CPDs, including conditional probability tables (CPTs), conditional linear Gaussian, or Mixtures of Truncated Basis Functions (MoTBFs). In this work, we have used a particular case of MoTBFs [56] called Mixtures of Truncated Exponentials (MTEs) [57], implemented in the Elvira software [58].

A BN can be used as a regression model by computing the conditional expectation of $Y$ given the observed explanatory variables, i.e., $E\left[Y \mid x_{1}, \ldots, x_{n}\right]$. Therefore, conditional density $f\left(y \mid x_{1}, \ldots, x_{n}\right)$ is computed in order to obtain the numerical prediction for $Y$, which means that the regression model is [59]:

$$
\hat{y}=E\left[Y \mid x_{1}, \ldots, x_{n}\right]=\int_{\Omega_{Y}} y f\left(y \mid x_{1}, \ldots, x_{n}\right) d y
$$

Typically, when facing regression problems only restricted network structures are considered since they reduce the number of parameters to be estimated from data. The extreme case is the naive Bayes (NB) structure, where all explanatory variables $\mathbf{X}$ are considered independent given $Y$ (Figure 4a). The independence assumption can be relaxed by expanding the NB structure, i.e., if more dependencies between the variables are considered. Tree-augmented naive Bayes (TAN) models allow each feature to have one more parent besides $Y$ (Figure 4b). The increase in complexity, in both structure and parameter learning, usually results in richer and more accurate models. In this work, we have included both the NB and the TAN models in the comparison of methods.
![img-3.jpeg](img-3.jpeg)

Figure 4. Examples of directed acyclic graphs (DAGs) in a Bayesian network with four explanatory variables. Left: a naive Bayes (NB) model. Right: a tree-augmented naive Bayes (TAN) model.

# 2.4. Variable Selection 

For all the methods, we followed a filter-wrapper variable selection procedure. Firstly, this approach orders explanatory variables $\mathbf{X}=\left\{X_{1}, \ldots, X_{n}\right\}$ according to their mutual information (MI) with response variable $Y$, obtaining an ordered set $\mathbf{Z}=\left\{Z_{1}, \ldots, Z_{n}\right\}$. Then, the first variable in $\mathbf{Z}$ $\left(Z_{1}\right)$ and the response $Y$ are used to learn a regression model. Afterward, the remaining explanatory variables in $\mathbf{Z}$ are inserted in the model, one by one, according to the aforementioned order, and a new regression model is obtained. Whenever the inclusion of a variable increases the accuracy of the model, it is kept; otherwise, it is excluded from the model. The accuracy of the model is measured in terms of its root mean squared error (RMSE), defined as:

$$
\mathrm{RMSE}=\sqrt{\frac{1}{n} \sum_{i=1}^{n}\left(y_{i}-\hat{y}_{i}\right)^{2}}
$$

Figure 5 shows a graphical representation of the variable selection procedure followed.

![img-4.jpeg](img-4.jpeg)

Figure 5. Algorithm for variable selection.

# 2.5. Model Validation 

The models were validated employing the $k$-fold cross-validation technique [60], obtaining a measure of error in each fold. This technique randomly splits the complete dataset into $k$ subsets, using $k-1$ for learning (train set) and the other for validation (test set). The method is repeated $k$ times so that each time a new train set is used to learn the model and a new test set is used to compute the RMSE. The average of the $k$ error measures gives an estimate of the out-of-sample error. Figure 6 shows a schematic representation of the $k$-fold cross-validation technique. In our experiments, a $k$-value of 10 was applied. The 10 RMSE measures of the five aforementioned regression models were compared using Friedman's Test with maxT statistics [61]. In those cases where significant differences were found, we deployed Wilcoxon-Nemenyi-McDonald-Thompson's posthoc test [62] to make a pairwise comparison of the methods.
![img-5.jpeg](img-5.jpeg)

Figure 6. Schematic representation of $k$-fold cross-validation.

## 3. Results

Table 3 shows the variables selected by each method. It can be noted that the number of selected variables is higher when the models were learned using the $5 \times 5 \mathrm{~km}$ grid dataset. In the case of

MLR, NB, and TAN, the selected number of variables is twice as high in the grid dataset than in the municipality one. Moreover, we computed the Fleiss kappa measure [63] to evaluate the degree of agreement of the different models at selecting variables, and obtained $k=0.337$ for the municipality dataset and $k=-0.043$ for the grid dataset, which means that there is a higher degree of agreement in the selection of variables when the models were learned using the municipality dataset.

On a municipality scale, all models selected Population density (pDens) and Distance to the main city (DMC) variables (Table 3). By contrast, the variable Population growth rate (EGR) was only selected by MLR model; the variables Unemployment rate (UR) and Tertiary sector (sect.T) were only selected by the MT model, and Mortality rate (MortR) was only selected by NB. NN selected the same variables as the models based on uncertainty, except for Old-age dependency index (ODI), Mortality rate (MortR), and No studies (st.no). These variables selected by uncertainty models can be representatives of the social characteristics of upland municipalities.

On a $5 \times 5$ grid scale, the number of variables selected ranged from nine (by Neural Networks) to 18 (by NB model). All models selected the variable Distance to the main city (DMC). The variables Population density (pDens), Sex ratio (SxR), Doubling time (DT), Population growth rate (EGR), Mortality rate (MortR), University (st.uni), and Tertiary sector (sec.T) were selected at least by four models. The variable Illiterate (st.ill) was only selected by TAN model.

A 10-fold cross-validation was carried out in order to test the predictive performance of the five regression models. Table 4 shows the RMSE measures obtained from the 10-fold cross-validation for each model and dataset. It is noticeable that the error is generally lower when the models were learned using the municipality dataset. The 10 RMSE measures of each model were compared to detect statistically significant differences. Figure 7 summarizes the results of the posthoc analysis carried out after the Friedman test. The box plots represent the difference in RMSE values between the corresponding models.

Table 3. Variables selected by each method for both the municipality and the $5 \times 5 \mathrm{~km}$ grid datasets. MLR: multiple linear regression; MT: model tree; NN: neural network; NB: naive Bayes; TAN: tree augmented naive Bayes.


For the sake of understanding, Figure 7 is explained in a simplified fashion. Let $\mathbf{A}$ be the set of $k$ RMSE values obtained from model $\mathcal{A}, \mathbf{B}$ the set of $k$ RMSE values corresponding to model $\mathcal{B}$ and $\mathbf{D}$ the

set of $k$ values corresponding to the difference between $\mathbf{A}$ and $\mathbf{B}$. The box plots in Figure 7 represent D, so that whenever $D_{i}<0$, with $i=1, \ldots, k$, the corresponding point in the box plot is below 0 (horizontal dashed line), which means that model $\mathcal{A}$ has a lower RMSE, since $A_{i}-B_{i}<0 \rightarrow A_{i}<B_{i}$, i.e., model $\mathcal{A}$ predicts better than model $\mathcal{B}$ in that particular fold. If model $\mathcal{A}$ systematically outperforms model $\mathcal{B}$, then the entire box plot is below 0 . Equivalently, whenever $D_{i}>0$, the corresponding point in the box plot is above 0 , which means that model $\mathcal{A}$ has higher RMSE since $A_{i}-B_{i}>0 \rightarrow A_{i}>B_{i}$, i.e., model $\mathcal{A}$ predicts worse than model $\mathcal{B}$ in that particular fold. If model $\mathcal{B}$ systematically outperforms model $\mathcal{A}$, then the entire box plot is above 0 .

It can be noted that the statistical test applied did not detect any significant difference ( $p$-value $>0.05$ ) between the models when they were learned using the municipality dataset (Figure 7a). On the other hand, we found significant differences ( $p$-value $<0.05$ ) between 4 pairs of models when they were learned using the grid dataset (Figure 7b). The differences are found between MT-MLR, with the former having a lower error, NB-MT, with the former having a higher error, TAN-MT, with the former having a higher error, and TAN-NN, with the former having a higher error.

Table 5 shows the execution time of the different models for both datasets. MLR is the fastest method, followed by the model tree (MT). On the other hand, the NN and the TAN models were the most time-consuming methods.

Table 4. RMSE obtained in each fold of the 10-fold cross-validation. The mean value of the 10 measures is also shown.


Table 5. Running time of the 10 -fold cross-validation for each model.


![img-6.jpeg](img-6.jpeg)

Figure 7. Box plots of the difference in model performance between pairs of models with regards to RMSE for both the (a) municipality and (b) grid datasets. Boxes filled in red indicate significant differences between the corresponding models according to the posthoc analysis carried out after the Friedman test.

# 4. Discussion 

### 4.1. Models Comparison

An MLR model is a mathematical tool for learning a model from data and making predictions afterward. However, the linear behavior in the data that this model assumes is rarely found in complex environments as the one studied in this paper. In ecology and environmental sciences, multiple regression has been frequently used in predictive modeling [10,11]. It is a simple method based on the linear and additive associations of the explanatory variables, but the colinearity between the independent variables can lead to incorrect identification of the most critical predictors [11]. If we consider cultural landscapes as socioecological systems, this tool should be used carefully, taking into account the nonlinear dynamics of the systems and the restrictions of the model.

On the contrary, MT is much more flexible than MLR [52]. It can adjust to complex data, splitting them into different chunks or pieces according to the values of some variables, and fitting an MLR on every leaf. MT can be understood as a piecewise multiple linear regression model. This makes these models rather adaptable and accurate with respect to learning errors [64]. Nevertheless, they have some significant inconveniences that have to be taken into account. Models involving trees are prone to overfitting, especially when the number of branches in the tree is large [65]. This means that, even if the fitting error is low, the predictions given by these models can be inexact. Additionally, the splitting criteria on the trees may involve thresholds with unnatural values or low-importance variables. This, along with the fact that the MLRs on the leaves of an MT are built with different subsets of variables (related or not with those that appear in the splitting criteria), makes medium- or large-size model trees hardly interpretable.

Even though NN often provide good results in regression problems (in terms of accuracy) [39,64], they require a computationally costly adjustment process in comparison to other methods. Due to their complex multilayer structure, these models are also difficult to interpret. Other problems that arise with the use of neural networks are the choices of their free parameters [35,36], These include the transfer function and the structural parameters (number of hidden layers, and amount of variables in each of them). Another issue is the stochastic nature of the fitting algorithm, which starts with a random guess of the weights, and thus several replications provide different models [36]. It is also known that, for small datasets, other, simpler regression models often outperform NNs, so that neural networks require large datasets to exhibit their advantages. Last but not least, neural networks can be

extremely complex models, even with a small size [38]. This can also lead to overfitting if only one focuses on the fitting error.

BNs provide a well-founded approach for dealing with complex systems [44]. The graphical representation provided by BNs makes them a transparent tool, since the different parts of the ecosystem can be seen as nodes that interact with other nodes in a network, and the relationship between them can be mathematically modeled [4,21]. BNs provide not only a numeric prediction of the response but also a full specification of the posterior probability distribution. Knowing this distribution can be useful in practice for making inferences about the response variable as, for instance, computing confidence intervals or testing hypotheses [48,49]. Another advantage is that there is no need to know the value of every explanatory variable to predict the value of the response, making this tool suitable for establishing scenarios of change where only a few variables are involved.

# 4.2. Socioeconomic Variables as Indicators 

The results show that the number of variables selected when the models were built using the municipality dataset differs from the case in which the $5 \times 5$ grid dataset was used. The Fleiss kappa measure indicates that the selection of socioeconomic indicators using the municipality scale can be more appropriate since there is a higher agreement among the methods. Moreover, the information collected in the $5 \times 5$ grid may not be as useful since the value taken by each variable in each cell was obtained by weight averaging the data from the municipality scale. Thus, this conversion led to repeated information. For this reason, the discussion is focused on the municipality scale.

- Population density (pDens) and Distance to the main city (DMC) can be considered as the most important indicators since all models selected them. Both variables can be related to land abandonment. The remoteness from big cities, where better connectivity to other cities and accessibility to public services are found, can be relevant factors of land abandonment [66]. Traditionally, emigration has abundantly occurred in cultural landscapes in Andalusia [67], especially among young people and women who seek to acquire a higher education level and better job opportunities in larger cities.
- In the past decades, these landscapes have attracted tourism [68]. The growth of tourism has changed the socioeconomic sectors, developing the tertiary (sec.T identified by the MT model) and hospitality sectors (sec.H). These sectors coexist with the primary sector through agriculture. In this sense, some authors [66,69] consider that many rural areas maintain symbiosis between tourism and agriculture. The variables related to tourism (sec.H) and agriculture (sec.P) were selected by the NN and NB models. Tourism is involved in population growth and the improvement of transportation infrastructures, such as roads [70], attenuating the abandonment process, and giving rural residents an opportunity to enhance their wellbeing [71].
- The variable related to middle-school studies (st.mid) can be considered as an important indicator since it was selected by four out of five models. Generally speaking, people with basic knowledge of writing and reading (st.no), and with middle school being their maximum level of attained education (st.mid), predominate in these landscapes. These variables emphasize the tourism-agriculture relationship. People dedicated to agriculture have basic knowledge, and people dedicated to tourism have middle professional training.
- Sex ratio (SxR) was selected by the MT and TAN models. As aforementioned, plenty of the emigrants are women who aim at obtaining a high education level and better job opportunities. As a consequence, the sex ratio is imbalanced toward men. This tendency is one of the main factors to the social and demographic sustainability of rural landscapes in Spain [70].


## 5. Conclusions

The applied statistical test did not find significant differences among the models, which means that all of them were competitive from a predictive accuracy point of view. However, they showed other

advantages/disadvantages that should be considered when building a model. The main disadvantage of MLR is the linearity assumption, with simplicity and speed being within its advantages. On the other hand, MTs overcome linearity assumptions by splitting the domain of the variables, obtaining more accurate results at the expense of making them hardly interpretable. NNs lack in interpretability and are time-consuming; however, these disadvantages can be accepted if a large dataset is available and the only concern is predictive accuracy. Finally, BNs provide many advantages, with transparency, interpretability, and potential inclusion of expert knowledge being especially relevant in the context of decision-making.

The comparison of these methods revealed some indicators of cultural landscapes that should be taken into account by decision-makers when planning policies or interventions to be implemented at the municipality scale. The management of cultural landscapes has traditionally considered environmental features. Since cultural landscapes are socioecological systems, this management should be done from an integrated perspective, including socioeconomic indicators. The indicators selected in this paper could be used in an integrated policy on cultural-landscape management in Andalusia. In general, the available socioeconomic information is limited to the municipality scale, making it difficult to obtain reliable results when artificially increasing spatial resolution, as shown in the results obtained by the grid dataset. Therefore, it is necessary that public administrations provide socioeconomic information in a higher level of detail. Possible future work in the land planning and management field is to characterize socioecological sectors within cultural landscapes according to the socioeconomic indicators selected in this paper.

Author Contributions: Conceptualization, P.A.A.; methodology, A.D.M. and D.R.-L.; software, A.D.M. and D.R.-L.; validation, A.D.M., D.R.-L., and P.A.A.; formal analysis, A.D.M. and D.R.-L.; investigation, A.D.M., D.R.-L., and P.A.A.; writing-original draft preparation, A.D.M., D.R.-L., and P.A.A.; supervision, A.D.M., D.R.-L., and P.A.A.
Funding: This work has been partly supported by the Spanish Ministry of Economy and Competitiveness, through project TIN2016-77902-C3-3-P.
Acknowledgments: D.R.-L. thanks the support from CDTIME (University of Almería), the research group FQM-229, and from the Campus de Excelencia Internacional del Mar (CEIMAR) of the University of Almería.
Conflicts of Interest: The authors declare no conflict of interest.
