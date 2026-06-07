# Comparison of Machine Learning Models to Predict Risk of Falling in Osteoporosis Elderly 

German Cuaya-Simbro, Alberto-Isaac Perez-Sanpablo, Angélica Muñoz-Meléndez, Ivett Quiñones Uriostegui, Eduardo-F. Morales-Manzanares, Lidia Nuñez-Carrera


#### Abstract

Falls are a multifactorial cause of injuries for older people. Subjects with osteoporosis are more vulnerable to falls. The focus of this study is to investigate the performance of the different machine learning models built on spatiotemporal gait parameters to predict falls particularly in subjects with osteoporosis. Spatiotemporal gait parameters and prospective registration of falls were obtained from a sample of 110 community dwelling older women with osteoporosis (age $74.3 \pm 6.3$ ) and 143 without osteoporosis (age $68.7 \pm$ 6.8). We built four different models, Support Vector Machines, Neuronal Networks, Decision Trees, and Dynamic Bayesian Networks (DBN), for each specific set of parameters used, and compared them considering their accuracy, precision, recall and F-score to predict fall risk. The F-score value shows that DBN based models are more efficient to predict fall risk, and the best result obtained is when we use a DBN model using the experts' variables with FSMC's variables, mixed variables set, obtaining an accuracy of $80 \%$, and recall of $73 \%$. The results confirm the feasibility of computational methods to complement experts' knowledge to predict risk of falling within a period of time as high as 12 months.


Keywords: GaitRite data, Prognosis falls, Computational methods, Osteoporosis

## 1. Introduction

Falls are a major threat to quality of life of elder [22], these could result in injuries which limit activity and restrict mobility of elder people. Falls are multifactorial but they can be

[^0]
[^0]:    * G. Cuaya-Simbro is with the Higher Technological Institute of the East of State of Hidalgo, Carretera ApanTepeapulco Km 3.5, Colonia Las Peñitas, Apan Hidalgo, México.
    - A. I. Perez-Sanpablo is with the National Rehabilitation Institute, Mexico-Xochimilco Av. 289, Arenal de Guadalupe, 14389, Mexico City, Mexico.
    - A. Muñoz-Mélendez is with the National Institute of Astrophysics, Optics and Electronics, Luis Enrique Erro 1, Santa Maria Tonatzintla, 72840 Puebla, Mexico.
    - I. Quiñones is with the National Rehabilitation Institute, Mexico-Xochimilco Av. 289, Arenal de Guadalupe, 14389, Mexico City, Mexico.
    - E. F. Morales-Manzanares is with the National Institute of Astrophysics, Optics and Electronics, Luis Enrique Erro 1, Santa Maria Tonatzintla, 72840 Puebla, Mexico.
    - L. Nuñez is with the National Rehabilitation Institute, Mexico-Xochimilco Av. 289, Arenal de Guadalupe, 14389, Mexico City, Mexico.

lessened if predisposing factors are addressed [22]. Consequently, clinical guidelines recommend screening risk of falling in older adults at least once at year [21, 22]. Screening includes registering falls history followed by an assessment of gait and balance of the subject [22]. Timed Up and Go (TUG) test has been used as a reference test to evaluate patient's gait and balance due to its practicality. However, a recent review has stressed the limited ability of TUG test to predict falls in elderly [1].

Previous studies have identified several gait related parameters as risk factors for falls. Fallers have been identified as having gait deficiencies on spatiotemporal gait parameters [4, 8, 14], gait stability [3], or on kinematic gait parameters as minimum toe clearance [9].

In [10] studies about the effect of age on spatial and temporal gait variables are presented, however, an explicit model to predict falls is not presented in the cited research. Such a model might certainly be useful to clinicians to represent the way as different way of walking and balance parameters change over time, as well as their effect in the prevalence of falls.

Consequently, spatiotemporal gait parameters are the only measures with proved validity to predict risk of falling, feasible to be assessed in clinical practice. Those spatiotemporal gait parameters can be assessed by the GaitRite system (CIR systems Inc, Havertown, PA, USA) which is a computerized walkway. Validity [20, 25] and reliability [2, 18] of GaitRite system have been already established.

Assessment models for risk of falling prediction have been already developed. Prediction models based on intelligent computing methods are thought to be better than regression techniques [12, 24], but these studies did not consider the spatial and temporal data.

Machine learning based techniques that have been used to complement standard statistical methods for analyzing data. For instance, in [15] the authors used Support Vector Machine (SVM), with parameter tuning, to distinguish between elderly people with/without balancing problems. The authors report a $95 \%$ of accuracy using only two features. However, the model was used exclusively for classifying people with balancing problems and not for predicting falls. Other example, is the use of Neural Networks (NN) [13] to automatically extract relevant information from data collected using different acquisition systems and devices, and classify individuals with different fall-risk. Among the variables that have been identified as relevant to predict falls are descriptive categorical variables, such as, "health compared with that of age group" or "frequency pushing or dragging heavy loads", as well as descriptive continuous variables, such as, "SAD score" or "time asleep". In [19] the authors using multitask learning, with gender and age as auxiliary tasks, and using deep learning models and reported a global performance $(\mathrm{AUC}=0.75)$ but they only analyzed spatial data.

More recent research [7], assess 3 different models, Random Forest (RF), NNs, and SVMs for faller classification, they used different feature selector, and they get the best performance with random forest classifier, and select-5-best feature selector, $73.4 \%$ accuracy, $60.5 \%$ recall, using 71 elder health's data.

In spite of the existence of previous described studies, it's not clear the usefulness of gait related parameters to identify risk of falling, and is less clear in osteoporotic elders even though subjects with osteoporosis are more vulnerable to falls.

Finally, Cuaya et al. [6] developed a dynamic Bayesian network (DBN) for estimating risk of falling from real gait data of 18 women aged $70 \pm 10$ years diagnosed with osteoporosis with scores of accuracy and recall of $72 \%$ and $90 \%$ respectively. They consider that the DBN's are potential alternatives to predict falls based on assessment of gait in osteoporotic subjects.

In this research, we compare the performance of the different classifiers, reported in the literature, applied to predict risk of falling in elder people with osteoporosis, and we using a specific feature selection method to improve models' performance. Finally, we contrast the results obtained with the literature and discus about of the relevance of this research to understand the relation with the fall risk of the different set of variables proved.

# 2. Methods 

### 2.1. Subjects and Procedures

Community-dwelling women older than 60 years, able to walk without any assistance and to follow instructions given by evaluators, were recruited at the National Institute of Rehabilitation (INR from its Spanish acronym) and at a community center in Mexico City. Bone mineral density (BMD) of all participants was measured using dual-energy X-ray absorptiometry (DXA) scanners (Hologic, Marlborough, MA, USA). Subjects were assigned by a specialist in Geriatric Rehabilitation, into two groups (osteoporotic or normal) based on their DXA results according to the World Health Organization (WHO) definition of osteoporosis. Subjects were assigned to osteoporotic (OP) group in presence of a T score lower than 2.5 standard deviation of the mean peak bone mass for healthy adults at one or more skeletal sites. A written consent was obtained from all participants and the study was approved by the Ethical Committee of the Institute.

All subjects underwent a functional gait assessment at their enrollment using the instrumented 12 -feet-long walkway GaitRite performed by experts on gait analysis at the Human Motion Analysis Lab (HML) in INR. Measurements were performed in a reproducible, well-lit environment, with no auditive or visual interference. Participants were allowed to wear comfortable and non-restrictive clothes and their own footwear. Three trials at self-comfortable stride speed were performed by each participant. Only data of a third trial was recorded in order to register steady-state gait. There were 2 meters before and after the computerized walkway in order to allow acceleration and deceleration of participants. All participants received the same instructions. For this study only, data of one year was used due to the increasing loss of participants during the follow up period.

### 2.2. Prediction models

According of the literature, we considered to compare the performance of four classifiers to build models to predict fall risk, Support Vector Machine (SVM), Neuronal Network (NN), Decision Tree (DT), and Dynamic Bayesian Network (DBN), described below briefly each one them.

SVM classifier uses a nonlinear mapping to transform the original training data into a higher dimension. Within this new dimension, it searches for the linear optimal separating hyper plane, i. e., a decision boundary separating the tuples of one class from another. The SVM finds this hyper plane using support vectors (training tuples) and margins (defined by the support vectors). Specifically, we used SMO-type decomposition method reported in [23].

For the NN classifier we used Multi Layer Perceptron (MLP), this is a feedforward neural network with one or more layers between input and output layer. Each neuron in each layer is connected to every neuron in the adjacent layers. The training or testing vectors are presented to the input layer, and processed by the hidden and output layers [11].

Random Forest was used to build model based in DT classifier, it is a meta-learner; it consisting of many individual trees. The random forest combines multiple random trees that votes on a particular outcome. In the random forest algorithm each vote is given equal weight. The forest chooses the classification that contains the most votes [17].

The model based in a DBN, consists of a series of time slices that represent the state of all the variables at a certain time, for each temporal slice, a dependency structure between the variables at that time is defined, called the base network, additionally, there are edges between variables from different slices, with their directions following the direction of time, defining the transition networks. DBNs are graphic models which represent probabilistic dependencies of a set of parameters and their relationships over time and can stablish causality among them [6].

# 2.3. Feature selection 

The set of gait related parameters from which probability of falling is calculated was identified by using three methods.

A first set of parameters was recommended by experts on clinical gait analysis based on previous studies to identify fallers among elderly population.

A second set was built using an automatic home-made algorithm named Feature Selection for Minority Class (FSMC) [5] which was applied using data of elders' gait in order to automatically select gait parameters able to distinguish people in the OP group from those in the normal group. The algorithm boils down to obtain the mean and standard deviation of each variable for the majority class (normal group) and the mean of the same variables for the minority class (OP group). If the mean value of the minority class is at least two standard deviations away from the mean value of the majority class, then that feature is selected as relevant.

A third set was built as a combination of the previous two sets.

## 3. Results

### 3.1. Subject's characteristics

One hundred twenty-six subjects were enrolled, and functional gait assessment was performed for each one of them, patients were asked to return every 6 months for a new data acquisition, for a period of 3 years, between each data acquisition patients were asked to report by phone call if they suffered a fall and this data was added to each one of the records (instance) of the patients. Due to different circumstances, in each new data collection, there was a smaller number of patients. For the first year of the study 16 patients stopped attending. For this reason, we only used the data collected from 110 patients in the first year of the study to the experiments reported in this research.

Table 1 shows characteristics and spatiotemporal gait parameters of normal and OP groups. 143 subjects were enrolled in the normal group (mean age $68.7 \pm 6.8$, height $151.7 \pm$ 6.4 , weight $65.2 \pm 10.9$, BMI $28.4 \pm 4.4$ ) whereas 110 subjects remained in the first year of the study in the OP group (mean age $74.3 \pm 6.3$, height $148.5 \pm 6.4$, weight $58.3 \pm 8.8$, BMI $26.5 \pm 3.8$ ).

According to literature OP group showed lower walking velocity [16] and step length [16] in comparison to normal group. They also showed higher ambulation time and lower cadence, stride length and normalized walking velocity. Normalized walking velocity

accounts for subject's height. OP group showed a statistically significant increment of ambulation time in the follow up at 6 months.

Table 1. Subject's characteristics and spatiotemporal gait parameters


BMI: Body Mass Index; LL: leg length; a Statistical significant difference between groups, T test independent samples ( $P \leq 0.05$ ); b Statistical significant difference between groups, Mann-Whitney test ( $P \leq 0.05$ ); d Statistical significant difference in OP group, Wilcoxon sign test ( $P \leq 0.05$ ).

# 3.2. Set of gait parameters relevant to predict falls 

Table 2 shows the three sets of gait parameters used to build the models. The first set, a priori knowledge given by the experts, Experts column, includes 4 parameters related mainly to spatial characteristics of gait (step length, stride length and base of support). The second set, FSMC column, developed using an automatic algorithm that emphasizes differences between OP group and normal group, includes 6 parameters, generally they aren't consider by the experts. All of them are related to temporal characteristics of gait. Finally, the third set is the mix of first and second sets, Mixed column, that is, in this set we considered spatial and temporal characteristics of gait.

Table 2. Parameters used to build the models


# 3.3. Model construction 

To create each model, the information from all 110 subjects across the 2 assessment sessions was used: first record ( 0 months), and second record ( 6 months from first record), thereby a total 220 records or instances were used. Each record was labelled as risk of falling or not risk of falling according to WHO-QSFE results made at the same time of gait functional evaluation together with the fall reported by the patients by phone between each record, falls reported between 0 months and 6 months, for the first record, and the falls reported between 6 month and 12 months, for the second record.

Then, the values of the relevant variables, for each sets of gait parameters showed in the Table 2, were binarized, according at follow:

1. Each of variable can take one of two values, $0=$ no change or normal deterioration, $l=$ change beyond normal deterioration.
2. To determine if a variable changed or not change, we validate if the patient's variable with osteoporosis (OP group) is in or out of the interval formed by the mean and the standard deviation of the value of same variable from the set of normal patients (normal group).
3. If value of a variable is in of interval, the variable changed, in other case, not changed.
Finally, all models for prediction of risk of falling 6 months after of initial gait assessment and after 6 months gait assessment were evaluated using 10 -fold cross validation where $10 \%$ of records are left out at a time and a model instance is trained with the remaining $90 \%$ of observations and tested on the $10 \%$ of observations initially left out. This procedure was repeated ten times randomly and predictive power is calculated as the average of all model instances. Accuracy, precision, recall, and F-score were calculated for each model.

### 3.4. Prediction models' performance

The global models' performance was assessment as a binary classification, i. e., two classes, positive or risk of falling, and negative or not risk of falling, are considered. So for each instance, the decision-making process falls into one of four possible scenarios: the sample is positive and the classifier correctly recognizes it as such (true positive or TP); the sample is negative and the classifier correctly recognizes it as such (true negative or TN ); the sample is positive but the classifier labels it as negative (false negative or FN ); or the sample is negative but the classifier labels it as positive (false positive or FP). The most representative measures of performance of a classifier, which we were used, are presented in Table 3.

The results of the models are presented in two parts. First, Table 4 shows the results scored for predicting risk of falling in period of 1 to 6 months (after initial gait assessment) named First Period, and the results scored for predicting risk of falling after 6 months until 12 months (after 6 months gait assessment) named Second Period, Table 5.

Measures such as accuracy and recall are common indicators to assess the efficiency of a model, but when it comes to the identification of a particular class, in our case, people with risk of falling, it is necessary to observe another type of measure, for example, F-score, which considers precision and recall metrics, this measure is the harmonic mean of these 2 metrics, as show in Table 3. The F-score is a good way to summarize the evaluation of a model in a unique number, and thus have a more complete evaluation of the behavior of a classifier.

Table 3. Measures used to assessment the models' performance


As shown in Tables 4 and 5, we obtain highest values in F-score when we use models based in DBN, this means that we have the best harmonic mean of precision and recall, i. e., we have models more efficient to identificate risk of falling in each periods of time analyzed, First and Second Period.

On the other hand, for the First Period, the results show that when we use a DBN model using the experts' variables together FSMC's variables, i. e., mixed variables set, we obtained the best accuracy and recall values, $80 \%$, and $73 \%$, respectively, to predict risk of falling in that period, in comparison of the others models. But, for the Second Period, the best values of accuracy, and recall were obtained using the FSMC's variables, $89 \%$ and $57 \%$ respectively, this is due at the number of falls in that period is less that in the first Period, see Table 1, and the FSMC is focused to identify the variables associated to minority class, in our case, variables associated to risk of falling.

Table 4. Models' performance for prediction of risk of falling in First Period.


Table 5. Models' performance for prediction of risk of falling in Second Period.


Finally, the Table 6 shows the comparation of results obtained with the best model built in our research, DBN using variables of the mixed set to predict risk of falling for the First Period, with the works reported in the literature.

Table 6. Research result comparation with the literature.


We can observe that the global accuracy got is less than the reported in [15] and [19], but the authors don't report the performance to identify the risk of falling using other measures, like precision or recall. In other hand, we have better accuracy that reported in works [7] and [6],

where the authors report the effectiveness to determine the risk of falling, using the recall measure and we have a less value in comparison of [6] that is probably due to number of patients and falls reported in that study, we have a less of number of falls.

# 4. Discussion 

Furthermore, the experts note that parameters selected by FSMC algorithm in order to distinguish patient in OP group with risk of falling from not risk of falling involve more time related measures such as ambulation time and differential step time. This finding contrasts with the parameters reported in the literature, where cadence and step length have been identified as distinctive markers of patients with risk of falling. Almost all spatiotemporal selected parameters either a priori or computing methods showed differences between normal and OP group. These differences could explain incidence of falls in OP group.

However, selection of differential step time by FSMC algorithm reveals the presence of spatiotemporal gait parameters which are not necessarily different among populations but could be related to risk of falling. This could be an advantage of automatic methods over traditional statistical approaches. But on the other hand, can be a limitation if not use complementary information, because of the only use of parameters obtained by FSMC on their own do not allow to build the best model, as the results show.

In general, we observe that the models' performance improves when using both sets of data, mixed variables, in comparison of only using the experts' variables. Moreover, is interesting to note that the best performances to determine the risk of falling after 6 months are obtained using only the variables obtained automatically, this could be a highlight that temporary variables are more relevant to predict fall risk after that time, although this does not mean that the experts' information should be discarded, it is complementary information for them, like show the results.

It is worth to remark that existing automatic models for classifying fallers from non-fallers are not directly comparable to our models [15, 19]. Furthermore, to the related works [6, 7] we have a comparison of the different models proposed in those researches, and we have showed that the DBN models get better performance to predict risk of falling in osteoporosis elders.

An important limitation of the DBN model is the binarization process of the data to avoid require high computational performance, in storage and processing, which can discard the use of information that can be relevant.

## 5. Clinical Implications

We have developed different models, but specifically we have built DBN models, whose global performance is better than the others, which can be useful for screening risk of falling of osteoporosis elders in the following 6 months after first record of gait data.

In contrast with the other models built, a DBN can model the evolution of the probabilistic dependencies within a system over time. In particular, variables are represented at multiple time points within the same network structure, like shows Figure 1.

![img-0.jpeg](img-0.jpeg)

Figure 1. Example of a DBN model built with experts' variables. For the gait related parameters subindex 1 (DBN's nodes in time 1) represents initial functional gait assessment, subindex 2 gait assessment at 6 months (DBN's nodes in time 1). Register of falls within next 6 months following each gait assessment as recorded by WHO-QSFE is represented by letter $\mathbf{C}$.

The graphic representation of a DBN (Figure 1), allows specialists in gait analysis understand easily the relationships amount the spatiotemporal gait parameters and the risk of falling.

Thereby, this model is feasible to be used in clinical practice, by using relatively simple equipment such as computerized walkways or accelerometers, with which is possible to get the value of the model's variables and the way to determine the risk of falling of elder.

It is clearly important due to the seriousness of the associated conditions and because it allows the establishment of an intervention to modify the associated risk within a reasonable time frame.

# 6. Conclusions 

DBN models get better performance than other models assess in this research and reported in the literature, also, developed DBN models not only reflect probabilistic relationships among gait parameters but also biomechanical relationships.

The completely computational model based on an automatic feature extraction algorithm selects a set of parameters to predict risk of falling of elders with osteoporosis, different from those recommended a priori by experts capable to distinguish elderly with risk of falling.

Therefore, a potential set of parameters to predict risk of falling in osteoporosis elders was proposed through the performance of DBN models that could be improved with priori recommendations including valuable knowledge that could not be obtained exclusively from the gait analysis data, i. e., the experts' knowledge incorporates information about risk of falling obtained from different studies in the same or other populations.

The results confirm the feasibility of computational methods to complement experts' knowledge to predict risk of falling within a period of time as high as 12 months. However, before applying this model in clinical practice further refinement is needed by improving the selected set of parameters as well as the sample structure and test performance of DBN's models for prediction of falls for period of times longer than 12 months.

# Conflict of interest statement 

No potential conflict of interest was reported by the authors.

## Funding

This work was supported by the Mexican National Council of Science and Technology CONACyT (grant number CONACYT-2003-42/A1).
