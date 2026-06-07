# HIS AperTO 

## UNIVERSITÀ DEGLI STUDI DI TORINO

AperTO - Archivio Istituzionale Open Access dell'Università di Torino

Comparing models for quantitative risk assessment: an application to the European Registry of foreign body injuries in children.

## This is the author's manuscript

Original Citation:

## Availability:

This version is available http://hdl.handle.net/2318/139382 since 2016-11-07T17:10:38Z

Published version:
DOI:10.1177/0962280213476167
Terms of use:
Open Access
Anyone can freely access the full text of works made available as "Open Access". Works made available under a Creative Commons license can be used according to the terms and conditions of said license. Use of all other works requires consent of the right holder (author or publisher) if not exempted from copyright protection by the applicable law.

# IIIS AperTO 

![img-0.jpeg](img-0.jpeg)

UNIVERSITÀ DEGLI STUDI DI TORINO

This is the author's final version of the contribution published as:

Berchialla P;Scarinzi C;Snidero S;Gregori D. Comparing models for quantitative risk assessment: an application to the European Registry of foreign body injuries in children.. STATISTICAL METHODS IN MEDICAL RESEARCH. None pp: ---.
DOI: $10.1177 / 0962280213476167$

The publisher's version is available at:
http://smm.sagepub.com/cgi/doi/10.1177/0962280213476167

When citing, please refer to the published version.

Link to this full text:
http://hdl.handle.net/2318/139382

# Comparingmodelsfor quantitative risk assessment: an application to the European Registry of foreign body injuries inchildren 

Paola Berchialla, ${ }^{1}$ Cecilia Scarinzi, ${ }^{2}$ Silvia Snidero ${ }^{2}$ and Dario Gregori ${ }^{3}$<br>${ }^{1}$ Department of Clinical and Biological Sciences, University of Torino, Italy<br>${ }^{2}$ Department of Statistics and Applied Mathematics "Diego de Castro", University of Torino, Italy<br>${ }^{3}$ Unit of Biostatistics, Epidemiology and Public Health, Department of Cardiac, Thoracic and Vascular Sciences, University of Padova, Italy

Corresponding author:
Dario Gregori,
Unit of Biostatistics, Epidemiology and Public Health,
Department of Cardiac, Thoracic and Vascular Sciences,
University of Padova,
via Loredan 18, 35121 Padova, Italy.
Email: dario.gregori@unipd.it

#### Abstract

Risk Assessment is the systematic study of decisions subject to uncertain consequences. An increasing interest has been focused on modeling techniques like Bayesian Networks since their capability of (1) combining in the probabilistic framework different type of evidence including both expert judgments and objective data; (2) overturning previous beliefs in the light of the new information being received and (3) making predictions even with incomplete data. In this work, we proposed a comparison among Bayesian Networks and other classical Quantitative Risk Assessment techniques such as Neural Networks, Classification Trees, Random Forests and Logistic Regression models. Hybrid approaches, combining both Classification Trees and Bayesian Networks, were also considered. Among Bayesian Networks, a clear distinction between purely data-driven approach and combination of expert knowledge with objective data is made. The aim of this paper consists in evaluating among this models which best can be applied, in the framework of Quantitative Risk Assessment, to assess the safety of children who are exposed to the risk of inhalation/insertion/aspiration of consumer products. The issue of preventing injuries in children is of paramount importance, in particular where product design is involved: quantifying the risk associated to product characteristics can be of great usefulness in addressing the product safety design regulation. Data of the European Registry of Foreign Bodies Injuries formed the starting evidence for risk assessment. Results showed that Bayesian Networks appeared to have both the ease of interpretability and accuracy in making prediction, even if simpler models like logistic regression still performed well.


# Keywords 

Bayesian Network, children, classification trees, foreign body injuries, quantitative risk assessment

# Introduction 

Quantitative risk assessment (QRA) is the systematic study of decisions subject to uncertain consequences by means of tools and techniques of probability theory and statistics. ${ }^{1}$ One of the key features of QRA is its effort to look at whole systems and not isolated parts. Each possible adverse event is followed through to its consequences and at the same time the consequences of different adverse outcomes can be combined.

A wide range of techniques have been developed to address the risk assessment problem. They can roughly be classified as engineering, statistical or causal modeling techniques. ${ }^{2}$ The engineering approach is based on the idea that risk objectively exists and risk analysis is a tool to express it by probabilities and expected values. ${ }^{3}$ Engineering techniques are mainly devoted to simulate the behavior of the system which is going to be assessed. In health risk assessment, Compartmental flow models and other continuous simulation models, Monte Carlo uncertainty models, Discreteevent simulation models are among the most common techniques, while Fault trees and Event trees are a major tool in safety and reliability analysis. ${ }^{4-7}$

Statistical risk modeling relies on observed data, on covariates and responses, rather than attempting to simulate the causal process that leads to the adverse outcome. The task is challenging because typically it is not known (1) which aspects of covariates are relevant to the response; (2) the mathematical form of the relation among variables and response probabilities; (3) how unobserved variables can affect the observed relation. ${ }^{2}$ Among the techniques that have successfully been applied in risk analysis across various disciplines, there are logistic regression, artificial neural network and classification and regression trees. ${ }^{8,9}$

While statistical and engineering approaches are complementary, causal modeling can combine elements of both. The risk assessment problem has been successfully addressed in a wide range of application domains using Bayesian Networks (BNs), ${ }^{10,11}$ which offer the benefit of explicitly model causal factors. The success of BNs in QRA is mainly due to their capability of: (1) combining in the probabilistic framework different types of evidence including both subjective beliefs and objective data, (2) overturning previous belief in the light of the new information received and (3) making predictions with incomplete data. The compositional modeling characteristic of the engineering approach is captured by the ingoing-outgoing relations in the network, while the conditional probability distribution of each variable may be determined by machine-learning algorithms.

In this paper, the comparison of different statistical modeling techniques developed in the framework of QRA is proposed. Unsafe consumer products are involved in

thousands of injuries in children, which can be caused for example by ingestion of batteries or broken plastic parts of toys and can have severe consequences. ${ }^{12}$ The aim of this work consists thus in evaluating which modeling techniques, among those presented, can be better applied to assess the risk of such foreign bodies (FB) injuries in children. In general, probabilistic methods enable the characterization of the risk posed by products' characteristics such as their size or shape. ${ }^{13-15}$ In this paper, we focused on the application of statistical modeling techniques for the assessment of the risk to experience a severe injury. In particular, we were aimed at characterizing consumer and product's features and the surrounding circumstances that lead to hospital admissions.

In order to achieve this objective, data from the European Registry of Foreign Bodies Injuries 'Susy Safe" was used. The "Susy Safe" Registry is a European Union funded registry, which has been established for the collection of FB injuries in children aged $0-14$ and it is aimed at describing the clinical pattern and the public health burden of those injuries.

Following a short presentation of the data source, the implementation of the modelling techniques for QRA was described. Performance of the models (area under the ROC curve, sensitivity and specificity) were compared and a sensitivity analysis was carried out in order to
determine which explanatory variables have the most influence on the injury severity, thus giving an insight on how different modelling techniques may provide different explanation of the phenomenon under study. Finally, results were summarized and the benefit and limitations of each approach were discussed.

# 2. Materials and methods 

### 2.1 Data source

The European Registry of Foreign Body Injuries "Susy Safe" ${ }^{16}$ collected data on FB injuries in children aged $0-14$ according to the International Classification of Disease ICD9-CM 931-935. A total of 7296 cases were registered in 28 European hospitals at the end of March 2007. Data encompassed four main aspects of the FB injuries: (1) the characteristics of the children (age, gender); (2) the characteristics of the object (shape, rigidity and dimensions); (3) the circumstances of injury (presence of parents; activity performed by the child immediately before the accident); (4) hospitalization's details.

With regard to the FB dimensions, volume (calculated as the volume of the smallest regular geometrical solid containing the FB) and ellipticity (representing the

ratio between the maximum and the minimum size reported) were considered.
In order to analyze data in QRA's framework, children's age and gender were considered as control variables whereas FB characteristics (volume, ellipticity, shape and pliability) and the circumstances of the injury (adult presence or absence and the activity performed by the child) were considered as the key variables of interest, since they are key factors weighing on prevention strategies to avoid injuries or mitigate their severity.

# 2.2 Statistical methods 

BNs and four other predictive models were implemented to quantify the risk of experiencing a severe injury. According to the report drafted from the e Consumer Affairs (CA) Directorate of the Department of Trade and Industry (DTI), ${ }^{17}$ an injury was defined "severe" when the injured child was hospitalized for at least 1 day.

After building the models, a 10 -fold cross validation repeated 20 times was performed to evaluate their performance, which was summarized by the area under the ROC curve, the sensitivity and the specificity. ${ }^{18,19}$ Model fitting and model validation, with the exception of BNs, were carried out using R version 2.8.1. ${ }^{20}$

Furthermore, for each model the mutual information (MI) was used to identify the variables that have the greatest influence on the risk of severe injury. MI allowed measuring the effect of each variable on the Hospitalization (yes/no) outcome variable and it was calculated as

1(hospitalization; $Y$ )

$$
=\sum_{\text {hospitalization }_{i} \in\{0,1\}} \sum_{y \in Y} p\left(\text { hospitalization }_{i}, y\right) \log \frac{p\left(\text { hospitalizati }_{i}, y\right)}{p\left(\text { hospitalizati }_{i}\right) p(y)}
$$

Where $p\left(\right.$ hospitalization $_{i}, y$ ) is the joint distribution of the binary outcome and the variable Y and $p$ (hospitalizaion) and $p(y)$ their marginal probability distribution. ${ }^{21,22}$ Continuous variables were discretized. Age was binned into 5 bins and volume and ellipticity were binned into 10 bins. The number of bins was chosen in order to range between $1+\log _{2} n$ and $\sqrt{ } n^{23}$. It has been shown that when the number of bins is within this range, the MI outperforms other distance measures. ${ }^{24}$ Finally, the MI of each variable was normalized by the entropy of the outcome:

$$
H(\text { hospitalization })=-\sum_{i \in\{0,1\}} p\left(\text { hospitalization }_{i}\right) \log p\left(x_{i}\right)
$$

# 2.2.1 Bayesian Networks 

A BN is a graphical representation of the joint probability distributions over a set of random variables. It consists of a series of nodes representing variables connected by arrows forming a graph that has no cycles. The arcs specify the independent assumptions holding between random variables.

The resulting network is known as a directed acyclic graph (DAG). ${ }^{25,26}$ Each node in a BN is associated with a set of probability tables. For those nodes without ingoing arcs, the probability distribution is a prior distribution which requires supplying a set of initial values.

Different strategies can be adopted to build BNs ${ }^{27}$ : (1) both structure and probability tables can be generated from data; (2) both structure and probability tables are elicited from experts; (3) expert knowledge and objective frequency data can be combined, for example BN's structure can be defined by domain experts and probability tables can be learned from the data.

In this work, two BNs were implemented: (1) a first one (BN1) was completely generated from data; (2) a second one (BN2) was built using causal knowledge from otorhinolaryngologist physicians to model the structure ${ }^{28-30}$ and data to learn probabilities.

For BN1, the Greedy thick-thin algorithm ${ }^{31}$ was performed for learning the structure of the network. Since the software requires discrete variable, continuous variables were discretized on the basis of quintiles (Age and Volume variables) and tertiles (Ellipticity variable). Structure learning was carried out using GeNie. ${ }^{32}$

The learning of probability tables and the validation phase were both carried out using Netica, ${ }^{33}$ which allowed for specifying a fading factor in order to treat more recent cases with a higher weight than older ones.

For BN2, the implementation was entirely carried out using Netica. ${ }^{33}$

# 2.2.2 Artificial neural networks 

Artificial Neural Networks denote a set of information processing paradigm inspired on the biological nervous system behaviour. The multilayer perceptron (MLP) is the most popular neural architecture where neurons are grouped in layers and only forward connections exist. ${ }^{34}$

Several feed-forward neural networks architectures with back-propagation learning method were implemented. ${ }^{34}$ All neural networks contained from 10 to 25 neurons in a single layer and one neuron in the output layer. In all calculations, the layers were fully connected. The least number of misclassifications given as the average on the validation datasets was obtained for the network with 17 neurons in the hidden layer.

### 2.2.3 Classification trees

Classification tree (CT) is a nonparametric method based on recursive partitioning of a sample into subgroups. At each step the most significant predictor is used to split the sample into subset until no improvement is achieved in the classification accuracy.

Two classification trees have been implemented. A first one (CT1) was developed by the standard binary recursive partitioning using all predictor variables described in Table 1.

Table 1. Definition of variables and their states in the Bayesian network. Continuous variables were discretized on the basis of quintile (Age and Volume nodes) and tertile (Ellipticity node).



To avoid over-fitting, 10 -fold cross validation was used to determine the optimal size of the tree. The best size was selected according to the 1SE rule, by which the largest tree with cross-validated error within one standard deviation of the minimum was chosen. ${ }^{37}$

A second classification tree (CT2) was implemented by means of a hybrid approach, exploiting a BN. Following Cox's establishments, ${ }^{38}$ a BN was implemented and sensitivity analysis was carried out. All variables whose MI had the outcome node (Hospitalization) fully explained by other variables or inconsistent with the hypothesis of causality were discarded. Finally a classification tree considering the outcome node and its minimal set of predictors, consisting in outcome node's parents, its children and children parents, was implemented. These pre-processing data procedures allowed to eliminate variables statistically associated with the outcome variable only due to confounding. In fact, in a causal graph $X \leftarrow Z \rightarrow Y$, the parent node Z is a confounder since it explains away an apparent association between X and Y . Thus, including outcome nodes' parents in the classification tree permitted to avoid these situations. ${ }^{38}$

# 2.2. 4 Logistic regression

Logistic regression (LR) model is a statistical tool widely used to fit probability of an event by a linear function of the explanatory variables. ${ }^{39}$

A logistic regression model was constructed using backwards variable elimination at a significant level of 0.05 . The backward variable elimination was based on sequential elimination of variables from an initial model consisting of all the predictor variables. At each step the variable which resulted in the greatest reduction of the AIC criterion was removed from the model. The rule of eliminating variables followed on until no further significant reduction of the AIC was obtained. ${ }^{19}$ Interaction among variables was checked in a similar way.

# 2.5 Random Forest 

Random forest (RF) is a collection of classification trees. ${ }^{40}$ Each tree is grown using a bootstrap sample from the original data. About two-thirds of the data are used to construct the classification tree, whereas the remaining Out-Of-Bag (OOB) data, which is left out, is used to obtain unbiased estimates of correct classification rates and variable importance.

Bootstrapping procedures are carried out for building an ensemble of trees with a reduced dependence among them. When building a classification tree, for each node of the tree, the RF algorithm selects some variables (the number of variables to select is usually taken to be the square root of the total number of variables) and uses only them to determine the best possible split at a single node - which is determined by the independent variable that best divides the sample in that node into two subgroups, each with the most pure membership using the Gini index as the splitting criterion.

Each tree in the forest is grown using the bootstrapped sample, and the OOB part is thus processed by the grown tree. This gives rise to classification for each point in the OOB part of that bootstrapped sample, meaning that about one third of the trees in the random forest give a prediction for each point in the original data. The final classification of a particular data point is decided on the basis of majority vote. The unbiased estimates of true classification rates are calculated by comparing the OOB set classification made by the forest to the experimentally observed classes to which the data points belong. The random forest package in R was used to implement the model.

## 3 Results

### 3.1 Input variables

In Table 1, input variables provided by the Susy Safe registry were listed in the "Node description" column. Variables Age and Gender recorded demographic characteristics of the injured child; Location reported the location of the foreign body, which caused the accident using International Classification of Disease (ICD-9) codes: ICD931 (FB in the ears), ICD932 (FB in the nose); ICD933 (FB in the pharynx and larynx); ICD934 (FB in the trachea, bronchi and lung); ICD935 (FB in the mouth).

The details of hospitalization were provided in two variables: (1) Hospitalization, which recorded whether the child experienced at least 1 day of hospitalization; (2) Complications, which recorded whether the child experienced complications, e.g. obstructions, pneumonia esophageal atresia, nasal odorous discharge.

FBs were described by shape, rigidity and size, according to Rimell's definition. With regard to
their shape, FBs were assigned to one of the following categories: 2D circle (e.g. some pieces of paper), 3D (e.g., pen cap), cylinder (e.g. coins), needle shape (e.g. pins and needles), spherical (e.g. balls and pebble) and other shapes.

With regard to the size, when the dimensions of the object (given in mms) were reported, the volume was calculated as follows: for 3D objects the volume of a parallelepiped was calculated considering the length of the axes; for spherical objects the volume of a sphere was calculated by the diameter reported; for 2D circle objects, the volume was approximated by that one of a cylinder with height 1 mm . Such volume measures represent how much space takes up the smallest geometrical figure containing the irregular-shaped foreign body. In addition, for three-dimensional not spherical objects, the ellipticity, i.e. the ratio between the longest axis and the shortest axis, was computed.

In Table 1, modalities of the discrete variables were reported (column 3), along with the classes used to discretize the continuous variables.

The structure of the BNs BN1 and BN2 is depicted in Figures 1 and 2, respectively (see Table 1 for the description of nodes); classification trees CT1 and CT2 are shown in Figures 3 and 4,

![img-1.jpeg](img-1.jpeg)

Figure 1. Structure of Bayesian network (BN) completely generated from data (BN1). Labeled rectangles are node (model variables); arrows represent conditional dependence relationships. Since BN1 is completely generated from data, the arrows between two nodes do not imply causation but just the existence of a relationship, which is given by
a conditional probability table.
respectively. In implementing the classification tree CT2, potential confounding effects with other variables were eliminated by means of data pre-processing described in section 2.2.3. Thus, in this case, the relationship among severe injuries and other variables was potentially interpretable as causal. Logistic regression parameter estimates are shown in Table 2.

In Table 3, the performance of each of the models is summarized with the Area under the ROC curve, sensitivity and specificity along with their $95 \%$ confidence intervals. The ranking of features based on the MI computed among Hospitalization and all other model variables is shown in Table 4, giving thus a measure of the relative importance of the variables as predictor of severe injuries.

It could be observed that in the BNs, nodes which are closer to the Hospitalization node (Figures 1 and 2) showed a greater impact in predicting injury severity. Conversely, the influence of nodes farther away tended to be diluted due to the uncertainty introduced by the intermediate nodes, in a phenomenon already known

and described in the literature. ${ }^{21}$ For the logistic regression model, backward variable elimination yielded a reduced model with 6 out of the 12 original variables.

# 3.2 Scenarios definition and prediction 

The combination of events, features and processes causing diverse natural phenomena could be taken as a scenario. The capability to predict scenarios and compute an occurrence probability is a
![img-2.jpeg](img-2.jpeg)

Figure 2. Bayesian network (BN) modeled using causal knowledge of the phenomenon derived from othorhinolaryngologist (BN2). Labeled rectangles are node (model variables); arrows represent conditional dependence relationships.
valuable tool for risk assessment because it allows for extrapolation of hazard and prevention. BNs can handle this feature in a very straight-forward way. To illustrate this point we calculated the risk of hospitalization of a few scenarios that may be encountered in the clinical practice.

In Figure 5, an example about how BNs deal with scenarios is presented. In this example, BN1 has been considered since it is the BN model that achieves the best accuracy (Table 3). After setting the evidence (a male who had an injury while he was playing with a spherical shaped object) the probability of being hospitalized was computed making use of the Bayes Theorem. Thus, given the injury occurred, the probability to be hospitalized is $83.3 \%$. Entering new evidence made it possible to

update probabilities. For example, if a needle-shaped foreign body, e.g. a fishbone, is swallowed while a child is eating, the probability of an injured male to be hospitalized was about $40 \%$, whereas for an injured female was slightly lower ( $37 \%$ ).

Finally, since the BN completely generated from data (BN1) outperformed all other models (Table 3), it was used to construct a set of risk profiles (Table 5). In fact, given the type of the foreign body, its shape, rigidity and volume, child's age and gender, the probability of observing an injury was computed. Also the most probable location of the foreign body along with the most probable extraction techniques required were reported in addition to the probability of experiencing a hospitalization.

# 4 Conclusion 

In this paper, a comparison among techniques widely used in QRA was proposed. An approach based on BNs was adopted to carry out a risk analysis on foreign body injuries in children. BNs

![img-3.jpeg](img-3.jpeg)

Figure 3. Classification tree (CT1). Prior probabilities at each group have been treated as equal. Terminal nodes are symbolized by rectangles; non-terminal nodes, by ovals. Splitting criteria are specified in the nodes. The probability of experiencing a hospitalization is given within the node according to the set of rules specified.
performance was compared to a set of competing statistical risk modeling methods: (1) logistic regression models (LR); (2) artificial neural networks, ANN; (3) classification trees, CT1 and (4) random forest. A hybrid approach using BNs in building classification trees (CT2) was also considered. Children's hospitalization was identified as the outcome measure of injury severity and it was studied in relation to the child's age and gender and accident details.

Artificial neural networks (ANNs) along with classification trees and random forest are a rich tool in dealing with noisy or incomplete data. A drawback of ANNs is, however, that there are no standard methods for constructing the architecture. In this study, we set up a single hidden layer feed-forward neural network, which is the

common type encountered in the literature. ${ }^{34}$
The classification tree approach is also a method extremely robust to the presence of irrelevant variables and variables with little predictive value. Besides a nonimpressive total accuracy, standard classification tree (CT1) showed to be capable of better identifying injuries at a higher risk of severity ( $96 \%$ of sensitivity). Furthermore, contrary to ANNs, which are "black box" models of difficult
![img-4.jpeg](img-4.jpeg)

Figure 4. Classification tree built using a hybrid approach (CT2). A Bayesian network was completely generated from data. Then a standard classification tree was fit between the outcome (hospitalization) and the minimal set of predictors given by the parents in the Bayesian network.
interpretation, it provided a way to extrapolate decision rules for achieving threat reduction in the form of a ready-understandable flowchart.

Like ANNs, random forests do not present a ready-understandable flow-chart. They are an ensemble method, which reduces variability of trees by averaging multiple trees. Thus, as expected, it showed a slightly better specificity and a lower sensitivity than CTs, achieving an overall performance which made it comparable to ANNs.

Logistic regression is a popular statistical method, owing largely to its simplicity

and the interpretability of the estimated parameters, which can generate excellent prognostic models. Although LR is not adept at modeling grossly nonlinear complex interaction, in our study it showed indeed its ability to capture non-linear effects outperforming ANNs and standard CT, which also were affected by a low specificity.

Two different strategies were chosen to implement BNs: (1) a BN in which both the structure and probability tables were generated purely from the data (BN1); (2) a BN in which the structure was defined by experts (mainly otorhinolaryngologists) of the phenomenon, whereas the probability tables were entirely learned from the data (BN2). One of the main differences that arose between the two models was the role of the Extraction technique and Complications variables. In a causal representation of the phenomenon, extraction methods can be potential cause of complications, which is the most important predictor of injury severity. This fact did not arise in the BN completely generated from data (BN1) as well as in the automatically generated models. Indeed, inspecting the

Table 2. Results of logistic regression model.


Table 3. Area under the ROC curve was used to assess the performance of the models: Bayesian Networks (BN1 and BN2); logistic regression (LR), neural networks (ANN); classification trees (CT1 and CT2); random forest (RF).


registry, it has been recognized that many records reported symptoms related to the presence of a FB, such as pain, epistaxis or hearing loss, instead of clinical complications, and this indeed explained why extraction technique and not complications was the most influential variable in predicting severe injuries.

Our analysis has shown that BN1 and the hybrid approach CT2 outperformed all methods in terms of accuracy. Opposing to CT2, the advantage of BNs relied on the fact that complex relationships among factors were explicated in a graphical model, which incorporated uncertainty via the conditional probability associated to each node. ${ }^{26}$ Indeed, BNs gave a picture of the influence of critical factors on the injury severity. Results from ranking of variables suggested the conclusion

Table 4. Sensitivity analysis was carried out on hospitalization variable to determine the covariates that have the most influence on the injury severity.


.

![img-5.jpeg](img-5.jpeg)

Figure 5. The scenario of a male who had an injury while he was playing with an object with spherical shape is depicted using BN1. Foreign body (FB) was located in the mouth, esophagus or stomach (ICD935). Hospitalization node returned the probability the injury lead to hospital admission (83.3\%). Probability table associated to Foreign body type
node (not showed to allow for a better visualization) gives that there is $89 \%$ of probability the child is playing with a button. Also, there is $63.3 \%$ of probability the injury occurred in absence of an adult (see adult presence node).
that models do not always give the same interpretation for the same covariates, according to other studies, ${ }^{42,43}$ rather they provide a different framework for the explanation of the evidence.

Thus, a tool which allows for a ready interpretation of relationships among risk factors is of great use. In the framework of risk analysis, this capability makes BN a competing alternative to other approach, such as logistic regressions, which are often preferred since they provide easily interpretable results. The possibility to analyze different scenarios is an import feature which allows to asses the effect of FB's characteristics and incident's circumstances, such as adult absence/presence, on the risk of experiencing a severe injury, once the injury has occurred. In fact, probability updating after setting evidence can be used to identify in a straightforward manner the characteristics of unsafe products or the importance of adult surveillance in

mitigating injury severity.
However, it should be noted that the logistic regression model showed an overall classification accuracy which was not far behind BNs, confirming to be an efficient model for classification task, despite its simplicity.

Even if BNs can be considered for causal modeling, in this study they were considered for association analysis only. The absence of an independent sample to externally validate the models constituted the major limitation of this study.

Table 5. Predicted probability of observing evidence on foreign body and children characteristics based on BN1. The probabilities of the most probable FB location (ICD) and extraction technique required are reported along with the probability of experiencing a hospitalization given that an injury occurred.


BN: Bayesian Network; FB: foreign body; ICD: International Classification of Disease.

.

# 4.1 Final remarks 

While logistic regression models were found to be a simpler model, which still perform well comparably with other more complex statistical techniques, BNs, beyond outperforming all other models, offered some advantages in the context of QRA.

Since the "Susy Safe" surveillance registry is set up to constantly receiving new cases, we chose to treat BN as an adaptive net giving a higher weight to more recent cases with respect to the older ones. As a result, we built a BN that while receiving cases and updating information on foreign body features (size, shape and rigidity) was able to quickly respond to instances of changing product safety design regulation.

The capability of identifying relationships among variables is a key feature of BNs. In this analysis, the BN confirmed the role of FB's type along with its shape and rigidity in determining the risk of severe injury, beside its location and the extraction procedure chosen by physicians. Moreover, the complex relationships among risk factors showed that there was not a single cause related to the severity of the injury but a more complex pattern of events contributing to the adverse outcome.

The conclusions drawn from this single comparative study are certainly not definitive.
