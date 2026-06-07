# A medical decision support system for predicting the severity level of COVID-19 

Mohsen Abbaspour Onari ${ }^{1} \cdot$ Samuel Yousefi ${ }^{1} \cdot$ Masome Rabieepour ${ }^{2} \cdot$ Azra Alizadeh ${ }^{3} \cdot$ Mustafa Jahangoshai Rezaee ${ }^{1}$ (D)<br>Received: 18 November 2020 / Accepted: 22 February 2021 / Published online: 4 March 2021<br>(c) The Author(s) 2021


#### Abstract

The main assay tool of COVID-19, as a pandemic, still has significant faults. To ameliorate the current situation, all facilities and tools in this realm should be implemented to encounter this epidemic. The current study has endeavored to propose a self-assessment decision support system (DSS) for distinguishing the severity of the COVID-19 between confirmed cases to optimize the patient care process. For this purpose, a DSS has been developed by the combination of the data-driven Bayesian network (BN) and the Fuzzy Cognitive Map (FCM). First, all of the data are utilized to extract the evidence-based paired (EBP) relationships between symptoms and symptoms' impact probability. Then, the results are evaluated in both independent and combined scenarios. After categorizing data in the triple severity levels by self-organizing map, the EBP relationships between symptoms are extracted by BN, and their significance is achieved and ranked by FCM. The results show that the most common symptoms necessarily do not have the key role in distinguishing the severity of the COVID-19, and extracting the EBP relationships could have better insight into the severity of the disease.


Keywords COVID-19 $\cdot$ Medical decision support system $\cdot$ Severity level prediction $\cdot$ Evidence-based paired relationships $\cdot$ Data-driven Bayesian network $\cdot$ Fuzzy cognitive map

## Introduction

Since December 2019, a couple of "unknown viral pneumonia" stems from a local Seafood Wholesale Market were reported in Wuhan city, the capital of Hubei province in

[^0]China [1]. The Coronavirus Disease 2019 (COVID-19) is taken into account by a family of the deadly Severe Acute Respiratory Syndrome (SARS) and the Middle East Respiratory Syndrome (MERS) Coronaviruses [2, 3]. In just 2 months, the virus spread from Wuhan to the whole of China and 33 countries [1]. Consequently, the World Health Organization (WHO), on 11 Mar. 2020, announced COVID2019 caused by SARS-CoV-2 to be a pandemic and public health emergency of an international outbreak [4]. To date, 12 Feb. 108,354,740 confirmed cases have been recorded worldwide that unfortunately $2,380,451$ have passed away, and $80,405,951$ of them have been recovered [5]. Figure 1 represents the total number of confirmed cases in countries with the highest number of patients per one million populations [5]. Figure 2 demonstrates the daily new confirmed cases [6].

COVID-19 infection causes systemic and respiratory disorders in the patient. Systemic disorders include fever, cough, fatigue, sputum production, headache, hemoptysis, acute cardiac injury, hypoxemia, dyspnoea, lymphopenia, and diarrhea. Respiratory disorders consist of rhinorrhoea, sneezing, sore throat, pneumonia, ground-grass opacities,


[^0]:    12 Mustafa Jahangoshai Rezaee m.jahangoshai@uut.ac.ir

    Mohsen Abbaspour Onari m.abbaspour@ine.uut.ac.ir

    Samuel Yousefi
    s.yousefi@ine.uut.ac.ir

    Masome Rabieepour
    rabiee.masome@yahoo.com
    Azra Alizadeh
    Alizadeh.azra@umsu.ac.ir
    1 Faculty of Industrial Engineering, Urmia University of Technology, Urmia, Iran
    2 Pulmonary Department, Urmia University of Medical Sciences, Urmia, Iran
    3 Department of Internal Medicine, Urmia University of Medical Sciences, Urmia, Iran

Fig. 1 Total cases of COVID-19 in countries with the highest number of patients per 1 million
![img-0.jpeg](img-0.jpeg)

Fig. 2 Daily new confirmed cases

RNAemia, and acute respiratory distress syndrome [7]. Fever, cough, and fatigue are the most common symptoms of COVID-19 at the early stages of the epidemic's advent. In contrast, later symptoms include sputum production, headache, hemoptysis, diarrhea, dyspnoea, and lymphopenia [7]. The disease's detection at the early stages is critical, because
there are no specific therapeutic drugs for COVID-19. After detecting the infected patient's symptoms, he/she should be isolated immediately from the healthy population [1]. Until now, real-time reverse transcription-polymerase-chain-reaction (RT-PCR) has been developed to assay COVID-19 in clinics [1]. RT-PCR still is the reference standard to make

a definitive diagnose of COVID-19 infection. Still, the high false-negative rate and its unavailability in the early stage of the disease confined quick diagnosis of infected patients [1]. Much research has been conducted to fight COVID-19 in various science domains in a limited time based on the provided information, which one of them is Artificial Intelligence (A.I) tools.

Srinivasa Rao and Vazquez [8] proposed that using Machine Learning (ML) algorithms for identifying a person under investigation for the COVID-19 infection with a mobile phone-based web survey could identify the high-risk cases and quarantined earlier, and subsequently decreasing the chance of spread. Chest computed tomography (CT) can recognize the early phase of lung infection and prompt larger public health surveillance and response systems [1]. Li et al. [9] constructed a convolutional neural network (CNN) to identify community-acquired pneumonia on chest CT exams and could successfully distinguish COVID-19 cases from community-acquired pneumonia and other non-pneumonic lung diseases. The emergency management and infection control teams at the radiology department of West China Hospital formulated various measures to battle COVID19, which protected all of the staff from COVID-19 risk: the reconfiguration of the radiology department, personal protection and training of staff, examination procedures for patients suspected of or confirmed with COVID-19 as well as patients without an exposure history or symptoms, and scanning persons with suspected or confirmed COVID-19 infection in the determined fever-CT unit [10]. Besides routine therapy, Xu et al. [11] prescribed tocilizumab to their patients and analyzed changes of clinical manifestations, CT-scan images, and laboratory trials retrospectively. Their results claim that the fever returned to normal within a few days, and all other symptoms improved significantly, and any obvious adverse reactions were observed. Tang et al. [12] modeled and trained a random forest to evaluate the severity of patients suffering from COVID-19 based on the chest CT images' quantitative features. Farid et al. [13] combined conventional statistical and ML to extract features from CT images and then classified extracted features by a hybrid classifier system based on Naive Bayes.

Taiwan's reactions against COVID-19 are phenomenal. Its response against COVID-19 includes three phases: (1) big data analytics: by gathering national health insurance database and integrating with immigration and customs database; (2) implementing new technology: using QR code scanning and online reporting to classify travelers' infectious risks based on-flight origin and travel history in the past 14 days; (3) proactive testing: to amplify the COVID19 case finding [2, 3]. Karar et al. [14] using X-ray scans proposed computer-aided diagnosis (CAD) systems based on cascaded deep learning (DL) classifiers for COVID-19. A similar study, analyzing chest X-ray images, has been conducted by Shankar and Perumal [15] for COVID-19 diagnosis and classification using a novel hand-crafted with DL feature-based fusion model. Elaziz et al. [16] based on the extracted features from the COVID-19 chest X-ray images using new fractional multichannel exponent moments (FrMEMs) exploited a modified manta-ray foraging optimization based on differential evolution to select the most significant features. de Moraes et al. (2020) implemented support vector machines (SVM) to extract features through multi-level thresholding from chest X-ray radiography images for early detection of COVID-19 cases. Laguarta et al. [17] developed a speech processing framework based on the CNN architecture for COVID-19's patients' cough recordings to discriminate them accurately. Wang et al. [2, 3] utilized linear discriminant analysis (LDA) for investigating the characteristics and rules of hematology changes in COVID-19 patients. Moreover, clinical and laboratory patients' test results were analyzed, and different hematological parameters fitted using LDA.

Given the importance of the pandemic, the current study attempts to propose an intelligent self-assessment decision support system (DSS) based on the combination of Bayesian network (BN) and the fuzzy cognitive map (FCM) to utilize the key symptoms for distinguishing the severity of the disease between confirmed cases. In self-assessment systems, patients can obtain a general evaluation of their disease by reporting information about their symptoms. For designing an efficient self-assessment DSS, symptoms are analyzed both entirely and in severity levels. First, BN is implemented to extract evidence-based paired (EBP) relationships and symptoms' impact probability for distinguishing severities for the whole data in various scenarios. To put it precisely, BN is applied to extract the EBP relationships between triple severity levels to develop FCM. BNs have various advantages: the ability to combine different knowledge sources, the capacity to handle small and defective datasets, and the availability of a wide range of validation methods besides data-driven validation methods [18]. Hence, it is a very powerful method to implement in the healthcare realm. This method has been applied in diagnosing breast cancer [19], Alzheimer's disease [20], and erythematous-squamous diseases [21]. In the second stage, in triple severities, the FCM is used to obtain the symptoms' significance based on BN's determined EBP relationships. The FCM is a modeling approach with two main advantages: it is easily understandable by experts of a particular domain and gives values to causal maps based on qualitative opinions [22]. The uncertainty and vagueness commonly associated with opinions are medical data characteristics due to enormous individual differences and measurement errors. In general, the effectiveness of FCMs to deal with this variability has convinced researchers to implement this technique broadly. FCMs have been applied to make DSSs in settings where

errors would have hazardous consequences [23] like thyroid diagnosis management [24], pulmonary differential diagnosis [25], estimate hospitals' outputs level [26], and Acute Leukemia self-assessment DSS [27]. After determining the significance of symptoms in every severity level, the key symptoms for distinguishing the severity levels of confirmed cases of COVID-19 are used to implement in clinical trial measures on patients. For this study, a database from https ://www.kaggle.com/ website has been collected, including COVID-19 symptoms for confirmed cases.

The rest of the paper is organized as follows: the implemented methods in this research are reviewed in "Methodology". The proposed approach is covered in "Proposed approach". In "Analysis of results", the results of the research are provided and analyzed. Finally, the conclusion of the study is discussed in "Conclusion".

## Methodology

This section is covered with the following materials: In "Introduction", the BN and its learning algorithm are introduced. In "Methodology", the mechanism of the FCM and its learning algorithm are provided.

## BNs and Bayesian search algorithm

Bayes theorem defines conditional or marginal probabilities for two variables $\alpha$ and $\beta$ as follows [21]:
$P(\alpha / \beta)=\frac{P(\beta / \alpha) P(\alpha)}{P(\beta)}$.
Human knowledge for multivariable problems can be considered a joint probability distribution (JPD) of these variables. Learning knowledge from data means to learn this joint probability. The joint probability has $2^{n}$ parameters for a binary variable problem with $n$ variables. Obtaining the joint probability is unpractical, where the complexity of the problem increases exponentially with the number of variables. A BN decomposing the joint probability into the product of some simple conditional probabilities can decrease the complexity [28]. BNs are a member of the probabilistic graphical model family, which consists of nodes and directional arrows. Usually, nodes in a BN are depicted as circles or ovals and indicate variables, and directed edges (arrows) between pairs of nodes demonstrate relationships between variables. In the BNs, those nodes that contribute to higher nodes align themselves in "child"-to-"parent" relationships, where parent nodes are superior to the child nodes [29]. A BN has two components, a graphical model $(G)$ and a set of parameters $(\Theta)(\beta=(G, \Theta]) . G$ can be made from random variables $X_{1}, X_{2}, X_{3}, \ldots, X_{n}$ and $\Theta$ contains
the states of each random variable given the parents set $\pi_{i}$ in $G$. In $G$, let random variables $V=\left\{X_{1}, X_{2}, X_{3}, \ldots, X_{n}\right\}$ with JPD with their values or states $x_{1}, x_{2}, x_{3}, \ldots, x_{n}$ of $V$. The probabilities of these variables can be represented as $P\left(X_{1}=x_{1}, X_{2}=x_{2}, X_{3}=x_{3}, \ldots, X_{n}=x_{n}\right)=P\left(x_{1}, x_{2}, x_{3}, \ldots x_{n}\right)$. A BN corresponds to graphical model $G$, which is a direct acyclic graph (DAG). The structure of DAG is described as vertices and directed edges. The vertices v is demonstrated as the set of nodes in $V$, and the edges denote the relationship between the vertices. Finally, each vertex in the graphical structure against $V$ has its specific conditional probability distribution (CPD), which can be defined as $P\left(x_{i} \mid \pi_{i}\right)$. Therefore, the JPD of BN is the product of CPDs [30]. For more simplification, suppose that a BN consists of $n$ random variables as $x_{1}, x_{2}, x_{3}, \ldots, x_{n}$. The full JPD can be written as follows $[27,31]:$

$$
\begin{aligned}
& P\left(x_{1}, x_{2}, x_{3}, \ldots, x_{n}\right)=P\left(x_{1} \mid x_{2}, x_{3}, \ldots, x_{n}\right) P\left(x_{2} \mid x_{3}, x_{4}, \ldots, x_{n}\right) \ldots \\
& \quad P\left(x_{n-1} \mid x_{n}\right) P\left(x_{n}\right)
\end{aligned}
$$

Then, it can be simplified as:
$P\left(x_{1}, x_{2}, x_{3}, \ldots, x_{n}\right)=\prod_{i=1}^{n} P\left(x_{i} \mid x_{i+1}, \ldots, x_{n}\right)$.
Afterward, suppose that $\pi_{i}$ indicates the set of parent nodes of the node $x_{i}$. Now, using the existing knowledge of what the parents of each node are, Eq. 3 can be reformulated as:
$P\left(x_{1}, x_{2}, x_{3}, \ldots, x_{n}\right)=\prod_{i=1}^{n} P\left(x_{i} \mid \pi_{i}\right)$.
Furthermore, BN assumes the independence assumption of nodes from its predecessors' whole set apart from the direct parental [30].

The way of building an effective BN has been a longterm research issue. Building a Bayesian network for a given dataset $D$ is finding the most appropriate network and generally is divided into two learning subtasks: structure learning and parameter learning. The structure learning seeks to determine the topology of the network. On the contrary, parameter learning concentrates on determining each conditional distribution $P\left(x_{i} \mid \pi_{i}\right)$ for a given network structure. Learning the BN structure requires higher accuracy rather than parameter learning [32]. The Bayesian search structure learning algorithm is one of the earliest and the most popular algorithms for BN. It was introduced by Cooper and Herskovits [33] and then was developed slightly by Heckerman et al. [34]. It follows essentially a hill-climbing procedure (guided by a scoring heuristic) with random restarts. The algorithm produces an acyclic directed graph that gives the maximum score. The score is proportional to the probability

of the data given the structure, which assumes that the same prior probability has been assigned to any structure, which is proportional to the probability of the structure given the data. The algorithm generates an on-screen text box that consists of all parameters' settings of the BS algorithms. The Bayesian search theory's foundation is updating the probability of the located target in the $i_{\text {th }}$ box based on previous failures to detect. After searching the $i_{\text {th }}$ box and failing to find it, the likelihood of being located there will reduce, and the probability of being located in another box will augment. In this model, only the conditional probabilities of detection failure have a role in updating the new location probabilities. Consequently, only the box with the highest likelihood of containing the target and searches is being explored using the search algorithm. Upon failure to find, it updates all location probabilities and repeats until the target is detected or the number of glimpses has been reached [35]. The algorithm includes the following parameters: maximum parent count, algorithm iterations, the sample size for representing the inertia of the current parameters when introducing new data, a seed that is the initial random number, link probability that is a parameter used when generating a random starting network at the outset of each of the iterations, prior link probability, max time, and scoring function [36].

## FCM method

For the first time, Kosko [37] introduced the concept of FCM by utilizing fuzzy logic and artificial neural networks (ANN) tools to draw a cognitive map or the cause-and-effect graphical models that those cause-and-effect relations can acquire numbers in the range $[0,1]$ or $[-1,1]$ [38]. FCM can be created by time-series and experience and knowledge of experts in the subject [39]. In the FCM, $C_{i}$ demonstrates nodes or concepts which are connected via weighted arcs. Each connection between the two concepts $C_{i}$ and $C_{j}$ has a weight equal to $W_{i j}$, which indicates the degree of causality and the type of relationship between concepts [40]. So that $W_{i j}>0$ represents a positive causal relationship, $W_{i j}<0$ represents a negative causal relationship, and $W_{i j}=0$ represents the absence of any relationship between the two concepts. After depicting the map, it must be modeled by mathematical formulas at the first step for analyzing the model. By achieving values of a node, the values of other nodes connected with this node can be obtained using Eq. 5:
$A_{i}^{(k+1)}=f\left(A_{i}^{(k)}+\sum_{\substack{i=1 \\ j \neq i}}^{n} W_{i j}^{(k)} A_{j}^{(k)}\right)$.

In Eq. 5, $A_{i}^{(k+1)}$ indicates the value of $C_{i}$ in $(k+1)$ repetitions, $A_{i}^{(k)}$ indicates the value of $C_{i}$ in $k$ repetitions, and $f(x)$ represents the normalization function.

In the FCM, for increasing their accuracy, improving the map's structure, and reducing reliance on experts' opinions, precise estimation of the map weights by learning algorithms is indispensable [41]. FCMs' learning algorithms are classified into four categories: Hebbian-based, population-based, hybrid algorithms, and other algorithms. Each category has corresponding characteristics and consists of several algorithms [42]. In the first category, Hebbian rule-based learning algorithms whose logic is derived from ANN, such as differential Hebbian [43], nonlinear Hebbian [44], and active Hebbian [45], have been developed. In the population-based learning algorithms, such as multi-local and balanced memetic algorithms [46], asexual reproduction optimization, and its modified version [47], etc., have been proposed. The third category of algorithms is based on both Hebbian-based and population-based algorithms, which can utilize human knowledge with historical data to adjust the weighting matrix. In the last category, developed algorithms are not in the main three groups and have been introduced to solve some of the previous algorithms' problems, such as the Delta-rule algorithm [38, 48].

## Proposed approach

In this study, a self-assessment DSS is proposed to utilize the key symptoms of COVID-19 for distinguishing the severity of the epidemic based on the "Diagnosis and Treatment Protocol for Novel Coronavirus Pneumonia released by the National Health Commission (NHC) \& State Administration of Traditional Chinese Medicine (NATCM) on 3 Mar. 2020" [49]. This method is a hybrid approach based on BNs and FCM. Initially, a set of data for confirmed cases of COVID-19 are collected, and after clustering data, they are categorized into three levels that exhibit the severity of the disease. In the first stage of this approach, the BN is implemented for two main purposes: (1) extracting the EBP relationships between attributes and their impact probability in the independent and combined modes; (2) extracting the EBP relationships between attributes inside the severity levels for developing FCM. First, the Bayesian search algorithm has been utilized to learn BN. This algorithm exploits background knowledge that can apply the experts' opinion in the network, and this characteristic has been used in this study. In BN's learning phase, relations between attributes are defined based on the conditional probability and the algorithm. The Bayesian search algorithm generates an acyclic directed graph that designates the maximum score. The score is proportional to the probability of the data given

the structure. It considers that the same prior probability has been specified to any structure, proportional to the structure's probability given the data. It should be mentioned that illogical relations between attributes are removed. For instance, fever cannot affect a patient's age, and consequently, this relation should be eliminated.

In the second stage, the FCM is constructed based on the extracted EBP relationships by BN. The disease's symptoms have been considered the main concepts of the FCM, and the severity of every level is the goal node of the FCMs. Developing FCM is based on the defining scenario for every symptom and achieving each symptom's impact on the goal node. For this purpose, every symptom is activated, and the rest of the symptoms are deactivated, and the FCM is trained. After training FCM for every symptom and severity level, the goal node's amount is picked out. In this study, due to the high importance of extracting the weights of EBP relationships between symptoms, a popu-lation-based learning algorithm has been utilized for training FCM. The used algorithm is based on the combination
of the particle swarm optimization (PSO) and the S-shaped Transfer Function (PSO-STF). For the first time, this algorithm was proposed by Abbaspour Onari et al. [50] as an extension of the PSO algorithm due to its shortcoming in distinguishing between various concepts. The PSO-STF, implementing the S-shaped transfer function, can enhance the algorithm's separability and give an accurate and vivid insight into the problem for decision-makers. It is practical in realms that concepts' priority is crucial for decisionmakers, and they need a precise and valid prioritization approach. Initially, the PSO generates various solutions for FCM, and due to generating solutions with high accuracy and separability, the S-shaped transfer function is applied to the algorithm. The corresponding weights between relations were allowed to assume values in the range $[0,1]$ to avoid generating physically meaningless weight matrices and lack of information about the impact of symptoms on each other. The pseudo-code for the mentioned algorithm is presented in Fig. 3. Finally, all of the achieved amounts of goal nodes in triple levels are picked out and are considered as the significance of symptoms in distinguishing the COVID-19 severity levels. It should be mention that

1. The objective function $f(x)$ defining: Mean squared error (MSE).
2. PSO parameters initialization: $c_{1}$ and $c_{2}$ (acceleration constants), $w$ (inertia weight), population size ( $n P o p$ ), and the maximum number of algorithm iteration, weights' constraints.
3. Generating an initial population of particles (Weight matrix of the identified EBP of the COVID-19 symptoms)
4. Applying the relevant scenario by activating the studied symptom.
5. Transforming generated populations and relevant scenario to the S-shaped transfer function
6. Evaluating the fitness of each particle and set all initial positions as $P_{\text {Best }}$.
7. While ( $t<$ Max Generation) or (Stop criterion)
8. Selecting $G_{\text {Best }}$ the particle in the swarm, which has the minimum fitness value.
9. for $i=1: n P o p$
10. Calculating the velocity of the particle $x_{i}$ according to the following expression:

$$
v_{i}(t+1)=w^{*} v_{1}(t)+c_{1}^{*} \operatorname{rand}()^{*}\left(p \text { best }_{i}(t)-x_{i}(t)\right)+c_{2}^{*} \operatorname{rand}()^{*}\left(g \text { best }(t)-x_{i}(t)\right)
$$

11. Updating the position of the particle $x_{i}$ according to the following expression:

$$
x_{i}(t+1)=x_{i}(t)+v_{i}(t+1)
$$

12. end for $\boldsymbol{i}$
13. for $i=1: n P o p$
14. Transforming generated populations to the S-shaped transfer function
15. Evaluating the fitness of updated particle $x_{i}$
16. if fitness $\left[(x)<P_{\text {Best }})\right]$

Setting the current position as $P_{\text {Best }}$
18. end if
19. end for $\boldsymbol{i}$
20. Finding the best particle.
21. end while

Fig. 3 The pseudo-code of PSO-STF

Fig. 4 The flowchart of the proposed approach
![img-1.jpeg](img-1.jpeg)
symptoms with a higher score will have higher rankings. This approach has been elaborated in Fig. 4.

## Analysis of results

In this section, the results of the proposed approach are analyzed. This section is organized as follows: In the first section, the research's preprocessing phase is presented

for data clustering. In the second section, the proposed approach's implementation is provided, and the results are analyzed.

## Data preprocessing for clustering

This study uses a dataset from https://www.kaggle.com/ website to be used as the COVID-19 dataset. In this dataset, the identified symptoms of COVID-19 have been considered as attributes. In this study, owing to the lack of genuine labels for samples, the clustering of these samples has been carried out using the self-organizing map. A self-organizing map, also known as the Kohonen map, belongs to instancebased ML algorithms. It can be visualized simply as a grid of neurons (nodes) of competitive nature where the outputs of these types of ANNs represent the network's actual state [51]. It is one type of unsupervised learning ANN techniques. It is a simple and practical tool for clustering in data mining applications. In principle, data with similar features are divided into similar groups [52]. Overall, the self-organizing map consists of four main phases: initialization phase, competitive phase, cooperation phase, and adjustment phase [53]. To start clustering, each node is initialized with a random weight. According to a uniform distribution, this can be an arbitrary probability distribution or even randomly sampled from the input training set. The learning process is a set of iterations and is based on a simple rule: each node "competes" to be the best match to a randomly selected vector from the training set. The best matching unit (BMU) is rewarded by becoming more like the input vector. Moreover, nodes in the proximity of the BMU are also allowed to be altered in the same direction; however, to a lesser extent than the BMU. After a multitude of samplings, the nodes can learn to become more like the training set [54]. In this regard, all samples have been categorized into three clusters based on the self-organizing map with lattice size $=[1,3]$. To put it differently, the distance between the center point of each cluster and the coordinate system's origin has been considered a criterion to assign a real label to each cluster. Those labels are clinical severities defined by the NHC and NATCM protocols: (1) severe severity; (2) moderate severity; and (3) mild severity. So that $37.50 \%$ of studied samples have been placed in Cluster 1 entitled "severe severity" because of their greatest Euclidean distance from the origin of the coordinate system. In this cluster, an adult case has to meet one or more of the identified criteria, including "Respiratory distress", "Oxygen saturation $\leq 93 \%$ at rest", "Arterial partial pressure of oxygen", and "having chest imaging that showed obvious lesion progression within $24-48 \mathrm{~h}>50 \%$ ". Also, a child case of Cluster 1 can experience specific conditions, including "Tachypnea independent of fever and crying", "Oxygen saturation $\leq 92 \%$ on finger pulse oximeter taken at rest", "Labored breathing, cyanosis, and intermittent apnea," "Lethargy and convulsion", and "Difficulty feeding and signs of dehydration" [49]. Furthermore, the self-organizing map has categorized $18.75 \%$ and $43.75 \%$ of available samples in Cluster 2 entitled "moderate severity" and Cluster 3 entitled "mild severity", respectively [49]. That is to say, if someone has fever and respiratory symptoms with radiological findings of pneumonia, they experience a moderate level of severity. The mild severity label indicates the cases experiencing a mild clinical symptoms level and no sign of pneumonia on imaging. After this stage, these clusters are considered as severity levels and are used as the input of BN and FCM.

## Implementing the proposed approach

This section is categorized into two sections. In "Introduction", the EBP relationships and impact probability of the symptoms are obtained in the independent and combined modes. In "Methodology", the EBP relationships between the symptoms into the triple severity level are extracted, and the FCM is constructed.

## Assessment of scenarios

The collected data set consists of confirmed cases of COVID-19 patients. Data consists of nine symptoms, which are categorized into two sub-levels: (1) symptoms include fever, fatigue, dry cough, dyspnoea, and sore throat; (2) experiencing symptoms includes pains, nasal congestion, rhinorrhoea, and diarrhea. Both levels have a state that indicates none of the mentioned symptoms has been observed in the cases: none symptoms and none experiencing symptoms. Patients are persons between 5 age intervals: [0, 9], [10, 19], [20, 24], [25, 59], and upper 60. However, because age does not categorize as the symptoms of the epidemic and does not affect the decision-making process, it has not been studied in the scenarios.

For executing BN, the Bayesian research and QGeNIe Modeler [55] method have been used. Figure 5 demonstrates the EBP relationships of the COVID-19 symptoms generated by BN from data.

In this phase, symptoms have been analyzed in two modes: (1) independent and (2) combined with different scenarios. Table 1 demonstrates the independent assessment mode based on BN , and probabilities have been extracted for triple severity levels. For illustration, in the symptoms' category, a patient who has experienced fever, with a probability of 0.4243 could be categorized in severe severity. Because fever has a meaningful difference in the probability with the others, it has a key role in distinguishing the severity. On one side, a patient without any symptoms cannot easily classify in the severity levels, because all of the probabilities have a close range ( 0.33 ,

![img-2.jpeg](img-2.jpeg)

Fig. 5 A general overview of COVID-19 symptoms' evidence-based paired relationships

Table 1 Evaluating the impact of disease symptoms on its severity in the independent mode

(probabil-
ity) | Mild (probability)  |
ing symp-
toms | Pains | 0.3615 | 0.2838 | 0.3547  |

$0.33,0.34$ ), and supplementary clinical trials should be considered for the patient to demonstrate the epidemic's severity. This symptom cannot be effective in distinguishing the severity of the epidemic. In other words, although according to the official protocols, it is one of the main symptoms of the disease, it is not appropriate to be used to differentiate the levels of disease severity. This argument is true in the experiencing symptoms' category when the role of rhinorrhoea is analyzed. For this symptom, the probabilities are $(0.3625,0.2799$, and 0.3576$)$ which role of this symptom in separating between severe severity and mild severity is controversial. The role of other symptoms can be analyzed in the same way.

Table 2 presents different scenarios for evaluating the symptoms based on BN. 18 scenarios have been designed to analyze confirmed cases' potential severities. For instance,

Table 2 Evaluating the impact of disease symptoms on its severity in the combined mode


for a patient, if diarrhea symptom appears without any previous symptoms, determining the exact severity of his/ her illness is very difficult, because all of the probabilities are very close to each other: $(0.3306,0.3306$, and 0.3388$)$. However, the probability of considering it as mild severity is more than others. Another scenario with the sore throat and not experiencing symptoms declares that distinguishing the disease's severity again is difficult due to its range: ( 0.3407,0.322 , and 0.3371 ). Again, the probability of classifying this patient on the severe level is more than others. Diagnosing the disease's severity without any previous disease symptoms is very difficult, because COVID-19 has very close mutual symptoms with other infectious diseases. As mentioned before, COVID-19 has some common symptoms (illustrated by CS in Table 2), which demonstrate in the first stages of the disease, and some later symptoms (showed by LS in Table 2) that exhibit themselves in the next stages of the disease. The combination of these symptoms may have a key role in distinguishing the disease. If a patient experiences fever, fatigue, and dry cough, he/she might suffer from severe severity of the disease with a probability of 0.7058 . On one side, if an additional symptom observes in the case, like diarrhea, with the probability of 0.6824 , he/she could experience the severe severity of the epidemic. An important point that should be taken into account is that, according to the independent mode, distinguishing the disease's severity with diarrhea is very difficult due to its close probabilities
( 0.3572 for severe and 0.3531 for mild). Hence, it cannot have an important effect on distinguishing the severity of the disease. The rest of the scenarios in the same way according to the independent scenarios are analyzable.

## Developing BN-based FCM

In this section, according to the clustered data in "Data preprocessing for clustering" section, the EBP relationships between symptoms of triple severities are obtained by BN and Bayesian search algorithm. In conventional FCMs, causal relationships between concepts are defined by human knowledge. However, in this study, EBPs for training FCM are determined automatically by BN. The PSO-STF algorithm has been implemented to train FCM based on the PSO algorithm and S-shaped transfer function. The algorithm achieves the weight of the relations between symptoms by optimizing them. The corresponding weights between algorithms are allowed to assume between $[0,1]$. The maximum number of iterations and population size is set to 400 and 50 , respectively, and the solution with the lowest fitness function has been collected for analysis. Clerc and Kennedy [56] generalized the PSO algorithm model, containing a set of coefficients to control the system's convergence tendencies. Their approach is implemented in this study, and the rest of the PSO parameters are set based on Eq. 6. The constriction coefficients are $\phi_{1}=\phi_{2}=2.05$ and $\Phi=\phi_{1}+\phi_{2}$. The value

of χ is attained based on Eq. 6 and Φ. The inertia weight ω is set to χ. The acceleration coefficients, c_{1} and c_{2}, are obtained as $c_{1}=\phi_{1} \times \chi$ and $c_{2}=\phi_{2} \times \chi$ :
$\chi=\frac{2}{\Phi-2+\sqrt{\Phi^{2}-4 \Phi}}$.
Figures 6, 7, and 8 illustrate the structure of the FCM in triple severities based on the BN and automatic weighting of FCM.

After training FCM and reaching the steady state, the significance of symptoms in the triple severities is obtained. These significant scores are the main factors for separating new cases into the severity levels, and they are discriminators of diagnosing the severity of the disease. In Table 3, the significance of symptoms in the triple severity levels is illustrated and ranked based on their score. Dyspnoea, pains, and rhinorrhoea are the key factors for classifying new cases in severe severity. If a new confirmed case is experiencing dyspnoea, pains, and rhinorrhoea could categorize in severe severity. Sore throat, fever, and none experiencing symptoms cannot classify the patient effectively in severe severity. On one side, pains, fatigue, and dry cough can have a separable role in moderate severity. Those are the key element of classifying the patients in moderate severity. However, sore throat, fever, and none experiencing symptoms cannot discriminate symptoms in moderate severity. By analyzing none experiencing symptoms, sore throat, and diarrhea, which have the highest score in mild severity can classify new confirmed cases into mild severity. These symptoms have the highest priority in categorizing confirmed cases in mild severity. On the other hand, fever, non-symptoms, and nasal congestion cannot be counted as discriminator factors to classify mild severity cases.

This study seeks the key symptoms of the disease, which can distinguish the severity of the COVID-19. However, based on the results, it does not necessarily mean that the epidemic's most common symptoms have this characteristic. This self-assessment DSS can consider the EBP relationships that human and normal data cannot infer. In other words, without considering the relations between attributes, the key symptoms cannot be inferrable.

## Conclusion

Based on the WHO report, COVID-19 is a global outbreak that threatens all human beings' lives on Earth. In the meantime, diagnosing the COVID-19 based on considerable errors of the main available methods, such as RT-PCR, has remained challenging to scientists. Due to the rapid spread of disease throughout the world, using a framework to categorize newly confirmed patients can help organize them effectively. This research aims to propose a
![img-3.jpeg](img-3.jpeg)

Fig. 6 An overview of FCM and weights of EBP relationships inferred between symptoms for severe level

![img-4.jpeg](img-4.jpeg)

Fig. 7 An overview of FCM and weights of EBP relationships inferred between symptoms for the moderate level
![img-5.jpeg](img-5.jpeg)

Fig. 8 An overview of FCM and weights of EBP relationships inferred between symptoms for the mild level

Table 3 The significance of symptoms for classifying confirmed cases into triple severities


self-assessment DSS to help classify new confirmed cases into triple severe severity. For this purpose, a dataset has been collected from confirmed cases, and they are analyzed as the whole and in the triple severity levels. For clustering data into severity levels, the self-organizing map method has been implemented. Then, BN is utilized for extracting EBP relationships between symptoms and their impact probability for analyzing scenarios and extracting EBP relationships inside the levels to develop FCM. Based on the defined scenarios, in the first phase of the research, the probability of the triple levels' symptoms should have a reasonable interval for distinguishing the epidemic level. Without that, classifying the severities cannot reliably possible. Moreover, defining scenarios based on the combination of the symptoms can effectively impact the distinguishing levels. After developing FCM and reaching the steady state, the significance of symptoms is ranked based on their scores to study their potential in distinguishing the severity of the disease. Symptoms with higher scores have a key role in classifying the patients in the triple severity levels. Based on these scores, dyspnoea, pains, and rhinorrhoea have the main role in distinguishing severe severity. In the moderate severity, pains, fatigue, and dry cough can make the distinction between severities. Finally, for mild severity, none experiencing symptoms, sore throat, and diarrhea are considered as the key symptoms for distinguishing between severities of the COVID-19. The proposed self-assessment DSS can consider the EBP relationships between symptoms that cannot be inferable for humans. Results show that the common symptoms are not necessarily the key factors for distinguishing between severities, and relations between symptoms should be taken into account for analyzing them.

For future studies, it is suggested that to consider some of the disease's new symptoms for analyzing their severity. Also, it is possible to utilize linguistic terms for reporting the severity of the symptoms and converting them to fuzzy numbers for conserving the accuracy of the information. It is worth suggesting that the proposed approach can be developed as an online application to enrich continuously with new and comprehensive data.

## Declarations

Conflict of interest The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

Ethical approval This article does not contain any studies with human participants or animals performed by any of the authors.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.
