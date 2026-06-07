# Review 

## Bayesian Networks for the Diagnosis and Prognosis of Diseases: A Scoping Review

Kristina Polotskaya ${ }^{1,1}$ (D), Carlos S. Muñoz-Valencia ${ }^{1,1,1}$ (D), Alejandro Rabasa ${ }^{1}$ (D), Jose A. Quesada-Rico ${ }^{2,3,4}$ (D), Domingo Orozco-Beltrán ${ }^{2,3}$ (D) and Xavier Barber ${ }^{1,4,+}$ (D)<br>check for updates

Citation: Polotskaya, K.; Muñoz-Valencia, C.S.; Rabasa, A.; Quesada-Rico, J.A.; Orozco-Beltrán, D.; Barber, X. Bayesian Networks for the Diagnosis and Prognosis of Diseases: A Scoping Review. Mach. Learn. Knowl. Extr. 2024, 6, 1243-1262. https: / / doi.org/10.3390/ make6020058

Academic Editor: Federico Cabitza
Received: 4 April 2024
Revised: 27 May 2024
Accepted: 31 May 2024
Published: 4 June 2024

## (0)

Copyright: (c) 2024 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 Center of Operations Research, Miguel Hernández University, 03202 Elche, Spain; k.polotskaya@umh.es (K.P.); carlos.munoz06@goumh.umh.es (C.S.M.-V.); a.rabasa@umh.es (A.R.)
2 Department of Clinical Medicine, Miguel Hernández University, 03550 San Juan de Alicante, Spain
3 Primary Care Research Center, 03550 San Juan de Alicante, Spain
4 Joint Research Unit for Advanced Statistical Methods in Health Sciences UMH-FISABIO: STATSALUT, Miguel Hernández University, 03202 Elche, Spain

* Correspondence: xbarber@umh.es

1 These authors contributed equally to this work.
I Current address: Centro de Investigación Operativa, Universidad Miguel Hernández de Elche, Avda. de la Universidad s/n, Edificio Torretamarit, 03202 Elche, Spain.


#### Abstract

Bayesian networks (BNs) are probabilistic graphical models that leverage Bayes' theorem to portray dependencies and cause-and-effect relationships between variables. These networks have gained prominence in the field of health sciences, particularly in diagnostic processes, by allowing the integration of medical knowledge into models and addressing uncertainty in a probabilistic manner. Objectives: This review aims to provide an exhaustive overview of the current state of Bayesian networks in disease diagnosis and prognosis. Additionally, it seeks to introduce readers to the fundamental methodology of BNs, emphasising their versatility and applicability across varied medical domains. Employing a meticulous search strategy with MeSH descriptors in diverse scientific databases, we identified 190 relevant references. These were subjected to a rigorous analysis, resulting in the retention of 60 papers for in-depth review. The robustness of our approach minimised the risk of selection bias. Results: The selected studies encompass a wide range of medical areas, providing insights into the statistical methodology, implementation feasibility, and predictive accuracy of BNs, as evidenced by an average area under the curve (AUC) exceeding $75 \%$. The comprehensive analysis underscores the adaptability and efficacy of Bayesian networks in diverse clinical scenarios. The majority of the examined studies demonstrate the potential of BNs as reliable adjuncts to clinical decision-making. The findings of this review affirm the role of Bayesian networks as accessible and versatile artificial intelligence tools in healthcare. They offer a viable solution to address complex medical challenges, facilitating timely and informed decision-making under conditions of uncertainty. The extensive exploration of Bayesian networks presented in this review highlights their significance and growing impact in the realm of disease diagnosis and prognosis. It underscores the need for further research and development to optimise their capabilities and broaden their applicability in addressing diverse and intricate healthcare challenges.


Keywords: Bayesian networks; disease diagnosis; disease prognosis; directed acyclic graph; Bayesian classifier; scoping review

## 1. Introduction

In medicine, determining the cause of an event is often not straightforward. Experts find numerous sources of possible uncertainty, unclear and incomplete measurements, and events for which it is difficult to establish causal relationships. Accordingly, probabilistic graphs are useful tools to understand, in a visual and intuitive way, how each factor affects the rest of the system.

In this review, we delve into the application of Bayesian networks (BNs) for diagnosis and prognosis in healthcare. The focus on BNs is driven by the potential to integrate these models into hospital decision support systems, particularly for specific diagnostic applications. Understanding the fundamentals and implications of BNs in these crucial areas is essential for their successful implementation. This review aims to provide a comprehensive background on the capabilities of BNs, enhancing healthcare delivery by improving diagnostic accuracy and prognostic assessments, thereby benefiting patient management and outcomes.

In this scoping review, we analyse various articles related to diagnosis, as mentioned in the previous paragraph. The objective of these publications is to examine how Bayesian networks can serve as an effective system for decision-making in medicine, although they are currently limited to being a decision support system. While the reader may be aware of the significant advancements in artificial intelligence and artificial neural networks (deep learning), it is important to note that not all diseases are diagnosed through image analysis. Bayesian networks, as we will explain in this section, use diagrams to identify probabilistic causality based on Bayes' rule.

A Bayesian network is a probabilistic graph that tries to reproduce a real system. Used in basic and applied research, as well as in artificial intelligence, BNs are based on Bayes' theorem and visualised with a directed acyclic graph (DAG), which is used to represent dependence or cause-and-effect relationships between variables. In this way, new knowledge is generated under conditions of uncertainty, which makes it easier to decide and reason through probability theory [1]. BNs were introduced in the 1980s as a formalism for representation and reasoning through problems involving uncertainty, by adopting probability theory as a basic framework [2]. Since then, they have not only been used successfully in medicine; they have also been central to the development of numerous applications in other fields, including environmental sciences [3], production processes [4], finance [5], the debugging of artificial intelligence programs [6], and genetics [7]. In the health sciences, BNs are applied to improve treatments, diagnosis, and prognosis, helping physicians to make reliable decisions by enabling faster and more accurate prediction [8]. According to Kyrimi et al. [9], the reason behind the wide application of BNs in medical diagnosis lies in their ability to express expert knowledge, model uncertainty, and deal with incomplete data. This literature review aims to provide a comprehensive description of BNs and their applications in medicine in general, as in [9]. In particular, this review will focus on diagnostic and prognostic processes, as well seeking as to show the advantages of this method compared to others from the fields of artificial intelligence or machine learning, areas that have been attracting more attention in recent times. Before presenting the conducted searches and analysing the content of the articles, we will provide a concise overview of Bayesian networks and their types, classifiers, and evaluation methods. The aim is to introduce the reader to the subject matter, thereby facilitating a better understanding of the results and terminology used in the articles that will be analysed subsequently.

# 1.1. Definition of Bayesian Networks 

We will now describe the basic concepts around BNs, the types of networks, and the unique structures known as Bayesian classifiers. We also briefly address the topic of learning about parametric and structural BNs, and finally we present the computation of a BN, describing the software available for BN applications.

Let us start by looking at the example in Figure 1, which defines a causal relationship between the variables flu, cough, and fever, where flu is expected to causally influence the presence of a cough or fever. The variables cough and fever are not independent. If a person has a cough, they may have the flu, and then they probably have a fever.

However, consider that, if a person has the flu, it is reasonable to conclude that the presence of a fever does not depend on the presence of a cough. Therefore, we assume that

the variables cough $\left(X_{2}\right)$ and fever $\left(X_{3}\right)$ are conditionally independent given the variable flu $\left(X_{1}\right)$. Formally, this can be expressed as follows:

$$
\begin{gathered}
P\left(X_{2} \mid X_{1}, X_{3}\right)=P\left(X_{2} \mid X_{1}\right) \\
P\left(X_{3} \mid X_{1}, X_{2}\right)=P\left(X_{3} \mid X_{1}\right)
\end{gathered}
$$

Therefore,

$$
P\left(X_{1}, X_{2}, X_{3}\right)=P\left(X_{2} \mid X_{1}\right) P\left(X_{3} \mid X_{1}\right)
$$

![img-0.jpeg](img-0.jpeg)

Figure 1. Representation of the relationships between variables (directed acyclic graph, DAG).
The variable $X_{1}$ has an influence on both $X_{2}$ and $X_{3}$, but it is assumed that there is no direct relationship between $X_{2}$ and $X_{3}$. The representation of these relationships is usually achieved via a node and arrow diagram, connecting the influencing variables (primary variables) with the influenced variables (secondary variables). The structure shown in Figure 1 is a BN.

Considering the graphic structure of Figure 1 and, more precisely, the parents of each variable, the joint probability distribution can be written as follows:

$$
P\left(X_{1}, X_{2}, X_{3}\right)=P\left(X_{1} \mid P a\left(X_{1}\right)\right) \cdot P\left(X_{2} \mid P a\left(X_{2}\right)\right) \cdot P\left(X_{3} \mid P a\left(X_{3}\right)\right)
$$

where $P a\left(X_{i}\right)$ is the parent variable of $X_{i}$.
This equation is the formal definition of a BN, in the case of three variables. Using the process of the analysis and classification of the unconditional independence between the three variables, we have converted $P\left(X_{1}, X_{2}, X_{3}\right)$ into a product of three conditional probabilities.

Probabilistic networks are visual depictions of the variables and their connections that define a particular scenario [10]. One of the most popular types is the BN [11], which provides information on the conditional dependencies and independencies among variables. The existence of independent relationships in a network makes BNs a valuable instrument in portraying knowledge consistently, as they decrease the required number of parameters. These relationships simplify the expression of the joint probability function by representing it as the multiplication of the conditional probability functions of each variable.

Because they represent a probability distribution, BNs confer a clear meaning, so they can be adapted for diagnostics, learning, explanation, and inferences [12]. Depending on the meaning given to them, they can represent causality [13] or correlations [14].

It could thus be said that a Bayesian network is a DAG whose nodes represent random variables and whose arcs represent direct dependencies-for example, causal relationships; see Figure 2. Each node has a conditional probability table, which quantifies the relationships between the connected variables [15].

A BN is a probabilistic model composed of two different parts: on the one hand, there is the graphical structure (DAG), which defines the relationships between the variables, and, on the other hand, it considers the probabilities established between these variables [1]. The elements of a BN are as follows [16]:

- A set of variables (continuous or discrete) that form the vertices or nodes of the network;
- A set of directed links connecting a pair of vertices-if there is a relationship with the direction $X \rightarrow Y$, then $X$ is said to be the parent of $Y$.

The network fulfills the following conditions:

- There is an association between each vertex $X_{i}$ and a conditional probability function $P\left(X_{i} \mid P_{x}\left(X_{i}\right)\right)$, which takes as input a specific set of values for the parent variables of the vertex and gives the probability of the variable representing $X_{i}$;
- The graph does not have directed cycles, i.e., it does not have directed trajectories or paths that start or end at the same node.
![img-1.jpeg](img-1.jpeg)

Figure 2. Generic structure (DAG) of a BN for $P$ with $n$ random variables $X_{1}, \ldots, X_{n}$.
BNs have a planning algorithm based on the Bayes theorem that describes and forecasts, so that inferences can be made, calculating the posterior probabilities of unknown variables based on known variables. A BN provides an inference system that changes the probability distributions as soon as new evidence is found about some vertices, while the new probabilities are transferred to the remaining nodes. The probability transfer is considered a probabilistic inference, which means that the probability of some variables can be determined from the evidence provided on other variables. Before the evidence is presented, they are called prior probabilities; afterwards, they are called posterior probabilities [16,17].

# 1.1.1. Types of Bayesian Networks 

Depending on the type of random variable used in the construction of a BN, there are discrete BNs, where each variable takes a finite number of values, and the probability distribution associated with each variable is multinomial. If the variables used to build the Bayesian networks are continuous, one method is to discretise the variables, i.e., to divide them into nominal intervals. However, discretisation implies a certain loss of information and the assignment of many parameters [18]. Modelling with continuous variables is a good alternative in this case. Gaussian BNs are used when continuous variables are used in the BN construction process, and each of them has a multivariate normal distribution [19]. When discrete and continuous variables are introduced in the construction process, they are called mixed BNs.

In discrete BNs, the probability distribution is determined by the probability tables, while, in Gaussian BNs [20], it is determined by the joint density function.

For [21], in scenarios where conditions evolve over time (such as the sequential activation of brain areas during cognitive decision-making), dynamic Bayesian Networks (BNs) are necessary. A standard BN sets the initial conditions. In dynamic BNs, the structures representing time intervals are consistent, and the conditional probabilities remain unchanged over time. Thus, dynamic BNs are time-invariant models, where 'dynamic' refers to their capability to model systems with temporal dynamics. However, three years later, Dagum [22] refined the concept of dynamic Bayesian networks to unify and extend them to forecast time-dependent systems.

# 1.1.2. Bayesian Classifiers 

Bayesian classifiers are a particular type of BN where there is a specific variable that is the class and the other variables are attributes or characteristics. A Bayesian classifier determines the posterior probability of each class, $C_{i}$ (i.e., ill or not ill due some symptoms), using Bayes' theorem:

$$
P\left(C_{i} \mid E\right)=P\left(C_{i}\right) P\left(E \mid C_{i}\right) / P(E)
$$

Many Bayesian classifiers have been proposed for the estimation of probabilities [23], such as the naive Bayesian classifier (NBC), the tree-augmented naive Bayesian classifier (TAN), and the Bayesian network-augmented naive Bayes (BAN) classifier.

The NBC allows the features to be independent of each other given the class, so the probability is found by multiplying the particular conditional probabilities of each feature given the class vertex [24]. $P(C)$ is the vector of the prior probabilities of each class, and $P\left(E_{i} \mid C\right)$ is the conditional probability matrix of each feature. The features are conditionally independent given the class, so that there are no edges between them, as shown in Figure 3.
![img-2.jpeg](img-2.jpeg)

Figure 3. An example of a naive Bayesian classifier.
The NBC presents high classification precision in many areas [25]. However, sometimes, its performance is affected by the dependence of the features or attributes. One way to resolve this situation is to expand the basic NBC structure by adding edges between features. Two basic options are known [23]:

- The Tree-Augmented Naive Bayes (TAN), with a tree structure added between the characteristics, so that, in principle, there are few links and the complexity of the structure does not increase substantially;
- The Augmented Naive Bayes (BAN) adds a general dependency structure between features, without restrictions.


### 1.1.3. Learning Bayesian Networks

Finding the structure that best fits the data becomes one of the key problems to solve when using BNs. This task is performed by two types of machine learning: structural learning, which acquires the network structure (trees, poly-trees, or multi-connected networks) from the data; and parametric learning, which has the associated probabilities (table of probability) of each root node and the other variables. In order to determine the probability distributions linked to each vertex of the network, it is necessary to know the type of network, i.e., these two learning approaches cannot be carried out independently [24].

### 1.1.4. Computation of a BN

The use of software plays an important role when building the structure of a BN, since it allows the graphic representation of a network so that it is understandable to those involved in its development. Ref. [26] describes the software programs Netica v.5.0 (Norsys Software Corp., Vancouver, BC, Canada), Elvira v.2.0 (Department of Statistics and Applied Mathematics University of Almería, Almería, Spain), and Hugin v.9.4 (HUGIN

EXPERT A/S, Aalborg, Denmark). Demo versions of Netica and Hugin are available free of charge, but some features are locked. The demo version of the Hugin software allows for a maximum of 20 variables, which is not enough to solve sequence analysis problems or even to compare the results with other tools. Elvira is a Java-based software tool that emerged from a collaboration among several Spanish universities, aimed at building and evaluating graphical probabilistic models. The software offers both exact and approximate algorithms to handle discrete and continuous variables and includes features for explanation, learning from databases, and network fusion [27].

The study by Charles River Analytics [11] describes the BNet program, which applies BNs to predict and display weather forecasts. Murphy et al. [28] provides different software applications for BNs. There are many private and free software programs available on the Internet.

Kenet et al. [29] presents a list of software packages used to generate and analyse BNs, including the following.

- GeNIe v.4.1.R2 (BayesFusion, LLC, Pittsburgh, PA, USA) is a development environment for reasoning in graphical probabilistic models, and SMILE is its inference engine. GeNIe is freely available for any use and has several useful features, such as a module for the exploration and analysis of a data set and the learning of BNs and their numerical parameters from data. It has a special module that addresses problems related to diagnosis [30].
- The R bnlearn package [31] is powerful and free. Compared to other available Bayesian network software, it can implement more constraint-based and score-based methods [31]. This R package is our preferred choice.
- Bayesia has also developed a proprietary technology for the analysis of BNs. In collaboration with laboratories and large research projects, the company develops innovative technological solutions. Its products include (1) BayesianLab, a learning program; (2) Bayesian Market Simulator, a simulation software package that can be used to compare the influences of a set of competing offerings relative to a defined population; (3) Bayesian Engines, a library of software components through which the modelling and use of Bayesian networks can be integrated; and (4) Bayesian Graph Layout Engine, a library of software components used to integrate the automatic positioning of graphs into specific applications.


# 1.1.5. Model Validation 

The validation of a model justifies its correctness. Validation usually involves checking the performance of the model and its further improvement. Model performance can be expressed through several measures [30], as shown in Table 1.

Now, using the information of the confusion matrix, some basic performance measures will be defined as follows:

$$
\begin{aligned}
\text { Sensitivity }(\text { Recall }) & =\frac{\mathrm{TP}}{\mathrm{TP}+\mathrm{FN}} \\
\text { Specificity } & =\frac{\mathrm{TN}}{\mathrm{TN}+\mathrm{FP}} \\
\text { Accuracy } & =\frac{\mathrm{TP}+\mathrm{TN}}{\mathrm{TP}+\mathrm{TN}+\mathrm{FP}+\mathrm{FN}} \\
\text { Positive predictive value }(\mathrm{PPV})=\text { Precision } & =\frac{\mathrm{TP}}{\mathrm{TP}+\mathrm{FP}} \\
\text { False Discovery Rate }(\mathrm{FDR}) & =1-\mathrm{PPV} \\
\text { F1 Score } & =2 \times \frac{\text { PPV } \times \text { Sensitivity }}{\text { PPV }+ \text { Sensitivity }}
\end{aligned}
$$

- Sensitivity, also known as recall or the true positive rate, is a measure used to evaluate the performance of a classification model. It is defined as the proportion of actual positives (e.g., diseases, positive cases) that are correctly identified by the model.
- Specificity, also referred to as the true negative rate, serves as a metric to assess the precision of a classification model, especially in its ability to precisely identify negative instances. It represents the ratio of actual negatives (for example, cases where a condition is not present) that the model correctly recognises as such.
- Accuracy is a measure used in a confusion matrix to evaluate the overall performance of a classification model. It is defined as the proportion of correct predictions (both positive and negative) made by the model out of all predictions. In essence, the accuracy assesses how often the model makes the correct decision for both positive and negative instances.
- The F1 score is a metric used within a confusion matrix to gauge the balance between precision and sensitivity (recall) in a classification model. It harmonises both measures into a single metric by calculating their harmonic mean. Essentially, the F1 score provides insights into the model's accuracy in predicting positive instances while considering both false positives and false negatives.
Two other metrics that are commonly used in the context of diagnostic testing are the positive predictive value (PPV) and the negative predictive value (NPV).
- The positive predictive value (PPV), or precision, is a statistical measure that quantifies the proportion of patients or test subjects who are correctly identified as having a condition (true positives) out of all of those who test positive for the condition, whether correctly or not (true positives and false positives). It reflects the likelihood that a positive test result accurately indicates the presence of the disease or condition in question. The PPV is crucial in evaluating the effectiveness of diagnostic tests, particularly in determining their reliability in correctly diagnosing patients within specific populations or under certain conditions.

$$
\text { Precision or } \mathrm{PPV}=\frac{\mathrm{TP}}{\mathrm{TP}+\mathrm{FP}}
$$

- The negative predictive value (NPV) represents the proportion of individuals who test negative for a condition and are correctly identified as not having the condition (true negatives), out of all of those who receive a negative test result (both true negatives and false negatives). It is an essential measure in assessing the accuracy of diagnostic tests, indicating the probability that a negative test result genuinely reflects the absence of the disease or condition. The NPV is particularly important in confirming the efficacy of diagnostic procedures in ruling out diseases in patients.

$$
\mathrm{NPV}=\frac{\mathrm{TN}}{\mathrm{TN}+\mathrm{FN}}
$$

In some cases, in addition to detecting the types of errors produced by the model, the test must meet high sensitivity and specificity requirements. In this regard, it is useful to take measurements of the receiver operating characteristic curve (ROC) [32], graphically observing the relationship between the two measurements. The area under the curve (AUC) provides a good measure of how well the BN model or classifier works. The closer to unity the area is, the more closely the model or classifier will conform to an ideal model or classifier ( $100 \%$ true positives and $0 \%$ false positives).


# 1.2. Bayesian Networks in the Health Sciences 

Since their creation, BNs have been linked to medical research, as probabilistic graphs are well suited to solving clinical problems. Understanding the causal relationships that lead to physiological processes is a challenge in clinical procedures; moreover, the health sciences frequently require reasoning through difficult problems under conditions of uncertainty.

Table 1. A confusion matrix example comparing a screening test against the gold standard. A confusion matrix illustrating the classification outcomes of the model. The matrix categorises the predictions into four fundamental types: true positives (TP), where the model correctly predicts the positive class; false positives (FP), where the model incorrectly predicts the negative class as positive; true negatives (TN), where the model correctly predicts the negative class; and false negatives (FN), where the model incorrectly predicts the positive class as negative. $N$ is the total number of analysed patients.


Probabilistic diagnosis has gained popularity in the medical literature in recent decades. According to [33,34], Bayesian methods began to be adopted in diagnostic procedures in the USA and the UK during the 1960s. These diagnoses used frequentist probabilistic methods to select variables that included possible diagnoses, as well as several variables that typically corresponded to symptoms. In the 1980s, some authors [35,36] described the development of Bayesian Networks (BNs) and influence diagrams in the medical field, from their definition to the construction of algorithms for the efficient processing of certainty.

In applying probabilistic graph models, researchers encounter uncertainty and inaccuracy due to three main reasons: randomness, a lack of precision in data collection, and model flaws. In clinical procedures, this manifests as incomplete clinical histories, subjective components presented by physicians or patients, and inaccuracies in measurements [37].

Two approaches are taken into account when building BNs: starting from a data set, through the application of techniques from network learning; or with the help of experts, where health professionals transfer their experience to include variables with cause-andeffect relationships in the model. The two approaches can be mixed by creating models using learning techniques, removing and imposing relationships based on personal criteria.

The first approach is the fastest way to build Bayesian networks in medicine, provided that the number of observations is sufficiently large. However, it has drawbacks: each observation often includes only a few measurements in addition to the diagnosis. These variables may not be sufficient to determine their conditional independence, and they might not contribute to the health professional's diagnosis.

In line with the above, there is usually an expert opinion on the model. The construction of BNs based on personal judgement can be divided into two stages: in the first, qualitative data are collected, clinically relevant variables are identified, and their relationships are used to build causal networks. In the second stage, quantitative information is collected: prior, conditional, and marginal probabilities.

Among specialists in statistics and information technology (the data scientist team), interest has been growing in the training of doctors so that they can appropriate the use of models. Accordingly, the BNs used in medicine could face challenges, such as the construction of algorithms that allow them to reduce the degree of difficulty in the growth of the BN [38].

Notably, probabilistic graph models are frequently used to forecast dependencies within a genetic test [7]. In parallel, Correa et al. [39] have developed BNs that explain assimilation networks by the modification and action exerted reciprocally between metabolites when analytical techniques such as Raman spectroscopy, liquid and gas chromatography, and Curie-point pyrolysis mass spectrometry data analysis require the examination

of a large number of features, including various mass spectra. The extensive number of features complicates the interpretation of the data. Consequently, the data analysis begins with dimensionality reduction, selecting a smaller subset of crucial masses for further analysis while discarding less significant ones. Then, they employ a feature selection process that integrates Bayesian network learning methods with genetic algorithms, facilitating the identification of bacterial spores and the classification of Bacillus species. Similarly, in the area of neurology, dependency modelling in cellular tissues has been widely applied by means of BNs [18].

# 1.3. Bayesian Networks in the Diagnosis and Prognosis of Diseases 

Medical diagnosis is often simplified to reasoning that entails the construction of hypotheses for each disease given the set of observed findings in a patient. The diagnosis results from choosing the most probable hypothesis for a set of observations [30]. Formally, it can be expressed by the equation

$$
\text { Diagnosis }=\max _{i} P\left(D_{i} \mid E\right)
$$

$P\left(D_{i} \mid E\right)$ is the probability of the disease $D_{i}$ given the evidence $E$, which represents the set of observed findings, including signs and symptoms, along with laboratory results (i.e., $P\left(D_{i} \mid E_{1}, E_{2}\right)=P($ flu $\mid$ fever and cough $)$ ).

In the medical field, prognosis aims to forecast the future condition of a patient by considering a combination of the observed symptoms and the treatment provided. Formally, it can be expressed by the equation

$$
\text { Prognosis }=P(O \mid E, T)
$$

Variable $E$ is the evidence, i.e., a set of observed findings, such as signs, symptoms, and laboratory results; $T$ represents a prescribed treatment for a patient; and the variable O is the outcome, which can represent, for example, life expectancy, the health status, or the spread of a disease.

Based on the information provided above, we are confident that the reader will be able to comprehend all of the articles that will be presented in the review of the diagnosis/prognosis literature.

## 2. Materials and Methods

The objective of this review is to comprehensively examine and synthesize the existing research on Bayesian networks (BNs) and their applications within the medical field, with a particular focus on their roles in disease diagnosis and prognosis.

### 2.1. Registration Statement

This review has been registered with PROSPERO, the international prospective register of systematic reviews. The registration details can be accessed through the PROSPERO database under the registration number 535260. The review protocol was registered before the start of the literature search to ensure transparency and reduce the risk of reporting bias. The protocol outlines the methods for the selection of the literature, data extraction, analysis, and the specific criteria used to assess the application of Bayesian networks in diagnosis and prognosis in the health sciences. The aim of this review is to synthesise the existing studies and provide a comprehensive evaluation of the effectiveness and accuracy of Bayesian networks in clinical settings.

### 2.2. PRISMA Statement

This review was conducted in accordance with the Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) guidelines. The methods of the literature search, selection, and data synthesis were structured to ensure the comprehensive coverage and unbiased analysis of studies involving Bayesian networks for diagnosis and prognosis

in the health sciences. A PRISMA flow diagram has been included to illustrate the search process and selection of studies (Figure 4). Additionally, the PRISMA checklist has been completed and is available in the Supplementary Materials to this article, providing detailed information on the adherence to these guidelines throughout the review process.
![img-3.jpeg](img-3.jpeg)

Figure 4. PRISMA flow chart for the review process of BNs in the diagnosis and prognosis field.

# 2.3. Data Sources 

Web of Science, Scopus, ProQuest Central, Google Scholar, and PubMed Central were searched for published articles containing the following keywords: Bayesian networks, disease prediction, medical diagnosis, applications in medicine, prognosis of disease. The search strategies implemented in this study were constructed utilising predefined keywords and aligning them with the pertinent descriptors of the chosen databases. The searches covered the literature from 1983 to the present to ensure the exhaustive inclusion of pertinent studies throughout this extensive timeframe. This methodology was designed to enable an in-depth review of the existing body of knowledge, thereby facilitating a nuanced understanding of the advancements and discoveries in the field.

MeSH terms: Medical Informatics, Decision Making, Computer-Assisted and Diagnosis, Computer-Assisted and Prognosis.

### 2.4. Data Extraction

The search period was from 1983 to 2023. The references of the included articles were hand-searched to identify additional relevant records based on the title, abstract, and full text.

### 2.5. Synthesis

The included studies were classified according to their main focus: (1) BNs, (2) the application of BNs in the health sciences, and (3) applications of BNs in the diagnosis and/or prognosis of diseases. Groupings were defined based on the data.

Among the publications considered for this scoping review, two fundamental aspects were sought: the first was that the disease was relatively common and that the variables involved in the diagnosis and/or prognosis were included, along with the directed acyclic graph (DAG) corresponding to the Bayesian network, or at least an indication that it had been used in the search for causality leading to the diagnosis; the second was that some measure of precision was provided. This second requirement was relaxed if the article was considered to provide sufficient information about the system, as in the case of [40], since it was a web-based decision-making system.

# 3. Results 

The searches yielded a total of 190 records, and, following the screening process, 60 articles focusing on BNs applied to medicine for diagnosis and prognosis were finally included in the review (Figure 4). Among the excluded studies, after close reading, seven articles were found that did not use BNs, fifteen considered BNs but did not include any examples or references to disease diagnosis or prognosis, and eight did not provide any measure ('non-measure') of the accuracy of the network.

Many models of BNs have been developed for medical diagnosis. They can be built using data, knowledge, the medical literature, ontologies, other sources of medical evidence, or a combination of these. For example, Moreira et al. [41] presented a Bayesian network model for the diagnosis of dementia, constructed based on expert knowledge. Seixas et al. [42] compared multiple models of BNs (developed from knowledge and data) with other classifiers fully learned from data to diagnose Alzheimer's, dementia, and mild cognitive impairment. For each of these conditions, the performance of the knowledgebased BN models, with AUC values of $0.86,0.96$, and 0.97 , respectively, was comparable to that of the best data-based classifier, with AUCs of $0.90,0.98$, and 0.97 , respectively. In contrast, Yin et al. [43] analysed the data to identify the most important variables and then trained a BN to diagnose Alzheimer's based on this information. Sa-Ngamuang et al. [44] presented a BN model to differentiate dengue from other acute febrile illnesses, combining expert knowledge, published evidence, and data. Farmer et al. [45] constructed a BN for the diagnosis of musculoskeletal disorders of the shoulder, using expert knowledge and the medical literature, along with retrospective data. The expert analysis was performed in two stages and an initial model was updated following a review by a panel of orthopaedic specialists. Refai et al. (2016) [46] proposed a maintenance strategy for Bayesian networks (BNs) that involves implementing policies to update a fixed structure and considering its reorganisation by defining additional variables, known as maintenance actions. These actions could involve adding or deleting variables and editing their values.

Some authors have suggested extracting medical knowledge from dictionaries or medical ontologies. Bucci et al. [47] built a two-level BN model for diagnosis that automatically extracted medical knowledge from an ontology; the diagnostic part was supplemented by a decision network to evaluate the available tests using utility values specified by a clinician. In Zhang et al. [48], several models, including a BN model, were automatically developed to diagnose mild cognitive impairment using a combination of approaches, including insights drawn from the SNOMED ontology. Shen et al. [49] explored the construction of a clinical BN for the probabilistic inference of medical ontology based on electronic medical records. By evaluating the learned topology against the opinions of expert clinicians and entropy calculations, and by calculating the diagnostic classification based on ontology, the study demonstrated that the direct and automated construction of a high-quality health topology and ontology is feasible using medical records.

Verduijn et al. [50] presented a BN that implements process-oriented and dynamic vision for forecasting. The procedure optimises the prediction of the results and accounts for patient dropout at an early stage. The paper describes how prognostic BNs can be applied to solve a series of information problems related to medical prognosis.

Other studies have used only data to build BN models. For example, Moreira and Namen [41] combined structured data with information extracted from medical notes (i.e.,

text) to build a BN model for the diagnosis of dementia. In another study, Somnay et al. [51] trained four data-based classifier models (rules, logistic regression, trees, and bay networks) to recognize primary hyperparathyroidism.

# Comprehensive Review of Bayesian Networks on Some Diseases 

Velikova et al. [52] presented the decomposition of a BN to model the detection of breast cancer, demonstrating some advantages of the method: the natural and more intuitive representation of breast abnormalities and their characteristics; the compact representation and efficient manipulation of large conditional probability tables; and a possible improvement in the processes of knowledge acquisition and representation.

The effectiveness of seven BN classifiers as potential tools for the diagnosis of breast cancer was evaluated by Cruz-Ramirez et al. [53] using two real-world databases containing fine needle aspirates of breast lesions, which were collected by a single and multiple observers, respectively. A certain element of subjectivity in the data was shown by the results: mean accuracy of $93.0 \%$ was shown in the single-observer data set, compared to $83.3 \%$ for the multiple-observer data set. The findings suggest that different aspects are identified by observers when examining samples under a microscope, a situation that significantly decreases the performance of these classifiers in the diagnosis of such a disease.

Elazmeh et al. [54] built a reliable BN model for the early assessment of emergency paediatric asthma exacerbation. Their predictive model was capable of distinguishing between patients with mild or moderate/severe asthma attacks at a medically acceptable level of performance.

Thermography was used by Yaneli et al. [55] for the pre-diagnosis of breast cancer, based on the predictive value of its attributes. A database of 98 patients was included in the BN used. It was suggested by the results that these attributes were not sufficient to produce good results in the pre-diagnosis of breast cancer. Unexpected interactions between thermographic attributes, especially those directly related to the class variable, were shown by the models. BNs were used by Djebbar and Merouani [56] to model case-based reasoning and apply it to the diagnosis of liver disease. It was found that the BN was an excellent tool for the modelling of uncertainty in terms of its clear graphical representation and the laws of conditional probability based on the similarity function, and the BN was useful in selecting the most similar cases as the recovery phase and optimising it. Two exact inference algorithms, JLO and Pearl, were used to calculate the conditional probabilities in order to improve the performance of case-based reasoning.

Park et al. [57] built a prognostic model for metabolic syndrome using BNs with an evolutionary optimisation ordering approach. This proposed model outperformed the conventional BN model and other neural network models.

Vila-Francés et al. [1] presented a decision-making support plan, using a BN to predict the probability of having unstable angina based on clinical data. The final model was implemented as a web application, which is currently being validated by clinical specialists. Seixas et al. [42] proposed a BN detection model for the early detection of Alzheimer's disease, dementia, and mild cognitive impairment. The parameters of this structure, built by experts in this field, were estimated using learning algorithms from a real-world data set. The proposed BN showed better accuracy in diagnosing Alzheimer's, dementia, and mild cognitive impairment compared to most other known classifiers. In addition, it provided additional useful information to clinicians, such as the contribution of certain factors to the diagnosis. Zhou et al. [40] described the development of BiotinNet, an Internet-based program that uses BNs to integrate published data on various aspects of biotin metabolism. Users can provide a combination of values for biotin-related metabolite levels to obtain predictions for other metabolites that are not specified. This system can help researchers to design future experiments while enabling the continuous incorporation of new data.

Sesen et al. [58] assessed the feasibility of BNs in providing accurate and personalized survival estimates and treatment selection recommendations in lung cancer care using the Lung Cancer Database (LUCADA).

Wang et al. [59] proposed a BN model to describe and predict the occurrence of brain metastases from lung cancer, which outperformed the naive Bayes, logistic regression, and support vector machine models in terms of the average sampled sensitivity. Furthermore, the proposed BN had advantages over the other approaches in interpreting how brain metastases develop from lung cancer.

Cai et al. [60] combined BNs with importance measures to identify key factors that have significant effects on the survival times of patients with hepatocellular carcinoma after hepatectomy. The accuracy of the BN model was $67.2 \%$. The true positive rate (TPR) of the model was $83.22 \%$, and the false positive rate (FPR) was $48.67 \%$.

Kaewprag et al. [61] developed a BN-based predictive model that enabled clinicians to better understand and explore clinical patient data along with risk factors for pressure ulcers in intensive care unit patients based on electronic medical records. The BN model increased the sensitivity of the prediction compared to logistic regression models, without sacrificing the overall accuracy.

Takenaka et al. [62] used a BN to predict the postoperative clinical recovery from foot drop attributable to lumbar degenerative diseases. The results obtained suggest that the clinician can intuitively understand the layered correlations between the predictors of the BN models, which successfully provide probability estimates of the post-tibial anterior muscle strength to inform treatment.

Spyroglou et al. [63] examined the performance of BN classifiers in predicting asthma exacerbation based on various patient parameters, including objective measurements and medical history data. The proposed semi-naive network classifier was able to predict whether a patient would experience disease exacerbation after the last evaluation with accuracy of $93.8 \%$ and sensitivity of $90.9 \%$. In addition, the resulting structure and conditional probability tables gave a clear view of the probabilistic relationships between the factors. This network could help clinicians to identify patients at high risk of exacerbation after stopping medication and confirm which factors are the most important.

Agrahari et al. [64] presented a method based on the analysis of BNs to classify two types of hematological malignancies: acute myeloid leukemia and myelodysplastic syndrome. The BN classifier showed accuracy of $93 \%$ and precision of $98 \%$, surpassing the results achieved by other investigators on the same data set.

More recently, several studies have incorporated Bayesian networks as a component of their methodologies, often in conjunction with artificial neural networks or other machine learning tools. Evidence from these studies is presented below, fulfilling the criteria for the selection of the sample of studies.

Cao et al. [65] compared Bayesian networks (BNs), convolutional neural networks, and multivariate logistic regression in predicting the long-term postoperative health status. The BN demonstrated an excellent predictive capacity for type 2 diabetes and dyslipidaemia (AUC 0.94 and 0.92 , respectively), a good capacity for hypertension and sleep apnoea syndrome (AUC 0.89 and 0.83 , respectively), and a fair capacity for depression (AUC 0.75). The study showed that BNs are useful tools in predicting the long-term health status and comorbidities in patients after bariatric surgery.

Siga et al. [66] proposed a BN model to predict all-cause mortality in haemodialysis patients. The model presented an AUC of 0.78 (standard deviation [SD] 0.01); a true positive rate (sensitivity) of $72 \%$ (SD 2\%); a true negative rate (specificity) of $69 \%$ (SD 2\%); a positive predictive value (PPV) of $70 \%$ (SD 1\%); and a negative predictive value (NPV) of $71 \%$ (SD $2 \%)$. The BN provided the most reliable prediction when comparing the results with those acquired by logistic regression.

A BN model was developed by Wu et al. [67] to guide individually targeted antibiotic therapy at the point of care by predicting the most likely causative pathogen in children with osteomyelitis and the antibiotic with the optimal expected utility. The complex relationship between the unobserved infectious pathogen, observed culture results, and clinical and demographic variables was explicitly modelled by the BN, integrating data with critical expert knowledge with the framework of causal inference.

Prochazka et al. [68] presented BN modelling as a tool to predict early disease progression in patients with follicular lymphoma. This study showed that the BN model had better prognostic power than multivariable logistic regression in terms of predicting the disease within 24 months of first-line immunochemotherapy (POD24). Unlike the logistic regression model, BNs allowed the visualisation of the complex relationships between the predictors and the individualised prediction of the risk associated with POD24, even if some of the predictors were unknown.

Finally, a BN-based approach to predict important clinical indicators to improve treatment for COVID-19-related pneumonia was developed by Derevitskii et al. [69]. Using expert knowledge, the current clinical recommendations, previous research, and classic predictive metrics, the models were validated. Following the validation of other COVID-19related pneumonia data sets for other hospitals, the proposed models can be utilised within decision-making support systems to enhance the treatment of COVID-19 pneumonia.

The multivariable probabilistic associations between the CVD risk and metabolic health, alongside the obesity status, and the potential elements influencing these relationships among Chinese adults were illustrated by Tian et al. [70]. It was concluded by the authors that network modelling is beneficial in amalgamating expert knowledge and observational data, facilitating the straightforward recognition of the probabilistic dependencies and conditional independence among variables via graphical representation.

Lee et al. [71] proposed a BN model to identify actionable factors contributing to racial differences in the breast cancer stage at diagnosis. They employed diverse Bayesian model evaluation tools to assess these two hidden pathways, as well as each of the four observed variables, in elucidating racial disparities in the stage at diagnosis.

Wu et al. [72] presented an insight-based BN modelling approach to diagnose rheumatoid arthritis. The authors explained that the Bayesian network models exhibited strong predictive abilities in forecasting osteoporosis in postmenopausal women. Moreover, these networks provided a more intuitive representation of the complex interplay of the risk mechanisms between diseases and various factors. Another study with a similar methodology examined the bone mineral density using multiple linear regression and a Bayesian network model [73].

To summarise the most significant results, we present them in Table 2, to provide the reader with a comparative analysis of the various studies based on their characteristics.

Table 2. Summary of selected studies on BNs, including medical application, type of BN used, numerical level of performance, and most salient study findings. The BN performance measures are as follows: accuracy measured between 0 -inaccurate system and 1 -highly accurate system; and AUC measured between 0 -inaccurate predictions and 1 -highly accurate prediction system.


Table 2. Cont.


# 4. Discussion 

Bayesian networks (BNs) are highly valuable tools in the health sciences, providing substantial support to medical professionals with satisfactory accuracy. This section discusses the outcomes achieved by BNs in the diagnosis and prognosis of diseases, emphasising the pertinent considerations, benefits, and limitations. BNs have demonstrated efficacy in identifying causal genetic biomarkers across a wide array of diseases, with precision that rivals that of expert clinician assessments and entropy calculations. Moreover, these networks have facilitated the development of ontology-based diagnostic classifications, enabling the automated construction of high-quality health topologies and ontologies directly from medical records.

An important part of the research on disease diagnosis systems using Bayesian networks employs dynamic retraining, where new diagnoses are incorporated as new data, leading to the re-calibration of the network [9,40,42]. This approach improves the robustness and reliability through elicitation and expert learning phases. The prototype clinical decision support system for diagnosis has demonstrated high validity and reliability. However, it has also identified several areas that require further research before clinical application can be considered.

Moreover, BNs can diagnose diseases with minimal human intervention, even in mild cases, and their integration into electronic medical record systems could aid in recognising underdiagnosed disorders. Djebbar et al.'s findings demonstrate that combining BNs with case-based reasoning enhances the efficiency of case retrieval in liver disease diagnosis [56].

A web-based medical decision support system optimised to maximise the negative predictive value (NPV) showed potential in reducing undetected risk cases in emergency room patients with nonspecific chest pain at risk of a heart attack. The quantification of the uncertainty in predictions is as critical as the prediction itself, indicating a need for further experimentation on unmeasured metabolites [1].

Furthermore, BN classifiers provide advantages over traditional clinical prediction methods by using multiple symptom-related factors simultaneously [63]. However, a significant limitation is their assumption of attribute independence, which may not hold in conditions like asthma, where symptom interactions can occur.

In summary, while BNs offer considerable promise in enhancing disease prediction and understanding, their effectiveness depends on robust data collection and the ability to update the predictions as new data become available. Despite some limitations, their flexibility in handling incomplete information and the dynamic nature of their forecasting make BNs a powerful tool in medical decision-making.

# 5. Conclusions 

This scoping review encompasses 60 articles, demonstrating that Bayesian networks (BNs) achieve high levels of accuracy in diagnosing and forecasting diseases. While recent advancements in machine learning may offer slight improvements in accuracy, the use of directed acyclic graphs (DAGs) in BNs significantly aids in understanding the results and studying causality, capabilities not offered by other classification methods. The increase in publications regarding BN development- 54 articles identified on PubMed and over 90 on Web of Science in 2023 alone-suggests their growing importance in clinical procedures.

BNs are particularly effective in modelling complex medical issues that require reasoning under uncertainty. The extensive literature and ongoing research into medical BNs reflect the significant interest in their application for medical diagnosis. BNs offer a versatile model that can evaluate, predict, diagnose, and optimise decisions, enhancing the effectiveness of BN construction efforts and the quality of the available software solutions [9]. As expert support systems, BNs provide a powerful tool for medical decision-making. They utilise a knowledge representation methodology to express variable relationships, employing probability theory to manage medical uncertainty and making the decision process comprehensible to non-specialists.

Looking forward, the development of advanced preprocessing methods and alternative learning strategies is crucial. Additionally, the establishment of more publicly accessible databases should be prioritised to enhance the training of Bayesian networks. Integration with electronic health records (EHRs) and interoperability with existing healthcare IT systems could further enhance the utility of BNs, enabling real-time updates and more personalised patient care.

Moreover, BNs facilitate a more intuitive understanding of complex medical data, which can be particularly valuable in multidisciplinary healthcare teams, where not all members may have advanced data science training. Their ability to incorporate expert knowledge into the model structure makes them highly adaptable to various medical contexts and conditions, from rare diseases to common chronic illnesses.

Given these considerations and the rapid advancements in artificial intelligence over the past 2-3 years, continuous research in Bayesian networks is indispensable. Similar to other machine learning techniques, BNs achieve comparable or superior results in disease diagnosis and prognosis. The notable precision of these intelligent systems supports healthcare professionals by enabling quicker, more certain decisions, whether based on imaging or clinical data, across a wide range of pathologies. Furthermore, the transparency and interpretability of BN models can improve the trust and adoption among healthcare practitioners, ultimately enhancing patient outcomes and advancing personalised medicine.

In conclusion, the continuous evolution of Bayesian networks, coupled with increasing computational power and more sophisticated algorithms, positions BNs as a cornerstone technology for future advancements in medical diagnostics and prognostics. Their integration into clinical workflows promises to elevate the standard of care, making healthcare delivery more efficient, accurate, and patient-centred.

Supplementary Materials: The following supporting information can be downloaded at: https://www. mdpi.com/article/10.3390/make6020058/s1. Reference [74] is cited in the supplementary materials.

Author Contributions: Conceptualisation, X.B. and A.R.; methodology. C.S.M.-V. and K.P.; investigation, C.S.M.-V. and K.P., formal analysis: C.S.M.-V., K.P., D.O.-B. and J.A.Q.-R.; writing—original draft preparation, C.S.M.-V. and K.P.; writing—review and editing, X.B.; supervision, X.B., A.R. and D.O.-B.; project administration, X.B. and D.O.-B.; funding acquisition, X.B. and D.O.-B. All authors have read and agreed to the published version of the manuscript.

Funding: This paper is part of the project PID2022-136455NB-I00, funded by the Ministerio de Ciencia, Innovación y Universidades of Spain (MCIN/AEI/10.13039/501100011033/FEDER, UE) and the European Regional Development Fund. and ILISABIO 2023 Modalidad de PROYECTOS DE INNOVACIÓN-ILISABIO23-PI03, funded by Universidad Miguel Hernández de Elche-Vicerrectorado de Planificación y responsabilidad Social.

Conflicts of Interest: The authors declare no conflicts of interest. The funders had no role in the design of the study; in the collection, analyses, or interpretation of data; in the writing of the manuscript; or in the decision to publish the results.

# Abbreviations 

The following abbreviations are used in this manuscript:

