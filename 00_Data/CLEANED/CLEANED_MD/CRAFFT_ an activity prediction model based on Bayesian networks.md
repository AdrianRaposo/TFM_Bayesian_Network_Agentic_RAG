# HHS Public Access 

Author manuscript
J Ambient Intell Humaniz Comput. Author manuscript; available in PMC 2015 April 29.
Published in final edited form as:
J Ambient Intell Humaniz Comput. 2015 April 1; 6(2): 193-205. doi:10.1007/s12652-014-0219-x.

## CRAFFT: An Activity Prediction Model based on Bayesian Networks

Ehsan Nazerfard and<br>School of Electrical Engineering and Computer Science, EME 206 Spokane Street, Washington State University, Pullman, WA USA, Tel.: +1 425 518-7974

## Diane J. Cook

School of Electrical Engineering and Computer Science, EME 121 Spokane Street, Washington State University, Pullman, WA USA, Tel.: +1 509 335-4985

Ehsan Nazerfard: nazerfard@eecs.wsu.edu; Diane J. Cook: cook@eecs.wsu.edu


#### Abstract

Recent advances in the areas of pervasive computing, data mining, and machine learning offer unique opportunities to provide health monitoring and assistance for individuals facing difficulties to live independently in their homes. Several components have to work together to provide health monitoring for smart home residents including, but not limited to, activity recognition, activity discovery, activity prediction, and prompting system. Compared to the significant research done to discover and recognize activities, less attention has been given to predict the future activities that the resident is likely to perform. Activity prediction components can play a major role in design of a smart home. For instance, by taking advantage of an activity prediction module, a smart home can learn context-aware rules to prompt individuals to initiate important activities. In this paper, we propose an activity prediction model using Bayesian networks together with a novel two-step inference process to predict both the next activity features and the next activity label. We also propose an approach to predict the start time of the next activity which is based on modeling the relative start time of the predicted activity using the continuous normal distribution and outlier detection. To validate our proposed models, we used real data collected from physical smart environments.


## Keywords

Bayesian Networks; Activity Prediction; Activity Recognition; Smart Environments; Prompting; Clustering

## 1 Introduction

With remarkable advances in pervasive sensing technology, networking, and various machine learning and data mining methods, we are rapidly moving into the world of ubiquitous computing. One research area that has benefited from the aforementioned advancements is smart environments. A smart environment, such as a home, is defined as an

environment that can acquire and apply knowledge to adapt to its inhabitants lifestyle in order to improve their experience in the environment (Cook and Das 2005). The main goal of such technologies is to achieve greater comfort, productivity, and energy efficiency. Over the last decade, researchers have come to realize the importance of applying smart home technologies for health monitoring (Pollack 2005; Helal et al. 2005; Lotfi et al. 2012; Holder and Cook 2013) and companies are recognizing the potential of such technologies in the market (Just Checking 2013).

In many smart home projects, the ultimate goal is to automate residents' interactions with the environment; in particular they target interactions which are repetitive or cumbersome to perform for older adults or patients with cognitive impairments. An example of an assistive living technologies is a remote health monitoring system that monitors and tracks the activities of daily living (ADLs) (Reisberg et al. 2001) for older adults with memory impairment. ADLs consist of self-care activities such as taking medication, eating, sleeping, cooking and dressing. The ability to perform ADLs completely and independently on a regular basis provides measurement of the functional status of residents, if they want to live independently in their own homes. Moreover, such systems can provide timely prompts to the residents in case they forget to perform important ADLs.

When older adults with cognitive impairment fail to initiate or complete everyday ADLs, caregivers are often responsible to monitor ADLs and provide a reminder or prompt The prompt is defined as any form of verbal or non-verbal intervention delivered to an individual on the basis of time or context to help the successful completion of an activity. The mentioned interventions are time consuming and cumbersome and often impact negatively on the caregiver's own health. Smart home technologies that can detect when assistance is needed and automatically deliver prompts can potentially reduce caregivers' burden and allow aging adults to retain their functional independence longer.

While reminder systems have been explored deeply in the literature, few take an individual's behavioural patterns into account to provide context-aware prompts; despite the fact that studies suggest activity-aware prompts offer significant advantages over traditional timebased prompts (Kaushik et al. 2008). Temporal activity prediction module is the component that can provide the behavioural pattern for the individuals. By taking advantage of such a prediction module, a reminder system can customize its behaviour to fit the lifestyles of the residents with no input on their part.

Our technology utilizes data collected from a smart home to learn context-aware rules for prompting the resident of the home to initiate important daily activities. We assume that sensor data is collected in a home while an individual performs her routine daily activities. We also assume that the training data is available from when the resident was performing the activities correctly or was prompted by a care-giver to initiate daily activities. Finally, we assume that we are given a list of critical activities for which the resident needs to be prompted.

The following scenario underscores the role of an activity prediction component together with the activity recognition module to provide an automated context-aware prompt, under

the assumption that "Taking Medication" is considered to be a critical activity (Nazerfard and Cook 2013):
"In the morning, the activity recognition module recognizes that the breakfast activity has occurred. Then the activity prediction component, which has already been trained with the correctly performed activities, makes the following prediction with a high enough confidence: The "Taking Medication" activity should follow within 30 minutes". Then the activity prompting system would have a relative time offset when "Taking Medication" usually happens. When the typical timespan passes and the medication is not taken, a prompt is delivered."

In this paper, we present a prediction model which employs Bayesian networks in a novel two-step inference process. While the focus on the current work is to predict the next activity that an older individual performs in the smart home, the proposed two-step inference process is not limited to the prediction problem and can be extended to other domains as well. In order to predict the start time of the next distinct activity, we propose a method based on a model of the relative start time of the activity using the continuous normal distribution and outlier detection. The rest of this paper is structured as follows. We first provide some related studies in the area of smart environment focusing on the activity prediction task. Next, we present a background overview for probabilistic graphical models. We then present the details of the proposed activity prediction approach, both for the activity label prediction and the relative start time prediction. We then provide the evaluation results for the proposed prediction approach. We end the paper by providing some concluding remarks together with future directions.

# 2 Related Work 

Over the past decade, a number of smart environment tes-beds have been deployed, including the CASAS project (Cook et al. 2013), PlaceLab (Intille et al. 2006), the Gator Tech Smart House (Helal et al. 2005), iDorm (Doctor et al. 2005), the Georgia Tech Aware Home (Abowd and Mynatt 2004) and the MavHome project (Das et al. 2002). In addition to creating physical testbeds, researchers have designed approaches to track locations and activities of the inhabitants, deliver timely prompts, discover abnormal behaviour and predict occupants' future activities. The differences among existing approaches can be categorized as follows:

1. Differences in sensor modalities used to monitor activities. These include but are not limited to: infra-red motion sensors (Cook et al. 2013), supervision cameras (Mocanu et al. 2011), wearable sensors (Ghasemzadeh et al. 2010), accelerometers (Yin et al. 2008), and RFID tags (Philipose et al. 2004).
2. Differences in models designed to learn activity patterns. These include but are not limited to: decision trees (Maurer et al. 2006), Bayesian networks (Kasteren and Krose 2007), association rule mining (Nazerfard et al. 2011), and artificial neural networks (Mahmoud et al. 2013).

3. Differences in experimental conditions. These include but are not limited to: smart environment residents perform scripted activities (Maurer et al. 2006) and residents perform normal unscripted daily living activities (Rashidi et al. 2011).

Based on the aforementioned advancements, researchers have recognized the importance of employing smart home technologies for health monitoring and assistance (Barger et al. 2005; Yu 2008; Tapia et al. 2010; Lotfi et al. 2012) and companies are recognizing the potential of such technologies in the market (BrainAid 2013).

In an assistive smart home, an activity recognition is a key component and many groups have looked into that (Duong et al. 2005; Liao et al. 2005; Heung-II et al. 2010); however, less attention has been given to the activity prediction problem. As smart environments become more prevalent, an important function that they require to possess is the ability to predict the occurrence of various events, such as the activities that residents perform, in order to have the visibility to make decisions in various situations. In the machine learning literature, "Prediction" too often refers to "sequential prediction" (Gopalratnam and Cook 2004); where the goal is to predict the next event based on a known limited history of past events.

The researchers in Tapia et al. (2010) take advantage of the activity prediction module to intervene and interact with the user as a means of reminding the user and preventing accidents. Also in an approach called Temporal Relation Discovery of Activity Patterns (TEREDA) (Nazerfard et al. 2011), the authors employ clustering techniques to discover typical wall-clock start times of activities. In this work, the authors model each activity as a normal mixture distribution and make use of association rule mining to discover temporal relations of daily activities. Furthermore, the authors in Mocanu and Florea (2012) propose a multi-agent architecture for a supervising system which encompasses an activity prediction layer. Their activity prediction component utilizes the active LeZi algorithm (Gopalratnam and Cook 2004) in order to detect emergencies in smart environments. More recently, the researchers in Mahmoud et al. (2013) discuss the application of soft computing techniques in prediction of an older adult's behaviour in a smart environment. In order to build the prediction model, they examine different neural networks and show that recurrent neural networks, such as NARX, achieve a great ability to finding the temporal relationships of input patterns.

Probabilistic graphical models have also been explored by researchers to detect and predict user activities. For instance, the authors in Kautz et al. (2003) focus on employing Hierarchical Hidden semi-Markov Models (HHSMMs) to identify the daily activities that residents perform in an assisted living community. The authors adopt Murphy's approach (Murphy 2002) for translating HHSMMs into dynamic Bayes networks (DBNs) and then applying regular approximate DBN inference algorithms. Also, the authors in Monekosso and Remagnino (2009) utilize hidden Markov models (HMMs) to model resident's behaviour to discover abnormal behaviour. Furthermore, the authors in Park and Cho (2010) propose an activity prediction method based on dynamic Bayesian networks (DBNs) in the context of wireless communication. For the training phase, they first collect activity attributes such as location, time of day, day of week and call record to learn the predictive

DBN for each user. The authors assume the features to be independent, therefore the learned model is similar to the naïve Bayes network. Next in the prediction phase, the system clusters users to different groups based on the collected data to conduct activity prediction. They evaluate their approach using alternative number of attribute sequences. In the experimental model section, we compare their method against our proposed model.

The work presented in this paper can be distinguished from these earlier efforts in two main ways. One primary distinction is that the proposed model employs Bayesian networks in a novel two-step inference process. In the first step, the model predicts the features associated with the next activity. In the second step, it predicts the activity label based on features that were predicted in the first step as well as the current activity label. A second distinction is that we predict the relative start time of the next distinct activity as a normal distribution over observed relative start times.

# 3 Probabilistic Directed Graphical Models 

In this section, we briefly overview the probabilistic directed acyclic graphical models, also known as Bayesian networks, and discuss the conditional independence relationships encoded by them.

### 3.1 Bayesian Networks

Probabilistic graphical models (PGMs) are graphs where nodes represent random variables and arcs represent the statistical dependencies between the corresponding random variables. Therefore, the PGMs provide a compact way of representing the joint probability distribution. The directed graphical models are also known as Bayesian networks (BNs) or belief networks. We refer to the directed graphical models as Bayesian networks (BNs) throughout the paper. A sample of BNs, representing 5 random variables, is illustrated in Fig. 1. The arcs in BNs represent the causality relationship between the corresponding variables. For instance, the arc from $A$ to $B$ in Fig. 1 indicates that node $A$ causes node $B$. One of the conclusions of the notion of causality is that the directed graph in a BN must be acyclic, as a node cannot cause itself.

In addition to the structure, a BN should specify the conditional probability distribution (CPD) for each node. If variables in the model are discrete, the CPD can be represented as a conditional probability table (CPT). A CPT for a node indicates the probability of the node being True or False for each combination of values for its parents. Table 1 represents a sample CPT for the variable $B$ in the BN illustrated in Fig. 1.

The inference in BNs boils down to marginalizing joint probability distributions (JPD). Given a JPD, we can answer all possible inference queries by marginalizing out the irrelevant variables. Consider a BN consisting of $N$ random variables $X=\left(X_{1}, X_{2}, \ldots, X_{N}\right)$, the general form of the joint probability distribution of the Bayesian network can be represented as in Equation 1, where $p a\left(X_{i}\right)$ represents the parents of node $X_{i}$ :

Equation 1 is based on the BN's property that each node is independent of the rest of the network, given its parents. Furthermore, dynamic Bayesian networks (DBNs) extend the BNs by adding a temporal dimension to BNs to model time series data.

# 3.2 Conditional Independence Relationships 

The conditional independence relationships allow the joint probability to be presented in a more compact form (factorized form). This form has fewer parameters, which makes learning easier. The conditional independence relationship answers to the question of whether random variable $A$ is conditionally independent of $B$, given random variable $C$. It is common to denote the conditional independence relationship with symbol $\Perp$, thus $A \Perp B \mid C$ should be interpreted as random variables $A$ and $B$ are conditionally independent, given variable $C$.

There are basically three types of relationships among random variables $A, B$, and $C$, which could be considered as building blocks of more complex relationships. The mentioned conditional independence relationships can be best explained by the Bayes Ball algorithm (Shachter 1998):

Two nodes $A$ and $B$ are conditionally independent given an observable node $C$, if there is no way for a ball to get from $A$ to $B$ (or vice versa), where the allowable move is represented in the second column of Fig. 2 (where there is no stop sign). One should note that a shaded node in Fig. 2 indicates that the node is observable in the data (which means either the node or its distribution is known). The second column in Fig. 2, which is referred to as the converging arrows case, implies that node $C$ allows the ball to pass through. As a conclusion, converging arrows case ${ }^{1}$ implies that nodes $A$ and $B$ are conditionally dependent, given node $C$. As opposed to the converging arrows case, the first and third columns represent the $A \Perp B \mid C$ conditional independence relationship.

We provide two intuitive examples for the first and third columns in Fig. 2, which together represent the conditional independence cases required to follow the proposed model. Let variables $A$ and $B$ denote a child's genes and his grandparents' genes, respectively. Also, let $C$ denote the child's parents' genes. Obviously, the child's genes and his grandparents' are dependent; however, given his parents' genes, they are conditionally independent. The mentioned example is compatible with the first case in Fig. 2. As another example, consider a scenario in which variables $A$ and $B$ represent that a person has lung cancer and has yellow teeth, respectively. Also, variable $C$ represents that the person is a smoker and we know that smoking causes both lung cancer and teeth to get yellow. Evidently, having lung cancer and having yellow teeth have some dependencies; however, they are conditionally independent

[^0]
[^0]:    ${ }^{1}$ Also referred to as the "explaining away" situation.

given that we know the person is a smoker. The mentioned example is consistent with the third case in Fig. 2. The examples discussed above both are formally defined as A ⊥B|C.

# 4 Proposed Model 

In this section, we present our proposed model for the daily activity prediction problem, when the BN structure is unknown and variables contributing in the model have full observability in the data. We assume the horizon of the prediction is one. We also assume variable $X_{t}$ represents the current activity label and variables $Y_{t}^{i}$ s $(i=1 . . n)$ represent activity features that correspond to $X_{t}$. Taking into account the prompting scenario mentioned in the Introduction, we assume an Activity Recognition (AR) module reports the current activity $X_{t}$ (or its distribution), the assumption which makes the next activity conditionally independent of all previous activities, i.e $X_{t+1} \Perp X_{t} X_{t}$ where $l<t$. The mentioned conditional independence relationship which is compatible with the first case in Fig. 2 is illustrated in Fig. 3. In addition to our proposed model, we also present two alternative network-based approaches in this section and compare their prediction accuracies against our proposed model in the Experimental Results section. Finally, we close this section by presenting our proposed approach to predict the start time of the predicted activity.

### 4.1 CRAFFT

In this section, we present our proposed method to solve the prediction problem illustrated in Fig. 3. Taking into consideration the conditional independence relationships in Fig. 3, one should note that activity features $Y_{t}^{i}$ s are conditionally independent of the next activity $X_{t+1}$ (see Fig. 2, 3rd case). Therefore, we propose the Bayesian network presented in Fig. 4 together with our proposed two-step inference process to address the prediction problem illustrated in Fig. 3.

We refer to our proposed model as CRAFFT, short for Using CuRrent Activity and Features to predict next FeaTures. As it stands from Fig. 4, CRAFFT utilizes three features for each activity. The description of all variables contributing to CRAFFT follows:

- State variable $\left(X_{t}\right)$ : the label of the current activity. Similarly, the variable $X_{t+1}$ refers to the label of the activity that is expected to occur immediately after $X_{t}$.
- Activity location feature $\left(Y_{t}^{1}\right)$ : the location in the smart home where the current activity occurs. The location is specified in terms of the location of a sensor. In a smart home, the corresponding sensor will generate a message if the movement of the resident is detected in its field of view. The locations we consider in our smart home include Kitchen, Bathroom, Bedroom, Living Room, Dining Room, Medication Cabinet, Lounge Chair, Kitchen Door, Bathroom Door, and Front Door.
- Activity time of day feature $\left(Y_{t}^{2}\right)$ : a discretized value of the time when the current activity occurs. Time values are binned into the following ranges: $0-3,4-7,8-11$, $12-15,16-19$, and $20-23$.

- Activity day of week feature $\left(Y_{t}^{3}\right)$ : an integer value ranging from 1 to 7 representing the day of the week in which the current activity happens, where 1 denotes Monday.

We provide two examples to justify why we consider the temporal features, time of day and day of week, in addition to the location feature in our proposed model:

- Our smart home activity dataset suggests that the same activity might be followed by different activities, when performed in different times of the day. For instance, the "Bathing" activity, when performed in the morning, is typically followed by the "Personal Hygiene" activity. However, when "Bathing" is performed in the evening, it is most likely followed by the "Sleeping in Bed" activity. The mentioned example justifies the need for considering the "time of day" feature in our model.
- Our smart home activity dataset indicates that the temporal relationships between activities are also affected by the day of week when the activity occurs. For instance, the "Lunch" activity is most likely followed by either the "Housekeeping" or "Personal Hygiene" activities, except on Mondays when it is followed by the "Leave Home" activity. The mentioned example suggests that in some cases, to make the correct prediction, we need to take advantage of the day of week feature.

In this section, we present our proposed method to make the prediction inference in the CRAFFT model illustrated in Fig. 4. The proposed approach consists of two prediction steps. In the first step, we predict the features associated with the next activity. In the second step, we predict the activity label based on the predicted features in the first step as well as the current activity label.

Step i: Next Activity Features Prediction-In the first step, CRAFFT predicts the features which correspond to the next activity, i.e. $Y_{t+1}^{1}, Y_{t+1}^{2}$, and $Y_{t+1}^{3}$. As illustrated in Fig. 4.1, we hypothesize that features representing the next activity are dependent on their current values as well as the current activity label. More specifically, CRAFFT hypothesizes that the next activity location is influenced by the current activity label, location, time of day, and day of week. Also, the next activity time of day and day of week are dependent upon their current values, as well as the current activity label. For instance, the goal of the activity location $\left(Y^{1}\right)$ prediction is to find $y_{t+1}^{1^{*}}$ that satisfies the following Equation.

$$
y_{t+1}^{1^{*}} \leftarrow \operatorname{argmax}_{y_{t+1}^{1}} P\left(Y_{t+1}^{1}=y_{t+1}^{1} \mid Y_{t}^{1}=y_{t}^{1}, Y_{t}^{2}=y_{t}^{2}, Y_{t}^{3}=y_{t}^{3}, X_{t}=x_{t}\right)
$$

In Table 2, we provide 5 examples for the feature prediction step, where the first row represents the template used to represent examples. Note that the start sign (*) can be replaced by any value of the corresponding feature.

The first example suggests that the Bathing activity, when performed in the morning, is typically followed by an activity that happens in the Bathroom; however, the second example indicates that it is followed by an activity in the Bedroom, when performed in the

evening. The first two examples imply why in addition to the current location, CRAFFT utilizes the current time of day feature to predict the next location. Moreover, the third example suggests that the Eating activity at noon is usually followed by an activity in the living room, when performed on Tuesdays through Sundays; however, the fourth example indicates that it is followed by an activity at the Front Door, when performed on Mondays. The last two examples advocate the need for considering the current day of week to predict the next activity location as shown in Fig. 4.1. The last example also suggests that the Sleeping activity, when performed in the evening, is followed by an activity in the Kitchen next day in the morning. This example shows how the day transitions are accommodated and how we connect the current activity to the next day of week feature.

Step ii: Next Activity Label Prediction-In the second step, CRAFFT predicts the next activity label based on the predicted features in the first step, as well as the current activity label. Fig. 6 represents the next activity label prediction step.

The prediction problem we take into account in this section is to find the $x_{t+1}^{*}$ that satisfies the following Equation. Also, its following Equation indicates how confident we are of our prediction.

$$
\begin{gathered}
x_{t+1}^{*} \leftarrow \operatorname{argmax}_{x_{t+1}} P\left(X_{t+1}=x_{t+1} \mid X_{t}=x_{t}, Y_{t+1}^{1}=y_{t+1}^{1}, Y_{t+1}^{2}=y_{t+1}^{2}, Y_{t+1}^{3}=y_{t+1}^{3}\right) \\
P\left(X_{t+1}=x_{t+1}^{*} \mid X_{t}=x_{t}, Y_{t+1}^{1}=y_{t+1}^{1}, Y_{t+1}^{2}=y_{t+1}^{2}, Y_{t+1}^{3}=y_{t+1}^{3}\right)
\end{gathered}
$$

# 4.2 Related Structure-based Models 

In this section, we review two related structure-based models for the prediction problem represented in Fig. 3. In the Experimental Results section, we compare their prediction accuracies against CRAFFT. Similar to the CRAFFT model, the models presented in this section utilize the same feature set (i.e. location, time of day and day of week) as well as the current activity label.

Considering the features corresponding to the current activity, one natural model is to predict the next activity based on the current feature set. We refer to the presented model in Fig. 7 as CEFA (short for using CurrEnt Features and activity to predict the next Activity).

As a baseline for comparison, we consider the naïve Bayes (NB) structure as illustrated in Fig. 8, where all of the activity features are assumed to be independent. As it stands from Fig. 8, naïve Bayes ignores the meaning and temporal relations among the variables, so the current activity $\left(X_{t}\right)$ is influenced by the next activity $\left(X_{t+1}\right)$ as illustrated in Fig. 8.

It is worth noting that the model presented in Fig. 8 emulates Park and Cho (2010) approach, where the number of attribute sequence is assumed to be 1 .

# 4.3 Relative Start Time Prediction for the Predicted Activity 

In the previous sections, we discussed how CRAFFT and alternative approaches predict the next most likely activity label. In this section, we explore the question of when that activity starts. As discussed in the prompting scenario presented in the Introduction, we are interested to know the relative start time of the predicted activity with respect to the start time of the current activity. In order to do that, we extract the time offset between each two consecutive activities in our dataset and cluster them using the Expectation Maximization algorithm to construct a normal mixture model for the time offsets. In Fig. 9, we show three most probable clusters which represent the time offsets between activity $X_{t}$ and $X_{t+1}$. It is noteworthy that the time offset in our setting is not exactly the duration of the current activity $\left(X_{t}\right)$, because some "other activities" that are not considered in our study might occur between $X_{t}$ and $X_{t+1}$.

Let $t_{i, j}$ denote the time offset between two activities $a_{i}$ and $a_{j}$. Equation 2 represents the time offset as a normal probability density function with parameters $\Theta_{k}=(\mu, \sigma)$. Here $\mu$ and $\sigma$ are the mean and standard deviation values, calculated for the time offset.

$$
\operatorname{prob}\left(t_{i, j} \mid \Theta_{k}\right)=\frac{1}{\sqrt{2 \pi \sigma^{2}}} e^{\frac{\left(t_{i, j}-\mu\right)^{2}}{2 \sigma^{2}}}
$$

According to the normal distribution characteristics, as illustrated in Fig. 10, the distance of "two standard deviations" from the mean accounts for about $95 \%$ of the values. Therefore, if we consider only observations falling within two standard deviations from the mean, observations that are deviating from the mean will be automatically removed. Such observations that are distant from the rest of the data are called outliers".

In the Experimental Results section, we present a sample for the time offset modeling between "Breakfast" and "Taking Medication" activities.

## 5 Experimental Results

In this section, we present the experimental results of the CRAFFT model, together with the results of the other related algorithms. Before getting into the evaluation of the CRAFFT model, we describe our Experimental Setup.

### 5.1 Experimental Setup

We used three one-bedroom single resident smart home apartments for our experiments, referred to as Apt1, Apt2 and Apt3. Our smart apartment residents were older adults who were performing normal unscripted daily activities. In order to track resident movements, we used sensors installed on ceilings, walls, doors, and cabinets. The sensor layouts for our testbeds are shown in Fig. 11, where red circles and blue triangles represent infrared motion/ area sensors and magnetic door/cabinet sensors, respectively. A sensor network captures all of the events generated by the sensors, and our middleware stores them in an SQL database. To provide real activity data for our experiments, we have collected data while the residents

were living in smart homes performing normal daily routines. Table 3 provides the characteristics of our smart home testbeds ${ }^{2}$ :

For our experiments, we consider 11 ADLs (Reisberg et al. 2001) performed by the residents in the smart homes. The list of the activities we take into consideration in our study follows: Bathing, Bed-Toilet Transition, Eating, Enter Home, Housekeeping, Leave Home, Meal Preparation, Personal Hygiene, Resting on Couch, Sleeping in Bed, and Taking Medication.

The datasets we use in our study consist of a set of discrete individual sensor events collected from various sensors deployed in the space. In a smart home the corresponding sensor will generate a message if resident movement is detected in its field of view. Events in the dataset have been manually annotated with corresponding activity labels by trained researchers who employed visualization tools and interviews with residents to generate accurate ground truth labels. Table 4 provides a sample data related to the "Eating" activity, where M05 and M12 represent motion sensors and D07 represents a door/cabinet sensor.

It is noteworthy that the activity instances in our dataset often overlap. For instance, Fig. 12 represents an example from our dataset, where 'Personal Hygiene' occurs during the 'Meal Preparation' activity (left). The CRAFFT model forces an end of the 'Meal Preparation' activity before the 'Personal Hygiene' starts as shown in Fig. 12 (right). We see the impact of such overlapping activities in the results that are presented in the next section.

# 5.2 Evaluation of CRAFFT 

In this section, we provide the results of running CRAFFT on our smart home data and compare them with the related prediction approaches. All of the prediction approaches were tested using 10 -fold cross validation. Each prediction method was trained on 9 out of 10 groups and tested on the remaining one. The results from all ten permutations were used for significance values and averaged together for an overall accuracy.

As already mentioned, CRAFFT consists of two prediction steps: (i) predict the next activity features, and (ii) predict the next activity label. The overall prediction accuracies corresponding to both steps using data gathered from our three smart apartment testbeds are provided in Table 5. The results presented in Table 5 suggest that CRAFFT achieves an overall accuracy of $64.18 \%$ with a standard deviation of 3.76 for Apt1, an accuracy of $74.57 \%$ with a standard deviation of 3.85 for Apt2 and an accuracy of $61.98 \%$ with a standard deviation of 4.72 for Apt3. The results indicate that CRAFFT achieves the highest accuracy for Apt2.

The next activity features prediction results for CRAFFT are also provided in Table 5. The results suggest that the location prediction accuracy is $46.52 \%$ for Apt1, whereas it is $60.80 \%$ and $46.99 \%$ for Apt2 and Apt3, respectively. Furthermore, the time of day prediction accuracies are $88.09 \%$ for Apt1, $86.23 \%$ for Apt2, and $67.07 \%$ for Apt3. Finally, the day of week prediction accuracies are $96.94 \%, 96.57 \%$, and $61.98 \%$ for Apt1, Apt2, and

[^0]
[^0]:    ${ }^{2}$ Datasets are available online at http://casas.eecs.wsu.edu/datasets/

Apt3, respectively. In order to justify why the next day of week prediction introduces these errors, we provide two scenarios, provided that Saturday is assumed to be the positive class.

Suppose that the resident goes to Bed at 11 pm on Friday. While the CRAFFT model predicts that the next activity occurs on Saturday, the resident actually may get up half an hour later to go to the Bathroom (as occasionally happens in the data). This is an example of a FP error. As an example for a FN error, consider that the resident intends to take a rest on the Couch at 10 pm Friday. In this case, CRAFFT predicts the next activity will occur on Friday; however, the resident falls sleep for three hours and wakes up on Saturday.

In order to present the results for alternative approaches, we first provide the activity prediction results using the CEFA model for our datasets. The results presented in Table 6 suggest that the overall activity label prediction accuracy of CEFA is $49.02 \%$ for Apt1, $59.78 \%$ for Apt2, and $47.18 \%$ for Apt3. Compared to the prediction results of CRAFFT provided in Table 6, the CEFA model shows a $15.16 \%$ decline for Apt1, a $14.79 \%$ decline for Apt2 and a $14.80 \%$ decline for Apt3. All three mentioned prediction accuracy drops for our smart home testbeds are statistically significant ( $p<0.05$ ). Also it is worth mentioning that the CEFA model does not predict the next activity features, therefore there is no entry allocated for the activity feature prediction in Table 6.

We present the overall activity prediction accuracy of naïve Bayes (NB) in Table 7. Compared to the prediction results of CEFA presented in Table 6, NB shows a $3.91 \%$ decline for Apt1, a $4.24 \%$ decline for Apt2 and a $3.42 \%$ decline in accuracy for Apt3. As stated previously, NB ignores the meaning and the temporal relations among variables and is compatible with the model presented in Park and Cho (2010).

In order to compare the results of CRAFFT with non-network based approaches, we present the prediction results for the Decision Tree (DT), Support Vector Machines (SVMs), and Multi-layer Perceptron (MLP) algorithms for our datasets. The overall activity prediction results for the DT algorithm presented in Table 8 suggest a $16.42 \%$ accuracy drop for Apt1, a $14.37 \%$ drop for Apt2 and a $14.06 \%$ drop for Apt3. In Table 8, we provide prediction results of the MLP algorithm. Compared to the results presented in Table 5 for the CRAFFT model, these results indicate that the accuracy dropped $15.60 \%$ for Apt1, $16.64 \%$ for Apt2 and $14.06 \%$ for Apt3. Finally, in Table 8, we provide the prediction accuracies of SVMs with a polynomial kernel on our smart apartment testbeds. The results imply a $17.59 \%$ decline for Apt1, and a $19.03 \%$ and a $17.67 \%$ decline for Apt2 and Apt3, compared to the results of CRAFFT. The discussed comparisons suggest that CRAFFT is significantly better $(p<0.05)$ over the non-network based algorithms for the temporal prediction task.

In Fig. 13, we summarize the activity label prediction comparison between CRAFFT and other structure-based and non-structure based algorithms examined in this study. As we already discussed, all the algorithms were fed with the current activity label and the features corresponding to the current activity. What makes CRAFFT outperform the other approaches is the fact that it does not rely on the current features to predict the next activity. Rather, it first predicts the features corresponding to the next activity and then employs them to predict the next activity label.

We demonstrate the confusion matrix for the CRAFFT predictions for Apt2 in Table 9, where the numbers in parentheses reflect the relative values. The results indicate that our dataset is highly imbalanced, which makes prediction on our dataset difficult. For instance it can be concluded from Table 9 that 'Personal Hygiene' is over-represented in our dataset, as compared to other activities. This may have caused some confusion in the predictions made by CRAFFT. Other than the imbalanced nature of our datasets, we briefly discuss some of the possible underlying reasons for major confusions made by CRAFFT.

The results indicate that the 'Taking Medication' activity gets confused with the 'Eating' activity. This confusion is mainly due to similar location of the occurrence of the two tasks. Also, the confusion between 'Housekeeping' and 'Meal Preparation' activities is most likely because these two activities overlap too often. Moreover, the results suggest some confusion between 'Sleeping in Bed' and 'Bed-Toilet Transition' activities, which is mainly because of their similar time and location of occurrence. It should be added that the relative values corresponding to the discussed confusions are also provided in Table 9.

Lastly, we close this section by presenting a sample result for our proposed relative start time discovery method. Assuming that the current and predicted activities are "Breakfast" and "Taking Medication", Fig. 14 illustrates the discovered time offset between the mentioned activities in our dataset. As previously mentioned, we model the time offset between activities using the continuous normal distribution. Taking into consideration our proposed outlier detection mechanism illustrated in Fig. 10, the presented results in Fig. 14 suggest that "Taking Medication" typically happens 13 to 37 minutes after the start of "Breakfast" activity (see Fig. 10):

$$
[\mu-2 \sigma, \mu+2 \sigma]=[25-2 * 6,25+2 * 6]=[13,37] \min
$$

# 6 Conclusions and Future Work 

In this paper, we proposed the CRAFFT prediction model which utilizes the Bayesian networks in a novel two-step inference process. While the focus of this paper was on the activity prediction in smart homes, the application of the proposed two-step inference process is not limited to this domain and can be applied to other areas as well. Once we have an activity prediction module, then the applications of such a component are endless.

To predict the start time of the predicted activity, we proposed a method based on continuous normal distribution and the outlier detection. We validated CRAFFT using real data collected from smart home apartments. The Experimental Results suggest the superior performance of the CRAFFT model over the other related prediction approaches. The input to all of the discussed algorithms is the current activity label and the features corresponding to the current activity. What makes CRAFFT outperform the other approaches mainly lie in the idea that it does not rely on the current features to predict the next activity. Instead, it first predicts the features corresponding to the next activity and then utilizes them to predict the next activity itself.

In future, we plan to extend the proposed two-step inference process to cases where data is partially observable or it contains hidden variables. Also, we aim to apply the proposed approach for context-aware prompting-based interventions for older adults.

# Table 2 

Intuitive examples for the feature prediction step.


Table 3
Characteristics of the smart homes used in our study.


Table 4 A sample for sensor events used in this study.


# Table 5 

The overall CRAFFT activity label prediction accuracy.


# Table 6 

The overall CEFA activity prediction accuracy for our smart home testbeds.


NB Prediction accuracy for our testbeds.


Table 8 Activity label prediction accuracy for DT, SVMs and MLP.


Table 9 Confusion matrix for the CRAFFT predictions.
