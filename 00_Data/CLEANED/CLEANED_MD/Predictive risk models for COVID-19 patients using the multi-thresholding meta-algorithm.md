# scientific reports

## OPEN

Predictive risk models for COVID-19 patients using the multithresholding meta-algorithm Rosario Delgado ${ }^{1,2,3}$, Francisco Fernández-Peláez ${ }^{2}$, Natàlia Pallarés ${ }^{3,15}$, Vicens Diaz-Brito ${ }^{5}$, Elisenda Izquierdo ${ }^{6}$, Isabel Oriol ${ }^{4,7,8}$, Antonella Simonetti ${ }^{3,13,14}$, Cristian Tebé ${ }^{3,4}$, Sebastià Videla ${ }^{10,11}$ \& Jordi Carratalà ${ }^{4,7,12,13}$ This study aims to develop a Machine Learning model to assess the risks faced by COVID-19 patients in a hospital setting, focusing specifically on predicting the complications leading to Intensive Care Unit (ICU) admission or mortality, which are minority classes compared to the majority class of discharged patients. We operate within a multiclass framework comprising three distinct classes, and address the challenge of dataset imbalance, a common source of model bias. To effectively manage this, we introduce the Multi-Thresholding meta-algorithm (MTh), an innovative output-level methodology that extends traditional thresholding from binary to multiclass classification. This methodology dynamically adjusts class probabilities using misclassification costs, making it highly effective in imbalanced datasets. Our approach is further enhanced by integrating the simplicity, transparency, and effectiveness of Bayesian networks to create a robust predictive model. Using patient admission data, the model accurately identifies key risk and protective factors for COVID-19 outcomes. Our findings indicate that certain patient characteristics, such as high Charlson Index and pre-existing conditions, significantly influence the risk of ICU admission and mortality. Moreover, we introduce an explanatory model that elucidates the interrelationships among these factors, demonstrating the influence of therapeutic limits on the overall risk assessment of COVID-19 patients. Overall, our research provides a significant contribution to the field of Machine Learning by offering a novel solution for multiclass classification in the context of imbalanced datasets. This model not only enhances predictive accuracy but also supports critical decision-making processes in healthcare, potentially improving patient outcomes and optimizing clinical resource allocation.

Keywords COVID-19 patient risks assessment, Cost-sensitive Machine Learning modelling, Bayesian Networks, Multiclass classification thresholding, Healthcare decision-making


[^0] [^0]: ${ }^{1}$ Department of Mathematics, Universitat Autònoma de Barcelona, Barcelona, Spain. ${ }^{2}$ Applied Artificial Intelligence Unit, Eurecat, Barcelona, Spain. ${ }^{3}$ Biostatistics Unit of the Bellvitge Biomedical Research Institute (IDIBELL), Barcelona, Spain. ${ }^{4}$ Department of Clinical Sciences, School of Medicine and Health Sciences, University of Barcelona, Barcelona, Spain. ${ }^{5}$ Department of Infectious Diseases, Parc Sanitari S. Joan de Deu, Sant Boi de Llobregat, Barcelona, Spain. ${ }^{6}$ Department of Anaesthesiology, Viladecans Hospital, Barcelona, Spain. ${ }^{7}$ Bellvitge Biomedical Research Institute, Barcelona, Spain. ${ }^{8}$ Unitat Malalties Infeccioses, Servei Medicina Interna, Consorci Sanitari Integral, Barcelona, Spain. ${ }^{9}$ Àrea de Recerca, Consorci Sanitari Alt Penedès Garraf, Barcelona, Spain. ${ }^{10}$ Department of Clinical Pharmacology, Bellvitge University Hospital, Barcelona, Spain. ${ }^{11}$ Department of Pathology and Exp. Therapeutics, School Medicine and Health Sci., University of Barcelona, Barcelona, Spain. ${ }^{12}$ Department of Infetious Diseases, Bellvitge University Hospital, Barcelona, Spain. ${ }^{13}$ CIBERINFEC, Instituto de Salud Carlos III, Sevilla, Spain. ${ }^{14}$ Infectious Disease Unit, Hospital de la Santa Creu i Sant Pau, Barcelona, Spain. ${ }^{15}$ Department of Basic Clinical Practice, School of Medicine and Health Sciences, University of Barcelona, Barcelona, Spain. ${ }^{16}$ email: Rosario.Delgado@uab.cat


Wilcoxon signed-rank test p-value adjusted p-values

## FWER

Type I error
Holm-Bonferroni method
Box plot
Heatmap
Odds
Odds Ratio (OR)
Priori probability
Posteriori probability
Sensitivity analysis

Non-parametric statistical test to compare the medians of paired observations. Does not assume normality
A measure used in statistical hypothesis testing to determine the strength of the evidence against the null hypothesis: the probability of observing the test statistic or a more extreme value, if the null hypothesis is true
A method for controlling the family-wise error rate (FWER) when performing multiple hypothesis tests
Family-wise error rate: the probability of making one or more Type I error among all the hypotheses tested
The incorrect rejection of the null hypothesis when it is actually true
A more powerful alternative to the traditional Bonferroni correction to adjust the p-values and control the FWER
Graphical representation to summarize the distribution of a sample: median, quartiles, and outliers
Graphical representation: individual values are displayed in a matrix format, with colors representing magnitudes
The ratio of the probability of an event occurring to the probability of it not occurring
The ratio of the odds of an event occurring in one group compared to another group
Probability of an event or outcome occurring before observing any data or experimental result
Probability of an event or outcome occurring given known information or evidence
A technique to study how the variation in the output of a model can be attributed to variations in its inputs

The COVID-19 pandemic, which began in December 2019 ${ }^{1}$, has had a profound global impact, resulting in millions of cases and fatalities worldwide. Although vaccines have slowed the rate of new infections, ongoing concerns about potential new waves and other health crises persist. In this context, advanced predictive models have become essential for improving clinical decision-making and patient care, particularly regarding hospital admissions for contagious diseases. Accurate risk assessment and timely interventions are crucial due to the rapid progression and variable severity of COVID-19. Advanced predictive models are needed to evaluate risks and optimize interventions based on individual patient profiles, ultimately improving patient outcomes and resource allocation.

Our study addresses these needs by introducing a novel Machine Learning (ML) methodology to construct predictive models specifically for COVID-19 patients for assessing ICU admission and death risks for COVID-19 patients admitted to the hospital. This model, which is a classifier, categorizes data points into predefined classes (icu, exitus and discharge) based on features such as demographics, vital signs, symptoms, comorbidities, and previous treatments available at hospital admission. The focus is on assessing the impact of therapeutic limits on ICU admission and death risks. To achieve this, we use a dataset comprising 3,362 SARS-CoV-2 infected patients admitted to hospitals in the south metropolitan area of Barcelona (Catalonia, Spain) between March and April $2020^{2}$. This dataset includes information on therapeutic limits, such as Non-Rebreather Mask (NRB) and Non-Invasive Mechanical Ventilation (NIMV). Therapeutic limits reflect critical decisions about the extent of medical interventions for COVID-19 patients based on factors such as age, physical activity, weight loss, and fatigue, which determine a patient's frailty level ${ }^{3}$. This inclusion allows to introduce ML methodology to address the impact of therapeutic limits on risk assessment for COVID-19 patients, which is a critical aspect of predictive modelling in healthcare. We evaluate the impact of therapeutic limits by dividing the patient cohort into two subsets: those with assigned therapeutic limits (NRB or NIMV) and those without, and constructing the ML predictive models for each data subset. Moreover, since the original number of variables is very high, we implement a feature selection process to manage the complexity of our large-scale dataset.

A key challenge in predictive modelling for COVID-19 is class imbalance within the dataset. For instance, the classes icu (10\%), exitus (17\%), and discharge (73\%) are significantly imbalanced, which is exacerbated when partitioning the dataset based on therapeutic limits, as detailed in Table 1. This imbalance can lead to model bias, where the classifier performs better on majority classes and poorly on minority classes. Some researchers have addressed multiclass imbalance by merging minority classes ${ }^{4}$, but this approach prevent for separate analysis of these classes.

To address this issue, our study employs a cost-sensitive classification approach. Traditional evaluation metrics like accuracy can be misleading in such scenarios, known as the accuracy's paradox. Focusing solely on


Table 1. Distribution of the "event" output variable within each data subset and across the entire dataset.

minimizing the error rate (or maximizing accuracy) during classifier learning and validation is not appropriate, as it assumes equal severity in classification errors, which does not make sense in this scenario. Our approach assigns different weights to classification errors based on their consequences, improving model performance on imbalanced datasets.

Cost-sensitive classification methods can be implemented at three levels: data, algorithm, and output. Data-level methods encompass techniques such as oversampling, relabelling, and instance weighting, before training a cost-insensitive classification algorithm. However, these methods have several drawbacks: time-consuming and computationally expensive; risk of overfitting, particularly with oversampling; inefficient handling of class overlap, which can result in poor discrimination between classes; and lack of adaptability to changes in class distributions or the introduction of new data inputs. Algorithm-level methods involve modifying the original learning algorithm to account for misclassification costs. Despite their potential, they also face several challenges: increased algorithm complexity in modifying it; limited flexibility, as this modifications are specific to each algorithm, reducing their general applicability; difficulties in fine-tuning to balance misclassification costs effectively.

In contrast, output-level techniques function as wrappers or meta-algorithms, improving classification algorithms by adjusting thresholds --a process commonly referred to as thresholding. These techniques focus on post-processing the classifier's output to transform any cost-insensitive probabilistic classifier into a costsensitive one without altering the underlying algorithm. The advantages of these methods include: simplicity and flexibility, allowing they to be applied to any probabilistic classifier without requiring changes to the data or the underlying algorithm, thereby reducing the risk of overfitting; easy dynamic adaptation to variations in misclassification costs; transparency and interpretability, which are crucial in many fields, particularly in healthcare; scalability and computational efficiency, as they do not require extensive preprocessing or algorithm modifications.

Traditional thresholding methods, typically used for binary classification, fall short in multiclass scenarios. Overall, while thresholding can be a powerful tool for cost-sensitive classification, its application in multiclass scenarios is fraught with challenges that require careful consideration and often bespoke solutions. Some of these challenges are:Each class requires its own specific threshold based on the misclassification costs associated with it, but handling multiple thresholds at the same time is more complex. In addition, with more thresholds to tune, there is a greater risk of overfitting.Determine the appropriate thresholds for each class to minimize the overall misclassification cost is intricate, as it involves balancing the trade-offs between different misclassification error rates and costs.The threshold for one class can affect the performance of the other classes due to the inter-class dependencies, thus complicating the optimization process.Evaluating the performance is more complex due tot the variety of possible misclassifications. This requires more sophisticated evaluation metrics and analysis to accurately measure the impact of thresholding.Finding the optimal thresholds for each class can be computationally expensive.Interpreting the results of a thresholding approach in a multiclass setting can be challenging, making difficult for practitioners to understand and trust the model's predictions, especially in critical applications like healthcare. Our study introduces the Multi-Thresholding meta-algorithm (MTh), which dynamically adjusts label probabilities based on factors derived from the probability distribution and misclassification costs. Any instance is then classified with the label having the highest adjusted probability (following the MAP criterion), offering a more nuanced approach to handling minority classes without merging them. Figure 1 schematically illustrates this process. See Section 3.5 for detailed information on MTh and Algorithm 1 for pseudocode. Additionally, we discuss some key properties in Appendix D.

The MTh meta-algorithm enjoy the benefits of the output-level techniques, and in particular integrates with any probabilistic classifier, such as Naive Bayes (NB) or Support Vector Machines (SVM). In our experiments,

Fig. 1. Scheme illustrating the three levels (data, algorithm and output) at which the cost-sensitive approach can be applied in classification.

we consider integrating MTh with various state-of-the-art models, including Neural Networks (NN), Support Vector Machine (SVM), and Random Forest (RF). This represents a significant advancement over traditional methods by extending thresholding from binary to multiclass classification settings.

On the other hand MTh does not suffer from the disadvantages of traditional thresholding methods when applied to multiclass classification that we have just discussed as it avoids the need to determine thresholds, which is the intrinsic source of the method's issues. Furthermore, in this context, the evaluation metric naturally associated with the cost-sensitive approach, Total Cost (TC), is perfectly appropriate and useful.

Our study also constructs different types of Bayesian Networks (BN) as explanatory or white-box models to elucidate variable interdependencies and the rationale behind risk assessments. We explore how these dependencies differ between patients with and without therapeutic limits, aiming to enhance more informed patient care decisions. It is worth noting that both the predictive and the explanatory models for the subpopulations of patients with and without therapeutic limits may, and indeed do, exhibit differences.

In summary, the key contributions of our research are as follows:Novelty of the MTh meta-algorithm: We introduce the MTh meta-algorithm, which extends traditional thresholding from binary to multiclass classification. MTh fills a critical gap in output-level methodologies for multiclass scenarios by employing a cost-sensitive approach to handle imbalanced datasets (see Figure 1). Unlike conventional algorithms that rely on static or less flexible thresholds, MTh dynamically adapts to different data subsets and scenarios, leading to more precise and finely-tuned predictions.Resolution of traditional thresholding issues: MTh circumvents the common issues associated with traditional thresholding methods applied to multiclass classification, such as the complex task of setting appropriate thresholds. By eliminating the need for these thresholds, MTh effectively addresses these challenges and utilizes the Total Cost metric, which aligns naturally with cost-sensitive classification. This approach is particularly well-suited for evaluating and optimizing predictions in imbalanced datasets.Application and impact: Our model effectively assesses ICU admission and death risks for COVID-19 patients, taking into account therapeutic limits. This capability provides valuable insights that enhance clinical decision-making and resource allocation, potentially improving patient outcomes.Integration and adaptability: The MTh meta-algorithm can be seamlessly integrated with any probabilistic classifier, including state-of-the-art models. This compatibility represents a significant advancement over traditional methods that may lack such flexibility, thereby enhancing the overall predictive modelling capabilities.Addressing class imbalance: By employing a cost-sensitive classification approach, our research tackles the issue of class imbalance, which is crucial for accurate risk prediction. This is reflected in the application of the MTh meta-algorithm for multiclass classification and the use of the Total Cost (TC) metric, both of which account for misclassification costs effectively.These contribution collectively advance predictive modelling in healthcare, offering valuable tools for managing patient risks and optimizing interventions.

The paper is structured as follows: Section 2 reviews related research. Section 3 details the materials and methods, including the dataset and preprocessing in Sections 3.1 and 3.2, respectively. Section 3.3 introduces Bayesian Networks used in our models. Section 3.4 covers validation and evaluation metrics. Section 3.5 presents the MTh meta-algorithm and its implementation, discussed further in Section 3.6. Results are presented in Section 4, followed by practical examples in Section 5. The paper concludes with final remarks in Section 6. Appendices A), B and C provide additional tables and figures, and Appendix D offers theoretical justification for the MTh meta-algorithm.

## Literature review

In this section, we provide a concise overview of relevant research related to the present study, covering various aspects of the topic. Overall, the intersection of COVID-19 research and ML techniques highlights a growing trend towards using advanced computational methods to enhance predictive capabilities and improve patient outcomes. This integrated approach underscores the evolving landscape of medical research, where traditional statistical methods and modern ML techniques complement each other to address complex health challenges.

Numerous research studies have explored COVID-19 using various statistical and ML methodologies to understand and predict different aspects of the disease. Early studies primarily focused on epidemiological aspects and potential risk factors. For instance, research has examined significant associations such as the link between blood type and disease severity^{5}, and the connection between myocardial injury and disease prognosis among hospitalized patients^{6}. Some studies have gone further by constructing statistical models to predict disease risk. For example^{7}, uses a multivariate logistic regression model to predict the risk of death within 30 days for COVID-19 patients in emergency rooms. Similarly^{4}, used Cox regression analyses to identify factors associated with mortality in hospitalized COVID-19 patients, marking a significant advancement in pinpointing clinical and laboratory predictors of death.

The advent of ML has led to the development of advanced predictive models that go beyond traditional statistical approaches. ML techniques have enhanced various aspects of medical research and practice, becoming crucial in predicting patient outcomes and improving diagnostic accuracy in medicine. For instance, ML models have streamlined data analysis in intensive care units (ICUs), aiding in sepsis prediction and improving patient care allocation^{8}. Other applications include predicting survival in heart failure patients based on serum creatinine and ejection fraction^{10}. We are interested in the integration of ML into COVID-19 research for medical diagnostic. For example, deep convolutional neural networks have been used to detect COVID-19 from chest X-ray images^{11}, and more recently deep learning has been applied to identifying COVID-19 patients from computed tomography scans^{12}. Given their reputation as effective classification algorithms in various fields and

their white-box nature, which differentiates them from other state-of-the-art supervised ML techniques like neural networks, we focus on Bayesian Networks (BNs).

BNs represent probabilistic relationships among variables, combining principles from graph theory, probability theory, computer science, and statistics^{13}. They are versatile models of supervised learning that transparently illustrate the relationships between variables involved in a phenomenon, enabling both effective predictions and the generation of valuable knowledge. BNs have proved effective in various fields, including document classification, image processing, spam filters, speech recognition, robotics, semantic search, and operational risk assessment^{14}. They have even found application in criminal profiling, such as identifying forest arsonists^{15}or multi-victim homicides^{16}. In the medical field, BNs have been successfully used to predict outcomes in areas such as pancreatic cancer^{17}and ICU patients^{18,19}. During the COVID-19 pandemic, BNs demonstrated their utility in predicting infection likelihood and disease severity using mobile applications powered by Bluetooth technology^{20}. They have also been applied to predict COVID-19 outcomes based on symptoms^{21}, assess infection risk by ethnicity or religion^{22}, and predict qRT-PCR results^{23}. Furthermore, BNs have contributed to predicting COVID-19 pneumonia outcomes from chest computed tomography scans evaluated by independent radiologists^{24}.

While many techniques exist for handling binary classification problems, there is a lack of satisfactory solutions for multiclass classification in imbalanced datasets, both within and outside the context of cost-sensitive learning. Cost-sensitive learning, in general, addresses the challenge of classification when different misclassification costs are involved, which is a common scenario in medical datasets. Some works have considered this issue, by assigning weights to training examples, which is not very effective, for example, if some classes have significant overlap in the feature space. For instance^{25}, introduces a method for multiclass classification within this framework that employs an iterative scheme for example weighting combined with a binary classification algorithm. Meanwhile^{26}, discusses the rescaling approach, which aims to rebalance classes according to their costs by assigning weights to the training examples based on their class. Although this method proves to be effective in the binary case, it often falls short in the multiclass setting. In such situations, the authors recommend decomposing the multiclass classification problem into a series of two-class problems to achieve better results.

Handling imbalanced medical data in the field of cost-sensitive classification is a rapidly evolving research area in ML^{27,28}. At the data-level, SMOTE (Synthetic Minority Over-sampling TEchnique)^{29}have become a widely adopted oversampling method in medical diagnostics. Innovations include combining SMOTE with Tomek links to balance medical data^{30}, integrating SMOTE with edited nearest neighbor^{31}, and applying SMOTE along with modified particle swarm optimization^{32}. Alternative oversampling methods, such as BOSME (Bayesian network-based Over-Sampling MEthod), address SMOTE's limitations by accommodating non-continuous data^{33}.

Algorithm-level approaches for cost-sensitive classification, which involve modifying classification algorithms themselves, are less common but ther are some notable exceptions. These include cost-sensitive decision trees integrating game theory principles^{34}, incorporating feature ranking capabilities into a cost sensitive ensemble for classifying chronic kidney disease^{35}, and cost-sensitive variants of XGBoost applied to datasets related to breast cancer detection^{36}. Additionally^{37}, provides a comprehensive list of cost-sensitive learning algorithms that modify loss functions to prioritize minority classes.

Finally, output-level adjustments, such as various binary thresholding methods, have been explored to improve cost-sensitive classification performance. Examples include MetaCost(^{38}), which employs bagging in decision trees to generate accurate probability estimates, CostSensitiveClassifier (^{39}), Cost-sensitive Naive Bayes^{40}, and Empirical Thresholding(^{28}), which focuses on improving probability estimate calibration.

## Materials and methods

### Dataset overview

The dataset utilized in this study was generously provided by the Bellvitge Biomedical Research Institute (IDIBELL). Due to the retrospective nature of this study and the use of anonymized data, informed consent was waived as authorized by the Ethics Committee of Bellvitge University Hospital. This committee ensures compliance with national data protection legislation, including Spain's Ley Orgánica 3/2018, de 5 de diciembre, de Protección de Datos Personales y garantía de los derechos digitales (LOPDGDD) (BOE number 294, December 6, 2018, pages 119788 to 119857), and the European Union's General Data Protection Regulation (Regulation EU 2016/679). The methodologies employed for data processing in this study, aimed at scientific research and statistical analysis, fully adhere to these regulations, ensuring the legality and protection of patient data.

The dataset encompasses a cohort of 3,362 patients admitted to five hospitals or hospital consortia in the southern metropolitan area of Barcelona (Catalonia, Spain) with confirmed SARS-CoV-2 infection. These healthcare institutions include the Consorci Sanitari de l'Alt Penedès i Garraf (402 cases), Consorci Sanitari Integral (895 cases), Parc Sanitari Sant Joan de Déu (538 cases), Hospital de Viladecans (404 cases), and Hospital Universitari de Bellvitge (1,123 cases). The patients were admitted between March 1, 2020, and April 30, 2020.

For each patient, we compiled a comprehensive set of characteristics, including demographic variables, comorbidities, and treatments administered since hospital admission. Initially, we dealt with a total of 1,012 variables (1,007 features and 5 output variables) distributed across 10 different files, which required extensive cleaning and preprocessing. This lead to a “large-scale” classification challenge due to the significant number of features, which can pose computational hurdles. To address this complexity, we applied a specific feature selection approach during the preprocessing phase (see Section 3.2 for more details). Regarding the output variables, we merged several into a single output variable called event. This variable signifies the patient's outcome and encompasses the values of discharge/icu/exitus, indicating whether the patient was discharged from the hospital without entering the ICU, admitted to the ICU, or passed away in the hospital without ICU admission.

Of noteworthy significance is the development of two distinct predictive models: one for patients with therapeutic limits and another for those without. This segregation is prompted by the expected differences in behaviour between these two patients subgroups, primarily due to their unique characteristics. One notable difference is the variation in the minority class labels for the output variable event. Among patients with therapeutic limits, the minority class label is icu (accounting for 2.66%), while for the remaining patients, it is exitus (representing 3.86%), as depicted in Table 1. A primary objective of this study is to compare these two patient populations, identifying distinctions both in terms of primary risk factors and their corresponding predictive models.

## Preprocessing

First, we adopted an expert-driven preprocessing approach to refine the dataset by eliminating redundant and irrelevant variables. Specifically, we excluded variables related to post-admission patient health status and information recorded before admission, as these were deemed nonessential for our research by medical experts. To streamline the dataset's efficiency and information content, we also merge related variables.

To facilitate the use of standard Bayesian Networks, it is imperative for all variables in the model to be of the factor type, which encompasses binary, categorical or discrete variables with a finite number of possible values. Consequently, we discretized continuous variables c-reactive protein, d-dimer, lactate, and lymphocytes into intervals based on the equal-frequency criterion, with slight adjustments to create more memorable or rounded intervals, provided these adjustments do not significantly imbalance them. This adjustment method maintains the integrity of the data distribution while making the intervals more intuitive and user-friendly. However, for variables age and O_{2} saturation, we determined categories based on domain expertise, following the guidelines provided by medical specialists to ensure the most relevant information was captured. Specifically, for O_{2} saturation, which is a percentage, the categorization is as follows: < 90 as “hypoxia”, [90, 95) as “low”, and ≥ 95 as “normal”. The values of the discrete variable Charlson index^{41}, which can take a finite but large number of possible values, were grouped into 5 categories using a binning method. The criterion for this binning was to ensure that the frequencies among the categories are relatively balanced. This approach helps to maintain a more even distribution across the categories, facilitating more robust analysis and interpretation.

Addressing missing data was another crucial aspect. Some variables within our dataset contained missing values, typically due to specific data unavailability for various reasons determined by the hospital's medical team. In response, we opted to remove certain variables with a substantial amount of missing data. For the remaining variables, instead of opting for imputation, we introduced a dummy category labeled “unknown” to account for missing values.

Considering the aforementioned points, after the initial feature selection phase, we streamline the number of input variables designated for constructing the predictive model. This not only reduces computational complexity but can also improve model performance in some cases. Traditional statistical-based feature selection methods involve assessing the relationship between each input variable and the output, selecting variables with the strongest associations. However, these methods rely on choosing an appropriate statistical measure to quantify the strength of these relationships, which can be challenging for any given dataset. Instead, we adopted the approach detailed in^{42}, which centers around the concept of the Markov blanket in a Bayesian Network. This approach has demonstrated remarkable efficiency in handling high-dimensional data, enabling the development of a sparse classifier that employs only a subset of the most informative features. This effectively reduces the problem's complexity and can lead to improved performance in both training and prediction, making it particularly advantageous for large-scale datasets. For a comprehensive breakdown of the characteristic set following this preprocessing, specific to each of the two data subsets (patients with and without therapeutic limits), please see Appendix A.

## Bayesian networks: a supervised ML tool

Bayesian Networks are probabilistic models that represent the relationships among variables influencing a particular phenomenon. For a given set of random variables, a Bayesian Network models their joint probability distribution. The graphical component of this model is a directed acyclic graph (DAG), where the nodes represent the random variables, and the directed arcs connecting these nodes indicate conditional dependencies (not necessarily causal) governed by the Markov condition. According to the Markov condition, each node in the DAG is independent of all other nodes that are not its descendants, given its parent nodes.

Bayesian inference involves updating the probabilities within the network based on observed evidence. This process requires calculating posterior probabilities using both the evidence and the prior probabilities. For predicting a query variable -in our case, the output variable “event”-, we employ the Maximum A Posteriori (MAP) criterion. This criterion selects the most probable instantiation of the event, with the corresponding probability termed the confidence level of the prediction.

In constructing both explanatory and predictive models for the variable event, we explore three types of Bayesian Networks: Naive Bayes, Augmented Naive Bayes and Tree Augmented Naive^{43}.Naive Bayes (NB): This is the simplest for of a Bayesian Network, assuming that all features are conditionally independent of each other given the value of the class variable “event”. Although this independence assumption may not always be valid, Naive Bayes has demonstrated good predictive performance in many scenarios. The DAG structure in NB is fixed, with directed edges originating from the class variable and pointing to each feature. Since the structure is predefined, no algorithm is required to learn it; however, the parameters are learned from the data using Maximum Likelihood Estimation (MLE). For that, we use the function bn.fit from the R package bnlearn(^{44}).

2. Augmented Naive Bayes (AN): This variant allows for additional directed edges between features, enabling both the structure (directed edges) and parameters to be learned from the data. The structure is determined using the function hc from the R package bnlearn, which implements a hill-climbing algorithm constrained by a whitelist that enforces directed edges from the class variable to the features. The Bayesian Information Criterion (BIC) score function is used to guide the structure learning process.
3. Tree Augmented Naive (TAN): TAN belongs to the One-Dependence Estimators (ODEs) family of models. It retains the simplicity of Naive Bayes while allowing for one additional dependency per feature. In TAN, in addition to the directed edges from the class variable to the features, each feature can also have a directed edge from at most one other feature. The TAN structure is learned using the tree.bayes function from the R package bnlearn, with parameters consistently estimated using the MLE method.For Bayesian inference with these Bayesian Networks, we use the R package gRain ${ }^{45}$. Figure 2 provides examples of DAGs corresponding to these three types, illustrating a class variable $C$ and five features, $X_{1}, \ldots, X_{5}$.

# Validation and performance evaluation 

To conduct the validation process and compare the different models, we employ a standard $K$-fold cross-validation with $K=10$. This approach ensures that the entire dataset is used for both training and validation across all $K$ iterations. The primary objective of cross-validation is to assess the model's ability to make predictions on new, unseen cases, thereby helping to detect issues such as overfitting. In this process, the dataset is randomly divided into $K$ roughly equal-sized folds. In each iteration, one fold is set aside for validation while the remaining folds are used to train the model. Upon completing the process, we generate $K$ confusion matrices for each classifier, from which we can compute the relevant performance metrics.

We denote the class labels as $\left\{c_{1}, \ldots, c_{r}\right\}$ and represent a general confusion matrix from the validation procedure as $\left(C_{i j}\right)_{i, j=1, \ldots, r}$. Here, $C_{i j}$ indicates the number of instances in the validation dataset that truly belong to class $c_{j}$ but are predicted by the classifier as class $c_{i}$. The total number of instances in the validation dataset is given by $N=\sum_{i=1}^{r} \sum_{j=1} C_{i j}$. While binary classification $(r=2)$ is most common, our class variable event comprises $r=3$ categories (discharge/exitus/icu), so we focus on the multiclass scenario.

In cost-insensitive classification, evaluation metrics do not account for the varying importance of different classification errors. The most common metric is accuracy, calculated as the proportion of correctly classified instances (i.e., accuracy $=\sum_{i=1}^{r} C_{i i} / N$ ). The error rate is the complement of accuracy, defined as the proportion of misclassified instances, i.e., error rate $=1-$ accuracy.

In classification tasks, particularly those involving imbalanced datasets, traditional accuracy may not be an adequate measure of model performance due to the risk of bias toward the majority class, a situation known as the accuracy paradox. Relying solely on accuracy (or error rate) can lead to selecting a poorly performing model. To address this issue, Balanced Accuracy (BA) is introduced. BA provides a more balanced evaluation by considering the performance across all classes equally, regardless of their proportions in the dataset. It is defined as the average of the true positive rates (TPR) for each class, offering a more comprehensive view of the model's ability to correctly classify instances from each class. This metric is particularly useful in cases where some classes are significantly underrepresented, ensuring that the model's performance is not overly influenced by the majority class. Mathematically, BA is expressed as:

$$
\mathrm{BA}=\frac{1}{r} \sum_{j=1}^{r} \frac{C_{j j}}{n_{j}}
$$

where $n_{j}=\sum_{i=1}^{r} C_{i j}$ is the total number of cases belonging to class $c_{j}$.
While BA provides a valuable metric by considering all classes equally, it does not account for the different consequences of misclassification errors. In many real-world applications, the cost associated with different types of errors varies significantly. This is particularly true in our case, where misclassifying a critically ill patient as stable could have far more severe implications than the reverse error. To address this, we introduce a cost-sensitive metric, Total Cost (TC), which incorporates the specific costs associated with different types of
![img-0.jpeg](img-0.jpeg)

Figure 2. Left: Naive Bayes (NB). Center: Augmented Naive (AN). Right: Tree Augmented Naive (TAN).

misclassification. Using a predefined cost matrix, TC quantifies the overall cost of errors made by the classifier, reflecting the practical importance of each type of misclassification. This approach aligns the model evaluation with real-world priorities and consequences. Mathematically, TC is calculated by summing the products of the number of misclassifications and their corresponding costs.

The cost of classifying a patient into class $c_{i}$ when they actually belong to class $c_{j}$ is denoted as $m_{i j}$, where $m_{j j}=0$ signifies no error and no cost. The Total Cost (TC) is then calculated as:

$$
\mathrm{TC}=\frac{1}{N} \sum_{i, j=1}^{r} C_{i j} m_{i j}
$$

Here, $\left(m_{i j}\right)_{i, j=1}^{r}$ represents the cost matrix. In our study, medical experts assigned a minimum cost of 1 for misclassifying a patient that actually belong to discharge as icu or exitus. The maximum cost, set to $\alpha=10$, corresponds to the most critical error of misclassifying exitus as discharge, with a lesser but still significant cost for misclassifying as icu. The cost of misclassifying a patient who should be in the ICU is $\beta=8$ when incorrectly classified as discharge, and half that when classified as exitus. Thus, the cost matrix is defined with $\alpha=10$ and $\beta=8$ in equation (1).


We assume the same cost matrix for both patient subsets, with and without therapeutic limits, though specific cost matrices could be defined for each subset if necessary. The Total Cost is calculated as follows:

$$
\mathrm{TC}=\frac{1}{N}\left(C_{12} \alpha+C_{13} \beta+C_{21}+C_{23} \frac{\beta}{2}+C_{31}+C_{32} \frac{\alpha}{2}\right)
$$

In the experimental phase, we perform a parameter sweep for $\alpha$ and $\beta$. We systematically vary these parameters to observe their impact on the predictive models using both the TC and the BA metrics. The parameters ranges are chosen to include $\alpha=10$ and $\beta=8$, with the constraint that $\beta$ must be less than $\alpha$. Specifically, $\alpha$ ranges from 2 to 20 , and $\beta$ ranges from 2 to $\alpha$, with both parameters being integers.

When $\alpha=\beta=2$, the costs of misclassifying a patient as exitus when the true class is icu, and vice versa, is set to 1 . The same as for misclassifying a discharged patient as exitus or icu. This scenario reflects a situation where all errors are treated as equally impactful, except for misclassifications involving discharge when the true class is exitus or icu, which are assigned double the cost due to their greater impact.

The constraint $\beta \leq \alpha$ highlights that the most critical misclassification errors are those where the true condition exitus but the patient is classified otherwise. We employ a grid search approach to explore the 190 possible pairs $(\alpha, \beta)$. This analysis helps us understand the sensitivity of our results to these parameters, identify trends or patterns, and evaluate how these parameters influence model performance.

# Thresholding: an indirect cost-sensitive meta-learning approach 

As previously mentioned, our dataset is imbalanced, with two minority classes (icu and exitus) and one majority class (discharge). This highlights the need for a specific approach. We use a cost-sensitive learning approach, the thresholding method, which we term the Multi-Thresholding meta-algorithm (MTh). This is an indirect cost-sensitive approach that acts as a wrapper, transforming any cost-insensitive probabilistic classifier into a cost-sensitive one. This transformation is achieved by post-processing the classifier's output, which includes the probability distribution assigned to the classes. MTh involves adjusting this probability distribution based on the expected costs associated with misclassification, ensuring that the class with the highest adjusted probability is selected. These expected costs are calculated using the cost matrix described in equation (1), derived from expert knowledge. For an overview of the algorithm, refer to Algorithm 1 below.

In our specific application, if a classifier assigns a probability distribution $p=\left(p_{1}, p_{2}, p_{3}\right)$ to the class labels $c_{1}$ :discharge, $c_{2}$ :exitus, and $c_{3}$ :icu, the adjusted probabilities are calculated by dividing $p_{i}$ by $\omega_{i}$. Here, $\omega_{i}$ represents the expected cost associated with misclassifying an instance when assigning it label $c_{i}$. The expected costs are calculated as follows:

$$
\begin{aligned}
& \omega_{1}=m_{12} p_{2}+m_{13} p_{3}=\alpha p_{2}+\beta p_{3} \\
& \omega_{2}=m_{21} p_{1}+m_{23} p_{3}=p_{1}+\frac{\beta}{2} p_{3} \\
& \omega_{3}=m_{31} p_{1}+m_{32} p_{2}=p_{1}+\frac{\alpha}{2} p_{2}
\end{aligned}
$$

The adjusted probabilities are then computed as: $\widetilde{p}_{1}=\frac{p_{1}}{\omega_{1}}, \quad \widetilde{p}_{2}=\frac{p_{2}}{\omega_{2}}, \quad \widetilde{p}_{3}=\frac{p_{3}}{\omega_{3}}$.
Strictly speaking, we should normalize these adjusted probabilities by dividing each $\widetilde{p}_{i}$ by the sum of all of them to ensure they form a probability distribution. However, this step is unnecessary for our purpose, as we only need to identify the class that maximizes the adjusted probabilities. To simplify, we refer to $\widetilde{p}_{i}$ as "probabilities",

although they are technically not. Notably, as the cost associated with misclassifying a label increases, the adjusted probability for that label decreases, making it less likely to be selected as the final prediction. This clearly illustrates the implementation of a cost-sensitive classification algorithm. While the results in Section 4 depend on the specific values in the cost matrix (1), the algorithm's procedure remains consistent regardless of these values. Appendix D further elaborates on and proves some properties of this algorithm.

```
    Input labels \(c_{1}, \ldots, c_{r}\), probability distribution assigned to the labels \(\left(p_{1}, \ldots, p_{r}\right)\),
```

$\operatorname{cost}$ matrix $\left(m_{i j}\right)_{i, j=1, \ldots, r}$

Output The predicted class (label) $c^{*}$
for $i$ in $1: r$ do
compute $\omega_{i}=\sum_{j=1}^{r} m_{i j} p_{j}$ (expected cost of misclassifying an instance as $c_{i}$ )
adjust probabilities by $\widetilde{p}_{i}=\frac{p_{i}}{\omega_{i}}$
end for
$\ell=\arg \max _{i=1, \ldots, r} \widetilde{p}_{i}$
$c^{*}=c_{\ell}$
return $c^{*}$
(If the maximum adjusted probability is not unique, a tiebreaker rule is used to select one of the labels.)

Algorithm 1. The Multi-Thresholding meta-algorithm, MTh

When the MTh meta-algorithm is not applied, meaning we take $\omega_{i}=1$ for all $i$, the adjusted probabilities $\widetilde{p}_{i}$ become identical to the original probabilities $p_{i}$. In this case, the classification follows the standard Maximum A Posteriori (MAP) criterion for multi-class classification. Thus, comparing the use of MTh with not using it is effectively a comparison between the MTh and the MAP criterion, the latter being the reference standard for multi-class classification.

# Implementation of the experimental phase 

All computational aspects of model implementation were conducted using the R programming language ${ }^{46}$. For each of the two data subsets -one for patients with therapeutic limits and the other for patients without such limits- we constructed three types of Bayesian Networks as predictive (and explanatory) models: Naive Bayes (NB), Augmented Naive (AN) and Tree Augmented Naive (TAN), both with and without applying the MTh metaalgorithm.

Additionally, to provide a comprehensive comparison and assess how our proposed approach compares with other state-of-the-art predictive models, we included three advances ML models: Neural Network (NN), Support Vector Machine (SVM), and Random Forest (RF), the latter being constructed as an ensemble of 100 decision trees. We constructed these models using the mlNnet, mlSvm and mlRforest functions from the R package mlearning.(Authors: Ph. Grosjean \& K. Denis. https://doi.org/10.32614/CRAN.package.mlearning).

Our primary objective was to experimentally validate the use of the MTh meta-algorithm for multi-class classification with imbalanced data. Once this validation was achieved, we focused on selecting the model with the best predictive performance from those tested. The comparison between models (using the MTh metaalgorithm) was structured as follows: First, we evaluated the three Bayesian Network models against each other, and separately compared the other three ML models among themselves. After identifying the best-performing model within each group, we then compared these "winning" models to determine the overall best performer. This comparison was conducted separately for each subpopulation -patients with and without therapeutic limits- and for each performance metric used: Total Cost (TC) and Balanced Accuracy (BA).

Although we also included the Balanced Accuracy metric, our main reference is the TC metric, which is specifically designed to account for the varying weights assigned to classification errors, making it particularly suited to our cost-sensitive approach. The BA metric, while valuable for its balanced evaluation of class performance, does not account for the different consequences of misclassification errors. Therefore, while the TC metric aligns with our cost-sensitive methodology, BA provides a complementary view to ensure a comprehensive evaluation of model performance in handling imbalanced data.

The $K$-fold cross-validation procedure, with $K$ set to 10 , resulted in each model producing 10 confusion matrices. This provided a sample of 10 values for both the TC metric and the BA metric (as detailed in Section 3.4). To compare the models, we conducted appropriate statistical hypothesis tests. Initially, we used the ShapiroWilk ${ }^{47}$ test to assess data normality. Based on the results, we applied either the paired Student's t-test ${ }^{48}$ or the Wilcoxon signed-rank test ${ }^{49}$ to compare pairs of samples, depending on whether the data could be assumed to follow a normal distribution. To account for multiple comparisons between models, we adjusted p-values using the Holm-Bonferroni method (We opted for paired tests with adjusted p-values over ANOVA with multiple comparisons due to the nature of our context. Paired tests are specifically designed for comparing paired samples, which aligns with the cross-validation setup. Furthermore, paired tests offer clear and interpretable results for pairwise model comparisons, simplifying the process of identifying superior-performing models.

As usual, throughout the paper superscripts $\cdot$ indicates statistical significance at $10 \%, *$ at $5 \%, * *$ at $1 \%$ and $* * *$ at $0.1 \%$, for all p -values). When applying p -value adjustments using the Holm-Bonferroni method in the context of multiple model comparisons, a significant challenge arises as the number of models increases. The Holm-Bonferroni method controls the family-wise error rate, thereby reducing the likelihood of Type I errors (false positives) during multiple hypothesis testing. However, as the number of comparisons grows, the adjustment becomes increasingly conservative, making it harder to detect statistically significant differences between models and raising the risk of Type II errors (false negatives), where genuinely significant differences are overlooked. To address this issue, we divided the six models into two groups. We first compared models within each group, identified the best-performing model in each, and then compared the "winners" against each other. This approach reduces the number of comparisons at each stage, thus mitigating the risk of overly conservative p-value adjustments and enhancing our ability to detect meaningful differences between models.

In the following section, we will present the validation results and perform a comparative analysis of the different models.

## Results

## The explanatory model

Among the six models we compared, only the three types of Bayesian Networks (BN) -Naive Bayes (NB), Augmented Naive (AN), and Tree Augmented Naive (TAN)- can be considered explanatory models. Bayesian Networks are categorized as "white-box" models, meaning their internal processes are transparent and interpretable. In contrast to "black-box" models such as Neural Networks, Support Vector Machines, and Random Forests, which may offer high predictive power but lack interpretability, BNs allow us to understand and explain how the predictions are generated. The probabilistic relationships between variables in these networks can be visualized and interpreted, making them particularly valuable in contexts where insight into the decision-making process is as important as the predictions themselves. This interpretability is a significant advantage in applications where understanding the reasoning behind a model's prediction is crucial, such as in medical decision-making or other high-stakes domains.

We use the $\mathrm{R}^{\text {th }}$ package bnlearn and its strength plot function to visualize the Bayesian network structures, represented by the Directed Acyclic Graphs (DAGs) in Figures 6 and 7 in Appendix B. These DAGs illustrate the conditional independence relationships entailed by the AN and TAN models for the "therapeutic limit" data subset, similar to Figures 8 and 9 for the "no-therapeutic limit" data subset.

In these plots, the thickness of directed arcs reflects the strength of the dependencies they represent, with thicker lines indicating stronger relationships. To quantify the strength of each arc (or feature) while keeping the rest of the network structure fixed, we use the arc.strength function, which provides a p-value associated with the conditional independence test for removing the arc from the network. Smaller p-values indicate stronger relationships.

Tables 11 and 12 in Appendix B present the most influential features for predicting event, considering only p-values less than 0.05 . Notably, among the two demographic features for the "no-therepeutic limit" patients, age shows a significantly stronger influence on predicting the output variable event. As expected, the limit type is highly influential for the "therapeutic limit" patients. Additionally, only three symptoms -confusional syndrome, dyspnoea and rhinorrhea- are influential for both data subsets. The only comorbidity that holds influence across both data subsets is dementia. Furthermore, only two previous treatments, acetylsalicylic acid and statins, play a notable role in risk prediction for both data subsets.

## The predictive model: Thresholding vs no-thresholding

In the validation procedure, we conducted a comprehensive comparison of the Total Cost (TC) and Balanced Accuracy (BA) metrics across all classifiers (the three types of Bayesian Networks, NN, SVM and RF) both with and without the application of the thresholding meta-algorithm MTh. This comparison encompasses every integer value of $\alpha$ ranging from 2 to 20 and each integer value of $\beta$ ranging from 2 to $\alpha$, resulting in a total of 190 distinct comparisons.

Table 2 below summarizes the number of comparisons that significantly favour predictive models utilizing the MTh meta-algorithm (first multi-row) versus those without it (second multi-row) out of the total of 190 possible comparisons. Notably, an overall advantage is observed in favour of using the MTh meta-algorithm. We observe a similar pattern across the two data subsets with the TC metric, but a markedly different pattern when the BA metric is used. The majority of statistically significant results support the superiority of MTh with the TC metric, except in a few cases with small values of $\alpha$ and $\beta$. When considering the BA metric, the results are favourables to MTh for the data subset of patients without therapeutic limits. In the subset of patients with therapeutic limits, there are fewer statistically significant results. Some of these support the MTh meta-algorithm, corresponding to low values of $\alpha$ and high values of $\beta(\beta \leq \alpha)$, while those that oppose its use correspond to high values of $\alpha$ and low values of $\beta$.

The experimental results strongly support the use of the MTh meta-algorithm when TC is used as performance metric, both for patients with and without therapeutic limits. When the BA metric is considered, the same trend is observed for the non-therapeutic limit data subset. However, for the "therapeutic limit" subset with the BA metric, the results are more balanced between favouring and opposing MTh.

Figure 3 illustrates the differences in the mean metric values between using and not using the MTh metaalgorithm (positive values favour MTh) across all predictive models, considering both patient groups. For simplicity in representing these differences in a line graph, we have reduced the parameter set by fixing $\alpha=10$ and $\beta=8$, as an example.

Based on these findings, we decided to adopt the use of the MTh meta-algorithm across both patient subsets and all predictive models. This experimental validation confirms the effectiveness of the MTh meta-algorithm,


Table 2. Number of comparisons, out of 190 possible, favouring predictive models with or without the MTh meta-algorithm, based on the TC and BA metrics. Comparisons are conducted with $\alpha=2, \ldots, 20$ and $\beta=2, \ldots, \alpha$, and results are distinguished for the two data subsets: patients with and without therapeutic limits.
![img-1.jpeg](img-1.jpeg)

Figure 3. Bar plots illustrating the increase in the mean of the TC and BA metrics when applying the MTh meta-algorithm versus not using it, across the predictive models and the data subsets of patients with and without therapeutic limits. The plots are generated with parameters set to $\alpha=10$ and $\beta=8$. Positive values indicate that the MTh meta-algorithm improves both metrics.

particularly when using the TC metric, and also for the patients without therapeutic limits. In the following subsection, we will identify the preferred predictive model for each data subset and metric.

# The predictive model: choosing the best 

Using the thresholding meta-algorithm MTh, we compared the mean (or median) values of the two metrics -Total Cost (TC) and Balanced Accuracy (BA)- across different predictive models, including three types of Bayesian Networks (NB, AN and TAN) and three state-of-the-art models (NN, SVM and RF), for each parameter pair $(\alpha, \beta)$ where $\alpha=2, \ldots, 20$ and $\beta=2, \ldots, \alpha$. We used adjusted p -values for multiple comparisons, applying the Holm-Bonferroni method to ensure statistical rigor.

Table 3 displays the number of $(\alpha, \beta)$ pairs, out of the 190 possible, for which significant differences were found between models. This table highlights which model's mean (or median) is significantly higher ( $>$ ) for each pair of models concerning the TC and BA metrics. Specifically, for each metric, it shows:

- The comparison among the three Bayesian Network classifiers (NB, AN, TAN) in the first multi-row.
- The comparison among the state-of-the-art models (NN, SVM, RF) in the second multi-row.
- A comparison between the best models from the two groups. They are NB and RF, respectively, with the TC metric, and with the BA metric for the "no-therapeutic limit" data subset. For the "therapeutic limit" data subset and the BA metric, NB is compared with SVM instead of RF. The results indicate a consistent advantage for NB over RF in the first case. Conversely, SVM shows slightly better performance for patients with therapeutic limits when using the BA metric.

Figure 4 presents box plots illustrating the distribution of TC values for $\alpha=20$ and $\beta=20$, providing a representative example of overall trends. These plots display results for the three models from both the "therapeutic limit" and the "no-therapeutic limit" data subsets, with the MTh meta-algorithm applied. Lower median TC values indicate better predictive performance, and the box plots visually confirm the superior performance of NB compared to the other models when $\alpha=\beta=20$, as previously observed in Table 3. Similarly, higher median values indicate better predictive performance for the BA metric. The box plots corroborate the clear advantage of NB for patients without therapeutic limits and highlight the slight edge of SVM for patients with therapeutic limits, as previously noted in Table 3.

That is, after a rigorous model comparison, Naive Bayes (NB) consistently emerges as the preferred predictive model when evaluated with the Total Cost (TC) metric, and is particularly favoured for patients without therapeutic limits when using the Balanced Accuracy (BA) metric. Conversely, while Support Vector Machine (SVM) shows some preference as the predictive model for patients with therapeutic limits, this preference is less pronounced.

Figure 5 includes heatmaps that show how different combinations of parameters affect the mean metric values for the selected predictive model NB across both data subsets and both metrics, except for the data subset of patients with therapeutic limits and BA metric, for which the chosen model is SVM). The heatmaps depict the mean metric value as a function of $\alpha=2, \ldots, 20$ and $\beta=2, \ldots, \alpha$, with values derived from $K=10$


Table 3. Number of pairs $(\alpha, \beta)$, out of the total 190 possible pairs, where one predictive model exhibits a significantly higher ( $>$ ) mean (or median) metric compared to another, using the MTh meta-algorithm. The metrics considered are TC and BA. Only statistically significant results are reported; cells left blank indicate no significant difference.

![img-2.jpeg](img-2.jpeg)

Figure 4. Box plots illustrating the TC and BA values obtained through cross-validation using the MTh meta-algorithm for both data subsets, with α = β = 20. Lower TC values indicate better performance, whereas higher BA values reflect better predictive behaviour.

Measurements per (α, β) pair during cross-validation. As anticipated, higher values of α or β generally result in increased mean TC values. Additionally, the mean TC values are consistently higher for the model applied to patients without therapeutic limits, reflecting diminished performance. Conversely, when using the BA metric, this trend becomes less predictable and more variable, especially for the patients without therapeutic limit.

### Case studies in risk assessment using the predictive model

In this section, we illustrate the capabilities of our predictive model with specific examples. Consider a COVID-19 patient admitted to the hospital with a therapeutic limit. The initial (*a priori*) risk estimates are as follows: exitus: 36.76%, icu: 2.66%, and discharge: 60.58%. We will now evaluate the updated (*a posteriori*) risk predictions based on the patient's specific characteristics using our selected predictive model. To measure the association between a patient's characteristic (factor) and the risks predicted by the model, we use the *Odds Ratio* (OR). The OR is a statistical measure that quantifies the strength and direction of the association between two events. An OR greater than 1 suggests a positive association, while an OR less than 1 indicates a negative association. An OR of 1 means there is no association between the two events. In this context, the OR quantifies how a specific factor influences the odds of a particular risk outcome. It expresses how much greater the odds are for one category of the factor compared to another.

Example 1 In Table 5, we have recorded some *a posteriori* probabilities for the patient in Example 1, whose characteristics are detailed in Table 4. These probabilities are provided for various pairs of α and β values. We assume that the patient has a therapeutic limit, although the specific limit is unknown. As observed, increasing α with a fixed β, or decreasing β with a fixed α, results in a decrease in the *a posteriori* probability of discharge, while the probabilities of exitus and icu increase. The probability of icu is the highest, and the confidence level (highest probability) is highlighted in bold.

How does the specific type of therapeutic limit affect the *a posteriori* probabilities we have obtained? Table 6 shows the results for the two possible therapeutic limits, highlighting the differences: when the therapeutic limit is NRB (non-rebreather mask), the probability assigned to icu remains very low across the entire range of parameter values. In contrast, when the therapeutic limit is NIMV (non-invasive mechanical ventilation), this probability increases up to 20% (when α = β = 20).

![img-3.jpeg](img-3.jpeg)

Figure 5. Heatmaps depicting the mean TC and BA values as functions of $\alpha=2, \ldots, 20$ and $\beta=2, \ldots, \alpha$ for the best models, with the MTh meta-algorithm. The median values are shown in white, with lower values in blue and higher values ir red.


Table 4. Patient characteristics for Example 1: Case with a therapeutic limit.


Table 5. A priori and a posteriori probabilities for the patient in Example 1. Limit type unknown.


Table 6. A posteriori probabilities for the patient in Example 1 based on the known type of therapeutic limit.

Table 6 reveals a striking contrast in the estimated a posteriori risks of exitus and icu depending on the type of therapeutic limit. When the limit is NRB, the probabilities of exitus closely resemble those when the limit type is unknown, with the probability of discharge increasing at the expense of the icu probability, which remains notably low. Interestingly, in this scenario, the icu probability is even lower than that of exitus, which differs from the situation when the limit type is unknown. Conversely, with NIMV, the estimated a posteriori risk of exitus is low, while the risk of icu significantly increases at the expense of the discharge probability. This underscores the substantial impact of the therapeutic limit type on the model's risk predictions.

The heatmaps in Appendix C display the a posteriori risks of exitus and icu for this example. These heatmaps not only provide the magnitude of these probabilities through colour scales, which may vary from one heatmap to another, but also reveal discernible trends. They illustrate how the risks change as we increase the values of $\alpha$, and for each $\alpha$, as we increase $\beta$. Importantly, this trend analysis depends on the specific type of therapeutic limit. Examining these heatmaps allows us to gain insights into how risk probabilities are affected by different parameter combinations and how these variations rely on the particular scenario at hand.

By focusing on regions with higher (red) or lower (blue) outcome values, we can closely examine the heatmaps and draw inferences about which combinations of parameters lead to better or worse outcomes. This allows us to perform a sensitivity analysis using the heatmaps as a valuable tool to understand how changes in parameters impact risk assessments for COVID-19 patients. For instance, in Figure 10, we observe that the color bands corresponding to the NRB therapeutic limit are nearly vertical for the risk of death. This suggests that the risk is sensitive to the value of $\alpha$, increasing as $\alpha$ increases, while remaining relatively stable concerning $\beta$. In contrast, the nearly horizontal color bands, such as those for the NIMV therapeutic limit in ICU admission risk, indicate sensitivity to the value of $\beta$, with the risk increasing as $\beta$ increases but showing robustness with respect to $\alpha$. These observations align with the cost matrix expression in (1), providing valuable insights into how the predicted risks behave based on the specific therapeutic limit type.

Next, we calculate the estimated Odds Ratios (OR) based on the probabilities assigned by the model for the patient in Example 1. (We can estimate the OR values from the provided probabilities, but without sample sizes or additional information, meaningful confidence intervals for the OR cannot be calculated). We consider the type of therapeutic limit as factor that could be associated with the risk of death or ICU admission. Table 7 presents the computed OR values for icu and exitus for a patient corresponding to Example 1. These OR values are calculated when the therapeutic limit is NIMV compared to NRB. For example, with $\alpha=\beta=2$, the OR in favor of icu is calculated as follows: $\frac{0.0292 /(1-0.0292)}{0.0012 /(1-0.0012)}=25.03516 \approx 25.035$.


Table 7. OR for ICU admission risk (1st row) and death risk (2nd row) for the patient in Example 1 with therapeutic limit NIMV, compared to NRB, across different $\alpha$ and $\beta$ values, based on probabilities from Table 6 .


Table 8. A posteriori probabilities for the patient in Example 2 based on the known type of therapeutic limit.

In Table 7, when OR $>1$, it indicates that the NIMV therapeutic limit is a risk factor compared to NRB. This is true for ICU admission risk across all values of $\alpha$ and $\beta$. However, it only applies to the risk of death when $\alpha=\beta=2$. For the other tested parameter values, NIMV serves as a protective factor against NRB for the risk of death.

Clinically, this can be explained as follows. When a patient is placed on NRB, it indicates they can receive oxygen support but are not on mechanical ventilation. This implies that the patient's initial condition is more fragile, and a proactive decision is made to avoid escalating treatment, including ICU admission and ventilation techniques. Such patients are at a higher risk if subjected to intensive care and ventilation maneuvers, which could potentially increase their mortality rate. Consequently, they have a lower likelihood of ICU admission, which, unfortunately, also entails higher mortality rates. On the other hand, NIMV implies that if the patient's respiratory distress has reached a point where mechanical support is necessary, they are typically provided with non-invasive ventilation within the ICU, with an emphasis on avoiding more invasive treatments. Patients with no therapeutic limit may undergo invasive mechanical ventilation (intubation in the ICU) if necessary. Therefore, the concept of a NIMB therapeutic limit reflects a deliberate approach to critical care, balancing lifesaving interventions and minimizing invasiveness.

The results in Table 7 align with clinical intuition and offer valuable quantification of these trends. This quantification is essential and serves various purposes. While healthcare professionals may have a general understanding of how different factors affect patient outcomes, quantifying these effects provides an objective, evidence-based assessment. It enables healthcare providers to make more informed decisions about the level of care and interventions required for specific patients. Resource allocation is particularly crucial in healthcare settings, especially during a pandemic. Understanding how various factors impact patient outcomes aids in the efficient distribution of resources. In summary, quantifying the influence of therapeutic factors such as the type of therapeutic limit (NRB and NIMV) on patient outcomes, as demonstrated in Table 7, is fundamental for evidence-based medicine. It enhances the precision of clinical decision-making, resource allocation, risk communication, healthcare research, and overall healthcare system management, ultimately resulting in improved patient care.

Example 2 Now, let us consider a patient with the same attributes as the one in Example 1 but with a Charlson Index of $4-5$. Clinically, a higher Charlson score indicates an increased risk of adverse outcomes. The resulting a posteriori probabilities for this patient are detailed in Table 8.

Using the values in Table 8, we can calculate Odds Ratios (OR) similar to our approach in Example 1. It is particularly insightful to assess the "Charlson Index effect". This involves understanding how a higher Charlson Index (as in Example 2) versus a lower one (as in Example 1) influences the patient's risks, keeping all other attributes constant. Evaluating the impact of the Charlson Index on death and ICU admission risk assessments helps healthcare professionals make informed decisions about treatment and care strategies. It also assists in the efficient allocation of resources, especially in the context of COVID-19 patient care.

This outcomes are consistent with those in Table 6 and align with our qualitative expectations. However, the true value of the model lies in its ability to quantify these expectations. Notably, for high $\alpha$ values, the model assigns the exitus category to the patient in Example 2, even when the therapeutic limit is of type NRB (or when


Table 9. Patient characteristics for Example 3.


Table 10. A posteriori probabilities for the patient in Example 3 with $\alpha=\beta=20$.
the limit type is unknown). In contrast, the patient in Example 1 was consistently assigned to the discharge category under the same conditions. This demonstrates the model's ability to capture subtle variations in risk assessment based on differing patient characteristics. For further insights, please refer to the corresponding heatmaps in Appendix C.

Example 3 To evaluate the impact of the presence and type of a therapeutic limit, we compare the estimated risks for a patient with the characteristics outlined in Table 9. This comparison hinges on whether the patient has a therapeutic limit, its type if applicable, and whether it is known. We have selected $\alpha=\beta=20$ for this analysis. The results are summarized in Table 10.

Given the vast number of potential scenarios, we will not explore further examples in this section. However, consider cases where multiple features influence outcomes simultaneously, such as age and the Charlson Index. In these situations, one feature might be a risk factor (e.g., a high Charlson Index) while another could act as a protective factor (e.g., low age). Evaluating the combined effect of a risk factor and a protective factor is complex without a suitable quantitative model. Our model provides a valuable tool for assessing how certain characteristics (protective factors) can mitigate the impact of risk factors on the likelihood of ICU admission or death.

# Discussion and Conclusions 

This study presents a comprehensive evaluation of the impact of therapeutic limits on predictive models for patient mortality and ICU admission risks, particularly within the context of COVID-19. By developing predictive models tailored to patient subgroups with and without therapeutic limits, we achieved significant improvements in risk prediction accuracy through the introduction of the novel MTh meta-algorithm. This innovative algorithm extends thresholding to multiclass settings and offers a cost-sensitive approach to predictive modelling, marking a significant progression in the field. The key findings and implications of the study are:

1. Impact of therapeutic limits: The choice and type of therapeutic limits, such as Non-Rebreather Mask (NRB) or Non-Invasive Mechanical Ventilation (NIMV), play a critical role in patient outcomes. This choice reflects the initial assessment of patient frailty, with NIMV typically indicating a less fragile condition, allowing for more intensive interventions if necessary. This often results in a higher risk of ICU admission but also an improved chance of survival. On the other hand, NRB is generally associated with a more fragile condition, preventing ICU admission and the use of invasive measures. While this may suffice for less severe cases, it can lead to higher mortality rates for patients in more critical conditions.

This complex interplay of clinical factors underscores the challenges in clinical decision-making, where therapeutic interventions must carefully balance the severity of the patient's condition, the available resources, and the expected outcomes. The ML models developed for each patient subgroup demonstrate how different therapeutic limits correlate with distinct probabilities of ICU admission and mortality, thereby supporting clinicians in making more informed decisions and optimizing resource allocation.
2. Explanatory and predictive insights: The integration of Bayesian Networks as explanatory models provides a clearer understanding of the interdependencies among patient variables, thereby supporting more nuanced and informed clinical decision-making. Our predictive model effectively quantifies the impact of patient

characteristics on risk predictions. The combination of predictive and explanatory modelling offers a robust framework for addressing the complexities of patient care.
3. Introduction of MTh meta-algorithm: MTh extends the concept of thresholding from binary to multiclass settings by adopting a cost-sensitive approach, focusing on the Total Cost (TC) metric as a behavioral indicator. This novel approach is particularly effective in handling multiclass classification problems and imbalanced datasets. Additionally, the adaptability of the MTh algorithm by updating the cost matrix to reflect changing circumstances, makes it a highly responsive and valuable tool in the evolving landscape of healthcare. Collectively, these findings highlight the importance of integrating advanced ML techniques into healthcare to improve patient outcomes and optimize clinical decision-making. However, several potential biases and limitations should be considered: (1) the model's performance is based on a specific dataset with a relatively small number of cases, which may limit its generalizability to broader patient populations; (2) the model's sensitivity to the chosen parameters ( $\alpha$ and $\beta$ ), representing misclassification costs, may affect the stability of risk predictions, and imprecise specifications of these parameters could undermine the reliability of the results; and (3) inaccuracies in identifying therapeutic limits could compromise the integrity of risk assessments.

These limitations underscore the need for ongoing research and refinement to enhance the model's robustness and applicability across different healthcare scenarios. Future research should focus on extending the model's applicability by incorporating more diverse patient populations and comorbidities, thereby enhancing its generalizability, robustness, and relevance. Additionally, further exploration of the effects of parameters $\alpha$ and $\beta$ on model reliability is essential. To address potential errors in the assignment of appropriate therapeutic limits, we plan to implement targeted training for medical personnel. Lastly, integrating the predictive model into electronic health records (EHR) systems could facilitate real-time risk assessments, improving clinical workflows and decision-making efficiency. This integration would represent a significant step forward in bringing predictive modelling into everyday clinical practice.

In summary, this work not only offers a holistic framework that integrates predictive and explanatory modelling to deliver actionable insights into patient outcomes, but also marks the introduction of the MTh meta-algorithm, a novel and significant advancement in predictive modelling. By advancing the application of ML in healthcare - particularly through the development and validation of the MTh meta-algorithm- we contribute to the ongoing evolution of personalized medicine. Our approach is cost-sensitive and employs rigorous model evaluation techniques. Its successful implementation demonstrates potential to enhance clinical decision-making, offering a promising path toward more tailored and effective patient care in the future.

# Data availability 

The data supporting these findings are restricted due to ethical and legal constraints. Access to these data may be granted upon request to the Ethics Committee of Bellvitge University Hospital (Barcelona, Spain), which will evaluate each request individually. To inquire about data access, please contact the Research Support Unit at Bellvitge University Hospital through the following email address: clinicalresearchwindow@bellvitgehospital. cat, or visit the website at www.bellvitgehospital.cat/clinicalresearch

## Appendix A: Overview of patient characteristics in the dataset

Variables highlighted in italic are exclusively utilized in constructing the predictive model for the data subset of patients with a therapeutic limit, while those highlighted in bold italic are specific to the data subset of patients without a therapeutic limit. Variables in black are used for both data subsets. Percentages refer to the entire dataset.

Demographic


Initial assessment


Therapeutic limit can be either NRB (non-rebreather mask) or NIMV (non-invasive mechanical ventilation).

## Vital signs


The Charlson Index is a medical score designed to predict 10-year survival in patients with multiple comorbidities. It ranges from 0 to 29 .

Symptoms


Rhinorrhea refers to nasal congestion, anosmia signifies a loss of smell, and ageusia loss of taste. Arthromyalgia indicates muscle or joint pain. Dyspnoea represents shortness of breath, asthenia denotes fatigue, and cephalea corresponds to headache.

# Blood test 


d-dimer is a byproduct of blood clots, while C-reactive protein is a protein that elevates in response to inflammation.

Comorbidities


Hemiplegia refers to the paralysis of one half of the body in a patient.

Previous treatments


# Appendix B: Arc strength and influential features 

![img-4.jpeg](img-4.jpeg)

Figure 6. Arcs strength in the DAG of the Augmented Naive model for the "therapeutic limit" data subset.

![img-5.jpeg](img-5.jpeg)

Figure 7. Arcs strength in the DAG of the TAN model for the "therapeutic limit" data subset.

![img-6.jpeg](img-6.jpeg)

**Figure 8.** Arcs strength in the DAG of the Augmented Naive model for the "no-therapeutic limit" data subset.

![img-7.jpeg](img-7.jpeg)

**Figure 9.** Arcs strength in the DAG of the TAN model for the "no-therapeutic limit" data subset.


Table 11. Therapeutic limit. Most influential features for risk prediction, with p-values indicating strength of influence (lower p-values indicate stronger influence). Unless otherwise indicated by a superscript * (5\%) or ** (1\%), the statistical significance of p -values is $1 \%$.


Table 12. No-therapeutic limit. Most influential features for risk prediction, with p-values indicating strength of influence (lower p-values indicate stronger influence). Unless otherwise indicated by a superscript * (5\%) or ${ }^{* *}(1 \%)$, the statistical significance of p -values is $1 \%$.

# Appendix C: Heatmaps for risk predictions 

![img-8.jpeg](img-8.jpeg)

Figure 10. Heatmaps showing the a posteriori probabilities for the patient in Example 1: probability of exitus (left) and icu (right) as functions of $\alpha=2, \ldots, 20$ and $\beta=2, \ldots, \alpha$, differentiated by therapeutic limit type. White represents the median value, with low probabilities in blue and high probabilities in red.

![img-9.jpeg](img-9.jpeg)

Figure 11. Heatmaps showing the a posteriori probabilities for the patient in Example 2: probability of exitus (left) and icu (right) as functions of $\alpha=2, \ldots, 20$ and $\beta=2, \ldots, \alpha$, differentiated by therapeutic limit type. White represents the median value, with low probabilities in blue and high probabilities in red.

# Appendix D: The Multi-Thresholding meta-algorithm, MTh 

In this appendix, we present and establish some properties of Algorithm 1.

## Remark 1

Bayes Minimum Risk (BMR) is a concept used in classification problems, particularly in the context of Bayesian Decision Theory and decision-making under uncertainty. BMR is especially valuable in situations where classification errors have different costs or consequences. This approach involves making predictions by selecting the class that minimizes the risk (or expected cost) associated with incorrectly predicting that class. Formally and with our notations:

$$
c_{\mathrm{BMR}}^{*}=c_{h} \quad \text { with } \quad h=\arg \min _{i=1, \ldots, r} \omega_{i}
$$

In contrast, the MTh meta-algorithm is based on selecting the class that maximizes the adjusted probabilities obtained by dividing the original probabilities by the corresponding risks. When the original probabilities are equal $\left(p_{1}=\cdots=p_{r}\right)$, both criteria coincide, meaning that $c^{*}=c_{\mathrm{BMR}}^{*}$.

The following result demonstrates that, in the binary case, MTh essentially acts as a "thresholding" method, modifying the conventional threshold of 0.5 in cost-insensitive approaches. This modified threshold determines which class label is assigned.

# Proposition 1 

In the binary case where $r=2$, MTh assigns class label $c_{1}$ when $p_{1}>\tau$, and it assigns class label $c_{2}$ when $p_{2}>1-\tau$ (otherwise, there is no clear evidence for either class, and a tie-breaking mechanism should be implemented). The value of this "threshold", denoted as $\tau$, is defined as follows with $\mu=m_{21} / m_{12}$ :

$$
\tau=\left\{\begin{array}{cl}
1 / 2 & \text { if } m_{21}=m_{12} \\
0 & \text { if } m_{21}>m_{12}=0 \\
1 & \text { if } m_{12}>m_{21}=0 \\
-1+\sqrt{\mu} & \text { otherwise }
\end{array}\right.
$$

## Proof

MTh assigns class label $c_{1}$ if $\widetilde{p}_{1}>\widetilde{p}_{2}$. Since $\omega_{1}=m_{12} p_{2}$ and $\omega_{2}=m_{21} p_{1}$, we can express this condition as follows:

$$
\widetilde{p}_{1}>\widetilde{p}_{2} \Leftrightarrow \frac{p_{1}}{m_{12} p_{2}}>\frac{p_{2}}{m_{21} p_{1}} \Leftrightarrow\left(m_{21}-m_{12}\right) p_{1}^{2}+2 m_{12} p_{1}-m_{12}>0
$$

Here, we have used the fact that $p_{2}=1-p_{1}$.
Notably, when $m_{12}=m_{21}$, the condition (D1) simplifies to $\Leftrightarrow p_{1}>1 / 2$, aligning with the cost-insensitive scenario as expected.
Let's assume, for now, that $m_{21}>m_{12}$. If $m_{12}=0$, equation (D1) is equivalent to $p_{1}>0$. In this case, when there is no cost associated with misclassifying and instance of class $c_{2}$ as $c_{1}$ (but there is a cost for the reverse misclassification), MTh always assigns class label $c_{1}$, which is a logical outcome. Otherwise, if we introduce the ratio $\mu=m_{21} / m_{12}$, which is greater than 1 , equation (D1) becomes equivalent to

$$
(\mu-1) p_{1}^{2}+2 p_{1}-1>0
$$

The roots of this quadratic equation are:

$$
\frac{-1-\sqrt{\mu}}{\mu-1}<0<\tau=\frac{-1+\sqrt{\mu}}{\mu-1}<\frac{1}{2}
$$

Therefore, equation (D2) holds if and only if $p_{1}>\tau$.
The case $m_{21}<m_{12}$ is analogous to the previous case. In particular, if $m_{21}=0$, equation (D1) is equivalent to $\left(p_{1}-1\right)^{2}<0$, which is not true for any value of $p_{1}$, leading to $\tau=1$. The interpretation here is that if there is no cost associated with misclassifying an instance of class $c_{1}$ as $c_{2}$ (but there is a cost for the reverse misclassification), MTh logically never assigns class label $c_{1}$. Now, in the case where $0<m_{21}<m_{12}$, which implies that $\mu=m_{21} / m_{12}<1$, the two roots of equation (D2) are:

$$
\frac{1}{2}<\tau=\frac{-1+\sqrt{\mu}}{\mu-1}<1<\frac{1+\sqrt{\mu}}{1+\mu}
$$

Consequently, equation (D2) (or equivalently, (D1)) holds if and only if $p_{1}>\tau$ due to the fact that $\mu<1$.

## Corollary 1

In the binary case where $r=2$, MTh assigns class label $c_{1}$ if $p_{1}>\tau$, where the "threshold" $\tau$ satisfies the condition:

$$
\left\{\begin{array}{lll}
0<\tau<1 / 2 & \text { if } & m_{21}>m_{12}>0 \\
1 / 2<\tau<1 & \text { if } & 0<m_{21}<m_{12}
\end{array}\right.
$$

That is, if the cost associated with misclassifying an instance of class $c_{i}$ is greater than the cost of the opposite error, MTh assigns class label $c_{i}$ with a higher probability than the other class label.

## Corollary 2

In the binary case where $r=2$, the "threshold" $\tau$ obtained with the MTh algorithm is a continuous and decreasing function of $\mu$ within the interval $[0,+\infty)$. As $\mu$ approaches infinity, $\tau$ tends towards zero.

# Proof 

The "threshold" $\tau$ obtained with the MTh algorithm where $r=2$ is given by the following function of $\mu$ in $[0,+\infty)$ :

$$
\tau=f(\mu)= \begin{cases}\frac{-1+\sqrt{\mu}}{\mu-1} & \text { if } \mu \neq 1 \\ 1 / 2 & \text { if } \mu=1\end{cases}
$$

This function is continuous and decreasing. Additionally, $f(0)=1$ and $\lim _{\mu \rightarrow+\infty} f(\mu)=0$.
The interpretation of this result is that, as $\mu$ increases (where $m_{21}$ increases relative to $m_{12}$ ), the threshold $\tau$ decreases, effectively biasing the decision in favor of $c_{1}$. In simpler terms, the cost influences the threshold to favor the less expensive option.

## Remark 2

When comparing the threshold $\tau$ obtained through the MTh meta-algorithm with the conventional threshold in the binary case, $p^{*} \frac{1}{1+\mu}$ (as described in ${ }^{27}$ ), we find that the MTh threshold is not so optimal. Specifically:

$$
\left\{\begin{array}{l}
0<p^{*}<\tau<1 / 2 \quad \text { if } m_{21}>m_{12}>0 \\
1 / 2<\tau<p^{*}<1 \quad \text { if } 0<m_{21}<m_{12}
\end{array}\right.
$$

In both cases, when the of misclassifying an instance as $c_{i}$ is lower, the probability of assigning $c_{i}$ increases with both methods. However, this increase is more pronounced with the classic thresholding method. The expression for $p^{*}$ is derived by considering that the classic method assigns class $c_{1}$ if the expected misclassification cost is lower than assigning $c_{2}$, that is, if $m_{12} p_{2}<m_{21} p_{1}$, resulting in $p_{1}>1 /(1+\mu)$, taking into account that $p_{2}=1-p_{1}$.

It is important to note that MTh offers the advantage of being readily applicable to multiclass scenarios and, in this context, satisfies the pseudo-optimality property outlined in Proposition 2. In simpler terms, MTh ensures that predicted class labels are not changed for instances if doing so would worsen the expected misclassification cost, as we demonstrate in the following result.

## Proposition 2

In cases where predictions are made without ties, the MTh algorithm maintains the predicted class label, thereby avoiding a switch from $c_{k}$ to $c_{\ell}$, if the expected cost of misclassification as $c_{\ell}$ is not lower than that of misclassification as $c_{k}$. This pseudo-optimality feature ensures that decisions made by the algorithm do not lead to worse expected misclassification costs when choosing between class labels.

## Proof

Let $\left(p_{1}, \ldots, p_{r}\right)$ denote the original a posteriori probabilities assigned to the class labels by any cost-insensitive classifier. The classifier's predicted class label is determined as:

$$
c^{*}=c_{k} \quad \text { with } k=\arg \max _{i=1, \ldots, r} p_{i}
$$

After applying the MTh meta-algorithm, the chosen class label becomes $c_{t h}^{*}=c_{\ell}$ if

$$
\ell=\arg \max _{i=1, \ldots, r} \bar{p}_{i}=\arg \max _{i=1, \ldots, r} \frac{p_{i}}{\omega_{i}}
$$

Hence, the change in the predicted class label, i.e. $\ell \neq k$, occurs when:

$$
p_{k}>p_{\ell}, \quad \text { but } \quad \frac{p_{\ell}}{\omega_{\ell}}>\frac{p_{k}}{\omega_{k}}
$$

This implies that $\omega_{\ell}<\omega_{k}$. In other words, the MTh meta-algorithm does not alter the predicted class label from the original $c^{*}=c_{k}$ to $c_{t h}^{*}=c_{\ell}$ if the expected cost of misclassifying an instance as $c_{\ell}$ is not less than that of misclassifying it as $c_{k}$.

Received: 14 February 2024; Accepted: 22 October 2024
Published online: 18 November 2024

# Acknowledgements 

The authors would like to thanks their support to J. Baró, PhD at the CRM, for his initial work of cleaning with the dataset, and to the components of the MetroSud study group: Abelenda-Alonso, G., Rombauts, A., Rodríguez-Molinero, A., Gudiol, C., Aranda-Lobo, J., Arroyo, M., Pérez-López, C., Sanmartí, M., Moreno, E., Álvarez, M ${ }^{\text {a }}$ C., Faura, A., González Bárcenas, M., Cruz Toro, P., Colom, M., Pérez, A., Serrano, L. They extend their sincere gratitude to the editor and reviewers for their valuable feedback and insightful suggestions, which have significantly contributed to the improvement of this manuscript. The author "Jordi Carratalà" is On behalf of MetroSud study group.

## Author contributions

Generation and maintenance of the datasets: J. Carratalà, V. Diaz-Brito, E. Izquierdo, I. Oriol, A. Simonetti, S. Videla, C. Tebé, N. Pallarés Dataset interpretation: C. Tebé, N. Pallarés Dataset cleaning and preprocessing: R. Delgado, F. Fernández-Peláez Methodology: conceptualization R. Delgado Methodology: implementation R. Delgado Writting: R. Delgado, F. Fernández-Peláez

## Funding

R. Delgado supported by Ministerio de Ciencia e Innovación, Gobierno de España, project ref. PID2021-123733NB-I00

## Declarations

## Conflict of interest

The authors declare no potential conflict of interests nor competing interests.github.com/RosDelgado/MTh

## Code availability

The computer programming code ( R function) that has been developed and utilized in this study, to implement Algorithm 1 (the Multi-Thresholding meta-algorithm, MTh) is accessible under an open-access (MIT) license. You can find it at https://github.com/RosDelgado/MTh.

## Ethical implications

The use of predictive models in clinical settings raises several important ethical considerations. First and foremost, privacy and data security are critical: patient data used for training and validating models must be protected, and all practices must comply with data protection regulations. Second, it is essential to address potential biases within the model to ensure that predictions are equitable across different patient groups and to prevent discrimination in care. Third, predictive models should be used to complement, rather than replace, clinical judgment. It is important to be transparent about the limitations and uncertainties inherent in the model's predictions. Lastly, patients should be adequately informed about the use of predictive models in their care. Clear communication is necessary to help patients to understand how these models influence clinical decisions.

## Additional information

Correspondence and requests for materials should be addressed to R.D.
Reprints and permissions information is available at www.nature.com/reprints.
Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommo ns.org/licenses/by-nc-nd/4.0/.
(c) The Author(s) 2024