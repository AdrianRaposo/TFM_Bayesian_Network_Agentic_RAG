# A Novel Probabilistic Hybrid Model to Detect Anomaly in Smart Homes 

Sasan Saqaeeyan ${ }^{1}$, Hamid Haj Seyyed Javadi ${ }^{1,2, *}$ and Hossein Amirkhani ${ }^{1,3}$


#### Abstract

Anomaly detection in smart homes provides support to enhance the health and safety of people who live alone. Compared to the previous studies done on this topic, less attention has been given to hybrid methods. This paper presents a two-steps hybrid probabilistic anomaly detection model in the smart home. First, it employs various algorithms with different characteristics to detect anomalies from sensory data. Then, it aggregates their results using a Bayesian network. In this Bayesian network, abnormal events are detected through calculating the probability of abnormality given anomaly detection results of base methods. Experimental evaluation of a real dataset indicates the effectiveness of the proposed method by reducing false positives and increasing true positives.


Keywords: Smart homes, sensory data, anomaly detection, Bayesian networks, ensemble method.

## 1 Introduction

Today, the elderly population are increasing quickly. They tend to live independently more often. However, this trend has negative consequences, and there are significant concerns about health and safety of this group of people [Eyal, Hurst, Norheim et al. (2013); Häfner, Baumert, Emeny et al. (2012); Risteska Stojkoska, Trivodaliev and Davcev (2017)]. As such, a system to detect dangerous incidents and take appropriate timely action is necessary to protect the residents' health. Remote healthcare monitoring systems have provided a viable option to solve this problem [Caroux, Consel, Dupuy et al. (2018); Gomes, Muniz, da Silva e Silva et al. (2017)]. By rapid advances in technologies related to sensors and machine learning algorithms, a number of smart home's commercial applications have been building and have been using in common daily life [Dahmen, Cook, Wang et al. (2017); Gomez, Chessa, Fleury et al. (2019); Suryadevara and Mukhopadhyay (2015)]. The applications are used for automating works at home, optimizing energy consumption, activity recognition, and dangerous event increasing security such as health monitoring [Dahmen, Cook, Wang et al. (2017); Stojkoska and Trivodaliev (2017)].

[^0]
[^0]:    ${ }^{1}$ Department of Computer Engineering, Borujerd Branch, Islamic Azad University, Borujerd, Iran.
    ${ }^{2}$ Department of Mathematics and Computer Science, Shahed University, Tehran, Iran.
    ${ }^{3}$ Computer Engineering and Information Technology Department, University of Qom, Qom, Iran.
    * Corresponding Author: Hamid Haj Seyyed Javadi. Email: h.s.javadi@shahed.ac.ir.

Smart homes system consists of hardware and software [Amiribesheli, Benmansour and Bouchachia (2015); Chan, Estève, Escriba et al. (2008); Ni, García Hernando and Pau de la Cruz (2016)]. The hardware includes sensors, communication network, server, and a caregiver interface device. Sensors are installed in different places at home, objects, and resident's body. In smart homes, the events are sensed using the embedded sensors which are attached to the residents' body, objects, and places at home. The collected data is then processed and analyzed using machine learning algorithms on the server. In situations that could be dangerous for residents, they send an alarm to caregiver to perform appropriate reactions. Caregivers can control the various parts of the smart home via interface software [Bakar, Ghayvat, Hasanm et al. (2016)]. Fig. 1 shows the smart home components and its data cycle.
![img-0.jpeg](img-0.jpeg)

Figure 1: Smart home's data cycle
In recent years, many research studies are conducted on smart homes to detect residents [Lesani, Ghazvini and Amirkhani (2019)], recognize residents' activities [Alemdar, van Kasteren and Ersoy (2017); Lara and Labrador (2013); Ni, García Hernando and Pau de la Cruz (2016); Yang, Jafari, Sastry et al. (2009)], predict activities and events [Nazerfard and Cook (2015)], and detect abnormal activities [Bakar (2016); Song, Wen, Lin et al. (2013); Zhu, Sheng and Liu (2015)]. However, these homes are immature in some aspects, such as the anomaly detection, security of software system, self-healing hardware failure, and the cost of installation and maintenance [Dahmen, Cook, Wang et al. (2017); Suryadevara and Mukhopadhyay (2015); Theoharidou, Tsalis and Gritzalis (2017)]. This paper presents a method for detecting anomalies in the pattern of residents' life from sensory data in a smart home.
Anomaly or outlier is defined as an object or data point that differs from other objects or the rest of data points [Chandola, Banerjee and Kumar (2009); Steen, Frenken, Eichelberg et al. (2013); Tonejc, Güttes, Kobekova et al. (2016)]. Accordingly, abnormal events or activities in the smart home are patterns in sensory data that do not conform subjects' past behavior patterns. Because abnormal events such as falling on the floor, and heart attack occur very rarely in the real life, it is an imbalanced problem. Moreover, we encounter a one-class problem, and our purpose is to detect novelties in the sensory data. The novelty

is new or unknown objects which differ from historical data. Because of the similar solutions for anomaly detection and novelty detection, these terms are used interchangeably in the literature [Pimentel, Clifton, Clifton et al. (2014)]. Novelty detection methods are used to detect unknown data points when the number of abnormal data is not sufficient for learning their pattern [Ding, Li, Belatreche et al. (2014); Pimentel, Clifton, Clifton et al. (2014)].
Various studies have been performed to detect one or more aspects of the anomaly (time, duration, location, sequence, etc...) through the use of different algorithms in smart homes [Bakar (2016); Dahmen, Cook, Wang et al. (2017)]. Each of these researches has its advantages and disadvantages, but they all suffer from a lack of an appropriate model to detect anomaly in different conditions and aspects. To alleviate this problem, we present a two-step ensemble method to aggregate the results of different methods. In the first step, it detects anomalies from sensory data using different novelty detection methods. Then, it builds a directed probabilistic graphical model (Bayesian network) which is used to calculate the probability of the current event given the results of other anomaly detection methods. If the probability is lower than a certain threshold, the model considers this event as an anomalous one.
The main contributions of this work are as follows:

- Presenting a probabilistic hybrid method based on Bayesian networks.
- Determining conditional independence relationships between different algorithms using the Bayesian network's d-separation algorithm.
The rest of the paper is organized as follows: Section 2 reviews the related work on novelty detection in smart homes. Section 3 briefly describes the Bayesian network and conditional independence. The proposed method is presented in Section 4 and it experimentally evaluated and discussed in Section 5. Finally, Section 6 concludes our work.


# 2 Related work 

Various methods have been used for anomaly detection in smart homes. These approaches can be categorized according to the type of anomaly, type of used sensor, and level of data analysis. Generally, there is three type of anomaly: point anomaly, contextual anomaly, and collective anomaly [Han, Pei and Kamber (2011); Anderson, Ros, Keller et al. (2012); Hoque, Dickerson, Preum et al. (2015)]. Furthermore, anomaly detection methods in smart homes are categorized into three classes based on sensor type: visual-based sensors, wearable sensors, and distributed sensors [Zhu, Sheng and Liu (2015); Lara and Labrador (2013); Yin, Yang and Pan (2008)]. Also, they divided into two class depending on the level of data analysis [Bakar, Ghayvat, Hasanm et al. (2016)]: detection of anomaly in activities and detection of anomalies in sensory data. In this paper, anomaly detection methods in smart homes are categorized into five categories according to the used algorithm [Pimentel, Clifton, Clifton et al. (2014)], as is reviewed in the following subsections.

### 2.1 Statistical methods

Statistical methods detect an object or data as an anomaly if the object is in the low-density areas of the training set. These areas have a high probability of containing abnormal objects.

These methods are categorized into parametric and nonparametric methods. The parametric methods assume a parametric distribution to generate the normal data. They define a probability function $f(x, \Theta)$ to calculate the probability of object $x$ with the parameters $\Theta$. The nonparametric methods do not assume a hypothesis in advance but try to determine the distribution from the input data [Ding, Li, Belatreche et al. (2014); Pimentel, Clifton, Clifton et al. (2014)].
Nonparametric statistical methods: Histogram is a nonparametric statistical method. Song et al. [Song, Wen, Lin et al. (2013)] calculated the number of times that an activity is repeated in a place and used that to detect anomalous behaviors according to the daily histogram changes. However, methods based on the histogram do not consider dependency between the features.
Parametric statistical methods: Three main parametric statistical methods used for anomaly detection are Dynamic Bayesian Network, Gaussian Mixture Model (GMM), and Hidden Markov Model (HMM).
Zhu et al. [Zhu, Sheng and Liu (2015)] use enhanced first-level Dynamic Bayesian network and added time as a new node. They proposed a coherent anomaly detection model to detect different types of anomalies in four contexts: spacing, timing, sequence, and duration of activities. They proposed to first recognize activities and then detect abnormal activities. This may propagate the errors from the activity recognition phase to anomaly detection.
Cardinaux et al. [Cardinaux, Brownsell, Hawley et al. (2008)] trained a GMM using normal data. They used rule-based algorithms to recognize activities and defined a set of characteristics consist of the start time, duration, weekday, and activity level to detect anomalies. GMM was trained for each type of pre-defined activities. Activities which get a probability lower than a threshold are considered as an anomaly. The GMM can consider dependencies between features for modelling, but it is not appropriate when the work comes with high dimensions or features. Rashidi et al. [Rashidi, Cook, Holder et al. (2011)] proposed to detect and track frequent resident's lifestyle activities. They defined irregular activities as an abnormality. In the first phase, a varied-order sequence miner discovers frequent patterns of sensor events. These patterns are grouped into clusters of frequent activities. In the second phase, a voting Multi-HMM system tracks frequent activities. Sensor events represent observable states and activity labels are hidden states. Ghayvat et al. [Ghayvat, Mukhopadhyay, Shenjie, et al. (2018)] proposed to perform real-time anomaly detection. They created an anomaly prediction model based on the active periods and inactive periods of objects. They defined two parameters for assessing the health of residents. The first parameter indicates that the resident does not use home's objects temporary or ever, and second parameter indicates if the resident uses objects dynamically or temporary. They used a time series to define trend of activities. If the current activity is outside the range of duration of routine activity, it is considered as an anomaly.
Generally, the small size of training dataset in statistical methods decreases performance [Ding, Li, Belatreche et al. (2014); Han, Pei and Kamber (2011)].

# 2.2 Distance-based methods 

Distance-based methods assume an object as an anomaly if the proximity of the object with its neighbours has a considerably different from the proximity of other objects with their neighbours in the same data set [Shams Shirazi (2017)].
Liao et al. [Liao, Kong and Wang et al. (2017)] used the local outlier factor (LOF) model to detect anomalies and defined three features including start time, times, and duration. They calculated behavior anomaly degree using k-nearest neighbours, the density of the feature vector and reachability distance between two feature vector. Also, they performed a deeper analysis of anomalies. They built a visual system. It visualized residents' daily activities from different views such as reasons of the anomaly, activities which have more impact on the anomaly, date of the anomaly. Parvin et al. [Parvin, Chessa, Manca et al. (2018)] presented an architecture that has two main parts. The first part analyzes and models resident's behaviors, and the second part performs real-time analysis, to identify the deviations, and propose appropriate activities to prevent anomalies based on the degree of anomaly. Their approach detected anomalies in the sequence of activities at the end of the day and detected online anomalies in the substring of activities throughout the day. Online detection of anomaly and determine the degree of anomaly are advantages of their method. However, they used pre-defined activities.
Distance-based methods require definite appropriate distance measure for the given data. Thus, when there is data with high-dimensional, they cannot accurately discriminate between normal and abnormal data points [Ding, Li, Belatreche et al. (2014); Shams Shirazi (2017)].

### 2.3 Domain-based methods

These methods draw a boundary around the normal data points out of this boundary are considered as anomaly [Pimentel, Clifton, Clifton et al. (2014)].
Shin et al. [Shin, Lee and Park (2011)] defined three features: activity level to model an individual's behavioral pattern: motion level, and non-response interval. Activity level was used to detect abnormal physical conditions such as weaknesses. Motion level was related to the resident's general health and detected diseases such as altered mental status. Nonresponse interval was for unresponsive statues such as when a person is found dead. They combined these three features and used Support Vector Data Description (SVDD) to detect abnormal behavioral situations. Yin et al. [Yin, Yang and Pan (2008)] focused on abnormal activities to reduce the false positive rate. They applied a One-Class Support Vector Machine (OCSVM) to detect abnormal activities. Then, they used a kernel nonlinear regression (KNLR) to filter the suspicious activities for more investigation. This study does not focus on the false negative rate. Domain-based methods require to choose an appropriate scaling method for their features. Moreover, because of locating the boundary just using the training data, there are outliers in training data that can influence the model [Ding, Li, Belatreche et al. (2014); Pimentel, Clifton, Clifton et al. (2014)].

# 2.4 Reconstruction-based method 

These methods build a regression model to compare the target (reconstruction data) with the actual observed data. An object is detected as an anomaly if the reconstruction error is 1 significant [Pimentel, Clifton, Clifton et al. (2014)]. Neural networks are a type of used reconstruction-based methods. Novák et al. [Novák, Biñas and Jakab (2012)] trained selforganizing map (SOM) based on the normal data and clustered activities. They defined a 2-dimensional data input. The first dimension represented the time of entry to a location and the second dimension was the duration of staying there. Activities that differed from the cluster group were detected as anomalies. They used the first-order Markov model to calculate the probability of transition between two activities. Reconstruction-based methods depend on a number of hyper-parameters to build the model structure [Ding, Li, Belatreche et al. (2014); Pimentel, Clifton, Clifton et al. (2014)].

### 2.5 Hybrid methods

A combination of algorithms can be used to alleviate the shortcoming of different methods. They are known as ensemble or hybrid methods. The results of based methods are combined in a final module or the results of one part is sent to another part as input.
Forkan et al. [Forkan, Khalil, Tari et al. (2015)] used different algorithms to detect anomalies for various contexts of individual life. An HMM detected changes in the location and sequence of activities. Gaussian distribution detected changes in routine behaviors. Also, they analyzed vital signs using statistical methods. Then, a fuzzy model fused their outputs to make the final decision. This study defined different levels for anomalies to perform proportional reactions for each level. Their study reduced false alarms rate. Ordóñez et al. [Ordóñez, Toledo and Sanchis (2015)] recognized the behavior patterns of occupants using the Bayesian statistic. They defined three probabilistic features: sensor activation likelihood (to detect individual health), sensor sequence likelihood (to recognize consciousness), and sensor duration likelihood (to determine the physical condition of an individual). The probability of each feature was calculated using Bernoulli, multinomial, and Gaussian distributions, respectively. The main advantage of this method is that it uses prior knowledge and efficiently and quickly combines this knowledge with the new sensory data via Bayesian theory. This study only detects specific aspects of anomalies.
The aforementioned methods have their advantages and disadvantages. However, to the best of our knowledge, no attempt has been made to obtain the most appropriate ensemble models. The present paper focuses on these cases and aims to determine the structure of the Bayesian network to fuse the results of other anomaly detection methods from different categories.
Fig. 2 shows the classification of smart homes' applications and components. As is clear in this chart, anomaly detection is a subgroup of the health of residents.

![img-1.jpeg](img-1.jpeg)

Figure 2: Smart homes' applications and components

# 3 Bayesian networks 

Bayesian network is a probabilistic directed acyclic graphical model. Its nodes correspond to random variables and its edges represent statistical conditional dependency relationships between nodes. These networks calculate the joint probability of distribution of $n$ variables using Eq. (1) [Heckerman, Geiger and Chickering (1995); Koller and Friedman (2009)]:
$P\left(X_{1}, X_{1}, \ldots, X_{n}\right)=\prod_{i} P\left(X_{i} \mid \operatorname{Parent}\left(X_{i}\right)\right)$
where $\mathrm{X}_{\mathrm{i}}$ indicates a random variable and $\mathrm{Pa}\left(\mathrm{X}_{\mathrm{i}}\right)$ is its parents.

# 3.1 Building and using a Bayesian network 

The process of building and using a Bayesian network with complete data consists of three steps of structure learning, parameter learning, and inference [Heckerman, Geiger and Chickering (1995); Koller and Friedman (2009)]. Network structure represents relationships between nodes with each other. An unknown structure can be learned using two major approaches: score-based and constraint-based methods. In addition to the training data, experts' knowledge can be exploited to obtain a more accurate network structure [Amirkhani, Rahmati, Lucas et al. (2016)]. Network parameters are the conditional probability distribution of random variables given their parents. Parameter learning estimates conditional probability tables (CPTs) based on the training data and network structure [Heckerman, Geiger and Chickering (1995); Koller and Friedman (2009)]. After learning the structure and parameter, the model can be used to answer probabilistic queries about random variables. This step is called inference which can be exact or approximate [Heckerman, Geiger and Chickering (1995); Koller and Friedman (2009)].

### 3.2 Conditional independence relationships

The Bayesian network structure can be investigated to extract the conditional independence relationships. It indicates whether nodes X are conditionally independent of Y , given nodes Z, denoted by $(\mathrm{X} \perp \mathrm{Y} \mid \mathrm{Z})$ [Cooper and Herskovits (1992)]. A node can have a relationship with another node either directly or indirectly.
If they are directly connected, they are correlated regardless of any other variables as evidence. Fig. 3 shows all types of indirect connections between X and Y via Z .
![img-2.jpeg](img-2.jpeg)

Figure 3: Relations between node X and Y via Z
A path between two nodes (or two sets of nodes) without considering the directions is called a trail. A trail between nodes X to Y via Z is called active if influence can flow from X to Y via Z ; otherwise, it is called blocked. In Fig. 3(a) (indirect causal effect), Fig. 3(b) (indirect evidential effect) and Fig. 3(c) (common cause), node X can influence node Y if and only if Z is unobserved and is denoted by $\mathrm{X} \perp \mathrm{Y} \mid \mathrm{Z}$. It means the trail between X and Y via Z is active if and only if Z is unobserved. In Fig. 3(d) (common effect or v-structure), influence can flow on the trail between X and Y via Z if Z is observed.
X and Y are called d-separated given Z if there is no active trail between any node $\mathrm{x} \in \mathrm{X}$ and $\mathrm{y} \in \mathrm{Y}$, given Z (it is denoted by $\mathrm{d}-\operatorname{sep}(\mathrm{X}, \mathrm{Y} \mid \mathrm{Z})$ ). The concept of d-separation can be used to determine conditional independence relationships between different nodes of a Bayesian network [Cooper and Herskovits (1992)].

# 4 The proposed method 

This section explains the details of the proposed hybrid method based on the Bayesian network to detect anomalies from collected sensory data in smart homes. The proposed model has two phases for detecting anomalies. In the first step of our method, it detects anomalies using various base methods with different types explained in Section 2. Subsequently, all methods are employed on the validation set and (obtained by crossvalidation) and build a new dataset containing the prediction of these methods and actual labels. This set is used for training the Bayesian network in the next phase. There is one node for each base anomaly detection method in this Bayesian network. Finally, learned Bayesian network is used to calculate the probability of abnormality for the test samples given the prediction of the base methods. A sample is detected as an anomaly if its probability of abnormality is greater than its normal of being normal. As is depicted in Fig 4, the proposed model works in five steps: pre-processing, base anomaly detection, building the Bayesian network, final anomaly detection and model evaluation.
![img-3.jpeg](img-3.jpeg)

Figure 4: The proposed architecture for anomaly detection in smart homes

### 4.1 Pre-processing

This phase consists of data cleaning, data conversion, features extraction, data normalization, and dataset splitting. Raw sensory data are collected in a dataset. Each record of the dataset

includes three features: time, date and the on/off states of different sensors. Time attributes are discretized based on $|a / b|+1$ where $a$ is the minute part of the time when a sensor's state changes, $b$ is an integer in $\{15,30\}$, and $|$.$\mid$ shows the floor function. For example, if time is 10: 21, $a$ is 21 . For $b=15$, time will map to 103 . Missing data and unused features are eliminated, for example, some records have their time of switching on, but their time of switching "off" missed. Table 1 shows the defined features based on the prepared data. The prepared data is then split up into two subsets: train and test sets.

Table 1: Features used in the proposed system


# 4.2 Base anomaly detection methods 

In this phase, we choose multiple novelty detection algorithms from different categories including statistics, distance based, domain based, reconstruction, and ensemble methods. Cross-validation strategy is employed to split the training data to training and validation sets. Various models are learned using the training subset. Then, the trained models are employed on the validation subset to form the training dataset for the next step. Tab. 2 illustrates the selected base anomaly detection methods. They are chosen according to the defined categories in Section 2 since the diversity of the methods is an important factor for the success of ensemble methods.

Table 2: The selected base anomaly detection methods



# 4.3 Building the Bayesian network 

This phase consists of four main parts: composing a results dataset, split up results dataset, structure learning, and parameter learning.
First, prediction results of train data for anomalies detection with the actual results, which are correct classification results of data, to build new results dataset. Each column of the dataset includes prediction results of one model, and the last column is actual results. Then, random variables are defined corresponding to each column of result dataset, a Bayesian network is trained based on the predicted training data. Finally, predication of test data and trained model will be sent to the next phase for the second step of anomaly detection. Tab. 3 shows samples of results dataset. If value of cell $_{\mathrm{m}, \mathrm{n}}$ is 1 , it represents that method $_{\mathrm{n}}$ has detected record $_{\mathrm{m}}$ of the first dataset as an anomaly.

Table 3: Results dataset includes anomaly detection results and actual results


### 4.4 Final anomaly detection

The trained model is used for final anomaly detection in three steps: inference, detect anomaly, and alarm to a caregiver.

- Inference: Each record of the test dataset is given to the trained Bayesian network and it calculates $\mathrm{p}(\mathrm{r} \mid$ evidence $)$, where r is the final label of the current record and evidence constitutes the predictions of the base anomaly detection methods.
- Anomaly detection and alarm: For the calculated probabilities, if p (normal $\mid$ evidence) $<\mathrm{p}$ (anomaly $\mid$ evidence), then the record is detected as an anomaly, and an alarm notification is generated in the next step.

# 4.5 Model evaluation 

Model evaluation is performed to study the performance of the proposed model. For this purpose, F-score and area under the curve (AUC), explained in Section 5.1, are calculated. Then, the d-separation algorithm is used to determine the conditional independence relations between nodes of the Bayesian network that demonstrate the relations between the used methods in the trained Bayesian network.

### 4.6 Pseudo-code of the proposed method

A pseudo-code of the proposed method is presented in Algorithm 1. It receives the training and test data. In each step of the outer loop, one model is selected. The inner loop is used for training and testing models. Model_Set is an array containing the base anomaly detection methods. The cross-validation process is repeated k times and ThisRoundDatasets indicates the current iteration. After building the Bayesian network, the trained model performs inference for each record in the test data to estimate its probability of being anomalous.

```
Algorithm 1 Proposed Algorithm
    Input: Training Dataset \(\left(\mathrm{D}_{\text {train }}\right)\),
        Testing Dataset \(\left(\mathrm{D}_{\text {test }}\right)\)
    Output: Evalution \(_{\text {metric }}\),
        Conditional Independence relationships
(Model_Set is an array containing base anomaly detection methods,
and CV refers to cross validation )
    BN_dataset = an empty dataset with models in Model_Set as features
FOR each subModel in Model_Set do
    FOR each \(\mathrm{CV}_{\text {train }}, \mathrm{CV}_{\text {test }}\) in CV[ThisRoundDatasets] do
    tempModel \(=\) Train a subModel on \(\mathrm{CV}_{\text {train }}\)
    tempPred \(=\) Apply the tempModel on \(\mathrm{CV}_{\text {test }}\)
            Add tempPred to BN_dataset[subModel]
BN_structure \(=\) HillClimbSearch(BN_dataset,scoring_method=K2Score)
    BN_parameters \(=\) ParameterEstimation(BN_dataset,BN_structure)
    Model \(=\) BayesianNetwork(BN_strucutre, BN_parameters)
For each record in \(\mathrm{D}_{\text {test }}\) do
    Probability \(=\) Inference(Model, record)
    IF Probability \(<0.5\) THEN
    Mark this record as an anomaly
```


## 5 Experimental evaluation

In this section, we evaluate the proposed method compared to alternative approaches.

# 5.1 Experimental setup 

The Kasteren dataset [van Kasteren, Englebienne and Kröse (2010)] is used for the evaluation of our work. This dataset consists of real-data records gathered from the daily life of a single-resident smart home apartment for 28 days. They used RFM DM 1810 kits to build a wireless network of nodes. Binary distributed sensors including Contact Switches sensors and pressure sensors are installed in different parts of the home, such as entrance door, beds, and kitchen, including freezer, microwave, and cabinets. Fig. 5 shows the smart home with the sensors marked by red signs. Records of the raw dataset have three fields: ID (sensor id), Start time (when the sensor switches on), and End time (when the sensor switches off). The sensory data gathered from daily life are considered as normal data. We manually generated a number of abnormal samples for the Kasteren dataset based on unusual behavior and statistical information of the dataset. They differ from the rest of the dataset in the time, location, sequence, or interval time between the switching on/off the sensors. Other abnormal samples were generated by the algorithm used in Novák et al. [Novák, Biñas and Jakab (2012)].
![img-4.jpeg](img-4.jpeg)

Figure 5: The location of the sensors in the smart home used in the experiments [van Kasteren, Englebienne, and Kröse (2010)]

## Evaluation criteria

We calculated the confusion matrix that consists of the following four cells:

- TP: Total number of abnormal records that are correctly detected.
- FP: Total number of normal records that are incorrectly detected as abnormal.
- TN: Total number of normal records that are correctly detected as normal.
- FN: Total number of abnormal records that are incorrectly detected as normal.

The used classification evaluation criteria are as follow [Han, Pei and Kamber (2011); Murphy (2007)]:

- Recall $=\mathrm{TP} /(\mathrm{TP}+\mathrm{FN})$
- Precision $=\mathrm{TP} /(\mathrm{TP}+\mathrm{FP})$
- $\mathrm{F} 1=(2 \times$ Precision $\times$ Recall $) /($ Precision + Recall $)$
- Receiver Operating Characteristics (ROC): ROC is a two-dimensional curve that shows the TP rate against the FP rate.
- AUC: The area under the ROC curve.


# 5.2 Experimental results 

The proposed system is implemented in python. For the first anomaly detection step, we used Python Outlier Detection (PyOD) which is an effective anomaly detection toolkit [Zhao, Nasrullah and Li (2019)]. Pgmpy is used to train the Bayesian network for final anomaly detection. It is an open-source python library for building probabilistic graphical models [Ankan and Panda (2015)]. Two other known ensemble approaches are compared with the proposed model: simple stacking and bagging. Simple stacking is similar to our proposed method but its final classifier is a simple logistic regression instead of Bayesian network. Bagging is a technique that bootstraps the training data into different sets, train a classifier on each set, and calculates the final result by majority voting [Han, Pei and Kamber (2011)]. Fig. 6 shows the structure of the trained Bayesian network (Y_true indicates final result). The K2 algorithm is used for structure-learning and Bayesian estimation for parameter learning [Amirkhani and Rahmati (2015)].
![img-5.jpeg](img-5.jpeg)

Figure 6: Trained Bayesian network based on the results of base methods

# Evaluation 

The evaluation results of the proposed method and base methods are presented in Tab. 4. It is clear that the proposed hybrid method obtains better F-score compared to the base anomaly detection methods. Especially, its precision is considerably higher than the base methods.

Table 4: Evaluation results


Tab. 5 shows the experimental results comparing the proposed method with the competing ensemble approaches. Fig. 7 shows the ROC curves of the proposed model and two competing ensemble methods. The results presented in Tab. 6 suggests that the proposed hybrid model achieves a significantly higher AUC.

Table 5: Comparison of different ensemble methods


![img-6.jpeg](img-6.jpeg)

Figure 7: The ROC curves of the ensemble models under investigation

Table 6: AUC of ensemble methods


Finally, Tab. 7 shows the calculated confusion matrix for the proposed method. Clearly, it is successful in detecting the anomalies while keeping the normal records correctly.

Table 7: The confusion matrix of the proposed method


# 5.3 Conditional independence relationships 

In this section, we determine conditional independence relationships between different nodes of Fig. 6 using the d-separation algorithm. Tab. 8 shows these relations. It indicates conditional independencies between different used anomaly detection methods. For example, the first row indicates that given the result of MCD and Naïve Bayes methods, all the methods in $\{$ KNN, CBLOF, LOF, IForest, OCSVM, PCA $\}$ are independent of Y_true.

Table 8: Conditional independence relationships between different algorithms


### 5.4 Discussion

The proposed hybrid model resembles the stacking approach to ensemble learning, but it uses the Bayesian network to aggregate the results of base classifiers in the second layer. According to the results shown in Tab. 4 and Tab. 5, the idea of using a new probabilistic hybrid method based on Bayesian networks to detect anomalies in smart homes is promising. This method outperforms the competing approaches. Also, the proposed method is suitable for different conditions because methods are employed from different domains of novelty detection.
Evaluation results of ROC curve (Fig. 7) shows that the Bayesian network structure has made proper relation between different methods (nodes) for final anomaly detection in a way to decrease false alarm rate and increase the true positive rate.

The anomalies in the proposed method are detected using the sensory data. Hence, proposed method in comparison to abnormal activities detection methods [Ghayvat, Mukhopadhyay, Shenjie et al. (2018); Parvin, Chessa, Manca et al. (2018)], which have used pre-defined activities, can detect different anomaly types in the life pattern such as: time, sequence, and duration. For example, late waking-up can be detected using the unusual start and end times of the events.
Determining relations between used methods in the proposed model (Tab. 8) is an effective achievement that indicates the relationships between different base methods from different domain. In addition, since careful selection of the base methods can result in a better ensemble performance, the proposed approach can be used to choose (nearly) independent methods to be used in the ensemble methods.
The main limitation of this approach in comparison with the methods presented in Forkan et al. [Forkan, Khalil, Tari et al. (2015); Ordóñez, de Toledo and Sanchis (2015)] is that it is unable to detect the anomaly type to perform appropriate reactions (i.e., normal, warning, and alert emergency [Novák, Biñas and Jakab (2012)].

# 6 Conclusion 

This paper proposed a novel multi-phase probabilistic hybrid model for anomaly detection in smart homes which is going to promote the residents' safety and health. The anomalies are detected in two steps. First, we deployed methods with different characteristics to obtain an initial guess of available anomalies from the sensory data. Then, we used a Bayesian network to hybridize their outputs. Experimental results using a real dataset found the proposed method strikingly efficient. The aim of this paper was to detect anomalies in smart homes, but the proposed framework can be applied to other areas as well. Also, in our experiments, some methods were detected to be conditionally independent of other methods. In future studies, we intend to improve the model through the combination of carefully selected methods according to their correlations. Moreover, we will extend the current model by using wearable sensors to investigate more aspects of anomaly in smart homes.
