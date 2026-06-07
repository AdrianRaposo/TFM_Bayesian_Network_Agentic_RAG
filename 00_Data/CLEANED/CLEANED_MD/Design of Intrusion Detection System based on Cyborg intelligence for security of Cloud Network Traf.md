# Design of Intrusion Detection System based on Cyborg intelligence for security of Cloud Network Traffic of Smart Cities 

Edeh Michael Onyema ${ }^{1}$, Surjeet Dalal ${ }^{2 *}$, Carlos Andrés Tavera Romero ${ }^{3}$ (D) Bijeta Seth ${ }^{4}$, Praise Young ${ }^{5}$ and Mohd Anas Wajid ${ }^{6}$


#### Abstract

The Internet of things (IoT) is an important technology that is highly beneficial in establishing smart items, connections and cities. However, there are worries regarding security and privacy vulnerabilities in loT in which some emerge from numerous sources, including cyberattacks, unsecured networks, data, connections or communication. This paper provides an ensemble intrusion strategy based on Cyborg Intelligence (machine learning and biological intelligence) framework to boost security of loT enabled networks utilized for network traffic of smart cities. To do this, multiple algorithms such Random Forest, Bayesian network (BN), C5.0, CART and Artificial Neural Network were investigated to determine their usefulness in identifying threats and attacks-botnets in loT networks based on cyborg intelligence using the KDDcup99 dataset. The results reveal that the AdaBoost ensemble learning based on Cyborg Intelligence Intrusion Detection framework facilitates dissimilar network characteristics with the capacity to swiftly identify different botnet assaults efficiently. The suggested framework has obtained good accuracy, detection rate and a decreased false positive rate in comparison to other standard methodologies. The conclusion of this study would be a valuable complement to the efforts toward protecting loT-powered networks and the accomplishment of safer smart cities.


Keywords: Cyborg, Ensemble learning, loT, Network Intrusion Detection System (NIDS), Cloud Computing

## Introduction

Technology is fast penetrating every sector of human life, including where we live and how we work or share things with people and organization [1]. Smart cities are becoming more common as a result of a rise in global urbanization. Infrastructure and amenities are needed to balance with ecological and transportation challenges as the population grows in metropolitan areas. Smart cities are evolving as a solution to the aforementioned difficulties [2]. Developing a wide range of smart city applications has become increasingly dependent on the rapid growth

[^0]and expansion of low-cost devices and other IoT-oriented infrastructure, which have been integrated with wireless communication technology [3]. Figure 1 shows variety of useful municipal services such as advanced public transit and health care, advanced construction, as well as innovative manufacturing and waste management.

The Internet of Things (IoT) is a key component of smart city technology. The Internet of Things refers to the interconnection of computer devices (smart items) via the Internet [4]. Using a variety of physical sensors and wireless networks, data is collected and analyzed in near-real time in the Internet of Things (IoT). Actuators are controlled and processed by the data collected by sensors [5]. As an outcome, the expansion of IoT infrastructure in smart cities will require the assurance of critical characteristics such security, secrecy, trust, scalability, and centralization [6]. IoT systems are more scattered and diverse than traditional systems. With the unique qualities [7] of IoT like memory competency and computing capacity, network bandwidth as well as long-lasting battery life, securing, protecting, and trusting IoT has become more difficult. The interconnectedness of various IoT sensors in smart networks that target IoT devices in smart cities introduces a multitude of possible risks. Smart cities are vulnerable to both physical and cyber threats. To initiate physical assaults, hackers must be in close proximity to equipment and be able to alter/tamper with the network's hardware and software [8].

It's becoming increasingly difficult to manage the security of data particularly that of IoT devices [2]. At present, the most popular method of storing data is via the cloud. The cloud servers have powerful computational and storage resources. Clients of the cloud store their files on cloud servers, pay only for what they use, and have access to a global network of computers and servers from anywhere in the world. However, as illustrated in Fig. 1, storing data in the cloud for smart cities might be wasteful and unreliable. There are several limitations of uploading data to the cloud. Substantial time delays can occur by uploading data from IoT devices to cloud servers, data integrity may be hindered, and the loss of control over the data can occur if the local backup is deleted.

A number of challenges relating to data privacy and security exist in smart city environments, putting at risk the proper operation of smart devices and degrading the use of their services. In addition, the images and videos that can be accessed in a smart city and the information collected in smart houses may show the level of life of the customers. The ethical difficulties are the root cause of these problems. Residents' safety might be jeopardized by malicious attackers using this information. People's personal information, such as photographs, videos, and other media, might be exposed as a result. In addition, malicious attackers may be able to identify the normal behavior of people (such as their departure or arrival times) that might have an impact on the citizens' lives through data mining studies. As a result, adequate safeguards against privacy and security concerns are essential to prevent citizens from rejecting smart cities [9].

To maintain the safety and privacy of the smart cities, the acquired data should be protected from unauthorized access. A smart city collects and analyses data about its residents' well-being and the environment in which they live, and then uses that data to augment the standard of their daily lives. Consequently, safety and confidentiality

issues might be considered hurdles to the smart city's degree of maturity. One of the most pressing concerns is the security of personal information and the dependability of data storage and processing.

Motivation and key challenges:
Although it isn't unexpected, there has been a lot of study done on how to protect data from cyberattacks. In support of the growth of sustainable smart cities, there are, nevertheless, a number of issues that must be addressed. Here are some of the motivational behind this research work:

1. To address the research gaps in network intrusion detection process in connected devices of Smart cities and analyze them carefully.
2. To develop a more accurate and efficient network intrusion detection mechanism for smart cities.
3. To design the above cited mechanism in context of Cyborg intelligence for getting benefits of both human and machine intelligence.
4. To implement proposed mechanism of particular dataset for judging the performance of this mechanism.
5. To assess the performance of existing machine learning algorithms in network intrusion detection.

To tackle the smart city challenges, this search paper propose a new AdaCyborg (AdaBoost ensemble learning method based on Cyborg Intelligence) Intrusion Detection for smart cities.

## Overview and literature survey

This segment includes schemes used in IoT-driven smart cities and its networks and latest investigation allied to threat detection, challenges of threat detection, covering known and unknown threats, and anomaly detection system, and several machine learning algorithms.

How does threat detection differ from threat protection?

Threat detection is the repeatable process conducted in near real time, or retroactively, in order to detect and respond to adversary actions or toolsets, typically detected through conventional security controls. It is a process which is often technology, or analyst-driven, and which combines security tools, analysis, and experience.

While these two terms are sometimes used interchangeably, the reality is that they are fundamentally different. Threat protection is typically signature-based, and is designed to alert based on Indicators Of Compromise (IOCs) of malware or tools. These artefacts, typically aligning to the lower levels of Dave Bianco's Pyramid of Pain, could include things such as IP addresses, domain names, hash values, and textual strings in a file. These
elements can be used for alerting, but they are "fragile" and signatures using them can break without notice if an attacker modifies their tools or changes their infrastructure, leading organizations to have a false sense of security.

Threat detection, however, aligns more to the upper levels of the Pyramid, and includes more complicated elements of malware and tools. This could include specific behaviors of malware or tools on the system or network as they attempt to establish persistence, exploit specific vulnerabilities, or communicate with their command and control (C2) servers. Detecting on these elements is more reliable, and it takes significantly more effort for adversaries to evade detection [8].

Challenges of threat detection
To be successful, threat detection should be done in real-time. However, there are many challenges that are associated with to-the-second detection. Analysts are overburdened by alerts from abundant security tools. Collecting hundreds of log types and analyzing them, even when using more sophisticated techniques including machine learning and behavioral analysis, is unsustainable for the majority of organizations. Even more so, logs lack content and context, making it difficult to parse out true threats. Though once a threat is detected, logs can help SOC teams quickly map timelines and provide analysis of the threat event:

- Best endpoint log sources for threat hunting
- Best network log sources for threat hunting

Known vs. unknown threats
To protect our environments, speed is critical. Security programs that detect threats quickly and efficiently are able to reduce the overall risk to the organization. Ideally, an organization's defense program can stop the majority of threats because the malicious acts have been spotted in the wild and their signature data in traditional threat protection platforms has been recorded-and the organization has details on how to mitigate the attack. Even still, some of these threats can slip through defensive measures, which is why SOCs should have analysts with hands on keyboards looking for threats [10]. The flip side of the coin is that the threat landscape is constantly changing and introducing new, unknown threats that have not yet been detected. To detect both known and unknown threats, defenders should use a variety of methods, including:

- Threat Intelligence: Effective threat intelligence is actionable, and consistently shares the traits of contextualization, evaluation, prioritization, customization and decomposition. Often, security programs

focus too much on the quantity of threat intelligence, instead of the more important "quality" of the intelligence. Threat intelligence lessens the overall danger to organizations, their members and clients as comparable to rapid threat detection and response.

- Threat Hunting: Unlike other forms of threat detection, threat hunting is a proactive process that identifies the presence of malicious actors and their tools before an attack.

Disconnected security tools and the problem with after-the-fact

Threat detection and response is more difficult than years ago because there are number of disconnected point tools for analysts to use. However, the effectiveness of these tools is limited because each tool must be deployed, configured, and operated daily. The analysts have to work for endpoint security, network security tools, cyber threat intelligence, malware and adversaries in the network [11].

The after-the-fact detection is a problem because it generally does not happen within minutes of an attack. Only $22 \%$ detect breaches in less than one day. And when there are low detection rates, there are much longer business impacts.

## Related work

Almeida et al. [10] managed a basic presentation investigation of an Internet of Things mindful Ambient Assisted Living (AAL) framework for older observing. The examination was centered around three fundamental framework parts: (I) the far reaching information catching layer, (ii) the Cloud- based unified information the executives vault, and (iii) the gamble investigation and expectation module. Every module could give different working modes, subsequently the basic examination targets characterizing which were the best arrangements as indicated by setting's necessities.

Moustafa et al. [12] proposed a gathering interruption location strategy to alleviate noxious occasions, specifically botnet assaults used in IoT organizations. In light of an investigation of their potential qualities, new factual stream highlights were derived from conventions. This was followed by the creation of an AdaBoost group learning approach that used three AI methods to analyze the influence of these aspects and differentiate malignant events. It had been determined by using the correlation and association coefficient measurements that the suggested highlights have the potential properties of either normal or noxious activity. In addition, the suggested collection approach had a greater recognition rate and a lower rate of false positives compared to the system and three other best-in-class grouping techniques.

Using the IoT/Fog/Cloud standards, miniature administrations, and DevOps foundations, Iasio et al. [11] presented the reference engineering, a model execution, and a city scale contextual investigation assessment of PROMENADE, a stage that ensured continuous improvement of strong and solid applications for ongoing checking and examination of traffic information produced by IoT gadgets in enormous intelligent urban areas. Based on on-line traffic circumstances, the model was evaluated for a scenario study on the semi-continuous detection of street network flaws using centrality measures derived from unconnected real datasets available for Lyon, France.

Using a sophisticated nonparametric Bayesian model, Makkar [13] proposed to create a discovery model for both known and obscure interruptions (or irregularity location). Our system's design might be expanded to meet the needs of IoT innovation as well as impressively smart city online applications. They used a Bayesianbased MCMC induction for infinitely limited summed up Gaussian blend models to familiarize ourselves with the examples of the exercises (typical and atypical). In spite of exemplary grouping techniques, our methodology did not have to indicate the quantity of bunches, thinks about the vulnerability through the presentation of earlier information for the boundaries of the model, and allows to tackle issues connected with over-and under-fitting. To get better grouping execution, include loads, model's boundaries, and the quantity of bunches were assessed at the same time and consequently. The created approach was assessed utilizing famous informational indexes. The acquired outcomes showed the proficiency of our methodology in recognizing different assaults.

Insightful electronic devices (IEDs) with built-in communicated interruption location frameworks had been proposed by Hong et al. [7]. For example, tested values and conventional items located in substations, the suggested IEDs could screen for and detect anomalies and weird ways of acting in the host arrangement of IED and IEC 61,850-based messages. As a group, the suggested IEDs aimed to pinpoint the start of digital attacks by coordinating with adjacent IEDs. Using the item inserted framework, the suggested interruption discovery framework was tested using IEDs' power framework insurance features. Overcurrent and distance protections on the installed board could be reliably and effectively mitigated by the provided moderation approaches.

The Trustworthy Privacy-Preserving Secured Framework (TP2SF) was developed by Kumar et al. [9] for smart urban communities. An interruption location module, a reliability module, and two-level security are all included in this system. Address-based blockchain renown will be implemented in the reliability module. Two-level security

uses a blockchain-based upgraded Proof of Work (ePoW) approach and Principal Component investigation (PCA) to transform information into a reduced form to prevent derivation and damaging attacks. An improved inclination tree support framework (XGBoost) was provided in the interruption locating module. Final results of the FogCloud design have led us to provide a blockchain-IPFS coordinated basis for the Fog-Cloud, notably CloudBlock and Fogblock, to express the suggested TP2SF system in the shining city. Both in non-blockchain and blockchain settings, the findings demonstrated the superiority of TP2SF structure over other cutting-edge approaches.

It had been developed by Bhayo et al. [14] to identify DDoS attacks based on the counter advantages of various organizational boundaries. C-DAD was a flexible and adaptable system that had been thoroughly tested across a wide range of organizational boundaries. The SDNenhanced findings were clearly seen in the computation. Aside from that, the proposed design distinguished the assault in a shorter amount of time and with less strain on the computer's processor and memory.

Guo et al. [15] proposed an AI based strategy that can distinguish explicit weak IoT gadget models associated behind a homegrown NAT, in this way recognizing home organizations that represented a gamble to the telcos framework and administration accessibility. To assess our strategy, they gathered a huge amount of organization traffic information from different business IoT gadgets in our lab and thought about a few grouping calculations. We discovered that our stream-based method is powerful and can cope with situations where previous NATdetection strategies fail, such as scrambled, non-TCP or non-DNS traffic, which can't be properly addressed by existing NAT-detection strategies. We've made our original marked benchmark dataset available for others to use in their research.

Nie et al. [16] utilized head part investigation (PCA) for include decrease and group based classifiers are utilized to foresee interruption assaults on the organizations. KDDCup-'99' dataset has been utilized and execution is assessed as far as exactness, accuracy, review and F-score. Nonetheless, in the shrewd medical care climate, IoMT gadgets face high weakness. Network safety was a fundamental part of a shrewd city that could accomplish a protected climate for savvy medical services. Accordingly, the Intrusion Detection System (IDS) was utilized as a security layer of correspondence towards online protection for the most recent gadgets and organizations frameworks.

Elsaeidy et al. [17] fostered a profound learning-based model for replay assault recognition in savvy urban communities. This model's performance was evaluated by comparing it to a real-world Smart City dataset, where attacks were re-enacted and replayed. According to their findings, the suggested model had the ability to accurately identify both normal and threatening ways of acting. In addition, the results showed that the suggested model outperformed both traditional order and deep learning methods. A real smart city informative indexed with imitated replay assaults was also included as an added commitment for future study.

Lee et al. [18] used Gated Recurrent Unit cells to uncover correlations between time series information, and used Gaussian Mixture priors in inactive space to depict multimodal information. The inability to fully capture information designs had been caused by previous efforts expecting simple conveyances for Gaussian Mixture priors. With the help of the Bayesian Inference Criterion (BIC), they proposed a model selection instrument throughout the preparation cycle to observe the model that can accurately measure conveyance in Gaussian Mixture (GM) space. On four datasets, they conducted extensive replications and discovered that our suggested plot outperforms cutting-edge peculiarity identification algorithms, improving F1scores by up to 47.88 percent. An information-driven IDS was being planned by Ahmad et al. [5] by researching the RSU's connection load methods of acting in the IoV against various attacks that caused traffic streams to vacillate. Convolutional Neural Network (CNN) was being used to separate the components of connection stacks and pinpoint the point of interruption centered on RSUs. As a result of the backpropagationcomputation, the suggested engineering was made up of a standard CNN and a simple blunder term. In the meantime, the proposed CNN-based profound designwas provided a hypothetical investigation by the probabilistic portrayal. IoT devices may be protected by using ML to identify spam, according to Seth et al. [18]. Spam Detection in IoT using Machine Learning system was presented to achieve this purpose. Five machine learning models were evaluated in this system using a wide range of measurements and data highlighting sets from a wide range of information sources. The enhanced information highlights are taken into consideration by each model when registering a spam score. The reliability of an IoT device may be measured by this score. The REFIT Smart Home dataset is used to provide the go-ahead to a new strategic plan. When compared to alternative options, the proposed scheme is more viable, according to the results obtained.

A Privacy Preserving and Secure Framework (PPSF) for IoT-driven brilliant cities is presented by Kumar et al. [3]. The PPSF relied on a two-level protection conspiracy and an interruption identification plan as the foundations of its design. Two-level protection begins with a blockchain module and Principal Component Analysis (PCA)

employed to transform unrefined IoT data into a more manageable form. Two IoT network datasets, namely ToN-IoT and BoT-IoT, were analyzed using a GradientBoosting Anomaly Detector (GBAD) in the interruption location plot to prepare and evaluate the suggested two-level protection conspiracy. To deliver the suggested PPSF structure, we also advocated an IPFS-integrated Fog- Cloud blockchain architecture. Exploratory outcomes showed the predominance of the PPSF structure over a few late methodologies in blockchain and nonblockchain frameworks.

Wan et al. [19] fostered an IoT traffic estimation structure on programmable and smart edge switches to consequently gather approaching, active, and inward organization traffic of IoT gadgets in edge organizations, and to fabricate multi-faceted social profiles which portray who, when, what, and why on the personal conduct standards of IoT gadgets in light of persistently gathered traffic information.

Shahraki et al. [20] surveyed the information stream handling instruments and structures that could be utilized to handle such information on the web or on-the-fly alongside their upsides and downsides, and their integrality with de truth information handling systems. To investigate the presentation of OL procedures, we lead an experimental assessment on the exhibition of various gathering and tree-based calculations for network traffic characterization. At last, the open issues and the future headings in investigating traffic information streams were introduced. This specialized review presented important bits of knowledge and standpoint for the organization research local area while managing the necessities and motivations behind web-based information streams examination and learning in the systems administration space.

Ahmed et al. [8] proposed a heap adjusting calculation to plan sensor information, vehicles and server farms performing assignments. They likewise offered a bundle level interruption recognition model. The outcomes demonstrated the way that the created model could further develop the choice limit by utilizing a pooling procedure and an entropy vulnerability measure. Table 1 summarizes the recent work done in this problem domain.

## Materials and methods

## Dataset

The research work has taken KDDCUP'99 data set for experimental work. It is most commonly used data sets available for network-based inconsistency detection systems. This dataset has 42 columns of various data types.

## Overview of Methods involved and algorithms chosen

Below is an outline of involved algorithms and steps.

## Data Pre-processing

Data collected from varied sources collected in a raw format need to be converted before analysis. Data preprocessing or data cleaning refers to the process used to transform raw data into a clean data set. It is an essential step in machine learning because it is said that "Better data beats fancier algorithms".

## Missing values

Different cleaning methods are required for different types of data. Missing data needs to be handled carefully in machine learning as they can be relevant. The missing data can be handled in two ways but may result in suboptimal information:

Table 1 Related Work Summery


- Dropping observations with missing values: It is sub-optimal as dropping observations may lead to drop information which may be informative.
- Imputing the missing values from past observations: It is sub-optimal and may lead to loss of information as the value was originally missing but we filled it in.

Outliers data Outliers are the values which look different from the other values in the data. They may occur because of a faulty sensor or an error in data entry and any natural discrepancy like wrong input of salaries. Outliers can create problems during model fitting or inflate the error metrics.

## Random forest for classification

Random forest, given by Tin Kam Ho in 1995, is a supervised machine learning algorithm employed for classification and regression problems. It builds decision trees on various samples and the majority vote for performing classification and average vote in case of regression.
For instance, checking an email is spam or not [21-25]. It uses random subspace method. An extension of algorithm was developed by Leo Breiman and Adda Cutter in 2006 using "Bagging" idea. It is depicted in Fig. 2.

RF model has following advantages as given below:

1. Bagging algorithm and Ensemble learning approach are the main advantages. On the data subset, it produces as many trees as possible and assembles their results. Overfitting and variance may be reduced using this method. As a result, it enhances accuracy.
2. Classification and regression issues are both addressed by this technique.
3. It is able to handle both categorical and continuous variables.
4. Missing values can be handled automatically.
5. Because it relies on a rule-based method rather than distance calculations, no standardization or normalization, i.e. feature scaling, is necessary.
6. Non-linear parameters may be handled well using this tool.
![img-1.jpeg](img-1.jpeg)

7. It is incredibly stable and has a low influence on the surrounding environment.

Table 2 shows the decision rules used for attack. Disadvantages 1. The algorithm increases the overall complexity as compared to decision trees due to high computational power and resources. 2. Longer training period is required as it produces many trees versus a single tree in case of decision tree.

## C5.0

A C5.0 model divides the sample into subsets based on the most informative field. Ross Quinlan was the brains behind it. The procedure repeats itself until the subsamples can no longer be divided further, at which point the process ends [26-29]. Figure 3 shows the specifics. Models of two distinct types may be generated using C5.0:

- Decision tree: This tree can only make one prediction based on a single piece of data.
- Rule set: Because they are based on decision trees, they have simpler mathematical models.



Figure 3 highlights the predicator importance in C5.0 model. It has following advantages as given below:

- C5.0 is quite robust in case of missing data and large numbers of input files. They don't require long training times to estimate.
- C5.0 is easy to understand as the rules derived from the model have straightforward interpretation.

### *Neural network*

A mathematical or computer model based on biological neural networks is known as an artificial neural network (ANN). It utilizes a connectionist approach to computation and is made up of a network of artificial neurons. Nodes and weighted edges are the building blocks of a neural network [30–32]. Recurrent and feed forward neural networks can be distinguished in general. Figure 4 depicts its specifications.

It has following advantages as given below:

1. Ability to train machines: In artificial neural networks, comparable events are used to learn and make judgments.
2. Parallel processing ability: An artificial neural network's numerical strength enables it to simultaneously accomplish a variety of tasks.

Figure 5 demonstrates the neural network design. It has some limitations also. Neural Networks employ "black box" nature which result in greater computational burden, proneness to overfitting, and the empirical nature of model development.

### *CART*

Gini's impurity index serves as the splitting criteria in the Classification and Regression Trees algorithm, which is a classification procedure for creating a decision tree. Leo

![img-3.jpeg](img-3.jpeg)

![img-4.jpeg](img-4.jpeg)

Braiman used the term "decision tree" to describe the method. Machine learning makes use of a type of predictive model that describes how the values of target variables may be predicted from the values of other variables. Forks in the CART output are separated into predictor variables, and each node in the end is given a predicted value. It is depicted in Fig. 6.

Advantages of CART

- However, unlike CHAID, CART always creates binary splits.
- Because CHAID constructs segments/deciles of continuous variables that are often arbitrary in nature and can sometimes mask the underlying patterns in the continuous variables, CART can test many more cut points than CHAID when dealing with continuous data.
- In comparison to CHAID, CART has a significantly smaller tree structure.
- Unlike CHAID, which naturally generates broad trees, CART develops tall and narrow trees.

Disadvantages of CART are that it is computationally expensive and slow in nature.

## CHAID

CHAID represents Chi_Square Automatic Interaction Detector. It is the oldest decision tree algorithm in history. CART and CHAID both use tree-like structures
to represent data, but they differ in their efforts to limit the development of the trees in the models. GordanKass invented it in 1980 and is used to uncover the correlations between variables in a statistical model CART is more commonly used for forecasting than CHAID for descriptive analysis. Figure 7 provides information about CHAID.

Advantages:
CHAID algorithm effectively generates multi-way frequency tables. It has been used in marketing research.

## Bayesian network

A supervised learning method based on the Bayes theorem, the nave Bayes algorithm is used to solve classification issues. Judea Pearl created the term "Bayesian network" in 1985. Text categorization using a large, multi-dimensional training set makes extensive use of this technique. Nodes in Bayesian networks represent variables in the Bayesian senseTheyare directed acyclic graphs (DAGs). Figure 8 explains this. Figure 9 depicts Bayesian Networks' conditioned probabilities.

Advantages:

1. It provides a way of combining prior information with data.
2. It provides interpretable answers.
3. It gives a convenient setting for a large number of models.

![img-5.jpeg](img-5.jpeg)

![img-6.jpeg](img-6.jpeg)

Figure 9 highlights the Condition Probabilities for Bayesian Network. It has following disadvantages as given below:

- There is no method to choose a prior.
- It often comes with a high computational cost.


## Proposed AdaCyborg intrusion detection technique

Cyborg intelligence is a new research paradigm that strives to blend the best of both biological and machine intelligence. For example, we can then compare the cyborg model's behavior to that driven by each of the two mechanisms on their own to see whether there are any similarities or differences in the model's behavior. The biological and computer portions are tightly intertwined.

Collaborations represents a long term integrated process which occurs when organizations interact formally and informally.Gray described collaboration
as "a process through which parties who seedifferent aspects of a problem can constructively explore their differences and searchfor solutions that go beyond their own limited vision of what is possible". According to brain computer integration requirements, a motivation could berepresented as a 3-tuples $\{\mathrm{N}, \mathrm{G}, \mathrm{I}\}$, where N means needs, G is goal, I means themotivation intensity [13].

There are three kinds of needs in the Cyborg system:

- Perception needs: Acquire environment information through vision, audition, touch, taste, and smell.
- Adaptation needs: Adapt environment condition and optimize impaction of action taken.
- Cooperation needs: Promise to reward a cooperation action between brain and machine.

A motivation is activated by motivational rules which structure has following format:

![img-7.jpeg](img-7.jpeg)

# Conditional Probabilities of duration 


Fig. 9 Condition Probabilities for Bayesian Network

$$R = (P, D, \text{Strength}(P|D))$$

where, P indicates the conditions of rule activation; D is a set of actions for the motivation; Strength(P|D) is a value within interval [0,1]. Based on the Adaboost approach, a network intrusion detection system is proposed in this research.

The proposed algorithm has the following steps as given below:

Step 1—First of all network connection vector will be assigned some weights. Initially, all the weights will be equal. It helps to define Perception needs of proposed system.

Step 2—To select the important features among these network traffic attributes, the correlation coefficient has been applied in this step. This step belongs to Feature selection and defines Adaptation needs.

Step 3—Next the decision stump has been created for each feature with respect to target classes. It describes the Cooperation needs.

Step 4—Next stage, the classification is done based on motivational rules which is based on conditions of rule activation and Strength.

Step 5—Final decision will be decided on outcome of step 4.

Step 6—Exit

An outline of the proposed work is shown in a flowchart below in Fig. 10.

The first step is to choose features from the KDD95 dataset, which contains a pool of features. For this purpose, we perform a correlation analysis. We eliminate those features that are substantially connected with each other from the results of the inquiry. Classifying network traffic as benign or dangerous is also covered in this study.

![img-8.jpeg](img-8.jpeg)

## Experimental results and discussion

The AdaCyborg (Cyborg Intelligence based ensemble model) is implemented in Python by utilizing package AdaBoost Scikit-Learn API for building decision tree base learners. The proposed system was applied to KDDCUP'99 data set. A large number of experiments were implemented using varied parameter settings detailed in the next sections.

## Machine learning algorithms in network intrusion detection

In the first phase, we implemented various machine learning algorithms discussed above to detect the network attacks. This section provides the accuracy level maintained in them individually.

Figure 11 demonstrated the accuracy level in Random Forest model. It has secured $84.29 \%$ accuracy on given dataset.

Figure 12 demonstrated the accuracy level in C 5.0 model. It has secured $83.94 \%$ accuracy on given dataset.

Figure 13 demonstrated the accuracy level in CART model. It has secured $99.43 \%$ accuracy on given dataset.

Figure 14 demonstrated the accuracy level in CHAID model. It has secured $76.91 \%$ accuracy on given dataset.

Figure 15 demonstrated the accuracy level in Bayesian Networkmodel. It has secured $95.84 \%$ accuracy on given dataset.

Figure 16 demonstrated the accuracy level in Bayesian Network model. It has secured $98.24 \%$ accuracy on given dataset.

## Proposed AdaCyborg model in network intrusion detection

Figure 17 demonstrated the accuracy level in the proposed AdaCyborg model. It has secured 99.43\% accuracy on given dataset.

As demonstrated in the simulations, the suggested technique has an excellent detection rate and low false positive rate. Table 3 highlights the comparison of accuracy of proposed model with existing works.

Additionally, AdaCyborg's detection time is short, demonstrating its efficiency. The Fig. 18 demonstrates the results graphically for better understanding.

Security both in the cloud and IoT would remain an important factor in achieving smart city and in maximizing the potentials of IoT - powered solutions [38-41].

## Complexity

Complexity is calculated in terms of space and time. Time complexity is the computational complexity that


Coincidence Matrix for R-attack (rows show actuals) Confidence Values Report for RC-attack


User Defined Score for R-attack


Fig. 11 Accuracy level in Random Forest model

Results for output field attack $\square$ Comparing R-attack with attack


Fig. 12 Accuracy level in C 5.0 model

Results for output field attack $\square$ Comparing R-attack with attack


Fig. 13 Accuracy level in CART model describes the amount of time it takes to run an algorithm. It is estimated by counting the number of elementary operations performed by the algorithm, supposing that each elementary operation takes a fixed amount of time to perform. Thus, the amount of time taken and the number of elementary operations performed by the algorithm

Results for output field attack $\square$ Comparing R-attack with attack


Confidence Values Report for RC-attack


$\square$ User Defined Score for R-attack


Fig. 14 Accuracy level in CHAID model

Results for output field attack $\square$ Comparing B-attack with attack


Confidence Values Report for BP-attack


$\square$ User Defined Score for B-attack


Fig. 15 accuracy level in Bayesian Network model

Results for output field attack $\square$ Comparing N-attack with attack


Confidence Values Report for NC-attack


$\square$ User Defined Score for N-attack


Fig. 16 accuracy level in Neural Network model

Results for output field attack $\square$ Comparing C-attack with attack


Confidence Values Report for CC-attack


$\square$ User Defined Score for C-attack


Fig. 17 accuracy level in Proposed AdaCybrog model

Table 3 Results comparison with existing works


is taken to differ by at most a constant factor. Space complexity is a measure of the amount of working storage an algorithm needs. Computational Complexity of Adaboost is estimated using following:

- Train time complexity: $\mathrm{O}\left(\mathrm{n}^{*} \mathrm{p}^{*} \mathrm{n}\right.$ trees)
- Test time complexity: $\mathrm{O}\left(\mathrm{p}^{*} \mathrm{n}\right.$ trees $)$

Here n denotes the data points in the dataset, p the number of features and n_trees suggest the number of estimators we are using in our model.

While training the model we are going through n variables for p features to find out the decision stump, and then calculate their loss function and to update the weights in this way we are taking $\mathrm{O}\left(\mathrm{n}^{*} \mathrm{p}\right)$ operations. Now the same is repeated for n_trees number of estimators so it takes $\mathrm{O}\left(\mathrm{n}^{*} \mathrm{p}^{*} \mathrm{n}\right.$ trees) operations.

The study inferred that security issues in the cloud have persisted but the proposed technique offers a good opportunity to enhance the security measures in Cloud Network Traffic of Smart Cities. The presented model in this study can help halt malicious goals in Cloud Network traffic. The system could be very effective in protecting users' privacy and the integrity of resources within the network. The study proved that vulnerability of cloud networks can be reduced using instruction detection system particularly as it relates to cyborg intelligence.

## Conclusions and future work

Intrusion detection is an important and challenging problem that has a major impact on quality and reliability of smart city services. To this extent, botnet attack has been one of the most common threats on smart city infrastructure. The biological brain and machine learning algorithms must operate together in order for this integration to be successful and co-adaptive. Experiment results show that accuracy measurements may be used to detect both normal and malicious behavior. We have chosen AdaBoost algorithm as it involves very short (one-level) decision trees. The weak learners are added sequentially to the ensemble. Each subsequent model attempts to correct the prediction made earlier by the model. This is achieved by weighing the training dataset to put more focus on training examples on which prior models made prediction errors. A budding notion, Cyborg intelligence, utilizes the best traits of both machine and biological intelligences have shown to have a significant influence on Network Intrusion Detection. According to the results, our proposed AdaBoost ensemble learning based on Cyborg Intelligence Intrusion Detection framework outperforms traditional classification and deep learning models. For future work, we want to develop a prototype of the algorithm in a real-world context, potentially inside a tight network of connected computers. This will allow us to more effectively evaluate its real-world utility.

# Accuracy

![img-9.jpeg](img-9.jpeg)

Fig. 18 Results comparison

## Acknowledgements

Not applicable.

## Authors' contributions

Edeh Michael Onyema: Results and analysis. Surjeet Dalal: Design, methods, submission and corresponding author. Carlos Andrés Tavera Romero: Conceptualization, Discussion and review of the final draft. Bijeta Seth: Introduction and background. Praise Young: Conclusion and background. Mohd Anas Wajid: Conclusion and review of the first draft. The author(s) read and approved the final manuscript.

## Funding

This research was funded by Dirección General de Investigaciones of Universidad Santiago de Cali under call No. 01-2022.

## Availability of data and materials

The supporting data may be provided by corresponding author on request.

## Declarations

## Ethics approval and consent to participate

There is no ethical approval required and authors express their consent to participate for paper which is a health care based on Blockchain and Privacy Computing.

## Consent for publication

Authors provide the consent for publication which is a health care based on Blockchain and Privacy Computing.

## Competing interests

The authors declare that they have no competing interests.

## Author details

${ }^{1}$ Department of Mathematics and Computer Science, Coal City University, Enugu, Nigeria. ${ }^{2}$ College of Computing Science and IT, Teerthanker Mahayeer University, Moradabad Uttar Pradesh, India. ${ }^{3}$ COMBA R\&D Laboratory, Faculty of Engineering, Universidad Santiago de Cali, 760000 Cali, Colombia. ${ }^{4}$ Department of Computer Science and Engineering, B. M. Institute of Engineering \& Technology, Sonipat, Haryana, India. ${ }^{5}$ Department of Linguistic Data Sciences, University of Eastern Finland, 80101 Joesuu, Finland. ${ }^{6}$ Department of Computer Science, Aligarh Muslim University, Aligarh 202002, India.

## Received: 21 May 2022 Accepted: 29 July 2022 Published online: 13 August 2022

## Publisher's Note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## Submit your manuscript to a SpringerOpen ${ }^{\circledR}$ journal and benefit from:

- Convenient online submission
- Rigorous peer review
- Open access: articles freely available online
- High visibility within the field
- Retaining the copyright to your article

Submit your next manuscript at $\boldsymbol{\sim}$ springeropen.com